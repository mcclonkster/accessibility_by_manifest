from __future__ import annotations

from pdf_accessibility.models.events import (
    NodeEvent,
    normalized_structure_event,
    region_status_event,
    review_task_event,
    workflow_state_event,
)
from pdf_accessibility.models.state import (
    Confidence,
    DocumentState,
    DocumentStatus,
    NormalizedUnit,
    RegionState,
    RegionStatus,
    ReviewTask,
)
from pdf_accessibility.utils.ids import event_id, stable_id

NODE_NAME = "accessibility_review"


def run(document: DocumentState) -> list[NodeEvent]:
    events: list[NodeEvent] = []
    normalized_units: list[NormalizedUnit] = []
    text_by_ref = {
        block.source_ref: block.text
        for page in document.pages
        for block in page.text_blocks
    }
    page_text_counts = {page.page_number: len(page.text_blocks) for page in document.pages}
    page_sizes = {
        page.page_number: (page.geometry.width, page.geometry.height)
        for page in document.pages
        if page.geometry is not None
    }
    order = 0
    for page in document.pages:
        for region in page.regions:
            events.append(region_status_event(event_id(NODE_NAME, region.region_id), NODE_NAME, region.region_id, RegionStatus.MEANING_INFERRED))
            events.append(region_status_event(event_id(NODE_NAME, region.region_id, "review"), NODE_NAME, region.region_id, RegionStatus.ACCESSIBILITY_REVIEWED))
            normalized_units.append(_normalized_unit(region, text_by_ref, order))
            order += 1
            if region.current_role == "figure_candidate":
                events.append(_figure_review_event(region, page_text_counts, page_sizes))
            elif region.current_role == "table_candidate":
                events.append(_table_review_event(region, text_by_ref))
            elif region.current_role == "unknown":
                events.append(_review_task_event("UNKNOWN_REGION_REVIEW", region.region_id, "Region has insufficient evidence for an accessibility role."))
    if normalized_units:
        events.append(normalized_structure_event(event_id(NODE_NAME, "normalized", document.document_id), NODE_NAME, normalized_units))
    events.extend(_document_review_tasks(document, normalized_units))
    events.append(workflow_state_event(event_id(NODE_NAME, "workflow", document.document_id), NODE_NAME, DocumentStatus.PLANNING_IN_PROGRESS))
    return events


def _normalized_unit(region: RegionState, text_by_ref: dict[str, str], order: int) -> NormalizedUnit:
    unit_type = _unit_type(region.current_role)
    text = "\n".join(text_by_ref[source_ref] for source_ref in region.source_refs if source_ref in text_by_ref) or None
    return NormalizedUnit(
        unit_id=f"unit-{stable_id(region.region_id)}",
        unit_type=unit_type,
        page_numbers=[region.page_number],
        bbox=region.bbox,
        text=text,
        source_refs=region.source_refs,
        evidence_basis=region.evidence_basis,
        confidence=region.confidence,
        reading_order_index=order,
        needs_review=region.confidence is Confidence.LOW or unit_type in {"table", "figure", "unknown"},
    )


def _unit_type(role: str | None) -> str:
    if role == "heading_candidate":
        return "heading"
    if role == "table_candidate":
        return "table"
    if role == "figure_candidate":
        return "figure"
    if role == "page_number_or_footer_candidate":
        return "artifact"
    if role == "paragraph_candidate":
        return "paragraph"
    return "unknown"


def _document_review_tasks(document: DocumentState, normalized_units: list[NormalizedUnit]) -> list[NodeEvent]:
    events: list[NodeEvent] = []
    if document.metadata is None or not document.metadata.title:
        events.append(
            _review_task_event(
                "DOCUMENT_TITLE_MISSING",
                "document",
                "Document title is missing or empty.",
                suggested_action="Set a trustworthy document title before final output.",
            )
        )
    if document.metadata is None or not document.metadata.primary_language:
        events.append(
            _review_task_event(
                "DOCUMENT_LANGUAGE_MISSING",
                "document",
                "Primary document language is missing.",
                suggested_action="Set the document primary language, for example en-US.",
            )
        )
    if not any(unit.unit_type == "heading" for unit in normalized_units):
        events.append(
            _review_task_event(
                "HEADING_STRUCTURE_REVIEW",
                "document",
                "No existing heading structure was available before this pass; inferred headings need review.",
                blocking=False,
                suggested_action="Review inferred heading candidates before claiming final accessibility.",
            )
        )
    return events


def _table_review_event(region: RegionState, text_by_ref: dict[str, str]) -> NodeEvent:
    text = "\n".join(text_by_ref[source_ref] for source_ref in region.source_refs if source_ref in text_by_ref)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    numeric_lines = sum(any(char.isdigit() for char in line) for line in lines)
    likely_complex = len(lines) >= 8 and numeric_lines >= 5
    return _review_task_event(
        "TABLE_HEADERS_UNCERTAIN" if likely_complex else "TABLE_STRUCTURE_SPOT_CHECK",
        region.region_id,
        (
            "Table candidate needs header and cell relationship review."
            if likely_complex
            else "Simple table candidate should be spot-checked before final accessibility claims."
        ),
        blocking=likely_complex,
        suggested_action="Review table boundaries, header rows, and reading order.",
        confidence_context={
            "line_count": len(lines),
            "numeric_line_count": numeric_lines,
            "blocking_threshold": "line_count >= 8 and numeric_line_count >= 5",
        },
    )


def _figure_review_event(
    region: RegionState,
    page_text_counts: dict[int, int],
    page_sizes: dict[int, tuple[float, float]],
) -> NodeEvent:
    page_width, page_height = page_sizes.get(region.page_number, (0.0, 0.0))
    page_area = page_width * page_height
    region_area = 0.0
    if region.bbox is not None:
        region_area = max(0.0, region.bbox.right - region.bbox.left) * max(0.0, region.bbox.bottom - region.bbox.top)
    area_ratio = region_area / page_area if page_area else 0.0
    image_only_page = page_text_counts.get(region.page_number, 0) == 0
    likely_meaningful = image_only_page or area_ratio >= 0.10
    return _review_task_event(
        "FIGURE_ALT_TEXT_REQUIRED" if likely_meaningful else "FIGURE_ALT_TEXT_SPOT_CHECK",
        region.region_id,
        (
            "Meaningful figure candidate needs trusted alt text before accessible finalization."
            if likely_meaningful
            else "Small figure candidate should be spot-checked for decorative versus meaningful status."
        ),
        blocking=likely_meaningful,
        suggested_action="Confirm whether the figure is meaningful; provide alt text or mark decorative.",
        confidence_context={
            "image_only_page": image_only_page,
            "page_area_ratio": round(area_ratio, 4),
            "blocking_threshold": "image-only page or image area >= 10% of page area",
        },
    )


def _review_task_event(
    issue_code: str,
    target_ref: str,
    reason: str,
    *,
    blocking: bool = True,
    suggested_action: str | None = None,
    confidence_context: dict[str, object] | None = None,
) -> NodeEvent:
    task = ReviewTask(
        task_id=f"review-{stable_id(issue_code, target_ref)}",
        issue_code=issue_code,
        severity="error" if blocking else "warning",
        target_ref=target_ref,
        reason=reason,
        blocking=blocking,
        suggested_action=suggested_action,
        confidence_context=confidence_context or {},
    )
    return review_task_event(event_id(NODE_NAME, issue_code, target_ref), NODE_NAME, task)
