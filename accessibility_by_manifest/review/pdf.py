from __future__ import annotations

from typing import Any


def review_pdf_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    """Add document-level review warnings that remain after normalization."""

    manifest.setdefault("review_entries", [])
    add_missing_metadata_warnings(manifest)
    add_image_only_page_warnings(manifest)
    add_reading_order_warnings(manifest)
    add_table_review_warnings(manifest)
    add_figure_review_warnings(manifest)
    manifest["document_summary"]["pages_with_warnings"] = pages_with_warnings(manifest)
    if manifest["document_warning_entries"] or manifest["review_entries"]:
        manifest["projected_target"]["projection_status"] = "manual_review_required"
    return manifest


def add_missing_metadata_warnings(manifest: dict[str, Any]) -> None:
    metadata = manifest.get("document_metadata", {})
    if not metadata.get("title"):
        append_review_entry(
            manifest,
            review_entry(
                "DOCUMENT_TITLE_MISSING",
                "warning",
                "metadata",
                "document_metadata.title",
                "No usable document title was found in metadata.",
                [],
                {"metadata_field": "title", "confidence": "missing"},
                "Derive a title from the first reliable heading or confirm a human-supplied title.",
            ),
        )
        append_document_warning(
            manifest,
            warning_entry(
                "DOCUMENT_TITLE_MISSING",
                "No usable document title was found in metadata; projection should derive or review a title.",
                "metadata",
            ),
        )
    if not metadata.get("language"):
        append_review_entry(
            manifest,
            review_entry(
                "DOCUMENT_LANGUAGE_MISSING",
                "warning",
                "metadata",
                "document_metadata.language",
                "No document language was found in metadata or catalog evidence.",
                [],
                {"metadata_field": "language", "confidence": "missing"},
                "Set the document language before treating projected output as final.",
            ),
        )
        append_document_warning(
            manifest,
            warning_entry(
                "DOCUMENT_LANGUAGE_MISSING",
                "No document language was found in metadata or catalog evidence.",
                "metadata",
            ),
        )


def add_image_only_page_warnings(manifest: dict[str, Any]) -> None:
    normalized_pages = {
        int(page_number)
        for block in manifest.get("normalized_block_entries", [])
        for page_number in block.get("page_span", [])
        if isinstance(page_number, int)
    }
    for page in manifest.get("page_entries", []):
        observed = page.get("observed_source", {})
        if not observed.get("image_only_page_suspected"):
            continue
        page_number = int(page.get("page_number") or 0)
        has_sidecar_recovery = page_number in normalized_pages
        issue_code = "IMAGE_ONLY_PAGE_WITH_SIDECAR_RECOVERY_REVIEW" if has_sidecar_recovery else "IMAGE_ONLY_PAGE_OCR_REQUIRED"
        reason = (
            "Image-only page has Docling/OCR sidecar recovery evidence; recovered text, regions, or structure require review."
            if has_sidecar_recovery
            else "Image-only page has no normalized text evidence; OCR or another recovery path is required."
        )
        append_review_entry(
            manifest,
            review_entry(
                issue_code,
                "warning",
                "page",
                f"page:{page_number}",
                reason,
                [f"page:{page_number}"],
                {"image_only_page_suspected": True, "sidecar_recovery_present": has_sidecar_recovery},
                "Review recovered text, regions, and table/figure structure before final accessible output." if has_sidecar_recovery else "Run OCR or a sidecar parser before final accessible output.",
            ),
        )
    if any(page.get("observed_source", {}).get("image_only_page_suspected") for page in manifest.get("page_entries", [])):
        append_document_warning(
            manifest,
            warning_entry(
                "IMAGE_ONLY_PAGES_REQUIRE_REVIEW",
                "One or more pages are image-only or scanned; recovered text/structure must be reviewed before final output.",
                "ocr",
            ),
        )


def add_reading_order_warnings(manifest: dict[str, Any]) -> None:
    normalized_blocks = manifest.get("normalized_block_entries", [])
    if not normalized_blocks:
        append_document_warning(
            manifest,
            warning_entry(
                "NO_NORMALIZED_BLOCKS",
                "No normalized blocks were produced from the extracted evidence.",
                "reading_order",
            ),
        )
        return
    low_confidence_count = sum(1 for block in normalized_blocks if block["normalized_workflow"]["role_confidence"] == "low")
    if low_confidence_count:
        low_confidence_refs = [
            block["block_id"]
            for block in normalized_blocks
            if block["normalized_workflow"]["role_confidence"] == "low"
        ][:50]
        append_review_entry(
            manifest,
            review_entry(
                "LOW_CONFIDENCE_NORMALIZATION_PRESENT",
                "info",
                "reading_order",
                "normalized_block_entries",
                f"{low_confidence_count} normalized block(s) were assigned low-confidence roles.",
                low_confidence_refs,
                {"low_confidence_count": low_confidence_count, "confidence": "low"},
                "Spot-check low-confidence roles before final projection.",
            ),
        )
        append_document_warning(
            manifest,
            warning_entry(
                "LOW_CONFIDENCE_NORMALIZATION_PRESENT",
                f"{low_confidence_count} normalized block(s) require review before projection is treated as final.",
                "reading_order",
                severity="info",
            ),
        )


