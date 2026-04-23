from __future__ import annotations

import json
from pathlib import Path

from pdf_accessibility.models.state import ArtifactRecord, DocumentState
from pdf_accessibility.services.internal_validator import validator_report_payload
from pdf_accessibility.utils.ids import stable_id
from pdf_accessibility.utils.json import model_to_jsonable, write_json


SNAPSHOT_ARTIFACTS: tuple[tuple[str, str], ...] = (
    ("input.pdf", "source_pdf"),
    ("document_state.json", "state_snapshot"),
    ("findings.jsonl", "findings_log"),
    ("review_tasks.json", "review_tasks"),
    ("review_decisions.json", "review_decisions"),
    ("normalized_structure.json", "normalized_structure"),
    ("structure_mapping_plan.json", "structure_mapping_plan"),
    ("writeback_report.json", "writeback_report"),
    ("tagging_plan.json", "tagging_plan"),
    ("validator_findings.json", "validator_findings"),
    ("finalization_status.json", "finalization_status"),
    ("run_log.json", "run_log"),
    ("artifact_manifest.json", "artifact_manifest"),
)


def write_run_snapshot(document: DocumentState) -> None:
    _ensure_required_artifact_records(document)

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
    write_json(document.run_dir / "run_log.json", _run_log(document))
    write_json(document.run_dir / "artifact_manifest.json", document.artifact_manifest)


def artifact_path(document: DocumentState, name: str) -> Path:
    return document.run_dir / name


def _ensure_required_artifact_records(document: DocumentState) -> None:
    for name, artifact_type in SNAPSHOT_ARTIFACTS:
        path = document.source_path if name == "input.pdf" else document.run_dir / name
        _register_artifact(document, name, path, artifact_type, producer_node="persistence")

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

    document.output_artifacts.review_tasks_json = document.run_dir / "review_tasks.json"
    document.output_artifacts.writeback_report_json = document.run_dir / "writeback_report.json"
    document.output_artifacts.validator_findings_json = document.run_dir / "validator_findings.json"
    document.output_artifacts.finalization_status_json = document.run_dir / "finalization_status.json"
    _deduplicate_artifact_records(document)


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


def _write_findings_jsonl(document: DocumentState) -> None:
    path = document.run_dir / "findings.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [model_to_jsonable(finding) for finding in document.findings]
    payload = "".join(f"{json.dumps(line, ensure_ascii=False)}\n" for line in lines)
    path.write_text(payload, encoding="utf-8")


def _write_validator_findings(document: DocumentState) -> None:
    path = document.run_dir / "validator_findings.json"
    if path.exists() and _existing_validator_report_matches(path, len(document.validator_findings)):
        return
    checked_path = document.output_artifacts.tagged_draft_pdf or document.run_dir / "tagged_draft.pdf"
    write_json(path, validator_report_payload(checked_path, document.validator_findings))


def _existing_validator_report_matches(path: Path, expected_finding_count: int) -> bool:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return (
        isinstance(payload, dict)
        and payload.get("validator") == "internal_tagged_draft"
        and payload.get("finding_count") == expected_finding_count
    )


def _finalization_status(document: DocumentState) -> dict[str, object]:
    return {
        "document_status": document.document_status.value,
        "finalization_state": document.finalization_state.value,
        "blocker_ids": document.blocker_ids,
        "can_finalize": document.finalization_state.value == "finalized",
        "tagged_draft_pdf": str(document.output_artifacts.tagged_draft_pdf)
        if document.output_artifacts.tagged_draft_pdf
        else None,
        "accessible_output_pdf": str(document.output_artifacts.accessible_output_pdf)
        if document.output_artifacts.accessible_output_pdf
        else None,
    }


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
        "written_structure_element_count": report.written_structure_element_count,
        "unsupported_element_count": report.unsupported_element_count,
        "finalization_blocked": report.finalization_blocked,
        "limitations": report.limitations,
    }
