from __future__ import annotations

from pathlib import Path

from pdf_accessibility.models.state import ReviewTask
from pdf_accessibility.services.review_decision_templates import build_review_decision_template


def _task(task_id: str, issue_code: str) -> ReviewTask:
    return ReviewTask(
        task_id=task_id,
        issue_code=issue_code,
        severity="warning",
        target_ref="document",
        reason=issue_code,
        blocking=True,
    )


def test_template_includes_title_and_language_decisions(tmp_path: Path) -> None:
    template = build_review_decision_template(
        [
            _task("task-title", "DOCUMENT_TITLE_MISSING"),
            _task("task-language", "DOCUMENT_LANGUAGE_MISSING"),
        ],
        source_path=tmp_path / "review_tasks.json",
    )

    decisions = template["decisions"]
    assert [entry["decision_type"] for entry in decisions] == ["set_document_title", "set_primary_language"]
    assert decisions[0]["value"] == ""
    assert decisions[1]["value"] == ""
    assert template["manual_only_tasks"] == []


def test_template_marks_non_resolvable_issue_as_manual_only(tmp_path: Path) -> None:
    template = build_review_decision_template(
        [_task("task-draft", "TAGGED_DRAFT_NOT_FINAL")],
        source_path=tmp_path / "review_tasks.json",
    )

    assert template["decisions"] == []
    assert template["manual_only_tasks"][0]["issue_code"] == "TAGGED_DRAFT_NOT_FINAL"
    assert "pipeline changes" in template["manual_only_tasks"][0]["why_not_in_template"]


def test_template_exposes_actionable_table_review_decision(tmp_path: Path) -> None:
    template = build_review_decision_template(
        [_task("task-table", "TABLE_HEADERS_UNCERTAIN")],
        source_path=tmp_path / "review_tasks.json",
    )

    decision = template["decisions"][0]
    assert decision["decision_type"] == "confirm_table_reviewed"
    assert decision["recommended_decision_types"] == ["confirm_table_reviewed", "defer_complex_table"]
    assert "does not imply the table is safely writable" in decision["note"]


def test_template_exposes_actionable_figure_review_decision(tmp_path: Path) -> None:
    template = build_review_decision_template(
        [_task("task-figure", "FIGURE_ALT_TEXT_REQUIRED")],
        source_path=tmp_path / "review_tasks.json",
    )

    decision = template["decisions"][0]
    assert decision["decision_type"] == "provide_alt_text"
    assert decision["recommended_decision_types"] == ["provide_alt_text", "mark_figure_decorative"]
    assert "mark_figure_decorative" in decision["note"]


def test_template_omits_summary_figure_task_when_per_figure_tasks_exist(tmp_path: Path) -> None:
    template = build_review_decision_template(
        [
            _task("task-summary", "FIGURE_CANDIDATES_REQUIRE_REVIEW"),
            _task("task-figure", "FIGURE_ALT_TEXT_REQUIRED"),
        ],
        source_path=tmp_path / "review_tasks.json",
    )

    assert len(template["decisions"]) == 1
    assert template["decisions"][0]["issue_code"] == "FIGURE_ALT_TEXT_REQUIRED"
    assert template["manual_only_tasks"] == []
