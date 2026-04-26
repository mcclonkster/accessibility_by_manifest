from __future__ import annotations

import shutil

from pdf_accessibility.models.events import NodeEvent, artifact_record, artifact_registration_event, finalization_state_event, workflow_state_event
from pdf_accessibility.models.state import DocumentState, DocumentStatus, FinalizationState
from pdf_accessibility.transition_guards.finalization import can_finalize
from pdf_accessibility.utils.ids import event_id, stable_id
from pdf_accessibility.utils.json import write_json

NODE_NAME = "finalize_accessible_output"


def run(document: DocumentState) -> list[NodeEvent]:
    status_path = document.run_dir / "finalization_status.json"
    if not can_finalize(document):
        report = document.writeback_report
        write_json(
            status_path,
            {
                "document_status": document.document_status.value,
                "finalization_state": "needs_review",
                "blocker_ids": document.blocker_ids,
                "can_finalize": False,
                "writeback_finalization_blocked": report.finalization_blocked if report is not None else None,
                "writeback_blocking_categories": report.blocking_categories if report is not None else [],
                "writeback_blocking_details": report.blocking_details if report is not None else {},
            },
        )
        status_artifact = artifact_record(
            artifact_id=f"artifact-{stable_id(NODE_NAME, status_path)}",
            name="finalization_status.json",
            path=status_path,
            artifact_type="json",
            producer_node=NODE_NAME,
        )
        return [
            artifact_registration_event(event_id(NODE_NAME, "status", document.document_id), NODE_NAME, status_artifact),
            finalization_state_event(event_id(NODE_NAME, "review", document.document_id), NODE_NAME, FinalizationState.NEEDS_REVIEW),
            workflow_state_event(event_id(NODE_NAME, "review", document.document_id), NODE_NAME, DocumentStatus.NEEDS_REVIEW),
        ]
    output_path = document.run_dir / "accessible_output.pdf"
    shutil.copyfile(document.output_artifacts.tagged_draft_pdf, output_path)
    write_json(
        status_path,
        {
            "document_status": document.document_status.value,
            "finalization_state": "finalized",
            "blocker_ids": [],
            "can_finalize": True,
            "writeback_finalization_blocked": False,
            "writeback_blocking_categories": [],
            "writeback_blocking_details": {},
        },
    )
    output_artifact = artifact_record(
        artifact_id=f"artifact-{stable_id(NODE_NAME, output_path)}",
        name="accessible_output.pdf",
        path=output_path,
        artifact_type="pdf",
        producer_node=NODE_NAME,
        metadata={"scaffold": True},
    )
    status_artifact = artifact_record(
        artifact_id=f"artifact-{stable_id(NODE_NAME, status_path)}",
        name="finalization_status.json",
        path=status_path,
        artifact_type="json",
        producer_node=NODE_NAME,
    )
    return [
        artifact_registration_event(event_id(NODE_NAME, "output", document.document_id), NODE_NAME, output_artifact),
        artifact_registration_event(event_id(NODE_NAME, "status", document.document_id), NODE_NAME, status_artifact),
        finalization_state_event(event_id(NODE_NAME, "finalized", document.document_id), NODE_NAME, FinalizationState.FINALIZED),
        workflow_state_event(event_id(NODE_NAME, "workflow", document.document_id), NODE_NAME, DocumentStatus.FINALIZED),
    ]
