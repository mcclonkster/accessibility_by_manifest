from __future__ import annotations

from pdf_accessibility.models.events import NodeEvent, finalization_state_event, region_status_event, workflow_state_event
from pdf_accessibility.models.state import DocumentState, DocumentStatus, FinalizationState, RegionStatus
from pdf_accessibility.utils.ids import event_id

NODE_NAME = "approval_gate"


def run(document: DocumentState) -> list[NodeEvent]:
    if document.blocker_ids:
        return [
            finalization_state_event(
                event_id(NODE_NAME, "blocked", document.document_id),
                NODE_NAME,
                FinalizationState.NEEDS_REVIEW,
            ),
            workflow_state_event(
                event_id(NODE_NAME, "review", document.document_id),
                NODE_NAME,
                DocumentStatus.NEEDS_REVIEW,
            ),
        ]
    events: list[NodeEvent] = []
    for page in document.pages:
        for region in page.regions:
            events.append(region_status_event(event_id(NODE_NAME, region.region_id), NODE_NAME, region.region_id, RegionStatus.COMMITTABLE))
    events.append(workflow_state_event(event_id(NODE_NAME, "ready", document.document_id), NODE_NAME, DocumentStatus.DRAFT_READY))
    return events

