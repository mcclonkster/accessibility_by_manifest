from __future__ import annotations

import json
from pathlib import Path

from pdf_accessibility.models.state import ArtifactRecord, DocumentState
from pdf_accessibility.models.state import FinalizationState
from pdf_accessibility.persistence.run_record import write_run_record
from pdf_accessibility.services.internal_validator import validator_report_payload
from pdf_accessibility.services.ocr_recovery_templates import build_ocr_recovery_template
from pdf_accessibility.services.review_decision_templates import build_review_decision_template
from pdf_accessibility.utils.ids import stable_id
from pdf_accessibility.utils.json import model_to_jsonable, write_json


SNAPSHOT_ARTIFACTS: tuple[tuple[str, str], ...] = (
    ("input.pdf", "source_pdf"),
    ("document_state.json", "state_snapshot"),
    ("command.txt", "run_command"),
    ("config.json", "run_config"),
    ("environment.txt", "run_environment"),
    ("git.txt", "run_git"),
    ("notes.md", "run_notes"),
    ("status.json", "run_status"),
    ("manifest.json", "run_manifest"),
    ("findings.jsonl", "findings_log"),
    ("review_tasks.json", "review_tasks"),
    ("review_decisions.json", "review_decisions"),
    ("normalized_structure.json", "normalized_structure"),
    ("structure_mapping_plan.json", "structure_mapping_plan"),
    ("writeback_report.json", "writeback_report"),
    ("tagging_plan.json", "tagging_plan"),
    ("validator_findings.json", "validator_findings"),
    ("finalization_status.json", "finalization_status"),
    ("operator_guide.json", "operator_guide"),
    ("run_log.json", "run_log"),
    ("artifact_manifest.json", "artifact_manifest"),
)


def write_run_snapshot(document: DocumentState) -> None:
    _sync_ocr_recovery_template(document)
    _sync_review_decisions_template(document)

    write_json(document.run_dir / "document_state.json", document)
    write_json(document.run_dir / "review_tasks.json", [task.model_dump(mode="json") for task in document.review_tasks])
    write_json(
        document.run_dir / "review_decisions.json",
        [decision.model_dump(mode="json") for decision in document.review_decisions],
    )
    write_json(
        document.run_dir / "normalized_structure.json",
        [unit.model_dump(mode="json") for unit in document.normalized_units],
    )
    write_json(
        document.run_dir / "structure_mapping_plan.json",
        document.structure_mapping_plan.model_dump(mode="json") if document.structure_mapping_plan else {},
    )
    write_json(
        document.run_dir / "writeback_report.json",
        document.writeback_report.model_dump(mode="json") if document.writeback_report else {},
    )
    _write_validator_findings(document)
    write_json(document.run_dir / "finalization_status.json", _finalization_status(document))
    write_json(document.run_dir / "operator_guide.json", _operator_guide(document))
    write_json(
        document.run_dir / "tagging_plan.json",
        {
            "status": document.document_status.value,
            "finalization_state": document.finalization_state.value,
            "blocker_ids": document.blocker_ids,
            "writeback_ready": not document.blocker_ids,
            "writeback_readiness_reason": _writeback_readiness_reason(document),
            "unit_count": len(document.normalized_units),
            "units_by_type": _unit_counts(document),
            "review_task_count": len(document.review_tasks),
            "review_counts_by_severity": _review_counts_by_severity(document),
            "blocker_counts_by_issue_code": _blocker_counts_by_issue_code(document),
            "structure_mapping": _structure_mapping_summary(document),
            "writeback_report": _writeback_summary(document),
        },
    )
    _write_findings_jsonl(document)
    write_run_record(document)
    _ensure_required_artifact_records(document)
    write_json(document.run_dir / "run_log.json", _run_log(document))
    write_json(document.run_dir / "artifact_manifest.json", document.artifact_manifest)


def artifact_path(document: DocumentState, name: str) -> Path:
    return document.run_dir / name


