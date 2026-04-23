from __future__ import annotations

import json
from pathlib import Path

import fitz
import pikepdf

from pdf_accessibility.graph.build_graph import build_workflow, langgraph_available
from pdf_accessibility.models.state import DocumentStatus, FinalizationState
from pdf_accessibility.persistence.runs import create_run, initial_document_state


def _write_one_page_pdf(path: Path) -> None:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Accessible PDF workflow scaffold")
    document.save(path)
    document.close()


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


def test_langgraph_import_is_available() -> None:
    assert langgraph_available()


def test_workflow_scaffold_writes_required_artifacts(tmp_path: Path) -> None:
    source_pdf = tmp_path / "input.pdf"
    _write_one_page_pdf(source_pdf)
    context = create_run(source_pdf, tmp_path / "runs")
    document = initial_document_state(context)

    result = build_workflow().invoke({"document": document})
    final_document = result["document"]

    assert final_document.document_status is DocumentStatus.NEEDS_REVIEW
    assert final_document.finalization_state is FinalizationState.NEEDS_REVIEW
    assert final_document.page_count == 1
    assert final_document.pages[0].text_blocks
    assert final_document.normalized_units
    assert final_document.blocker_ids
    assert any(blocker_id.startswith(("review-", "finding-")) for blocker_id in final_document.blocker_ids)
    assert (context.run_dir / "document_state.json").exists()
    assert (context.run_dir / "normalized_structure.json").exists()
    assert (context.run_dir / "tagging_plan.json").exists()
    assert (context.run_dir / "structure_mapping_plan.json").exists()
    assert (context.run_dir / "review_tasks.json").exists()
    assert (context.run_dir / "finalization_status.json").exists()
    assert not (context.run_dir / "accessible_output.pdf").exists()

    run_log = json.loads((context.run_dir / "run_log.json").read_text(encoding="utf-8"))
    trace = {entry["node_name"]: entry for entry in run_log["workflow_trace"]}
    assert trace["write_tagged_draft"]["action"] == "skipped"
    assert "unresolved blockers" in trace["write_tagged_draft"]["reason"]
    assert trace["validator_check"]["action"] == "skipped"
    assert trace["human_review"]["action"] == "ran"
    assert trace["finalize_accessible_output"]["action"] == "ran"


def test_workflow_routes_through_draft_and_validator_when_ready(tmp_path: Path) -> None:
    source_pdf = tmp_path / "ready.pdf"
    _write_ready_one_page_pdf(source_pdf)
    context = create_run(source_pdf, tmp_path / "runs")
    document = initial_document_state(context)

    result = build_workflow().invoke({"document": document})
    final_document = result["document"]

    assert final_document.document_status is DocumentStatus.NEEDS_REVIEW
    assert final_document.finalization_state is FinalizationState.NEEDS_REVIEW
    assert (context.run_dir / "tagged_draft.pdf").exists()
    assert (context.run_dir / "validator_findings.json").exists()
    assert not (context.run_dir / "accessible_output.pdf").exists()

    run_log = json.loads((context.run_dir / "run_log.json").read_text(encoding="utf-8"))
    trace = {entry["node_name"]: entry for entry in run_log["workflow_trace"]}
    assert trace["write_tagged_draft"]["action"] == "ran"
    assert trace["validator_check"]["action"] == "ran"
    assert trace["human_review"]["action"] == "ran"
    assert trace["finalize_accessible_output"]["action"] == "ran"


def test_workflow_does_not_register_final_output_without_legal_finalization(tmp_path: Path) -> None:
    source_pdf = tmp_path / "ready.pdf"
    _write_ready_one_page_pdf(source_pdf)
    context = create_run(source_pdf, tmp_path / "runs")
    document = initial_document_state(context)

    final_document = build_workflow().invoke({"document": document})["document"]

    assert final_document.output_artifacts.accessible_output_pdf is None
    assert not (context.run_dir / "accessible_output.pdf").exists()
    artifact_manifest = json.loads((context.run_dir / "artifact_manifest.json").read_text(encoding="utf-8"))
    artifact_names = [record["name"] for record in artifact_manifest["records"]]
    assert "accessible_output.pdf" not in artifact_names
