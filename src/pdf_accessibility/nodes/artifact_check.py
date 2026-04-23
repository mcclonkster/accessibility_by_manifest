from __future__ import annotations

from collections import Counter, defaultdict

from pdf_accessibility.models.events import NodeEvent, finding_event, normalized_structure_event
from pdf_accessibility.models.state import Confidence, DocumentState, Finding, FindingClass, NormalizedUnit, TextBlockEvidence
from pdf_accessibility.utils.ids import event_id, stable_id

NODE_NAME = "artifact_check"


def run(document: DocumentState) -> list[NodeEvent]:
    repeated = _repeated_header_footer_blocks(document)
    events: list[NodeEvent] = [
        finding_event(
            event_id(NODE_NAME, document.document_id),
            NODE_NAME,
            Finding(
                finding_id=f"finding-{stable_id(NODE_NAME, document.document_id)}",
                node_name=NODE_NAME,
                finding_class=FindingClass.PROPOSED_DECISION,
                target_ref="document",
                message=f"Detected {len(repeated)} repeated header/footer/page-number artifact candidates.",
                confidence=Confidence.MEDIUM,
                payload={"artifact_candidate_count": len(repeated)},
            ),
        )
    ]
    if repeated:
        units = [
            NormalizedUnit(
                unit_id=f"unit-{stable_id(f'region-{block.block_id}')}",
                unit_type="artifact",
                page_numbers=[block.page_number],
                bbox=block.bbox,
                text=block.text,
                source_refs=[block.source_ref],
                evidence_basis=["repeated text in page header/footer band"],
                confidence=Confidence.MEDIUM,
                reading_order_index=None,
                needs_review=False,
            )
            for block in repeated
        ]
        events.append(normalized_structure_event(event_id(NODE_NAME, "artifacts", document.document_id), NODE_NAME, units))
    return events


def _repeated_header_footer_blocks(document: DocumentState) -> list[TextBlockEvidence]:
    candidates_by_text: dict[str, list[TextBlockEvidence]] = defaultdict(list)
    for page in document.pages:
        height = page.geometry.height if page.geometry else None
        if height is None:
            continue
        for block in page.text_blocks:
            text_key = " ".join(block.text.split()).lower()
            if not text_key or len(text_key) > 140:
                continue
            in_header = block.bbox.top <= height * 0.12
            in_footer = block.bbox.bottom >= height * 0.88
            if in_header or in_footer:
                candidates_by_text[text_key].append(block)
    page_threshold = max(2, min(4, document.page_count // 3 if document.page_count else 2))
    repeated_texts = {
        text
        for text, blocks in candidates_by_text.items()
        if len({block.page_number for block in blocks}) >= page_threshold
    }
    short_page_numbers = [
        block
        for blocks in candidates_by_text.values()
        for block in blocks
        if _looks_like_page_number(block.text)
    ]
    repeated = [block for text in repeated_texts for block in candidates_by_text[text]]
    counts = Counter(block.source_ref for block in repeated + short_page_numbers)
    return [block for block in repeated + short_page_numbers if counts[block.source_ref] >= 1]


def _looks_like_page_number(text: str) -> bool:
    normalized = text.strip().lower().removeprefix("page").strip()
    return normalized.isdigit() and len(normalized) <= 4
