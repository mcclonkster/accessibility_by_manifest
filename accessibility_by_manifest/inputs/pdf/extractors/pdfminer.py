from __future__ import annotations

from typing import Any

from accessibility_by_manifest.manifest.pdf_builder import ManifestBuilder, warning_entry
from accessibility_by_manifest.util.logging import get_logger
from accessibility_by_manifest.util.pdf_text import clean_text


logger = get_logger("inputs.pdf.extractors.pdfminer")


class PdfminerAdapter:
    """Add pdfminer.six layout, character, font, and text-container evidence."""

    extractor_name = "pdfminer.six"

    def populate(self, builder: ManifestBuilder) -> None:
        try:
            import pdfminer
            from pdfminer.high_level import extract_pages
            from pdfminer.layout import LTChar, LTTextContainer, LTTextLine
        except Exception as exc:
            builder.extractor_versions[self.extractor_name] = None
            builder.document_warning_entries.append(
                warning_entry("PDFMINER_UNAVAILABLE", f"pdfminer.six could not be imported: {exc}", "document", severity="info", manual_review_required=False)
            )
            return

        builder.extractor_versions[self.extractor_name] = getattr(pdfminer, "__version__", None)
        block_index_by_page: dict[int, int] = {}
        try:
            pages = extract_pages(str(builder.input_path))
            for page_number, layout in enumerate(pages, start=1):
                page_evidence = {
                    "bbox": list(getattr(layout, "bbox", []) or []),
                    "rotate": getattr(layout, "rotate", None),
                    "width": getattr(layout, "width", None),
                    "height": getattr(layout, "height", None),
                    "text_container_count": 0,
                    "line_count": 0,
                    "char_count": 0,
                    "fonts": {},
                }
                for element in layout:
                    if not isinstance(element, LTTextContainer):
                        continue
                    text = clean_text(element.get_text())
                    if not text:
                        continue
                    block_index_by_page[page_number] = block_index_by_page.get(page_number, 0) + 1
                    text_items, style_hints, stats, debug_text_items = text_items_for_element(
                        element,
                        LTTextLine,
                        LTChar,
                        include_char_level_evidence=builder.config.include_char_level_evidence,
                    )
                    block_id = f"pdfminer_p{page_number:04d}_b{block_index_by_page[page_number]:04d}"
                    if debug_text_items:
                        builder.debug_evidence.setdefault(self.extractor_name, {}).setdefault("raw_block_entries", []).append(
                            {
                                "block_id": block_id,
                                "page_number": page_number,
                                "source_ref": f"pdfminer:page:{page_number}/text_container:{block_index_by_page[page_number]}",
                                "text_items": debug_text_items,
                            }
                        )
                    page_evidence["text_container_count"] += 1
                    page_evidence["line_count"] += stats["line_count"]
                    page_evidence["char_count"] += stats["char_count"]
                    for font_name, count in stats["fonts"].items():
                        page_evidence["fonts"][font_name] = page_evidence["fonts"].get(font_name, 0) + count
                    builder.raw_block_entries.append(
                        {
                            "block_id": block_id,
                            "page_number": page_number,
                            "source_evidence_type": "untagged_text",
                            "source_ref": f"pdfminer:page:{page_number}/text_container:{block_index_by_page[page_number]}",
                            "bbox": bbox_to_list(getattr(element, "bbox", None)),
                            "text": text,
                            "text_items": text_items,
                            "style_hints": style_hints,
                            "structure_hints": {
                                "tag_name": None,
                                "parent_tag_name": None,
                                "mcid": None,
                                "language": None,
                                "extractor": self.extractor_name,
                            },
                            "role_basis": ["pdfminer_layout_text_container"],
                            "manual_review_required": False,
                            "warning_entries": [],
                            "extractor_evidence": {
                                self.extractor_name: {
                                    "element_type": type(element).__name__,
                                    "index_within_page": block_index_by_page[page_number],
                                    "line_count": stats["line_count"],
                                    "char_count": stats["char_count"],
                                    "fonts": stats["fonts"],
                                }
                            },
                        }
                    )
                if page_number <= len(builder.page_entries):
                    builder.page_entries[page_number - 1].setdefault("extractor_evidence", {})[self.extractor_name] = page_evidence
            builder.extractor_evidence[self.extractor_name] = {
                "raw_blocks_added": sum(block_index_by_page.values()),
                "pages_with_pdfminer_text": sorted(block_index_by_page),
            }
            logger.info(
                "pdfminer.six extraction completed: raw_blocks_added=%s pages_with_text=%s",
                sum(block_index_by_page.values()),
                len(block_index_by_page),
            )
        except Exception as exc:
            builder.document_warning_entries.append(warning_entry("PDFMINER_EXTRACTION_FAILED", f"pdfminer.six extraction failed: {exc}", "document"))
            logger.exception("pdfminer.six extraction failed")


def text_items_for_element(
    element: Any,
    line_type: type,
    char_type: type,
    *,
    include_char_level_evidence: bool,
) -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    items: list[dict[str, Any]] = []
    debug_items: list[dict[str, Any]] = []
    fonts: dict[str, int] = {}
    sizes: list[float] = []
    line_count = 0
    char_count = 0
    for line in element:
        if not isinstance(line, line_type):
            continue
        line_count += 1
        line_text = clean_text(line.get_text())
        line_chars = []
        for item in line:
            if not isinstance(item, char_type):
                continue
            text = clean_text(item.get_text())
            if not text:
                continue
            font_name = getattr(item, "fontname", None)
            font_size = float(getattr(item, "size", 0) or 0)
            fonts[font_name or "unknown"] = fonts.get(font_name or "unknown", 0) + 1
            sizes.append(font_size)
            char_count += 1
            if include_char_level_evidence:
                line_chars.append(
                    {
                        "str": text,
                        "bbox": bbox_to_list(getattr(item, "bbox", None)),
                        "fontName": font_name,
                        "font_size": font_size,
                        "adv": getattr(item, "adv", None),
                        "upright": getattr(item, "upright", None),
                        "extractor": "pdfminer.six",
                    }
                )
        line_entry = {
            "str": line_text,
            "bbox": bbox_to_list(getattr(line, "bbox", None)),
            "extractor": "pdfminer.six",
        }
        items.append(line_entry)
        if include_char_level_evidence:
            debug_items.append(
                {
                    "str": line_text,
                    "bbox": bbox_to_list(getattr(line, "bbox", None)),
                    "chars": line_chars,
                    "extractor": "pdfminer.six",
                }
            )
    dominant_font = max(fonts, key=fonts.get) if fonts else None
    style_hints = {
        "font_name": dominant_font,
        "font_size": max(sizes) if sizes else None,
        "font_weight": "bold" if dominant_font and "bold" in dominant_font.lower() else None,
        "font_style": "italic" if dominant_font and ("italic" in dominant_font.lower() or "oblique" in dominant_font.lower()) else None,
        "font_names": fonts,
        "font_sizes": sorted(set(round(size, 3) for size in sizes)),
    }
    return items, style_hints, {"line_count": line_count, "char_count": char_count, "fonts": fonts}, debug_items


def bbox_to_list(value: Any) -> list[float] | None:
    if isinstance(value, (list, tuple)) and len(value) == 4:
        return [float(item) for item in value]
    return None
