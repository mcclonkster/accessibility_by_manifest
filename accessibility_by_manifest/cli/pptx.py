from __future__ import annotations

import argparse
from pathlib import Path

from accessibility_by_manifest.inputs.pptx.config import PptxManifestConfig
from accessibility_by_manifest.inputs.pptx.dependencies import check_dependencies
from accessibility_by_manifest.inputs.pptx.paths import discover_pptx_files, plan_runs
from accessibility_by_manifest.pipelines.pptx import DeckResult, run_deck


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert PPTX files into image-retaining DOCX accessibility review artifacts.",
    )
    parser.add_argument("input", type=Path, help="A .pptx file or a folder containing .pptx files.")
    parser.add_argument("--output-dir", type=Path, default=None, help="Output folder. Folder input creates one subfolder per deck.")
    parser.add_argument("--no-recursive", action="store_true", help="Only scan the top level of a folder input.")
    parser.add_argument("--no-slide-images", action="store_true", help="Skip slide-image rendering and insertion.")
    parser.add_argument("--require-slide-images", action="store_true", help="Fail if slide images cannot be rendered.")
    parser.add_argument("--render-dpi", type=int, default=160, help="DPI used when rendering slide images.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing outputs.")
    parser.add_argument("--dry-run", action="store_true", help="Read and extract without writing outputs.")
    return parser


def config_from_args(args: argparse.Namespace) -> PptxManifestConfig:
    return PptxManifestConfig(
        input_path=args.input.expanduser().resolve(),
        output_root=args.output_dir.expanduser().resolve() if args.output_dir else None,
        recursive=not args.no_recursive,
        overwrite=args.overwrite,
        dry_run=args.dry_run,
        include_slide_images=not args.no_slide_images,
        require_slide_images=args.require_slide_images,
        render_dpi=args.render_dpi,
    )


def validate_config(parser: argparse.ArgumentParser, config: PptxManifestConfig) -> None:
    if not config.input_path.exists():
        parser.error(f"input path does not exist: {config.input_path}")
    if config.render_dpi < 72 or config.render_dpi > 300:
        parser.error("--render-dpi must be between 72 and 300.")
    report = check_dependencies(config)
    if not report.ok:
        parser.error("Dependency check failed:\n- " + "\n- ".join(report.errors))


def print_result(result: DeckResult, index: int, total: int) -> None:
    status = "SUCCESS" if result.ok else "FAILURE"
    print(f"\n=== [{index}/{total}] {result.run.pptx_path} ===")
    print(f"Status: {status}")
    print(f"Message: {result.message}")
    print(f"Output folder: {result.run.output_dir}")
    print(f"Companion DOCX: {result.output_paths.companion_docx}")
    print(f"Slides DOCX: {result.output_paths.slides_docx}")
    print(f"Slides Markdown: {result.output_paths.slides_markdown}")
    print(f"Manifest JSON: {result.output_paths.manifest_json}")
    if result.manifest:
        summary = result.manifest.summary()
        print(f"Slides processed: {summary['total_slides']}")
        print(f"Slides with warnings: {summary['slides_with_warnings']}")
        print(f"Detected visual entries: {summary['detected_visual_entries']}")
        missing_images = sum(1 for slide in result.manifest.slides if not slide.preview_image)
        print(f"Slides missing images: {missing_images}")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    config = config_from_args(args)
    validate_config(parser, config)

    pptx_files = discover_pptx_files(config.input_path, config.recursive)
    if not pptx_files:
        parser.error(f"no .pptx files found at: {config.input_path}")

    if config.output_root is not None and not config.dry_run:
        config.output_root.mkdir(parents=True, exist_ok=True)

    runs = plan_runs(pptx_files, config.input_path, config.output_root)
    print(f"Found {len(runs)} PPTX file(s).")

    results = [run_deck(config, run) for run in runs]
    for index, result in enumerate(results, start=1):
        print_result(result, index, len(results))

    failures = [result for result in results if not result.ok]
    if failures:
        print("\nManifest run completed with failures.")
        return 1

    print("\nManifest run completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
