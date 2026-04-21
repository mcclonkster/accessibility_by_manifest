from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class WarningEntry:
    code: str
    message: str
    scope: str
    manual_review_required: bool = True

    def to_manifest(self) -> dict[str, Any]:
        return {
            "warning_code": self.code,
            "warning_message": self.message,
            "warning_scope": self.scope,
            "manual_review_required": self.manual_review_required,
        }


@dataclass(frozen=True)
class ParagraphEntry:
    text: str
    level: int = 0
    list_kind: str = "plain"
    list_marker_hint: str = ""
    warnings: tuple[WarningEntry, ...] = ()


@dataclass(frozen=True)
class TextBlockEntry:
    source_name: str
    source_text_container_type: str
    placeholder_type: str | None
    interpreted_text_role: str
    role_confidence: str
    auto_merge_allowed: bool
    order: int
    paragraphs: tuple[ParagraphEntry, ...]
    warnings: tuple[WarningEntry, ...] = ()


@dataclass(frozen=True)
class VisualEntry:
    label: str
    visual_type: str
    description: str
    description_source: str
    warnings: tuple[WarningEntry, ...] = ()


@dataclass(frozen=True)
class SlideEntry:
    slide_number: int
    title: str
    title_source: str
    preview_image: str | None
    text_blocks: tuple[TextBlockEntry, ...]
    visuals: tuple[VisualEntry, ...]
    warnings: tuple[WarningEntry, ...] = ()

    @property
    def needs_manual_review(self) -> bool:
        return bool(self.warnings or any(block.warnings for block in self.text_blocks) or any(v.warnings for v in self.visuals))


@dataclass(frozen=True)
class Manifest:
    source_path: Path
    output_docx_path: Path
    preview_image_dir: Path | None
    slides: tuple[SlideEntry, ...]
    warnings: tuple[WarningEntry, ...] = ()
    manifest_version: str = "1.0"
    manifest_kind: str = "pptx_accessibility_manifest"

    def summary(self) -> dict[str, int]:
        visual_count = sum(len(slide.visuals) for slide in self.slides)
        missing_descriptions = sum(1 for slide in self.slides for visual in slide.visuals if visual.description_source == "missing")
        return {
            "total_slides": len(self.slides),
            "slides_with_warnings": sum(1 for slide in self.slides if slide.needs_manual_review),
            "detected_visual_entries": visual_count,
            "detected_visual_entries_missing_descriptions": missing_descriptions,
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "manifest_version": self.manifest_version,
            "manifest_kind": self.manifest_kind,
            "source_package": {
                "format_family": "OOXML",
                "package_model": "OPC",
                "document_vocabulary": "PresentationML",
                "input_file_name": self.source_path.name,
                "input_file_path": str(self.source_path),
            },
            "target_package": {
                "format_family": "OOXML",
                "package_model": "OPC",
                "document_vocabulary": "WordprocessingML",
                "draft_output_file_name": self.output_docx_path.name,
                "draft_output_file_path": str(self.output_docx_path),
            },
            "run_config": {
                "include_preview_images": self.preview_image_dir is not None,
                "preview_image_dir": str(self.preview_image_dir) if self.preview_image_dir else None,
                "slide_separator_mode": "PAGE_BREAK",
            },
            "manifest_summary": self.summary(),
            "manifest_warning_entries": [warning.to_manifest() for warning in self.warnings],
            "slide_entries": [slide_to_manifest(slide) for slide in self.slides],
        }


def slide_to_manifest(slide: SlideEntry) -> dict[str, Any]:
    return {
        "slide_number": slide.slide_number,
        "observed_source": {
            "package_part": f"ppt/slides/slide{slide.slide_number}.xml",
            "presentationml_root": "p:sld",
            "preview_image_candidates": [slide.preview_image] if slide.preview_image else [],
        },
        "normalized_workflow": {
            "chosen_title": slide.title,
            "title_source": slide.title_source,
            "manual_review_required": slide.needs_manual_review,
        },
        "projected_target": {
            "target_package_part": "word/document.xml",
            "projected_slide_heading_text": f"Slide {slide.slide_number}. {slide.title}",
            "projected_slide_heading_style": "Heading1",
            "projected_slide_separator_mode": "PAGE_BREAK",
            "projection_status": "planned",
        },
        "warning_entries": [warning.to_manifest() for warning in slide.warnings],
        "text_block_entries": [text_block_to_manifest(block) for block in slide.text_blocks],
        "visual_entries": [visual_to_manifest(visual) for visual in slide.visuals],
    }


def text_block_to_manifest(block: TextBlockEntry) -> dict[str, Any]:
    return {
        "observed_source": {
            "source_text_container_type": block.source_text_container_type,
            "placeholder_type": block.placeholder_type,
            "shape_name": block.source_name,
        },
        "normalized_workflow": {
            "source_name": block.source_name,
            "ordered_position": block.order,
            "interpreted_text_role": block.interpreted_text_role,
            "role_confidence": block.role_confidence,
            "auto_merge_allowed": block.auto_merge_allowed,
        },
        "warning_entries": [warning.to_manifest() for warning in block.warnings],
        "paragraph_entries": [paragraph_to_manifest(paragraph) for paragraph in block.paragraphs],
    }


def paragraph_to_manifest(paragraph: ParagraphEntry) -> dict[str, Any]:
    return {
        "normalized_workflow": {
            "text": paragraph.text,
            "level": paragraph.level,
            "list_kind": paragraph.list_kind,
            "list_marker_hint": paragraph.list_marker_hint,
        },
        "warning_entries": [warning.to_manifest() for warning in paragraph.warnings],
    }


def visual_to_manifest(visual: VisualEntry) -> dict[str, Any]:
    return {
        "normalized_workflow": {
            "label": visual.label,
            "visual_type": visual.visual_type,
            "description": visual.description,
            "description_source": visual.description_source,
            "manual_review_required": True,
        },
        "warning_entries": [warning.to_manifest() for warning in visual.warnings],
    }
