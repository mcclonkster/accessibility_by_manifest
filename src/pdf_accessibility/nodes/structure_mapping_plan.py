from __future__ import annotations

from pdf_accessibility.models.events import NodeEvent, region_status_event, structure_mapping_plan_event
from pdf_accessibility.models.state import (
    DocumentPropertyPlan,
    DocumentState,
    NormalizedUnit,
    RegionStatus,
    StructureElementPlan,
    StructureMappingPlan,
)
from pdf_accessibility.utils.ids import event_id, stable_id
from pdf_accessibility.writeback.mcid import assign_mcid_plan
from pdf_accessibility.writeback.parenttree import plan_parent_tree_entries

NODE_NAME = "structure_mapping_plan"


def run(document: DocumentState) -> list[NodeEvent]:
    events = [
        region_status_event(event_id(NODE_NAME, region.region_id), NODE_NAME, region.region_id, RegionStatus.MAPPING_PLANNED)
        for page in document.pages
        for region in page.regions
    ]
    events.append(
        structure_mapping_plan_event(
            event_id(NODE_NAME, "plan", document.document_id),
            NODE_NAME,
            _build_structure_mapping_plan(document),
        )
    )
    return events


def _build_structure_mapping_plan(document: DocumentState) -> StructureMappingPlan:
    elements = assign_mcid_plan([_element_for_unit(unit) for unit in document.normalized_units])
    parent_tree_entries = plan_parent_tree_entries(elements)
    artifact_unit_ids = [element.unit_id for element in elements if element.artifact]
    reading_order_unit_ids = [
        element.unit_id
        for element in sorted(elements, key=lambda item: (item.reading_order_index is None, item.reading_order_index or 0))
        if element.include_in_structure_tree and element.reading_order_index is not None
    ]
    unresolved_unit_ids = [element.unit_id for element in elements if element.unresolved_mapping]
    document_properties = _document_property_plan(document)
    return StructureMappingPlan(
        document_properties=document_properties,
        elements=elements,
        parent_tree_entries=parent_tree_entries,
        artifact_unit_ids=artifact_unit_ids,
        reading_order_unit_ids=reading_order_unit_ids,
        unresolved_unit_ids=unresolved_unit_ids,
        structure_tree_ready=False,
        writeback_prerequisites_ready=False,
    )


def _document_property_plan(document: DocumentState) -> DocumentPropertyPlan:
    metadata = document.metadata
    title = metadata.title if metadata else None
    language = metadata.primary_language if metadata else None
    basis = []
    if title:
        basis.append("title from PDF metadata")
    if language:
        basis.append("primary language from PDF catalog or metadata")
    return DocumentPropertyPlan(
        title=title,
        primary_language=language,
        title_ready=bool(title),
        primary_language_ready=bool(language),
        evidence_basis=basis,
    )


def _element_for_unit(unit: NormalizedUnit) -> StructureElementPlan:
    role = _pdf_role(unit.unit_type)
    artifact = unit.unit_type == "artifact"
    unresolved = unit.unit_type in {"unknown", "table", "figure", "list"} or role is None
    notes: list[str] = []
    if artifact:
        notes.append("Excluded from logical structure tree; candidate artifact.")
    if unit.unit_type == "table":
        notes.append("Table child structure is unresolved pending header/cell review.")
    elif unit.unit_type == "list":
        notes.append("Explicit list-container writeback is not implemented in the v0.1 draft writer.")
    elif unit.unit_type == "list_item":
        notes.append("Flat list item writeback is supported in the v0.1 draft writer.")
    elif unit.unit_type == "figure":
        notes.append("Figure mapping requires trusted alt text or decorative decision.")
    elif unit.unit_type == "unknown":
        notes.append("Unknown unit type cannot be mapped safely.")
    return StructureElementPlan(
        element_id=f"element-{stable_id(unit.unit_id)}",
        unit_id=unit.unit_id,
        pdf_structure_role=role,
        include_in_structure_tree=not artifact and role is not None,
        artifact=artifact,
        page_number=unit.page_numbers[0] if unit.page_numbers else None,
        reading_order_index=unit.reading_order_index if not artifact else None,
        source_refs=unit.source_refs,
        page_numbers=unit.page_numbers,
        review_required=unit.needs_review or unresolved,
        unresolved_mapping=unresolved,
        notes=notes,
    )


def _pdf_role(unit_type: str) -> str | None:
    return {
        "heading": "H",
        "paragraph": "P",
        "list": "L",
        "list_item": "LI",
        "table": "Table",
        "figure": "Figure",
        "artifact": "Artifact",
    }.get(unit_type)
