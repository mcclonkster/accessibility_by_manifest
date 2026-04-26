from __future__ import annotations

from typing import Any

import fitz

from pdf_accessibility.models.events import NodeEvent, document_metadata_event, page_evidence_event
from pdf_accessibility.models.state import (
    AnnotationEvidence,
    BBox,
    DocumentMetadataEvidence,
    DocumentState,
    ImageEvidence,
    LinkEvidence,
    PageGeometryEvidence,
    TextBlockEvidence,
    TextSpanEvidence,
)
from pdf_accessibility.services.manifest_bridge import document_uses_shared_pdf_bridge
from pdf_accessibility.utils.ids import event_id, stable_id

NODE_NAME = "native_pdf_analysis"


def run(document: DocumentState) -> list[NodeEvent]:
    events: list[NodeEvent] = []
    shared_bridge = document_uses_shared_pdf_bridge(document)
    pages_by_number = {page.page_number: page for page in document.pages}
    with fitz.open(document.source_path) as pdf:
        if not shared_bridge:
            events.append(
                document_metadata_event(
                    event_id(NODE_NAME, "metadata", document.document_id),
                    NODE_NAME,
                    _document_metadata(pdf),
                )
            )
        for index, page in enumerate(pdf, start=1):
            evidence = _page_evidence(page, index)
            existing_page = pages_by_number.get(index)
            events.append(
                page_evidence_event(
                    event_id(NODE_NAME, "page", index, document.document_id),
                    NODE_NAME,
                    index,
                    geometry=existing_page.geometry if shared_bridge and existing_page is not None else evidence["geometry"],
                    text_blocks=(
                        existing_page.text_blocks
                        if shared_bridge and existing_page is not None and existing_page.text_blocks
                        else evidence["text_blocks"]
                    ),
                    images=evidence["images"],
                    links=(
                        existing_page.links
                        if shared_bridge and existing_page is not None and existing_page.links
                        else evidence["links"]
                    ),
                    annotations=(
                        existing_page.annotations
                        if shared_bridge and existing_page is not None and existing_page.annotations
                        else evidence["annotations"]
                    ),
                    font_names=sorted(
                        {
                            *evidence["font_names"],
                            *(
                                existing_page.font_names
                                if shared_bridge and existing_page is not None
                                else []
                            ),
                        }
                    ),
                )
            )
    return events


def _document_metadata(pdf: fitz.Document) -> DocumentMetadataEvidence:
    raw_metadata = dict(pdf.metadata or {})
    lang = _catalog_lang(pdf)
    return DocumentMetadataEvidence(
        title=_clean(raw_metadata.get("title")),
        author=_clean(raw_metadata.get("author")),
        subject=_clean(raw_metadata.get("subject")),
        keywords=_clean(raw_metadata.get("keywords")),
        creator=_clean(raw_metadata.get("creator")),
        producer=_clean(raw_metadata.get("producer")),
        creation_date=_clean(raw_metadata.get("creationDate")),
        modification_date=_clean(raw_metadata.get("modDate")),
        primary_language=lang,
        pdf_version=_clean(raw_metadata.get("format")),
        encrypted=bool(pdf.is_encrypted),
        raw_metadata=raw_metadata,
        provenance={"extractor": "pymupdf", "catalog_lang": lang is not None},
    )


def _catalog_lang(pdf: fitz.Document) -> str | None:
    try:
        catalog = pdf.pdf_catalog()
        kind, value = pdf.xref_get_key(catalog, "Lang")
    except (RuntimeError, ValueError):
        return None
    if kind in {"null", "none"} or not value:
        return None
    return value.strip("()") or None


def _page_evidence(page: fitz.Page, page_number: int) -> dict[str, Any]:
    text_blocks: list[TextBlockEvidence] = []
    images: list[ImageEvidence] = []
    font_names: set[str] = set()
    text_dict = page.get_text("dict")
    for block_index, block in enumerate(text_dict.get("blocks", [])):
        block_type = block.get("type")
        bbox = _bbox(block.get("bbox"))
        if bbox is None:
            continue
        if block_type == 0:
            text_block = _text_block(page_number, block_index, block, bbox)
            if text_block.text.strip():
                text_blocks.append(text_block)
                font_names.update(text_block.font_names)
        elif block_type == 1:
            images.append(
                ImageEvidence(
                    image_id=f"image-{stable_id(page_number, block_index, block.get('bbox'))}",
                    page_number=page_number,
                    bbox=bbox,
                    width=block.get("width"),
                    height=block.get("height"),
                    xref=block.get("xref"),
                    source_ref=f"pymupdf:page:{page_number}:block:{block_index}",
                )
            )
    for font in page.get_fonts(full=True):
        if len(font) > 3 and font[3]:
            font_names.add(str(font[3]))
    return {
        "geometry": _geometry(page),
        "text_blocks": text_blocks,
        "images": images,
        "links": _links(page, page_number),
        "annotations": _annotations(page, page_number),
        "font_names": sorted(font_names),
    }


