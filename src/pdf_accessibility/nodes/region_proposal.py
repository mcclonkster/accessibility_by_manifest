from __future__ import annotations

from pdf_accessibility.models.events import NodeEvent, region_discovery_event
from pdf_accessibility.models.state import Confidence, DocumentState, RegionState, RegionStatus, TextBlockEvidence
from pdf_accessibility.utils.ids import event_id

NODE_NAME = "region_proposal"


def run(document: DocumentState) -> list[NodeEvent]:
    regions: list[RegionState] = []
    for page in document.pages:
        if page.regions:
            continue
        median_font_size = _median_font_size(page.text_blocks)
        for block in page.text_blocks:
            role, confidence, basis = _role_for_text_block(block, median_font_size)
            regions.append(
                RegionState(
                    region_id=f"region-{block.block_id}",
                    page_number=page.page_number,
                    bbox=block.bbox,
                    status=RegionStatus.EVIDENCE_COLLECTED,
                    current_role=role,
                    confidence=confidence,
                    source_refs=[block.source_ref],
                    evidence_basis=basis,
                )
            )
        for image in page.images:
            regions.append(
                RegionState(
                    region_id=f"region-{image.image_id}",
                    page_number=page.page_number,
                    bbox=image.bbox,
                    status=RegionStatus.EVIDENCE_COLLECTED,
                    current_role="figure_candidate",
                    confidence=Confidence.MEDIUM,
                    source_refs=[image.source_ref],
                    evidence_basis=["pymupdf image block"],
                )
            )
        if not page.text_blocks and not page.images:
            regions.append(
                RegionState(
                    region_id=f"page-{page.page_number}-empty",
                    page_number=page.page_number,
                    status=RegionStatus.EVIDENCE_COLLECTED,
                    current_role="unknown",
                    confidence=Confidence.LOW,
                    evidence_basis=["no text or image evidence extracted"],
                )
            )
    if not regions:
        return []
    return [region_discovery_event(event_id(NODE_NAME, document.document_id, len(regions)), NODE_NAME, regions)]


def _role_for_text_block(block: TextBlockEvidence, median_font_size: float | None) -> tuple[str, Confidence, list[str]]:
    text = block.text.strip()
    line_count = len([line for line in text.splitlines() if line.strip()])
    max_size = max(block.font_sizes) if block.font_sizes else None
    basis = ["pymupdf text block"]
    if _looks_like_table(text):
        return "table_candidate", Confidence.MEDIUM, basis + ["dense numeric/aligned text pattern"]
    if max_size and median_font_size and max_size >= median_font_size * 1.18 and line_count <= 2 and len(text) <= 140:
        return "heading_candidate", Confidence.MEDIUM, basis + ["font size above page median", "short isolated text block"]
    if line_count == 1 and len(text) <= 20 and any(char.isdigit() for char in text):
        return "page_number_or_footer_candidate", Confidence.LOW, basis + ["short numeric text"]
    return "paragraph_candidate", Confidence.MEDIUM, basis


def _median_font_size(blocks: list[TextBlockEvidence]) -> float | None:
    sizes = sorted(size for block in blocks for size in block.font_sizes)
    if not sizes:
        return None
    return sizes[len(sizes) // 2]


def _looks_like_table(text: str) -> bool:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) < 3:
        return False
    numeric_lines = sum(any(char.isdigit() for char in line) for line in lines)
    money_or_percent_lines = sum("$" in line or "%" in line for line in lines)
    spaced_lines = sum("  " in line or "\t" in line for line in lines)
    if numeric_lines >= 5 and len(lines) >= 6:
        return True
    if numeric_lines >= 3 and money_or_percent_lines >= 2:
        return True
    return numeric_lines >= 3 and spaced_lines >= 3
