from __future__ import annotations

from collections import Counter
from typing import Any

from accessibility_by_manifest.normalize.accessibility_model import (
    NormalizedBBox,
    NormalizedDocumentMetadata,
    NormalizedProjectionHints,
    NormalizedProvenance,
    NormalizedReviewEntry,
    NormalizedSourcePackage,
    NormalizedSummary,
)


def document_id_for_source_package(source_package: dict[str, Any]) -> str:
    sha256 = str(source_package.get("sha256") or "").strip()
    if sha256:
        if sha256.startswith("sha256:"):
            return sha256
        return f"sha256:{sha256}"
    input_path = str(source_package.get("input_file_path") or "").strip()
    if input_path:
        return input_path
    input_name = str(source_package.get("input_file_name") or "").strip()
    if input_name:
        return input_name
    return "unknown-document"


def source_package_from_manifest(source_package: dict[str, Any], source_format: str) -> NormalizedSourcePackage:
    return NormalizedSourcePackage(
        input_file_name=str(source_package.get("input_file_name") or "unknown").strip(),
        input_file_path=str(source_package.get("input_file_path") or source_package.get("input_file_name") or "unknown").strip(),
        sha256=source_package.get("sha256"),
        source_id=source_package.get("source_id"),
        format_family=source_package.get("format_family") or source_format,
    )


def document_metadata_from_manifest(
    metadata: dict[str, Any],
    source_package: dict[str, Any],
    *,
    source_format: str,
    metadata_refs: list[str] | None = None,
    metadata_basis: list[str] | None = None,
) -> NormalizedDocumentMetadata:
    return NormalizedDocumentMetadata(
        document_id=document_id_for_source_package(source_package),
        title=metadata.get("title"),
        primary_language=metadata.get("language"),
        author=metadata.get("author"),
        subject=metadata.get("subject"),
        keywords=metadata.get("keywords") or [],
        created_at=metadata.get("created_at") or metadata.get("creation_date"),
        modified_at=metadata.get("modified_at") or metadata.get("modification_date"),
        metadata_provenance=NormalizedProvenance(
            source_refs=_normalized_refs(
                metadata_refs
                or [
                    "document_metadata.title",
                    "document_metadata.language",
                    "source_package.input_file_path",
                ]
            ),
            evidence_basis=_normalized_refs(metadata_basis or [f"{source_format.lower()}_document_metadata"]),
            source_format=source_format,
        ),
    )


def summary_from_entries(
    unit_entries: list[Any],
    review_entries: list[Any],
    table_entries: list[Any],
    *,
    input_count: int = 1,
) -> NormalizedSummary:
    unit_type_counts = Counter(getattr(unit, "unit_type", "unknown") or "unknown" for unit in unit_entries)
    confidence_counts = Counter(getattr(unit, "confidence", "unknown") or "unknown" for unit in unit_entries)
    return NormalizedSummary(
        unit_count=len(unit_entries),
        review_item_count=len(review_entries),
        table_count=len(table_entries),
        unit_type_counts=dict(sorted(unit_type_counts.items())),
        confidence_counts=dict(sorted(confidence_counts.items())),
        input_count=max(1, input_count),
    )


def review_entry_from_payload(
    entry: dict[str, Any],
    *,
    task_prefix: str,
    index: int,
    fallback_target_ref: str,
) -> NormalizedReviewEntry:
    issue_code = str(entry.get("issue_code") or "UNKNOWN_REVIEW_ITEM").strip()
    target_ref = str(entry.get("target_ref") or fallback_target_ref).strip() or fallback_target_ref
    source_refs = _normalized_refs(entry.get("source_refs") or [target_ref])
    severity = str(entry.get("severity") or "warning").strip() or "warning"
    return NormalizedReviewEntry(
        task_id=f"{task_prefix}_{index:04d}_{issue_code.lower()}",
        issue_code=issue_code,
        severity=severity,
        scope=str(entry.get("scope") or "document").strip() or "document",
        target_ref=target_ref,
        reason=str(entry.get("reason") or issue_code).strip() or issue_code,
        source_refs=source_refs,
        blocking=severity not in {"info", "note"},
        suggested_action=entry.get("suggested_action"),
        resolved=bool(entry.get("resolved", False)),
        confidence_context=dict(entry.get("confidence_context") or {}),
    )


def projection_hints_from_payload(
    payload: dict[str, Any] | None,
    *,
    artifact_candidate: bool = False,
    decorative_candidate: bool = False,
    html_tag_hint: str | None = None,
    pdf_structure_role_hint: str | None = None,
    docx_style_hint: str | None = None,
    preferred_output_roles: dict[str, str] | None = None,
) -> NormalizedProjectionHints:
    payload = payload or {}
    return NormalizedProjectionHints(
        projection_status=str(payload.get("projection_status") or "planned"),
        preferred_output_roles=preferred_output_roles or {},
        html_tag_hint=html_tag_hint,
        pdf_structure_role_hint=pdf_structure_role_hint,
        docx_style_hint=docx_style_hint or payload.get("docx_style") or payload.get("target_style"),
        artifact_candidate=artifact_candidate,
        decorative_candidate=decorative_candidate,
        metadata={
            key: value
            for key, value in payload.items()
            if key not in {"projection_status", "docx_style", "target_style"}
        },
    )


def provenance_from_payload(
    *,
    source_refs: list[str],
    evidence_basis: list[str],
    source_format: str,
    derived_by: list[str] | None = None,
    extractor_names: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
) -> NormalizedProvenance:
    return NormalizedProvenance(
        source_refs=_normalized_refs(source_refs),
        evidence_basis=_normalized_refs(evidence_basis),
        derived_by=_normalized_refs(derived_by or []),
        source_format=source_format,
        extractor_names=_normalized_refs(extractor_names or []),
        metadata=metadata or {},
    )


def bbox_from_payload(bbox: Any) -> NormalizedBBox | None:
    if isinstance(bbox, list) and len(bbox) == 4 and all(value is not None for value in bbox):
        return NormalizedBBox(
            left=float(bbox[0]),
            top=float(bbox[1]),
            right=float(bbox[2]),
            bottom=float(bbox[3]),
        )
    return None


def _normalized_refs(values: list[Any]) -> list[str]:
    refs = [str(value).strip() for value in values if str(value).strip()]
    return refs
