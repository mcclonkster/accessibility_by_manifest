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
    document_metadata_from_manifest,
    projection_hints_from_payload,
    provenance_from_payload,
    review_entry_from_payload,
    source_package_from_manifest,
    summary_from_entries,
)
from accessibility_by_manifest.normalize.docx import normalize_docx_manifest_to_ir


def normalize_docx_manifest_to_accessibility_model(manifest: dict[str, Any]) -> NormalizedAccessibilityDocument:
    return docx_ir_to_accessibility_model(normalize_docx_manifest_to_ir(manifest))


def docx_ir_to_accessibility_model(normalized_ir: dict[str, Any]) -> NormalizedAccessibilityDocument:
    source_package = source_package_from_manifest(normalized_ir.get("source_package", {}), "DOCX")
    unit_entries = [_unit_from_ir_node(node) for node in normalized_ir.get("node_entries", [])]
    table_entries = [_table_from_ir_entry(table_entry) for table_entry in normalized_ir.get("table_entries", [])]
    review_entries = [
        review_entry_from_payload(entry, task_prefix="docx_review", index=index, fallback_target_ref="document")
        for index, entry in enumerate(normalized_ir.get("review_entries", []), start=1)
    ]
    return NormalizedAccessibilityDocument(
        source_format="DOCX",
        source_manifest_kind=normalized_ir.get("source_manifest_kind"),
        source_manifest_version=normalized_ir.get("source_manifest_version"),
        source_package=source_package,
        document=document_metadata_from_manifest(
            normalized_ir.get("document", {}),
            normalized_ir.get("source_package", {}),
            source_format="DOCX",
            metadata_basis=["docx_normalized_ir"],
        ),
        summary=summary_from_entries(unit_entries, review_entries, table_entries),
        unit_entries=unit_entries,
        table_entries=table_entries,
        review_entries=review_entries,
        notes=list(normalized_ir.get("notes") or []),
        metadata={"source_view_kind": normalized_ir.get("view_kind"), "source_ir_version": normalized_ir.get("ir_version")},
    )


def _unit_from_ir_node(node: dict[str, Any]) -> NormalizedUnit:
    source_refs = list(node.get("source_refs") or [str(node.get("node_id") or "node")])
    evidence_basis = list(node.get("evidence_basis") or ["docx_normalized_ir"])
    review_flags = [
        review_entry_from_payload(entry, task_prefix="docx_unit_review", index=index, fallback_target_ref=node["node_id"])
        for index, entry in enumerate(node.get("review_flags", []), start=1)
    ]
    content = dict(node.get("content") or {})
    text = content.get("text") if isinstance(content.get("text"), str) else None
    return NormalizedUnit(
        unit_id=str(node.get("node_id") or "unknown-unit"),
        unit_type=str(node.get("node_type") or "unknown"),
        reading_order_index=node.get("reading_order_index"),
        page_numbers=[],
        source_refs=source_refs,
        evidence_basis=evidence_basis,
        confidence=str(node.get("confidence") or "medium"),
        needs_review=bool(review_flags),
        text=text,
        content=content,
        structure=dict(node.get("structure") or {}),
        review_flags=review_flags,
        projection_hints=projection_hints_from_payload(
            dict(node.get("projection_hints") or {}),
            artifact_candidate=str(node.get("node_type") or "") == "artifact",
            html_tag_hint=html_tag_hint_for_unit(str(node.get("node_type") or ""), dict(node.get("projection_hints") or {}), heading_level=(node.get("structure") or {}).get("heading_level")),
            docx_style_hint=docx_style_hint_for_unit(str(node.get("node_type") or ""), dict(node.get("projection_hints") or {}), heading_level=(node.get("structure") or {}).get("heading_level")),
            preferred_output_roles={"html": html_tag_hint_for_unit(str(node.get("node_type") or ""), dict(node.get("projection_hints") or {}), heading_level=(node.get("structure") or {}).get("heading_level"))} if html_tag_hint_for_unit(str(node.get("node_type") or ""), dict(node.get("projection_hints") or {}), heading_level=(node.get("structure") or {}).get("heading_level")) else {},
        ),
        provenance=provenance_from_payload(
            source_refs=source_refs,
            evidence_basis=evidence_basis,
            source_format="DOCX",
            derived_by=["normalize_docx_manifest_to_ir", "docx_ir_to_accessibility_model"],
        ),
    )


def _table_from_ir_entry(table_entry: dict[str, Any]) -> NormalizedTableEntry:
    review_flags = [
        review_entry_from_payload(entry, task_prefix="docx_table_review", index=index, fallback_target_ref=table_entry["table_id"])
        for index, entry in enumerate(table_entry.get("review_flags", []), start=1)
    ]
    row_entries = [
        NormalizedTableRow(
            row_index=int(row_entry.get("row_index") or 0),
            cell_entries=[
                NormalizedTableCell(
                    column_index=int(cell_entry.get("column_index") or 0),
                    text=cell_entry.get("text"),
                    source_refs=list(table_entry.get("source_refs") or [table_entry["table_id"]]),
                )
                for cell_entry in row_entry.get("cell_entries", [])
            ],
            header_candidate=bool(row_entry.get("header_candidate")),
            confidence=str(row_entry.get("confidence") or "medium"),
        )
        for row_entry in table_entry.get("row_entries", [])
    ]
    return NormalizedTableEntry(
        table_id=str(table_entry.get("table_id") or "unknown-table"),
        source_refs=list(table_entry.get("source_refs") or [str(table_entry.get("table_id") or "unknown-table")]),
        row_entries=row_entries,
        header_candidate_row_indexes=list(table_entry.get("header_candidate_row_indexes") or []),
        row_count=table_entry.get("row_count"),
        cell_count=table_entry.get("cell_count"),
        grid_column_count=table_entry.get("grid_column_count"),
        confidence=str(table_entry.get("confidence") or "medium"),
        evidence_basis=list(table_entry.get("evidence_basis") or ["docx_normalized_ir"]),
        review_flags=review_flags,
        projection_hints=projection_hints_from_payload(
            {"projection_status": "manual_review_required" if review_flags else "planned"},
            html_tag_hint=html_tag_hint_for_unit("table", None),
            pdf_structure_role_hint=pdf_structure_role_hint_for_unit("table", None),
            docx_style_hint=docx_style_hint_for_unit("table", None),
            preferred_output_roles={"html": "table", "pdf": "Table"},
        ),
    )
