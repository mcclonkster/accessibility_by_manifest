from __future__ import annotations

from pathlib import Path

import fitz
import pikepdf
from typer.testing import CliRunner
import json

import pdf_accessibility.cli as cli_module
from pdf_accessibility.cli import app
from pdf_accessibility.models.state import DocumentStatus, FinalizationState
from pdf_accessibility.utils.ids import stable_id
from pdf_accessibility.utils.json import write_json


def _write_ready_one_page_pdf(path: Path) -> None:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Annual Report")
    page.insert_text((72, 110), "A short accessible paragraph.")
    document.set_metadata({"title": "Annual Report"})
    document.save(path)
    document.close()
    with pikepdf.open(path, allow_overwriting_input=True) as pdf:
        pdf.Root["/Lang"] = pikepdf.String("en-US")
        pdf.save(path)


def _write_ready_simple_list_pdf(path: Path) -> None:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Quarterly Tasks")
    page.insert_text((72, 110), "1. Review filings")
    page.insert_text((72, 132), "2. Update disclosures")
    document.set_metadata({"title": "Quarterly Tasks"})
    document.save(path)
    document.close()
    with pikepdf.open(path, allow_overwriting_input=True) as pdf:
        pdf.Root["/Lang"] = pikepdf.String("en-US")
        pdf.save(path)


def test_pdf_cli_smoke_produces_finalized_output_for_simple_pdf(tmp_path: Path) -> None:
    source_pdf = tmp_path / "ready.pdf"
    output_dir = tmp_path / "runs"
    _write_ready_one_page_pdf(source_pdf)

    result = CliRunner().invoke(app, ["run", str(source_pdf), "--output-dir", str(output_dir)])

    assert result.exit_code == 0, result.output
    assert "execution_log:" in result.output
    assert "debug_log:" in result.output
    assert "events_jsonl:" in result.output
    assert "document_status: finalized" in result.output
    assert "finalization_state: finalized" in result.output
    assert "primary_next_step: none" in result.output
    assert "review_decisions_template: none" in result.output
    assert "ocr_recovery_template: none" in result.output
    assert "run_explanation: none" in result.output
    run_dirs = [path for path in output_dir.iterdir() if path.is_dir()]
    assert len(run_dirs) == 1
    run_dir = run_dirs[0]
    assert (run_dir / "logs" / "execution.log").exists()
    assert (run_dir / "logs" / "debug.log").exists()
    events_path = run_dir / "logs" / "events.jsonl"
    assert events_path.exists()
    first_event = json.loads(events_path.read_text(encoding="utf-8").splitlines()[0])
    assert "@timestamp" in first_event
    assert "log.level" in first_event
    assert first_event["service.name"] == "accessibility_by_manifest"
    assert first_event["run.id"] == run_dir.name
    assert (run_dir / "tagged_draft.pdf").exists()
    assert (run_dir / "accessible_output.pdf").exists()
    html_payload = (run_dir / "accessible_output.html").read_text(encoding="utf-8")
    assert "<h1>Annual Report</h1>" in html_payload


def test_pdf_cli_smoke_produces_finalized_output_for_simple_list_pdf(tmp_path: Path) -> None:
    source_pdf = tmp_path / "ready-list.pdf"
    output_dir = tmp_path / "runs"
    _write_ready_simple_list_pdf(source_pdf)

    result = CliRunner().invoke(app, ["run", str(source_pdf), "--output-dir", str(output_dir)])

    assert result.exit_code == 0, result.output
    assert "execution_log:" in result.output
    assert "debug_log:" in result.output
    assert "events_jsonl:" in result.output
    assert "document_status: finalized" in result.output
    assert "finalization_state: finalized" in result.output
    assert "primary_next_step: none" in result.output
    assert "run_explanation: none" in result.output
    run_dirs = [path for path in output_dir.iterdir() if path.is_dir()]
    assert len(run_dirs) == 1
    run_dir = run_dirs[0]
    assert (run_dir / "logs" / "execution.log").exists()
    assert (run_dir / "logs" / "debug.log").exists()
    assert (run_dir / "logs" / "events.jsonl").exists()
    assert (run_dir / "tagged_draft.pdf").exists()
    assert (run_dir / "accessible_output.pdf").exists()
    html_payload = (run_dir / "accessible_output.html").read_text(encoding="utf-8")
    assert "<h1>Quarterly Tasks</h1>" in html_payload
    assert "<ul>" in html_payload
    assert "<li>1. Review filings</li>" in html_payload


