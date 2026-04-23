from __future__ import annotations

import ast
import json
from importlib import import_module, metadata
from pathlib import Path
from typing import Any

from accessibility_by_manifest.inputs.pdf.extractors.common import safe_value
from accessibility_by_manifest.manifest.pdf_builder import ManifestBuilder, warning_entry
from accessibility_by_manifest.util.logging import get_logger


logger = get_logger("inputs.pdf.extractors.ai_parsers.docling")


class DoclingAdapter:
    """Run Docling as an optional sidecar parser and record its claims as evidence."""

    extractor_name = "docling"

    def populate(self, builder: ManifestBuilder) -> None:
        logger.info("Docling sidecar parser started")
        converter_class = load_document_converter()
        builder.extractor_versions[self.extractor_name] = package_version("docling")
        parser_dir = builder.output_paths.ai_parser_dir(self.extractor_name)
        evidence: dict[str, Any] = {
            "parser_role": "optional_ai_parser_sidecar",
            "canonical_status": "evidence_only",
            "output_mode": builder.config.ai_parser_output_mode,
            "artifacts_written": False,
            "artifact_dir": str(parser_dir),
            "artifact_paths": {},
            "document_claims": {},
            "warnings": [],
        }
        try:
            converter = converter_class()
            result = converter.convert(str(builder.input_path))
            document = getattr(result, "document", result)
            exports = exported_docling_artifacts(document)
            claims = docling_claims(document, exports)
            if not builder.config.dry_run and builder.config.ai_parser_output_mode == "artifacts":
                evidence["artifact_paths"] = write_docling_artifacts(parser_dir, builder.input_path.stem, exports, builder.config.overwrite)
                evidence["artifacts_written"] = True
            elif builder.config.dry_run:
                evidence["warnings"].append("Artifact writing skipped because this is a dry run.")
            evidence["document_claims"] = claims
            materialized_counts = materialize_docling_evidence(builder, exports.get("json"))
            evidence["materialized_evidence"] = materialized_counts
            add_docling_page_hints(builder, claims)
            logger.info(
                "Docling sidecar parser completed: exports=%s tables=%s headings=%s figures=%s raw_blocks=%s artifacts_written=%s",
                claims.get("export_formats"),
                claims.get("table_candidate_count"),
                claims.get("heading_candidate_count"),
                claims.get("figure_candidate_count"),
                materialized_counts.get("raw_block_count"),
                evidence["artifacts_written"],
            )
        except Exception as exc:
            logger.exception("Docling sidecar parser failed")
            raise RuntimeError(f"Docling sidecar parser failed: {exc}") from exc
        builder.extractor_evidence[self.extractor_name] = evidence


def load_document_converter() -> Any:
    try:
        module = import_module("docling.document_converter")
    except ImportError as exc:
        raise RuntimeError("Docling sidecar requested, but the optional 'docling' package is not installed.") from exc
    converter_class = getattr(module, "DocumentConverter", None)
    if converter_class is None:
        raise RuntimeError("Docling sidecar requested, but docling.document_converter.DocumentConverter was not found.")
    return converter_class


def package_version(package_name: str) -> str | None:
    try:
        return metadata.version(package_name)
    except metadata.PackageNotFoundError:
        return None


def exported_docling_artifacts(document: Any) -> dict[str, Any]:
    artifacts: dict[str, Any] = {}
    for name, method_name in (
        ("markdown", "export_to_markdown"),
        ("html", "export_to_html"),
        ("json", "export_to_dict"),
    ):
        method = getattr(document, method_name, None)
        if not callable(method):
            continue
        try:
            artifacts[name] = method()
        except Exception as exc:
            artifacts[f"{name}_error"] = str(exc)
    return artifacts


