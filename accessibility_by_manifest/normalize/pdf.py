from __future__ import annotations

from statistics import median
from typing import Any


def normalize_pdf_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    """Populate v0.1 normalized blocks without mutating raw evidence."""

    raw_blocks = selected_raw_blocks(manifest.get("raw_block_entries", []))
    font_baseline = median_font_size(raw_blocks)
    repeated_artifacts = repeated_artifact_texts(raw_blocks)
    page_profiles = profile_pages(manifest, raw_blocks)
    normalized_blocks = []
    for reading_order_index, raw_block in enumerate(sort_blocks_for_reading(raw_blocks), start=1):
        page_profile = page_profiles.get(int(raw_block.get("page_number") or 0), {})
        role, heading_level, confidence, role_basis = interpret_block_role(raw_block, font_baseline, repeated_artifacts, page_profile)
        block_warnings = normalization_warnings(raw_block, role, confidence)
        normalized_blocks.append(
            {
                "block_id": f"n_{raw_block['block_id']}",
                "page_span": [raw_block["page_number"], raw_block["page_number"]],
                "observed_source_refs": observed_source_refs(raw_block),
                "normalized_workflow": {
                    "interpreted_role": role,
                    "heading_level": heading_level,
                    "list_kind": list_kind_for_role(role, raw_block),
                    "role_confidence": confidence,
                    "semantic_source_quality": semantic_source_quality(raw_block),
                    "role_basis": role_basis,
                    "reading_order_index": reading_order_index,
                    "reading_order_basis": ["page_number", "bbox_top", "bbox_left", "extractor_block_order"],
                    "manual_review_required": bool(block_warnings),
                },
                "warning_entries": block_warnings,
                "projected_target": projected_target_for_role(role, raw_block),
            }
        )
    normalized_table_entries = assign_table_regions(normalized_blocks, raw_blocks)
    manifest["normalized_block_entries"] = normalized_blocks
    manifest["normalized_table_entries"] = normalized_table_entries
    manifest["document_summary"]["normalized_block_count"] = len(normalized_blocks)
    manifest["document_summary"]["pages_with_warnings"] = pages_with_warnings(manifest)
    if normalized_blocks:
        manifest["document_accessibility"]["reading_order_source"] = reading_order_source(manifest)
    return manifest


