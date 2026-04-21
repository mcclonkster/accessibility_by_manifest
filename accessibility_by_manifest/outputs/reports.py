from __future__ import annotations

import json
import tempfile
from pathlib import Path

from accessibility_by_manifest.errors import OutputWriteError
from accessibility_by_manifest.inputs.pptx.paths import OutputPaths
from accessibility_by_manifest.manifest.pptx import Manifest


def write_manifest_files(manifest: Manifest, output_paths: OutputPaths, overwrite: bool) -> None:
    import yaml

    data = manifest.to_dict()
    atomic_write_text(output_paths.manifest_json, json.dumps(data, indent=2, ensure_ascii=False) + "\n", overwrite)
    atomic_write_text(output_paths.manifest_yaml, yaml.safe_dump(data, sort_keys=False, allow_unicode=True), overwrite)


def write_reports(manifest: Manifest, output_paths: OutputPaths, overwrite: bool) -> None:
    atomic_write_text(output_paths.extract_report, build_extract_report(manifest), overwrite)
    atomic_write_text(output_paths.review_notes, build_review_notes(manifest), overwrite)
    atomic_write_text(output_paths.review_report, build_review_report(manifest, output_paths), overwrite)


def write_review_outputs(manifest: Manifest, output_paths: OutputPaths, overwrite: bool) -> None:
    write_reports(manifest, output_paths, overwrite)


def build_extract_report(manifest: Manifest) -> str:
    summary = manifest.summary()
    lines = [
        "# Extract Report",
        "",
        "## Manifest Summary",
        "",
        f"- Total slides: {summary['total_slides']}",
        f"- Slides with warnings: {summary['slides_with_warnings']}",
        f"- Detected visual entries: {summary['detected_visual_entries']}",
        f"- Detected visual entries missing descriptions: {summary['detected_visual_entries_missing_descriptions']}",
        "",
    ]
    for slide in manifest.slides:
        lines.extend(
            [
                f"## Slide {slide.slide_number}. {slide.title}",
                "",
                f"- Preview image: {slide.preview_image or '[missing]'}",
                f"- Text blocks: {len(slide.text_blocks)}",
                f"- Visual entries: {len(slide.visuals)}",
                f"- Manual review required: {'Yes' if slide.needs_manual_review else 'No'}",
                "",
            ]
        )
    return "\n".join(lines)


def build_review_notes(manifest: Manifest) -> str:
    lines = ["# Review Notes", ""]
    for slide in manifest.slides:
        warnings = list(slide.warnings)
        for block in slide.text_blocks:
            warnings.extend(block.warnings)
            for paragraph in block.paragraphs:
                warnings.extend(paragraph.warnings)
        for visual in slide.visuals:
            warnings.extend(visual.warnings)
        if not warnings:
            continue
        lines.extend([f"## Slide {slide.slide_number}. {slide.title}", ""])
        for warning in warnings:
            lines.append(f"- {warning.code}: {warning.message}")
        lines.append("")
    if len(lines) == 2:
        lines.append("No warnings were generated.")
    return "\n".join(lines)


def build_review_report(manifest: Manifest, output_paths: OutputPaths) -> str:
    summary = manifest.summary()
    missing_images = sum(1 for slide in manifest.slides if not slide.preview_image)
    return "\n".join(
        [
            "# Review Report",
            "",
            f"- Source PPTX: {manifest.source_path}",
            f"- Companion DOCX: {output_paths.companion_docx}",
            f"- Slides DOCX: {output_paths.slides_docx}",
            f"- Slides Markdown: {output_paths.slides_markdown}",
            f"- Slides processed: {summary['total_slides']}",
            f"- Slides with warnings: {summary['slides_with_warnings']}",
            f"- Detected visual entries: {summary['detected_visual_entries']}",
            f"- Slides missing images: {missing_images}",
            "",
            "Manual review is still required for the slides DOCX.",
            "",
        ]
    )


def atomic_write_text(path: Path, content: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise OutputWriteError(f"Output already exists. Use --overwrite or choose another folder: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=path.suffix or ".tmp", dir=str(path.parent), prefix=f"{path.stem}_") as temp_file:
            temp_path = Path(temp_file.name)
        temp_path.write_text(content, encoding="utf-8")
        temp_path.replace(path)
    except Exception as exc:
        if temp_path and temp_path.exists():
            temp_path.unlink(missing_ok=True)
        raise OutputWriteError(f"Failed to write file '{path}': {exc}") from exc
