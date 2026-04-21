from pathlib import Path

from pptx_to_docx_accessibility.markdown_writer import build_slides_markdown
from pptx_to_docx_accessibility.models import Manifest, ParagraphEntry, SlideEntry, TextBlockEntry


def test_slides_markdown_uses_markdown_image_convention_with_relative_path(tmp_path: Path) -> None:
    image_dir = tmp_path / "deck_slide_images"
    image_dir.mkdir()
    (image_dir / "slide_001.png").write_bytes(b"not inspected")
    markdown_path = tmp_path / "deck_slides.md"
    manifest = Manifest(
        source_path=tmp_path / "deck.pptx",
        output_docx_path=tmp_path / "deck_slides.docx",
        preview_image_dir=image_dir,
        slides=(
            SlideEntry(
                slide_number=1,
                title="Accessible Slide",
                title_source="TITLE_PLACEHOLDER",
                preview_image="slide_001.png",
                text_blocks=(
                    TextBlockEntry(
                        source_name="Title 1",
                        source_text_container_type="placeholder_text",
                        placeholder_type="title",
                        interpreted_text_role="title_candidate",
                        role_confidence="high",
                        auto_merge_allowed=False,
                        order=1,
                        paragraphs=(ParagraphEntry(text="Accessible Slide"),),
                    ),
                ),
                visuals=(),
            ),
        ),
    )

    markdown = build_slides_markdown(manifest, markdown_path)

    assert "## Slide 1. Accessible Slide" in markdown
    assert '![Slide 1 image: Accessible Slide](<deck_slide_images/slide_001.png> "Image of slide 1, titled \'Accessible Slide\'.' in markdown
    assert "### Slide text" in markdown