def _ensure_required_artifact_records(document: DocumentState) -> None:
    for name, artifact_type in SNAPSHOT_ARTIFACTS:
        path = document.source_path if name == "input.pdf" else document.run_dir / name
        _register_artifact(document, name, path, artifact_type, producer_node="persistence")
    _register_optional_run_log_artifacts(document)

    if document.output_artifacts.tagged_draft_pdf and document.output_artifacts.tagged_draft_pdf.exists():
        _register_artifact(
            document,
            "tagged_draft.pdf",
            document.output_artifacts.tagged_draft_pdf,
            "tagged_draft_pdf",
            producer_node="write_tagged_draft",
        )
    if document.output_artifacts.accessible_output_pdf and document.output_artifacts.accessible_output_pdf.exists():
        _register_artifact(
            document,
            "accessible_output.pdf",
            document.output_artifacts.accessible_output_pdf,
            "accessible_output_pdf",
            producer_node="finalize_accessible_output",
        )
    if document.output_artifacts.accessible_output_html and document.output_artifacts.accessible_output_html.exists():
        _register_artifact(
            document,
            "accessible_output.html",
            document.output_artifacts.accessible_output_html,
            "accessible_output_html",
            producer_node="write_accessible_html",
        )
    if (
        document.output_artifacts.review_decisions_template_json
        and document.output_artifacts.review_decisions_template_json.exists()
    ):
        _register_artifact(
            document,
            "review_decisions_template.json",
            document.output_artifacts.review_decisions_template_json,
            "review_decisions_template",
            producer_node="persistence",
        )
    if document.output_artifacts.ocr_recovery_template_json and document.output_artifacts.ocr_recovery_template_json.exists():
        _register_artifact(
            document,
            "ocr_recovery_template.json",
            document.output_artifacts.ocr_recovery_template_json,
            "ocr_recovery_template",
            producer_node="persistence",
        )
    if document.output_artifacts.run_explanation_markdown and document.output_artifacts.run_explanation_markdown.exists():
        _register_artifact(
            document,
            "run_explanation.md",
            document.output_artifacts.run_explanation_markdown,
            "run_explanation_markdown",
            producer_node="cli",
        )
    if document.output_artifacts.run_explanation_log and document.output_artifacts.run_explanation_log.exists():
        _register_artifact(
            document,
            "run_explanation.log",
            document.output_artifacts.run_explanation_log,
            "run_explanation_log",
            producer_node="cli",
        )

    document.output_artifacts.review_tasks_json = document.run_dir / "review_tasks.json"
    document.output_artifacts.execution_log = document.run_dir / "logs" / "execution.log"
    document.output_artifacts.debug_log = document.run_dir / "logs" / "debug.log"
    document.output_artifacts.events_jsonl = document.run_dir / "logs" / "events.jsonl"
    if document.output_artifacts.review_decisions_template_json is None:
        candidate = document.run_dir / "review_decisions_template.json"
        if candidate.exists():
            document.output_artifacts.review_decisions_template_json = candidate
    if document.output_artifacts.ocr_recovery_template_json is None:
        candidate = document.run_dir / "ocr_recovery_template.json"
        if candidate.exists():
            document.output_artifacts.ocr_recovery_template_json = candidate
    if document.output_artifacts.run_explanation_markdown is None:
        candidate = document.run_dir / "run_explanation.md"
        if candidate.exists():
            document.output_artifacts.run_explanation_markdown = candidate
    if document.output_artifacts.run_explanation_log is None:
        candidate = document.run_dir / "logs" / "run_explanation.log"
        if candidate.exists():
            document.output_artifacts.run_explanation_log = candidate
    document.output_artifacts.writeback_report_json = document.run_dir / "writeback_report.json"
    document.output_artifacts.validator_findings_json = document.run_dir / "validator_findings.json"
    document.output_artifacts.operator_guide_json = document.run_dir / "operator_guide.json"
    document.output_artifacts.finalization_status_json = document.run_dir / "finalization_status.json"
    _deduplicate_artifact_records(document)


def _register_optional_run_log_artifacts(document: DocumentState) -> None:
    execution_log = document.run_dir / "logs" / "execution.log"
    if execution_log.exists():
        _register_artifact(
            document,
            "execution.log",
            execution_log,
            "execution_log",
            producer_node="persistence",
        )
    debug_log = document.run_dir / "logs" / "debug.log"
    if debug_log.exists():
        _register_artifact(
            document,
            "debug.log",
            debug_log,
            "debug_log",
            producer_node="persistence",
        )
    events_jsonl = document.run_dir / "logs" / "events.jsonl"
    if events_jsonl.exists():
        _register_artifact(
            document,
            "events.jsonl",
            events_jsonl,
            "structured_events",
            producer_node="persistence",
        )
    for name, artifact_type, path in (
        ("inputs/manifest.json", "inputs_manifest", document.run_dir / "inputs" / "manifest.json"),
        ("outputs/manifest.json", "outputs_manifest", document.run_dir / "outputs" / "manifest.json"),
        ("metrics/summary.json", "metrics_summary", document.run_dir / "metrics" / "summary.json"),
        ("metrics/timings.csv", "metrics_timings", document.run_dir / "metrics" / "timings.csv"),
    ):
        if path.exists():
            _register_artifact(document, name, path, artifact_type, producer_node="persistence")


