from __future__ import annotations

from pikepdf import Array, Dictionary, Name

from pdf_accessibility.models.state import StructureElementPlan


SUPPORTED_DRAFT_ROLES = {"H", "P", "LI"}


def supported_structure_elements(elements: list[StructureElementPlan]) -> list[StructureElementPlan]:
    return [
        element
        for element in elements
        if element.include_in_structure_tree and element.pdf_structure_role in SUPPORTED_DRAFT_ROLES
    ]


def build_minimal_structure_tree(elements: list[StructureElementPlan]) -> Dictionary:
    kids = Array()
    index = 0
    while index < len(elements):
        element = elements[index]
        if element.pdf_structure_role == "LI":
            list_items = []
            while index < len(elements) and elements[index].pdf_structure_role == "LI":
                list_items.append(elements[index])
                index += 1
            kids.append(_list_struct_elem(list_items))
            continue
        kids.append(_struct_elem(element))
        index += 1
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


def _struct_elem(element: StructureElementPlan) -> Dictionary:
    return Dictionary(
        {
            "/Type": Name("/StructElem"),
            "/S": Name(f"/{element.pdf_structure_role}"),
            "/ID": f"{element.element_id}",
        }
    )


def _list_struct_elem(items: list[StructureElementPlan]) -> Dictionary:
    return Dictionary(
        {
            "/Type": Name("/StructElem"),
            "/S": Name("/L"),
            "/K": Array([_struct_elem(item) for item in items]),
        }
    )
