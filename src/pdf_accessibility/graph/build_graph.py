from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timezone
import time
from typing import TypedDict

from accessibility_by_manifest.util.logging import get_logger
from pdf_accessibility.models.events import NodeEvent, workflow_trace_event
from pdf_accessibility.models.state import DocumentState, DocumentStatus, FinalizationState
from pdf_accessibility.nodes import (
    accessibility_review,
    apply_review_decisions,
    approval_gate,
    artifact_check,
    behavior_check,
    caption_association,
    document_consistency,
    finalize_accessible_output,
    ingest_pdf,
    native_pdf_analysis,
    ocr_layout_analysis,
    region_proposal,
    render_pages,
    structure_mapping_plan,
    tagging_plan,
    validator_check,
    vision_analysis,
    write_accessible_html,
    write_tagged_draft,
    human_review,
)
from pdf_accessibility.persistence.artifacts import write_run_snapshot
from pdf_accessibility.reducers.apply_events import apply_events
from pdf_accessibility.transition_guards.finalization import can_finalize, can_write_draft
from pdf_accessibility.utils.ids import event_id


class GraphState(TypedDict):
    document: DocumentState


LOGGER = get_logger("pdf_accessibility.workflow")


def langgraph_available() -> bool:
    try:
        import langgraph  # noqa: F401
    except ImportError:
        return False
    return True


class WorkflowGraph:
    def __init__(self) -> None:
        self.setup_nodes = (ingest_pdf, render_pages)
        self.evidence_nodes = (vision_analysis, ocr_layout_analysis, native_pdf_analysis, region_proposal)
        self.planning_nodes = (
            accessibility_review,
            apply_review_decisions,
            artifact_check,
            caption_association,
            tagging_plan,
            document_consistency,
            structure_mapping_plan,
            behavior_check,
            approval_gate,
        )

    def invoke(self, state: GraphState) -> GraphState:
        document = state["document"]
        for node in self.setup_nodes + self.evidence_nodes + self.planning_nodes:
            document = self._run_node(document, node.NODE_NAME, node.run)

        if can_write_draft(document):
            document = self._run_node(document, write_tagged_draft.NODE_NAME, write_tagged_draft.run)
        else:
            document = self._skip_node(document, write_tagged_draft.NODE_NAME, _write_draft_skip_reason(document))

        if _can_validate(document):
            document = self._run_node(document, validator_check.NODE_NAME, validator_check.run)
        else:
            document = self._skip_node(document, validator_check.NODE_NAME, _validator_skip_reason(document))

        if _needs_human_review(document):
            document = self._run_node(document, human_review.NODE_NAME, human_review.run)
            document = self._run_node(document, apply_review_decisions.NODE_NAME, apply_review_decisions.run)
            if not document.blocker_ids:
                for node in (structure_mapping_plan, behavior_check, approval_gate):
                    document = self._run_node(document, node.NODE_NAME, node.run)
        else:
            document = self._skip_node(document, human_review.NODE_NAME, "No unresolved blockers or review state present.")
            document = self._skip_node(document, apply_review_decisions.NODE_NAME, "No human review pass ran in this route.")

        if can_finalize(document) or document.finalization_state is FinalizationState.NEEDS_REVIEW:
            document = self._run_node(document, finalize_accessible_output.NODE_NAME, finalize_accessible_output.run)
        else:
            document = self._skip_node(document, finalize_accessible_output.NODE_NAME, _finalization_skip_reason(document))
        if document.finalization_state is FinalizationState.FINALIZED:
            document = self._run_node(document, write_accessible_html.NODE_NAME, write_accessible_html.run)
        else:
            document = self._skip_node(document, write_accessible_html.NODE_NAME, _html_skip_reason(document))
        return {"document": document}

    @staticmethod
    def _run_node(
        document: DocumentState,
        node_name: str,
        run: Callable[[DocumentState], list[NodeEvent]],
    ) -> DocumentState:
        before_status = document.document_status
        before_finalization_state = document.finalization_state
        before_blockers = len(document.blocker_ids)
        before_findings = len(document.findings)
        before_review_tasks = len(document.review_tasks)
        started_at = _now_iso()
        started_monotonic = time.monotonic()
        LOGGER.info("Node started: %s", node_name, extra={"event_action": "node_started", "node_name": node_name})
        LOGGER.debug(
            "Node state before: node=%s status=%s finalization=%s blockers=%s findings=%s review_tasks=%s",
            node_name,
            before_status.value,
            before_finalization_state.value,
            before_blockers,
            before_findings,
            before_review_tasks,
            extra={
                "event_action": "node_state_before",
                "node_name": node_name,
                "document_status_before": before_status.value,
                "finalization_state_before": before_finalization_state.value,
                "blocker_count_before": before_blockers,
                "findings_count_before": before_findings,
                "review_task_count_before": before_review_tasks,
            },
        )
        events = run(document)
        document = apply_events(document, events)
        LOGGER.info(
            "Node completed: %s events=%s status=%s finalization=%s",
            node_name,
            len(events),
            document.document_status.value,
            document.finalization_state.value,
            extra={
                "event_action": "node_completed",
                "node_name": node_name,
                "event_count": len(events),
                "document_status_after": document.document_status.value,
                "finalization_state_after": document.finalization_state.value,
                "duration_ms": _duration_ms(started_monotonic),
            },
        )
        LOGGER.debug(
            "Node state after: node=%s blockers_before=%s blockers_after=%s findings_before=%s findings_after=%s "
            "review_tasks_before=%s review_tasks_after=%s",
            node_name,
            before_blockers,
            len(document.blocker_ids),
            before_findings,
            len(document.findings),
            before_review_tasks,
            len(document.review_tasks),
            extra={
                "event_action": "node_state_after",
                "node_name": node_name,
                "blocker_count_before": before_blockers,
                "blocker_count_after": len(document.blocker_ids),
                "findings_count_before": before_findings,
                "findings_count_after": len(document.findings),
                "review_task_count_before": before_review_tasks,
                "review_task_count_after": len(document.review_tasks),
            },
        )
        document = _record_trace(
            document,
            node_name=node_name,
            action="ran",
            started_at=started_at,
            ended_at=_now_iso(),
            duration_ms=_duration_ms(started_monotonic),
            reason=None,
            before_status=before_status,
            before_finalization_state=before_finalization_state,
            event_count=len(events),
        )
        write_run_snapshot(document)
        return document

    @staticmethod
    def _skip_node(document: DocumentState, node_name: str, reason: str) -> DocumentState:
        started_at = _now_iso()
        LOGGER.info(
            "Node skipped: %s reason=%s",
            node_name,
            reason,
            extra={
                "event_action": "node_skipped",
                "node_name": node_name,
                "skip_reason": reason,
                "document_status_after": document.document_status.value,
                "finalization_state_after": document.finalization_state.value,
            },
        )
        LOGGER.debug(
            "Node skip state: node=%s status=%s finalization=%s blockers=%s reason=%s",
            node_name,
            document.document_status.value,
            document.finalization_state.value,
            len(document.blocker_ids),
            reason,
            extra={
                "event_action": "node_skip_state",
                "node_name": node_name,
                "document_status_after": document.document_status.value,
                "finalization_state_after": document.finalization_state.value,
                "blocker_count_after": len(document.blocker_ids),
                "skip_reason": reason,
            },
        )
        document = _record_trace(
            document,
            node_name=node_name,
            action="skipped",
            started_at=started_at,
            ended_at=_now_iso(),
            duration_ms=0,
            reason=reason,
            before_status=document.document_status,
            before_finalization_state=document.finalization_state,
            event_count=0,
        )
        write_run_snapshot(document)
        return document