def _register_artifact(
    document: DocumentState,
    name: str,
    path: Path,
    artifact_type: str,
    *,
    producer_node: str,
) -> None:
    resolved_path = path.resolve() if path.exists() else path
    if any(record.name == name and record.path == resolved_path for record in document.artifact_manifest.records):
        return
    document.artifact_manifest.records.append(
        ArtifactRecord(
            artifact_id=f"artifact-{stable_id(document.document_id, name, resolved_path)}",
            name=name,
            path=resolved_path,
            artifact_type=artifact_type,
            producer_node=producer_node,
        )
    )


def _deduplicate_artifact_records(document: DocumentState) -> None:
    deduped: dict[tuple[str, Path], ArtifactRecord] = {}
    for record in document.artifact_manifest.records:
        key = (record.name, record.path)
        existing = deduped.get(key)
        if existing is None or (existing.producer_node == "persistence" and record.producer_node != "persistence"):
            deduped[key] = record
    document.artifact_manifest.records = list(deduped.values())


def _sync_review_decisions_template(document: DocumentState) -> None:
    path = document.run_dir / "review_decisions_template.json"
    unresolved_tasks = [task for task in document.review_tasks if not task.resolved]
    should_write = bool(unresolved_tasks) and document.finalization_state is FinalizationState.NEEDS_REVIEW

    if should_write:
        payload = build_review_decision_template(unresolved_tasks, source_path=document.run_dir / "review_tasks.json")
        write_json(path, payload)
        document.output_artifacts.review_decisions_template_json = path
        return

    if path.exists():
        path.unlink()
    document.output_artifacts.review_decisions_template_json = None
    document.artifact_manifest.records = [
        record for record in document.artifact_manifest.records if record.name != "review_decisions_template.json"
    ]


def _sync_ocr_recovery_template(document: DocumentState) -> None:
    path = document.run_dir / "ocr_recovery_template.json"
    unresolved_tasks = [
        task
        for task in document.review_tasks
        if not task.resolved and task.issue_code == "IMAGE_ONLY_PAGE_OCR_REQUIRED"
    ]
    should_write = bool(unresolved_tasks) and document.finalization_state is FinalizationState.NEEDS_REVIEW

    if should_write:
        payload = build_ocr_recovery_template(unresolved_tasks, source_path=document.run_dir / "review_tasks.json")
        write_json(path, payload)
        document.output_artifacts.ocr_recovery_template_json = path
        return

    if path.exists():
        path.unlink()
    document.output_artifacts.ocr_recovery_template_json = None
    document.artifact_manifest.records = [
        record for record in document.artifact_manifest.records if record.name != "ocr_recovery_template.json"
    ]


def _write_findings_jsonl(document: DocumentState) -> None:
    path = document.run_dir / "findings.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [model_to_jsonable(finding) for finding in document.findings]
    payload = "".join(f"{json.dumps(line, ensure_ascii=False)}\n" for line in lines)
    path.write_text(payload, encoding="utf-8")


def _write_validator_findings(document: DocumentState) -> None:
    path = document.run_dir / "validator_findings.json"
    checked_path = document.output_artifacts.tagged_draft_pdf
    validation_state = "completed" if checked_path and checked_path.exists() else "skipped"
    if path.exists() and _existing_validator_report_matches(path, len(document.validator_findings), checked_path, validation_state):
        return
    write_json(
        path,
        validator_report_payload(
            checked_path,
            document.validator_findings,
            skipped_reason="no_tagged_draft_available" if validation_state == "skipped" else None,
        ),
    )


