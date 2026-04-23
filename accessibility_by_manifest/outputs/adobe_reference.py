from __future__ import annotations

import json
import re
from html import unescape
from pathlib import Path
from typing import Any
from zipfile import BadZipFile, ZipFile

from accessibility_by_manifest.inputs.pdf.paths import PdfOutputPaths, PdfRun
from accessibility_by_manifest.outputs.manifest import atomic_write_text
from accessibility_by_manifest.util.logging import get_logger


LOGGER = get_logger(__name__)

REFERENCE_POLICY = (
    "Adobe reference exports are comparison evidence. They show how Adobe interpreted "
    "the same source PDF across export modes, but they are not canonical ground truth "
    "and do not replace the master manifest."
)


def write_adobe_reference_comparison_if_available(
    manifest: dict[str, Any], run: PdfRun, output_paths: PdfOutputPaths, overwrite: bool
) -> bool:
    report = build_adobe_reference_comparison(manifest, run.pdf_path)
    if not report["reference_summary"]["any_reference_present"]:
        LOGGER.info("No Adobe reference exports found for %s", run.pdf_path)
        return False

    LOGGER.info("Writing Adobe reference comparison for %s", run.pdf_path)
    atomic_write_text(
        output_paths.adobe_reference_comparison_json,
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        overwrite,
    )
    atomic_write_text(output_paths.adobe_reference_comparison_markdown, build_adobe_reference_markdown(report), overwrite)
    return True


def build_adobe_reference_comparison(manifest: dict[str, Any], pdf_path: Path) -> dict[str, Any]:
    reference_paths = detect_adobe_reference_paths(pdf_path)
    references = {
        "docx": inspect_docx(reference_paths["docx"]),
        "html": inspect_html(reference_paths["html"]),
        "xml": inspect_xml(reference_paths["xml"]),
        "html_asset_dir": inspect_asset_dir(reference_paths["html_asset_dir"]),
        "print_pdf": inspect_file(reference_paths["print_pdf"], reference_kind="adobe_print_pdf"),
        "postscript": inspect_file(reference_paths["postscript"], reference_kind="adobe_print_postscript"),
        "image_exports": inspect_image_exports(reference_paths["image_dir"], pdf_path.stem),
    }
    observations = comparison_observations(manifest, references)
    return {
        "report_kind": "adobe_reference_comparison",
        "comparison_policy": REFERENCE_POLICY,
        "source_pdf": inspect_file(pdf_path, reference_kind="source_pdf"),
        "pipeline_manifest_summary": {
            "manifest_version": manifest.get("manifest_version"),
            "input_file_name": manifest.get("source_package", {}).get("input_file_name"),
            "input_file_path": manifest.get("source_package", {}).get("input_file_path"),
            "total_pages": manifest.get("document_summary", {}).get("total_pages"),
            "raw_block_count": manifest.get("document_summary", {}).get("raw_block_count"),
            "normalized_block_count": manifest.get("document_summary", {}).get("normalized_block_count"),
            "annotation_count": manifest.get("document_summary", {}).get("annotation_count"),
            "warning_count": len(manifest.get("document_warning_entries", [])),
            "review_item_count": len(manifest.get("review_entries", [])),
        },
        "reference_summary": {
            "any_reference_present": any_reference_present(references),
            "present_reference_kinds": [
                reference_kind for reference_kind, reference in references.items() if reference.get("present")
            ],
            "missing_reference_kinds": [
                reference_kind for reference_kind, reference in references.items() if not reference.get("present")
            ],
        },
        "references": references,
        "comparison_observations": observations,
        "next_use": [
            "Use these facts to compare Adobe's export choices against pipeline extraction, normalization, and draft output.",
            "Prefer repeated successes across Adobe exports as hints, not as unreviewed truth.",
            "Treat Adobe failures as useful negative examples when improving normalization and projection.",
        ],
    }


def detect_adobe_reference_paths(pdf_path: Path) -> dict[str, Path]:
    parent = pdf_path.parent
    stem = pdf_path.stem
    return {
        "docx": parent / f"{stem}.docx",
        "html": parent / f"{stem}.html",
        "xml": parent / f"{stem}.xml",
        "html_asset_dir": parent / f"{stem}_files",
        "print_pdf": parent / f"{stem}_print_pdf.pdf",
        "postscript": parent / f"{stem}-1_print_postscript.ps",
        "image_dir": parent / "images",
    }