def selected_raw_blocks(raw_blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    pymupdf_blocks = [block for block in raw_blocks if "pymupdf" in block.get("extractor_evidence", {})]
    if pymupdf_blocks:
        pymupdf_pages = {int(block.get("page_number") or 0) for block in pymupdf_blocks}
        sidecar_fallback_blocks = [
            block
            for block in raw_blocks
            if sidecar_recovery_present(block) and int(block.get("page_number") or 0) not in pymupdf_pages
        ]
        return [*pymupdf_blocks, *sidecar_fallback_blocks]
    return [block for block in raw_blocks if block.get("text", "").strip()]


def sort_blocks_for_reading(raw_blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(raw_blocks, key=lambda block: (block.get("page_number") or 0, bbox_top(block), bbox_left(block), block.get("block_id", "")))


def median_font_size(raw_blocks: list[dict[str, Any]]) -> float | None:
    sizes = []
    for block in raw_blocks:
        font_size = block.get("style_hints", {}).get("font_size")
        if isinstance(font_size, (int, float)) and font_size > 0:
            sizes.append(float(font_size))
    return float(median(sizes)) if sizes else None


def profile_pages(manifest: dict[str, Any], raw_blocks: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    blocks_by_page: dict[int, list[dict[str, Any]]] = {}
    for block in raw_blocks:
        blocks_by_page.setdefault(int(block.get("page_number") or 0), []).append(block)

    profiles: dict[int, dict[str, Any]] = {}
    for page in manifest.get("page_entries", []):
        page_number = int(page.get("page_number") or 0)
        page_blocks = blocks_by_page.get(page_number, [])
        page_text = "\n".join(block.get("text", "") for block in page_blocks).lower()
        observed = page.get("observed_source", {})
        table_score = table_density_score(page_blocks)
        if observed.get("image_only_page_suspected"):
            page_type = "image_only"
        elif page_number == 1:
            page_type = "cover"
        elif "table of contents" in page_text[:1200]:
            page_type = "table_of_contents"
        elif table_score >= 0.45:
            page_type = "table_heavy"
        elif any(token in page_text[:1600] for token in ("schedule", "statement of", "notes to financial statements")):
            page_type = "mixed"
        else:
            page_type = "narrative"
        profiles[page_number] = {
            "page_type": page_type,
            "table_density_score": table_score,
            "block_count": len(page_blocks),
        }
    return profiles


def table_density_score(raw_blocks: list[dict[str, Any]]) -> float:
    if not raw_blocks:
        return 0.0
    table_like = sum(1 for block in raw_blocks if table_like_text(block.get("text", "")) or is_short_grid_fragment(block))
    return table_like / len(raw_blocks)


def table_like_text(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    chars = [char for char in stripped if not char.isspace()]
    if not chars:
        return False
    digit_count = sum(1 for char in chars if char.isdigit())
    currency_or_paren = any(char in stripped for char in "$(),.%")
    return digit_count / len(chars) >= 0.25 or currency_or_paren and digit_count > 0


def is_short_grid_fragment(raw_block: dict[str, Any]) -> bool:
    text = raw_block.get("text", "").strip()
    bbox = raw_block.get("bbox") or []
    if not text or len(text) > 80 or len(bbox) != 4:
        return False
    width = float(bbox[2]) - float(bbox[0]) if bbox[0] is not None and bbox[2] is not None else 999.0
    return width <= 220.0


def interpret_block_role(
    raw_block: dict[str, Any],
    font_baseline: float | None,
    repeated_artifacts: set[str],
    page_profile: dict[str, Any],
) -> tuple[str, int | None, str, list[str]]:
    text = raw_block.get("text", "").strip()
    style_hints = raw_block.get("style_hints", {})
    font_size = style_hints.get("font_size")
    font_weight = style_hints.get("font_weight")
    basis = ["raw_text_block"]
    doctr_role = doctr_interpreted_role(raw_block)
    if doctr_role is not None:
        role, heading_level, confidence, role_basis = doctr_role
        return role, heading_level, confidence, basis + role_basis
    docling_role = docling_interpreted_role(raw_block)
    if docling_role is not None:
        role, heading_level, confidence, role_basis = docling_role
        return role, heading_level, confidence, basis + role_basis
    if normalized_text_key(text) in repeated_artifacts and is_margin_region(raw_block):
        return "artifact", None, "medium", basis + ["repeated_header_footer_pattern"]
    if is_list_item(text):
        return "list_item", None, "medium", basis + ["list_marker_pattern"]
    if is_table_cell_candidate(raw_block, page_profile):
        return "table_cell", None, "medium", basis + [f"page_type:{page_profile.get('page_type')}", "table_density_or_numeric_alignment"]
    if is_heading_candidate(raw_block, font_size, font_baseline, font_weight, page_profile):
        level = 1 if raw_block.get("page_number") == 1 or is_large_heading(font_size, font_baseline) else 2
        confidence = "medium" if font_baseline else "low"
        return "heading", level, confidence, basis + ["font_or_text_heading_heuristic"]
    if text:
        return "paragraph", None, "medium", basis + ["text_block_continuity_pending"]
    return "unknown", None, "low", basis + ["empty_or_unclassified_text"]


def repeated_artifact_texts(raw_blocks: list[dict[str, Any]]) -> set[str]:
    pages_by_text: dict[str, set[int]] = {}
    for block in raw_blocks:
        key = normalized_text_key(block.get("text", ""))
        if not key or len(key) < 4:
            continue
        pages_by_text.setdefault(key, set()).add(int(block.get("page_number") or 0))
    return {key for key, pages in pages_by_text.items() if len(pages) >= 3}


def normalized_text_key(text: str) -> str:
    return " ".join(text.lower().split())


def is_margin_region(raw_block: dict[str, Any]) -> bool:
    bbox = raw_block.get("bbox") or []
    if len(bbox) != 4 or bbox[1] is None or bbox[3] is None:
        return False
    top = float(bbox[1])
    bottom = float(bbox[3])
    return top <= 90.0 or bottom >= 720.0


def is_table_cell_candidate(raw_block: dict[str, Any], page_profile: dict[str, Any]) -> bool:
    page_type = page_profile.get("page_type")
    if page_type not in {"table_heavy", "mixed"}:
        return False
    if is_margin_region(raw_block):
        return False
    text = raw_block.get("text", "").strip()
    if not text:
        return False
    if page_type == "mixed" and not table_like_text(text):
        return False
    return table_like_text(text) or is_short_grid_fragment(raw_block)


def is_heading_candidate(raw_block: dict[str, Any], font_size: Any, font_baseline: float | None, font_weight: Any, page_profile: dict[str, Any]) -> bool:
    text = raw_block.get("text", "").strip()
    if not text or len(text) > 140 or "\n" in text and len(text) > 80:
        return False
    if page_profile.get("page_type") == "table_heavy" and not near_top_of_main_region(raw_block):
        return False
    if is_large_heading(font_size, font_baseline):
        return True
    if font_weight == "bold" and len(text) <= 100 and page_profile.get("page_type") != "table_heavy":
        return True
    letters = [char for char in text if char.isalpha()]
    return (
        len(letters) >= 4
        and sum(1 for char in letters if char.isupper()) / len(letters) > 0.8
        and len(text) <= 100
        and not table_like_text(text)
    )


def near_top_of_main_region(raw_block: dict[str, Any]) -> bool:
    bbox = raw_block.get("bbox") or []
    if len(bbox) != 4 or bbox[1] is None:
        return False
    return float(bbox[1]) <= 180.0


def is_large_heading(font_size: Any, font_baseline: float | None) -> bool:
    return isinstance(font_size, (int, float)) and font_baseline is not None and float(font_size) >= font_baseline + 2.0


def is_list_item(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    bullet_markers = ("-", "*", "\u2022", "\u25e6")
    if stripped.startswith(bullet_markers):
        return True
    prefix = stripped.split(maxsplit=1)[0].rstrip(".)")
    return prefix.isdigit() and len(prefix) <= 3


def list_kind_for_role(role: str, raw_block: dict[str, Any]) -> str | None:
    if role != "list_item":
        return None
    text = raw_block.get("text", "").strip()
    return "number" if text[:1].isdigit() else "bullet"


def semantic_source_quality(raw_block: dict[str, Any]) -> str:
    structure = raw_block.get("structure_hints", {})
    if structure.get("tag_name") or structure.get("mcid") is not None:
        if sidecar_recovery_present(raw_block):
            return "low"
        return "high"
    if "pymupdf" in raw_block.get("extractor_evidence", {}) or "pdfminer.six" in raw_block.get("extractor_evidence", {}):
        return "low"
    return "unknown"


def sidecar_recovery_present(raw_block: dict[str, Any]) -> bool:
    evidence = raw_block.get("extractor_evidence", {})
    return "docling" in evidence or "doctr" in evidence


def doctr_interpreted_role(raw_block: dict[str, Any]) -> tuple[str, int | None, str, list[str]] | None:
    if "doctr" not in raw_block.get("extractor_evidence", {}):
        return None
    return "paragraph", None, "medium", ["doctr_ocr_sidecar", "image_only_page", "ocr_text", "evidence_only"]


def docling_interpreted_role(raw_block: dict[str, Any]) -> tuple[str, int | None, str, list[str]] | None:
    if "docling" not in raw_block.get("extractor_evidence", {}):
        return None
    label = str(raw_block.get("structure_hints", {}).get("tag_name") or "").lower()
    basis = ["docling_sidecar_hint", f"docling_label:{label}", "ai_parser_evidence_only"]
    if label in {"heading", "section_header", "title"}:
        return "heading", 1, "medium", basis
    if label == "table":
        return "table", None, "medium", basis
    if label == "table_cell":
        return "table_cell", None, "medium", basis
    if label in {"page_header", "page_footer", "header", "footer"}:
        return "artifact", None, "medium", basis
    if label in {"picture", "figure", "image"}:
        return "figure", None, "low", basis
    if raw_block.get("text", "").strip():
        return "paragraph", None, "medium", basis
    return "unknown", None, "low", basis


def normalization_warnings(raw_block: dict[str, Any], role: str, confidence: str) -> list[dict[str, Any]]:
    if confidence != "low" and role != "unknown":
        return []
    return [
        warning_entry(
            "LOW_CONFIDENCE_NORMALIZED_BLOCK",
            f"Block {raw_block.get('block_id')} was normalized with low confidence.",
            "block",
            severity="info",
        )
    ]


def assign_table_regions(normalized_blocks: list[dict[str, Any]], raw_blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    raw_by_normalized_id = {f"n_{block['block_id']}": block for block in raw_blocks}
    cells_by_page: dict[int, list[tuple[dict[str, Any], dict[str, Any]]]] = {}
    for normalized_block in normalized_blocks:
        if normalized_block["normalized_workflow"]["interpreted_role"] != "table_cell":
            continue
        raw_block = raw_by_normalized_id.get(normalized_block["block_id"])
        if raw_block is None:
            continue
        page_number = int(normalized_block["page_span"][0])
        cells_by_page.setdefault(page_number, []).append((normalized_block, raw_block))

    table_entries = []
    for page_number, cells in cells_by_page.items():
        current_region = 0
        previous_bottom: float | None = None
        region_cells: list[tuple[dict[str, Any], dict[str, Any]]] = []
        for normalized_block, raw_block in sorted(cells, key=lambda item: (bbox_top(item[1]), bbox_left(item[1]), item[0]["block_id"])):
            top = bbox_top(raw_block)
            bottom = bbox_bottom(raw_block)
            if previous_bottom is None or top - previous_bottom > 42.0:
                current_region += 1
                if region_cells:
                    table_entries.append(table_entry_for_region(page_number, current_region - 1, region_cells))
                region_cells = []
            table_id = f"page_{page_number:04d}_table_{current_region:03d}"
            normalized_block["projected_target"]["target_table_id"] = table_id
            workflow = normalized_block["normalized_workflow"]
            workflow["role_basis"] = [*workflow["role_basis"], "table_region_grouped", "row_clustered_by_bbox"]
            region_cells.append((normalized_block, raw_block))
            previous_bottom = max(previous_bottom or bottom, bottom)
        if region_cells:
            table_entries.append(table_entry_for_region(page_number, current_region, region_cells))
    return table_entries


def table_entry_for_region(
    page_number: int,
    region_index: int,
    cells: list[tuple[dict[str, Any], dict[str, Any]]],
) -> dict[str, Any]:
    table_id = f"page_{page_number:04d}_table_{region_index:03d}"
    row_entries = table_row_entries(cells)
    header_candidate_row_indexes = [row["row_index"] for row in row_entries if row["header_candidate"]]
    warning_entries = []
    if not header_candidate_row_indexes:
        warning_entries.append(
            warning_entry(
                "TABLE_HEADERS_UNCERTAIN",
                f"Table region {table_id} has no confident header-row candidate.",
                "block",
            )
        )
    return {
        "table_id": table_id,
        "page_span": [page_number, page_number],
        "source_block_ids": [normalized_block["block_id"] for normalized_block, _raw_block in cells],
        "row_entries": row_entries,
        "header_candidate_row_indexes": header_candidate_row_indexes,
        "confidence": "medium" if row_entries else "low",
        "basis": ["table_region_grouped", "bbox_vertical_gap", "row_clustered_by_bbox"],
        "warning_entries": warning_entries,
    }


def table_row_entries(cells: list[tuple[dict[str, Any], dict[str, Any]]]) -> list[dict[str, Any]]:
    rows: list[list[tuple[dict[str, Any], dict[str, Any]]]] = []
    for normalized_block, raw_block in sorted(cells, key=lambda item: (bbox_top(item[1]), bbox_left(item[1]), item[0]["block_id"])):
        if not rows:
            rows.append([(normalized_block, raw_block)])
            continue
        current_row = rows[-1]
        current_top = median([bbox_top(raw) for _normalized, raw in current_row])
        if abs(bbox_top(raw_block) - current_top) <= 8.0:
            current_row.append((normalized_block, raw_block))
        else:
            rows.append([(normalized_block, raw_block)])

    row_entries = []
    for row_index, row_cells in enumerate(rows, start=1):
        sorted_row = sorted(row_cells, key=lambda item: (bbox_left(item[1]), item[0]["block_id"]))
        header_candidate, header_basis = row_header_candidate(row_index, sorted_row)
        row_entries.append(
            {
                "row_index": row_index,
                "cell_block_ids": [normalized_block["block_id"] for normalized_block, _raw_block in sorted_row],
                "bbox": union_bbox([raw_block.get("bbox") for _normalized_block, raw_block in sorted_row]),
                "header_candidate": header_candidate,
                "confidence": "medium" if len(sorted_row) > 1 else "low",
                "basis": ["row_clustered_by_bbox", *header_basis],
            }
        )
    return row_entries


def row_header_candidate(row_index: int, row_cells: list[tuple[dict[str, Any], dict[str, Any]]]) -> tuple[bool, list[str]]:
    if row_index != 1:
        return False, []
    text = " ".join(raw_block.get("text", "") for _normalized_block, raw_block in row_cells).strip()
    if not text:
        return False, []
    non_numeric_tokens = [token for token in text.replace("$", " ").replace(",", " ").split() if not token.strip("().%").isdigit()]
    numeric_tokens = [token for token in text.replace("$", " ").replace(",", " ").split() if token.strip("().%").isdigit()]
    label_heavy = len(non_numeric_tokens) >= max(1, len(numeric_tokens))
    if label_heavy:
        return True, ["header_candidate_first_row", "label_heavy_row_text"]
    return False, []


def union_bbox(bboxes: list[Any]) -> list[float] | None:
    valid_bboxes = [bbox for bbox in bboxes if isinstance(bbox, list) and len(bbox) == 4 and all(value is not None for value in bbox)]
    if not valid_bboxes:
        return None
    return [
        min(float(bbox[0]) for bbox in valid_bboxes),
        min(float(bbox[1]) for bbox in valid_bboxes),
        max(float(bbox[2]) for bbox in valid_bboxes),
        max(float(bbox[3]) for bbox in valid_bboxes),
    ]


def warning_entry(code: str, message: str, scope: str, severity: str = "warning", manual_review_required: bool = True) -> dict[str, Any]:
    return {
        "warning_code": code,
        "warning_message": message,
        "warning_scope": scope,
        "warning_severity": severity,
        "manual_review_required": manual_review_required,
    }


def projected_target_for_role(role: str, raw_block: dict[str, Any]) -> dict[str, Any]:
    return {
        "target_package_part": "word/document.xml",
        "target_style": target_style_for_role(role),
        "target_heading_text": raw_block.get("text", "").strip() if role == "heading" else None,
        "target_list_kind": list_kind_for_role(role, raw_block),
        "target_table_id": None,
        "projection_status": "omitted" if role == "artifact" else "planned",
    }


def target_style_for_role(role: str) -> str | None:
    if role == "heading":
        return "Heading1"
    if role in {"paragraph", "list_item", "table_cell"}:
        return "Normal"
    return None


def observed_source_refs(raw_block: dict[str, Any]) -> list[str]:
    refs = [raw_block.get("source_ref"), raw_block.get("block_id")]
    return [ref for ref in refs if ref]


def reading_order_source(manifest: dict[str, Any]) -> str:
    if manifest.get("document_accessibility", {}).get("struct_tree_detected"):
        return "mixed"
    return "layout_inference"


def pages_with_warnings(manifest: dict[str, Any]) -> int:
    pages = {page["page_number"] for page in manifest.get("page_entries", []) if page.get("warning_entries")}
    for block in manifest.get("normalized_block_entries", []):
        if block.get("warning_entries"):
            pages.update(block.get("page_span", []))
    return len(pages)


def bbox_top(block: dict[str, Any]) -> float:
    bbox = block.get("bbox") or []
    return float(bbox[1]) if len(bbox) == 4 and bbox[1] is not None else 0.0


def bbox_left(block: dict[str, Any]) -> float:
    bbox = block.get("bbox") or []
    return float(bbox[0]) if len(bbox) == 4 and bbox[0] is not None else 0.0


def bbox_bottom(block: dict[str, Any]) -> float:
    bbox = block.get("bbox") or []
    return float(bbox[3]) if len(bbox) == 4 and bbox[3] is not None else bbox_top(block)
