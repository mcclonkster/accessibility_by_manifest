from __future__ import annotations

from pathlib import Path

from pdf_accessibility.models.events import finding_event, workflow_state_event
from pdf_accessibility.models.state import DocumentState, DocumentStatus, Finding, FindingClass
from pdf_accessibility.reducers.apply_events import apply_events


def test_apply_events_recomputes_blockers(tmp_path: Path) -> None:
    document = DocumentState(document_id="doc-1", source_path=tmp_path / "input.pdf", run_dir=tmp_path)
    finding = Finding(
        finding_id="finding-1",
        node_name="test",
        finding_class=FindingClass.BLOCKING_ISSUE,
        target_ref="document",
        message="Missing primary language.",
    )

    updated = apply_events(document, [finding_event("event-1", "test", finding)])

    assert updated.blocker_ids == ["finding-1"]
    assert document.blocker_ids == []


def test_illegal_workflow_transition_is_ignored(tmp_path: Path) -> None:
    document = DocumentState(document_id="doc-1", source_path=tmp_path / "input.pdf", run_dir=tmp_path)

    updated = apply_events(document, [workflow_state_event("event-1", "test", DocumentStatus.FINALIZED)])

    assert updated.document_status is DocumentStatus.PENDING

