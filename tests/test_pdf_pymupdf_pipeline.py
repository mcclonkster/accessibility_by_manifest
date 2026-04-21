from pathlib import Path

from jsonschema import Draft202012Validator

from pdf_to_docx_accessibility.config import PdfWorkflowConfig
from pdf_to_docx_accessibility.manifest.validate import load_schema
from pdf_to_docx_accessibility.paths import PdfRun
from pdf_to_docx_accessibility.pipeline import run_pdf


def make_pdf(path: Path) -> None:
    import fitz

    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Accessible PDF heading")
    page.insert_text((72, 100), "This is body text extracted by PyMuPDF.")
    page.insert_link({"kind": fitz.LINK_URI, "from": fitz.Rect(72, 120, 180, 140), "uri": "https://example.com"})
    document.set_metadata({"title": "Accessible PDF", "author": "Test Author"})
    document.save(path)
    document.close()


def test_pymupdf_first_pass_writes_schema_valid_manifest(tmp_path: Path) -> None:
    pdf_path = tmp_path / "accessible.pdf"
    output_dir = tmp_path / "out"
    make_pdf(pdf_path)
    config = PdfWorkflowConfig(input_path=pdf_path, output_root=output_dir, overwrite=True)
    result = run_pdf(config, PdfRun(pdf_path=pdf_path, output_dir=output_dir))

    assert result.ok, result.message
    assert result.output_paths.manifest_json.exists()
    manifest = result.manifest
    assert manifest is not None
    Draft202012Validator(load_schema()).validate(manifest)
    assert manifest["source_package"]["format_family"] == "PDF"
    assert manifest["document_summary"]["total_pages"] == 1
    assert manifest["document_summary"]["raw_block_count"] >= 1
    assert manifest["document_summary"]["annotation_count"] >= 1
    assert manifest["document_metadata"]["title"] == "Accessible PDF"
    assert manifest["page_entries"][0]["observed_source"]["text_layer_detected"] is True
    assert manifest["raw_block_entries"][0]["source_evidence_type"] == "untagged_text"


def test_pymupdf_first_pass_dry_run_writes_no_manifest(tmp_path: Path) -> None:
    pdf_path = tmp_path / "accessible.pdf"
    output_dir = tmp_path / "out"
    make_pdf(pdf_path)
    config = PdfWorkflowConfig(input_path=pdf_path, output_root=output_dir, dry_run=True)
    result = run_pdf(config, PdfRun(pdf_path=pdf_path, output_dir=output_dir))

    assert result.ok, result.message
    assert not result.output_paths.manifest_json.exists()
    assert result.manifest is not None