def docling_claims(document: Any, exports: dict[str, Any]) -> dict[str, Any]:
    json_export = exports.get("json")
    markdown = exports.get("markdown")
    claims = {
        "export_formats": sorted(key for key in exports if not key.endswith("_error")),
        "export_errors": {key: value for key, value in exports.items() if key.endswith("_error")},
        "markdown_character_count": len(markdown) if isinstance(markdown, str) else None,
        "json_top_level_keys": sorted(json_export) if isinstance(json_export, dict) else None,
        "reading_order_claim_source": "docling_document_order",
        "table_candidate_count": count_docling_items(json_export, ("table",)),
        "heading_candidate_count": count_docling_items(json_export, ("heading", "section_header", "title")),
        "figure_candidate_count": count_docling_items(json_export, ("picture", "figure", "image")),
        "artifact_candidate_count": count_docling_items(json_export, ("header", "footer", "page_header", "page_footer")),
        "raw_document_summary": safe_value(summary_attrs(document)),
    }
    return claims


def summary_attrs(document: Any) -> dict[str, Any]:
    summary = {}
    for attr_name in ("pages", "texts", "tables", "pictures", "groups", "body"):
        value = getattr(document, attr_name, None)
        if value is None:
            continue
        try:
            summary[attr_name] = {"type": type(value).__name__, "count": len(value)}
        except Exception:
            summary[attr_name] = {"type": type(value).__name__}
    return summary


def count_docling_items(value: Any, labels: tuple[str, ...]) -> int:
    label_set = {label.lower() for label in labels}
    count = 0
    if isinstance(value, dict):
        possible_label = str(value.get("label") or value.get("type") or value.get("name") or "").lower()
        if possible_label in label_set:
            count += 1
        for item in value.values():
            count += count_docling_items(item, labels)
    elif isinstance(value, list):
        for item in value:
            count += count_docling_items(item, labels)
    return count


