from __future__ import annotations

import json
from pathlib import Path

from pdf_accessibility.models.events import (
    EventType,
    NodeEvent,
    artifact_record,
    artifact_registration_event,
    finding_event,
    normalized_structure_event,
    page_evidence_event,
    region_discovery_event,
)
from pdf_accessibility.models.state import (
    BBox,
    Confidence,
    DocumentState,
    Finding,
    FindingClass,
    NormalizedUnit,
    RegionState,
    RegionStatus,
    TextBlockEvidence,
)
from pdf_accessibility.utils.ids import event_id, stable_id

NODE_NAME = "ocr_layout_analysis"


def run(document: DocumentState) -> list[NodeEvent]:
    recoveries = _load_ocr_recoveries(document.run_dir / "ocr_recovery_input.json")
    if not recoveries:
        return []

    events: list[NodeEvent] = []
    input_path = document.run_dir / "ocr_recovery_input.json"
    if input_path.exists():
        events.append(
            artifact_registration_event(
                event_id(NODE_NAME, "artifact", document.document_id),
                NODE_NAME,
                artifact_record(
                    artifact_id=f"artifact-{stable_id(NODE_NAME, input_path)}",
                    name="ocr_recovery_input.json",
                    path=input_path,
                    artifact_type="ocr_recovery_input",
                    producer_node=NODE_NAME,
                    metadata={"page_recovery_count": len(recoveries)},
                ),
            )
        )

    recovered_units: list[NormalizedUnit] = []
    recovered_regions: list[RegionState] = []
    existing_page_blocks = {page.page_number: list(page.text_blocks) for page in document.pages}
    next_index = _next_reading_order_index(document)

    for offset, recovery in enumerate(recoveries):
        page_number = recovery["page_number"]
        text = recovery["text"]
        source_ref = f"ocr_recovery:page:{page_number}"
        page = next((page for page in document.pages if page.page_number == page_number), None)
        bbox = _page_bbox(page)
        block_id = f"ocr-recovery-{stable_id(document.document_id, page_number, text[:80])}"
        recovered_block = TextBlockEvidence(
            block_id=block_id,
            page_number=page_number,
            bbox=bbox or BBox(left=0.0, top=0.0, right=0.0, bottom=0.0),
            text=text,
            source_ref=source_ref,
            extractor="manual_ocr_recovery",
        )
        merged_blocks = [*existing_page_blocks.get(page_number, []), recovered_block]
        events.append(
            page_evidence_event(
                event_id(NODE_NAME, "page", page_number, document.document_id),
                NODE_NAME,
                page_number,
                geometry=page.geometry if page is not None else None,
                text_blocks=merged_blocks,
                images=page.images if page is not None else [],
                links=page.links if page is not None else [],
                annotations=page.annotations if page is not None else [],
                font_names=page.font_names if page is not None else [],
            )
        )
        recovered_units.append(
            NormalizedUnit(
                unit_id=f"ocr-unit-{stable_id(document.document_id, page_number)}",
                unit_type="paragraph",
                page_numbers=[page_number],
                bbox=bbox,
                text=text,
                source_refs=[source_ref],
                evidence_basis=["manual_ocr_recovery", "image_only_page", "human_supplied_text"],
                confidence=Confidence.MEDIUM,
                reading_order_index=next_index + offset,
                needs_review=True,
            )
        )
        recovered_regions.append(
            RegionState(
                region_id=f"ocr-region-{stable_id(document.document_id, page_number)}",
                page_number=page_number,
                bbox=bbox,
                status=RegionStatus.STRUCTURE_PLANNED,
                current_role="paragraph_candidate",
                confidence=Confidence.MEDIUM,
                source_refs=[source_ref],
                evidence_basis=["manual_ocr_recovery", "image_only_page", "human_supplied_text"],
            )
        )
        events.append(
            finding_event(
                event_id(NODE_NAME, "recovery", page_number, document.document_id),
                NODE_NAME,
                Finding(
                    finding_id=f"finding-{stable_id(NODE_NAME, page_number, source_ref)}",
                    node_name=NODE_NAME,
                    finding_class=FindingClass.EVIDENCE,
                    target_ref=f"page:{page_number}",
                    message="Manual OCR recovery text was supplied for an image-only page.",
                    confidence=Confidence.MEDIUM,
                    payload={
                        "page_number": page_number,
                        "source_ref": source_ref,
                        "recovery_method": "manual_ocr_recovery",
                    },
                ),
            )
        )
        matching_tasks = [
            task
            for task in document.review_tasks
            if task.issue_code == "IMAGE_ONLY_PAGE_OCR_REQUIRED"
            and task.target_ref == f"page:{page_number}"
            and not task.resolved
        ]
        for task in matching_tasks:
            events.append(
                NodeEvent(
                    event_id=event_id(NODE_NAME, "resolve", task.task_id),
                    node_name=NODE_NAME,
                    event_type=EventType.REVIEW_RESOLUTION,
                    review_task_id=task.task_id,
                )
            )

    if recovered_regions:
        events.append(
            region_discovery_event(
                event_id(NODE_NAME, "regions", document.document_id),
                NODE_NAME,
                recovered_regions,
            )
        )
    if recovered_units:
        events.append(
            normalized_structure_event(
                event_id(NODE_NAME, "normalized", document.document_id),
                NODE_NAME,
                recovered_units,
            )
        )
    return events


def _load_ocr_recoveries(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    if isinstance(raw, dict):
        raw = raw.get("page_recoveries")
    if not isinstance(raw, list):
        return []

    recoveries: list[dict[str, object]] = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        page_number = item.get("page_number")
        text = item.get("text")
        if not isinstance(page_number, int) or page_number <= 0:
            continue
        if not isinstance(text, str) or not text.strip():
            continue
        recoveries.append({"page_number": page_number, "text": text.strip()})
    return recoveries


def _page_bbox(page) -> BBox | None:
    if page is None or page.geometry is None:
        return None
    return BBox(left=0.0, top=0.0, right=page.geometry.width, bottom=page.geometry.height)


def _next_reading_order_index(document: DocumentState) -> int:
    current = [unit.reading_order_index for unit in document.normalized_units if unit.reading_order_index is not None]
    return (max(current) + 1) if current else 0
