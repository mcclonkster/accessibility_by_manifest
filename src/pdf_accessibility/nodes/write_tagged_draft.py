from __future__ import annotations

from pdf_accessibility.models.events import (
    NodeEvent,
    artifact_record,
    artifact_registration_event,
    finalization_state_event,
    review_task_event,
    workflow_state_event,
    writeback_report_event,
)
from pdf_accessibility.models.state import DocumentState, DocumentStatus, FinalizationState, ReviewTask
from pdf_accessibility.transition_guards.finalization import can_write_draft
from pdf_accessibility.utils.ids import event_id, stable_id
from pdf_accessibility.utils.json import write_json
from pdf_accessibility.writeback.draft_writer import write_tagged_draft

NODE_NAME = "write_tagged_draft"


def run(document: DocumentState) -> list[NodeEvent]:
    if not can_write_draft(document):
        return [
            finalization_state_event(
                event_id(NODE_NAME, "blocked", document.document_id),
                NODE_NAME,
                FinalizationState.WRITE_BLOCKED,
            ),
            workflow_state_event(
                event_id(NODE_NAME, "blocked", document.document_id),
                NODE_NAME,
                DocumentStatus.WRITE_BLOCKED,
            ),
        ]
    draft_path = document.run_dir / "tagged_draft.pdf"
    report = write_tagged_draft(document, draft_path)
    report_path = document.run_dir / "writeback_report.json"
    write_json(report_path, report)
    draft_artifact = artifact_record(
        artifact_id=f"artifact-{stable_id(NODE_NAME, draft_path)}",
        name="tagged_draft.pdf",
        path=draft_path,
        artifact_type="pdf",
        producer_node=NODE_NAME,
        metadata={
            "draft_only": True,
            "supported_element_count": report.supported_element_count,
            "written_structure_element_count": report.written_structure_element_count,
            "skipped_supported_element_count": report.skipped_supported_element_count,
            "unsupported_element_count": report.unsupported_element_count,
        },
    )
    report_artifact = artifact_record(
        artifact_id=f"artifact-{stable_id(NODE_NAME, report_path)}",
        name="writeback_report.json",
        path=report_path,
        artifact_type="json",
        producer_node=NODE_NAME,
        metadata={"finalization_blocked": report.finalization_blocked},
    )
    events = [
        writeback_report_event(event_id(NODE_NAME, "report-state", document.document_id), NODE_NAME, report),
        artifact_registration_event(event_id(NODE_NAME, "draft-artifact", document.document_id), NODE_NAME, draft_artifact),
        artifact_registration_event(event_id(NODE_NAME, "report-artifact", document.document_id), NODE_NAME, report_artifact),
        workflow_state_event(event_id(NODE_NAME, "workflow", document.document_id), NODE_NAME, DocumentStatus.DRAFT_WRITTEN),
    ]
    if report.finalization_blocked:
        events.append(
            review_task_event(
                event_id(NODE_NAME, "draft-not-final", document.document_id),
                NODE_NAME,
                ReviewTask(
                    task_id=f"review-{stable_id(NODE_NAME, 'draft-not-final', document.document_id)}",
                    issue_code="TAGGED_DRAFT_NOT_FINAL",
                    severity="error",
                    target_ref="document",
                    reason=_draft_not_final_reason(report),
                    suggested_action=_draft_not_final_suggested_action(report),
                    blocking=True,
                    confidence_context={
                        "blocking_categories": report.blocking_categories,
                        "blocking_details": report.blocking_details,
                        "supported_element_count": report.supported_element_count,
                        "skipped_supported_element_count": report.skipped_supported_element_count,
                        "unsupported_element_count": report.unsupported_element_count,
                        "skipped_mcid_count": report.skipped_mcid_count,
                        "title_written": report.title_written,
                        "primary_language_written": report.primary_language_written,
                    },
                ),
            )
        )
    return events


def _draft_not_final_reason(report) -> str:
    reasons: list[str] = []
    categories = set(report.blocking_categories)
    if "unsupported_structure_roles" in categories:
        role_counts = report.unsupported_role_counts or {}
        rendered = ", ".join(f"{role}={count}" for role, count in sorted(role_counts.items()))
        reasons.append(f"unsupported structure roles remain ({rendered})")
    if "skipped_content_stream_marking" in categories:
        reasons.append(f"{report.skipped_mcid_count} planned MCIDs could not be written into page content streams")
    if "missing_document_title" in categories:
        reasons.append("document title is still missing")
    if "missing_primary_language" in categories:
        reasons.append("primary language is still missing")
    if "no_supported_elements" in categories:
        reasons.append("no supported structure elements were available for writeback")
    if not reasons:
        return "Tagged draft writer could not produce a fully finalizable accessible PDF from this structure plan."
    return "Tagged draft writer stopped finalization because " + "; ".join(reasons) + "."


def _draft_not_final_suggested_action(report) -> str:
    actions: list[str] = []
    categories = set(report.blocking_categories)
    if "unsupported_structure_roles" in categories:
        actions.append("resolve or remove unsupported structure roles before treating the draft as final")
    if "skipped_content_stream_marking" in categories:
        actions.append("simplify or re-plan content stream marking for skipped supported elements")
    if "missing_document_title" in categories:
        actions.append("set a document title")
    if "missing_primary_language" in categories:
        actions.append("set a primary language")
    if "no_supported_elements" in categories:
        actions.append("add at least one supported simple structure element to the plan")
    if not actions:
        return "Resolve unsupported structure elements, skipped MCIDs, or missing document properties before finalization."
    return "; ".join(actions).capitalize() + "."
