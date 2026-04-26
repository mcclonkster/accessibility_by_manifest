from __future__ import annotations

import json
from pathlib import Path

from pdf_accessibility.models.state import (
    ArtifactRecord,
    DocumentState,
    FinalizationState,
    Finding,
    FindingClass,
    ReviewTask,
    WritebackReport,
)
from pdf_accessibility.persistence.artifacts import write_run_snapshot


def _document(tmp_path: Path) -> DocumentState:
    source = tmp_path / "input.pdf"
    source.write_bytes(b"%PDF-1.7\n%%EOF\n")
    (tmp_path / "command.txt").write_text("test command\n", encoding="utf-8")
    logs_dir = tmp_path / "logs"
    logs_dir.mkdir(exist_ok=True)
    (logs_dir / "execution.log").write_text("run started\n", encoding="utf-8")
    (logs_dir / "debug.log").write_text("debug started\n", encoding="utf-8")
    (logs_dir / "events.jsonl").write_text('{"message":"run started"}\n', encoding="utf-8")
    return DocumentState(document_id="doc-1", source_path=source, run_dir=tmp_path)


def _artifact_names(tmp_path: Path) -> list[str]:
    payload = json.loads((tmp_path / "artifact_manifest.json").read_text(encoding="utf-8"))
    return [record["name"] for record in payload["records"]]


def test_run_snapshot_writes_required_artifact_contract(tmp_path: Path) -> None:
    document = _document(tmp_path)

    write_run_snapshot(document)

    expected = {
        "command.txt",
        "config.json",
        "document_state.json",
        "environment.txt",
        "findings.jsonl",
        "git.txt",
        "manifest.json",
        "review_tasks.json",
        "review_decisions.json",
        "normalized_structure.json",
        "notes.md",
        "status.json",
        "structure_mapping_plan.json",
        "writeback_report.json",
        "tagging_plan.json",
        "validator_findings.json",
        "finalization_status.json",
        "operator_guide.json",
        "run_log.json",
        "artifact_manifest.json",
    }
    assert expected <= {path.name for path in tmp_path.iterdir()}
    assert (tmp_path / "logs" / "execution.log").exists()
    assert (tmp_path / "logs" / "debug.log").exists()
    assert (tmp_path / "logs" / "events.jsonl").exists()
    assert (tmp_path / "metrics" / "summary.json").exists()
    assert (tmp_path / "metrics" / "timings.csv").exists()
    assert (tmp_path / "inputs" / "manifest.json").exists()
    assert (tmp_path / "outputs" / "manifest.json").exists()
    assert "input.pdf" in _artifact_names(tmp_path)
    assert expected <= set(_artifact_names(tmp_path))
    assert "execution.log" in _artifact_names(tmp_path)
    assert "debug.log" in _artifact_names(tmp_path)
    assert "events.jsonl" in _artifact_names(tmp_path)
    assert "metrics/summary.json" in _artifact_names(tmp_path)
    assert "metrics/timings.csv" in _artifact_names(tmp_path)
    assert "inputs/manifest.json" in _artifact_names(tmp_path)
    assert "outputs/manifest.json" in _artifact_names(tmp_path)


def test_findings_jsonl_is_written_even_when_empty(tmp_path: Path) -> None:
    document = _document(tmp_path)

    write_run_snapshot(document)

    assert (tmp_path / "findings.jsonl").read_text(encoding="utf-8") == ""


def test_snapshot_artifact_registration_is_idempotent(tmp_path: Path) -> None:
    document = _document(tmp_path)

    write_run_snapshot(document)
    write_run_snapshot(document)

    names = _artifact_names(tmp_path)
    assert names.count("document_state.json") == 1
    assert names.count("artifact_manifest.json") == 1
    assert names.count("run_log.json") == 1


def test_snapshot_registration_prefers_node_artifact_record(tmp_path: Path) -> None:
    document = _document(tmp_path)
    review_tasks_path = tmp_path / "review_tasks.json"
    document.artifact_manifest.records.append(
        ArtifactRecord(
            artifact_id="artifact-node-review",
            name="review_tasks.json",
            path=review_tasks_path,
            artifact_type="json",
            producer_node="human_review",
        )
    )

    write_run_snapshot(document)

    payload = json.loads((tmp_path / "artifact_manifest.json").read_text(encoding="utf-8"))
    review_records = [record for record in payload["records"] if record["name"] == "review_tasks.json"]
    assert len(review_records) == 1
    assert review_records[0]["producer_node"] == "human_review"


