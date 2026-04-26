from __future__ import annotations

import json
from pathlib import Path

from pdf_accessibility.models.state import DocumentState, FinalizationState
from pdf_accessibility.services.run_explanation import build_run_explanation_prompt


def _document(tmp_path: Path) -> DocumentState:
    source = tmp_path / "input.pdf"
    source.write_bytes(b"%PDF-1.7\n%%EOF\n")
    return DocumentState(document_id="doc-1", source_path=source, run_dir=tmp_path)


def test_build_run_explanation_prompt_separates_actionable_and_structural_blockers(tmp_path: Path) -> None:
    document = _document(tmp_path)
    document.finalization_state = FinalizationState.NEEDS_REVIEW

    (tmp_path / "operator_guide.json").write_text(
        json.dumps(
            {
                "blocker_count": 4,
                "primary_next_step": {
                    "action": "fill_review_decisions",
                    "path": str(tmp_path / "review_decisions_template.json"),
                },
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "finalization_status.json").write_text(
        json.dumps(
            {
                "writeback_blocking_categories": ["unsupported_structure_roles"],
                "writeback_blocking_details": {
                    "unsupported_structure_roles": {
                        "unsupported_role_counts": {"Figure": 1}
                    }
                },
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "artifact_manifest.json").write_text(json.dumps({"records": []}), encoding="utf-8")
    (tmp_path / "writeback_report.json").write_text(json.dumps({"finalization_blocked": True}), encoding="utf-8")
    (tmp_path / "review_tasks.json").write_text(
        json.dumps(
            [
                {
                    "task_id": "task-title",
                    "issue_code": "DOCUMENT_TITLE_MISSING",
                    "severity": "warning",
                    "target_ref": "document_metadata.title",
                    "reason": "Missing title.",
                    "resolved": False,
                },
                {
                    "task_id": "task-ocr",
                    "issue_code": "IMAGE_ONLY_PAGE_OCR_REQUIRED",
                    "severity": "warning",
                    "target_ref": "page:75",
                    "reason": "OCR required.",
                    "resolved": False,
                },
                {
                    "task_id": "task-draft",
                    "issue_code": "TAGGED_DRAFT_NOT_FINAL",
                    "severity": "error",
                    "target_ref": "document",
                    "reason": "Draft not final.",
                    "resolved": False,
                },
                {
                    "task_id": "task-language",
                    "issue_code": "DOCUMENT_LANGUAGE_MISSING",
                    "severity": "warning",
                    "target_ref": "document_metadata.primary_language",
                    "reason": "Missing language.",
                    "resolved": True,
                },
            ]
        ),
        encoding="utf-8",
    )
    (tmp_path / "review_decisions.json").write_text(
        json.dumps(
            [
                {
                    "decision_type": "set_document_title",
                    "target_review_task_id": "task-title",
                    "value": "Annual Report",
                }
            ]
        ),
        encoding="utf-8",
    )

    prompt = build_run_explanation_prompt(document)

    assert "Explicitly separate actionable blockers, structural blockers, and already-resolved inputs." in prompt
    assert "Do not enumerate more than max_blockers_to_enumerate blockers" in prompt
    assert '"blocker_counts_by_issue_code": {' in prompt
    assert '"DOCUMENT_TITLE_MISSING": 1' in prompt
    assert '"IMAGE_ONLY_PAGE_OCR_REQUIRED": 1' in prompt
    assert '"TAGGED_DRAFT_NOT_FINAL": 1' in prompt
    assert '"actionable_blockers": [' in prompt
    assert '"structural_blockers": [' in prompt
    assert '"already_resolved_inputs": [' in prompt
    assert '"decision_type": "set_document_title"' in prompt
