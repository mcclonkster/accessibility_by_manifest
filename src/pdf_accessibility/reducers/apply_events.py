from __future__ import annotations

from collections.abc import Iterable

from pdf_accessibility.models.events import EventType, NodeEvent
from pdf_accessibility.models.state import (
    DocumentState,
    DocumentStatus,
    DocumentMetadataEvidence,
    FindingClass,
    FindingStatus,
    FinalizationState,
    PageState,
    ReviewDecision,
)
from pdf_accessibility.transition_guards.states import (
    can_transition_finalization,
    can_transition_region,
    can_transition_workflow,
)


EVENT_ORDER = {
    EventType.DOCUMENT_PAGES: 0,
    EventType.DOCUMENT_METADATA: 0,
    EventType.PAGE_EVIDENCE: 0,
    EventType.REGION_DISCOVERY: 0,
    EventType.NORMALIZED_STRUCTURE: 0,
    EventType.STRUCTURE_MAPPING_PLAN: 0,
    EventType.WRITEBACK_REPORT: 0,
    EventType.FINDING: 1,
    EventType.VALIDATOR_FINDING: 2,
    EventType.WORKFLOW_TRACE: 3,
    EventType.REVIEW_TASK: 4,
    EventType.REVIEW_DECISION: 5,
    EventType.REVIEW_RESOLUTION: 6,
    EventType.ARTIFACT_REGISTRATION: 7,
    EventType.REOPEN: 8,
    EventType.APPROVAL: 9,
    EventType.REGION_STATUS: 10,
    EventType.WORKFLOW_STATE: 11,
    EventType.FINALIZATION_STATE: 12,
}


def apply_events(document: DocumentState, events: Iterable[NodeEvent]) -> DocumentState:
    updated = document.model_copy(deep=True)
    for event in sorted(events, key=lambda item: EVENT_ORDER[item.event_type]):
        if event.event_type is EventType.DOCUMENT_PAGES:
            updated = _apply_document_pages(updated, event)
        elif event.event_type is EventType.DOCUMENT_METADATA:
            updated = _apply_document_metadata(updated, event)
        elif event.event_type is EventType.PAGE_EVIDENCE:
            updated = _apply_page_evidence(updated, event)
        elif event.event_type is EventType.REGION_DISCOVERY:
            updated = _apply_region_discovery(updated, event)
        elif event.event_type is EventType.NORMALIZED_STRUCTURE:
            updated = _apply_normalized_structure(updated, event)
        elif event.event_type is EventType.STRUCTURE_MAPPING_PLAN:
            updated = _apply_structure_mapping_plan(updated, event)
        elif event.event_type is EventType.WRITEBACK_REPORT:
            updated = _apply_writeback_report(updated, event)
        elif event.event_type is EventType.FINDING and event.finding is not None:
            updated.findings.append(event.finding)
        elif event.event_type is EventType.VALIDATOR_FINDING and event.validator_finding is not None:
            updated.validator_findings.append(event.validator_finding)
        elif event.event_type is EventType.WORKFLOW_TRACE and event.workflow_trace is not None:
            updated.workflow_trace.append(event.workflow_trace)
        elif event.event_type is EventType.REVIEW_TASK and event.review_task is not None:
            updated.review_tasks.append(event.review_task)
        elif event.event_type is EventType.REVIEW_DECISION and event.review_decision is not None:
            updated = _apply_review_decision(updated, event.review_decision)
        elif event.event_type is EventType.REVIEW_RESOLUTION and event.review_task_id is not None:
            updated = _apply_review_resolution(updated, event.review_task_id)
        elif event.event_type is EventType.ARTIFACT_REGISTRATION and event.artifact is not None:
            updated = _apply_artifact_registration(updated, event)
        elif event.event_type is EventType.REOPEN:
            updated = _apply_reopen(updated, event)
        elif event.event_type is EventType.APPROVAL:
            updated = _apply_approval(updated, event)
        elif event.event_type is EventType.REGION_STATUS:
            updated = _apply_region_status(updated, event)
        elif event.event_type is EventType.WORKFLOW_STATE and event.document_status is not None:
            updated = _apply_workflow_state(updated, event.document_status)
        elif event.event_type is EventType.FINALIZATION_STATE and event.finalization_state is not None:
            updated = _apply_finalization_state(updated, event.finalization_state)
    return recompute_blockers(updated)


