from __future__ import annotations

from pdf_accessibility.models.state import DocumentState, DocumentStatus, FinalizationState, RegionStatus


def has_blockers(document: DocumentState) -> bool:
    return bool(document.blocker_ids)


def can_write_draft(document: DocumentState) -> bool:
    if document.document_status is not DocumentStatus.DRAFT_READY:
        return False
    if document.finalization_state is FinalizationState.WRITE_BLOCKED:
        return False
    if has_blockers(document):
        return False
    return any(region.status is RegionStatus.COMMITTABLE for page in document.pages for region in page.regions)


def can_finalize(document: DocumentState) -> bool:
    if document.output_artifacts.tagged_draft_pdf is None:
        return False
    if has_blockers(document):
        return False
    return document.document_status in {DocumentStatus.VALIDATED, DocumentStatus.REVIEW_APPLIED}

