from __future__ import annotations

from typing import Any

from accessibility_by_manifest.inputs.pdf.extractors.common import safe_value
from accessibility_by_manifest.manifest.pdf_builder import ManifestBuilder, warning_entry
from accessibility_by_manifest.util.pdf_text import clean_text


class PyMuPDFAdapter:
    """Populate the v0.1 manifest with PyMuPDF-owned first-pass evidence."""

    def populate(self, builder: ManifestBuilder) -> None:
        try:
            import fitz
        except Exception as exc:  # pragma: no cover - dependency check catches this.
            raise RuntimeError("PyMuPDF is required for PDF extraction.") from exc

        with fitz.open(builder.input_path) as document:
            builder.extractor_versions["pymupdf"] = getattr(fitz, "version", [None])[0]
            builder.page_count = document.page_count
            builder.byte_length = builder.input_path.stat().st_size
            builder.metadata = dict(document.metadata or {})
            builder.xmp_present = bool(get_xmp_metadata(document))
            builder.extractor_evidence["pymupdf"] = {
                "document_metadata": builder.metadata,
                "xmp_metadata_length": len(get_xmp_metadata(document)),
                "needs_pass": getattr(document, "needs_pass", None),
                "is_encrypted": getattr(document, "is_encrypted", None),
                "page_count": document.page_count,
            }

            for page_index in range(document.page_count):
                page = document.load_page(page_index)
                page_number = page_index + 1
                text_dict = page.get_text("dict")
                raw_blocks = text_dict.get("blocks", [])
                text_blocks = [block for block in raw_blocks if block.get("type") == 0 and block_text(block)]
                image_blocks = [block for block in raw_blocks if block.get("type") == 1]
                annotation_entries = annotation_entries_for_page(page)
                widgets = list_or_empty(page.widgets())
                annotation_count = len(annotation_entries)
                form_field_count = len(widgets)
                image_count = len(image_blocks) + len(page.get_images(full=True))
                text_layer_detected = bool(text_blocks)
                image_only_suspected = not text_layer_detected and image_count > 0
                ocr_text_detected = text_layer_detected and image_count > 0
                page_warnings = []
                if image_only_suspected:
                    page_warnings.append(
                        warning_entry(
                            "IMAGE_ONLY_PAGE_SUSPECTED",
                            "Page has image evidence but no extractable text blocks; OCR may be required.",
                            "ocr",
                        )
                    )
                if annotation_count:
                    page_warnings.append(
                        warning_entry(
                            "ANNOTATIONS_PRESENT",
                            "Page contains annotations or links that require review.",
                            "annotation",
                            severity="info",
                        )
                    )

                builder.annotation_count += annotation_count
                builder.form_field_count += form_field_count
                builder.figure_candidate_count += image_count
                builder.page_entries.append(
                    {
                        "page_number": page_number,
                        "observed_source": {
                            "page_ref": f"page:{page_number}",
                            "page_rotation": float(page.rotation or 0),
                            "user_unit": 1.0,
                            "page_bbox": bbox_to_list(page.rect),
                            "viewport": {"width": float(page.rect.width), "height": float(page.rect.height)},
                            "struct_tree_present": None,
                            "text_layer_detected": text_layer_detected,
                            "image_only_page_suspected": image_only_suspected,
                            "ocr_text_detected": ocr_text_detected,
                            "annotation_count": annotation_count,
                            "form_field_count": form_field_count,
                            "xfa_present": None,
                            "operator_list_present": None,
                            "page_label": None,
                        },
                        "struct_tree": None,
                        "annotation_entries": annotation_entries,
                        "xfa_entries": [],
                        "operator_evidence": None,
                        "extractor_evidence": {
                            "pymupdf": {
                                "raw_text_dict_block_count": len(raw_blocks),
                                "text_block_count": len(text_blocks),
                                "image_block_count": len(image_blocks),
                                "image_xref_count": len(page.get_images(full=True)),
                                "font_entries": safe_value(page.get_fonts(full=True)),
                                "link_entries": safe_value(page.get_links()),
                                "widget_count": form_field_count,
                                "page_rect": bbox_to_list(page.rect),
                                "cropbox": bbox_to_list(page.cropbox),
                                "mediabox": bbox_to_list(page.mediabox),
                            }
                        },
                        "warning_entries": page_warnings,
                    }
                )

                for block_index, block in enumerate(text_blocks, start=1):
                    builder.raw_block_entries.append(raw_block_entry(page_number, block_index, block))


def get_xmp_metadata(document: Any) -> str:
    try:
        return document.get_xml_metadata() or ""
    except Exception:
        return ""


