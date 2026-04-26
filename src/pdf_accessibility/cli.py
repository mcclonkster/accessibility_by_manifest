from __future__ import annotations

import json
from pathlib import Path
import shutil
import sys
from enum import Enum

import typer

from accessibility_by_manifest.util.logging import get_logger
from pdf_accessibility.graph.build_graph import build_workflow, langgraph_available
from pdf_accessibility.persistence.artifacts import write_run_snapshot
from pdf_accessibility.persistence.run_logging import run_logging
from pdf_accessibility.persistence.run_record import bootstrap_run_record
from pdf_accessibility.persistence.runs import create_run, initial_document_state
from pdf_accessibility.services.review_decision_templates import (
    build_review_decision_template,
    load_review_tasks,
    resolve_review_tasks_path,
)
from pdf_accessibility.services.run_explanation import (
    RunExplainerConfig,
    RunExplainerError,
    generate_run_explanation_markdown,
)
from pdf_accessibility.utils.json import write_json

app = typer.Typer(help="Run the v0.1.0 PDF accessibility workflow scaffold.")
LOGGER = get_logger("pdf_accessibility.cli")


class ExplainerProvider(str, Enum):
    CODEX = "codex"
    CLAUDE_CODE = "claude_code"
    OPENROUTER = "openrouter"
    OLLAMA = "ollama"
    LMSTUDIO = "lmstudio"


def _run_workflow(
    input_pdf: Path,
    output_dir: Path,
    review_decisions: Path | None,
    ocr_recovery: Path | None,
    explain_run: bool,
    explainer_provider: ExplainerProvider,
    explainer_model: str | None,
    explainer_endpoint: str | None,
) -> None:
    context = create_run(input_pdf, output_dir)
    bootstrap_run_record(
        context.run_dir,
        argv=sys.argv,
        config={
            "input_pdf": str(input_pdf),
            "output_dir": str(output_dir),
            "review_decisions": str(review_decisions) if review_decisions is not None else None,
            "ocr_recovery": str(ocr_recovery) if ocr_recovery is not None else None,
            "explain_run": explain_run,
            "explainer_provider": explainer_provider.value,
            "explainer_model": explainer_model,
            "explainer_endpoint": explainer_endpoint,
        },
    )
    with run_logging(context.run_dir, argv=sys.argv):
        LOGGER.info(
            "CLI run started: input_pdf=%s output_dir=%s",
            input_pdf,
            output_dir,
            extra={"event_action": "cli_run_started", "input_path": str(input_pdf), "output_dir": str(output_dir)},
        )
        if review_decisions is not None:
            target = context.run_dir / "review_decisions_input.json"
            if review_decisions.resolve() != target.resolve():
                shutil.copyfile(review_decisions, target)
            LOGGER.info(
                "Seeded review decisions input: %s",
                target,
                extra={"event_action": "seed_review_decisions", "artifact_path": str(target)},
            )
        if ocr_recovery is not None:
            target = context.run_dir / "ocr_recovery_input.json"
            if ocr_recovery.resolve() != target.resolve():
                shutil.copyfile(ocr_recovery, target)
            LOGGER.info(
                "Seeded OCR recovery input: %s",
                target,
                extra={"event_action": "seed_ocr_recovery", "artifact_path": str(target)},
            )
        document = initial_document_state(context)
        result = build_workflow().invoke({"document": document})
        final_document = result["document"]
        if final_document.output_artifacts.execution_log is None:
            final_document.output_artifacts.execution_log = context.run_dir / "logs" / "execution.log"
        if final_document.output_artifacts.debug_log is None:
            final_document.output_artifacts.debug_log = context.run_dir / "logs" / "debug.log"
        if final_document.output_artifacts.events_jsonl is None:
            final_document.output_artifacts.events_jsonl = context.run_dir / "logs" / "events.jsonl"
        explanation_path, explanation_error = _maybe_generate_run_explanation(
            final_document,
            explain_run=explain_run,
            provider=explainer_provider,
            model=explainer_model,
            endpoint=explainer_endpoint,
        )
        guide = _load_operator_guide(context.run_dir / "operator_guide.json")
        LOGGER.info(
            "CLI run completed: status=%s finalization=%s blockers=%s",
            final_document.document_status.value,
            final_document.finalization_state.value,
            len(final_document.blocker_ids),
            extra={
                "event_action": "cli_run_completed",
                "document_status_after": final_document.document_status.value,
                "finalization_state_after": final_document.finalization_state.value,
                "blocker_count_after": len(final_document.blocker_ids),
            },
        )
        _emit_run_summary(
            context.run_dir,
            final_document,
            guide,
            explanation_path=explanation_path,
            explanation_error=explanation_error,
        )


