from __future__ import annotations

from pdf_accessibility.models.events import NodeEvent, finding_event
from pdf_accessibility.models.state import Confidence, DocumentState, Finding, FindingClass
from pdf_accessibility.utils.ids import event_id, stable_id

NODE_NAME = "render_pages"


def run(document: DocumentState) -> list[NodeEvent]:
    return [
        finding_event(
            event_id(NODE_NAME, "stub", document.document_id),
            NODE_NAME,
            Finding(
                finding_id=f"finding-{stable_id(NODE_NAME, document.document_id)}",
                node_name=NODE_NAME,
                finding_class=FindingClass.EVIDENCE,
                target_ref="document",
                message="Page rendering placeholder recorded; image rendering service is not implemented in this scaffold.",
                confidence=Confidence.MEDIUM,
            ),
        )
    ]

