from __future__ import annotations

from pathlib import Path

from pdf_accessibility.models.state import (
    BBox,
    Confidence,
    DocumentMetadataEvidence,
    DocumentState,
    NormalizedUnit,
    PageState,
    RegionState,
    RegionStatus,
)
from pdf_accessibility.nodes import behavior_check, structure_mapping_plan
from pdf_accessibility.persistence.artifacts import write_run_snapshot
from pdf_accessibility.reducers.apply_events import apply_events


def _document(tmp_path: Path, units: list[NormalizedUnit]) -> DocumentState:
    return DocumentState(
        document_id="doc-1",
        source_path=tmp_path / "input.pdf",
        run_dir=tmp_path,
        metadata=DocumentMetadataEvidence(title="Annual Report", primary_language="en-US"),
        page_count=1,
        pages=[
            PageState(
                page_number=1,
                regions=[
                    RegionState(
                        region_id="region-1",
                        page_number=1,
                        status=RegionStatus.STRUCTURE_PLANNED,
                    )
                ],
            )
        ],
        normalized_units=units,
    )


def test_paragraph_heading_and_artifact_mapping(tmp_path: Path) -> None:
    document = _document(
        tmp_path,
        [
            NormalizedUnit(
                unit_id="heading-1",
                unit_type="heading",
                page_numbers=[1],
                bbox=BBox(left=72, top=72, right=300, bottom=92),
                reading_order_index=0,
            ),
            NormalizedUnit(
                unit_id="paragraph-1",
                unit_type="paragraph",
                page_numbers=[1],
                bbox=BBox(left=72, top=110, right=420, bottom=160),
                reading_order_index=1,
            ),
            NormalizedUnit(
                unit_id="artifact-1",
                unit_type="artifact",
                page_numbers=[1],
                bbox=BBox(left=72, top=760, right=120, bottom=780),
                reading_order_index=None,
            ),
        ],
    )

    updated = apply_events(document, structure_mapping_plan.run(document))
    plan = updated.structure_mapping_plan

    assert plan is not None
    roles = {element.unit_id: element.pdf_structure_role for element in plan.elements}
    assert roles["heading-1"] == "H"
    assert roles["paragraph-1"] == "P"
    artifact = next(element for element in plan.elements if element.unit_id == "artifact-1")
    assert artifact.pdf_structure_role == "Artifact"
    assert artifact.artifact
    assert not artifact.include_in_structure_tree
    assert artifact.mcid is None
    assert "artifact-1" not in plan.reading_order_unit_ids
    heading = next(element for element in plan.elements if element.unit_id == "heading-1")
    paragraph = next(element for element in plan.elements if element.unit_id == "paragraph-1")
    assert heading.mcid == 0
    assert paragraph.mcid == 1
    assert heading.marked_content_ref == "page:1:mcid:0"
    assert paragraph.marked_content_ref == "page:1:mcid:1"
    assert len(plan.parent_tree_entries) == 2
    assert not plan.content_streams_modified


def test_table_and_figure_remain_unresolved_review_gated(tmp_path: Path) -> None:
    document = _document(
        tmp_path,
        [
            NormalizedUnit(
                unit_id="table-1",
                unit_type="table",
                page_numbers=[1],
                confidence=Confidence.MEDIUM,
                reading_order_index=0,
            ),
            NormalizedUnit(
                unit_id="figure-1",
                unit_type="figure",
                page_numbers=[1],
                confidence=Confidence.MEDIUM,
                reading_order_index=1,
            ),
        ],
    )

    updated = apply_events(document, structure_mapping_plan.run(document))
    plan = updated.structure_mapping_plan

    assert plan is not None
    assert set(plan.unresolved_unit_ids) == {"table-1", "figure-1"}
    assert all(element.review_required for element in plan.elements)
    assert all(element.mcid is None for element in plan.elements)


def test_behavior_check_flags_missing_mapping_plan(tmp_path: Path) -> None:
    document = _document(tmp_path, [])

    updated = apply_events(document, behavior_check.run(document))

    assert any(task.issue_code == "STRUCTURE_MAPPING_PLAN_MISSING" for task in updated.review_tasks)
    assert updated.blocker_ids


def test_structure_mapping_plan_json_is_written(tmp_path: Path) -> None:
    document = _document(
        tmp_path,
        [
            NormalizedUnit(
                unit_id="paragraph-1",
                unit_type="paragraph",
                page_numbers=[1],
                reading_order_index=0,
            )
        ],
    )
    updated = apply_events(document, structure_mapping_plan.run(document))

    write_run_snapshot(updated)

    assert (tmp_path / "structure_mapping_plan.json").exists()
