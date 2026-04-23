from __future__ import annotations

import argparse
from pathlib import Path

from accessibility_by_manifest.ai.vision_alt_text import (
    VisionAltTextConfig,
    collect_image_requests,
    generate_alt_text_for_images,
    write_alt_text_report,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate draft alt text with a local vision model.")
    parser.add_argument("input", type=Path, help="An image file, image folder, or .docx file.")
    parser.add_argument("--output", type=Path, default=None, help="Alt-text report JSON path.")
    parser.add_argument("--image-output-dir", type=Path, default=None, help="Where DOCX media images are extracted before analysis.")
    parser.add_argument("--provider", choices=("ollama", "lmstudio"), default="ollama", help="Local vision provider.")
    parser.add_argument("--model", default=None, help="Local vision model name.")
    parser.add_argument("--endpoint", default=None, help="Provider endpoint URL.")
    parser.add_argument("--timeout", type=int, default=120, help="Request timeout in seconds.")
    parser.add_argument("--limit", type=int, default=None, help="Only process the first N discovered images.")
    parser.add_argument(
        "--lmstudio-json-mode",
        action="store_true",
        help="Ask LM Studio for JSON mode. Leave off if the loaded model/server rejects response_format.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing extracted images/report.")
    return parser


def config_from_args(args: argparse.Namespace) -> VisionAltTextConfig:
    default_model = "llava" if args.provider == "ollama" else "local-model"
    return VisionAltTextConfig(
        provider=args.provider,
        model=args.model or default_model,
        endpoint=args.endpoint,
        timeout_seconds=args.timeout,
        lmstudio_json_mode=args.lmstudio_json_mode,
    )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    input_path = args.input.expanduser().resolve()
    if not input_path.exists():
        parser.error(f"input path does not exist: {input_path}")

    config = config_from_args(args)
    image_output_dir = args.image_output_dir.expanduser().resolve() if args.image_output_dir else None
    requests_to_process = collect_image_requests(input_path, image_output_dir, overwrite=args.overwrite)
    if args.limit is not None:
        requests_to_process = requests_to_process[: args.limit]
    if not requests_to_process:
        parser.error(f"no supported images found at: {input_path}")

    output_path = args.output.expanduser().resolve() if args.output else default_output_path(input_path)
    print(f"Images queued: {len(requests_to_process)}")
    results = []
    for index, item in enumerate(requests_to_process, start=1):
        print(f"Processing image {index}/{len(requests_to_process)}: {item.image_path.name}")
        result = generate_alt_text_for_images([item], config)[0]
        status = "generated" if result.alt_text and not result.error else "error"
        print(f"Finished image {index}/{len(requests_to_process)}: {status}")
        results.append(result)
    write_alt_text_report(output_path, results, config, overwrite=args.overwrite)

    print(f"Provider: {config.provider}")
    print(f"Model: {config.model}")
    print(f"Images processed: {len(results)}")
    print(f"Generated: {sum(1 for result in results if result.alt_text and not result.error)}")
    print(f"Errors: {sum(1 for result in results if result.error)}")
    print(f"Alt-text report: {output_path}")
    return 0 if all(result.alt_text and not result.error for result in results) else 1


def default_output_path(input_path: Path) -> Path:
    stem = input_path.stem if input_path.is_file() else input_path.name
    return input_path.parent / f"{stem}_local_vision_alt_text.json"


if __name__ == "__main__":
    raise SystemExit(main())
