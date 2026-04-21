from __future__ import annotations

import os
from pathlib import Path

from accessibility_by_manifest.inputs.pptx.paths import OutputPaths
from accessibility_by_manifest.manifest.pptx import Manifest, ParagraphEntry, SlideEntry
from accessibility_by_manifest.outputs.docx_accessibility import slide_image_alt_text
from accessibility_by_manifest.outputs.reports import atomic_write_text


def write_slides_markdown(manifest: Manifest, output_paths: OutputPaths, overwrite: bool) -> None:
    atomic_write_text(output_paths.slides_markdown, build_slides_markdown(manifest, output_paths.slides_markdown), overwrite)


def write_markdown_outputs(manifest: Manifest, output_paths: OutputPaths, overwrite: bool) -> None:
    write_slides_markdown(manifest, output_paths, overwrite)


def build_slides_markdown(manifest: Manifest, markdown_path: Path) -> str:
    lines = [f"# {manifest.source_path.stem} slides", ""]
    for slide in manifest.slides:
        lines.extend(slide_markdown(slide, manifest, markdown_path))
    return "\n".join(lines).rstrip() + "\n"


def slide_markdown(slide: SlideEntry, manifest: Manifest, markdown_path: Path) -> list[str]:
    lines = [f"## Slide {slide.slide_number}. {slide.title}", ""]
    image_line = slide_image_markdown(slide, manifest, markdown_path)
    if image_line:
        lines.extend([image_line, ""])
    else:
        lines.extend(["[Slide image unavailable. Review required.]", ""])

    paragraphs = [paragraph for block in sorted(slide.text_blocks, key=lambda item: item.order) for paragraph in block.paragraphs]
    if paragraphs:
        lines.extend(["### Slide text", ""])
        for paragraph in paragraphs:
            lines.append(paragraph_markdown(paragraph))
        lines.append("")

    if slide.visuals:
        lines.extend(["### Visual descriptions", ""])
        for visual in slide.visuals:
            description = visual.description or "Description metadata missing. Review needed."
            lines.append(f"- **{escape_markdown_text(visual.label)}. {escape_markdown_text(visual.visual_type.capitalize())}:** {escape_markdown_text(description)}")
        lines.append("")

    return lines


def slide_image_markdown(slide: SlideEntry, manifest: Manifest, markdown_path: Path) -> str:
    if manifest.preview_image_dir is None or slide.preview_image is None:
        return ""
    image_path = manifest.preview_image_dir / slide.preview_image
    alt_text, title_text = slide_image_alt_text(slide.slide_number, slide.title)
    relative_path = Path(os.path.relpath(image_path, markdown_path.parent))
    return f"![{escape_alt_text(alt_text)}](<{escape_markdown_destination(relative_path)}> \"{escape_title_text(title_text)}\")"


def paragraph_markdown(paragraph: ParagraphEntry) -> str:
    text = escape_markdown_text(paragraph.text)
    indent = "  " * max(paragraph.level, 0)
    if paragraph.list_kind == "bullet":
        return f"{indent}- {text}"
    if paragraph.list_kind == "number":
        return f"{indent}1. {text}"
    return text


def escape_alt_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]").replace("\n", " ")


def escape_title_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def escape_markdown_destination(path: Path) -> str:
    return path.as_posix().replace(">", "%3E")


def escape_markdown_text(value: str) -> str:
    replacements = {
        "\\": "\\\\",
        "*": "\\*",
        "_": "\\_",
        "`": "\\`",
        "[": "\\[",
        "]": "\\]",
    }
    output = value
    for old, new in replacements.items():
        output = output.replace(old, new)
    return output