def list_or_empty(value: Any) -> list[Any]:
    if value is None:
        return []
    return list(value)


def annotation_entries_for_page(page: Any) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for annotation in list_or_empty(page.annots()):
        info = getattr(annotation, "info", {}) or {}
        subtype = annotation.type[1] if getattr(annotation, "type", None) else None
        entries.append(
            {
                "annotation_subtype": clean_text(subtype) or None,
                "contents": clean_text(info.get("content")) or None,
                "alt_text": clean_text(info.get("title")) or None,
                "url": None,
                "dest": None,
                "manual_review_required": True,
            }
        )
    for link in list_or_empty(page.get_links()):
        uri = clean_text(link.get("uri")) or None
        dest = link_destination(link)
        entries.append(
            {
                "annotation_subtype": "link",
                "contents": None,
                "alt_text": None,
                "url": uri,
                "dest": dest,
                "manual_review_required": True,
            }
        )
    return entries


def link_destination(link: dict[str, Any]) -> str | list[Any] | None:
    if "page" in link and link.get("page") is not None:
        return f"page:{int(link['page']) + 1}"
    if "to" in link and link.get("to") is not None:
        return str(link["to"])
    return None


def raw_block_entry(page_number: int, block_index: int, block: dict[str, Any]) -> dict[str, Any]:
    text = block_text(block)
    warnings = []
    if not text:
        warnings.append(warning_entry("EMPTY_TEXT_BLOCK", "Text block had no usable text after cleanup.", "block"))
    return {
        "block_id": f"p{page_number:04d}_b{block_index:04d}",
        "page_number": page_number,
        "source_evidence_type": "untagged_text",
        "source_ref": f"page:{page_number}/block:{block_index}",
        "bbox": bbox_to_list(block.get("bbox")),
        "text": text,
        "text_items": text_items(block),
        "style_hints": style_hints(block),
        "structure_hints": {
            "tag_name": None,
            "parent_tag_name": None,
            "mcid": None,
            "language": None,
        },
        "role_basis": ["pymupdf_text_block"],
        "manual_review_required": bool(warnings),
        "warning_entries": warnings,
        "extractor_evidence": {
            "pymupdf": {
                "block_type": block.get("type"),
                "block_number": block.get("number"),
                "line_count": len(block.get("lines", [])),
                "raw_block": safe_value(block),
            }
        },
    }


def block_text(block: dict[str, Any]) -> str:
    parts: list[str] = []
    for line in block.get("lines", []):
        line_parts = [clean_text(span.get("text", "")) for span in line.get("spans", [])]
        line_text = clean_text(" ".join(part for part in line_parts if part))
        if line_text:
            parts.append(line_text)
    return clean_text("\n".join(parts))


def text_items(block: dict[str, Any]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for line in block.get("lines", []):
        direction = line.get("dir")
        for span in line.get("spans", []):
            text = clean_text(span.get("text", ""))
            if not text:
                continue
            bbox = span.get("bbox") or [None, None, None, None]
            width = None if bbox[0] is None or bbox[2] is None else float(bbox[2]) - float(bbox[0])
            height = None if bbox[1] is None or bbox[3] is None else float(bbox[3]) - float(bbox[1])
            items.append(
                {
                    "str": text,
                    "dir": ",".join(str(item) for item in direction) if direction else None,
                    "width": width,
                    "height": height,
                    "fontName": clean_text(span.get("font")) or None,
                    "transform": None,
                }
            )
    return items


def style_hints(block: dict[str, Any]) -> dict[str, Any]:
    first_span = first_text_span(block)
    if not first_span:
        return {"font_name": None, "font_size": None, "font_weight": None, "font_style": None}
    font_name = clean_text(first_span.get("font")) or None
    flags = int(first_span.get("flags") or 0)
    return {
        "font_name": font_name,
        "font_size": float(first_span["size"]) if first_span.get("size") is not None else None,
        "font_weight": "bold" if flags & 16 else None,
        "font_style": "italic" if flags & 2 else None,
    }


def first_text_span(block: dict[str, Any]) -> dict[str, Any] | None:
    for line in block.get("lines", []):
        for span in line.get("spans", []):
            if clean_text(span.get("text", "")):
                return span
    return None


def bbox_to_list(value: Any) -> list[float] | None:
    if value is None:
        return None
    if hasattr(value, "x0"):
        return [float(value.x0), float(value.y0), float(value.x1), float(value.y1)]
    if isinstance(value, (list, tuple)) and len(value) == 4:
        return [float(item) for item in value]
    return None
