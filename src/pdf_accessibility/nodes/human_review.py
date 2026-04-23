from __future__ import annotations

from pdf_accessibility.models.events import NodeEvent, artifact_record, artifact_registration_event, finalization_state_event
from pdf_accessibility.models.state import DocumentState, FinalizationState
from pdf_accessibility.utils.ids import event_id, stable_id
from pdf_accessibility.utils.json import write_json

NODE_NAME = "human_review"


def run(document: DocumentState) -> list[NodeEvent]:
    output_path = document.run_dir / "review_tasks.json"
    write_json(output_path, [task.model_dump(mode="json") for task in document.review_tasks])
    artifact = artifact_record(
        artifact_id=f"artifact-{stable_id(NODE_NAME, output_path)}",
        name="review_tasks.json",
        path=output_path,
        artifact_type="json",
        producer_node=NODE_NAME,
        metadata={"open_task_count": sum(1 for task in document.review_tasks if not task.resolved)},
    )
    state = FinalizationState.NEEDS_REVIEW if document.blocker_ids else FinalizationState.PENDING
    return [
        artifact_registration_event(event_id(NODE_NAME, "artifact", document.document_id), NODE_NAME, artifact),
        finalization_state_event(event_id(NODE_NAME, "finalization", document.document_id), NODE_NAME, state),
    ]

