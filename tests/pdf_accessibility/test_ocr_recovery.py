from __future__ import annotations

from pathlib import Path

import fitz

from pdf_accessibility.models.state import (
    DocumentMetadataEvidence,
    DocumentState,
    DocumentStatus,
    PageGeometryEvidence,
    PageState,
    RegionStatus,
    ReviewTask,
)
from pdf_accessibility.nodes import approval_gate, behavior_check, ocr_layout_analysis, structure_mapping_plan, write_tagged_draft
from pdf_accessibility.reducers.apply_events import apply_events
from pdf_accessibility.utils.json import write_json


def _write_blank_pdf(path: Path) -> None:
    document = fitz.open()
    document.new_page(width=612, height=792)
    document.save(path)
    document.close()


def _document(tmp_path: Path) -> DocumentState:
    source = tmp_path / "input.pdf"
    _write_blank_pdf(source)
    return DocumentState(
        document_id="doc-1",
        source_path=source,
        run_dir=tmp_path,
        metadata=DocumentMetadataEvidence(title="Recovered OCR Doc", primary_language="en-US"),
        page_count=1,
        pages=[PageState(page_number=1, geometry=PageGeometryEvidence(width=612, height=792, rotation=0))],
        review_tasks=[
            ReviewTask(
                task_id="task-ocr-1",
                issue_code="IMAGE_ONLY_PAGE_OCR_REQUIRED",
                severity="warning",
                target_ref="page:1",
                reason="Image-only page has no normalized text evidence; OCR or another recovery path is required.",
                blocking=True,
            )
        ],
    )


def test_ocr_recovery_resolves_image_only_page_task_and_adds_recovered_text(tmp_path: Path) -> None:
    document = _document(tmp_path)
    write_json(
        tmp_path / "ocr_recovery_input.json",
        {"page_recoveries": [{"page_number": 1, "text": "Recovered OCR paragraph text."}]},
    )

    updated = apply_events(document, ocr_layout_analysis.run(document))

    assert updated.review_tasks[0].resolved
    assert updated.blocker_ids == []
    assert updated.normalized_units
    assert updated.normalized_units[0].unit_type == "paragraph"
    assert updated.normalized_units[0].text == "Recovered OCR paragraph text."
    assert updated.pages[0].text_blocks
    assert updated.pages[0].text_blocks[0].extractor == "manual_ocr_recovery"
    artifact_names = [record.name for record in updated.artifact_manifest.records]
    assert "ocr_recovery_input.json" in artifact_names


def test_ocr_recovery_ignores_blank_recovery_text(tmp_path: Path) -> None:
    document = _document(tmp_path)
    write_json(
        tmp_path / "ocr_recovery_input.json",
        {"page_recoveries": [{"page_number": 1, "text": "   "}]},
    )

    updated = apply_events(document, ocr_layout_analysis.run(document))

    assert not updated.review_tasks[0].resolved
    assert updated.blocker_ids == ["task-ocr-1"]
    assert updated.normalized_units == []


def test_ocr_recovery_does_not_imply_finalizable_writeback(tmp_path: Path) -> None:
    document = _document(tmp_path)
    write_json(
        tmp_path / "ocr_recovery_input.json",
        {"page_recoveries": [{"page_number": 1, "text": "Recovered OCR paragraph text."}]},
    )

    updated = apply_events(document, ocr_layout_analysis.run(document))
    updated = apply_events(updated, structure_mapping_plan.run(updated))
    updated.document_status = DocumentStatus.PLANNING_IN_PROGRESS
    updated = apply_events(updated, behavior_check.run(updated))
    updated = apply_events(updated, approval_gate.run(updated))
    assert updated.document_status is DocumentStatus.DRAFT_READY
    assert any(region.status is RegionStatus.COMMITTABLE for page in updated.pages for region in page.regions)

    updated = apply_events(updated, write_tagged_draft.run(updated))

    assert updated.writeback_report is not None
    assert updated.writeback_report.finalization_blocked is True
    assert any(task.issue_code == "TAGGED_DRAFT_NOT_FINAL" for task in updated.review_tasks)
    assert updated.blocker_ids
