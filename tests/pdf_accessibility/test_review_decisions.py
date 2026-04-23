from __future__ import annotations

from pathlib import Path

from pdf_accessibility.models.events import review_decision_event
from pdf_accessibility.models.state import DocumentState, ReviewDecision, ReviewTask
from pdf_accessibility.nodes import apply_review_decisions, structure_mapping_plan
from pdf_accessibility.persistence.artifacts import write_run_snapshot
from pdf_accessibility.reducers.apply_events import apply_events
from pdf_accessibility.utils.ids import stable_id
from pdf_accessibility.utils.json import write_json


def _document(tmp_path: Path, tasks: list[ReviewTask]) -> DocumentState:
    return DocumentState(
        document_id="doc-1",
        source_path=tmp_path / "input.pdf",
        run_dir=tmp_path,
        review_tasks=tasks,
    )


def _task(task_id: str, issue_code: str) -> ReviewTask:
    return ReviewTask(
        task_id=task_id,
        issue_code=issue_code,
        severity="error",
        target_ref="document",
        reason=issue_code,
        blocking=True,
    )


def _decision(task_id: str, decision_type: str, value: str | None = None) -> ReviewDecision:
    return ReviewDecision(
        decision_id=f"decision-{stable_id(task_id, decision_type, value)}",
        target_review_task_id=task_id,
        decision_type=decision_type,
        value=value,
        reviewer="test",
        created_at="2026-04-22T00:00:00Z",
    )


def test_set_document_title_decision_resolves_title_task(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-title", "DOCUMENT_TITLE_MISSING")])
    document = apply_events(document, [])
    decision = _decision("task-title", "set_document_title", "Annual Financial Report")

    updated = apply_events(
        document,
        [review_decision_event("event-1", "test", decision)],
    )

    assert updated.metadata is not None
    assert updated.metadata.title == "Annual Financial Report"
    assert updated.review_tasks[0].resolved
    assert updated.review_decisions[0].resolved
    assert updated.blocker_ids == []


def test_set_primary_language_decision_updates_mapping_plan_after_rerun(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-language", "DOCUMENT_LANGUAGE_MISSING")])
    document = apply_events(document, [])
    decision = _decision("task-language", "set_primary_language", "en-US")

    updated = apply_events(document, [review_decision_event("event-1", "test", decision)])
    updated = apply_events(updated, structure_mapping_plan.run(updated))

    assert updated.metadata is not None
    assert updated.metadata.primary_language == "en-US"
    assert updated.structure_mapping_plan is not None
    assert updated.structure_mapping_plan.document_properties.primary_language_ready


def test_draft_only_blocker_cannot_be_resolved_by_review_decision(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-draft", "TAGGED_DRAFT_NOT_FINAL")])
    document = apply_events(document, [])
    decision = _decision("task-draft", "resolve_review_task")

    updated = apply_events(document, [review_decision_event("event-1", "test", decision)])

    assert not updated.review_tasks[0].resolved
    assert not updated.review_decisions[0].resolved
    assert "cannot be resolved" in (updated.review_decisions[0].blocked_reason or "")
    assert updated.blocker_ids == ["task-draft"]


def test_defer_complex_table_records_decision_but_keeps_blocker(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-table", "TABLE_HEADERS_UNCERTAIN")])
    document = apply_events(document, [])
    decision = _decision("task-table", "defer_complex_table", "defer to later table review")

    updated = apply_events(document, [review_decision_event("event-1", "test", decision)])

    assert not updated.review_tasks[0].resolved
    assert not updated.review_decisions[0].resolved
    assert "table deferral recorded" in (updated.review_decisions[0].blocked_reason or "")
    assert updated.blocker_ids == ["task-table"]


def test_apply_review_decisions_node_loads_file_based_decisions(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-title", "DOCUMENT_TITLE_MISSING")])
    decision = _decision("task-title", "set_document_title", "Filed Title")
    write_json(tmp_path / "review_decisions.json", [decision.model_dump(mode="json")])

    updated = apply_events(document, apply_review_decisions.run(document))

    assert updated.metadata is not None
    assert updated.metadata.title == "Filed Title"
    assert updated.review_tasks[0].resolved


def test_review_decisions_json_is_persisted(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-title", "DOCUMENT_TITLE_MISSING")])
    decision = _decision("task-title", "set_document_title", "Annual Report")
    updated = apply_events(document, [review_decision_event("event-1", "test", decision)])

    write_run_snapshot(updated)

    assert (tmp_path / "review_decisions.json").exists()