def test_run_log_summarizes_current_state(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.findings.append(
        Finding(
            finding_id="finding-1",
            node_name="test",
            finding_class=FindingClass.EVIDENCE,
            target_ref="document",
            message="Evidence recorded.",
        )
    )

    write_run_snapshot(document)

    payload = json.loads((tmp_path / "run_log.json").read_text(encoding="utf-8"))
    assert payload["run_id"] == tmp_path.name
    assert payload["counts"]["findings"] == 1
    assert payload["terminal_state"] == "pending"
    assert "document_state.json" in payload["artifact_names"]


def test_run_record_writes_status_manifest_and_metrics(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.finalization_state = FinalizationState.NEEDS_REVIEW
    document.review_tasks.append(
        ReviewTask(
            task_id="task-title",
            issue_code="DOCUMENT_TITLE_MISSING",
            severity="warning",
            target_ref="document_metadata.title",
            reason="No usable document title was found.",
            blocking=True,
            resolved=False,
        )
    )

    write_run_snapshot(document)

    status_payload = json.loads((tmp_path / "status.json").read_text(encoding="utf-8"))
    assert status_payload["document_status"] == "pending"
    assert status_payload["finalization_state"] == "needs_review"
    assert status_payload["blocker_count"] == 0
    manifest_payload = json.loads((tmp_path / "manifest.json").read_text(encoding="utf-8"))
    assert manifest_payload["metrics"]["summary_json"].endswith("metrics/summary.json")
    summary_payload = json.loads((tmp_path / "metrics" / "summary.json").read_text(encoding="utf-8"))
    assert summary_payload["review_task_count"] == 1
    assert summary_payload["warning_count"] == 1


def test_accessible_output_is_not_registered_until_file_exists(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.output_artifacts.accessible_output_pdf = tmp_path / "accessible_output.pdf"
    document.output_artifacts.accessible_output_html = tmp_path / "accessible_output.html"

    write_run_snapshot(document)

    assert "accessible_output.pdf" not in _artifact_names(tmp_path)
    assert "accessible_output.html" not in _artifact_names(tmp_path)


def test_run_explanation_is_registered_when_markdown_exists(tmp_path: Path) -> None:
    document = _document(tmp_path)
    explanation_path = tmp_path / "run_explanation.md"
    explanation_path.write_text("# Run Explanation\n", encoding="utf-8")
    document.output_artifacts.run_explanation_markdown = explanation_path

    write_run_snapshot(document)

    assert "run_explanation.md" in _artifact_names(tmp_path)


def test_run_explanation_log_is_registered_when_log_exists(tmp_path: Path) -> None:
    document = _document(tmp_path)
    log_path = tmp_path / "logs" / "run_explanation.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text('{"provider":"codex"}\n', encoding="utf-8")
    document.output_artifacts.run_explanation_log = log_path

    write_run_snapshot(document)

    assert "run_explanation.log" in _artifact_names(tmp_path)


def test_snapshot_marks_validator_report_skipped_when_no_tagged_draft_exists(tmp_path: Path) -> None:
    document = _document(tmp_path)

    write_run_snapshot(document)

    payload = json.loads((tmp_path / "validator_findings.json").read_text(encoding="utf-8"))
    assert payload["checked_path"] is None
    assert payload["draft_available"] is False
    assert payload["validation_state"] == "skipped"
    assert payload["skipped_reason"] == "no_tagged_draft_available"
    assert payload["passed"] is False


def test_snapshot_writes_review_decisions_template_for_needs_review_state(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.finalization_state = FinalizationState.NEEDS_REVIEW
    document.review_tasks.append(
        ReviewTask(
            task_id="task-title",
            issue_code="DOCUMENT_TITLE_MISSING",
            severity="warning",
            target_ref="document_metadata.title",
            reason="No usable document title was found.",
            blocking=True,
            resolved=False,
        )
    )

    write_run_snapshot(document)

    template_path = tmp_path / "review_decisions_template.json"
    assert template_path.exists()
    payload = json.loads(template_path.read_text(encoding="utf-8"))
    assert payload["decision_count"] == 1
    assert payload["decisions"][0]["decision_type"] == "set_document_title"
    assert "review_decisions_template.json" in _artifact_names(tmp_path)
    guide_payload = json.loads((tmp_path / "operator_guide.json").read_text(encoding="utf-8"))
    assert guide_payload["primary_next_step"]["action"] == "fill_review_decisions"


def test_snapshot_removes_review_decisions_template_when_run_is_finalized(tmp_path: Path) -> None:
    document = _document(tmp_path)
    template_path = tmp_path / "review_decisions_template.json"
    template_path.write_text('{"decisions": []}', encoding="utf-8")
    document.output_artifacts.review_decisions_template_json = template_path
    document.artifact_manifest.records.append(
        ArtifactRecord(
            artifact_id="artifact-review-template",
            name="review_decisions_template.json",
            path=template_path,
            artifact_type="review_decisions_template",
            producer_node="persistence",
        )
    )
    document.finalization_state = FinalizationState.FINALIZED

    write_run_snapshot(document)

    assert not template_path.exists()
    assert "review_decisions_template.json" not in _artifact_names(tmp_path)


def test_snapshot_writes_ocr_recovery_template_for_needs_review_ocr_task(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.finalization_state = FinalizationState.NEEDS_REVIEW
    document.review_tasks.append(
        ReviewTask(
            task_id="task-ocr-1",
            issue_code="IMAGE_ONLY_PAGE_OCR_REQUIRED",
            severity="warning",
            target_ref="page:3",
            reason="Image-only page needs OCR recovery.",
            blocking=True,
            resolved=False,
        )
    )

    write_run_snapshot(document)

    template_path = tmp_path / "ocr_recovery_template.json"
    assert template_path.exists()
    payload = json.loads(template_path.read_text(encoding="utf-8"))
    assert payload["page_recovery_count"] == 1
    assert payload["page_recoveries"][0]["page_number"] == 3
    assert "ocr_recovery_template.json" in _artifact_names(tmp_path)
    guide_payload = json.loads((tmp_path / "operator_guide.json").read_text(encoding="utf-8"))
    assert guide_payload["primary_next_step"]["action"] == "fill_ocr_recovery"


def test_snapshot_removes_ocr_recovery_template_when_run_is_finalized(tmp_path: Path) -> None:
    document = _document(tmp_path)
    template_path = tmp_path / "ocr_recovery_template.json"
    template_path.write_text('{"page_recoveries": []}', encoding="utf-8")
    document.output_artifacts.ocr_recovery_template_json = template_path
    document.artifact_manifest.records.append(
        ArtifactRecord(
            artifact_id="artifact-ocr-template",
            name="ocr_recovery_template.json",
            path=template_path,
            artifact_type="ocr_recovery_template",
            producer_node="persistence",
        )
    )
    document.finalization_state = FinalizationState.FINALIZED

    write_run_snapshot(document)

    assert not template_path.exists()
    assert "ocr_recovery_template.json" not in _artifact_names(tmp_path)


def test_snapshot_finalization_status_includes_writeback_blocking_categories(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.finalization_state = FinalizationState.NEEDS_REVIEW
    document.writeback_report = WritebackReport(
        draft_path=tmp_path / "tagged_draft.pdf",
        finalization_blocked=True,
        blocking_categories=["unsupported_structure_roles", "missing_document_title"],
        blocking_details={
            "unsupported_structure_roles": {"unsupported_role_counts": {"Figure": 1}},
            "missing_document_title": {"target": "document_metadata.title"},
        },
    )

    write_run_snapshot(document)

    payload = json.loads((tmp_path / "finalization_status.json").read_text(encoding="utf-8"))
    assert payload["writeback_finalization_blocked"] is True
    assert payload["writeback_blocking_categories"] == ["unsupported_structure_roles", "missing_document_title"]
    assert payload["writeback_blocking_details"]["unsupported_structure_roles"]["unsupported_role_counts"] == {
        "Figure": 1
    }


def test_snapshot_operator_guide_says_no_manual_next_step_when_finalized(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.finalization_state = FinalizationState.FINALIZED

    write_run_snapshot(document)

    payload = json.loads((tmp_path / "operator_guide.json").read_text(encoding="utf-8"))
    assert payload["finalization_state"] == "finalized"
    assert payload["primary_next_step"] is None
    assert payload["next_actions"] == []