def test_pdf_cli_can_apply_review_decisions_file_for_needs_review_pdf(tmp_path: Path) -> None:
    source_pdf = tmp_path / "needs_review.pdf"
    output_dir = tmp_path / "runs"
    decisions_path = tmp_path / "review_decisions.json"
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Needs Review Report")
    document.save(source_pdf)
    document.close()
    write_json(
        decisions_path,
        [
            {
                "decision_id": f"decision-{stable_id('title')}",
                "target_review_task_id": f"review-{stable_id('DOCUMENT_TITLE_MISSING', 'document')}",
                "decision_type": "set_document_title",
                "value": "Needs Review Report",
                "reviewer": "test",
                "created_at": "2026-04-25T00:00:00Z",
            },
            {
                "decision_id": f"decision-{stable_id('language')}",
                "target_review_task_id": f"review-{stable_id('DOCUMENT_LANGUAGE_MISSING', 'document')}",
                "decision_type": "set_primary_language",
                "value": "en-US",
                "reviewer": "test",
                "created_at": "2026-04-25T00:00:00Z",
            },
        ],
    )

    result = CliRunner().invoke(
        app,
        ["run", str(source_pdf), "--output-dir", str(output_dir), "--review-decisions", str(decisions_path)],
    )

    assert result.exit_code == 0, result.output
    assert "execution_log:" in result.output
    assert "debug_log:" in result.output
    assert "events_jsonl:" in result.output
    assert "document_status: finalized" in result.output
    assert "finalization_state: finalized" in result.output
    assert "primary_next_step: none" in result.output
    run_dirs = [path for path in output_dir.iterdir() if path.is_dir()]
    assert len(run_dirs) == 1
    run_dir = run_dirs[0]
    assert (run_dir / "review_decisions_input.json").exists()
    assert (run_dir / "review_decisions.json").exists()
    assert (run_dir / "tagged_draft.pdf").exists()
    assert (run_dir / "accessible_output.pdf").exists()
    assert not (run_dir / "review_decisions_template.json").exists()


def test_pdf_cli_auto_writes_review_decisions_template_for_needs_review_run(tmp_path: Path) -> None:
    source_pdf = tmp_path / "needs_review.pdf"
    output_dir = tmp_path / "runs"
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Needs Review Report")
    document.save(source_pdf)
    document.close()

    result = CliRunner().invoke(app, ["run", str(source_pdf), "--output-dir", str(output_dir)])

    assert result.exit_code == 0, result.output
    assert "execution_log:" in result.output
    assert "debug_log:" in result.output
    assert "events_jsonl:" in result.output
    assert "document_status: needs_review" in result.output
    assert "finalization_state: needs_review" in result.output
    assert "primary_next_step: fill_review_decisions" in result.output
    assert "review_decisions_template:" in result.output
    assert "ocr_recovery_template: none" in result.output
    assert "run_explanation: none" in result.output
    run_dirs = [path for path in output_dir.iterdir() if path.is_dir()]
    assert len(run_dirs) == 1
    run_dir = run_dirs[0]
    template_path = run_dir / "review_decisions_template.json"
    assert template_path.exists()
    payload = __import__("json").loads(template_path.read_text(encoding="utf-8"))
    assert payload["decision_count"] >= 1


