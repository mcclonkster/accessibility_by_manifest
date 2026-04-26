from __future__ import annotations

from pdf_accessibility.models.events import NodeEvent, document_pages_event, finding_event, workflow_state_event
from pdf_accessibility.models.state import Confidence, DocumentState, DocumentStatus, Finding, FindingClass
from pdf_accessibility.services.manifest_bridge import load_shared_pdf_events
from pdf_accessibility.utils.ids import event_id, stable_id

NODE_NAME = "ingest_pdf"


def run(document: DocumentState) -> list[NodeEvent]:
    bridge_events = load_shared_pdf_events(document)
    page_count_event = next(
        (
            event
            for event in bridge_events
            if event.event_type.value == document_pages_event("", "", 0).event_type.value
        ),
        None,
    )
    page_count = int(page_count_event.payload.get("page_count", 0)) if page_count_event is not None else 0
    return [
        *bridge_events,
        document_pages_event(event_id(NODE_NAME, document.document_id, page_count), NODE_NAME, page_count),
        finding_event(
            event_id(NODE_NAME, "input", document.document_id),
            NODE_NAME,
            Finding(
                finding_id=f"finding-{stable_id(NODE_NAME, document.document_id)}",
                node_name=NODE_NAME,
                finding_class=FindingClass.EVIDENCE,
                target_ref="document",
                message=f"Input PDF ingested through shared normalization bridge with {page_count} pages.",
                confidence=Confidence.HIGH,
            ),
        ),
        workflow_state_event(
            event_id(NODE_NAME, "workflow", document.document_id),
            NODE_NAME,
            DocumentStatus.EVIDENCE_IN_PROGRESS,
        ),
    ]
