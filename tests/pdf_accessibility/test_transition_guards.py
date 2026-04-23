from __future__ import annotations

from pathlib import Path

from pdf_accessibility.models.state import DocumentState, DocumentStatus, PageState, RegionState, RegionStatus
from pdf_accessibility.transition_guards.finalization import can_finalize, can_write_draft


def test_write_draft_requires_ready_committable_unblocked_document(tmp_path: Path) -> None:
    document = DocumentState(
        document_id="doc-1",
        source_path=tmp_path / "input.pdf",
        run_dir=tmp_path,
        document_status=DocumentStatus.DRAFT_READY,
        pages=[PageState(page_number=1, regions=[RegionState(region_id="r1", page_number=1, status=RegionStatus.COMMITTABLE)])],
    )

    assert can_write_draft(document)


def test_finalize_requires_tagged_draft_and_validated_state(tmp_path: Path) -> None:
    document = DocumentState(
        document_id="doc-1",
        source_path=tmp_path / "input.pdf",
        run_dir=tmp_path,
        document_status=DocumentStatus.VALIDATED,
    )
    document.output_artifacts.tagged_draft_pdf = tmp_path / "tagged_draft.pdf"

    assert can_finalize(document)

