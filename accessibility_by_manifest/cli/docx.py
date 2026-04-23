from __future__ import annotations

import argparse
from pathlib import Path

from accessibility_by_manifest.inputs.docx.config import DocxManifestConfig
from accessibility_by_manifest.inputs.docx.paths import discover_docx_files, plan_runs
from accessibility_by_manifest.pipelines.docx import DocxManifestResult, run_docx


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract DOCX evidence into a v0.1 manifest.")
    parser.add_argument("input", type=Path, help="A .docx file or a folder containing .docx files.")
    parser.add_argument("--output-dir", type=Path, default=None, help="Output folder. Folder input creates one subfolder per DOCX.")
    parser.add_argument("--no-recursive", action="store_true", help="Only scan the top level of a folder input.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing manifest outputs.")
    parser.add_argument("--dry-run", action="store_true", help="Extract without writing outputs.")
    parser.add_argument(
        "--include-rebuild-payloads",
        action="store_true",
        help="Inline raw DOCX package XML and binary payloads in the manifest. Off by default because it can make very large JSON files.",
    )
    return parser


def config_from_args(args: argparse.Namespace) -> DocxManifestConfig:
    return DocxManifestConfig(
        input_path=args.input.expanduser().resolve(),
        output_root=args.output_dir.expanduser().resolve() if args.output_dir else None,
        recursive=not args.no_recursive,
        overwrite=args.overwrite,
        dry_run=args.dry_run,
        include_rebuild_payloads=args.include_rebuild_payloads,
    )


def print_result(result: DocxManifestResult, index: int, total: int) -> None:
    status = "SUCCESS" if result.ok else "FAILURE"
    print(f"\n=== [{index}/{total}] {result.run.docx_path} ===")
    print(f"Status: {status}")
    print(f"Message: {result.message}")
    print(f"Output folder: {result.run.output_dir}")
    print(f"Log file: {result.output_paths.log_file}")
    print(f"Manifest JSON: {result.output_paths.manifest_json}")
    print(f"Normalized IR JSON: {result.output_paths.normalized_manifest_json}")
    if result.manifest:
        summary = result.manifest["document_summary"]
        print(f"Paragraphs: {summary['paragraph_count']}")
        print(f"Tables: {summary['table_count']}")
        print(f"Images: {summary['image_count']}")
        print(f"Headers: {summary['header_count']}")
        print(f"Footers: {summary['footer_count']}")
        print(f"Rebuild payloads included: {summary['rebuild_payloads_included']}")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    config = config_from_args(args)
    if not config.input_path.exists():
        parser.error(f"input path does not exist: {config.input_path}")

    docx_files = discover_docx_files(config.input_path, config.recursive)
    if not docx_files:
        parser.error(f"no .docx files found at: {config.input_path}")

    runs = plan_runs(docx_files, config.input_path, config.output_root)
    print(f"Found {len(runs)} DOCX file(s).")
    results = [run_docx(config, run) for run in runs]
    for index, result in enumerate(results, start=1):
        print_result(result, index, len(results))

    failures = [result for result in results if not result.ok]
    if failures:
        print("\nDOCX manifest extraction completed with failures.")
        return 1
    print("\nDOCX manifest extraction completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
