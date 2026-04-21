from __future__ import annotations

from datetime import datetime, timezone

import extracted_chat_artifacts.archive.docx_remediation_transformer as script2
import extracted_chat_artifacts.archive.pptx_extract_and_manifest as script1

from .config import WorkflowOptions
from .paths import DeckRun, Script1Paths, Script2Paths, script1_paths, script2_paths


def configure_script1(options: WorkflowOptions, run: DeckRun) -> Script1Paths:
    paths = script1_paths(run)

    script1.INPUT_PATH = str(run.pptx_path)
    script1.OUTPUT_DOCX_PATH = str(paths.companion_docx)
    script1.OUTPUT_JSON_MANIFEST_PATH = str(paths.manifest_json)
    script1.OUTPUT_YAML_MANIFEST_PATH = str(paths.manifest_yaml)
    script1.OUTPUT_EXTRACT_REPORT_PATH = str(paths.extract_report)
    script1.OUTPUT_REVIEW_NOTES_PATH = str(paths.review_notes)
    script1.OVERWRITE = options.overwrite
    script1.DRY_RUN = options.dry_run
    script1.PREVIEW_IMAGE_DIR = str(options.preview_dir) if options.preview_dir else ""
    script1.INCLUDE_PREVIEW_IMAGES = options.include_slide_images
    script1.AUTO_RENDER_SLIDE_IMAGES = options.auto_render_slide_images
    script1.TIMESTAMP_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    return paths


def configure_script2(options: WorkflowOptions, run: DeckRun, first_pass_paths: Script1Paths) -> Script2Paths:
    paths = script2_paths(run)

    script2.INPUT_DOCX_PATH = str(first_pass_paths.companion_docx)
    script2.INPUT_MANIFEST_JSON_PATH = str(first_pass_paths.manifest_json)
    script2.INPUT_REVIEW_NOTES_PATH = str(first_pass_paths.review_notes)
    script2.OUTPUT_DOCX_PATH = str(paths.remediated_docx)
    script2.OUTPUT_REMEDIATION_REPORT_PATH = str(paths.remediation_report)
    script2.OVERWRITE = options.overwrite
    script2.DRY_RUN = options.dry_run
    script2.SLIDE_IMAGE_DIR = str(options.preview_dir) if options.preview_dir else ""
    script2.REQUIRE_SLIDE_IMAGES = bool(options.require_slide_images and options.include_slide_images)

    return paths


def run_script1(options: WorkflowOptions, run: DeckRun) -> tuple[int, Script1Paths]:
    paths = configure_script1(options, run)
    return script1.main(), paths


def run_script2(options: WorkflowOptions, run: DeckRun, first_pass_paths: Script1Paths) -> int:
    configure_script2(options, run, first_pass_paths)
    return script2.main()