def recompute_blockers(document: DocumentState) -> DocumentState:
    blocker_ids: list[str] = []
    for finding in document.findings:
        if finding.finding_class is FindingClass.BLOCKING_ISSUE and finding.status is FindingStatus.ACTIVE:
            blocker_ids.append(finding.finding_id)
    for review_task in document.review_tasks:
        if review_task.blocking and not review_task.resolved:
            blocker_ids.append(review_task.task_id)
    for validator_finding in document.validator_findings:
        if validator_finding.blocking and not validator_finding.resolved:
            blocker_ids.append(validator_finding.finding_id)
    document.blocker_ids = sorted(set(blocker_ids))
    return document


def _apply_document_pages(document: DocumentState, event: NodeEvent) -> DocumentState:
    page_count = int(event.payload.get("page_count", 0))
    document.page_count = page_count
    existing = {page.page_number: page for page in document.pages}
    document.pages = [existing.get(number, PageState(page_number=number)) for number in range(1, page_count + 1)]
    return document


def _apply_document_metadata(document: DocumentState, event: NodeEvent) -> DocumentState:
    metadata = event.payload.get("metadata")
    if metadata is not None:
        document.metadata = metadata
    return document


def _apply_page_evidence(document: DocumentState, event: NodeEvent) -> DocumentState:
    page_number = int(event.payload["page_number"])
    page = _get_or_create_page(document, page_number)
    if event.payload.get("geometry") is not None:
        page.geometry = event.payload["geometry"]
    page.text_blocks = event.payload.get("text_blocks", [])
    page.images = event.payload.get("images", [])
    page.links = event.payload.get("links", [])
    page.annotations = event.payload.get("annotations", [])
    page.font_names = sorted(set(event.payload.get("font_names", [])))
    return document


def _apply_region_discovery(document: DocumentState, event: NodeEvent) -> DocumentState:
    regions = event.payload.get("regions", [])
    by_page = {page.page_number: page for page in document.pages}
    for region in regions:
        page = by_page.get(region.page_number)
        if page is None:
            page = PageState(page_number=region.page_number)
            document.pages.append(page)
            by_page[region.page_number] = page
        if not any(existing.region_id == region.region_id for existing in page.regions):
            page.regions.append(region)
    document.pages.sort(key=lambda page: page.page_number)
    return document


def _apply_normalized_structure(document: DocumentState, event: NodeEvent) -> DocumentState:
    incoming = event.payload.get("units", [])
    existing = {unit.unit_id: unit for unit in document.normalized_units}
    for unit in incoming:
        existing[unit.unit_id] = unit
    document.normalized_units = sorted(
        existing.values(),
        key=lambda unit: (unit.reading_order_index is None, unit.reading_order_index or 0, unit.unit_id),
    )
    return document


def _apply_structure_mapping_plan(document: DocumentState, event: NodeEvent) -> DocumentState:
    plan = event.payload.get("plan")
    if plan is not None:
        document.structure_mapping_plan = plan
    return document


def _apply_writeback_report(document: DocumentState, event: NodeEvent) -> DocumentState:
    report = event.payload.get("report")
    if report is not None:
        document.writeback_report = report
    return document


def _get_or_create_page(document: DocumentState, page_number: int) -> PageState:
    for page in document.pages:
        if page.page_number == page_number:
            return page
    page = PageState(page_number=page_number)
    document.pages.append(page)
    document.pages.sort(key=lambda item: item.page_number)
    return page


def _apply_review_resolution(document: DocumentState, review_task_id: str) -> DocumentState:
    document.review_tasks = [
        task.model_copy(update={"resolved": True}) if task.task_id == review_task_id else task
        for task in document.review_tasks
    ]
    return document


NON_RESOLVABLE_ISSUE_CODES = {
    "TAGGED_DRAFT_NOT_FINAL",
    "STRUCTURE_MAPPING_PLAN_MISSING",
}


