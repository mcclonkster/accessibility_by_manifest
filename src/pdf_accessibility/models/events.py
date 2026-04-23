from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from pdf_accessibility.models.state import (
    ArtifactRecord,
    DocumentMetadataEvidence,
    DocumentStatus,
    FinalizationState,
    Finding,
    NormalizedUnit,
    PageGeometryEvidence,
    RegionStatus,
    RegionState,
    StructureMappingPlan,
    TextBlockEvidence,
    ImageEvidence,
    LinkEvidence,
    AnnotationEvidence,
    ReviewDecision,
    ReviewTask,
    ValidatorFinding,
    WorkflowTraceEntry,
    WritebackReport,
)


class EventType(str, Enum):
    DOCUMENT_PAGES = "document_pages"
    DOCUMENT_METADATA = "document_metadata"
    PAGE_EVIDENCE = "page_evidence"
    REGION_DISCOVERY = "region_discovery"
    NORMALIZED_STRUCTURE = "normalized_structure"
    STRUCTURE_MAPPING_PLAN = "structure_mapping_plan"
    WRITEBACK_REPORT = "writeback_report"
    FINDING = "finding"
    REGION_STATUS = "region_status"
    WORKFLOW_STATE = "workflow_state"
    FINALIZATION_STATE = "finalization_state"
    REVIEW_TASK = "review_task"
    REVIEW_DECISION = "review_decision"
    REVIEW_RESOLUTION = "review_resolution"
    VALIDATOR_FINDING = "validator_finding"
    ARTIFACT_REGISTRATION = "artifact_registration"
    WORKFLOW_TRACE = "workflow_trace"
    REOPEN = "reopen"
    APPROVAL = "approval"


class NodeEvent(BaseModel):
    event_id: str
    node_name: str
    event_type: EventType
    finding: Finding | None = None
    region_id: str | None = None
    region_status: RegionStatus | None = None
    document_status: DocumentStatus | None = None
    finalization_state: FinalizationState | None = None
    review_task: ReviewTask | None = None
    review_decision: ReviewDecision | None = None
    review_task_id: str | None = None
    validator_finding: ValidatorFinding | None = None
    workflow_trace: WorkflowTraceEntry | None = None
    artifact: ArtifactRecord | None = None
    payload: dict[str, Any] = Field(default_factory=dict)


def document_pages_event(event_id: str, node_name: str, page_count: int) -> NodeEvent:
    return NodeEvent(
        event_id=event_id,
        node_name=node_name,
        event_type=EventType.DOCUMENT_PAGES,
        payload={"page_count": page_count},
    )


def region_discovery_event(event_id: str, node_name: str, regions: list[RegionState]) -> NodeEvent:
    return NodeEvent(
        event_id=event_id,
        node_name=node_name,
        event_type=EventType.REGION_DISCOVERY,
        payload={"regions": regions},
    )


def document_metadata_event(
    event_id: str,
    node_name: str,
    metadata: DocumentMetadataEvidence,
) -> NodeEvent:
    return NodeEvent(
        event_id=event_id,
        node_name=node_name,
        event_type=EventType.DOCUMENT_METADATA,
        payload={"metadata": metadata},
    )


def page_evidence_event(
    event_id: str,
    node_name: str,
    page_number: int,
    *,
    geometry: PageGeometryEvidence | None = None,
    text_blocks: list[TextBlockEvidence] | None = None,
    images: list[ImageEvidence] | None = None,
    links: list[LinkEvidence] | None = None,
    annotations: list[AnnotationEvidence] | None = None,
    font_names: list[str] | None = None,
) -> NodeEvent:
    return NodeEvent(
        event_id=event_id,
        node_name=node_name,
        event_type=EventType.PAGE_EVIDENCE,
        payload={
            "page_number": page_number,
            "geometry": geometry,
            "text_blocks": text_blocks or [],
            "images": images or [],
            "links": links or [],
            "annotations": annotations or [],
            "font_names": font_names or [],
        },
    )


def normalized_structure_event(
    event_id: str,
    node_name: str,
    units: list[NormalizedUnit],
) -> NodeEvent:
    return NodeEvent(
        event_id=event_id,
        node_name=node_name,
        event_type=EventType.NORMALIZED_STRUCTURE,
        payload={"units": units},
    )


def structure_mapping_plan_event(
    event_id: str,
    node_name: str,
    plan: StructureMappingPlan,
) -> NodeEvent:
    return NodeEvent(
        event_id=event_id,
        node_name=node_name,
        event_type=EventType.STRUCTURE_MAPPING_PLAN,
        payload={"plan": plan},
    )


def writeback_report_event(event_id: str, node_name: str, report: WritebackReport) -> NodeEvent:
    return NodeEvent(
        event_id=event_id,
        node_name=node_name,
        event_type=EventType.WRITEBACK_REPORT,
        payload={"report": report},
    )


def finding_event(event_id: str, node_name: str, finding: Finding) -> NodeEvent:
    return NodeEvent(event_id=event_id, node_name=node_name, event_type=EventType.FINDING, finding=finding)


def workflow_state_event(event_id: str, node_name: str, status: DocumentStatus) -> NodeEvent:
    return NodeEvent(event_id=event_id, node_name=node_name, event_type=EventType.WORKFLOW_STATE, document_status=status)


def finalization_state_event(event_id: str, node_name: str, state: FinalizationState) -> NodeEvent:
    return NodeEvent(event_id=event_id, node_name=node_name, event_type=EventType.FINALIZATION_STATE, finalization_state=state)


def review_task_event(event_id: str, node_name: str, review_task: ReviewTask) -> NodeEvent:
    return NodeEvent(event_id=event_id, node_name=node_name, event_type=EventType.REVIEW_TASK, review_task=review_task)


def review_decision_event(event_id: str, node_name: str, review_decision: ReviewDecision) -> NodeEvent:
    return NodeEvent(
        event_id=event_id,
        node_name=node_name,
        event_type=EventType.REVIEW_DECISION,
        review_decision=review_decision,
    )


def artifact_registration_event(event_id: str, node_name: str, artifact: ArtifactRecord) -> NodeEvent:
    return NodeEvent(event_id=event_id, node_name=node_name, event_type=EventType.ARTIFACT_REGISTRATION, artifact=artifact)


def validator_finding_event(event_id: str, node_name: str, finding: ValidatorFinding) -> NodeEvent:
    return NodeEvent(event_id=event_id, node_name=node_name, event_type=EventType.VALIDATOR_FINDING, validator_finding=finding)


def workflow_trace_event(event_id: str, node_name: str, trace: WorkflowTraceEntry) -> NodeEvent:
    return NodeEvent(event_id=event_id, node_name=node_name, event_type=EventType.WORKFLOW_TRACE, workflow_trace=trace)


def region_status_event(event_id: str, node_name: str, region_id: str, status: RegionStatus) -> NodeEvent:
    return NodeEvent(
        event_id=event_id,
        node_name=node_name,
        event_type=EventType.REGION_STATUS,
        region_id=region_id,
        region_status=status,
    )


def artifact_record(
    *,
    artifact_id: str,
    name: str,
    path: Path,
    artifact_type: str,
    producer_node: str,
    metadata: dict[str, Any] | None = None,
) -> ArtifactRecord:
    return ArtifactRecord(
        artifact_id=artifact_id,
        name=name,
        path=path,
        artifact_type=artifact_type,
        producer_node=producer_node,
        metadata=metadata or {},
    )
