from __future__ import annotations

import argparse
from pathlib import Path

from .config import WorkflowOptions
from .dependencies import check_dependencies
from .paths import DeckRun, discover_pptx_files, plan_runs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert one PPTX or a folder of PPTX files into image-retaining accessible DOCX workflow outputs.",
    )
    parser.add_argument("input", type=Path, help="Path to a source .pptx file or a folder containing .pptx files.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=(
            "Output folder. For one file, outputs go directly here. For a folder input, "
            "one '<deck>_workflow_output' subfolder is created per deck. Defaults next to each PPTX."
        ),
    )
    parser.add_argument(
        "--preview-dir",
        type=Path,
        default=None,
        help=(
            "Optional folder of pre-exported slide images for a single PPTX. "
            "If omitted, Script 1 renders slide images automatically."
        ),
    )
    parser.add_argument(
        "--no-recursive",
        action="store_true",
        help="For folder input, only process PPTX files directly inside that folder.",
    )
    parser.add_argument(
        "--no-slide-images",
        action="store_true",
        help="Do not render or insert slide images. Text extraction still runs.",
    )
    parser.add_argument(
        "--script1-only",
        action="store_true",
        help="Only run extraction/manifest generation. Do not run the remediation pass.",
    )
    parser.add_argument(
        "--require-slide-images",
        action="store_true",
        help="Treat missing slide images as critical warnings in Script 2.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing generated outputs.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and build in memory without writing files.",
    )
    return parser


def options_from_args(args: argparse.Namespace) -> WorkflowOptions:
    return WorkflowOptions(
        input_path=args.input.expanduser().resolve(),
        output_root=args.output_dir.expanduser().resolve() if args.output_dir else None,
        preview_dir=args.preview_dir.expanduser().resolve() if args.preview_dir else None,
        recursive=not args.no_recursive,
        include_slide_images=not args.no_slide_images,
        script1_only=args.script1_only,
        require_slide_images=args.require_slide_images,
        overwrite=args.overwrite,
        dry_run=args.dry_run,
    )


def validate_options(parser: argparse.ArgumentParser, options: WorkflowOptions) -> None:
    if not options.input_path.exists():
        parser.error(f"input path does not exist: {options.input_path}")

    if options.preview_dir:
        if not options.preview_dir.exists() or not options.preview_dir.is_dir():
            parser.error(f"--preview-dir must be an existing folder: {options.preview_dir}")
        if options.input_path.is_dir():
            parser.error("--preview-dir is only supported when processing a single PPTX file.")

    report = check_dependencies(options)
    if not report.ok:
        parser.error("Dependency check failed:\n- " + "\n- ".join(report.errors))


def run_deck(options: WorkflowOptions, run: DeckRun, index: int, total: int) -> int:
    from .legacy_backend import run_script1, run_script2

    print(f"\n=== [{index}/{total}] {run.pptx_path} ===")
    print(f"Output folder: {run.output_dir}")

    if not options.dry_run:
        run.output_dir.mkdir(parents=True, exist_ok=True)

    script1_result, first_pass_paths = run_script1(options, run)
    if script1_result != 0:
        return script1_result

    if options.script1_only:
        return script1_result

    return run_script2(options, run, first_pass_paths)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    options = options_from_args(args)
    validate_options(parser, options)

    pptx_files = discover_pptx_files(options.input_path, recursive=options.recursive)
    if not pptx_files:
        parser.error(f"no .pptx files found at: {options.input_path}")

    if options.output_root is not None and not options.dry_run:
        options.output_root.mkdir(parents=True, exist_ok=True)

    runs = plan_runs(pptx_files, options.input_path, options.output_root)
    print(f"Found {len(runs)} PPTX file(s).")

    failures: list[tuple[Path, int]] = []
    for index, run in enumerate(runs, start=1):
        result = run_deck(options, run, index, len(runs))
        if result != 0:
            failures.append((run.pptx_path, result))

    if failures:
        print("\nWorkflow completed with failures:")
        for pptx_path, result in failures:
            print(f"- exit {result}: {pptx_path}")
        return 1

    print("\nWorkflow completed successfully.")
    return 0
