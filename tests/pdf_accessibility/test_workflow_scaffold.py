from __future__ import annotations

import json
from pathlib import Path

import fitz
import pikepdf

from pdf_accessibility.graph.build_graph import build_workflow, langgraph_available
from pdf_accessibility.models.state import (
    BBox,
    Confidence,
    DocumentState,
    DocumentMetadataEvidence,
    DocumentStatus,
    FinalizationState,
    ImageEvidence,
    NormalizedUnit,
    PageGeometryEvidence,
    PageState,
    RegionState,
    RegionStatus,
    ReviewTask,
    TextBlockEvidence,
)
from pdf_accessibility.nodes import accessibility_review, region_proposal
from pdf_accessibility.persistence.runs import create_run, initial_document_state
from pdf_accessibility.persistence.artifacts import write_run_snapshot
from pdf_accessibility.reducers.apply_events import apply_events
from pdf_accessibility.services.manifest_bridge import BRIDGE_MARKER
from pdf_accessibility.utils.ids import stable_id
from pdf_accessibility.utils.json import write_json


def _write_one_page_pdf(path: Path) -> None:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Accessible PDF workflow scaffold")
    document.save(path)
    document.close()


def _write_ready_one_page_pdf(path: Path) -> None:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Annual Report")
    page.insert_text((72, 110), "A short accessible paragraph.")
    document.set_metadata({"title": "Annual Report"})
    document.save(path)
    document.close()
    with pikepdf.open(path, allow_overwriting_input=True) as pdf:
        pdf.Root["/Lang"] = pikepdf.String("en-US")
        pdf.save(path)


def test_langgraph_import_is_available() -> None:
    assert langgraph_available()


def test_workflow_scaffold_writes_required_artifacts(tmp_path: Path) -> None:
    source_pdf = tmp_path / "input.pdf"
    _write_one_page_pdf(source_pdf)
    context = create_run(source_pdf, tmp_path / "runs")
    document = initial_document_state(context)

    result = build_workflow().invoke({"document": document})
    final_document = result["document"]

    assert final_document.document_status is DocumentStatus.NEEDS_REVIEW
    assert final_document.finalization_state is FinalizationState.NEEDS_REVIEW
    assert final_document.page_count == 1
    assert final_document.pages[0].text_blocks
    assert final_document.normalized_units
    assert final_document.blocker_ids
    assert any(blocker_id.startswith(("review-", "finding-")) for blocker_id in final_document.blocker_ids)
    assert (context.run_dir / "document_state.json").exists()
    assert (context.run_dir / "normalized_structure.json").exists()
    assert (context.run_dir / "tagging_plan.json").exists()
    assert (context.run_dir / "structure_mapping_plan.json").exists()
    assert (context.run_dir / "review_tasks.json").exists()
    assert (context.run_dir / "review_decisions_template.json").exists()
    assert (context.run_dir / "operator_guide.json").exists()
    assert (context.run_dir / "finalization_status.json").exists()
    assert (context.run_dir / "status.json").exists()
    assert (context.run_dir / "manifest.json").exists()
    assert (context.run_dir / "metrics" / "summary.json").exists()
    assert (context.run_dir / "metrics" / "timings.csv").exists()
    assert (context.run_dir / "environment.txt").exists()
    assert (context.run_dir / "git.txt").exists()
    assert not (context.run_dir / "accessible_output.pdf").exists()

    run_log = json.loads((context.run_dir / "run_log.json").read_text(encoding="utf-8"))
    trace = {entry["node_name"]: entry for entry in run_log["workflow_trace"]}
    assert trace["write_tagged_draft"]["action"] == "skipped"
    assert trace["write_tagged_draft"]["duration_ms"] == 0
    assert "unresolved blockers" in trace["write_tagged_draft"]["reason"]
    assert trace["validator_check"]["action"] == "skipped"
    assert trace["human_review"]["action"] == "ran"
    assert trace["finalize_accessible_output"]["action"] == "ran"
    assert trace["ingest_pdf"]["duration_ms"] >= 0
    validator_payload = json.loads((context.run_dir / "validator_findings.json").read_text(encoding="utf-8"))
    assert validator_payload["checked_path"] is None
    assert validator_payload["draft_available"] is False
    assert validator_payload["validation_state"] == "skipped"
    assert validator_payload["passed"] is False
    template_payload = json.loads((context.run_dir / "review_decisions_template.json").read_text(encoding="utf-8"))
    assert template_payload["decision_count"] >= 1
    guide_payload = json.loads((context.run_dir / "operator_guide.json").read_text(encoding="utf-8"))
    assert guide_payload["primary_next_step"]["action"] == "fill_review_decisions"


