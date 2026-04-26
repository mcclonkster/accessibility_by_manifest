from __future__ import annotations

import csv
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pdf_accessibility.models.state import DocumentState
from pdf_accessibility.utils.json import write_json


DEFAULT_STATUS = "queued"
LIFECYCLE_STATUSES = {"queued", "running", "completed", "failed", "interrupted", "abandoned"}


def bootstrap_run_record(
    run_dir: Path,
    *,
    argv: list[str],
    config: dict[str, Any],
) -> None:
    (run_dir / "inputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "outputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "metrics").mkdir(parents=True, exist_ok=True)

    (run_dir / "command.txt").write_text(" ".join(argv).strip() + "\n", encoding="utf-8")
    write_json(run_dir / "config.json", config)
    (run_dir / "environment.txt").write_text(_environment_text(), encoding="utf-8")
    (run_dir / "git.txt").write_text(_git_text(run_dir), encoding="utf-8")
    notes_path = run_dir / "notes.md"
    if not notes_path.exists():
        notes_path.write_text("# Run Notes\n\n", encoding="utf-8")
    write_json(
        run_dir / "status.json",
        {
            "run_id": run_dir.name,
            "run_status": DEFAULT_STATUS,
            "started_at": None,
            "ended_at": None,
            "duration_ms": None,
            "exit_code": None,
            "error_message": None,
        },
    )


def update_run_status(
    run_dir: Path,
    *,
    run_status: str,
    started_at: str | None = None,
    ended_at: str | None = None,
    duration_ms: int | None = None,
    exit_code: int | None = None,
    error_message: str | None = None,
    document_status: str | None = None,
    finalization_state: str | None = None,
    blocker_count: int | None = None,
) -> None:
    if run_status not in LIFECYCLE_STATUSES:
        raise ValueError(f"Unsupported run status: {run_status}")
    path = run_dir / "status.json"
    payload = _load_json(path)
    payload.update(
        {
            "run_id": run_dir.name,
            "run_status": run_status,
            "started_at": started_at if started_at is not None else payload.get("started_at"),
            "ended_at": ended_at if ended_at is not None else payload.get("ended_at"),
            "duration_ms": duration_ms if duration_ms is not None else payload.get("duration_ms"),
            "exit_code": exit_code if exit_code is not None else payload.get("exit_code"),
            "error_message": error_message if error_message is not None else payload.get("error_message"),
            "document_status": document_status if document_status is not None else payload.get("document_status"),
            "finalization_state": finalization_state if finalization_state is not None else payload.get("finalization_state"),
            "blocker_count": blocker_count if blocker_count is not None else payload.get("blocker_count"),
            "updated_at": _now_iso(),
        }
    )
    write_json(path, payload)


def write_run_record(document: DocumentState) -> None:
    run_dir = document.run_dir
    _ensure_bootstrap_files(run_dir)
    _write_status_json(document)
    _write_metrics_summary(document)
    _write_timings_csv(document)
    _write_inputs_manifest(document)
    _write_outputs_manifest(document)
    _write_manifest(document)


def _write_status_json(document: DocumentState) -> None:
    path = document.run_dir / "status.json"
    payload = _load_json(path)
    payload.update(
        {
            "run_id": document.run_dir.name,
            "document_status": document.document_status.value,
            "finalization_state": document.finalization_state.value,
            "blocker_count": len(document.blocker_ids),
            "terminal_state": _terminal_state(document),
        }
    )
    write_json(path, payload)


