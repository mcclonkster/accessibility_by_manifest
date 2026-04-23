from __future__ import annotations

from pdf_accessibility.models.state import StructureElementPlan


MCID_DRAFT_ROLES = {"H", "P"}


def can_plan_mcid(element: StructureElementPlan) -> bool:
    return (
        element.include_in_structure_tree
        and not element.artifact
        and element.pdf_structure_role in MCID_DRAFT_ROLES
        and element.page_number is not None
    )


def assign_mcid_plan(elements: list[StructureElementPlan]) -> list[StructureElementPlan]:
    counters_by_page: dict[int, int] = {}
    planned: list[StructureElementPlan] = []
    for element in elements:
        if not can_plan_mcid(element):
            planned.append(element)
            continue
        page_number = int(element.page_number)
        mcid = counters_by_page.get(page_number, 0)
        counters_by_page[page_number] = mcid + 1
        planned.append(
            element.model_copy(
                update={
                    "mcid": mcid,
                    "marked_content_ref": f"page:{page_number}:mcid:{mcid}",
                    "parent_tree_index": page_number - 1,
                    "content_stream_update_status": "planned_not_written",
                }
            )
        )
    return planned


def mcid_planned_count(elements: list[StructureElementPlan]) -> int:
    return sum(1 for element in elements if element.mcid is not None)

