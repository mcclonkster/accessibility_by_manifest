from __future__ import annotations

from typing import Any


AAA_TEXT_COLOR_HEX = "000000"


def slide_image_alt_text(slide_number: int, title: str) -> tuple[str, str]:
    alt_title = f"Slide {slide_number} image: {title}"
    description = (
        f"Image of slide {slide_number}, titled '{title}'. "
        "The slide's extracted text and visual descriptions are provided as real Word content following this image."
    )
    return alt_title, description


def apply_picture_alt_text(inline_shape: Any, title: str, description: str) -> None:
    doc_pr = inline_shape._inline.docPr
    doc_pr.set("title", title)
    doc_pr.set("descr", description)


def enforce_wcag_aaa_text_colors(document: Any) -> None:
    from docx.oxml.ns import qn
    from docx.shared import RGBColor

    black = RGBColor(0, 0, 0)
    for style in document.styles:
        try:
            style.font.color.rgb = black
        except Exception:
            pass
        normalize_style_color_markup(style.element, qn)

    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            run.font.color.rgb = black


def normalize_style_color_markup(style_element: Any, qn: Any) -> None:
    theme_attrs = (
        "w:themeColor",
        "w:themeTint",
        "w:themeShade",
        "w:themeFill",
        "w:themeFillTint",
        "w:themeFillShade",
    )
    for element in style_element.iter():
        for attr_name in theme_attrs:
            element.attrib.pop(qn(attr_name), None)

        if element.tag == qn("w:color"):
            element.set(qn("w:val"), AAA_TEXT_COLOR_HEX)

        if qn("w:color") in element.attrib:
            element.set(qn("w:color"), AAA_TEXT_COLOR_HEX)

        if element.tag == qn("w:shd") or qn("w:fill") in element.attrib:
            element.set(qn("w:fill"), "FFFFFF")
