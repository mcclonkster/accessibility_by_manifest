from __future__ import annotations

from pdf_accessibility.models.events import NodeEvent, finding_event, region_status_event, review_task_event
from pdf_accessibility.models.state import Confidence, DocumentState, Finding, FindingClass, RegionStatus, ReviewTask
from pdf_accessibility.utils.ids import event_id, stable_id

NODE_NAME = "behavior_check"


def run(document: DocumentState) -> list[NodeEvent]:
    events: list[NodeEvent] = [
        region_status_event(event_id(NODE_NAME, region.region_id), NODE_NAME, region.region_id, RegionStatus.BEHAVIOR_CHECKED)
        for page in document.pages
        for region in page.regions
    ]
    events.extend(_behavior_findings(document))
    return events


def _behavior_findings(document: DocumentState) -> list[NodeEvent]:
    plan = document.structure_mapping_plan
    if plan is None:
        return [
            review_task_event(
                event_id(NODE_NAME, "missing-plan", document.document_id),
                NODE_NAME,
                ReviewTask(
                    task_id=f"review-{stable_id(NODE_NAME, 'missing-plan', document.document_id)}",
                    issue_code="STRUCTURE_MAPPING_PLAN_MISSING",
                    severity="error",
                    target_ref="document",
                    reason="Structure mapping plan was not created.",
                    blocking=True,
                    suggested_action="Run structure_mapping_plan before behavior_check.",
                ),
            )
        ]
    issues = _plan_issues(document)
    return [
        finding_event(
            event_id(NODE_NAME, "plan-check", document.document_id),
            NODE_NAME,
            Finding(
                finding_id=f"finding-{stable_id(NODE_NAME, 'plan-check', document.document_id)}",
                node_name=NODE_NAME,
                finding_class=FindingClass.PROPOSED_DECISION if not issues else FindingClass.BLOCKING_ISSUE,
                target_ref="document",
                message=(
                    "Structure mapping behavior check passed."
                    if not issues
                    else "Structure mapping behavior check found writeback prerequisite gaps."
                ),
                confidence=Confidence.HIGH,
                payload={
                    "issue_count": len(issues),
                    "issues": issues,
                    "element_count": len(plan.elements),
                    "artifact_count": len(plan.artifact_unit_ids),
                    "reading_order_count": len(plan.reading_order_unit_ids),
                    "unresolved_unit_count": len(plan.unresolved_unit_ids),
                },
            ),
        )
    ]


def _plan_issues(document: DocumentState) -> list[str]:
    plan = document.structure_mapping_plan
    if plan is None:
        return ["structure mapping plan missing"]
    issues: list[str] = []
    if not plan.document_properties.title_ready:
        issues.append("document title is not ready")
    if not plan.document_properties.primary_language_ready:
        issues.append("primary language is not ready")
    for element in plan.elements:
        if element.artifact and element.include_in_structure_tree:
            issues.append(f"{element.unit_id} is an artifact but included in the structure tree")
        if not element.artifact and element.include_in_structure_tree and element.pdf_structure_role is None:
            issues.append(f"{element.unit_id} is included without a PDF structure role")
        if not element.artifact and element.include_in_structure_tree and element.reading_order_index is None:
            issues.append(f"{element.unit_id} is included without a reading order index")
    return issues
