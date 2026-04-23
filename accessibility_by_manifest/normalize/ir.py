from __future__ import annotations

from collections import Counter
from typing import Any


IR_VERSION = "0.1"


def normalized_document_ir(
    *,
    source_manifest: dict[str, Any],
    source_format: str,
    node_entries: list[dict[str, Any]],
    table_entries: list[dict[str, Any]] | None = None,
    review_entries: list[dict[str, Any]] | None = None,
    notes: list[str] | None = None,
) -> dict[str, Any]:
    """Build the source-neutral normalized document model used by outputs."""

    node_type_counts = Counter(node.get("node_type") or "unknown" for node in node_entries)
    confidence_counts = Counter(node.get("confidence") or "unknown" for node in node_entries)
    source_package = source_manifest.get("source_package", {})
    metadata = source_manifest.get("document_metadata", {})
    return {
        "view_kind": "normalized_document_ir",
        "ir_version": IR_VERSION,
        "source_manifest_kind": source_manifest.get("manifest_kind"),
        "source_manifest_version": source_manifest.get("manifest_version"),
        "source_format": source_format,
        "source_package": {
            "input_file_name": source_package.get("input_file_name"),
            "input_file_path": source_package.get("input_file_path"),
            "sha256": source_package.get("sha256"),
        },
        "document": {
            "title": metadata.get("title"),
            "language": metadata.get("language"),
        },
        "summary": {
            "node_count": len(node_entries),
            "table_count": len(table_entries or []),
            "review_item_count": len(review_entries or []),
            "node_type_counts": dict(sorted(node_type_counts.items())),
            "confidence_counts": dict(sorted(confidence_counts.items())),
        },
        "node_entries": node_entries,
        "table_entries": table_entries or [],
        "review_entries": review_entries or [],
        "notes": notes or [],
    }


def ir_node(
    *,
    node_id: str,
    node_type: str,
    reading_order_index: int,
    source_refs: list[str],
    content: dict[str, Any] | None = None,
    structure: dict[str, Any] | None = None,
    evidence_basis: list[str] | None = None,
    confidence: str = "medium",
    review_flags: list[dict[str, Any]] | None = None,
    projection_hints: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "node_id": node_id,
        "node_type": node_type,
        "reading_order_index": reading_order_index,
        "source_refs": source_refs,
        "content": content or {},
        "structure": structure or {},
        "evidence_basis": evidence_basis or [],
        "confidence": confidence,
        "review_flags": review_flags or [],
        "projection_hints": projection_hints or {},
    }


def review_item(
    *,
    issue_code: str,
    severity: str,
    scope: str,
    target_ref: str,
    reason: str,
    source_refs: list[str],
    suggested_action: str | None = None,
) -> dict[str, Any]:
    return {
        "issue_code": issue_code,
        "severity": severity,
        "scope": scope,
        "target_ref": target_ref,
        "reason": reason,
        "source_refs": source_refs,
        "suggested_action": suggested_action,
    }