def _text_block(page_number: int, block_index: int, block: dict[str, Any], bbox: BBox) -> TextBlockEvidence:
    spans: list[TextSpanEvidence] = []
    block_text_parts: list[str] = []
    font_names: set[str] = set()
    font_sizes: set[float] = set()
    for line in block.get("lines", []):
        line_parts: list[str] = []
        for span in line.get("spans", []):
            text = span.get("text", "")
            span_bbox = _bbox(span.get("bbox"))
            if not text or span_bbox is None:
                continue
            line_parts.append(text)
            font_name = _clean(span.get("font"))
            font_size = span.get("size")
            if font_name:
                font_names.add(font_name)
            if isinstance(font_size, int | float):
                font_sizes.add(round(float(font_size), 2))
            spans.append(
                TextSpanEvidence(
                    text=text,
                    bbox=span_bbox,
                    font_name=font_name,
                    font_size=float(font_size) if isinstance(font_size, int | float) else None,
                    flags=span.get("flags"),
                    color=span.get("color"),
                )
            )
        if line_parts:
            block_text_parts.append("".join(line_parts).strip())
    text = "\n".join(part for part in block_text_parts if part)
    return TextBlockEvidence(
        block_id=f"text-{stable_id(page_number, block_index, text[:80])}",
        page_number=page_number,
        bbox=bbox,
        text=text,
        spans=spans,
        font_names=sorted(font_names),
        font_sizes=sorted(font_sizes),
        source_ref=f"pymupdf:page:{page_number}:block:{block_index}",
    )


def _geometry(page: fitz.Page) -> PageGeometryEvidence:
    return PageGeometryEvidence(
        width=float(page.rect.width),
        height=float(page.rect.height),
        rotation=int(page.rotation),
        media_box=_rect_to_bbox(page.mediabox),
        crop_box=_rect_to_bbox(page.cropbox),
    )


def _links(page: fitz.Page, page_number: int) -> list[LinkEvidence]:
    links: list[LinkEvidence] = []
    for index, link in enumerate(page.get_links()):
        links.append(
            LinkEvidence(
                link_id=f"link-{stable_id(page_number, index, link)}",
                page_number=page_number,
                bbox=_rect_to_bbox(link.get("from")),
                uri=_clean(link.get("uri")),
                target=str(link.get("page")) if link.get("page") is not None else None,
                source_ref=f"pymupdf:page:{page_number}:link:{index}",
            )
        )
    return links


def _annotations(page: fitz.Page, page_number: int) -> list[AnnotationEvidence]:
    annotations: list[AnnotationEvidence] = []
    annot_iter = page.annots()
    if annot_iter is None:
        return annotations
    for index, annot in enumerate(annot_iter):
        info = annot.info or {}
        annotations.append(
            AnnotationEvidence(
                annotation_id=f"annotation-{stable_id(page_number, index, info)}",
                page_number=page_number,
                bbox=_rect_to_bbox(annot.rect),
                annotation_type=annot.type[1] if annot.type else None,
                contents=_clean(info.get("content")),
                source_ref=f"pymupdf:page:{page_number}:annotation:{index}",
            )
        )
    return annotations


def _bbox(value: Any) -> BBox | None:
    if value is None:
        return None
    try:
        left, top, right, bottom = value
    except (TypeError, ValueError):
        return None
    return BBox(left=float(left), top=float(top), right=float(right), bottom=float(bottom))


def _rect_to_bbox(rect: Any) -> BBox | None:
    if rect is None:
        return None
    if hasattr(rect, "x0"):
        return BBox(left=float(rect.x0), top=float(rect.y0), right=float(rect.x1), bottom=float(rect.y1))
    return _bbox(rect)


def _clean(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
