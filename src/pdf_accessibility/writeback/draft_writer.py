from __future__ import annotations

from pathlib import Path

import pikepdf
from pikepdf import Dictionary, Name

from pdf_accessibility.models.state import DocumentState, WritebackReport
from pdf_accessibility.writeback.marked_content import mark_simple_page_content
from pdf_accessibility.writeback.mcid import mcid_planned_count
from pdf_accessibility.writeback.parenttree import build_parent_tree
from pdf_accessibility.writeback.structure_tree import build_minimal_structure_tree, supported_structure_elements


def write_tagged_draft(document: DocumentState, draft_path: Path) -> WritebackReport:
    plan = document.structure_mapping_plan
    if plan is None:
        raise ValueError("Cannot write tagged draft without a structure mapping plan.")

    supported_elements = supported_structure_elements(plan.elements)
    unsupported_count = len(
        [
            element
            for element in plan.elements
            if element.include_in_structure_tree and element.pdf_structure_role not in {"H", "P"}
        ]
    )
    marking_details: list[dict[str, object]] = []
    draft_path.parent.mkdir(parents=True, exist_ok=True)
    with pikepdf.open(document.source_path) as pdf:
        root = pdf.Root
        title_written = _write_title(pdf, plan.document_properties.title)
        language_written = _write_language(root, plan.document_properties.primary_language)
        for page_number in sorted({element.page_number for element in supported_elements if element.page_number is not None}):
            page_elements = [element for element in supported_elements if element.page_number == page_number]
            page = pdf.pages[page_number - 1]
            detail = mark_simple_page_content(page, page_elements)
            detail["page_number"] = page_number
            marking_details.append(detail)
            if detail["written_mcid_count"]:
                page.obj["/StructParents"] = page_number - 1
        root[Name("/MarkInfo")] = Dictionary({"/Marked": True})
        struct_tree = build_minimal_structure_tree(supported_elements)
        written_entries = [
            entry
            for entry in plan.parent_tree_entries
            if any(
                detail.get("page_number") == entry.page_number and detail.get("written_mcid_count", 0) > 0
                for detail in marking_details
            )
        ]
        if written_entries:
            struct_tree[Name("/ParentTree")] = build_parent_tree(written_entries, supported_elements)
        root[Name("/StructTreeRoot")] = struct_tree
        pdf.save(draft_path)

    written_mcid_count = sum(int(detail.get("written_mcid_count", 0)) for detail in marking_details)
    skipped_mcid_count = sum(int(detail.get("skipped_mcid_count", 0)) for detail in marking_details)
    parent_tree_written_count = written_mcid_count
    content_streams_modified = written_mcid_count > 0
    limitations = [
        "Draft writer supports simple H/P marked-content wrapping only when page text streams align with planned elements.",
        "Table, figure, list, annotation, and link writeback are not implemented.",
        "Output is a tagged draft artifact, not a finalized accessible PDF.",
    ]
    if skipped_mcid_count:
        limitations.append(f"{skipped_mcid_count} planned MCIDs were skipped because the content stream was complex.")
    if unsupported_count:
        limitations.append(f"{unsupported_count} planned non-H/P structure elements were not written.")
    return WritebackReport(
        draft_path=draft_path,
        title_written=title_written,
        primary_language_written=language_written,
        mark_info_written=True,
        struct_tree_root_written=True,
        mcid_planned_count=mcid_planned_count(plan.elements),
        parent_tree_planned_count=len(plan.parent_tree_entries),
        mcid_written_count=written_mcid_count,
        parent_tree_written_count=parent_tree_written_count,
        skipped_mcid_count=skipped_mcid_count,
        content_streams_modified=content_streams_modified,
        content_stream_marking_details=marking_details,
        planned_element_count=len(plan.elements),
        written_structure_element_count=len(supported_elements),
        unsupported_element_count=unsupported_count,
        limitations=limitations,
        finalization_blocked=True,
    )


def _write_title(pdf: pikepdf.Pdf, title: str | None) -> bool:
    if not title:
        return False
    with pdf.open_metadata(set_pikepdf_as_editor=False) as metadata:
        metadata["dc:title"] = title
    pdf.docinfo[Name("/Title")] = title
    return True


def _write_language(root: pikepdf.Dictionary, language: str | None) -> bool:
    if not language:
        return False
    root[Name("/Lang")] = language
    return True
