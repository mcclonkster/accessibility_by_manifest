from accessibility_by_manifest.normalize import (
    NormalizedAccessibilityDocument,
    NormalizedDocumentMetadata,
    NormalizedProjectionHints,
    NormalizedReviewEntry,
    NormalizedSourcePackage,
    NormalizedSummary,
    NormalizedTableCell,
    NormalizedTableEntry,
    NormalizedTableRow,
    NormalizedUnit,
)
from accessibility_by_manifest.outputs.html import build_accessible_html


def test_accessible_html_renders_heading_paragraph_table_and_figure() -> None:
    document = NormalizedAccessibilityDocument(
        source_format="PDF",
        source_package=NormalizedSourcePackage(input_file_name="sample.pdf", input_file_path="/tmp/sample.pdf"),
        document=NormalizedDocumentMetadata(document_id="doc-1", title="Sample", primary_language="en-US"),
        summary=NormalizedSummary(
            unit_count=5,
            review_item_count=1,
            table_count=1,
            unit_type_counts={"heading": 1, "paragraph": 1, "table": 1, "figure": 1, "artifact": 1},
            confidence_counts={"high": 5},
        ),
        unit_entries=[
            NormalizedUnit(unit_id="u1", unit_type="heading", reading_order_index=1, page_numbers=[1], text="Report", source_refs=["r1"], evidence_basis=["b1"], structure={"heading_level": 2}),
            NormalizedUnit(unit_id="u2", unit_type="paragraph", reading_order_index=2, page_numbers=[1], text="A short paragraph.", source_refs=["r2"], evidence_basis=["b2"]),
            NormalizedUnit(unit_id="u3", unit_type="table", reading_order_index=3, page_numbers=[1], source_refs=["t1"], evidence_basis=["b3"], structure={"table_id": "table-1"}),
            NormalizedUnit(unit_id="u4", unit_type="figure", reading_order_index=4, page_numbers=[1], text="Figure caption", source_refs=["f1"], evidence_basis=["b4"], content={"alt_text": "Meaningful chart"}),
            NormalizedUnit(unit_id="u5", unit_type="artifact", reading_order_index=5, page_numbers=[1], text="Page 1", source_refs=["a1"], evidence_basis=["b5"], projection_hints=NormalizedProjectionHints(projection_status="omitted")),
        ],
        table_entries=[
            NormalizedTableEntry(
                table_id="table-1",
                source_refs=["t1"],
                evidence_basis=["b3"],
                header_candidate_row_indexes=[1],
                row_entries=[
                    NormalizedTableRow(row_index=1, header_candidate=True, cell_entries=[NormalizedTableCell(column_index=1, text="Account"), NormalizedTableCell(column_index=2, text="Amount")]),
                    NormalizedTableRow(row_index=2, header_candidate=False, cell_entries=[NormalizedTableCell(column_index=1, text="Cash"), NormalizedTableCell(column_index=2, text="$10")]),
                ],
            )
        ],
        review_entries=[
            NormalizedReviewEntry(
                task_id="r-1",
                issue_code="FIGURE_ALT_TEXT_REVIEW",
                severity="warning",
                scope="figure",
                target_ref="u4",
                reason="Review figure wording.",
                source_refs=["f1"],
                blocking=False,
            )
        ],
    )

    rendered = build_accessible_html(document)

    assert '<html lang="en-US">' in rendered
    assert "<h2>Report</h2>" in rendered
    assert "<p>A short paragraph.</p>" in rendered
    assert "<table>" in rendered
    assert "<th>Account</th>" in rendered
    assert "<td>$10</td>" in rendered
    assert 'alt="Meaningful chart"' in rendered
    assert "<figcaption>Figure caption</figcaption>" in rendered
    assert "Page 1" not in rendered


def test_accessible_html_groups_list_items_and_uses_review_placeholder_alt() -> None:
    document = NormalizedAccessibilityDocument(
        source_format="DOCX",
        source_package=NormalizedSourcePackage(input_file_name="sample.docx", input_file_path="/tmp/sample.docx"),
        document=NormalizedDocumentMetadata(document_id="doc-2", title="List Sample", primary_language="en"),
        summary=NormalizedSummary(
            unit_count=3,
            review_item_count=0,
            table_count=0,
            unit_type_counts={"list_item": 2, "figure": 1},
            confidence_counts={"medium": 3},
        ),
        unit_entries=[
            NormalizedUnit(unit_id="l1", unit_type="list_item", reading_order_index=1, page_numbers=[], text="One", source_refs=["l1"], evidence_basis=["b1"]),
            NormalizedUnit(unit_id="l2", unit_type="list_item", reading_order_index=2, page_numbers=[], text="Two", source_refs=["l2"], evidence_basis=["b2"]),
            NormalizedUnit(unit_id="f1", unit_type="figure", reading_order_index=3, page_numbers=[], source_refs=["f1"], evidence_basis=["b3"], needs_review=True),
        ],
        review_entries=[],
    )

    rendered = build_accessible_html(document)

    assert "<ul>" in rendered
    assert "<li>One</li>" in rendered
    assert "<li>Two</li>" in rendered
    assert 'alt="Description pending review."' in rendered


def test_accessible_html_promotes_title_paragraph_to_h1_when_no_heading_exists() -> None:
    document = NormalizedAccessibilityDocument(
        source_format="PDF",
        source_package=NormalizedSourcePackage(input_file_name="sample.pdf", input_file_path="/tmp/sample.pdf"),
        document=NormalizedDocumentMetadata(document_id="doc-3", title="Quarterly Tasks", primary_language="en-US"),
        summary=NormalizedSummary(
            unit_count=3,
            review_item_count=0,
            table_count=0,
            unit_type_counts={"paragraph": 1, "list_item": 2},
            confidence_counts={"medium": 3},
        ),
        unit_entries=[
            NormalizedUnit(unit_id="p1", unit_type="paragraph", reading_order_index=1, page_numbers=[1], text="Quarterly Tasks", source_refs=["p1"], evidence_basis=["b1"]),
            NormalizedUnit(unit_id="l1", unit_type="list_item", reading_order_index=2, page_numbers=[1], text="1. Review filings", source_refs=["l1"], evidence_basis=["b2"]),
            NormalizedUnit(unit_id="l2", unit_type="list_item", reading_order_index=3, page_numbers=[1], text="2. Update disclosures", source_refs=["l2"], evidence_basis=["b3"]),
        ],
    )

    rendered = build_accessible_html(document)

    assert "<h1>Quarterly Tasks</h1>" in rendered
    assert "<p>Quarterly Tasks</p>" not in rendered
    assert "<ul>" in rendered