def test_workflow_routes_through_draft_and_validator_when_ready(tmp_path: Path) -> None:
    source_pdf = tmp_path / "ready.pdf"
    _write_ready_one_page_pdf(source_pdf)
    context = create_run(source_pdf, tmp_path / "runs")
    document = initial_document_state(context)

    result = build_workflow().invoke({"document": document})
    final_document = result["document"]

    assert final_document.document_status is DocumentStatus.FINALIZED
    assert final_document.finalization_state is FinalizationState.FINALIZED
    assert (context.run_dir / "tagged_draft.pdf").exists()
    assert (context.run_dir / "validator_findings.json").exists()
    assert (context.run_dir / "accessible_output.pdf").exists()
    assert (context.run_dir / "accessible_output.html").exists()
    assert not (context.run_dir / "review_decisions_template.json").exists()
    assert (context.run_dir / "operator_guide.json").exists()
    assert (context.run_dir / "metrics" / "summary.json").exists()
    assert (context.run_dir / "metrics" / "timings.csv").exists()

    run_log = json.loads((context.run_dir / "run_log.json").read_text(encoding="utf-8"))
    trace = {entry["node_name"]: entry for entry in run_log["workflow_trace"]}
    assert trace["write_tagged_draft"]["action"] == "ran"
    assert trace["write_tagged_draft"]["duration_ms"] >= 0
    assert trace["validator_check"]["action"] == "ran"
    assert trace["human_review"]["action"] == "skipped"
    assert trace["finalize_accessible_output"]["action"] == "ran"
    assert trace["write_accessible_html"]["action"] == "ran"
    validator_payload = json.loads((context.run_dir / "validator_findings.json").read_text(encoding="utf-8"))
    assert validator_payload["checked_path"] == str(context.run_dir / "tagged_draft.pdf")
    assert validator_payload["draft_available"] is True
    assert validator_payload["validation_state"] == "completed"
    assert validator_payload["passed"] is True
    guide_payload = json.loads((context.run_dir / "operator_guide.json").read_text(encoding="utf-8"))
    assert guide_payload["primary_next_step"] is None
    html_payload = (context.run_dir / "accessible_output.html").read_text(encoding="utf-8")
    assert "<h1>Annual Report</h1>" in html_payload
    assert "<p>A short accessible paragraph.</p>" in html_payload


