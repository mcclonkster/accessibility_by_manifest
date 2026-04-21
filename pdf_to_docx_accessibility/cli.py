from __future__ import annotations

import argparse
from pathlib import Path

from .config import PdfWorkflowConfig
from .paths import discover_pdf_files, plan_runs
from .pipeline import PdfDeckResult, run_pdf


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract PDF accessibility evidence into a v0.1 PDF-to-DOCX manifest.")
    parser.add_argument("input", type=Path, help="A .pdf file or a folder containing .pdf files.")
    parser.add_argument("--output-dir", type=Path, default=None, help="Output folder. Folder input creates one subfolder per PDF.")
    parser.add_argument("--no-recursive", action="store_true", help="Only scan the top level of a folder input.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing manifest outputs.")
    parser.add_argument("--dry-run", action="store_true", help="Extract and validate without writing outputs.")
    return parser


def config_from_args(args: argparse.Namespace) -> PdfWorkflowConfig:
    return PdfWorkflowConfig(
        input_path=args.input.expanduser().resolve(),
        output_root=args.output_dir.expanduser().resolve() if args.output_dir else None,
        recursive=not args.no_recursive,
        overwrite=args.overwrite,
        dry_run=args.dry_run,
    )


def print_result(result: PdfDeckResult, index: int, total: int) -> None:
    status = "SUCCESS" if result.ok else "FAILURE"
    print(f"\n=== [{index}/{total}] {result.run.pdf_path} ===")
    print(f"Status: {status}")
    print(f"Message: {result.message}")
    print(f"Output folder: {result.run.output_dir}")
    print(f"Manifest JSON: {result.output_paths.manifest_json}")
    if result.manifest:
        summary = result.manifest["document_summary"]
        accessibility = result.manifest["document_accessibility"]
        print(f"Pages processed: {summary['total_pages']}")
        print(f"Raw blocks: {summary['raw_block_count']}")
        print(f"Annotations: {summary['annotation_count']}")
        print(f"Image-only pages present: {accessibility['image_only_pages_present']}")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    config = config_from_args(args)
    if not config.input_path.exists():
        parser.error(f"input path does not exist: {config.input_path}")

    pdf_files = discover_pdf_files(config.input_path, config.recursive)
    if not pdf_files:
        parser.error(f"no .pdf files found at: {config.input_path}")

    runs = plan_runs(pdf_files, config.input_path, config.output_root)
    print(f"Found {len(runs)} PDF file(s).")
    results = [run_pdf(config, run) for run in runs]
    for index, result in enumerate(results, start=1):
        print_result(result, index, len(results))

    failures = [result for result in results if not result.ok]
    if failures:
        print("\nWorkflow completed with failures.")
        return 1
    print("\nWorkflow completed successfully.")
    return 0
