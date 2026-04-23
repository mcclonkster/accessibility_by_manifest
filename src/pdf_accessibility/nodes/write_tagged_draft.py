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
            "written_structure_element_count": report.written_structure_element_count,
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
    return [
        writeback_report_event(event_id(NODE_NAME, "report-state", document.document_id), NODE_NAME, report),
        artifact_registration_event(event_id(NODE_NAME, "draft-artifact", document.document_id), NODE_NAME, draft_artifact),
        artifact_registration_event(event_id(NODE_NAME, "report-artifact", document.document_id), NODE_NAME, report_artifact),
        review_task_event(
            event_id(NODE_NAME, "draft-not-final", document.document_id),
            NODE_NAME,
            ReviewTask(
                task_id=f"review-{stable_id(NODE_NAME, 'draft-not-final', document.document_id)}",
                issue_code="TAGGED_DRAFT_NOT_FINAL",
                severity="error",
                target_ref="document",
                reason="Tagged draft writer is a limited spike and cannot produce a finalized accessible PDF yet.",
                suggested_action="Complete MCID assignment, ParentTree construction, validator repair, and full structure writeback before finalization.",
                blocking=True,
            ),
        ),
        workflow_state_event(event_id(NODE_NAME, "workflow", document.document_id), NODE_NAME, DocumentStatus.DRAFT_WRITTEN),
    ]
