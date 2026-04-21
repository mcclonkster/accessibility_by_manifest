from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..config import PdfWorkflowConfig
from ..paths import PdfOutputPaths
from ..util.fingerprints import file_sha256


def warning_entry(code: str, message: str, scope: str, severity: str = "warning", manual_review_required: bool = True) -> dict[str, Any]:
    return {
        "warning_code": code,
        "warning_message": message,
        "warning_scope": scope,
        "warning_severity": severity,
        "manual_review_required": manual_review_required,
    }


@dataclass
class ManifestBuilder:
    input_path: Path
    output_paths: PdfOutputPaths
    config: PdfWorkflowConfig
    page_count: int = 0
    byte_length: int | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    xmp_present: bool = False
    page_entries: list[dict[str, Any]] = field(default_factory=list)
    raw_block_entries: list[dict[str, Any]] = field(default_factory=list)
    document_warning_entries: list[dict[str, Any]] = field(default_factory=list)
    annotation_count: int = 0
    form_field_count: int = 0
    figure_candidate_count: int = 0

    def build(self) -> dict[str, Any]:
        pages_with_warnings = sum(1 for page in self.page_entries if page["warning_entries"])
        image_only_pages_present = any(page["observed_source"]["image_only_page_suspected"] for page in self.page_entries)
        ocr_required = image_only_pages_present
        ocr_detected = any(page["observed_source"]["ocr_text_detected"] for page in self.page_entries)
        title = clean_metadata_value(self.metadata.get("title"))
        document_title_strategy = "metadata_title" if title else "manual_review"
        return {
            "manifest_version": "0.1",
            "manifest_kind": "pdf_to_docx_accessibility_manifest",
            "source_package": {
                "format_family": "PDF",
                "input_file_name": self.input_path.name,
                "input_file_path": str(self.input_path),
                "page_count": self.page_count,
                "document_fingerprints": [file_sha256(self.input_path)],
                "byte_length": self.byte_length,
            },
            "target_package": {
                "format_family": "OOXML",
                "package_model": "OPC",
                "document_vocabulary": "WordprocessingML",
                "draft_output_file_name": self.output_paths.projected_docx.name,
                "draft_output_file_path": str(self.output_paths.projected_docx),
            },
            "run_config": {
                "include_preview_images": self.config.include_preview_images,
                "preview_image_dir": str(self.output_paths.preview_image_dir) if self.config.include_preview_images else None,
                "page_separator_mode": self.config.page_separator_mode,
                "include_warning_appendix": self.config.include_warning_appendix,
                "include_page_traceback": self.config.include_page_traceback,
                "prefer_outline_for_headings": self.config.prefer_outline_for_headings,
            },
            "document_summary": {
                "total_pages": self.page_count,
                "pages_with_warnings": pages_with_warnings,
                "raw_block_count": len(self.raw_block_entries),
                "normalized_block_count": 0,
                "annotation_count": self.annotation_count,
                "form_field_count": self.form_field_count,
                "figure_candidate_count": self.figure_candidate_count,
            },
            "document_metadata": {
                "info": {key: clean_metadata_value(value) for key, value in self.metadata.items()},
                "xmp_present": self.xmp_present,
                "title": title,
                "author": clean_metadata_value(self.metadata.get("author")),
                "subject": clean_metadata_value(self.metadata.get("subject")),
                "keywords": clean_metadata_value(self.metadata.get("keywords")),
                "language": clean_metadata_value(self.metadata.get("language")),
            },
            "document_accessibility": {
                "mark_info": None,
                "tagged_pdf_detected": None,
                "struct_tree_detected": None,
                "image_only_pages_present": image_only_pages_present,
                "ocr_required": ocr_required,
                "ocr_detected": ocr_detected,
                "reading_order_source": "layout_inference",
            },
            "document_navigation": {
                "outline_present": None,
                "outline_entries": None,
                "page_labels": None,
                "named_destinations_present": None,
                "named_destinations": None,
                "viewer_preferences": None,
                "page_layout": None,
                "page_mode": None,
            },
            "document_security": {
                "permissions": None,
            },
            "document_interactivity": {
                "javascript_present": None,
                "javascript_actions": None,
                "forms_present": self.form_field_count > 0,
                "form_fields": None,
                "calculation_order_ids": None,
                "xfa_present": None,
                "is_pure_xfa": None,
                "all_xfa_html": None,
            },
            "document_warning_entries": self.document_warning_entries,
            "page_entries": self.page_entries,
            "raw_block_entries": self.raw_block_entries,
            "normalized_block_entries": [],
            "projected_target": {
                "target_package_part": "word/document.xml",
                "document_title_strategy": document_title_strategy,
                "page_separator_mode": self.config.page_separator_mode,
                "include_warning_appendix": self.config.include_warning_appendix,
                "projection_status": "planned",
            },
        }


def clean_metadata_value(value: object) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
