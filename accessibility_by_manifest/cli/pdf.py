from __future__ import annotations

import argparse
from pathlib import Path

from accessibility_by_manifest.inputs.pdf.config import PdfManifestConfig
from accessibility_by_manifest.inputs.pdf.paths import discover_pdf_files, plan_runs
from accessibility_by_manifest.pipelines.pdf import PdfManifestResult, run_pdf


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract PDF accessibility evidence into a v0.1 manifest.")
    parser.add_argument("input", type=Path, help="A .pdf file or a folder containing .pdf files.")
    parser.add_argument("--output-dir", type=Path, default=None, help="Output folder. Folder input creates one subfolder per PDF.")
    parser.add_argument("--no-recursive", action="store_true", help="Only scan the top level of a folder input.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing manifest outputs.")
    parser.add_argument("--dry-run", action="store_true", help="Extract and validate without writing outputs.")
    parser.add_argument("--ai-parser", choices=("none", "docling"), default="none", help="Optional whole-document AI parser sidecar.")
    parser.add_argument(
        "--ocr-parser",
        choices=("none", "doctr"),
        default="none",
        help="Optional targeted OCR sidecar for image-only pages.",
    )
    parser.add_argument(
        "--ai-parser-output-mode",
        choices=("artifacts",),
        default="artifacts",
        help="How optional AI parser sidecar outputs are written.",
    )
    parser.add_argument(
        "--include-rebuild-payloads",
        action="store_true",
        help="Inline heavier raw PDF-native extractor payloads for debug/rebuild analysis.",
    )
    parser.add_argument(
        "--include-char-level-evidence",
        action="store_true",
        help="Include pdfminer.six per-character evidence in text items.",
    )
    return parser


def config_from_args(args: argparse.Namespace) -> PdfManifestConfig:
    return PdfManifestConfig(
        input_path=args.input.expanduser().resolve(),
        output_root=args.output_dir.expanduser().resolve() if args.output_dir else None,
        recursive=not args.no_recursive,
        overwrite=args.overwrite,
        dry_run=args.dry_run,
        ai_parser=args.ai_parser,
        ai_parser_output_mode=args.ai_parser_output_mode,
        ocr_parser=args.ocr_parser,
        include_rebuild_payloads=args.include_rebuild_payloads,
        include_char_level_evidence=args.include_char_level_evidence,
    )


def print_result(result: PdfManifestResult, index: int, total: int) -> None:
    status = "SUCCESS" if result.ok else "FAILURE"
    print(f"\n=== [{index}/{total}] {result.run.pdf_path} ===")
    print(f"Status: {status}")
    print(f"Message: {result.message}")
    print(f"Output folder: {result.run.output_dir}")
    print(f"Log file: {result.output_paths.log_file}")
    print(f"Manifest JSON: {result.output_paths.manifest_json}")
    print(f"Draft DOCX: {result.output_paths.projected_docx}")
    print(f"Extractor manifests: {result.output_paths.extractor_manifest_dir}")
    if result.output_paths.adobe_reference_comparison_json.exists():
        print(f"Adobe reference comparison: {result.output_paths.adobe_reference_comparison_json}")
    if result.manifest and result.manifest.get("extractor_evidence", {}).get("docling"):
        print(f"AI parser outputs: {result.output_paths.ai_parser_dir('docling')}")
    if result.manifest and result.manifest.get("extractor_evidence", {}).get("doctr"):
        print("OCR parser: doctr")
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
        print("\nManifest extraction completed with failures.")
        return 1
    print("\nManifest extraction completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
