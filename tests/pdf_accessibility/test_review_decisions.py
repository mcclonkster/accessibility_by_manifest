from __future__ import annotations

from pathlib import Path

import fitz

from pdf_accessibility.models.state import DocumentMetadataEvidence, DocumentStatus, NormalizedUnit, PageState, RegionState, RegionStatus
from pdf_accessibility.models.events import review_decision_event
from pdf_accessibility.models.state import DocumentState, ReviewDecision, ReviewTask
from pdf_accessibility.nodes import apply_review_decisions, structure_mapping_plan
from pdf_accessibility.persistence.artifacts import write_run_snapshot
from pdf_accessibility.reducers.apply_events import apply_events
from pdf_accessibility.utils.ids import stable_id
from pdf_accessibility.utils.json import write_json
from pdf_accessibility.nodes import write_tagged_draft


def _document(tmp_path: Path, tasks: list[ReviewTask]) -> DocumentState:
    source = tmp_path / "input.pdf"
    _write_pdf(source)
    return DocumentState(
        document_id="doc-1",
        source_path=source,
        run_dir=tmp_path,
        review_tasks=tasks,
    )


def _write_pdf(path: Path) -> None:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Review decision test PDF")
    document.save(path)
    document.close()


def _task(task_id: str, issue_code: str, *, target_ref: str = "document", blocking: bool = True) -> ReviewTask:
    return ReviewTask(
        task_id=task_id,
        issue_code=issue_code,
        severity="error",
        target_ref=target_ref,
        reason=issue_code,
        blocking=blocking,
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


def test_confirm_table_reviewed_resolves_table_task(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-table", "TABLE_HEADERS_UNCERTAIN")])
    document = apply_events(document, [])
    decision = _decision("task-table", "confirm_table_reviewed", "Header row reviewed and accepted by human.")

    updated = apply_events(document, [review_decision_event("event-1", "test", decision)])

    assert updated.review_tasks[0].resolved
    assert updated.review_decisions[0].resolved
    assert updated.blocker_ids == []


def test_confirm_table_reviewed_requires_non_empty_summary(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-table", "TABLE_HEADERS_UNCERTAIN")])
    document = apply_events(document, [])
    decision = _decision("task-table", "confirm_table_reviewed", "")

    updated = apply_events(document, [review_decision_event("event-1", "test", decision)])

    assert not updated.review_tasks[0].resolved
    assert not updated.review_decisions[0].resolved
    assert "table review summary is empty" in (updated.review_decisions[0].blocked_reason or "")
    assert updated.blocker_ids == ["task-table"]


def test_provide_alt_text_requires_non_empty_value(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-figure", "FIGURE_ALT_TEXT_REQUIRED", target_ref="region-figure-1")])
    document = apply_events(document, [])
    decision = _decision("task-figure", "provide_alt_text", "")

    updated = apply_events(document, [review_decision_event("event-1", "test", decision)])

    assert not updated.review_tasks[0].resolved
    assert not updated.review_decisions[0].resolved
    assert "alt text value is empty" in (updated.review_decisions[0].blocked_reason or "")
    assert updated.blocker_ids == ["task-figure"]


def test_mark_figure_decorative_resolves_figure_task(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-figure", "FIGURE_ALT_TEXT_REQUIRED", target_ref="region-figure-1")])
    document = apply_events(document, [])
    decision = _decision("task-figure", "mark_figure_decorative")

    updated = apply_events(document, [review_decision_event("event-1", "test", decision)])

    assert updated.review_tasks[0].resolved
    assert updated.review_decisions[0].resolved
    assert updated.blocker_ids == []


def test_resolving_all_figure_tasks_resolves_summary_blocker(tmp_path: Path) -> None:
    document = _document(
        tmp_path,
        [
            _task(
                "task-summary",
                "FIGURE_CANDIDATES_REQUIRE_REVIEW",
                target_ref="document_summary.figure_candidate_count",
            ),
            _task("task-figure-1", "FIGURE_ALT_TEXT_REQUIRED", target_ref="region-figure-1"),
            _task("task-figure-2", "FIGURE_ALT_TEXT_SPOT_CHECK", target_ref="region-figure-2", blocking=False),
        ],
    )
    document = apply_events(document, [])

    updated = apply_events(
        document,
        [
            review_decision_event("event-1", "test", _decision("task-figure-1", "provide_alt_text", "Quarterly revenue chart.")),
            review_decision_event("event-2", "test", _decision("task-figure-2", "mark_figure_decorative")),
        ],
    )

    summary_task = next(task for task in updated.review_tasks if task.task_id == "task-summary")
    assert summary_task.resolved
    assert all(decision.resolved for decision in updated.review_decisions)
    assert updated.blocker_ids == []


def test_confirm_table_reviewed_does_not_imply_finalizable_writeback(tmp_path: Path) -> None:
    source = tmp_path / "input.pdf"
    _write_pdf(source)
    document = DocumentState(
        document_id="doc-1",
        source_path=source,
        run_dir=tmp_path,
        metadata=DocumentMetadataEvidence(title="Annual Report", primary_language="en-US"),
        review_tasks=[_task("task-table", "TABLE_HEADERS_UNCERTAIN")],
        normalized_units=[
            NormalizedUnit(
                unit_id="table-1",
                unit_type="table",
                page_numbers=[1],
                reading_order_index=0,
            )
        ],
        pages=[
            PageState(
                page_number=1,
                regions=[RegionState(region_id="region-1", page_number=1, status=RegionStatus.COMMITTABLE)],
            )
        ],
    )
    document = apply_events(document, [])
    decision = _decision("task-table", "confirm_table_reviewed", "Table structure and headers reviewed by human.")

    updated = apply_events(document, [review_decision_event("event-1", "test", decision)])
    updated = apply_events(updated, structure_mapping_plan.run(updated))
    updated.document_status = DocumentStatus.DRAFT_READY
    updated = apply_events(updated, write_tagged_draft.run(updated))

    assert any(task.issue_code == "TAGGED_DRAFT_NOT_FINAL" for task in updated.review_tasks)
    assert updated.writeback_report is not None
    assert updated.writeback_report.finalization_blocked is True
    assert updated.writeback_report.unsupported_element_count >= 1
    assert updated.blocker_ids


def test_apply_review_decisions_node_loads_file_based_decisions(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-title", "DOCUMENT_TITLE_MISSING")])
    decision = _decision("task-title", "set_document_title", "Filed Title")
    write_json(tmp_path / "review_decisions.json", [decision.model_dump(mode="json")])

    updated = apply_events(document, apply_review_decisions.run(document))

    assert updated.metadata is not None
    assert updated.metadata.title == "Filed Title"
    assert updated.review_tasks[0].resolved


def test_apply_review_decisions_node_accepts_wrapper_object(tmp_path: Path) -> None:
    document = _document(tmp_path, [_task("task-title", "DOCUMENT_TITLE_MISSING")])
    decision = _decision("task-title", "set_document_title", "Filed Title")
    write_json(tmp_path / "review_decisions.json", {"decisions": [decision.model_dump(mode="json")]})

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
