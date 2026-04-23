from __future__ import annotations

import json
from pathlib import Path

from pdf_accessibility.models.state import ArtifactRecord, DocumentState, Finding, FindingClass
from pdf_accessibility.persistence.artifacts import write_run_snapshot


def _document(tmp_path: Path) -> DocumentState:
    source = tmp_path / "input.pdf"
    source.write_bytes(b"%PDF-1.7\n%%EOF\n")
    return DocumentState(document_id="doc-1", source_path=source, run_dir=tmp_path)


def _artifact_names(tmp_path: Path) -> list[str]:
    payload = json.loads((tmp_path / "artifact_manifest.json").read_text(encoding="utf-8"))
    return [record["name"] for record in payload["records"]]


def test_run_snapshot_writes_required_artifact_contract(tmp_path: Path) -> None:
    document = _document(tmp_path)

    write_run_snapshot(document)

    expected = {
        "document_state.json",
        "findings.jsonl",
        "review_tasks.json",
        "review_decisions.json",
        "normalized_structure.json",
        "structure_mapping_plan.json",
        "writeback_report.json",
        "tagging_plan.json",
        "validator_findings.json",
        "finalization_status.json",
        "run_log.json",
        "artifact_manifest.json",
    }
    assert expected <= {path.name for path in tmp_path.iterdir()}
    assert "input.pdf" in _artifact_names(tmp_path)
    assert expected <= set(_artifact_names(tmp_path))


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


def test_accessible_output_is_not_registered_until_file_exists(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.output_artifacts.accessible_output_pdf = tmp_path / "accessible_output.pdf"

    write_run_snapshot(document)

    assert "accessible_output.pdf" not in _artifact_names(tmp_path)