def _write_metrics_summary(document: DocumentState) -> None:
    duration_ms = _run_duration_ms(document)
    summary = {
        "run_id": document.run_dir.name,
        "document_status": document.document_status.value,
        "finalization_state": document.finalization_state.value,
        "page_count": document.page_count,
        "normalized_unit_count": len(document.normalized_units),
        "finding_count": len(document.findings),
        "active_finding_count": sum(1 for finding in document.findings if finding.status.value == "active"),
        "review_task_count": len(document.review_tasks),
        "unresolved_review_task_count": sum(1 for task in document.review_tasks if not task.resolved),
        "review_decision_count": len(document.review_decisions),
        "validator_finding_count": len(document.validator_findings),
        "blocker_count": len(document.blocker_ids),
        "blocker_counts_by_issue_code": _blocker_counts_by_issue_code(document),
        "warning_count": sum(1 for task in document.review_tasks if task.severity == "warning"),
        "error_count": sum(1 for task in document.review_tasks if task.severity == "error"),
        "duration_ms": duration_ms,
        "node_count": len(document.workflow_trace),
    }
    write_json(document.run_dir / "metrics" / "summary.json", summary)


def _write_timings_csv(document: DocumentState) -> None:
    path = document.run_dir / "metrics" / "timings.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "node_name",
                "action",
                "started_at",
                "ended_at",
                "duration_ms",
                "event_count",
                "before_status",
                "after_status",
                "before_finalization_state",
                "after_finalization_state",
                "reason",
            ],
        )
        writer.writeheader()
        for entry in document.workflow_trace:
            writer.writerow(
                {
                    "node_name": entry.node_name,
                    "action": entry.action,
                    "started_at": entry.started_at,
                    "ended_at": entry.ended_at,
                    "duration_ms": entry.duration_ms,
                    "event_count": entry.event_count,
                    "before_status": entry.before_status.value,
                    "after_status": entry.after_status.value,
                    "before_finalization_state": entry.before_finalization_state.value,
                    "after_finalization_state": entry.after_finalization_state.value,
                    "reason": entry.reason or "",
                }
            )


def _write_inputs_manifest(document: DocumentState) -> None:
    input_artifacts = ["input.pdf"]
    if (document.run_dir / "review_decisions_input.json").exists():
        input_artifacts.append("review_decisions_input.json")
    if (document.run_dir / "ocr_recovery_input.json").exists():
        input_artifacts.append("ocr_recovery_input.json")
    write_json(
        document.run_dir / "inputs" / "manifest.json",
        {
            "source_pdf": str(document.source_path),
            "input_artifacts": input_artifacts,
        },
    )


def _write_outputs_manifest(document: DocumentState) -> None:
    outputs = {
        "tagged_draft_pdf": str(document.output_artifacts.tagged_draft_pdf)
        if document.output_artifacts.tagged_draft_pdf and document.output_artifacts.tagged_draft_pdf.exists()
        else None,
        "accessible_output_pdf": str(document.output_artifacts.accessible_output_pdf)
        if document.output_artifacts.accessible_output_pdf and document.output_artifacts.accessible_output_pdf.exists()
        else None,
        "accessible_output_html": str(document.output_artifacts.accessible_output_html)
        if document.output_artifacts.accessible_output_html and document.output_artifacts.accessible_output_html.exists()
        else None,
        "run_explanation_markdown": str(document.output_artifacts.run_explanation_markdown)
        if document.output_artifacts.run_explanation_markdown and document.output_artifacts.run_explanation_markdown.exists()
        else None,
    }
    write_json(document.run_dir / "outputs" / "manifest.json", outputs)


def _write_manifest(document: DocumentState) -> None:
    manifest = {
        "run_id": document.run_dir.name,
        "document_id": document.document_id,
        "source_path": str(document.source_path),
        "run_dir": str(document.run_dir),
        "status_path": str(document.run_dir / "status.json"),
        "command_path": str(document.run_dir / "command.txt"),
        "config_path": str(document.run_dir / "config.json"),
        "environment_path": str(document.run_dir / "environment.txt"),
        "git_path": str(document.run_dir / "git.txt"),
        "notes_path": str(document.run_dir / "notes.md"),
        "logs": {
            "execution_log": str(document.run_dir / "logs" / "execution.log"),
            "debug_log": str(document.run_dir / "logs" / "debug.log"),
            "events_jsonl": str(document.run_dir / "logs" / "events.jsonl"),
            "run_explanation_log": str(document.run_dir / "logs" / "run_explanation.log"),
        },
        "metrics": {
            "summary_json": str(document.run_dir / "metrics" / "summary.json"),
            "timings_csv": str(document.run_dir / "metrics" / "timings.csv"),
        },
        "inputs_manifest": str(document.run_dir / "inputs" / "manifest.json"),
        "outputs_manifest": str(document.run_dir / "outputs" / "manifest.json"),
        "artifact_manifest": str(document.run_dir / "artifact_manifest.json"),
    }
    write_json(document.run_dir / "manifest.json", manifest)


