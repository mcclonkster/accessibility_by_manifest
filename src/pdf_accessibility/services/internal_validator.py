from __future__ import annotations

from pathlib import Path

import pikepdf

from pdf_accessibility.models.state import ValidatorFinding, WritebackReport
from pdf_accessibility.utils.ids import stable_id


def validate_tagged_draft(pdf_path: Path, report: WritebackReport | None = None) -> list[ValidatorFinding]:
    findings: list[ValidatorFinding] = []
    try:
        with pikepdf.open(pdf_path) as pdf:
            findings.extend(_validate_catalog(pdf))
            findings.extend(_validate_report_consistency(pdf, report))
    except Exception as exc:  # noqa: BLE001 - validator must convert PDF failures into findings.
        findings.append(
            _finding(
                "PDF_OPEN_FAILED",
                "document",
                f"Draft PDF could not be opened: {exc}",
            )
        )
    return findings


def validator_report_payload(
    pdf_path: Path | None,
    findings: list[ValidatorFinding],
    *,
    skipped_reason: str | None = None,
) -> dict[str, object]:
    blocking = [finding for finding in findings if finding.blocking and not finding.resolved]
    draft_available = pdf_path is not None and pdf_path.exists()
    validation_state = "completed" if draft_available else "skipped"
    return {
        "validator": "internal_tagged_draft",
        "checked_path": str(pdf_path) if draft_available else None,
        "draft_available": draft_available,
        "validation_state": validation_state,
        "skipped_reason": None if draft_available else (skipped_reason or "no_tagged_draft_available"),
        "blocking_finding_count": len(blocking),
        "finding_count": len(findings),
        "passed": draft_available and not blocking,
        "findings": [finding.model_dump(mode="json") for finding in findings],
    }


def _validate_catalog(pdf: pikepdf.Pdf) -> list[ValidatorFinding]:
    findings: list[ValidatorFinding] = []
    root = pdf.Root
    if root.get("/MarkInfo") is None:
        findings.append(_finding("MARK_INFO_MISSING", "document", "Draft PDF catalog is missing /MarkInfo."))
    if root.get("/StructTreeRoot") is None:
        findings.append(_finding("STRUCT_TREE_ROOT_MISSING", "document", "Draft PDF catalog is missing /StructTreeRoot."))
    if root.get("/Lang") is None:
        findings.append(_finding("DOCUMENT_LANGUAGE_MISSING", "document", "Draft PDF catalog is missing /Lang."))
    if not str(pdf.docinfo.get("/Title", "")).strip():
        findings.append(_finding("DOCUMENT_TITLE_MISSING", "document", "Draft PDF Info dictionary is missing /Title."))
    return findings


def _validate_report_consistency(pdf: pikepdf.Pdf, report: WritebackReport | None) -> list[ValidatorFinding]:
    if report is None:
        return [_finding("WRITEBACK_REPORT_MISSING", "document", "Writeback report is missing for draft validation.")]
    findings: list[ValidatorFinding] = []
    marked_content_exists = _marked_content_exists(pdf)
    struct_tree = pdf.Root.get("/StructTreeRoot")
    parent_tree_exists = struct_tree is not None and struct_tree.get("/ParentTree") is not None
    if report.content_streams_modified and not marked_content_exists:
        findings.append(
            _finding(
                "MARKED_CONTENT_MISSING",
                "document",
                "Writeback report says content streams were modified, but no marked content was found.",
            )
        )
    if report.mcid_written_count > 0 and not parent_tree_exists:
        findings.append(
            _finding(
                "PARENT_TREE_MISSING",
                "document",
                "Writeback report says MCIDs were written, but /StructTreeRoot has no /ParentTree.",
            )
        )
    return findings


def _marked_content_exists(pdf: pikepdf.Pdf) -> bool:
    for page in pdf.pages:
        for data in _content_stream_bytes(page):
            if b"BDC" in data and b"EMC" in data and b"/MCID" in data:
                return True
    return False


def _content_stream_bytes(page) -> list[bytes]:
    contents = page.get("/Contents", None)
    if contents is None:
        return []
    if isinstance(contents, pikepdf.Array):
        return [stream.read_bytes() for stream in contents if hasattr(stream, "read_bytes")]
    if hasattr(contents, "read_bytes"):
        return [contents.read_bytes()]
    return []


def _finding(issue_code: str, target_ref: str, message: str, severity: str = "error") -> ValidatorFinding:
    return ValidatorFinding(
        finding_id=f"validator-{stable_id(issue_code, target_ref, message)}",
        target_ref=target_ref,
        message=message,
        severity=severity,
        blocking=severity == "error",
    )
