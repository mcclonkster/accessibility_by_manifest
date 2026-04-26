from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pdf_accessibility.models.state import ReviewTask
from pdf_accessibility.utils.ids import stable_id

FIGURE_REVIEW_ISSUE_CODES = {
    "FIGURE_ALT_TEXT_REQUIRED",
    "FIGURE_ALT_TEXT_SPOT_CHECK",
}


def resolve_review_tasks_path(path: Path) -> Path:
    if path.is_dir():
        return path / "review_tasks.json"
    return path


def load_review_tasks(path: Path) -> list[ReviewTask]:
    review_tasks_path = resolve_review_tasks_path(path)
    raw = json.loads(review_tasks_path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError(f"Expected review task list in {review_tasks_path}")
    return [ReviewTask.model_validate(item) for item in raw]


def build_review_decision_template(review_tasks: list[ReviewTask], *, source_path: Path) -> dict[str, Any]:
    decisions: list[dict[str, Any]] = []
    manual_only_tasks: list[dict[str, Any]] = []
    has_figure_child_tasks = any(task.issue_code in FIGURE_REVIEW_ISSUE_CODES and not task.resolved for task in review_tasks)
    for task in review_tasks:
        if task.resolved:
            continue
        if task.issue_code == "FIGURE_CANDIDATES_REQUIRE_REVIEW" and has_figure_child_tasks:
            continue
        template = _decision_template_for_task(task)
        if template is None:
            manual_only_tasks.append(
                {
                    "target_review_task_id": task.task_id,
                    "issue_code": task.issue_code,
                    "reason": task.reason,
                    "suggested_action": task.suggested_action,
                    "why_not_in_template": _manual_only_reason(task),
                }
            )
            continue
        decisions.append(template)
    return {
        "source_review_tasks_path": str(source_path),
        "decision_count": len(decisions),
        "manual_only_task_count": len(manual_only_tasks),
        "notes": [
            "Fill in blank values before using this file with --review-decisions.",
            "Tasks listed under manual_only_tasks are not safely resolvable through the current review-decision path.",
        ],
        "decisions": decisions,
        "manual_only_tasks": manual_only_tasks,
    }


def _decision_template_for_task(task: ReviewTask) -> dict[str, Any] | None:
    if task.issue_code == "DOCUMENT_TITLE_MISSING":
        return _decision(task, "set_document_title", "", "Provide a trustworthy document title.")
    if task.issue_code == "DOCUMENT_LANGUAGE_MISSING":
        return _decision(task, "set_primary_language", "", "Provide a BCP 47 language tag such as en-US.")
    if task.issue_code == "FIGURE_ALT_TEXT_REQUIRED":
        return _decision(
            task,
            "provide_alt_text",
            "",
            "Provide trusted alt text, or change decision_type to mark_figure_decorative if the figure is decorative.",
            recommended_decision_types=["provide_alt_text", "mark_figure_decorative"],
        )
    if task.issue_code == "FIGURE_ALT_TEXT_SPOT_CHECK":
        return _decision(
            task,
            "provide_alt_text",
            "",
            "Confirm whether the figure is meaningful. Provide trusted alt text for meaningful figures, or change decision_type to mark_figure_decorative if human review confirms it is decorative.",
            recommended_decision_types=["provide_alt_text", "mark_figure_decorative"],
        )
    if task.issue_code in {"TABLE_HEADERS_UNCERTAIN", "TABLE_STRUCTURE_SPOT_CHECK"}:
        return _decision(
            task,
            "confirm_table_reviewed",
            "",
            "Record the human table-review outcome. This can clear review uncertainty, but it does not imply the table is safely writable/finalizable.",
            recommended_decision_types=["confirm_table_reviewed", "defer_complex_table"],
        )
    return None


def _decision(
    task: ReviewTask,
    decision_type: str,
    value: str,
    note: str,
    *,
    recommended_decision_types: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "decision_id": f"decision-template-{stable_id(task.task_id, decision_type)}",
        "target_review_task_id": task.task_id,
        "issue_code": task.issue_code,
        "decision_type": decision_type,
        "recommended_decision_types": recommended_decision_types or [decision_type],
        "value": value,
        "note": note,
        "reviewer": "local",
    }


def _manual_only_reason(task: ReviewTask) -> str:
    if task.issue_code == "TAGGED_DRAFT_NOT_FINAL":
        return "Requires writeback, structure, or pipeline changes rather than a simple review decision."
    if task.issue_code == "STRUCTURE_MAPPING_PLAN_MISSING":
        return "Requires workflow/planning regeneration before a review decision can help."
    if task.issue_code == "FIGURE_CANDIDATES_REQUIRE_REVIEW":
        return "Requires per-figure review tasks before the current workflow can offer actionable figure decisions."
    return "No safe automated review-decision template is defined for this issue code yet."
