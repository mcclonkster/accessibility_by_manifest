from __future__ import annotations

from pikepdf import Array, Dictionary, Name

from pdf_accessibility.models.state import ParentTreeEntryPlan, StructureElementPlan


def plan_parent_tree_entries(elements: list[StructureElementPlan]) -> list[ParentTreeEntryPlan]:
    entries: list[ParentTreeEntryPlan] = []
    for element in elements:
        if element.mcid is None or element.parent_tree_index is None or element.page_number is None:
            continue
        entries.append(
            ParentTreeEntryPlan(
                parent_tree_index=element.parent_tree_index,
                element_id=element.element_id,
                unit_id=element.unit_id,
                page_number=element.page_number,
                mcid=element.mcid,
            )
        )
    return entries


def build_parent_tree(entries: list[ParentTreeEntryPlan], elements: list[StructureElementPlan]) -> Dictionary:
    elements_by_id = {element.element_id: element for element in elements}
    nums = Array()
    for index in sorted({entry.parent_tree_index for entry in entries}):
        page_entries = [entry for entry in entries if entry.parent_tree_index == index]
        kids = Array()
        for entry in sorted(page_entries, key=lambda item: item.mcid):
            element = elements_by_id.get(entry.element_id)
            if element is None:
                continue
            kids.append(
                Dictionary(
                    {
                        "/Type": Name("/StructElem"),
                        "/S": Name(f"/{element.pdf_structure_role}"),
                        "/ID": element.element_id,
                    }
                )
            )
        nums.append(index)
        nums.append(kids)
    return Dictionary({"/Nums": nums})
