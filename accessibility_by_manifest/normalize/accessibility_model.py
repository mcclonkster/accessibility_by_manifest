from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


MODEL_VERSION = "0.1"


class NormalizedBBox(BaseModel):
    model_config = ConfigDict(frozen=True)

    left: float
    top: float
    right: float
    bottom: float


class NormalizedSourcePackage(BaseModel):
    input_file_name: str
    input_file_path: str
    sha256: str | None = None
    source_id: str | None = None
    format_family: str | None = None

    @field_validator("input_file_name", "input_file_path")
    @classmethod
    def _non_empty_required_strings(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("must not be empty")
        return value


class NormalizedProvenance(BaseModel):
    source_refs: list[str] = Field(default_factory=list)
    evidence_basis: list[str] = Field(default_factory=list)
    derived_by: list[str] = Field(default_factory=list)
    review_overrides: list[str] = Field(default_factory=list)
    source_format: str | None = None
    extractor_names: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class NormalizedDocumentMetadata(BaseModel):
    document_id: str
    title: str | None = None
    primary_language: str | None = None
    author: str | None = None
    subject: str | None = None
    keywords: list[str] = Field(default_factory=list)
    created_at: str | None = None
    modified_at: str | None = None
    metadata_provenance: NormalizedProvenance = Field(default_factory=NormalizedProvenance)

    @field_validator("document_id")
    @classmethod
    def _non_empty_document_id(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("document_id must not be empty")
        return value


class NormalizedProjectionHints(BaseModel):
    projection_status: Literal["planned", "preserve", "omitted", "manual_review_required"] = "planned"
    preferred_output_roles: dict[str, str] = Field(default_factory=dict)
    html_tag_hint: str | None = None
    pdf_structure_role_hint: str | None = None
    docx_style_hint: str | None = None
    artifact_candidate: bool = False
    decorative_candidate: bool = False
    metadata: dict[str, Any] = Field(default_factory=dict)


class NormalizedReviewEntry(BaseModel):
    task_id: str
    issue_code: str
    severity: str
    scope: str
    target_ref: str
    reason: str
    source_refs: list[str] = Field(default_factory=list)
    blocking: bool = True
    suggested_action: str | None = None
    resolved: bool = False
    confidence_context: dict[str, Any] = Field(default_factory=dict)

    @field_validator("task_id", "issue_code", "severity", "scope", "target_ref", "reason")
    @classmethod
    def _non_empty_review_strings(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("must not be empty")
        return value

    @field_validator("source_refs")
    @classmethod
    def _review_entries_need_provenance(cls, value: list[str]) -> list[str]:
        refs = [item.strip() for item in value if item and item.strip()]
        if not refs:
            raise ValueError("review entries must include at least one source_ref")
        return refs


class NormalizedTableCell(BaseModel):
    column_index: int
    text: str | None = None
    row_span: int = 1
    col_span: int = 1
    source_refs: list[str] = Field(default_factory=list)


class NormalizedTableRow(BaseModel):
    row_index: int
    cell_entries: list[NormalizedTableCell] = Field(default_factory=list)
    header_candidate: bool = False
    confidence: str = "medium"


class NormalizedTableEntry(BaseModel):
    table_id: str
    source_refs: list[str] = Field(default_factory=list)
    row_entries: list[NormalizedTableRow] = Field(default_factory=list)
    header_candidate_row_indexes: list[int] = Field(default_factory=list)
    row_count: int | None = None
    cell_count: int | None = None
    grid_column_count: int | None = None
    confidence: str = "medium"
    evidence_basis: list[str] = Field(default_factory=list)
    review_flags: list[NormalizedReviewEntry] = Field(default_factory=list)
    projection_hints: NormalizedProjectionHints = Field(default_factory=NormalizedProjectionHints)

    @field_validator("table_id")
    @classmethod
    def _non_empty_table_id(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("table_id must not be empty")
        return value

    @field_validator("source_refs", "evidence_basis")
    @classmethod
    def _table_entries_need_non_empty_lists(cls, value: list[str]) -> list[str]:
        items = [item.strip() for item in value if item and item.strip()]
        if not items:
            raise ValueError("must contain at least one non-empty item")
        return items


class NormalizedUnit(BaseModel):
    unit_id: str
    unit_type: str
    reading_order_index: int | None = None
    page_numbers: list[int] = Field(default_factory=list)
    source_refs: list[str] = Field(default_factory=list)
    evidence_basis: list[str] = Field(default_factory=list)
    confidence: str = "medium"
    needs_review: bool = False
    bbox: NormalizedBBox | None = None
    text: str | None = None
    content: dict[str, Any] = Field(default_factory=dict)
    structure: dict[str, Any] = Field(default_factory=dict)
    review_flags: list[NormalizedReviewEntry] = Field(default_factory=list)
    projection_hints: NormalizedProjectionHints = Field(default_factory=NormalizedProjectionHints)
    provenance: NormalizedProvenance = Field(default_factory=NormalizedProvenance)

    @field_validator("unit_id", "unit_type")
    @classmethod
    def _non_empty_unit_strings(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("must not be empty")
        return value

    @field_validator("page_numbers")
    @classmethod
    def _units_page_numbers_are_non_negative(cls, value: list[int]) -> list[int]:
        if any(page_number < 0 for page_number in value):
            raise ValueError("page_numbers must be non-negative when present")
        return value

    @field_validator("source_refs", "evidence_basis")
    @classmethod
    def _units_need_non_empty_lists(cls, value: list[str]) -> list[str]:
        items = [item.strip() for item in value if item and item.strip()]
        if not items:
            raise ValueError("must contain at least one non-empty item")
        return items


class NormalizedSummary(BaseModel):
    unit_count: int = Field(ge=0)
    review_item_count: int = Field(ge=0)
    table_count: int = Field(default=0, ge=0)
    unit_type_counts: dict[str, int] = Field(default_factory=dict)
    confidence_counts: dict[str, int] = Field(default_factory=dict)
    input_count: int = Field(default=1, ge=1)


class NormalizedAccessibilityDocument(BaseModel):
    """Shared contract between inputs/normalization and output-specific workflows.

    Downstream workflows may rely on:
    - stable document identity and source package fields
    - normalized units already ordered by reading_order_index when present
    - explicit review entries rather than hidden blockers
    - provenance on units and document metadata
    - projection hints being advisory rather than final
    """

    view_kind: Literal["normalized_accessibility_model"] = "normalized_accessibility_model"
    model_version: str = MODEL_VERSION
    source_format: str
    source_manifest_kind: str | None = None
    source_manifest_version: str | None = None
    source_package: NormalizedSourcePackage
    document: NormalizedDocumentMetadata
    summary: NormalizedSummary
    unit_entries: list[NormalizedUnit] = Field(default_factory=list)
    table_entries: list[NormalizedTableEntry] = Field(default_factory=list)
    review_entries: list[NormalizedReviewEntry] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("source_format")
    @classmethod
    def _non_empty_source_format(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("source_format must not be empty")
        return value

    @model_validator(mode="after")
    def _summary_counts_match_payload(self) -> "NormalizedAccessibilityDocument":
        if self.summary.unit_count != len(self.unit_entries):
            raise ValueError("summary.unit_count must match len(unit_entries)")
        if self.summary.review_item_count != len(self.review_entries):
            raise ValueError("summary.review_item_count must match len(review_entries)")
        if self.summary.table_count != len(self.table_entries):
            raise ValueError("summary.table_count must match len(table_entries)")
        return self