def _apply_review_decision(document: DocumentState, decision: ReviewDecision) -> DocumentState:
    task = next((task for task in document.review_tasks if task.task_id == decision.target_review_task_id), None)
    if task is None:
        document.review_decisions.append(decision.model_copy(update={"blocked_reason": "target review task not found"}))
        return document
    if task.issue_code in NON_RESOLVABLE_ISSUE_CODES:
        document.review_decisions.append(
            decision.model_copy(update={"blocked_reason": f"{task.issue_code} cannot be resolved by review decision"})
        )
        return document
    if decision.decision_type == "set_document_title" and task.issue_code == "DOCUMENT_TITLE_MISSING":
        value = (decision.value or "").strip()
        if not value:
            document.review_decisions.append(decision.model_copy(update={"blocked_reason": "title value is empty"}))
            return document
        document.metadata = _metadata_with_update(document.metadata, title=value)
        _resolve_task(document, task.task_id)
        document.review_decisions.append(decision.model_copy(update={"resolved": True}))
        return document
    if decision.decision_type == "set_primary_language" and task.issue_code == "DOCUMENT_LANGUAGE_MISSING":
        value = (decision.value or "").strip()
        if not value:
            document.review_decisions.append(decision.model_copy(update={"blocked_reason": "primary language value is empty"}))
            return document
        document.metadata = _metadata_with_update(document.metadata, primary_language=value)
        _resolve_task(document, task.task_id)
        document.review_decisions.append(decision.model_copy(update={"resolved": True}))
        return document
    if decision.decision_type in {"mark_figure_decorative", "provide_alt_text"} and task.issue_code in {
        "FIGURE_ALT_TEXT_REQUIRED",
        "FIGURE_ALT_TEXT_SPOT_CHECK",
    }:
        _resolve_task(document, task.task_id)
        document.review_decisions.append(decision.model_copy(update={"resolved": True}))
        return document
    if decision.decision_type == "defer_complex_table" and task.issue_code in {
        "TABLE_HEADERS_UNCERTAIN",
        "TABLE_STRUCTURE_SPOT_CHECK",
    }:
        document.review_decisions.append(
            decision.model_copy(update={"blocked_reason": "table deferral recorded but blocking table review remains unresolved"})
        )
        return document
    if decision.decision_type == "resolve_review_task":
        _resolve_task(document, task.task_id)
        document.review_decisions.append(decision.model_copy(update={"resolved": True}))
        return document
    document.review_decisions.append(decision.model_copy(update={"blocked_reason": "decision type does not match target review task"}))
    return document


def _resolve_task(document: DocumentState, task_id: str) -> None:
    document.review_tasks = [
        task.model_copy(update={"resolved": True}) if task.task_id == task_id else task
        for task in document.review_tasks
    ]


def _metadata_with_update(
    metadata: DocumentMetadataEvidence | None,
    *,
    title: str | None = None,
    primary_language: str | None = None,
) -> DocumentMetadataEvidence:
    base = metadata or DocumentMetadataEvidence()
    provenance = dict(base.provenance)
    provenance["review_decision"] = True
    return base.model_copy(
        update={
            "title": title if title is not None else base.title,
            "primary_language": primary_language if primary_language is not None else base.primary_language,
            "provenance": provenance,
        }
    )


def _apply_artifact_registration(document: DocumentState, event: NodeEvent) -> DocumentState:
    artifact = event.artifact
    if artifact is None:
        return document
    document.artifact_manifest.records.append(artifact)
    if artifact.name == "tagged_draft.pdf":
        document.output_artifacts.tagged_draft_pdf = artifact.path
    elif artifact.name == "writeback_report.json":
        document.output_artifacts.writeback_report_json = artifact.path
    elif artifact.name == "validator_findings.json":
        document.output_artifacts.validator_findings_json = artifact.path
    elif artifact.name == "review_tasks.json":
        document.output_artifacts.review_tasks_json = artifact.path
    elif artifact.name == "finalization_status.json":
        document.output_artifacts.finalization_status_json = artifact.path
    elif artifact.name == "accessible_output.pdf":
        document.output_artifacts.accessible_output_pdf = artifact.path
    return document


def _apply_reopen(document: DocumentState, event: NodeEvent) -> DocumentState:
    target_status = event.payload.get("document_status")
    if target_status:
        return _apply_workflow_state(document, DocumentStatus(target_status))
    return document


def _apply_approval(document: DocumentState, event: NodeEvent) -> DocumentState:
    target_ref = event.payload.get("target_ref", "document")
    document.findings.append(
        event.payload["finding"] if "finding" in event.payload else event.finding
    ) if event.finding else None
    if target_ref == "document" and document.document_status is DocumentStatus.PLANNING_IN_PROGRESS:
        return _apply_workflow_state(document, DocumentStatus.DRAFT_READY)
    return document


def _apply_region_status(document: DocumentState, event: NodeEvent) -> DocumentState:
    if event.region_id is None or event.region_status is None:
        return document
    for page in document.pages:
        for index, region in enumerate(page.regions):
            if region.region_id == event.region_id and can_transition_region(region.status, event.region_status):
                page.regions[index] = region.model_copy(update={"status": event.region_status})
                return document
    return document


def _apply_workflow_state(document: DocumentState, status: DocumentStatus) -> DocumentState:
    if can_transition_workflow(document.document_status, status):
        document.document_status = status
    return document


def _apply_finalization_state(document: DocumentState, state: FinalizationState) -> DocumentState:
    if can_transition_finalization(document.finalization_state, state):
        document.finalization_state = state
    return document