class LangGraphWorkflow:
    def __init__(self) -> None:
        from langgraph.graph import END, START, StateGraph

        graph = StateGraph(GraphState)
        graph.add_node("workflow_orchestrator", self._run_workflow)
        graph.add_edge(START, "workflow_orchestrator")
        graph.add_edge("workflow_orchestrator", END)
        self._compiled = graph.compile()

    @staticmethod
    def _run_workflow(state: GraphState) -> GraphState:
        return WorkflowGraph().invoke(state)

    def invoke(self, state: GraphState) -> GraphState:
        return self._compiled.invoke(state)


def build_workflow() -> WorkflowGraph | LangGraphWorkflow:
    if langgraph_available():
        return LangGraphWorkflow()
    return WorkflowGraph()


def _record_trace(
    document: DocumentState,
    *,
    node_name: str,
    action: str,
    started_at: str,
    ended_at: str,
    duration_ms: int,
    reason: str | None,
    before_status: DocumentStatus,
    before_finalization_state: FinalizationState,
    event_count: int,
) -> DocumentState:
    from pdf_accessibility.models.state import WorkflowTraceEntry

    return apply_events(
        document,
        [
            workflow_trace_event(
                event_id("workflow_orchestrator", node_name, action, len(document.workflow_trace)),
                "workflow_orchestrator",
                WorkflowTraceEntry(
                    node_name=node_name,
                    action=action,
                    started_at=started_at,
                    ended_at=ended_at,
                    duration_ms=duration_ms,
                    reason=reason,
                    before_status=before_status,
                    after_status=document.document_status,
                    before_finalization_state=before_finalization_state,
                    after_finalization_state=document.finalization_state,
                    event_count=event_count,
                ),
            )
        ],
    )


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _duration_ms(started_monotonic: float) -> int:
    return int((time.monotonic() - started_monotonic) * 1000)


def _can_validate(document: DocumentState) -> bool:
    return document.document_status is DocumentStatus.DRAFT_WRITTEN and document.output_artifacts.tagged_draft_pdf is not None


def _needs_human_review(document: DocumentState) -> bool:
    return bool(document.blocker_ids) or document.finalization_state is FinalizationState.NEEDS_REVIEW


def _write_draft_skip_reason(document: DocumentState) -> str:
    if document.blocker_ids:
        return "Draft write blocked by unresolved blockers."
    if document.finalization_state is FinalizationState.WRITE_BLOCKED:
        return "Draft write blocked by write-blocked finalization state."
    if document.document_status is not DocumentStatus.DRAFT_READY:
        return f"Draft write requires document_status=draft_ready; current status is {document.document_status.value}."
    return "Draft write requires at least one committable region."


def _validator_skip_reason(document: DocumentState) -> str:
    if document.document_status is not DocumentStatus.DRAFT_WRITTEN:
        return f"Validator requires document_status=draft_written; current status is {document.document_status.value}."
    return "Validator requires tagged_draft.pdf to be registered."


def _finalization_skip_reason(document: DocumentState) -> str:
    if document.output_artifacts.tagged_draft_pdf is None:
        return "Finalization requires a tagged draft PDF."
    if document.blocker_ids:
        return "Finalization blocked by unresolved blockers."
    return f"Finalization requires validated or review_applied status; current status is {document.document_status.value}."


def _html_skip_reason(document: DocumentState) -> str:
    return f"HTML output requires finalized PDF workflow state; current finalization_state is {document.finalization_state.value}."
