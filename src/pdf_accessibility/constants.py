from __future__ import annotations


FROZEN_NODE_NAMES = (
    "ingest_pdf",
    "render_pages",
    "region_proposal",
    "vision_analysis",
    "ocr_layout_analysis",
    "native_pdf_analysis",
    "accessibility_review",
    "artifact_check",
    "caption_association",
    "tagging_plan",
    "document_consistency",
    "structure_mapping_plan",
    "behavior_check",
    "approval_gate",
    "write_tagged_draft",
    "validator_check",
    "human_review",
    "apply_review_decisions",
    "finalize_accessible_output",
    "workflow_orchestrator",
)

REQUIRED_ARTIFACT_NAMES = (
    "input.pdf",
    "document_state.json",
    "findings.jsonl",
    "review_tasks.json",
    "run_log.json",
)

PDF_OUTPUT_ARTIFACT_NAMES = (
    "tagged_draft.pdf",
    "validator_findings.json",
    "finalization_status.json",
    "accessible_output.pdf",
    "accessible_output.html",
    "artifact_manifest.json",
)
