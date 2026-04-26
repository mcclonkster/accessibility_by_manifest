from __future__ import annotations

from pathlib import Path

import fitz
import pikepdf

from pdf_accessibility.models.state import (
    DocumentMetadataEvidence,
    DocumentState,
    DocumentStatus,
    NormalizedUnit,
    PageState,
    RegionState,
    RegionStatus,
)
from pdf_accessibility.nodes import structure_mapping_plan, write_tagged_draft
from pdf_accessibility.reducers.apply_events import apply_events
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
            NormalizedUnit(
                unit_id="heading-1",
                unit_type="heading",
                page_numbers=[1],
                text="Report Title",
                reading_order_index=0,
            ),
            NormalizedUnit(
                unit_id="paragraph-1",
                unit_type="paragraph",
                page_numbers=[1],
                text="A short paragraph.",
                reading_order_index=1,
            ),
        ],
    )


def test_draft_writer_writes_title_language_and_structure_tree(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document = apply_events(document, structure_mapping_plan.run(document))
    draft_path = tmp_path / "tagged_draft.pdf"

    report = write_draft(document, draft_path)

    assert draft_path.exists()
    assert report.title_written
    assert report.primary_language_written
    assert report.mark_info_written
    assert report.struct_tree_root_written
    assert report.mcid_planned_count == 2
    assert report.parent_tree_planned_count == 2
    assert report.mcid_written_count == 2
    assert report.parent_tree_written_count == 2
    assert report.skipped_mcid_count == 0
    assert report.content_streams_modified
    assert report.supported_element_count == 2
    assert report.written_structure_element_count == 2
    assert report.skipped_supported_element_count == 0
    assert report.planned_role_counts == {"H": 1, "P": 1}
    assert report.supported_role_counts == {"H": 1, "P": 1}
    assert report.written_role_counts == {"H": 1, "P": 1}
    assert report.skipped_role_counts == {}
    assert report.unsupported_role_counts == {}
    assert report.blocking_categories == []
    assert report.blocking_details == {}
    assert report.finalization_blocked is False
    with pikepdf.open(draft_path) as pdf:
        assert str(pdf.Root.get("/Lang")) == "en-US"
        assert pdf.Root.get("/MarkInfo") is not None
        struct_tree = pdf.Root.get("/StructTreeRoot")
        assert struct_tree is not None
        assert struct_tree.get("/ParentTree") is not None
        assert str(pdf.docinfo.get("/Title")) == "Report Title"
        content = _page_content_bytes(pdf)
        assert b"/H <</MCID 0>> BDC" in content
        assert b"/P <</MCID 1>> BDC" in content


def test_write_tagged_draft_node_registers_draft_report_and_blocker(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.pages = [
        PageState(
            page_number=1,
            regions=[RegionState(region_id="region-1", page_number=1, status=RegionStatus.COMMITTABLE)],
        )
    ]
    document = apply_events(document, structure_mapping_plan.run(document))
    document.document_status = DocumentStatus.DRAFT_READY

    updated = apply_events(document, write_tagged_draft.run(document))

    assert updated.output_artifacts.tagged_draft_pdf is not None
    assert updated.output_artifacts.writeback_report_json is not None
    assert updated.writeback_report is not None
    assert updated.writeback_report.mcid_planned_count == 2
    assert updated.writeback_report.parent_tree_planned_count == 2
    assert updated.writeback_report.mcid_written_count == 2
    assert updated.writeback_report.parent_tree_written_count == 2
    assert updated.writeback_report.content_streams_modified
    assert updated.writeback_report.supported_element_count == 2
    assert updated.writeback_report.skipped_supported_element_count == 0
    assert updated.writeback_report.finalization_blocked is False
    assert not any(task.issue_code == "TAGGED_DRAFT_NOT_FINAL" for task in updated.review_tasks)
    assert not updated.blocker_ids


def test_draft_writer_reports_supported_vs_unsupported_structure_explicitly(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.normalized_units.append(
        NormalizedUnit(
            unit_id="list-1",
            unit_type="list",
            page_numbers=[1],
            text="1. First item\n2. Second item",
            reading_order_index=2,
        )
    )
    document = apply_events(document, structure_mapping_plan.run(document))
    list_element = next(element for element in document.structure_mapping_plan.elements if element.unit_id == "list-1")
    assert list_element.unresolved_mapping is True
    assert any("Explicit list-container writeback is not implemented" in note for note in list_element.notes)
    draft_path = tmp_path / "tagged_draft.pdf"

    report = write_draft(document, draft_path)

    assert draft_path.exists()
    assert report.planned_element_count == 3
    assert report.supported_element_count == 2
    assert report.written_structure_element_count == 2
    assert report.skipped_supported_element_count == 0
    assert report.unsupported_element_count == 1
    assert report.planned_role_counts == {"H": 1, "P": 1, "L": 1}
    assert report.supported_role_counts == {"H": 1, "P": 1}
    assert report.written_role_counts == {"H": 1, "P": 1}
    assert report.unsupported_role_counts == {"L": 1}
    assert report.blocking_categories == ["unsupported_structure_roles"]
    assert report.blocking_details["unsupported_structure_roles"]["unsupported_role_counts"] == {"L": 1}
    assert report.finalization_blocked is True
    assert any("L=1" in limitation for limitation in report.limitations)


def test_draft_writer_supports_simple_flat_list_items(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.normalized_units = [
        NormalizedUnit(
            unit_id="list-item-1",
            unit_type="list_item",
            page_numbers=[1],
            text="1. First item",
            reading_order_index=0,
        ),
        NormalizedUnit(
            unit_id="list-item-2",
            unit_type="list_item",
            page_numbers=[1],
            text="2. Second item",
            reading_order_index=1,
        ),
    ]
    document = apply_events(document, structure_mapping_plan.run(document))
    list_elements = [element for element in document.structure_mapping_plan.elements if element.pdf_structure_role == "LI"]

    assert len(list_elements) == 2
    assert all(not element.unresolved_mapping for element in list_elements)
    assert all(any("Flat list item writeback is supported" in note for note in element.notes) for element in list_elements)

    draft_path = tmp_path / "tagged_draft.pdf"
    report = write_draft(document, draft_path)

    assert draft_path.exists()
    assert report.finalization_blocked is False
    assert report.supported_element_count == 2
    assert report.written_structure_element_count == 2
    assert report.unsupported_element_count == 0
    assert report.planned_role_counts == {"LI": 2}
    assert report.supported_role_counts == {"LI": 2}
    assert report.written_role_counts == {"LI": 2}
    assert report.blocking_categories == []
    with pikepdf.open(draft_path) as pdf:
        content = _page_content_bytes(pdf)
        assert b"/LI <</MCID 0>> BDC" in content
        assert b"/LI <</MCID 1>> BDC" in content
        struct_tree = pdf.Root.get("/StructTreeRoot")
        assert struct_tree is not None
        document_root = struct_tree.get("/K")[0]
        first_kid = document_root.get("/K")[0]
        assert str(first_kid.get("/S")) == "/L"


def test_draft_writer_reports_missing_document_properties_explicitly(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.metadata = DocumentMetadataEvidence()
    document = apply_events(document, structure_mapping_plan.run(document))

    report = write_draft(document, tmp_path / "tagged_draft.pdf")

    assert report.finalization_blocked is True
    assert report.blocking_categories == ["missing_document_title", "missing_primary_language"]
    assert report.blocking_details["missing_document_title"]["target"] == "document_metadata.title"
    assert report.blocking_details["missing_primary_language"]["target"] == "document_metadata.primary_language"


def test_write_tagged_draft_node_records_explicit_blocking_categories(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.normalized_units.append(
        NormalizedUnit(
            unit_id="list-1",
            unit_type="list",
            page_numbers=[1],
            text="1. First item\n2. Second item",
            reading_order_index=2,
        )
    )
    document.pages = [
        PageState(
            page_number=1,
            regions=[RegionState(region_id="region-1", page_number=1, status=RegionStatus.COMMITTABLE)],
        )
    ]
    document = apply_events(document, structure_mapping_plan.run(document))
    document.document_status = DocumentStatus.DRAFT_READY

    updated = apply_events(document, write_tagged_draft.run(document))

    draft_blocker = next(task for task in updated.review_tasks if task.issue_code == "TAGGED_DRAFT_NOT_FINAL")
    assert "unsupported structure roles remain (L=1)" in draft_blocker.reason
    assert draft_blocker.confidence_context["blocking_categories"] == ["unsupported_structure_roles"]
    assert draft_blocker.confidence_context["blocking_details"]["unsupported_structure_roles"][
        "unsupported_role_counts"
    ] == {"L": 1}


def _page_content_bytes(pdf: pikepdf.Pdf) -> bytes:
    contents = pdf.pages[0].Contents
    if isinstance(contents, pikepdf.Array):
        return b"\n".join(stream.read_bytes() for stream in contents)
    return contents.read_bytes()
