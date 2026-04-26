from __future__ import annotations

from pathlib import Path

import fitz
import pikepdf

from pdf_accessibility.models.state import DocumentStatus
from pdf_accessibility.persistence.runs import create_run, initial_document_state
from pdf_accessibility.reducers.apply_events import apply_events
from pdf_accessibility.services.manifest_bridge import BRIDGE_MARKER, document_uses_shared_pdf_bridge, load_shared_pdf_events


def _write_ready_one_page_pdf(path: Path) -> None:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Annual Report")
    page.insert_text((72, 110), "A short accessible paragraph.")
    document.set_metadata({"title": "Annual Report"})
    document.save(path)
    document.close()
    with pikepdf.open(path, allow_overwriting_input=True) as pdf:
        pdf.Root["/Lang"] = pikepdf.String("en-US")
        pdf.save(path)


def test_manifest_bridge_hydrates_document_from_shared_pdf_model(tmp_path: Path) -> None:
    source_pdf = tmp_path / "input.pdf"
    _write_ready_one_page_pdf(source_pdf)
    context = create_run(source_pdf, tmp_path / "runs")
    document = initial_document_state(context)

    updated = apply_events(document, load_shared_pdf_events(document))

    assert updated.page_count == 1
    assert updated.metadata is not None
    assert updated.metadata.title == "Annual Report"
    assert updated.metadata.primary_language == "en-US"
    assert updated.metadata.provenance["bridge_marker"] == BRIDGE_MARKER
    assert updated.pages[0].text_blocks
    assert updated.pages[0].regions
    assert updated.normalized_units
    assert any(unit.unit_type in {"heading", "paragraph"} for unit in updated.normalized_units)
    assert document_uses_shared_pdf_bridge(updated)


def test_manifest_bridge_review_entries_become_workflow_review_tasks(tmp_path: Path) -> None:
    source_pdf = tmp_path / "input.pdf"
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Untitled")
    document.save(source_pdf)
    document.close()

    context = create_run(source_pdf, tmp_path / "runs")
    initial = initial_document_state(context)
    updated = apply_events(initial, load_shared_pdf_events(initial))

    issue_codes = {task.issue_code for task in updated.review_tasks}
    assert "DOCUMENT_TITLE_MISSING" in issue_codes
    assert "DOCUMENT_LANGUAGE_MISSING" in issue_codes
    assert updated.document_status is DocumentStatus.PENDING