def test_pdf_cli_can_generate_review_decision_template(tmp_path: Path) -> None:
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    write_json(
        run_dir / "review_tasks.json",
        [
            {
                "task_id": "task-title",
                "issue_code": "DOCUMENT_TITLE_MISSING",
                "severity": "warning",
                "target_ref": "document_metadata.title",
                "reason": "No usable document title was found.",
                "blocking": True,
                "resolved": False,
                "confidence_context": {},
                "source_finding_ids": [],
            },
            {
                "task_id": "task-draft",
                "issue_code": "TAGGED_DRAFT_NOT_FINAL",
                "severity": "error",
                "target_ref": "document",
                "reason": "Tagged draft is not finalizable.",
                "blocking": True,
                "resolved": False,
                "confidence_context": {},
                "source_finding_ids": [],
            },
        ],
    )

    result = CliRunner().invoke(app, ["template-review-decisions", str(run_dir)])

    assert result.exit_code == 0, result.output
    assert "decision_count: 1" in result.output
    assert "manual_only_task_count: 1" in result.output
    template_path = run_dir / "review_decisions_template.json"
    assert template_path.exists()
    payload = __import__("json").loads(template_path.read_text(encoding="utf-8"))
    assert payload["decisions"][0]["decision_type"] == "set_document_title"
    assert payload["manual_only_tasks"][0]["issue_code"] == "TAGGED_DRAFT_NOT_FINAL"


def test_pdf_cli_generates_actionable_table_review_template(tmp_path: Path) -> None:
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    write_json(
        run_dir / "review_tasks.json",
        [
            {
                "task_id": "task-table",
                "issue_code": "TABLE_HEADERS_UNCERTAIN",
                "severity": "warning",
                "target_ref": "table:1",
                "reason": "Header row is uncertain.",
                "blocking": True,
                "resolved": False,
                "confidence_context": {},
                "source_finding_ids": [],
            }
        ],
    )

    result = CliRunner().invoke(app, ["template-review-decisions", str(run_dir)])

    assert result.exit_code == 0, result.output
    payload = __import__("json").loads((run_dir / "review_decisions_template.json").read_text(encoding="utf-8"))
    assert payload["decisions"][0]["decision_type"] == "confirm_table_reviewed"


def test_pdf_cli_generates_actionable_figure_review_template_without_summary_shortcut(tmp_path: Path) -> None:
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    write_json(
        run_dir / "review_tasks.json",
        [
            {
                "task_id": "task-summary",
                "issue_code": "FIGURE_CANDIDATES_REQUIRE_REVIEW",
                "severity": "warning",
                "target_ref": "document_summary.figure_candidate_count",
                "reason": "Figure candidates require review.",
                "blocking": True,
                "resolved": False,
                "confidence_context": {"figure_candidate_count": 2},
                "source_finding_ids": [],
            },
            {
                "task_id": "task-figure-1",
                "issue_code": "FIGURE_ALT_TEXT_REQUIRED",
                "severity": "error",
                "target_ref": "region-figure-1",
                "reason": "Meaningful figure candidate needs trusted alt text.",
                "blocking": True,
                "resolved": False,
                "confidence_context": {},
                "source_finding_ids": [],
            },
        ],
    )

    result = CliRunner().invoke(app, ["template-review-decisions", str(run_dir)])

    assert result.exit_code == 0, result.output
    payload = __import__("json").loads((run_dir / "review_decisions_template.json").read_text(encoding="utf-8"))
    assert [entry["issue_code"] for entry in payload["decisions"]] == ["FIGURE_ALT_TEXT_REQUIRED"]
    assert payload["manual_only_tasks"] == []


