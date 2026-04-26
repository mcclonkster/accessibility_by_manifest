from __future__ import annotations

from pathlib import Path
from typing import Any

from pdf_accessibility.models.state import ReviewTask
from pdf_accessibility.utils.ids import stable_id


def build_ocr_recovery_template(review_tasks: list[ReviewTask], *, source_path: Path) -> dict[str, Any]:
    page_recoveries: list[dict[str, Any]] = []
    for task in review_tasks:
        if task.resolved or task.issue_code != "IMAGE_ONLY_PAGE_OCR_REQUIRED":
            continue
        page_number = _page_number_from_target_ref(task.target_ref)
        if page_number is None:
            continue
        page_recoveries.append(
            {
                "template_id": f"ocr-template-{stable_id(task.task_id, page_number)}",
                "target_review_task_id": task.task_id,
                "issue_code": task.issue_code,
                "page_number": page_number,
                "text": "",
                "note": "Provide trusted OCR recovery text for this page. Leave no placeholder text in the final file.",
            }
        )

    page_recoveries.sort(key=lambda item: int(item["page_number"]))
    return {
        "source_review_tasks_path": str(source_path),
        "page_recovery_count": len(page_recoveries),
        "notes": [
            "Fill in page_recoveries[].text before using this file with --ocr-recovery.",
            "Use only trusted recovered text for image-only pages that actually need OCR recovery.",
        ],
        "page_recoveries": page_recoveries,
    }


def _page_number_from_target_ref(target_ref: str) -> int | None:
    prefix = "page:"
    if not target_ref.startswith(prefix):
        return None
    suffix = target_ref[len(prefix) :].strip()
    if not suffix.isdigit():
        return None
    page_number = int(suffix)
    return page_number if page_number > 0 else None
