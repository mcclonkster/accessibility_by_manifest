from __future__ import annotations

from pdf_accessibility.models.events import NodeEvent, finding_event
from pdf_accessibility.models.state import Confidence, DocumentState, Finding, FindingClass
from pdf_accessibility.utils.ids import event_id, stable_id

NODE_NAME = "document_consistency"


def run(document: DocumentState) -> list[NodeEvent]:
    return [
        finding_event(
            event_id(NODE_NAME, document.document_id),
            NODE_NAME,
            Finding(
                finding_id=f"finding-{stable_id(NODE_NAME, document.document_id)}",
                node_name=NODE_NAME,
                finding_class=FindingClass.PROPOSED_DECISION,
                target_ref="document",
                message="Document-level consistency checks are scaffolded but not semantic yet.",
                confidence=Confidence.LOW,
            ),
        )
    ]