def inspect_file(path: Path, *, reference_kind: str) -> dict[str, Any]:
    return {
        "reference_kind": reference_kind,
        "path": str(path),
        "file_name": path.name,
        "present": path.exists(),
        "byte_size": path.stat().st_size if path.exists() and path.is_file() else None,
    }


def inspect_docx(path: Path) -> dict[str, Any]:
    data = inspect_file(path, reference_kind="adobe_docx_export")
    data.update(
        {
            "paragraph_count": None,
            "table_count": None,
            "image_count": None,
            "header_part_count": None,
            "footer_part_count": None,
            "numbering_present": None,
            "text_character_count": None,
            "text_sample": [],
            "parse_warning": None,
        }
    )
    if not data["present"]:
        return data

    try:
        with ZipFile(path) as docx_zip:
            names = docx_zip.namelist()
            document_xml = docx_zip.read("word/document.xml").decode("utf-8", errors="replace")
            text_runs = extract_word_text_runs(document_xml)
            data.update(
                {
                    "paragraph_count": count_regex(document_xml, r"<w:p(?:\s|>)"),
                    "table_count": count_regex(document_xml, r"<w:tbl(?:\s|>)"),
                    "image_count": sum(1 for name in names if name.startswith("word/media/")),
                    "header_part_count": sum(1 for name in names if name.startswith("word/header") and name.endswith(".xml")),
                    "footer_part_count": sum(1 for name in names if name.startswith("word/footer") and name.endswith(".xml")),
                    "numbering_present": "word/numbering.xml" in names,
                    "text_character_count": len(" ".join(text_runs)),
                    "text_sample": text_runs[:12],
                }
            )
    except (BadZipFile, KeyError, OSError) as exc:
        data["parse_warning"] = f"Could not inspect DOCX export: {exc}"
    return data


def inspect_html(path: Path) -> dict[str, Any]:
    data = inspect_file(path, reference_kind="adobe_html_export")
    data.update(
        {
            "table_count": None,
            "image_count": None,
            "heading_count": None,
            "alt_attribute_count": None,
            "linked_asset_count": None,
            "text_character_count": None,
            "text_sample": [],
            "parse_warning": None,
        }
    )
    if not data["present"]:
        return data

    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        visible_text = html_visible_text(text)
        data.update(
            {
                "table_count": count_regex(text, r"<table\b", re.IGNORECASE),
                "image_count": count_regex(text, r"<img\b", re.IGNORECASE),
                "heading_count": count_regex(text, r"<h[1-6]\b", re.IGNORECASE),
                "alt_attribute_count": count_regex(text, r"\salt\s*=", re.IGNORECASE),
                "linked_asset_count": len(re.findall(r"\bsrc\s*=\s*['\"]([^'\"]+)['\"]", text, flags=re.IGNORECASE)),
                "text_character_count": len(" ".join(visible_text)),
                "text_sample": visible_text[:12],
            }
        )
    except OSError as exc:
        data["parse_warning"] = f"Could not inspect HTML export: {exc}"
    return data