def write_docling_artifacts(parser_dir: Path, stem: str, exports: dict[str, Any], overwrite: bool) -> dict[str, str]:
    parser_dir.mkdir(parents=True, exist_ok=True)
    paths = {}
    for key, value in exports.items():
        if key.endswith("_error"):
            continue
        suffix = {"markdown": ".md", "html": ".html", "json": ".json"}.get(key)
        if suffix is None:
            continue
        path = parser_dir / f"{stem}_docling{suffix}"
        if path.exists() and not overwrite:
            raise FileExistsError(f"Output already exists. Use --overwrite or choose another folder: {path}")
        if suffix == ".json":
            path.write_text(json.dumps(safe_value(value), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        else:
            path.write_text(str(value), encoding="utf-8")
        paths[key] = str(path)
    return paths


def materialize_docling_evidence(builder: ManifestBuilder, json_export: Any) -> dict[str, int]:
    if not isinstance(json_export, dict):
        return {"raw_block_count": 0, "text_block_count": 0, "table_cell_block_count": 0, "picture_block_count": 0}

    before_count = len(builder.raw_block_entries)
    text_count = 0
    table_region_count = 0
    table_cell_count = 0
    picture_count = 0
    page_heights = page_height_by_number(builder)

    for index, item in enumerate(docling_text_items(json_export), start=1):
        text = clean_docling_text(item.get("text") or item.get("orig") or "")
        if not text:
            continue
        label = str(item.get("label") or "text")
        prov = first_prov(item)
        page_number = page_number_from_prov(prov)
        if page_number is None:
            page_number = 1
        builder.raw_block_entries.append(
            docling_raw_block(
                block_id=f"docling_p{page_number:04d}_b{index:05d}",
                page_number=page_number,
                text=text,
                label=label,
                source_ref=str(item.get("self_ref") or f"docling:texts/{index}"),
                bbox=docling_bbox(prov, page_heights.get(page_number)),
                evidence=safe_value({"kind": "text", "label": label, "item": item}),
            )
        )
        text_count += 1

    table_index = 0
    for table in docling_table_items(json_export):
        table_index += 1
        table_prov = first_prov(table)
        page_number = page_number_from_prov(table_prov) or 1
        builder.raw_block_entries.append(
            docling_raw_block(
                block_id=f"docling_p{page_number:04d}_table_{table_index:04d}",
                page_number=page_number,
                text=docling_table_text(table),
                label="table",
                source_ref=str(table.get("self_ref") or f"docling:tables/{table_index}"),
                bbox=docling_bbox(table_prov, page_heights.get(page_number)),
                evidence=safe_value({"kind": "table", "table_index": table_index, "table": table}),
            )
        )
        table_region_count += 1
        cells = docling_table_cells(table)
        for cell_index, cell in enumerate(cells, start=1):
            text = clean_docling_text(cell.get("text") or "")
            if not text:
                continue
            row_index = parse_int(cell.get("start_row_offset_idx"))
            column_index = parse_int(cell.get("start_col_offset_idx"))
            cell_bbox = parsed_docling_bbox(cell.get("bbox"))
            builder.raw_block_entries.append(
                docling_raw_block(
                    block_id=f"docling_p{page_number:04d}_t{table_index:04d}_r{(row_index or 0) + 1:03d}_c{(column_index or 0) + 1:03d}",
                    page_number=page_number,
                    text=text,
                    label="table_cell",
                    source_ref=str(table.get("self_ref") or f"docling:tables/{table_index}/cells/{cell_index}"),
                    bbox=docling_bbox({"bbox": cell_bbox}, page_heights.get(page_number)),
                    evidence=safe_value(
                        {
                            "kind": "table_cell",
                            "table_index": table_index,
                            "row_index": row_index,
                            "column_index": column_index,
                            "table_prov": table.get("prov"),
                            "cell": cell,
                        }
                    ),
                )
            )
            table_cell_count += 1

    for index, item in enumerate(docling_picture_items(json_export), start=1):
        label = str(item.get("label") or "picture")
        prov = first_prov(item)
        page_number = page_number_from_prov(prov) or 1
        builder.raw_block_entries.append(
            docling_raw_block(
                block_id=f"docling_p{page_number:04d}_picture_{index:05d}",
                page_number=page_number,
                text=clean_docling_text(item.get("text") or item.get("caption") or ""),
                label=label,
                source_ref=str(item.get("self_ref") or f"docling:pictures/{index}"),
                bbox=docling_bbox(prov, page_heights.get(page_number)),
                evidence=safe_value({"kind": "picture", "label": label, "item": item}),
            )
        )
        picture_count += 1

    return {
        "raw_block_count": len(builder.raw_block_entries) - before_count,
        "text_block_count": text_count,
        "table_region_block_count": table_region_count,
        "table_cell_block_count": table_cell_count,
        "picture_block_count": picture_count,
    }


def docling_raw_block(
    *,
    block_id: str,
    page_number: int,
    text: str,
    label: str,
    source_ref: str,
    bbox: list[float] | None,
    evidence: Any,
) -> dict[str, Any]:
    source_evidence_type = "artifact_text" if label in {"page_header", "page_footer", "header", "footer"} else "ocr_text"
    return {
        "block_id": block_id,
        "page_number": page_number,
        "source_evidence_type": source_evidence_type,
        "source_ref": source_ref,
        "bbox": bbox,
        "text": text,
        "text_items": [],
        "style_hints": {"font_name": None, "font_size": None, "font_weight": None, "font_style": None},
        "structure_hints": {"tag_name": label, "parent_tag_name": None, "mcid": None, "language": None},
        "role_basis": ["docling_sidecar", f"docling_label:{label}", "evidence_only"],
        "manual_review_required": True,
        "warning_entries": [],
        "extractor_evidence": {
            DoclingAdapter.extractor_name: {
                "parser_role": "optional_ai_parser_sidecar",
                "canonical_status": "evidence_only",
                "label": label,
                "source_kind": evidence.get("kind") if isinstance(evidence, dict) else None,
                "raw": evidence,
            }
        },
    }


def docling_text_items(json_export: dict[str, Any]) -> list[dict[str, Any]]:
    items = json_export.get("texts")
    if isinstance(items, list):
        return [item for item in items if isinstance(item, dict)]
    return [
        item
        for item in recursive_labeled_items(json_export)
        if item.get("label") in {"heading", "section_header", "title", "text", "paragraph", "page_header", "page_footer"}
    ]


def docling_table_items(json_export: dict[str, Any]) -> list[dict[str, Any]]:
    items = json_export.get("tables")
    if isinstance(items, list):
        return [item for item in items if isinstance(item, dict)]
    return [item for item in recursive_labeled_items(json_export) if item.get("label") == "table"]


def docling_picture_items(json_export: dict[str, Any]) -> list[dict[str, Any]]:
    items = json_export.get("pictures")
    if isinstance(items, list):
        return [item for item in items if isinstance(item, dict)]
    return [item for item in recursive_labeled_items(json_export) if item.get("label") in {"picture", "figure", "image"}]


def recursive_labeled_items(value: Any) -> list[dict[str, Any]]:
    items = []
    if isinstance(value, dict):
        if value.get("label"):
            items.append(value)
        for child in value.values():
            items.extend(recursive_labeled_items(child))
    elif isinstance(value, list):
        for child in value:
            items.extend(recursive_labeled_items(child))
    return items


def docling_table_cells(table: dict[str, Any]) -> list[dict[str, Any]]:
    data = table.get("data")
    if isinstance(data, dict) and isinstance(data.get("table_cells"), list):
        return [cell for cell in data["table_cells"] if isinstance(cell, dict)]
    cells = table.get("cells")
    if isinstance(cells, list):
        return [cell for cell in cells if isinstance(cell, dict)]
    return []


def docling_table_text(table: dict[str, Any]) -> str:
    cells = docling_table_cells(table)
    text = " ".join(clean_docling_text(cell.get("text") or "") for cell in cells).strip()
    return text


def first_prov(item: dict[str, Any]) -> dict[str, Any] | None:
    prov = item.get("prov")
    if isinstance(prov, list) and prov and isinstance(prov[0], dict):
        return prov[0]
    return None


def page_number_from_prov(prov: dict[str, Any] | None) -> int | None:
    if not prov:
        return None
    return parse_int(prov.get("page_no"))


def page_height_by_number(builder: ManifestBuilder) -> dict[int, float]:
    heights = {}
    for page in builder.page_entries:
        page_number = page.get("page_number")
        page_bbox = page.get("observed_source", {}).get("page_bbox") or []
        if isinstance(page_number, int) and len(page_bbox) == 4:
            heights[page_number] = float(page_bbox[3]) - float(page_bbox[1])
    return heights


def docling_bbox(prov: dict[str, Any] | None, page_height: float | None) -> list[float] | None:
    if not prov:
        return None
    bbox = parsed_docling_bbox(prov.get("bbox"))
    if not bbox:
        return None
    left = parse_float(bbox.get("l"))
    top = parse_float(bbox.get("t"))
    right = parse_float(bbox.get("r"))
    bottom = parse_float(bbox.get("b"))
    if None in {left, top, right, bottom}:
        return None
    origin = str(bbox.get("coord_origin") or "").strip("'\"").upper()
    if origin == "BOTTOMLEFT" and page_height is not None:
        return [left, page_height - top, right, page_height - bottom]
    return [left, top, right, bottom]


def parsed_docling_bbox(value: Any) -> dict[str, Any] | None:
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            parsed = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return None
        return parsed if isinstance(parsed, dict) else None
    return None


def clean_docling_text(value: Any) -> str:
    return str(value).strip().strip("'\"").strip()


def parse_int(value: Any) -> int | None:
    try:
        return int(str(value).strip("'\""))
    except (TypeError, ValueError):
        return None


def parse_float(value: Any) -> float | None:
    try:
        return float(str(value).strip("'\""))
    except (TypeError, ValueError):
        return None


def add_docling_page_hints(builder: ManifestBuilder, claims: dict[str, Any]) -> None:
    hint = {
        "parser_role": "optional_ai_parser_sidecar",
        "canonical_status": "evidence_only",
        "reading_order_claim_source": claims.get("reading_order_claim_source"),
    }
    for page_entry in builder.page_entries:
        page_entry.setdefault("extractor_evidence", {})[DoclingAdapter.extractor_name] = hint
    if any(claims.get(key, 0) for key in ("table_candidate_count", "heading_candidate_count", "figure_candidate_count")):
        builder.document_warning_entries.append(
            warning_entry(
                "DOCLING_SIDE_CAR_HINTS_PRESENT",
                "Docling sidecar parser produced structural hints. Treat them as comparison evidence, not canonical output.",
                "document",
                severity="info",
                manual_review_required=False,
            )
        )
