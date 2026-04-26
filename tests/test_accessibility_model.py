from accessibility_by_manifest.normalize import (
    NormalizedAccessibilityDocument,
    NormalizedDocumentMetadata,
    NormalizedProjectionHints,
    NormalizedProvenance,
    NormalizedReviewEntry,
    NormalizedSourcePackage,
    NormalizedSummary,
    NormalizedUnit,
)
import pytest


def test_normalized_accessibility_model_has_required_contract_fields() -> None:
    document = NormalizedAccessibilityDocument(
        source_format="PDF",
        source_manifest_kind="pdf_accessibility_manifest",
        source_manifest_version="0.1",
        source_package=NormalizedSourcePackage(
            input_file_name="sample.pdf",
            input_file_path="/tmp/sample.pdf",
            sha256="abc123",
        ),
        document=NormalizedDocumentMetadata(document_id="doc-sample"),
        summary=NormalizedSummary(
            unit_count=1,
            review_item_count=1,
            unit_type_counts={"heading": 1},
            confidence_counts={"high": 1},
        ),
        unit_entries=[
            NormalizedUnit(
                unit_id="unit-1",
                unit_type="heading",
                reading_order_index=1,
                page_numbers=[1],
                source_refs=["pymupdf:page:1:block:0"],
                evidence_basis=["font_size_above_page_median"],
            )
        ],
        review_entries=[
            NormalizedReviewEntry(
                task_id="review-1",
                issue_code="DOCUMENT_TITLE_MISSING",
                severity="warning",
                scope="document",
                target_ref="document",
                reason="No document title was found.",
                source_refs=["document_metadata.title"],
                blocking=True,
            )
        ],
    )

    payload = document.model_dump(mode="json")

    assert payload["view_kind"] == "normalized_accessibility_model"
    assert payload["model_version"] == "0.1"
    assert payload["source_format"] == "PDF"
    assert payload["source_manifest_kind"] == "pdf_accessibility_manifest"
    assert payload["source_manifest_version"] == "0.1"
    assert payload["source_package"]["input_file_name"] == "sample.pdf"
    assert payload["document"]["document_id"] == "doc-sample"
    assert payload["document"]["title"] is None
    assert payload["document"]["primary_language"] is None
    assert payload["unit_entries"][0]["source_refs"]
    assert payload["unit_entries"][0]["evidence_basis"]
    assert payload["review_entries"][0]["blocking"] is True


def test_normalized_accessibility_model_supports_optional_projection_and_provenance_fields() -> None:
    unit = NormalizedUnit(
        unit_id="unit-2",
        unit_type="figure",
        page_numbers=[2],
        source_refs=["image:2:0"],
        evidence_basis=["image_block_detected"],
        needs_review=True,
        projection_hints=NormalizedProjectionHints(
            projection_status="manual_review_required",
            html_tag_hint="figure",
            pdf_structure_role_hint="Figure",
            decorative_candidate=False,
        ),
        provenance=NormalizedProvenance(
            source_refs=["image:2:0"],
            evidence_basis=["image_block_detected"],
            derived_by=["pdf_normalize_v0_1"],
            extractor_names=["pymupdf"],
        ),
    )

    payload = unit.model_dump(mode="json")

    assert payload["projection_hints"]["html_tag_hint"] == "figure"
    assert payload["projection_hints"]["pdf_structure_role_hint"] == "Figure"
    assert payload["provenance"]["derived_by"] == ["pdf_normalize_v0_1"]
    assert payload["provenance"]["extractor_names"] == ["pymupdf"]


def test_normalized_accessibility_model_rejects_units_without_provenance() -> None:
    with pytest.raises(ValueError, match="must contain at least one non-empty item"):
        NormalizedUnit(
            unit_id="unit-bad",
            unit_type="paragraph",
            source_refs=[],
            evidence_basis=[""],
        )


def test_normalized_accessibility_model_allows_non_paginated_units() -> None:
    unit = NormalizedUnit(
        unit_id="docx-unit-1",
        unit_type="paragraph",
        page_numbers=[],
        source_refs=["body_block:1"],
        evidence_basis=["wordprocessingml_paragraph"],
    )

    assert unit.page_numbers == []


def test_normalized_accessibility_model_rejects_summary_count_mismatch() -> None:
    with pytest.raises(ValueError, match="summary.unit_count must match len\\(unit_entries\\)"):
        NormalizedAccessibilityDocument(
            source_format="DOCX",
            source_package=NormalizedSourcePackage(
                input_file_name="sample.docx",
                input_file_path="/tmp/sample.docx",
            ),
            document=NormalizedDocumentMetadata(document_id="doc-mismatch"),
            summary=NormalizedSummary(
                unit_count=2,
                review_item_count=0,
                table_count=0,
                unit_type_counts={"paragraph": 1},
                confidence_counts={"medium": 1},
            ),
            unit_entries=[
                NormalizedUnit(
                    unit_id="unit-1",
                    unit_type="paragraph",
                    page_numbers=[1],
                    source_refs=["body_block:1"],
                    evidence_basis=["wordprocessingml_paragraph"],
                )
            ],
            review_entries=[],
            table_entries=[],
        )