def _existing_validator_report_matches(
    path: Path,
    expected_finding_count: int,
    expected_checked_path: Path | None,
    expected_validation_state: str,
) -> bool:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    expected_checked_path_str = (
        str(expected_checked_path) if expected_checked_path is not None and expected_checked_path.exists() else None
    )
    return (
        isinstance(payload, dict)
        and payload.get("validator") == "internal_tagged_draft"
        and payload.get("finding_count") == expected_finding_count
        and payload.get("checked_path") == expected_checked_path_str
        and payload.get("validation_state") == expected_validation_state
    )


def _finalization_status(document: DocumentState) -> dict[str, object]:
    report = document.writeback_report
    return {
        "document_status": document.document_status.value,
        "finalization_state": document.finalization_state.value,
        "blocker_ids": document.blocker_ids,
        "can_finalize": document.finalization_state.value == "finalized",
        "writeback_finalization_blocked": report.finalization_blocked if report is not None else None,
        "writeback_blocking_categories": report.blocking_categories if report is not None else [],
        "writeback_blocking_details": report.blocking_details if report is not None else {},
        "tagged_draft_pdf": str(document.output_artifacts.tagged_draft_pdf)
        if document.output_artifacts.tagged_draft_pdf
        else None,
        "accessible_output_pdf": str(document.output_artifacts.accessible_output_pdf)
        if document.output_artifacts.accessible_output_pdf
        else None,
        "accessible_output_html": str(document.output_artifacts.accessible_output_html)
        if document.output_artifacts.accessible_output_html
        else None,
    }


def _operator_guide(document: DocumentState) -> dict[str, object]:
    review_template_path = document.output_artifacts.review_decisions_template_json
    ocr_template_path = document.output_artifacts.ocr_recovery_template_json
    review_template_exists = review_template_path is not None and review_template_path.exists()
    ocr_template_exists = ocr_template_path is not None and ocr_template_path.exists()
    review_template_actionable = _template_count(review_template_path, "decision_count") > 0
    ocr_template_actionable = _template_count(ocr_template_path, "page_recovery_count") > 0
    blocker_counts = _blocker_counts_by_issue_code(document)
    next_actions: list[dict[str, object]] = []
    summary = "Run finalized. No manual next step is required."

    if document.finalization_state is not FinalizationState.FINALIZED:
        summary = "Run needs review. Follow the suggested next files in order."
        if review_template_exists and review_template_actionable:
            next_actions.append(
                {
                    "action": "fill_review_decisions",
                    "path": str(review_template_path),
                    "reason": "Resolvable review tasks are present.",
                }
            )
        if ocr_template_exists and ocr_template_actionable:
            next_actions.append(
                {
                    "action": "fill_ocr_recovery",
                    "path": str(ocr_template_path),
                    "reason": "Image-only pages still need OCR recovery text.",
                }
            )
        if not next_actions:
            next_actions.append(
                {
                    "action": "inspect_review_tasks",
                    "path": str(document.run_dir / "review_tasks.json"),
                    "reason": "No direct operator template is available for the remaining blockers.",
                }
            )

    primary_next_step = next_actions[0] if next_actions else None
    return {
        "document_status": document.document_status.value,
        "finalization_state": document.finalization_state.value,
        "summary": summary,
        "blocker_count": len(document.blocker_ids),
        "blocker_counts_by_issue_code": blocker_counts,
        "template_artifacts": {
            "review_decisions_template": str(review_template_path)
            if review_template_exists
            else None,
            "ocr_recovery_template": str(ocr_template_path)
            if ocr_template_exists
            else None,
        },
        "primary_next_step": primary_next_step,
        "next_actions": next_actions,
    }


def _template_count(path: Path | None, key: str) -> int:
    if path is None or not path.exists():
        return 0
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return 0
    value = payload.get(key)
    return value if isinstance(value, int) and value >= 0 else 0


def _run_log(document: DocumentState) -> dict[str, object]:
    return {
        "run_id": document.run_dir.name,
        "document_id": document.document_id,
        "source_path": str(document.source_path),
        "run_dir": str(document.run_dir),
        "document_status": document.document_status.value,
        "finalization_state": document.finalization_state.value,
        "terminal_state": _terminal_state(document),
        "counts": {
            "pages": document.page_count,
            "normalized_units": len(document.normalized_units),
            "findings": len(document.findings),
            "active_findings": sum(1 for finding in document.findings if finding.status.value == "active"),
            "review_tasks": len(document.review_tasks),
            "unresolved_review_tasks": sum(1 for task in document.review_tasks if not task.resolved),
            "review_decisions": len(document.review_decisions),
            "validator_findings": len(document.validator_findings),
            "unresolved_blockers": len(document.blocker_ids),
        },
        "artifact_names": sorted({record.name for record in document.artifact_manifest.records}),
        "output_artifacts": document.output_artifacts.model_dump(mode="json"),
        "workflow_trace": [entry.model_dump(mode="json") for entry in document.workflow_trace],
    }


