from __future__ import annotations

import json
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any

from accessibility_by_manifest.inputs.pdf.paths import PdfOutputPaths


PDF_EXTRACTOR_NAMES = ("pymupdf", "pypdf", "pikepdf", "pdfminer.six")


def write_json_manifest(path: Path, data: dict[str, Any], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Output already exists. Use --overwrite or choose another folder: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json", dir=str(path.parent), prefix=f"{path.stem}_") as temp_file:
            temp_path = Path(temp_file.name)
        temp_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        temp_path.replace(path)
    except Exception:
        if temp_path and temp_path.exists():
            temp_path.unlink(missing_ok=True)
        raise


def write_pdf_manifest_bundle(output_paths: PdfOutputPaths, manifest: dict[str, Any], overwrite: bool) -> None:
    write_json_manifest(output_paths.manifest_json, manifest, overwrite)
    for extractor_name in PDF_EXTRACTOR_NAMES:
        write_json_manifest(
            output_paths.extractor_manifest_json(extractor_name),
            extractor_manifest_view(manifest, extractor_name),
            overwrite,
        )


def extractor_manifest_view(manifest: dict[str, Any], extractor_name: str) -> dict[str, Any]:
    data = deepcopy(manifest)
    extractor_versions = manifest.get("extractor_provenance", {}).get("extractor_versions", {})
    data["extractor_provenance"] = {
        "primary_extractor": extractor_name,
        "secondary_extractors": [],
        "extractor_versions": {extractor_name: extractor_versions.get(extractor_name)},
        "source_manifest_kind": manifest.get("manifest_kind"),
        "source_manifest_version": manifest.get("manifest_version"),
        "source_manifest_extractors": list(extractor_versions.keys()),
        "filter_scope": "single_extractor_view",
        "notes": ["Derived from the master manifest without rerunning extraction."],
    }
    data["extractor_evidence"] = keep_extractor_evidence(manifest.get("extractor_evidence", {}), extractor_name)
    data["document_warning_entries"] = [
        warning for warning in manifest.get("document_warning_entries", []) if warning_belongs_to_extractor(warning, extractor_name)
    ]
    data["page_entries"] = [extractor_page_entry(page_entry, extractor_name) for page_entry in manifest.get("page_entries", [])]
    data["raw_block_entries"] = [
        extractor_block_entry(block_entry, extractor_name)
        for block_entry in manifest.get("raw_block_entries", [])
        if extractor_name in block_entry.get("extractor_evidence", {})
    ]
    data["normalized_block_entries"] = [
        extractor_block_entry(block_entry, extractor_name)
        for block_entry in manifest.get("normalized_block_entries", [])
        if extractor_name in block_entry.get("extractor_evidence", {})
    ]
    update_extractor_summary(data)
    return data


def extractor_page_entry(page_entry: dict[str, Any], extractor_name: str) -> dict[str, Any]:
    page = deepcopy(page_entry)
    page["extractor_evidence"] = keep_extractor_evidence(page_entry.get("extractor_evidence", {}), extractor_name)
    page["warning_entries"] = [
        warning for warning in page_entry.get("warning_entries", []) if warning_belongs_to_extractor(warning, extractor_name)
    ]
    if extractor_name != "pymupdf":
        page["annotation_entries"] = []
    if extractor_name != "pikepdf":
        page["operator_evidence"] = None
    return page


def extractor_block_entry(block_entry: dict[str, Any], extractor_name: str) -> dict[str, Any]:
    block = deepcopy(block_entry)
    block["extractor_evidence"] = keep_extractor_evidence(block_entry.get("extractor_evidence", {}), extractor_name)
    return block


def keep_extractor_evidence(evidence: dict[str, Any], extractor_name: str) -> dict[str, Any]:
    return {extractor_name: deepcopy(evidence[extractor_name])} if extractor_name in evidence else {}


def warning_belongs_to_extractor(warning: dict[str, Any], extractor_name: str) -> bool:
    warning_code = str(warning.get("warning_code", "")).lower()
    extractor_aliases = {
        "pymupdf": ("pymupdf", "fitz"),
        "pypdf": ("pypdf",),
        "pikepdf": ("pikepdf",),
        "pdfminer.six": ("pdfminer", "pdfminersix"),
    }
    return any(warning_code.startswith(alias) for alias in extractor_aliases.get(extractor_name, (extractor_name,)))


def update_extractor_summary(manifest: dict[str, Any]) -> None:
    summary = manifest.get("document_summary", {})
    page_entries = manifest.get("page_entries", [])
    raw_block_entries = manifest.get("raw_block_entries", [])
    normalized_block_entries = manifest.get("normalized_block_entries", [])
    summary["pages_with_warnings"] = sum(1 for page in page_entries if page.get("warning_entries"))
    summary["raw_block_count"] = len(raw_block_entries)
    summary["normalized_block_count"] = len(normalized_block_entries)
    summary["annotation_count"] = sum(len(page.get("annotation_entries", [])) for page in page_entries)
    summary["form_field_count"] = sum(int(page.get("observed_source", {}).get("form_field_count") or 0) for page in page_entries)


def write_yaml_manifest(path: Path, data: dict[str, Any], overwrite: bool) -> None:
    import yaml

    atomic_write_text(path, yaml.safe_dump(data, sort_keys=False, allow_unicode=True), overwrite)


def atomic_write_text(path: Path, content: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Output already exists. Use --overwrite or choose another folder: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=path.suffix or ".tmp", dir=str(path.parent), prefix=f"{path.stem}_") as temp_file:
            temp_path = Path(temp_file.name)
        temp_path.write_text(content, encoding="utf-8")
        temp_path.replace(path)
    except Exception:
        if temp_path and temp_path.exists():
            temp_path.unlink(missing_ok=True)
        raise
