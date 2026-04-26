from __future__ import annotations

from typing import Any


DEFAULT_HTML_TAGS = {
    "heading": "h1",
    "paragraph": "p",
    "list_item": "li",
    "figure": "figure",
    "table": "table",
    "table_cell": "td",
    "section": "section",
}

DEFAULT_DOCX_STYLES = {
    "heading": "Heading 1",
    "paragraph": "Normal",
    "list_item": "List Paragraph",
    "table": "Table Grid",
}

DEFAULT_PDF_STRUCTURE_ROLES = {
    "heading": "H1",
    "paragraph": "P",
    "list_item": "LI",
    "figure": "Figure",
    "table": "Table",
    "table_cell": "TD",
    "artifact": "Artifact",
}


def projection_status_allows_output(projection_hints: Any) -> bool:
    status = _hint_value(projection_hints, "projection_status")
    return status != "omitted"


def preferred_output_role(projection_hints: Any, target_format: str) -> str | None:
    preferred_roles = _hint_value(projection_hints, "preferred_output_roles") or {}
    if isinstance(preferred_roles, dict):
        role = preferred_roles.get(target_format)
        if isinstance(role, str) and role.strip():
            return role.strip()
    return None


def html_tag_hint_for_unit(unit_type: str, projection_hints: Any, *, heading_level: int | None = None) -> str | None:
    preferred = preferred_output_role(projection_hints, "html")
    if preferred:
        return preferred
    explicit = _hint_value(projection_hints, "html_tag_hint")
    if isinstance(explicit, str) and explicit.strip():
        return explicit.strip()
    if unit_type == "heading":
        level = min(max(int(heading_level or 1), 1), 6)
        return f"h{level}"
    return DEFAULT_HTML_TAGS.get(unit_type)


def docx_style_hint_for_unit(unit_type: str, projection_hints: Any, *, heading_level: int | None = None) -> str | None:
    preferred = preferred_output_role(projection_hints, "docx")
    if preferred:
        return preferred
    explicit = _hint_value(projection_hints, "docx_style_hint") or _hint_value(projection_hints, "docx_style") or _hint_value(projection_hints, "target_style")
    if isinstance(explicit, str) and explicit.strip():
        return explicit.strip()
    if unit_type == "heading":
        level = min(max(int(heading_level or 1), 1), 9)
        return f"Heading {level}"
    return DEFAULT_DOCX_STYLES.get(unit_type)


def pdf_structure_role_hint_for_unit(unit_type: str, projection_hints: Any, *, heading_level: int | None = None) -> str | None:
    preferred = preferred_output_role(projection_hints, "pdf")
    if preferred:
        return preferred
    explicit = _hint_value(projection_hints, "pdf_structure_role_hint")
    if isinstance(explicit, str) and explicit.strip():
        return explicit.strip()
    if unit_type == "heading":
        level = min(max(int(heading_level or 1), 1), 6)
        return f"H{level}"
    return DEFAULT_PDF_STRUCTURE_ROLES.get(unit_type)


def _hint_value(projection_hints: Any, name: str) -> Any:
    if projection_hints is None:
        return None
    if isinstance(projection_hints, dict):
        return projection_hints.get(name)
    return getattr(projection_hints, name, None)
