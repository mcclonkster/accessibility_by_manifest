from __future__ import annotations

import html
from pathlib import Path

from accessibility_by_manifest.normalize import NormalizedAccessibilityDocument
from accessibility_by_manifest.outputs.manifest import atomic_write_text
from accessibility_by_manifest.outputs.projection import (
    html_tag_hint_for_unit,
    projection_status_allows_output,
)


def build_accessible_html(document: NormalizedAccessibilityDocument) -> str:
    title = document.document.title or document.source_package.input_file_name
    lang = document.document.primary_language or "en"
    body_parts: list[str] = []
    rendered_table_ids: set[str] = set()
    list_buffer: list[str] = []
    has_explicit_heading = any(
        unit.unit_type == "heading"
        and projection_status_allows_output(unit.projection_hints)
        and unit.unit_type != "artifact"
        for unit in _ordered_units(document)
    )
    promoted_title_heading = False

    for unit in _ordered_units(document):
        if not projection_status_allows_output(unit.projection_hints):
            continue
        if unit.unit_type == "artifact":
            continue

        if unit.unit_type == "list_item":
            list_buffer.append(_render_list_item(unit))
            continue
        if list_buffer:
            body_parts.append("<ul>")
            body_parts.extend(list_buffer)
            body_parts.append("</ul>")
            list_buffer = []

        if unit.unit_type in {"table", "table_cell"}:
            table_id = str(unit.structure.get("table_id") or unit.content.get("table_id") or "")
            if table_id and table_id in rendered_table_ids:
                continue
            table_entry = _table_for_unit(document, unit)
            if table_entry is not None:
                body_parts.append(_render_table(table_entry, unit))
                rendered_table_ids.add(table_entry.table_id)
                continue
        if (
            not has_explicit_heading
            and not promoted_title_heading
            and unit.unit_type == "paragraph"
            and _text_matches_title(unit, title)
        ):
            body_parts.append(_render_unit(unit, override_tag="h1"))
            promoted_title_heading = True
            continue
        body_parts.append(_render_unit(unit))

    if list_buffer:
        body_parts.append("<ul>")
        body_parts.extend(list_buffer)
        body_parts.append("</ul>")

    review_comment = ""
    if document.review_entries:
        review_comment = f"<!-- review_task_count: {len(document.review_entries)} -->\n"
    rendered_body = "\n".join(f"  {part}" for part in body_parts if part)

    return (
        "<!DOCTYPE html>\n"
        f'<html lang="{html.escape(lang, quote=True)}">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"  <title>{html.escape(title)}</title>\n"
        "</head>\n"
        "<body>\n"
        f"{review_comment}"
        f"{rendered_body}\n"
        "</body>\n"
        "</html>\n"
    )


def write_accessible_html(document: NormalizedAccessibilityDocument, path: Path, overwrite: bool) -> None:
    atomic_write_text(path, build_accessible_html(document), overwrite)


def _ordered_units(document: NormalizedAccessibilityDocument):
    return sorted(
        document.unit_entries,
        key=lambda unit: (unit.reading_order_index is None, unit.reading_order_index or 0, unit.unit_id),
    )


def _render_unit(unit, *, override_tag: str | None = None) -> str:
    heading_level = unit.structure.get("heading_level")
    tag = override_tag or html_tag_hint_for_unit(unit.unit_type, unit.projection_hints, heading_level=heading_level) or "div"
    if tag == "figure":
        return _render_figure(unit)
    text = unit.text or unit.content.get("text") or unit.content.get("text_sample") or ""
    return f"<{tag}>{html.escape(str(text))}</{tag}>"


def _render_list_item(unit) -> str:
    text = unit.text or unit.content.get("text") or ""
    return f"<li>{html.escape(str(text))}</li>"


def _render_figure(unit) -> str:
    alt_text = (
        unit.content.get("alt_text")
        or unit.content.get("description")
        or ("Description pending review." if unit.needs_review else "Figure")
    )
    figcaption = unit.text or unit.content.get("caption") or ""
    parts = [
        "<figure>",
        f'  <img alt="{html.escape(str(alt_text), quote=True)}">',
    ]
    if figcaption:
        parts.append(f"  <figcaption>{html.escape(str(figcaption))}</figcaption>")
    parts.append("</figure>")
    return "\n".join(parts)


def _table_for_unit(document: NormalizedAccessibilityDocument, unit):
    explicit_id = unit.structure.get("table_id") or unit.content.get("table_id")
    if explicit_id:
        for table_entry in document.table_entries:
            if table_entry.table_id == explicit_id:
                return table_entry
    unit_refs = set(unit.source_refs)
    for table_entry in document.table_entries:
        if unit_refs.intersection(table_entry.source_refs):
            return table_entry
    return document.table_entries[0] if document.table_entries and unit.unit_type == "table" else None


def _render_table(table_entry, unit) -> str:
    lines = ["<table>"]
    header_rows = set(table_entry.header_candidate_row_indexes)
    for row in table_entry.row_entries:
        lines.append("  <tr>")
        cell_tag = "th" if row.row_index in header_rows else "td"
        for cell in row.cell_entries:
            text = cell.text or ""
            lines.append(f"    <{cell_tag}>{html.escape(str(text))}</{cell_tag}>")
        lines.append("  </tr>")
    lines.append("</table>")
    return "\n".join(lines)


def _text_matches_title(unit, title: str) -> bool:
    text = (unit.text or unit.content.get("text") or "").strip()
    return bool(text) and text == title.strip()
