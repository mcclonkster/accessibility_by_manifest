import base64
from pathlib import Path
from zipfile import ZipFile

from accessibility_by_manifest.inputs.pptx.paths import OutputPaths
from accessibility_by_manifest.manifest.pptx import Manifest, ParagraphEntry, SlideEntry, TextBlockEntry
from accessibility_by_manifest.outputs.docx import write_slides_docx


ONE_PIXEL_PNG = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8"
    "/x8AAwMCAO+/p9sAAAAASUVORK5CYII="
)


def test_slides_docx_embeds_slide_image_alt_text_and_normalized_style_colors(tmp_path: Path) -> None:
    image_dir = tmp_path / "images"
    image_dir.mkdir()
    (image_dir / "slide_001.png").write_bytes(base64.b64decode(ONE_PIXEL_PNG))
    slides_docx = tmp_path / "slides.docx"
    paths = OutputPaths(
        companion_docx=tmp_path / "companion.docx",
        slides_docx=slides_docx,
        slides_markdown=tmp_path / "slides.md",
        manifest_json=tmp_path / "manifest.json",
        manifest_yaml=tmp_path / "manifest.yaml",
        extract_report=tmp_path / "extract.md",
        review_notes=tmp_path / "review.md",
        review_report=tmp_path / "review_report.md",
        slide_image_dir=image_dir,
    )
    manifest = Manifest(
        source_path=tmp_path / "deck.pptx",
        output_docx_path=slides_docx,
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

    write_slides_docx(manifest, paths, overwrite=False)

    with ZipFile(slides_docx) as docx_zip:
        names = docx_zip.namelist()
        document_xml = docx_zip.read("word/document.xml").decode("utf-8")
        styles_xml = docx_zip.read("word/styles.xml").decode("utf-8")

    assert len([name for name in names if name.startswith("word/media/")]) == 1
    assert 'title="Slide 1 image: Accessible Slide"' in document_xml
    assert 'descr="Image of slide 1, titled \'Accessible Slide\'.' in document_xml
    assert '<w:jc w:val="center"/>' in document_xml
    assert 'cy="3429000"' in document_xml
    assert "w:themeColor=" not in styles_xml
    assert "w:themeTint=" not in styles_xml
    assert "w:themeShade=" not in styles_xml
    assert "w:themeFill=" not in styles_xml
    assert "w:themeFillTint=" not in styles_xml
    assert "w:themeFillShade=" not in styles_xml
