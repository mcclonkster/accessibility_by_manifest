from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Confidence(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class FindingClass(str, Enum):
    EVIDENCE = "evidence"
    PROPOSED_DECISION = "proposed_decision"
    CONTRADICTION = "contradiction"
    BLOCKING_ISSUE = "blocking_issue"
    APPROVAL = "approval"
    REOPEN_REQUEST = "reopen_request"
    VALIDATOR_RESULT = "validator_result"
    REVIEW_DECISION = "review_decision"


class FindingStatus(str, Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    SUPERSEDED = "superseded"


class DocumentStatus(str, Enum):
    PENDING = "pending"
    EVIDENCE_IN_PROGRESS = "evidence_in_progress"
    PLANNING_IN_PROGRESS = "planning_in_progress"
    DRAFT_READY = "draft_ready"
    DRAFT_WRITTEN = "draft_written"
    VALIDATED = "validated"
    NEEDS_REVIEW = "needs_review"
    REVIEW_APPLIED = "review_applied"
    WRITE_BLOCKED = "write_blocked"
    FINALIZED = "finalized"


class RegionStatus(str, Enum):
    UNSEEN = "unseen"
    EVIDENCE_COLLECTED = "evidence_collected"
    MEANING_INFERRED = "meaning_inferred"
    ACCESSIBILITY_REVIEWED = "accessibility_reviewed"
    STRUCTURE_PLANNED = "structure_planned"
    MAPPING_PLANNED = "mapping_planned"
    BEHAVIOR_CHECKED = "behavior_checked"
    COMMITTABLE = "committable"
    WRITTEN_TO_DRAFT = "written_to_draft"
    VALIDATED = "validated"
    ESCALATED = "escalated"
    COMPLETE = "complete"


class FinalizationState(str, Enum):
    PENDING = "pending"
    FINALIZED = "finalized"
    NEEDS_REVIEW = "needs_review"
    WRITE_BLOCKED = "write_blocked"


class BBox(BaseModel):
    model_config = ConfigDict(frozen=True)

    left: float
    top: float
    right: float
    bottom: float


class DocumentMetadataEvidence(BaseModel):
    title: str | None = None
    author: str | None = None
    subject: str | None = None
    keywords: str | None = None
    creator: str | None = None
    producer: str | None = None
    creation_date: str | None = None
    modification_date: str | None = None
    primary_language: str | None = None
    pdf_version: str | None = None
    encrypted: bool = False
    raw_metadata: dict[str, Any] = Field(default_factory=dict)
    provenance: dict[str, Any] = Field(default_factory=dict)


class PageGeometryEvidence(BaseModel):
    width: float
    height: float
    rotation: int = 0
    media_box: BBox | None = None
    crop_box: BBox | None = None


class TextSpanEvidence(BaseModel):
    text: str
    bbox: BBox
    font_name: str | None = None
    font_size: float | None = None
    flags: int | None = None
    color: int | None = None


class TextBlockEvidence(BaseModel):
    block_id: str
    page_number: int
    bbox: BBox
    text: str
    spans: list[TextSpanEvidence] = Field(default_factory=list)
    font_names: list[str] = Field(default_factory=list)
    font_sizes: list[float] = Field(default_factory=list)
    source_ref: str
    extractor: str = "pymupdf"


class ImageEvidence(BaseModel):
    image_id: str
    page_number: int
    bbox: BBox
    width: int | None = None
    height: int | None = None
    xref: int | None = None
    source_ref: str
    extractor: str = "pymupdf"


class LinkEvidence(BaseModel):
    link_id: str
    page_number: int
    bbox: BBox | None = None
    uri: str | None = None
    target: str | None = None
    source_ref: str
    extractor: str = "pymupdf"


class AnnotationEvidence(BaseModel):
    annotation_id: str
    page_number: int
    bbox: BBox | None = None
    annotation_type: str | None = None
    contents: str | None = None
    source_ref: str
    extractor: str = "pymupdf"


class NormalizedUnit(BaseModel):
    unit_id: str
    unit_type: str
    page_numbers: list[int]
    bbox: BBox | None = None
    text: str | None = None
    source_refs: list[str] = Field(default_factory=list)
    evidence_basis: list[str] = Field(default_factory=list)
    confidence: Confidence = Confidence.MEDIUM
    reading_order_index: int | None = None
    needs_review: bool = False


class DocumentPropertyPlan(BaseModel):
    title: str | None = None
    primary_language: str | None = None
    title_ready: bool = False
    primary_language_ready: bool = False
    evidence_basis: list[str] = Field(default_factory=list)


class StructureElementPlan(BaseModel):
    element_id: str
    unit_id: str
    pdf_structure_role: str | None = None
    include_in_structure_tree: bool = True
    artifact: bool = False
    page_number: int | None = None
    mcid: int | None = None
    marked_content_ref: str | None = None
    parent_tree_index: int | None = None
    content_stream_update_status: str = "not_planned"
    reading_order_index: int | None = None
    source_refs: list[str] = Field(default_factory=list)
    page_numbers: list[int] = Field(default_factory=list)
    review_required: bool = False
    unresolved_mapping: bool = False
    notes: list[str] = Field(default_factory=list)


class ParentTreeEntryPlan(BaseModel):
    parent_tree_index: int
    element_id: str
    unit_id: str
    page_number: int
    mcid: int
    status: str = "planned"


class StructureMappingPlan(BaseModel):
    document_properties: DocumentPropertyPlan = Field(default_factory=DocumentPropertyPlan)
    elements: list[StructureElementPlan] = Field(default_factory=list)
    parent_tree_entries: list[ParentTreeEntryPlan] = Field(default_factory=list)
    artifact_unit_ids: list[str] = Field(default_factory=list)
    reading_order_unit_ids: list[str] = Field(default_factory=list)
    unresolved_unit_ids: list[str] = Field(default_factory=list)
    marked_content_strategy: str = "planned_mcid_assignment_pending_content_stream_updates"
    parent_tree_strategy: str = "planned_parent_tree_entries_pending_pdf_write"
    content_streams_modified: bool = False
    structure_tree_ready: bool = False
    writeback_prerequisites_ready: bool = False


class WritebackReport(BaseModel):
    draft_path: Path
    title_written: bool = False
    primary_language_written: bool = False
    mark_info_written: bool = False
    struct_tree_root_written: bool = False
    mcid_planned_count: int = 0
    parent_tree_planned_count: int = 0
    mcid_written_count: int = 0
    parent_tree_written_count: int = 0
    skipped_mcid_count: int = 0
    content_streams_modified: bool = False
    content_stream_marking_details: list[dict[str, Any]] = Field(default_factory=list)
    planned_element_count: int = 0
    written_structure_element_count: int = 0
    unsupported_element_count: int = 0
    limitations: list[str] = Field(default_factory=list)
    finalization_blocked: bool = True


class Finding(BaseModel):
    model_config = ConfigDict(frozen=True)

    finding_id: str
    node_name: str
    finding_class: FindingClass
    target_ref: str
    message: str
    confidence: Confidence = Confidence.MEDIUM
    status: FindingStatus = FindingStatus.ACTIVE
    payload: dict[str, Any] = Field(default_factory=dict)


class ReviewTask(BaseModel):
    model_config = ConfigDict(frozen=True)

    task_id: str
    issue_code: str = "REVIEW_REQUIRED"
    severity: str = "warning"
    target_ref: str
    reason: str
    suggested_action: str | None = None
    confidence_context: dict[str, Any] = Field(default_factory=dict)
    blocking: bool = True
    resolved: bool = False
    source_finding_ids: list[str] = Field(default_factory=list)


class ReviewDecision(BaseModel):
    model_config = ConfigDict(frozen=True)

    decision_id: str
    target_review_task_id: str
    decision_type: str
    value: str | None = None
    note: str | None = None
    reviewer: str = "local"
    created_at: str | None = None
    resolved: bool = False
    blocked_reason: str | None = None


class ValidatorFinding(BaseModel):
    model_config = ConfigDict(frozen=True)

    finding_id: str
    target_ref: str
    message: str
    severity: str
    blocking: bool = True
    resolved: bool = False


class WorkflowTraceEntry(BaseModel):
    model_config = ConfigDict(frozen=True)

    node_name: str
    action: str
    reason: str | None = None
    before_status: DocumentStatus
    after_status: DocumentStatus
    before_finalization_state: FinalizationState
    after_finalization_state: FinalizationState
    event_count: int = 0


class ArtifactRecord(BaseModel):
    model_config = ConfigDict(frozen=True)

    artifact_id: str
    name: str
    path: Path
    artifact_type: str
    producer_node: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class OutputArtifacts(BaseModel):
    tagged_draft_pdf: Path | None = None
    writeback_report_json: Path | None = None
    validator_findings_json: Path | None = None
    review_tasks_json: Path | None = None
    finalization_status_json: Path | None = None
    accessible_output_pdf: Path | None = None


class RegionState(BaseModel):
    region_id: str
    page_number: int
    bbox: BBox | None = None
    status: RegionStatus = RegionStatus.UNSEEN
    current_role: str | None = None
    confidence: Confidence = Confidence.MEDIUM
    source_refs: list[str] = Field(default_factory=list)
    evidence_basis: list[str] = Field(default_factory=list)
    blocker_ids: list[str] = Field(default_factory=list)


class PageState(BaseModel):
    page_number: int
    image_path: Path | None = None
    page_classification: str | None = None
    geometry: PageGeometryEvidence | None = None
    text_blocks: list[TextBlockEvidence] = Field(default_factory=list)
    images: list[ImageEvidence] = Field(default_factory=list)
    links: list[LinkEvidence] = Field(default_factory=list)
    annotations: list[AnnotationEvidence] = Field(default_factory=list)
    font_names: list[str] = Field(default_factory=list)
    regions: list[RegionState] = Field(default_factory=list)


class ArtifactManifest(BaseModel):
    records: list[ArtifactRecord] = Field(default_factory=list)


class DocumentState(BaseModel):
    document_id: str
    source_path: Path
    run_dir: Path
    document_status: DocumentStatus = DocumentStatus.PENDING
    finalization_state: FinalizationState = FinalizationState.PENDING
    page_count: int = 0
    metadata: DocumentMetadataEvidence | None = None
    pages: list[PageState] = Field(default_factory=list)
    normalized_units: list[NormalizedUnit] = Field(default_factory=list)
    structure_mapping_plan: StructureMappingPlan | None = None
    writeback_report: WritebackReport | None = None
    findings: list[Finding] = Field(default_factory=list)
    review_tasks: list[ReviewTask] = Field(default_factory=list)
    review_decisions: list[ReviewDecision] = Field(default_factory=list)
    validator_findings: list[ValidatorFinding] = Field(default_factory=list)
    workflow_trace: list[WorkflowTraceEntry] = Field(default_factory=list)
    artifact_manifest: ArtifactManifest = Field(default_factory=ArtifactManifest)
    output_artifacts: OutputArtifacts = Field(default_factory=OutputArtifacts)
    blocker_ids: list[str] = Field(default_factory=list)
