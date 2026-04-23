from __future__ import annotations

import re
from typing import Any

from accessibility_by_manifest.normalize.ir import ir_node, normalized_document_ir, review_item


def normalize_docx_manifest_to_ir(manifest: dict[str, Any]) -> dict[str, Any]:
    """Normalize a DOCX evidence manifest into the shared document IR."""

    nodes: list[dict[str, Any]] = []
    tables: list[dict[str, Any]] = []
    reviews: list[dict[str, Any]] = []
    table_index = 0
    reading_order_index = 1

    table_cells_by_table = cells_by_table(manifest.get("table_cell_entries", []))
    for block in manifest.get("body_block_entries", []):
        block_type = block.get("block_type")
        if block_type == "paragraph":
            node, block_reviews = paragraph_node(block, reading_order_index)
            nodes.append(node)
            reviews.extend(block_reviews)
            reading_order_index += 1
        elif block_type == "table":
            table_index += 1
            table_id = f"docx_table_{table_index:04d}"
            table_node, table_entry, table_reviews = table_nodes(block, table_id, table_index, table_cells_by_table, reading_order_index)
            nodes.append(table_node)
            tables.append(table_entry)
            reviews.extend(table_reviews)
            reading_order_index += 1
        elif block_type == "section_properties":
            nodes.append(section_node(block, reading_order_index))
            reading_order_index += 1

    reviews.extend(document_review_items(manifest))
    return normalized_document_ir(
        source_manifest=manifest,
        source_format="DOCX",
        node_entries=nodes,
        table_entries=tables,
        review_entries=dedupe_review_items(reviews),
        notes=[
            "This is a source-neutral normalized document IR derived from the DOCX evidence manifest.",
            "Outputs should read this IR rather than raw DOCX extractor evidence whenever possible.",
            "Raw evidence remains in the DOCX manifest; this view carries normalized structure, confidence, review flags, and projection hints.",
        ],
    )