def _terminal_state(document: DocumentState) -> str:
    if document.finalization_state.value in {"finalized", "needs_review", "write_blocked"}:
        return document.finalization_state.value
    if document.blocker_ids:
        return "needs_review"
    return "pending"


def _unit_counts(document: DocumentState) -> dict[str, int]:
    counts: dict[str, int] = {}
    for unit in document.normalized_units:
        counts[unit.unit_type] = counts.get(unit.unit_type, 0) + 1
    return counts


def _review_counts_by_severity(document: DocumentState) -> dict[str, int]:
    counts: dict[str, int] = {}
    for task in document.review_tasks:
        counts[task.severity] = counts.get(task.severity, 0) + 1
    return counts


def _blocker_counts_by_issue_code(document: DocumentState) -> dict[str, int]:
    counts: dict[str, int] = {}
    for task in document.review_tasks:
        if task.blocking and not task.resolved:
            counts[task.issue_code] = counts.get(task.issue_code, 0) + 1
    return counts


def _writeback_readiness_reason(document: DocumentState) -> str:
    if not document.blocker_ids:
        return "No unresolved blockers are present."
    counts = _blocker_counts_by_issue_code(document)
    if counts:
        parts = [f"{issue_code}: {count}" for issue_code, count in sorted(counts.items())]
        return "Blocked by unresolved review tasks: " + ", ".join(parts)
    return "Blocked by unresolved findings or validator issues."


def _structure_mapping_summary(document: DocumentState) -> dict[str, object]:
    plan = document.structure_mapping_plan
    if plan is None:
        return {"created": False}
    return {
        "created": True,
        "element_count": len(plan.elements),
        "artifact_unit_count": len(plan.artifact_unit_ids),
        "reading_order_unit_count": len(plan.reading_order_unit_ids),
        "unresolved_unit_count": len(plan.unresolved_unit_ids),
        "mcid_planned_count": sum(1 for element in plan.elements if element.mcid is not None),
        "parent_tree_planned_count": len(plan.parent_tree_entries),
        "content_streams_modified": plan.content_streams_modified,
        "document_properties_ready": (
            plan.document_properties.title_ready and plan.document_properties.primary_language_ready
        ),
        "structure_tree_ready": plan.structure_tree_ready,
        "writeback_prerequisites_ready": plan.writeback_prerequisites_ready,
        "marked_content_strategy": plan.marked_content_strategy,
        "parent_tree_strategy": plan.parent_tree_strategy,
    }


def _writeback_summary(document: DocumentState) -> dict[str, object]:
    report = document.writeback_report
    if report is None:
        return {"created": False}
    return {
        "created": True,
        "title_written": report.title_written,
        "primary_language_written": report.primary_language_written,
        "mark_info_written": report.mark_info_written,
        "struct_tree_root_written": report.struct_tree_root_written,
        "mcid_planned_count": report.mcid_planned_count,
        "parent_tree_planned_count": report.parent_tree_planned_count,
        "mcid_written_count": report.mcid_written_count,
        "parent_tree_written_count": report.parent_tree_written_count,
        "skipped_mcid_count": report.skipped_mcid_count,
        "content_streams_modified": report.content_streams_modified,
        "content_stream_marking_details": report.content_stream_marking_details,
        "planned_element_count": report.planned_element_count,
        "supported_element_count": report.supported_element_count,
        "written_structure_element_count": report.written_structure_element_count,
        "skipped_supported_element_count": report.skipped_supported_element_count,
        "unsupported_element_count": report.unsupported_element_count,
        "planned_role_counts": report.planned_role_counts,
        "supported_role_counts": report.supported_role_counts,
        "written_role_counts": report.written_role_counts,
        "skipped_role_counts": report.skipped_role_counts,
        "unsupported_role_counts": report.unsupported_role_counts,
        "blocking_categories": report.blocking_categories,
        "blocking_details": report.blocking_details,
        "finalization_blocked": report.finalization_blocked,
        "limitations": report.limitations,
    }
