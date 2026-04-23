from __future__ import annotations

from pdf_accessibility.models.state import DocumentState, DocumentStatus, FinalizationState

NODE_NAME = "workflow_orchestrator"


def terminal_state(document: DocumentState) -> str | None:
    if document.document_status is DocumentStatus.FINALIZED:
        return FinalizationState.FINALIZED.value
    if document.document_status is DocumentStatus.WRITE_BLOCKED:
        return FinalizationState.WRITE_BLOCKED.value
    if document.finalization_state is FinalizationState.NEEDS_REVIEW:
        return FinalizationState.NEEDS_REVIEW.value
    return None