def paragraph_node(block: dict[str, Any], reading_order_index: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    text = block.get("text") or ""
    style_id = block.get("style_id")
    heading_level = heading_level_from_block(block)
    if heading_level is not None:
        node_type = "heading"
        confidence = "high"
        projection_style = f"Heading {heading_level}"
        basis = ["docx_body_order", "wordprocessingml_paragraph_style"]
        structure = {"heading_level": heading_level, "style_id": style_id}
    elif block.get("numbering"):
        node_type = "list_item"
        confidence = "high"
        projection_style = "List Paragraph"
        basis = ["docx_body_order", "wordprocessingml_numbering"]
        structure = {"list_kind": "numbered_or_bulleted", "numbering": block.get("numbering"), "style_id": style_id}
    elif block.get("drawing_count", 0) > 0 and not text.strip():
        node_type = "figure"
        confidence = "medium"
        projection_style = None
        basis = ["docx_body_order", "wordprocessingml_drawing"]
        structure = {"drawing_count": block.get("drawing_count"), "style_id": style_id}
    elif not text.strip():
        node_type = "artifact"
        confidence = "medium"
        projection_style = None
        basis = ["docx_body_order", "empty_paragraph"]
        structure = {"style_id": style_id}
    else:
        node_type = "paragraph"
        confidence = "high"
        projection_style = "Normal"
        basis = ["docx_body_order", "wordprocessingml_paragraph"]
        structure = {"style_id": style_id}

    node_id = f"docx_block_{int(block.get('block_index') or reading_order_index):06d}"
    reviews = []
    if node_type == "figure":
        reviews.append(
            review_item(
                issue_code="FIGURE_ALT_TEXT_REVIEW",
                severity="review",
                scope="node",
                target_ref=node_id,
                reason="Figure-like DOCX paragraph needs meaningful-vs-decorative and alt-text review.",
                source_refs=source_refs_for_block(block),
                suggested_action="Use reviewed drawing metadata or local vision alt-text evidence before final accessible output.",
            )
        )
    return (
        ir_node(
            node_id=node_id,
            node_type=node_type,
            reading_order_index=reading_order_index,
            source_refs=source_refs_for_block(block),
            content={"text": text},
            structure=structure,
            evidence_basis=basis,
            confidence=confidence,
            review_flags=reviews,
            projection_hints={
                "docx_style": projection_style,
                "projection_status": "omitted" if node_type == "artifact" else "planned",
            },
        ),
        reviews,
    )


def table_nodes(
    block: dict[str, Any],
    table_id: str,
    table_index: int,
    table_cells_by_table: dict[int, list[dict[str, Any]]],
    reading_order_index: int,
) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    cells = table_cells_by_table.get(table_index, [])
    row_entries = table_row_entries(cells)
    header_row_indexes = [row["row_index"] for row in row_entries if row["header_candidate"]]
    confidence = "high" if cells else "medium"
    reviews = []
    if not header_row_indexes:
        reviews.append(
            review_item(
                issue_code="TABLE_HEADERS_UNCERTAIN",
                severity="review",
                scope="table",
                target_ref=table_id,
                reason="DOCX table was detected, but no strong header-row signal was found.",
                source_refs=source_refs_for_block(block),
                suggested_action="Confirm header rows and column relationships before final accessible output.",
            )
        )
    table_entry = {
        "table_id": table_id,
        "source_refs": source_refs_for_block(block),
        "row_count": block.get("row_count"),
        "cell_count": block.get("cell_count"),
        "grid_column_count": block.get("grid_column_count"),
        "row_entries": row_entries,
        "header_candidate_row_indexes": header_row_indexes,
        "confidence": confidence,
        "evidence_basis": ["docx_body_order", "wordprocessingml_table", "python_docx_table_cells"],
        "review_flags": reviews,
    }
    node = ir_node(
        node_id=table_id,
        node_type="table",
        reading_order_index=reading_order_index,
        source_refs=source_refs_for_block(block),
        content={"text_sample": block.get("text_sample", [])},
        structure={
            "table_id": table_id,
            "row_count": block.get("row_count"),
            "cell_count": block.get("cell_count"),
            "grid_column_count": block.get("grid_column_count"),
        },
        evidence_basis=["docx_body_order", "wordprocessingml_table"],
        confidence=confidence,
        review_flags=reviews,
        projection_hints={"docx_style": "Table Grid", "projection_status": "planned"},
    )
    return node, table_entry, reviews


def section_node(block: dict[str, Any], reading_order_index: int) -> dict[str, Any]:
    node_id = f"docx_section_{int(block.get('block_index') or reading_order_index):06d}"
    return ir_node(
        node_id=node_id,
        node_type="section",
        reading_order_index=reading_order_index,
        source_refs=source_refs_for_block(block),
        content={},
        structure={
            "section_type": block.get("section_type"),
            "page_width_twips": block.get("page_width_twips"),
            "page_height_twips": block.get("page_height_twips"),
            "orientation": block.get("orientation"),
            "margins_twips": {
                "top": block.get("top_margin_twips"),
                "bottom": block.get("bottom_margin_twips"),
                "left": block.get("left_margin_twips"),
                "right": block.get("right_margin_twips"),
            },
        },
        evidence_basis=["docx_body_order", "wordprocessingml_section_properties"],
        confidence="high",
        projection_hints={"projection_status": "preserve"},
    )


def table_row_entries(cells: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: dict[int, list[dict[str, Any]]] = {}
    for cell in cells:
        rows.setdefault(int(cell.get("row_index") or 0), []).append(cell)
    entries = []
    for row_index, row_cells in sorted(rows.items()):
        row_cells = sorted(row_cells, key=lambda cell: int(cell.get("column_index") or 0))
        entries.append(
            {
                "row_index": row_index,
                "cell_entries": [
                    {
                        "column_index": int(cell.get("column_index") or 0),
                        "text": cell.get("text") or "",
                        "paragraph_count": cell.get("paragraph_count"),
                        "nested_table_count": cell.get("nested_table_count"),
                    }
                    for cell in row_cells
                ],
                "header_candidate": row_index == 1 and row_looks_like_header(row_cells),
                "confidence": "medium" if row_cells else "low",
            }
        )
    return entries


def row_looks_like_header(cells: list[dict[str, Any]]) -> bool:
    text = " ".join((cell.get("text") or "").strip() for cell in cells).strip()
    if not text:
        return False
    tokens = text.split()
    numeric_tokens = [token for token in tokens if token.strip("$,().%").isdigit()]
    return len(numeric_tokens) <= max(1, len(tokens) // 3)


def cells_by_table(cells: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
    by_table: dict[int, list[dict[str, Any]]] = {}
    for cell in cells:
        by_table.setdefault(int(cell.get("table_index") or 0), []).append(cell)
    return by_table


def heading_level_from_block(block: dict[str, Any]) -> int | None:
    outline_level = parse_int(block.get("outline_level"))
    if outline_level is not None:
        return max(1, min(outline_level + 1, 9))
    style_id = block.get("style_id") or ""
    match = re.search(r"heading\s*([1-9])|Heading([1-9])", style_id, re.IGNORECASE)
    if match:
        return int(next(value for value in match.groups() if value))
    return None


def parse_int(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def source_refs_for_block(block: dict[str, Any]) -> list[str]:
    block_index = block.get("block_index")
    refs = [f"body_block:{block_index}" if block_index is not None else None]
    raw_hash = block.get("raw_xml_sha256")
    if raw_hash:
        refs.append(f"raw_xml_sha256:{raw_hash}")
    return [ref for ref in refs if ref]


def document_review_items(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    reviews = []
    metadata = manifest.get("document_metadata", {})
    style_evidence = manifest.get("style_evidence", {})
    if not metadata.get("title"):
        reviews.append(
            review_item(
                issue_code="DOCUMENT_TITLE_MISSING",
                severity="warning",
                scope="document",
                target_ref="document.title",
                reason="DOCX core title is empty.",
                source_refs=["document_metadata.title"],
                suggested_action="Set a document title before final accessible output.",
            )
        )
    if not metadata.get("language") and not style_evidence.get("document_default_language"):
        reviews.append(
            review_item(
                issue_code="DOCUMENT_LANGUAGE_MISSING",
                severity="warning",
                scope="document",
                target_ref="document.language",
                reason="DOCX language is not declared in core metadata or style defaults.",
                source_refs=["document_metadata.language", "style_evidence.document_default_language"],
                suggested_action="Set the document language before final accessible output.",
            )
        )
    if manifest.get("document_summary", {}).get("drawing_count", 0) > manifest.get("document_summary", {}).get("drawing_with_alt_text_count", 0):
        reviews.append(
            review_item(
                issue_code="DRAWING_ALT_TEXT_INCOMPLETE",
                severity="review",
                scope="document",
                target_ref="drawing_entries",
                reason="Some DOCX drawings do not expose title or description attributes.",
                source_refs=["drawing_entries"],
                suggested_action="Apply reviewed alt text before final accessible output.",
            )
        )
    return reviews


def dedupe_review_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen = set()
    deduped = []
    for item in items:
        key = (item.get("issue_code"), item.get("scope"), item.get("target_ref"), item.get("reason"))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)
    return deduped
