from __future__ import annotations

from pdf_accessibility.models.events import NodeEvent, region_status_event
from pdf_accessibility.models.state import DocumentState, RegionStatus
from pdf_accessibility.utils.ids import event_id

NODE_NAME = "tagging_plan"


def run(document: DocumentState) -> list[NodeEvent]:
    return [
        region_status_event(event_id(NODE_NAME, region.region_id), NODE_NAME, region.region_id, RegionStatus.STRUCTURE_PLANNED)
        for page in document.pages
        for region in page.regions
    ]

