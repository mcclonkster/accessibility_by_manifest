from __future__ import annotations

from pdf_accessibility.models.events import NodeEvent
from pdf_accessibility.models.state import DocumentState

NODE_NAME = "vision_analysis"


def run(document: DocumentState) -> list[NodeEvent]:
    return []