def test_workflow_can_finalize_after_file_based_review_decisions(tmp_path: Path) -> None:
    source_pdf = tmp_path / "needs_review.pdf"
    _write_one_page_pdf(source_pdf)
    context = create_run(source_pdf, tmp_path / "runs")
    write_json(
        context.run_dir / "review_decisions_input.json",
        [
            {
                "decision_id": f"decision-{stable_id('title')}",
                "target_review_task_id": f"review-{stable_id('DOCUMENT_TITLE_MISSING', 'document')}",
                "decision_type": "set_document_title",
                "value": "Filed Report Title",
                "reviewer": "test",
                "created_at": "2026-04-25T00:00:00Z",
            },
            {
                "decision_id": f"decision-{stable_id('language')}",
                "target_review_task_id": f"review-{stable_id('DOCUMENT_LANGUAGE_MISSING', 'document')}",
                "decision_type": "set_primary_language",
                "value": "en-US",
                "reviewer": "test",
                "created_at": "2026-04-25T00:00:00Z",
            },
        ],
    )
    document = initial_document_state(context)

    final_document = build_workflow().invoke({"document": document})["document"]

    assert final_document.document_status is DocumentStatus.FINALIZED
    assert final_document.finalization_state is FinalizationState.FINALIZED
    assert (context.run_dir / "review_decisions.json").exists()
    assert (context.run_dir / "tagged_draft.pdf").exists()
    assert (context.run_dir / "accessible_output.pdf").exists()
    assert (context.run_dir / "accessible_output.html").exists()
    assert not (context.run_dir / "review_decisions_template.json").exists()
    validator_payload = json.loads((context.run_dir / "validator_findings.json").read_text(encoding="utf-8"))
    assert validator_payload["draft_available"] is True
    assert validator_payload["validation_state"] == "completed"
    assert validator_payload["passed"] is True


def test_workflow_does_not_register_final_output_without_legal_finalization(tmp_path: Path) -> None:
    source_pdf = tmp_path / "ready.pdf"
    _write_ready_one_page_pdf(source_pdf)
    context = create_run(source_pdf, tmp_path / "runs")
    document = initial_document_state(context)

    final_document = build_workflow().invoke({"document": document})["document"]

    assert final_document.output_artifacts.accessible_output_pdf is not None
    assert final_document.output_artifacts.accessible_output_html is not None
    assert (context.run_dir / "accessible_output.pdf").exists()
    assert (context.run_dir / "accessible_output.html").exists()
    artifact_manifest = json.loads((context.run_dir / "artifact_manifest.json").read_text(encoding="utf-8"))
    artifact_names = [record["name"] for record in artifact_manifest["records"]]
    assert "accessible_output.pdf" in artifact_names
    assert "accessible_output.html" in artifact_names


def test_shared_bridge_figure_review_expands_summary_into_actionable_tasks(tmp_path: Path) -> None:
    source_pdf = tmp_path / "figures.pdf"
    _write_one_page_pdf(source_pdf)
    document = DocumentState(
        document_id="doc-1",
        source_path=source_pdf,
        run_dir=tmp_path,
        metadata=DocumentMetadataEvidence(
            title="Figure Review Report",
            primary_language="en-US",
            provenance={"bridge_marker": BRIDGE_MARKER},
        ),
        review_tasks=[
            ReviewTask(
                task_id="task-summary",
                issue_code="FIGURE_CANDIDATES_REQUIRE_REVIEW",
                severity="warning",
                target_ref="document_summary.figure_candidate_count",
                reason="Figure candidates require review.",
                blocking=True,
                confidence_context={"figure_candidate_count": 2},
            )
        ],
        normalized_units=[
            NormalizedUnit(unit_id="figure-1", unit_type="figure", page_numbers=[1], reading_order_index=0),
            NormalizedUnit(unit_id="figure-2", unit_type="figure", page_numbers=[2], reading_order_index=1),
        ],
        pages=[
            PageState(
                page_number=1,
                geometry=PageGeometryEvidence(width=1000, height=1000),
                regions=[
                    RegionState(
                        region_id="region-figure-1",
                        page_number=1,
                        bbox=BBox(left=0, top=0, right=400, bottom=400),
                        status=RegionStatus.ACCESSIBILITY_REVIEWED,
                        current_role="figure_candidate",
                        confidence=Confidence.MEDIUM,
                    )
                ],
            ),
            PageState(
                page_number=2,
                geometry=PageGeometryEvidence(width=1000, height=1000),
                text_blocks=[
                    TextBlockEvidence(
                        block_id="text-1",
                        page_number=2,
                        bbox=BBox(left=0, top=0, right=100, bottom=30),
                        text="Page text",
                        source_ref="source-text-1",
                    )
                ],
                regions=[
                    RegionState(
                        region_id="region-figure-2",
                        page_number=2,
                        bbox=BBox(left=0, top=0, right=80, bottom=80),
                        status=RegionStatus.ACCESSIBILITY_REVIEWED,
                        current_role="figure_candidate",
                        confidence=Confidence.MEDIUM,
                    )
                ],
            ),
        ],
    )

    updated = apply_events(document, accessibility_review.run(document))

    figure_tasks = [task for task in updated.review_tasks if task.issue_code.startswith("FIGURE_ALT_TEXT")]
    assert {task.issue_code for task in figure_tasks} == {"FIGURE_ALT_TEXT_REQUIRED", "FIGURE_ALT_TEXT_SPOT_CHECK"}
    assert not next(task for task in updated.review_tasks if task.task_id == "task-summary").resolved

    rerun = apply_events(updated, accessibility_review.run(updated))

    rerun_figure_tasks = [task for task in rerun.review_tasks if task.issue_code.startswith("FIGURE_ALT_TEXT")]
    assert len(rerun_figure_tasks) == 2

    updated.finalization_state = FinalizationState.NEEDS_REVIEW
    write_run_snapshot(updated)
    template_payload = json.loads((tmp_path / "review_decisions_template.json").read_text(encoding="utf-8"))
    assert {entry["issue_code"] for entry in template_payload["decisions"]} == {
        "FIGURE_ALT_TEXT_REQUIRED",
        "FIGURE_ALT_TEXT_SPOT_CHECK",
    }
    assert all(entry["issue_code"] != "FIGURE_CANDIDATES_REQUIRE_REVIEW" for entry in template_payload["manual_only_tasks"])


