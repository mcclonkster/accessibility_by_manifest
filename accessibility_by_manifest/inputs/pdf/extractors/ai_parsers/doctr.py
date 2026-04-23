from __future__ import annotations

import tempfile
import os
from importlib import import_module, metadata
from pathlib import Path
from typing import Any

import fitz

from accessibility_by_manifest.inputs.pdf.extractors.common import safe_value
from accessibility_by_manifest.manifest.pdf_builder import ManifestBuilder, warning_entry
from accessibility_by_manifest.util.logging import get_logger


logger = get_logger("inputs.pdf.extractors.ai_parsers.doctr")


class DoctrOcrAdapter:
    """Run python-doctr as optional targeted OCR for image-only pages."""

    extractor_name = "doctr"

    def populate(self, builder: ManifestBuilder) -> None:
        logger.info("doctr OCR sidecar started")
        document_file_class, predictor_factory = load_doctr()
        builder.extractor_versions[self.extractor_name] = package_version("python-doctr")
        target_pages = image_only_page_numbers(builder)
        evidence: dict[str, Any] = {
            "parser_role": "optional_targeted_ocr_sidecar",
            "canonical_status": "evidence_only",
            "target_policy": "image_only_pages_only",
            "target_page_numbers": target_pages,
            "page_count": len(target_pages),
            "raw_block_count": 0,
            "warnings": [],
        }
        if not target_pages:
            evidence["warnings"].append("No image-only pages were detected; OCR sidecar skipped.")
            builder.extractor_evidence[self.extractor_name] = evidence
            return

        try:
            with tempfile.TemporaryDirectory(prefix=f"{builder.input_path.stem}_doctr_ocr_") as temp_dir:
                configure_doctr_cache(builder)
                image_paths = render_target_pages(builder.input_path, target_pages, Path(temp_dir))
                document = document_file_class.from_images([str(path) for path in image_paths])
                predictor = predictor_factory(pretrained=True)
                result = predictor(document)
                exported = result.export() if hasattr(result, "export") else result
                counts = materialize_doctr_ocr(builder, exported, target_pages)
                evidence.update(counts)
                evidence["raw_export_summary"] = safe_value(ocr_export_summary(exported))
            if counts.get("raw_block_count", 0):
                builder.document_warning_entries.append(
                    warning_entry(
                        "DOCTR_OCR_SIDE_CAR_EVIDENCE_PRESENT",
                        "doctr OCR recovered text evidence for image-only pages. Treat it as review-required sidecar evidence.",
                        "ocr",
                        severity="info",
                        manual_review_required=False,
                    )
                )
            logger.info("doctr OCR sidecar completed: pages=%s raw_blocks=%s", len(target_pages), counts.get("raw_block_count"))
        except Exception as exc:
            logger.exception("doctr OCR sidecar failed")
            raise RuntimeError(f"doctr OCR sidecar failed: {exc}") from exc
        builder.extractor_evidence[self.extractor_name] = evidence


def load_doctr() -> tuple[Any, Any]:
    try:
        io_module = import_module("doctr.io")
        models_module = import_module("doctr.models")
    except ImportError as exc:
        raise RuntimeError("doctr OCR requested, but the optional 'python-doctr' package is not installed.") from exc
    document_file_class = getattr(io_module, "DocumentFile", None)
    predictor_factory = getattr(models_module, "ocr_predictor", None)
    if document_file_class is None or predictor_factory is None:
        raise RuntimeError("doctr OCR requested, but doctr.io.DocumentFile or doctr.models.ocr_predictor was not found.")
    return document_file_class, predictor_factory


def package_version(package_name: str) -> str | None:
    try:
        return metadata.version(package_name)
    except metadata.PackageNotFoundError:
        return None


def configure_doctr_cache(builder: ManifestBuilder) -> None:
    cache_dir = builder.output_paths.ai_parser_dir(DoctrOcrAdapter.extractor_name) / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("DOCTR_CACHE_DIR", str(cache_dir))


def image_only_page_numbers(builder: ManifestBuilder) -> list[int]:
    return [
        int(page.get("page_number"))
        for page in builder.page_entries
        if page.get("observed_source", {}).get("image_only_page_suspected") and page.get("page_number") is not None
    ]


def render_target_pages(pdf_path: Path, page_numbers: list[int], temp_dir: Path) -> list[Path]:
    image_paths: list[Path] = []
    document = fitz.open(pdf_path)
    try:
        for page_number in page_numbers:
            page = document[page_number - 1]
            pixmap = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
            image_path = temp_dir / f"page_{page_number:04d}.png"
            pixmap.save(image_path)
            image_paths.append(image_path)
    finally:
        document.close()
    return image_paths


