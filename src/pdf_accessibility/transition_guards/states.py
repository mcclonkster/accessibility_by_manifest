from __future__ import annotations

from pdf_accessibility.models.state import DocumentStatus, FinalizationState, RegionStatus


REGION_TRANSITIONS: dict[RegionStatus, set[RegionStatus]] = {
    RegionStatus.UNSEEN: {RegionStatus.EVIDENCE_COLLECTED, RegionStatus.ESCALATED},
    RegionStatus.EVIDENCE_COLLECTED: {RegionStatus.MEANING_INFERRED, RegionStatus.ESCALATED},
    RegionStatus.MEANING_INFERRED: {RegionStatus.ACCESSIBILITY_REVIEWED, RegionStatus.ESCALATED},
    RegionStatus.ACCESSIBILITY_REVIEWED: {RegionStatus.STRUCTURE_PLANNED, RegionStatus.ESCALATED},
    RegionStatus.STRUCTURE_PLANNED: {RegionStatus.MAPPING_PLANNED, RegionStatus.ESCALATED},
    RegionStatus.MAPPING_PLANNED: {RegionStatus.BEHAVIOR_CHECKED, RegionStatus.ESCALATED},
    RegionStatus.BEHAVIOR_CHECKED: {RegionStatus.COMMITTABLE, RegionStatus.ESCALATED},
    RegionStatus.COMMITTABLE: {RegionStatus.WRITTEN_TO_DRAFT, RegionStatus.ESCALATED},
    RegionStatus.WRITTEN_TO_DRAFT: {RegionStatus.VALIDATED, RegionStatus.ESCALATED},
    RegionStatus.VALIDATED: {RegionStatus.COMPLETE, RegionStatus.ESCALATED},
    RegionStatus.ESCALATED: {
        RegionStatus.EVIDENCE_COLLECTED,
        RegionStatus.MEANING_INFERRED,
        RegionStatus.ACCESSIBILITY_REVIEWED,
        RegionStatus.STRUCTURE_PLANNED,
        RegionStatus.MAPPING_PLANNED,
        RegionStatus.BEHAVIOR_CHECKED,
        RegionStatus.COMMITTABLE,
        RegionStatus.COMPLETE,
    },
    RegionStatus.COMPLETE: set(),
}


WORKFLOW_TRANSITIONS: dict[DocumentStatus, set[DocumentStatus]] = {
    DocumentStatus.PENDING: {DocumentStatus.EVIDENCE_IN_PROGRESS, DocumentStatus.WRITE_BLOCKED},
    DocumentStatus.EVIDENCE_IN_PROGRESS: {
        DocumentStatus.PLANNING_IN_PROGRESS,
        DocumentStatus.NEEDS_REVIEW,
        DocumentStatus.WRITE_BLOCKED,
    },
    DocumentStatus.PLANNING_IN_PROGRESS: {
        DocumentStatus.DRAFT_READY,
        DocumentStatus.NEEDS_REVIEW,
        DocumentStatus.WRITE_BLOCKED,
    },
    DocumentStatus.DRAFT_READY: {
        DocumentStatus.DRAFT_WRITTEN,
        DocumentStatus.NEEDS_REVIEW,
        DocumentStatus.WRITE_BLOCKED,
    },
    DocumentStatus.DRAFT_WRITTEN: {DocumentStatus.VALIDATED, DocumentStatus.NEEDS_REVIEW, DocumentStatus.WRITE_BLOCKED},
    DocumentStatus.VALIDATED: {DocumentStatus.FINALIZED, DocumentStatus.NEEDS_REVIEW, DocumentStatus.REVIEW_APPLIED},
    DocumentStatus.NEEDS_REVIEW: {DocumentStatus.REVIEW_APPLIED, DocumentStatus.WRITE_BLOCKED},
    DocumentStatus.REVIEW_APPLIED: {DocumentStatus.DRAFT_READY, DocumentStatus.VALIDATED, DocumentStatus.FINALIZED},
    DocumentStatus.WRITE_BLOCKED: {DocumentStatus.NEEDS_REVIEW, DocumentStatus.REVIEW_APPLIED},
    DocumentStatus.FINALIZED: set(),
}


FINALIZATION_TRANSITIONS: dict[FinalizationState, set[FinalizationState]] = {
    FinalizationState.PENDING: {
        FinalizationState.NEEDS_REVIEW,
        FinalizationState.WRITE_BLOCKED,
        FinalizationState.FINALIZED,
    },
    FinalizationState.NEEDS_REVIEW: {FinalizationState.PENDING, FinalizationState.WRITE_BLOCKED, FinalizationState.FINALIZED},
    FinalizationState.WRITE_BLOCKED: {FinalizationState.NEEDS_REVIEW, FinalizationState.PENDING},
    FinalizationState.FINALIZED: set(),
}


def can_transition_region(current: RegionStatus, new: RegionStatus) -> bool:
    return current == new or new in REGION_TRANSITIONS[current]


def can_transition_workflow(current: DocumentStatus, new: DocumentStatus) -> bool:
    return current == new or new in WORKFLOW_TRANSITIONS[current]


def can_transition_finalization(current: FinalizationState, new: FinalizationState) -> bool:
    return current == new or new in FINALIZATION_TRANSITIONS[current]