def add_figure_review_warnings(manifest: dict[str, Any]) -> None:
    if manifest.get("document_summary", {}).get("figure_candidate_count", 0) <= 0:
        return
    append_review_entry(
        manifest,
        review_entry(
            "FIGURE_CANDIDATES_REQUIRE_REVIEW",
            "warning",
            "figure",
            "document_summary.figure_candidate_count",
            "Image or figure-like evidence was detected, but meaningful-vs-decorative status is unresolved.",
            [],
            {"figure_candidate_count": manifest.get("document_summary", {}).get("figure_candidate_count", 0), "confidence": "unknown"},
            "Confirm which figures need text alternatives before final output.",
        ),
    )
    append_document_warning(
        manifest,
        warning_entry(
            "FIGURE_CANDIDATES_REQUIRE_REVIEW",
            "Image or figure-like evidence was detected; meaningful figures need text alternatives before final output.",
            "figure",
        ),
    )


def add_table_review_warnings(manifest: dict[str, Any]) -> None:
    table_blocks = [block for block in manifest.get("normalized_block_entries", []) if block["normalized_workflow"]["interpreted_role"] == "table_cell"]
    table_cell_count = len(table_blocks)
    if table_cell_count <= 0:
        return
    table_entries = manifest.get("normalized_table_entries", [])
    table_ids = sorted({table["table_id"] for table in table_entries} or {block["projected_target"].get("target_table_id") for block in table_blocks if block["projected_target"].get("target_table_id")})
    for table_entry in table_entries:
        if not table_entry.get("header_candidate_row_indexes"):
            append_review_entry(
                manifest,
                review_entry(
                    "TABLE_HEADERS_UNCERTAIN",
                    "warning",
                    "table",
                    table_entry["table_id"],
                    "This normalized table region does not have a confident header-row candidate.",
                    table_entry.get("source_block_ids", []),
                    {
                        "confidence": table_entry.get("confidence"),
                        "row_count": len(table_entry.get("row_entries", [])),
                        "header_candidate_row_indexes": table_entry.get("header_candidate_row_indexes", []),
                    },
                    "Review the table header row and spanning-cell relationships before final projection.",
                ),
            )
        if len(table_entry.get("row_entries", [])) <= 1:
            append_review_entry(
                manifest,
                review_entry(
                    "TABLE_BOUNDARY_REVIEW",
                    "info",
                    "table",
                    table_entry["table_id"],
                    "This table region has one or fewer inferred rows, so the table boundary may be too narrow.",
                    table_entry.get("source_block_ids", []),
                    {"confidence": table_entry.get("confidence"), "row_count": len(table_entry.get("row_entries", []))},
                    "Check whether nearby table-cell candidates belong to the same table.",
                ),
            )
    append_document_warning(
        manifest,
        warning_entry(
            "TABLE_STRUCTURE_REVIEW",
            f"{table_cell_count} table-cell candidate block(s) across {len(table_ids)} table region(s) were detected; table boundaries and headers need normalization/review.",
            "block",
        ),
    )
    append_document_warning(
        manifest,
        warning_entry(
            "TABLE_HEADERS_UNCERTAIN",
            "Table region candidates were grouped, but header rows and spanning-cell relationships have not been resolved.",
            "block",
        ),
    )


def append_document_warning(manifest: dict[str, Any], warning: dict[str, Any]) -> None:
    existing = {
        (item.get("warning_code"), item.get("warning_scope"), item.get("warning_message"))
        for item in manifest.get("document_warning_entries", [])
    }
    key = (warning.get("warning_code"), warning.get("warning_scope"), warning.get("warning_message"))
    if key not in existing:
        manifest.setdefault("document_warning_entries", []).append(warning)


def append_review_entry(manifest: dict[str, Any], entry: dict[str, Any]) -> None:
    existing = {
        (item.get("issue_code"), item.get("scope"), item.get("target_ref"), item.get("reason"))
        for item in manifest.get("review_entries", [])
    }
    key = (entry.get("issue_code"), entry.get("scope"), entry.get("target_ref"), entry.get("reason"))
    if key not in existing:
        manifest.setdefault("review_entries", []).append(entry)


def warning_entry(code: str, message: str, scope: str, severity: str = "warning", manual_review_required: bool = True) -> dict[str, Any]:
    return {
        "warning_code": code,
        "warning_message": message,
        "warning_scope": scope,
        "warning_severity": severity,
        "manual_review_required": manual_review_required,
    }


def review_entry(
    code: str,
    severity: str,
    scope: str,
    target_ref: str | None,
    reason: str,
    source_refs: list[str],
    confidence_context: dict[str, Any],
    suggested_action: str | None,
) -> dict[str, Any]:
    return {
        "issue_code": code,
        "severity": severity,
        "scope": scope,
        "target_ref": target_ref,
        "reason": reason,
        "source_refs": source_refs,
        "confidence_context": confidence_context,
        "suggested_action": suggested_action,
    }


def pages_with_warnings(manifest: dict[str, Any]) -> int:
    pages = {page["page_number"] for page in manifest.get("page_entries", []) if page.get("warning_entries")}
    for block in manifest.get("normalized_block_entries", []):
        if block.get("warning_entries"):
            pages.update(block.get("page_span", []))
    return len(pages)
