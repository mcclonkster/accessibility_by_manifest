from __future__ import annotations

from pathlib import Path

import fitz
import pikepdf

from pdf_accessibility.models.state import DocumentMetadataEvidence, DocumentState, DocumentStatus, NormalizedUnit
from pdf_accessibility.nodes import structure_mapping_plan, validator_check, write_tagged_draft
from pdf_accessibility.reducers.apply_events import apply_events
from pdf_accessibility.services.internal_validator import validate_tagged_draft
from pdf_accessibility.writeback.draft_writer import write_tagged_draft as write_draft


def _write_pdf(path: Path) -> None:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Report Title")
    page.insert_text((72, 110), "A short paragraph.")
    document.save(path)
    document.close()


def _document(tmp_path: Path) -> DocumentState:
    source = tmp_path / "source.pdf"
    _write_pdf(source)
    return DocumentState(
        document_id="doc-1",
        source_path=source,
        run_dir=tmp_path,
        metadata=DocumentMetadataEvidence(title="Report Title", primary_language="en-US"),
        page_count=1,
        normalized_units=[
            NormalizedUnit(unit_id="heading-1", unit_type="heading", page_numbers=[1], reading_order_index=0),
            NormalizedUnit(unit_id="paragraph-1", unit_type="paragraph", page_numbers=[1], reading_order_index=1),
        ],
    )


def _draft(tmp_path: Path) -> tuple[Path, object]:
    document = _document(tmp_path)
    document = apply_events(document, structure_mapping_plan.run(document))
    draft_path = tmp_path / "tagged_draft.pdf"
    report = write_draft(document, draft_path)
    return draft_path, report


def test_internal_validator_passes_tiny_draft(tmp_path: Path) -> None:
    draft_path, report = _draft(tmp_path)

    findings = validate_tagged_draft(draft_path, report)

    assert findings == []


def test_internal_validator_fails_missing_language(tmp_path: Path) -> None:
    draft_path, report = _draft(tmp_path)
    with pikepdf.open(draft_path, allow_overwriting_input=True) as pdf:
        del pdf.Root["/Lang"]
        pdf.save(draft_path)

    findings = validate_tagged_draft(draft_path, report)

    assert {finding.finding_id.split("-")[1] for finding in findings}
    assert any("missing /Lang" in finding.message for finding in findings)


def test_internal_validator_fails_missing_struct_tree_root(tmp_path: Path) -> None:
    draft_path, report = _draft(tmp_path)
    with pikepdf.open(draft_path, allow_overwriting_input=True) as pdf:
        del pdf.Root["/StructTreeRoot"]
        pdf.save(draft_path)

    findings = validate_tagged_draft(draft_path, report)

    assert any("missing /StructTreeRoot" in finding.message for finding in findings)


def test_internal_validator_fails_report_content_mismatch(tmp_path: Path) -> None:
    draft_path, report = _draft(tmp_path)
    with pikepdf.open(draft_path, allow_overwriting_input=True) as pdf:
        for page in pdf.pages:
            contents = page.Contents
            streams = contents if isinstance(contents, pikepdf.Array) else [contents]
            for stream in streams:
                data = stream.read_bytes()
                data = data.replace(b"/H <</MCID 0>> BDC\n", b"")
                data = data.replace(b"/P <</MCID 1>> BDC\n", b"")
                data = data.replace(b"\nEMC", b"")
                stream.write(data)
        pdf.save(draft_path)

    findings = validate_tagged_draft(draft_path, report)

    assert any("no marked content was found" in finding.message for finding in findings)


def test_validator_check_node_records_no_findings_for_tiny_draft(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document = apply_events(document, structure_mapping_plan.run(document))
    document.document_status = DocumentStatus.DRAFT_READY
    document = apply_events(document, write_tagged_draft.run(document))

    updated = apply_events(document, validator_check.run(document))

    assert updated.output_artifacts.validator_findings_json is not None
    assert updated.validator_findings == []
    assert updated.output_artifacts.validator_findings_json.exists()
