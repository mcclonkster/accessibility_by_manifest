from __future__ import annotations

from typing import Any

from accessibility_by_manifest.normalize.accessibility_model import (
    NormalizedAccessibilityDocument,
    NormalizedTableCell,
    NormalizedTableEntry,
    NormalizedTableRow,
    NormalizedUnit,
)
from accessibility_by_manifest.outputs.projection import (
    docx_style_hint_for_unit,
    html_tag_hint_for_unit,
    pdf_structure_role_hint_for_unit,
)
from accessibility_by_manifest.normalize.accessibility_model_bridge import (
    bbox_from_payload,
    document_metadata_from_manifest,
    projection_hints_from_payload,
    provenance_from_payload,
    review_entry_from_payload,
    source_package_from_manifest,
    summary_from_entries,
)


def normalize_pdf_manifest_to_accessibility_model(manifest: dict[str, Any]) -> NormalizedAccessibilityDocument:
    raw_blocks_by_id = {str(block.get("block_id")): block for block in manifest.get("raw_block_entries", [])}
    unit_entries = [_unit_from_pdf_block(block, raw_blocks_by_id) for block in manifest.get("normalized_block_entries", [])]
    table_entries = [_table_from_pdf_entry(table_entry, raw_blocks_by_id) for table_entry in manifest.get("normalized_table_entries", [])]
    review_entries = [
        review_entry_from_payload(entry, task_prefix="pdf_review", index=index, fallback_target_ref="document")
        for index, entry in enumerate(manifest.get("review_entries", []), start=1)
    ]
    summary = manifest.get("document_summary", {})
    return NormalizedAccessibilityDocument(
        source_format="PDF",
        source_manifest_kind=manifest.get("manifest_kind"),
        source_manifest_version=manifest.get("manifest_version"),
        source_package=source_package_from_manifest(manifest.get("source_package", {}), "PDF"),
        document=document_metadata_from_manifest(
            manifest.get("document_metadata", {}),
            manifest.get("source_package", {}),
            source_format="PDF",
            metadata_basis=["pdf_document_metadata", "pdf_catalog_metadata"],
        ),
        summary=summary_from_entries(
            unit_entries,
            review_entries,
            table_entries,
            input_count=int(summary.get("total_pages") or 1),
        ),
        unit_entries=unit_entries,
        table_entries=table_entries,
        review_entries=review_entries,
        notes=[
            "Derived from the PDF manifest without rerunning extraction.",
            "Raw evidence remains in the source manifest; this view is the shared accessibility contract.",
        ],
        metadata={
            "pages_with_warnings": summary.get("pages_with_warnings"),
            "image_only_pages_present": summary.get("image_only_pages_present"),
            "document_accessibility": dict(manifest.get("document_accessibility") or {}),
            "projected_target": dict(manifest.get("projected_target") or {}),
        },
    )


def _unit_from_pdf_block(normalized_block: dict[str, Any], raw_blocks_by_id: dict[str, dict[str, Any]]) -> NormalizedUnit:
    normalized_workflow = dict(normalized_block.get("normalized_workflow") or {})
    raw_block_id = str(normalized_block.get("block_id") or "").removeprefix("n_")
    raw_block = raw_blocks_by_id.get(raw_block_id, {})
    unit_type = str(normalized_workflow.get("interpreted_role") or "unknown")
    source_refs = list(normalized_block.get("observed_source_refs") or [str(normalized_block.get("block_id") or raw_block_id or "unknown-block")])
    evidence_basis = list(normalized_workflow.get("role_basis") or ["pdf_normalized_block"])
    review_flags = [
        review_entry_from_payload(entry, task_prefix="pdf_unit_review", index=index, fallback_target_ref=str(normalized_block.get("block_id") or raw_block_id or "unknown-block"))
        for index, entry in enumerate(_warning_entries_to_review_entries(normalized_block.get("warning_entries", []), source_refs, normalized_block.get("block_id")), start=1)
    ]
    heading_level = normalized_workflow.get("heading_level")
    return NormalizedUnit(
        unit_id=str(normalized_block.get("block_id") or raw_block_id or "unknown-block"),
        unit_type=unit_type,
        reading_order_index=normalized_workflow.get("reading_order_index"),
        page_numbers=[int(page_number) for page_number in normalized_block.get("page_span", []) if isinstance(page_number, int)],
        source_refs=source_refs,
        evidence_basis=evidence_basis,
        confidence=str(normalized_workflow.get("role_confidence") or "medium"),
        needs_review=bool(normalized_workflow.get("manual_review_required")) or bool(review_flags),
        bbox=bbox_from_payload(raw_block.get("bbox")),
        text=raw_block.get("text"),
        content={"text": raw_block.get("text")} if raw_block.get("text") else {},
        structure={
            "heading_level": heading_level,
            "list_kind": normalized_workflow.get("list_kind"),
            "semantic_source_quality": normalized_workflow.get("semantic_source_quality"),
        },
        review_flags=review_flags,
        projection_hints=projection_hints_from_payload(
            dict(normalized_block.get("projected_target") or {}),
            artifact_candidate=unit_type == "artifact",
            html_tag_hint=html_tag_hint_for_unit(unit_type, None, heading_level=heading_level),
            pdf_structure_role_hint=pdf_structure_role_hint_for_unit(unit_type, None, heading_level=heading_level),
            docx_style_hint=docx_style_hint_for_unit(unit_type, dict(normalized_block.get("projected_target") or {}), heading_level=heading_level),
            preferred_output_roles=_preferred_output_roles_for_pdf_role(unit_type, heading_level),
        ),
        provenance=provenance_from_payload(
            source_refs=source_refs,
            evidence_basis=evidence_basis,
            source_format="PDF",
            derived_by=["normalize_pdf_manifest", "normalize_pdf_manifest_to_accessibility_model"],
            extractor_names=sorted((raw_block.get("extractor_evidence") or {}).keys()),
        ),
    )