def test_shared_bridge_region_proposal_adds_missing_figure_regions_from_images(tmp_path: Path) -> None:
    source_pdf = tmp_path / "figures.pdf"
    _write_one_page_pdf(source_pdf)
    document = DocumentState(
        document_id="doc-1",
        source_path=source_pdf,
        run_dir=tmp_path,
        metadata=DocumentMetadataEvidence(
            title="Figure Review Report",
            primary_language="en-US",
            provenance={"bridge_marker": BRIDGE_MARKER},
        ),
        normalized_units=[NormalizedUnit(unit_id="paragraph-1", unit_type="paragraph", page_numbers=[1], reading_order_index=0)],
        review_tasks=[
            ReviewTask(
                task_id="task-summary",
                issue_code="FIGURE_CANDIDATES_REQUIRE_REVIEW",
                severity="warning",
                target_ref="document_summary.figure_candidate_count",
                reason="Figure candidates require review.",
                blocking=True,
                confidence_context={"figure_candidate_count": 1},
            )
        ],
        pages=[
            PageState(
                page_number=1,
                geometry=PageGeometryEvidence(width=1000, height=1000),
                images=[
                    ImageEvidence(
                        image_id="image-1",
                        page_number=1,
                        bbox=BBox(left=0, top=0, right=400, bottom=400),
                        source_ref="pymupdf:page:1:image:1",
                    )
                ],
                regions=[
                    RegionState(
                        region_id="region-paragraph-1",
                        page_number=1,
                        bbox=BBox(left=0, top=450, right=500, bottom=550),
                        status=RegionStatus.ACCESSIBILITY_REVIEWED,
                        current_role="paragraph_candidate",
                        confidence=Confidence.MEDIUM,
                        source_refs=["source-text-1"],
                    )
                ],
            )
        ],
    )

    augmented = apply_events(document, region_proposal.run(document))
    review_updated = apply_events(augmented, accessibility_review.run(augmented))

    figure_regions = [region for page in review_updated.pages for region in page.regions if region.current_role == "figure_candidate"]
    figure_tasks = [task for task in review_updated.review_tasks if task.issue_code.startswith("FIGURE_ALT_TEXT")]

    assert len(figure_regions) == 1
    assert len(figure_tasks) == 1
    assert figure_tasks[0].target_ref == figure_regions[0].region_id
