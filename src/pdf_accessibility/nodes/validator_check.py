from __future__ import annotations

from pdf_accessibility.models.events import (
    NodeEvent,
    artifact_record,
    artifact_registration_event,
    validator_finding_event,
    workflow_state_event,
)
from pdf_accessibility.models.state import DocumentState, DocumentStatus
from pdf_accessibility.services.internal_validator import validate_tagged_draft, validator_report_payload
from pdf_accessibility.utils.ids import event_id, stable_id
from pdf_accessibility.utils.json import write_json

NODE_NAME = "validator_check"


def run(document: DocumentState) -> list[NodeEvent]:
    output_path = document.run_dir / "validator_findings.json"
    draft_path = document.output_artifacts.tagged_draft_pdf
    findings = validate_tagged_draft(draft_path, document.writeback_report) if draft_path else []
    write_json(output_path, validator_report_payload(draft_path or document.run_dir / "tagged_draft.pdf", findings))
    artifact = artifact_record(
        artifact_id=f"artifact-{stable_id(NODE_NAME, output_path)}",
        name="validator_findings.json",
        path=output_path,
        artifact_type="json",
        producer_node=NODE_NAME,
        metadata={"validator": "internal_tagged_draft", "finding_count": len(findings)},
    )
    events: list[NodeEvent] = [
        artifact_registration_event(event_id(NODE_NAME, "artifact", document.document_id), NODE_NAME, artifact),
        workflow_state_event(event_id(NODE_NAME, "workflow", document.document_id), NODE_NAME, DocumentStatus.VALIDATED),
    ]
    events.extend(
        validator_finding_event(event_id(NODE_NAME, finding.finding_id), NODE_NAME, finding)
        for finding in findings
    )
    return events
