from __future__ import annotations

from collections import Counter
from pathlib import Path

import pikepdf
from pikepdf import Dictionary, Name

from pdf_accessibility.models.state import DocumentState, WritebackReport
from pdf_accessibility.writeback.marked_content import mark_simple_page_content
from pdf_accessibility.writeback.mcid import mcid_planned_count
from pdf_accessibility.writeback.parenttree import build_parent_tree
from pdf_accessibility.writeback.structure_tree import (
    SUPPORTED_DRAFT_ROLES,
    build_minimal_structure_tree,
    supported_structure_elements,
)


def write_tagged_draft(document: DocumentState, draft_path: Path) -> WritebackReport:
    plan = document.structure_mapping_plan
    if plan is None:
        raise ValueError("Cannot write tagged draft without a structure mapping plan.")

    supported_elements = supported_structure_elements(plan.elements)
    unsupported_elements = [
        element
        for element in plan.elements
        if element.include_in_structure_tree and element.pdf_structure_role not in SUPPORTED_DRAFT_ROLES
    ]
    unsupported_count = len(unsupported_elements)
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

    supported_count = len(supported_elements)
    planned_role_counts = _role_counts(plan.elements)
    supported_role_counts = _role_counts(supported_elements)
    written_role_counts, skipped_role_counts = _written_and_skipped_role_counts(supported_elements, marking_details)
    written_mcid_count = sum(int(detail.get("written_mcid_count", 0)) for detail in marking_details)
    skipped_mcid_count = sum(int(detail.get("skipped_mcid_count", 0)) for detail in marking_details)
    parent_tree_written_count = written_mcid_count
    content_streams_modified = written_mcid_count > 0
    skipped_supported_count = sum(skipped_role_counts.values())
    unsupported_role_counts = _role_counts(unsupported_elements)
    blocking_details = _build_blocking_details(
        unsupported_count=unsupported_count,
        unsupported_role_counts=unsupported_role_counts,
        skipped_mcid_count=skipped_mcid_count,
        skipped_role_counts=skipped_role_counts,
        title_written=title_written,
        language_written=language_written,
        supported_count=supported_count,
        planned_element_count=len(plan.elements),
        marking_details=marking_details,
    )
    blocking_categories = list(blocking_details.keys())
    finalization_blocked = bool(blocking_categories)
    limitations = [
        "Draft writer supports simple H/P/LI marked-content wrapping only when page text streams align with planned elements.",
        "Table, figure, explicit list-container, annotation, and link writeback are not implemented.",
    ]
    if finalization_blocked:
        limitations.append("Output remains a tagged draft artifact and cannot be treated as a finalized accessible PDF yet.")
    if skipped_mcid_count:
        limitations.append(f"{skipped_mcid_count} planned MCIDs were skipped because the content stream was complex.")
    if unsupported_count:
        limitations.append(
            f"{unsupported_count} planned unsupported structure elements were not written: "
            + ", ".join(f"{role}={count}" for role, count in sorted(unsupported_role_counts.items()))
            + "."
        )
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
        supported_element_count=supported_count,
        written_structure_element_count=len(supported_elements),
        skipped_supported_element_count=skipped_supported_count,
        unsupported_element_count=unsupported_count,
        planned_role_counts=dict(planned_role_counts),
        supported_role_counts=dict(supported_role_counts),
        written_role_counts=dict(written_role_counts),
        skipped_role_counts=dict(skipped_role_counts),
        unsupported_role_counts=dict(unsupported_role_counts),
        blocking_categories=blocking_categories,
        blocking_details=blocking_details,
        limitations=limitations,
        finalization_blocked=finalization_blocked,
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


def _role_counts(elements) -> Counter[str]:
    return Counter(element.pdf_structure_role or "unknown" for element in elements)


def _written_and_skipped_role_counts(elements, marking_details: list[dict[str, object]]) -> tuple[Counter[str], Counter[str]]:
    written = Counter()
    skipped = Counter()
    details_by_page = {int(detail.get("page_number") or 0): detail for detail in marking_details if detail.get("page_number")}
    for element in elements:
        role = element.pdf_structure_role or "unknown"
        detail = details_by_page.get(int(element.page_number or 0))
        if detail is not None and int(detail.get("written_mcid_count", 0)) > 0:
            written[role] += 1
        else:
            skipped[role] += 1
    return written, skipped


def _build_blocking_details(
    *,
    unsupported_count: int,
    unsupported_role_counts: Counter[str],
    skipped_mcid_count: int,
    skipped_role_counts: Counter[str],
    title_written: bool,
    language_written: bool,
    supported_count: int,
    planned_element_count: int,
    marking_details: list[dict[str, object]],
) -> dict[str, object]:
    details: dict[str, object] = {}
    if unsupported_count > 0:
        details["unsupported_structure_roles"] = {
            "unsupported_element_count": unsupported_count,
            "unsupported_role_counts": dict(unsupported_role_counts),
        }
    if skipped_mcid_count > 0:
        details["skipped_content_stream_marking"] = {
            "skipped_mcid_count": skipped_mcid_count,
            "skipped_role_counts": dict(skipped_role_counts),
            "page_statuses": [
                {
                    "page_number": detail.get("page_number"),
                    "status": detail.get("status"),
                    "skipped_mcid_count": detail.get("skipped_mcid_count", 0),
                }
                for detail in marking_details
                if int(detail.get("skipped_mcid_count", 0)) > 0
            ],
        }
    if not title_written:
        details["missing_document_title"] = {"target": "document_metadata.title"}
    if not language_written:
        details["missing_primary_language"] = {"target": "document_metadata.primary_language"}
    if supported_count == 0:
        details["no_supported_elements"] = {
            "planned_element_count": planned_element_count,
            "supported_element_count": supported_count,
        }
    return details
