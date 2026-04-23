from __future__ import annotations

from pathlib import Path

from pdf_accessibility.models.state import (
    BBox,
    Confidence,
    DocumentMetadataEvidence,
    DocumentState,
    NormalizedUnit,
    PageGeometryEvidence,
    PageState,
    RegionState,
    RegionStatus,
    TextBlockEvidence,
)
from pdf_accessibility.nodes import accessibility_review, artifact_check
from pdf_accessibility.reducers.apply_events import apply_events
from pdf_accessibility.utils.ids import stable_id


def _document(tmp_path: Path, text: str, role: str = "table_candidate") -> DocumentState:
    block = TextBlockEvidence(
        block_id="text-1",
        page_number=1,
        bbox=BBox(left=72, top=72, right=420, bottom=180),
        text=text,
        source_ref="pymupdf:page:1:block:0",
        font_sizes=[10.0],
    )
    return DocumentState(
        document_id="doc-1",
        source_path=tmp_path / "input.pdf",
        run_dir=tmp_path,
        metadata=DocumentMetadataEvidence(title="Test", primary_language="en-US"),
        page_count=1,
        pages=[
            PageState(
                page_number=1,
                geometry=PageGeometryEvidence(width=612, height=792),
                text_blocks=[block],
                regions=[
                    RegionState(
                        region_id="region-text-1",
                        page_number=1,
                        bbox=block.bbox,
                        status=RegionStatus.EVIDENCE_COLLECTED,
                        current_role=role,
                        confidence=Confidence.MEDIUM,
                        source_refs=[block.source_ref],
                    )
                ],
            )
        ],
    )


def test_simple_table_candidate_is_warning_not_blocking(tmp_path: Path) -> None:
    document = _document(tmp_path, "Label    2025\nRevenue  12\nExpense  8")

    updated = apply_events(document, accessibility_review.run(document))
    table_tasks = [task for task in updated.review_tasks if task.issue_code == "TABLE_STRUCTURE_SPOT_CHECK"]

    assert table_tasks
    assert not table_tasks[0].blocking
    assert "TABLE_STRUCTURE_SPOT_CHECK" not in _blocking_issue_codes(updated)


def test_complex_table_candidate_is_blocking(tmp_path: Path) -> None:
    document = _document(
        tmp_path,
        "\n".join(
            [
                "Fund    2021    2022    2023",
                "A       10      11      12",
                "B       20      21      22",
                "C       30      31      32",
                "D       40      41      42",
                "E       50      51      52",
                "F       60      61      62",
                "G       70      71      72",
            ]
        ),
    )

    updated = apply_events(document, accessibility_review.run(document))

    assert "TABLE_HEADERS_UNCERTAIN" in _blocking_issue_codes(updated)


def test_artifact_check_replaces_existing_unit_for_same_source(tmp_path: Path) -> None:
    document = _document(tmp_path, "Page 1", role="page_number_or_footer_candidate")
    block = document.pages[0].text_blocks[0]
    unit_id = f"unit-{stable_id(f'region-{block.block_id}')}"
    document.normalized_units = [
        NormalizedUnit(
            unit_id=unit_id,
            unit_type="paragraph",
            page_numbers=[1],
            bbox=block.bbox,
            text=block.text,
            source_refs=[block.source_ref],
        )
    ]

    updated = apply_events(document, artifact_check.run(document))

    assert len(updated.normalized_units) == 1
    assert updated.normalized_units[0].unit_type == "artifact"
    assert not any(task.issue_code.startswith("ARTIFACT") for task in updated.review_tasks)


def _blocking_issue_codes(document: DocumentState) -> set[str]:
    return {task.issue_code for task in document.review_tasks if task.blocking and not task.resolved}