def _environment_text() -> str:
    lines = [
        f"generated_at: {_now_iso()}",
        f"cwd: {Path.cwd()}",
        f"python_executable: {sys.executable}",
        f"python_version: {sys.version}",
        f"platform: {platform.platform()}",
        f"PYTHONPATH: {os.environ.get('PYTHONPATH', '')}",
        f"VIRTUAL_ENV: {os.environ.get('VIRTUAL_ENV', '')}",
    ]
    return "\n".join(lines).rstrip() + "\n"


def _git_text(run_dir: Path) -> str:
    commands = {
        "repo_root": ["git", "-C", str(run_dir), "rev-parse", "--show-toplevel"],
        "branch": ["git", "-C", str(run_dir), "rev-parse", "--abbrev-ref", "HEAD"],
        "commit": ["git", "-C", str(run_dir), "rev-parse", "HEAD"],
        "status": ["git", "-C", str(run_dir), "status", "--short"],
    }
    lines: list[str] = [f"generated_at: {_now_iso()}"]
    for label, cmd in commands.items():
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=10)
        except OSError as exc:
            lines.append(f"{label}: unavailable ({exc})")
            continue
        if result.returncode != 0:
            stderr = result.stderr.strip() or result.stdout.strip() or "unknown error"
            lines.append(f"{label}: unavailable ({stderr})")
            continue
        value = result.stdout.rstrip("\n")
        lines.append(f"{label}:")
        lines.append(value if value else "<empty>")
    return "\n".join(lines).rstrip() + "\n"


def _run_duration_ms(document: DocumentState) -> int | None:
    durations = [entry.duration_ms for entry in document.workflow_trace if entry.duration_ms is not None]
    return sum(durations) if durations else None


def _blocker_counts_by_issue_code(document: DocumentState) -> dict[str, int]:
    counts: dict[str, int] = {}
    for task in document.review_tasks:
        if task.blocking and not task.resolved:
            counts[task.issue_code] = counts.get(task.issue_code, 0) + 1
    return counts


def _terminal_state(document: DocumentState) -> str:
    if document.finalization_state.value in {"finalized", "needs_review", "write_blocked"}:
        return document.finalization_state.value
    if document.blocker_ids:
        return "needs_review"
    return "pending"


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _ensure_bootstrap_files(run_dir: Path) -> None:
    (run_dir / "inputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "outputs").mkdir(parents=True, exist_ok=True)
    (run_dir / "metrics").mkdir(parents=True, exist_ok=True)
    (run_dir / "logs").mkdir(parents=True, exist_ok=True)
    if not (run_dir / "command.txt").exists():
        (run_dir / "command.txt").write_text("\n", encoding="utf-8")
    if not (run_dir / "config.json").exists():
        write_json(run_dir / "config.json", {})
    if not (run_dir / "environment.txt").exists():
        (run_dir / "environment.txt").write_text(_environment_text(), encoding="utf-8")
    if not (run_dir / "git.txt").exists():
        (run_dir / "git.txt").write_text(_git_text(run_dir), encoding="utf-8")
    if not (run_dir / "notes.md").exists():
        (run_dir / "notes.md").write_text("# Run Notes\n\n", encoding="utf-8")
