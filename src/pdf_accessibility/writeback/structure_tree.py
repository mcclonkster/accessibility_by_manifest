from __future__ import annotations

from pikepdf import Array, Dictionary, Name

from pdf_accessibility.models.state import StructureElementPlan


SUPPORTED_DRAFT_ROLES = {"H", "P"}


def supported_structure_elements(elements: list[StructureElementPlan]) -> list[StructureElementPlan]:
    return [
        element
        for element in elements
        if element.include_in_structure_tree and element.pdf_structure_role in SUPPORTED_DRAFT_ROLES
    ]


def build_minimal_structure_tree(elements: list[StructureElementPlan]) -> Dictionary:
    kids = Array()
    for element in elements:
        kids.append(
            Dictionary(
                {
                    "/Type": Name("/StructElem"),
                    "/S": Name(f"/{element.pdf_structure_role}"),
                    "/ID": f"{element.element_id}",
                }
            )
        )
    document_root = Dictionary(
        {
            "/Type": Name("/StructElem"),
            "/S": Name("/Document"),
            "/K": kids,
        }
    )
    return Dictionary(
        {
            "/Type": Name("/StructTreeRoot"),
            "/K": Array([document_root]),
        }
    )