def _table_from_pdf_entry(table_entry: dict[str, Any], raw_blocks_by_id: dict[str, dict[str, Any]]) -> NormalizedTableEntry:
    source_block_ids = list(table_entry.get("source_block_ids") or [str(table_entry.get("table_id") or "unknown-table")])
    review_flags = [
        review_entry_from_payload(entry, task_prefix="pdf_table_review", index=index, fallback_target_ref=str(table_entry.get("table_id") or "unknown-table"))
        for index, entry in enumerate(_warning_entries_to_review_entries(table_entry.get("warning_entries", []), source_block_ids, table_entry.get("table_id")), start=1)
    ]
    row_entries = []
    for row_entry in table_entry.get("row_entries", []):
        cell_entries = []
        for column_index, block_id in enumerate(row_entry.get("cell_block_ids", []), start=1):
            raw_block = raw_blocks_by_id.get(str(block_id).removeprefix("n_"), {})
            cell_entries.append(
                NormalizedTableCell(
                    column_index=column_index,
                    text=raw_block.get("text"),
                    source_refs=[str(block_id)],
                )
            )
        row_entries.append(
            NormalizedTableRow(
                row_index=int(row_entry.get("row_index") or 0),
                cell_entries=cell_entries,
                header_candidate=bool(row_entry.get("header_candidate")),
                confidence=str(row_entry.get("confidence") or "medium"),
            )
        )
    return NormalizedTableEntry(
        table_id=str(table_entry.get("table_id") or "unknown-table"),
        source_refs=source_block_ids,
        row_entries=row_entries,
        header_candidate_row_indexes=list(table_entry.get("header_candidate_row_indexes") or []),
        row_count=len(row_entries),
        cell_count=sum(len(row.cell_entries) for row in row_entries),
        grid_column_count=max((len(row.cell_entries) for row in row_entries), default=0),
        confidence=str(table_entry.get("confidence") or "medium"),
        evidence_basis=list(table_entry.get("basis") or ["pdf_table_region"]),
        review_flags=review_flags,
        projection_hints=projection_hints_from_payload(
            {"projection_status": "manual_review_required" if review_flags else "planned"},
            html_tag_hint=html_tag_hint_for_unit("table", None),
            pdf_structure_role_hint=pdf_structure_role_hint_for_unit("table", None),
            preferred_output_roles={"html": "table", "pdf": "Table"},
        ),
    )


def _warning_entries_to_review_entries(
    warning_entries: list[dict[str, Any]],
    source_refs: list[str],
    target_ref: Any,
) -> list[dict[str, Any]]:
    return [
        {
            "issue_code": warning.get("warning_code"),
            "severity": warning.get("warning_severity", "warning"),
            "scope": warning.get("warning_scope", "unit"),
            "target_ref": str(target_ref or "document"),
            "reason": warning.get("warning_message"),
            "source_refs": list(source_refs),
            "confidence_context": {"manual_review_required": warning.get("manual_review_required", True)},
        }
        for warning in warning_entries
    ]


def _preferred_output_roles_for_pdf_role(unit_type: str, heading_level: Any) -> dict[str, str]:
    preferred_roles: dict[str, str] = {}
    html_tag_hint = html_tag_hint_for_unit(unit_type, None, heading_level=heading_level)
    pdf_structure_role_hint = pdf_structure_role_hint_for_unit(unit_type, None, heading_level=heading_level)
    if html_tag_hint:
        preferred_roles["html"] = html_tag_hint
    if pdf_structure_role_hint:
        preferred_roles["pdf"] = pdf_structure_role_hint
    return preferred_roles
