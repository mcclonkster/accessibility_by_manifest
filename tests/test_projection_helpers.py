from accessibility_by_manifest.outputs.projection import (
    docx_style_hint_for_unit,
    html_tag_hint_for_unit,
    pdf_structure_role_hint_for_unit,
    preferred_output_role,
    projection_status_allows_output,
)


def test_projection_helpers_prefer_explicit_roles_and_status() -> None:
    projection_hints = {
        "projection_status": "manual_review_required",
        "preferred_output_roles": {"html": "aside", "pdf": "Note"},
        "docx_style_hint": "Intense Quote",
    }

    assert projection_status_allows_output(projection_hints) is True
    assert preferred_output_role(projection_hints, "html") == "aside"
    assert html_tag_hint_for_unit("paragraph", projection_hints) == "aside"
    assert pdf_structure_role_hint_for_unit("paragraph", projection_hints) == "Note"
    assert docx_style_hint_for_unit("paragraph", projection_hints) == "Intense Quote"


def test_projection_helpers_fall_back_to_shared_defaults() -> None:
    assert html_tag_hint_for_unit("heading", None, heading_level=2) == "h2"
    assert html_tag_hint_for_unit("table", None) == "table"
    assert pdf_structure_role_hint_for_unit("heading", None, heading_level=3) == "H3"
    assert pdf_structure_role_hint_for_unit("artifact", None) == "Artifact"
    assert docx_style_hint_for_unit("heading", None, heading_level=2) == "Heading 2"
    assert docx_style_hint_for_unit("table", None) == "Table Grid"


def test_projection_helpers_respect_omitted_status() -> None:
    assert projection_status_allows_output({"projection_status": "omitted"}) is False