@app.command()
def run(
    input_pdf: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False),
    output_dir: Path = typer.Option(Path("runs"), "--output-dir", "-o"),
    review_decisions: Path | None = typer.Option(None, "--review-decisions", exists=True, file_okay=True, dir_okay=False),
    ocr_recovery: Path | None = typer.Option(None, "--ocr-recovery", exists=True, file_okay=True, dir_okay=False),
    explain_run: bool = typer.Option(False, "--explain-run/--no-explain-run"),
    explainer_provider: ExplainerProvider = typer.Option(ExplainerProvider.CODEX, "--explainer-provider"),
    explainer_model: str | None = typer.Option(None, "--explainer-model"),
    explainer_endpoint: str | None = typer.Option(None, "--explainer-endpoint"),
) -> None:
    _run_workflow(
        input_pdf,
        output_dir,
        review_decisions,
        ocr_recovery,
        explain_run,
        explainer_provider,
        explainer_model,
        explainer_endpoint,
    )


@app.command("template-review-decisions")
def template_review_decisions(
    review_tasks_source: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=True),
    output: Path | None = typer.Option(None, "--output", "-o"),
) -> None:
    review_tasks_path = resolve_review_tasks_path(review_tasks_source)
    tasks = load_review_tasks(review_tasks_path)
    output_path = output or review_tasks_path.parent / "review_decisions_template.json"
    template = build_review_decision_template(tasks, source_path=review_tasks_path)
    write_json(output_path, template)
    typer.echo(f"template_path: {output_path}")
    typer.echo(f"decision_count: {template['decision_count']}")
    typer.echo(f"manual_only_task_count: {template['manual_only_task_count']}")


def main() -> None:
    argv = sys.argv[1:]
    known_commands = {"run", "template-review-decisions"}
    if argv and argv[0] not in known_commands and not argv[0].startswith("-"):
        argv = ["run", *argv]
    app(args=argv)


def _load_operator_guide(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _maybe_generate_run_explanation(
    final_document,
    *,
    explain_run: bool,
    provider: ExplainerProvider,
    model: str | None,
    endpoint: str | None,
) -> tuple[Path | None, str | None]:
    if not explain_run:
        return None, None
    LOGGER.info("Run explanation started: provider=%s", provider.value, extra={"event_action": "run_explanation_started", "ai_provider": provider.value})
    try:
        path = generate_run_explanation_markdown(
            final_document,
            RunExplainerConfig(
                provider=provider.value,
                model=model,
                endpoint=endpoint,
            ),
        )
    except RunExplainerError as exc:
        LOGGER.warning(
            "Run explanation failed: provider=%s error=%s",
            provider.value,
            exc,
            extra={"event_action": "run_explanation_failed", "ai_provider": provider.value, "error_message": str(exc)},
        )
        return None, str(exc)
    write_run_snapshot(final_document)
    LOGGER.info(
        "Run explanation completed: path=%s",
        path,
        extra={"event_action": "run_explanation_completed", "ai_provider": provider.value, "artifact_path": str(path)},
    )
    return path, None


def _emit_run_summary(
    run_dir: Path,
    final_document,
    guide: dict[str, object],
    *,
    explanation_path: Path | None,
    explanation_error: str | None,
) -> None:
    template_artifacts = guide.get("template_artifacts")
    if not isinstance(template_artifacts, dict):
        template_artifacts = {}
    primary_next_step = guide.get("primary_next_step")
    blocker_count = guide.get("blocker_count")
    typer.echo(f"run_dir: {run_dir}")
    typer.echo(f"langgraph_available: {langgraph_available()}")
    if final_document.output_artifacts.execution_log:
        typer.echo(f"execution_log: {final_document.output_artifacts.execution_log}")
    if final_document.output_artifacts.debug_log:
        typer.echo(f"debug_log: {final_document.output_artifacts.debug_log}")
    if final_document.output_artifacts.events_jsonl:
        typer.echo(f"events_jsonl: {final_document.output_artifacts.events_jsonl}")
    typer.echo(f"document_status: {final_document.document_status.value}")
    typer.echo(f"finalization_state: {final_document.finalization_state.value}")
    if isinstance(blocker_count, int):
        typer.echo(f"blocker_count: {blocker_count}")
    typer.echo(
        "review_decisions_template: "
        + (str(template_artifacts.get("review_decisions_template")) if template_artifacts.get("review_decisions_template") else "none")
    )
    typer.echo(
        "ocr_recovery_template: "
        + (str(template_artifacts.get("ocr_recovery_template")) if template_artifacts.get("ocr_recovery_template") else "none")
    )
    if isinstance(primary_next_step, dict) and primary_next_step.get("action"):
        typer.echo(f"primary_next_step: {primary_next_step.get('action')}")
        if primary_next_step.get("path"):
            typer.echo(f"primary_next_step_path: {primary_next_step.get('path')}")
    else:
        typer.echo("primary_next_step: none")
    if explanation_path is not None:
        typer.echo(f"run_explanation: {explanation_path}")
    elif explanation_error is not None:
        typer.echo(f"run_explanation: failed ({explanation_error})")
    else:
        typer.echo("run_explanation: none")


if __name__ == "__main__":
    main()