def inspect_xml(path: Path) -> dict[str, Any]:
    data = inspect_file(path, reference_kind="adobe_xml_export")
    data.update(
        {
            "tagged_pdf_doc_present": None,
            "paragraph_tag_count": None,
            "list_tag_count": None,
            "list_item_tag_count": None,
            "table_tag_count": None,
            "table_row_tag_count": None,
            "table_cell_tag_count": None,
            "figure_tag_count": None,
            "actual_text_attribute_count": None,
            "alt_attribute_count": None,
            "workbook_tag_count": None,
            "worksheet_tag_count": None,
            "text_character_count": None,
            "text_sample": [],
            "parse_warning": None,
        }
    )
    if not data["present"]:
        return data

    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        text_sample = xml_visible_text(text)
        data.update(
            {
                "tagged_pdf_doc_present": "<TaggedPDF-doc" in text,
                "paragraph_tag_count": count_regex(text, r"<P(?:\s|>)"),
                "list_tag_count": count_regex(text, r"<L(?:\s|>)"),
                "list_item_tag_count": count_regex(text, r"<LI(?:\s|>)"),
                "table_tag_count": count_regex(text, r"<Table(?:\s|>)"),
                "table_row_tag_count": count_regex(text, r"<TR(?:\s|>)"),
                "table_cell_tag_count": count_regex(text, r"<T[DH](?:\s|>)"),
                "figure_tag_count": count_regex(text, r"<Figure(?:\s|>)"),
                "actual_text_attribute_count": count_regex(text, r"\bActualText\s*="),
                "alt_attribute_count": count_regex(text, r"\bAlt\s*="),
                "workbook_tag_count": count_regex(text, r"<Workbook(?:\s|>)"),
                "worksheet_tag_count": count_regex(text, r"<Worksheet(?:\s|>)"),
                "text_character_count": len(" ".join(text_sample)),
                "text_sample": text_sample[:12],
            }
        )
    except OSError as exc:
        data["parse_warning"] = f"Could not inspect XML export: {exc}"
    return data


def inspect_asset_dir(path: Path) -> dict[str, Any]:
    data = {
        "reference_kind": "adobe_html_asset_dir",
        "path": str(path),
        "directory_name": path.name,
        "present": path.exists() and path.is_dir(),
        "asset_count": None,
        "png_count": None,
        "jpg_count": None,
        "other_file_count": None,
        "total_byte_size": None,
        "sample_files": [],
    }
    if not data["present"]:
        return data

    files = sorted(file_path for file_path in path.iterdir() if file_path.is_file())
    data.update(
        {
            "asset_count": len(files),
            "png_count": sum(1 for file_path in files if file_path.suffix.lower() == ".png"),
            "jpg_count": sum(1 for file_path in files if file_path.suffix.lower() in {".jpg", ".jpeg"}),
            "other_file_count": sum(1 for file_path in files if file_path.suffix.lower() not in {".png", ".jpg", ".jpeg"}),
            "total_byte_size": sum(file_path.stat().st_size for file_path in files),
            "sample_files": [file_path.name for file_path in files[:12]],
        }
    )
    return data


def inspect_image_exports(image_dir: Path, stem: str) -> dict[str, Any]:
    data = {
        "reference_kind": "adobe_image_exports",
        "path": str(image_dir),
        "directory_name": image_dir.name,
        "present": image_dir.exists() and image_dir.is_dir(),
        "matching_image_count": None,
        "total_byte_size": None,
        "sample_files": [],
    }
    if not data["present"]:
        return data

    images = sorted(
        file_path
        for file_path in image_dir.iterdir()
        if file_path.is_file() and file_path.name.startswith(f"{stem}_img_")
    )
    data.update(
        {
            "present": bool(images),
            "matching_image_count": len(images),
            "total_byte_size": sum(file_path.stat().st_size for file_path in images),
            "sample_files": [file_path.name for file_path in images[:12]],
        }
    )
    return data