def materialize_doctr_ocr(builder: ManifestBuilder, exported: Any, target_pages: list[int]) -> dict[str, int]:
    if not isinstance(exported, dict):
        return {"raw_block_count": 0, "word_count": 0}
    pages = exported.get("pages")
    if not isinstance(pages, list):
        return {"raw_block_count": 0, "word_count": 0}

    raw_block_count = 0
    word_count = 0
    page_sizes = page_size_by_number(builder)
    for page_offset, page in enumerate(pages):
        if page_offset >= len(target_pages) or not isinstance(page, dict):
            continue
        page_number = target_pages[page_offset]
        page_width, page_height = page_sizes.get(page_number, (None, None))
        for line_index, line in enumerate(iter_doctr_lines(page), start=1):
            words = [word for word in line.get("words", []) if isinstance(word, dict)]
            text = " ".join(str(word.get("value") or "").strip() for word in words).strip()
            if not text:
                continue
            word_count += len(words)
            bbox = doctr_line_bbox(words, page_width, page_height)
            block_id = f"doctr_p{page_number:04d}_l{line_index:05d}"
            builder.raw_block_entries.append(
                {
                    "block_id": block_id,
                    "page_number": page_number,
                    "source_evidence_type": "ocr_text",
                    "source_ref": f"doctr:page:{page_number}/line:{line_index}",
                    "bbox": bbox,
                    "text": text,
                    "text_items": [
                        {
                            "str": str(word.get("value") or ""),
                            "dir": None,
                            "width": None,
                            "height": None,
                            "fontName": None,
                            "transform": None,
                            "confidence": word.get("confidence"),
                            "geometry": safe_value(word.get("geometry")),
                        }
                        for word in words
                    ],
                    "style_hints": {"font_name": None, "font_size": None, "font_weight": None, "font_style": None},
                    "structure_hints": {"tag_name": "ocr_line", "parent_tag_name": None, "mcid": None, "language": None},
                    "role_basis": ["doctr_ocr_sidecar", "image_only_page", "evidence_only"],
                    "manual_review_required": True,
                    "warning_entries": [
                        warning_entry(
                            "OCR_TEXT_REQUIRES_REVIEW",
                            "OCR text was recovered from an image-only page and must be reviewed before final output.",
                            "ocr",
                        )
                    ],
                    "extractor_evidence": {
                        DoctrOcrAdapter.extractor_name: {
                            "parser_role": "optional_targeted_ocr_sidecar",
                            "canonical_status": "evidence_only",
                            "line_index": line_index,
                            "words": safe_value(words),
                        }
                    },
                }
            )
            mark_page_ocr_detected(builder, page_number)
            raw_block_count += 1
    return {"raw_block_count": raw_block_count, "word_count": word_count}


def iter_doctr_lines(page: dict[str, Any]) -> list[dict[str, Any]]:
    lines: list[dict[str, Any]] = []
    for block in page.get("blocks", []) if isinstance(page.get("blocks"), list) else []:
        if not isinstance(block, dict):
            continue
        for line in block.get("lines", []) if isinstance(block.get("lines"), list) else []:
            if isinstance(line, dict):
                lines.append(line)
    return lines


def doctr_line_bbox(words: list[dict[str, Any]], page_width: float | None, page_height: float | None) -> list[float] | None:
    boxes = [doctr_word_bbox(word, page_width, page_height) for word in words]
    boxes = [box for box in boxes if box is not None]
    if not boxes:
        return None
    return [
        min(box[0] for box in boxes),
        min(box[1] for box in boxes),
        max(box[2] for box in boxes),
        max(box[3] for box in boxes),
    ]


def doctr_word_bbox(word: dict[str, Any], page_width: float | None, page_height: float | None) -> list[float] | None:
    geometry = word.get("geometry")
    if page_width is None or page_height is None or not isinstance(geometry, (list, tuple)) or len(geometry) != 2:
        return None
    try:
        left = float(geometry[0][0]) * page_width
        top = float(geometry[0][1]) * page_height
        right = float(geometry[1][0]) * page_width
        bottom = float(geometry[1][1]) * page_height
    except (TypeError, ValueError, IndexError):
        return None
    return [left, top, right, bottom]


def page_size_by_number(builder: ManifestBuilder) -> dict[int, tuple[float | None, float | None]]:
    sizes = {}
    for page in builder.page_entries:
        page_number = page.get("page_number")
        page_bbox = page.get("observed_source", {}).get("page_bbox") or []
        if isinstance(page_number, int) and len(page_bbox) == 4:
            sizes[page_number] = (float(page_bbox[2]) - float(page_bbox[0]), float(page_bbox[3]) - float(page_bbox[1]))
    return sizes


def mark_page_ocr_detected(builder: ManifestBuilder, page_number: int) -> None:
    for page in builder.page_entries:
        if page.get("page_number") == page_number:
            page.setdefault("extractor_evidence", {})[DoctrOcrAdapter.extractor_name] = {
                "parser_role": "optional_targeted_ocr_sidecar",
                "canonical_status": "evidence_only",
                "ocr_text_detected": True,
            }
            page.setdefault("observed_source", {})["ocr_text_detected"] = True
            return


def ocr_export_summary(exported: Any) -> dict[str, Any]:
    if not isinstance(exported, dict):
        return {"type": type(exported).__name__}
    pages = exported.get("pages")
    if not isinstance(pages, list):
        return {"keys": sorted(exported.keys())}
    return {
        "page_count": len(pages),
        "block_count": sum(len(page.get("blocks", [])) for page in pages if isinstance(page, dict)),
        "line_count": sum(len(block.get("lines", [])) for page in pages if isinstance(page, dict) for block in page.get("blocks", []) if isinstance(block, dict)),
    }
