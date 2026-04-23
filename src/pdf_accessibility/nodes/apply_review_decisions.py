from __future__ import annotations

import json

from pydantic import ValidationError

from pdf_accessibility.models.events import NodeEvent, review_decision_event, workflow_state_event
from pdf_accessibility.models.state import DocumentState, DocumentStatus, ReviewDecision
from pdf_accessibility.utils.ids import event_id

NODE_NAME = "apply_review_decisions"


def run(document: DocumentState) -> list[NodeEvent]:
    decisions = _load_review_decisions(document)
    events = [
        review_decision_event(event_id(NODE_NAME, decision.decision_id), NODE_NAME, decision)
        for decision in decisions
        if decision.decision_id not in {existing.decision_id for existing in document.review_decisions}
    ]
    if not document.blocker_ids:
        events.append(
            workflow_state_event(
                event_id(NODE_NAME, "workflow", document.document_id),
                NODE_NAME,
                DocumentStatus.REVIEW_APPLIED,
            )
        )
    return events


def _load_review_decisions(document: DocumentState) -> list[ReviewDecision]:
    path = document.run_dir / "review_decisions.json"
    if not path.exists():
        return []
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    if not isinstance(raw, list):
        return []
    decisions: list[ReviewDecision] = []
    for item in raw:
        try:
            decisions.append(ReviewDecision.model_validate(item))
        except ValidationError:
            continue
    return decisions