def test_pdf_cli_surfaces_ocr_template_next_step_when_operator_guide_requires_it(tmp_path: Path, monkeypatch) -> None:
    source_pdf = tmp_path / "ocr-needs-review.pdf"
    output_dir = tmp_path / "runs"
    _write_ready_one_page_pdf(source_pdf)

    class _FakeWorkflow:
        def invoke(self, payload):
            document = payload["document"]
            document.document_status = DocumentStatus.NEEDS_REVIEW
            document.finalization_state = FinalizationState.NEEDS_REVIEW
            guide_path = document.run_dir / "operator_guide.json"
            write_json(
                guide_path,
                {
                    "document_status": "needs_review",
                    "finalization_state": "needs_review",
                    "blocker_count": 2,
                    "template_artifacts": {
                        "review_decisions_template": None,
                        "ocr_recovery_template": str(document.run_dir / "ocr_recovery_template.json"),
                    },
                    "primary_next_step": {
                        "action": "fill_ocr_recovery",
                        "path": str(document.run_dir / "ocr_recovery_template.json"),
                        "reason": "Image-only pages still need OCR recovery text.",
                    },
                    "next_actions": [],
                },
            )
            return {"document": document}

    monkeypatch.setattr(cli_module, "build_workflow", lambda: _FakeWorkflow())

    result = CliRunner().invoke(app, ["run", str(source_pdf), "--output-dir", str(output_dir)])

    assert result.exit_code == 0, result.output
    assert "execution_log:" in result.output
    assert "debug_log:" in result.output
    assert "events_jsonl:" in result.output
    assert "document_status: needs_review" in result.output
    assert "finalization_state: needs_review" in result.output
    assert "blocker_count: 2" in result.output
    assert "primary_next_step: fill_ocr_recovery" in result.output
    assert "review_decisions_template: none" in result.output
    assert "ocr_recovery_template:" in result.output


def test_pdf_cli_can_write_run_explanation_when_enabled(tmp_path: Path, monkeypatch) -> None:
    source_pdf = tmp_path / "ready.pdf"
    output_dir = tmp_path / "runs"
    _write_ready_one_page_pdf(source_pdf)

    def _fake_generate(document, config):
        path = document.run_dir / "run_explanation.md"
        path.write_text("# Run Explanation\n\nGenerated by test.\n", encoding="utf-8")
        document.output_artifacts.run_explanation_markdown = path
        return path

    monkeypatch.setattr(cli_module, "generate_run_explanation_markdown", _fake_generate)

    result = CliRunner().invoke(
        app,
        [
            "run",
            str(source_pdf),
            "--output-dir",
            str(output_dir),
            "--explain-run",
            "--explainer-provider",
            "codex",
        ],
    )

    assert result.exit_code == 0, result.output
    assert "execution_log:" in result.output
    assert "debug_log:" in result.output
    assert "events_jsonl:" in result.output
    run_dir = next(path for path in output_dir.iterdir() if path.is_dir())
    assert (run_dir / "run_explanation.md").exists()
    assert "run_explanation:" in result.output
    artifact_names = __import__("json").loads((run_dir / "artifact_manifest.json").read_text(encoding="utf-8"))
    assert "run_explanation.md" in [record["name"] for record in artifact_names["records"]]


def test_pdf_cli_soft_fails_when_run_explanation_provider_errors(tmp_path: Path, monkeypatch) -> None:
    source_pdf = tmp_path / "ready.pdf"
    output_dir = tmp_path / "runs"
    _write_ready_one_page_pdf(source_pdf)

    def _fake_generate(document, config):
        raise cli_module.RunExplainerError("provider unavailable")

    monkeypatch.setattr(cli_module, "generate_run_explanation_markdown", _fake_generate)

    result = CliRunner().invoke(
        app,
        [
            "run",
            str(source_pdf),
            "--output-dir",
            str(output_dir),
            "--explain-run",
            "--explainer-provider",
            "ollama",
        ],
    )

    assert result.exit_code == 0, result.output
    assert "execution_log:" in result.output
    assert "debug_log:" in result.output
    assert "events_jsonl:" in result.output
    assert "document_status: finalized" in result.output
    assert "run_explanation: failed (provider unavailable)" in result.output