def comparison_observations(manifest: dict[str, Any], references: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    observations = [
        {
            "code": "ADOBE_REFERENCE_POLICY",
            "severity": "info",
            "message": REFERENCE_POLICY,
        }
    ]
    docx = references["docx"]
    html = references["html"]
    xml = references["xml"]
    assets = references["html_asset_dir"]

    if docx.get("present"):
        observations.append(
            {
                "code": "ADOBE_DOCX_AVAILABLE",
                "severity": "info",
                "message": "Adobe DOCX export is available for draft output comparison.",
                "facts": pick(docx, "paragraph_count", "table_count", "image_count", "header_part_count", "footer_part_count"),
            }
        )
    if html.get("present"):
        observations.append(
            {
                "code": "ADOBE_HTML_AVAILABLE",
                "severity": "info",
                "message": "Adobe HTML export is available for structure and asset-reference comparison.",
                "facts": pick(html, "heading_count", "table_count", "image_count", "alt_attribute_count"),
            }
        )
    if xml.get("present"):
        observations.append(
            {
                "code": "ADOBE_XML_AVAILABLE",
                "severity": "info",
                "message": "Adobe XML export is available for tag and attribute comparison.",
                "facts": pick(
                    xml,
                    "tagged_pdf_doc_present",
                    "paragraph_tag_count",
                    "table_tag_count",
                    "figure_tag_count",
                    "actual_text_attribute_count",
                    "alt_attribute_count",
                ),
            }
        )
    if assets.get("present"):
        observations.append(
            {
                "code": "ADOBE_ASSETS_AVAILABLE",
                "severity": "info",
                "message": "Adobe exported image assets are available for image/figure comparison.",
                "facts": pick(assets, "asset_count", "png_count", "jpg_count"),
            }
        )

    normalized_count = manifest.get("document_summary", {}).get("normalized_block_count") or 0
    if normalized_count == 0 and any_reference_present(references):
        observations.append(
            {
                "code": "NORMALIZATION_NOT_READY_FOR_REFERENCE_COMPARISON",
                "severity": "warning",
                "message": "Adobe references exist, but the manifest has no normalized blocks to compare against yet.",
            }
        )
    return observations


def build_adobe_reference_markdown(report: dict[str, Any]) -> str:
    source_pdf = report["source_pdf"]
    summary = report["pipeline_manifest_summary"]
    references = report["references"]
    lines = [
        "# Adobe Reference Comparison",
        "",
        report["comparison_policy"],
        "",
        "## Source",
        "",
        f"- PDF: `{source_pdf['file_name']}`",
        f"- Pages: {summary.get('total_pages')}",
        f"- Raw blocks: {summary.get('raw_block_count')}",
        f"- Normalized blocks: {summary.get('normalized_block_count')}",
        f"- Warnings: {summary.get('warning_count')}",
        f"- Review items: {summary.get('review_item_count')}",
        "",
        "## References Found",
        "",
    ]
    for reference_name, reference in references.items():
        present = "yes" if reference.get("present") else "no"
        lines.append(f"- {reference_name}: {present}")

    lines.extend(["", "## Reference Facts", ""])
    for reference_name, reference in references.items():
        if not reference.get("present"):
            continue
        lines.extend([f"### {reference_name}", ""])
        for key, value in reference.items():
            if key in {"path", "reference_kind", "present"}:
                continue
            lines.append(f"- {key}: {markdown_value(value)}")
        lines.append("")

    lines.extend(["## Observations", ""])
    for observation in report["comparison_observations"]:
        lines.append(f"- `{observation['code']}` ({observation['severity']}): {observation['message']}")
    lines.append("")
    return "\n".join(lines)


def any_reference_present(references: dict[str, dict[str, Any]]) -> bool:
    return any(reference.get("present") for reference in references.values())


def extract_word_text_runs(document_xml: str) -> list[str]:
    runs = re.findall(r"<w:t[^>]*>(.*?)</w:t>", document_xml, flags=re.DOTALL)
    return [unescape(strip_tags(run)).strip() for run in runs if unescape(strip_tags(run)).strip()]


def html_visible_text(text: str) -> list[str]:
    text = re.sub(r"(?is)<script\b.*?</script>", " ", text)
    text = re.sub(r"(?is)<style\b.*?</style>", " ", text)
    return compact_text_items(re.split(r"\s{2,}", strip_tags(text)))


def xml_visible_text(text: str) -> list[str]:
    text = re.sub(r"(?is)<\?xpacket.*?\?>", " ", text)
    text = re.sub(r"(?is)<x:xmpmeta\b.*?</x:xmpmeta>", " ", text)
    return compact_text_items(re.split(r"\s{2,}", strip_tags(text)))


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text)


def compact_text_items(items: list[str]) -> list[str]:
    compacted: list[str] = []
    for item in items:
        cleaned = unescape(re.sub(r"\s+", " ", item)).strip()
        if cleaned:
            compacted.append(cleaned)
    return compacted


def count_regex(text: str, pattern: str, flags: int = 0) -> int:
    return len(re.findall(pattern, text, flags=flags))


def pick(data: dict[str, Any], *keys: str) -> dict[str, Any]:
    return {key: data.get(key) for key in keys}


def markdown_value(value: Any) -> str:
    if isinstance(value, list):
        return ", ".join(f"`{item}`" for item in value) if value else "[]"
    return f"`{value}`"
