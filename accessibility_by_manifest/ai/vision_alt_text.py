from __future__ import annotations

import base64
import json
import tempfile
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any
from urllib import request
from urllib.error import HTTPError, URLError
from zipfile import ZipFile

from accessibility_by_manifest.outputs.manifest import atomic_write_text
from accessibility_by_manifest.util.fingerprints import file_sha256
from accessibility_by_manifest.util.logging import get_logger


LOGGER = get_logger(__name__)

SUPPORTED_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}
DEFAULT_OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
DEFAULT_LMSTUDIO_ENDPOINT = "http://localhost:1234/v1/chat/completions"
DEFAULT_ALT_TEXT_PROMPT = (
    "Write concise accessibility alt text for this document image. "
    "Return JSON with keys alt_text, image_kind, confidence, and review_note. "
    "Use one sentence for alt_text, under 160 characters when possible. "
    "Describe visible meaning, not aesthetics. Do not say 'image of' unless needed. "
    "If it is decorative, say so in alt_text. If it is a chart/table/scan and details are not fully legible, say what review is needed."
)


@dataclass(frozen=True)
class VisionAltTextConfig:
    provider: str = "ollama"
    model: str = "llava"
    endpoint: str | None = None
    timeout_seconds: int = 120
    prompt: str = DEFAULT_ALT_TEXT_PROMPT
    max_context_chars: int = 1200
    temperature: float = 0.1
    lmstudio_json_mode: bool = False


@dataclass(frozen=True)
class ImageAltTextRequest:
    image_path: Path
    source_ref: str
    context_text: str = ""
    existing_title: str | None = None
    existing_description: str | None = None


@dataclass(frozen=True)
class ImageAltTextResult:
    source_ref: str
    image_path: str
    sha256: str
    provider: str
    model: str
    alt_text: str | None
    image_kind: str | None
    confidence: str
    review_note: str | None
    existing_title: str | None = None
    existing_description: str | None = None
    elapsed_seconds: float | None = None
    raw_response: str | None = None
    error: str | None = None
    warnings: list[str] = field(default_factory=list)


def generate_alt_text_for_images(
    requests_to_process: list[ImageAltTextRequest], config: VisionAltTextConfig
) -> list[ImageAltTextResult]:
    if config.provider == "ollama":
        client: LocalVisionClient = OllamaVisionClient(config)
    elif config.provider == "lmstudio":
        client = LMStudioVisionClient(config)
    else:
        raise ValueError(f"Unsupported local vision provider: {config.provider}")

    results: list[ImageAltTextResult] = []
    for item in requests_to_process:
        LOGGER.info("Generating local vision alt text: image=%s model=%s", item.image_path, config.model)
        results.append(client.generate_alt_text(item))
    return results


def write_alt_text_report(path: Path, results: list[ImageAltTextResult], config: VisionAltTextConfig, *, overwrite: bool) -> None:
    report = {
        "report_kind": "local_vision_alt_text_report",
        "provider": config.provider,
        "model": config.model,
        "endpoint": endpoint_for_config(config),
        "result_count": len(results),
        "generated_count": sum(1 for result in results if result.alt_text and not result.error),
        "error_count": sum(1 for result in results if result.error),
        "results": [asdict(result) for result in results],
        "notes": [
            "Local vision model output is draft alt text. Human review is still required for meaningful figures, charts, and complex tables.",
            "This report should feed a DOCX repair plan rather than overwrite source evidence.",
        ],
    }
    atomic_write_text(path, json.dumps(report, indent=2, ensure_ascii=False) + "\n", overwrite)


def collect_image_requests(input_path: Path, output_dir: Path | None = None, *, overwrite: bool = False) -> list[ImageAltTextRequest]:
    input_path = input_path.expanduser().resolve()
    if input_path.is_dir():
        return [ImageAltTextRequest(image_path=path, source_ref=str(path)) for path in discover_images(input_path)]
    if input_path.suffix.lower() == ".docx":
        if output_dir is None:
            output_dir = input_path.parent / f"{input_path.stem}_vision_images"
        return extract_docx_media_requests(input_path, output_dir, overwrite=overwrite)
    if input_path.suffix.lower() in SUPPORTED_IMAGE_SUFFIXES and input_path.is_file():
        return [ImageAltTextRequest(image_path=input_path, source_ref=str(input_path))]
    raise ValueError(f"Expected an image file, image folder, or .docx file: {input_path}")


def discover_images(folder: Path) -> list[Path]:
    return sorted(path for path in folder.rglob("*") if path.is_file() and path.suffix.lower() in SUPPORTED_IMAGE_SUFFIXES)


def extract_docx_media_requests(docx_path: Path, image_output_dir: Path, *, overwrite: bool) -> list[ImageAltTextRequest]:
    image_output_dir.mkdir(parents=True, exist_ok=True)
    requests_to_process: list[ImageAltTextRequest] = []
    with ZipFile(docx_path) as docx_zip:
        media_names = sorted(
            name
            for name in docx_zip.namelist()
            if name.startswith("word/media/") and Path(name).suffix.lower() in SUPPORTED_IMAGE_SUFFIXES
        )
        for media_name in media_names:
            target = image_output_dir / Path(media_name).name
            if target.exists() and not overwrite:
                raise FileExistsError(f"Output already exists. Use --overwrite or choose another folder: {target}")
            atomic_write_bytes(target, docx_zip.read(media_name))
            requests_to_process.append(
                ImageAltTextRequest(
                    image_path=target,
                    source_ref=f"{docx_path.name}:{media_name}",
                    context_text=f"Image extracted from DOCX media part {media_name}.",
                )
            )
    return requests_to_process


class LocalVisionClient:
    def generate_alt_text(self, item: ImageAltTextRequest) -> ImageAltTextResult:
        raise NotImplementedError


class OllamaVisionClient(LocalVisionClient):
    def __init__(self, config: VisionAltTextConfig) -> None:
        self.config = config

    def generate_alt_text(self, item: ImageAltTextRequest) -> ImageAltTextResult:
        started_at = time.monotonic()
        warnings = validate_image_request(item)
        if warnings:
            return result_from_error(item, self.config, "; ".join(warnings), warnings, time.monotonic() - started_at)

        payload = {
            "model": self.config.model,
            "prompt": build_prompt(item, self.config),
            "images": [base64.b64encode(item.image_path.read_bytes()).decode("ascii")],
            "stream": False,
            "format": "json",
            "options": {"temperature": self.config.temperature},
        }
        try:
            data = json.dumps(payload).encode("utf-8")
            http_request = request.Request(
                endpoint_for_config(self.config),
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with request.urlopen(http_request, timeout=self.config.timeout_seconds) as response:
                response_data = json.loads(response.read().decode("utf-8"))
            raw_response = str(response_data.get("response", "")).strip()
            parsed = parse_model_response(raw_response)
            return ImageAltTextResult(
                source_ref=item.source_ref,
                image_path=str(item.image_path),
                sha256=file_sha256(item.image_path),
                provider=self.config.provider,
                model=self.config.model,
                alt_text=parsed.get("alt_text"),
                image_kind=parsed.get("image_kind"),
                confidence=parsed.get("confidence") or "low",
                review_note=parsed.get("review_note"),
                existing_title=item.existing_title,
                existing_description=item.existing_description,
                elapsed_seconds=round(time.monotonic() - started_at, 3),
                raw_response=raw_response,
                warnings=response_warnings(parsed),
            )
        except (OSError, URLError, json.JSONDecodeError) as exc:
            return result_from_error(item, self.config, str(exc), warnings, time.monotonic() - started_at)


class LMStudioVisionClient(LocalVisionClient):
    def __init__(self, config: VisionAltTextConfig) -> None:
        self.config = config

    def generate_alt_text(self, item: ImageAltTextRequest) -> ImageAltTextResult:
        started_at = time.monotonic()
        warnings = validate_image_request(item)
        if warnings:
            return result_from_error(item, self.config, "; ".join(warnings), warnings, time.monotonic() - started_at)

        payload = {
            "model": self.config.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": build_prompt(item, self.config)},
                        {
                            "type": "image_url",
                            "image_url": {"url": image_data_url(item.image_path)},
                        },
                    ],
                }
            ],
            "temperature": self.config.temperature,
            "stream": False,
        }
        if self.config.lmstudio_json_mode:
            payload["response_format"] = {"type": "json_object"}
        try:
            data = json.dumps(payload).encode("utf-8")
            http_request = request.Request(
                endpoint_for_config(self.config),
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with request.urlopen(http_request, timeout=self.config.timeout_seconds) as response:
                response_data = json.loads(response.read().decode("utf-8"))
            raw_response = lmstudio_response_text(response_data)
            parsed = parse_model_response(raw_response)
            return ImageAltTextResult(
                source_ref=item.source_ref,
                image_path=str(item.image_path),
                sha256=file_sha256(item.image_path),
                provider=self.config.provider,
                model=self.config.model,
                alt_text=parsed.get("alt_text"),
                image_kind=parsed.get("image_kind"),
                confidence=parsed.get("confidence") or "low",
                review_note=parsed.get("review_note"),
                existing_title=item.existing_title,
                existing_description=item.existing_description,
                elapsed_seconds=round(time.monotonic() - started_at, 3),
                raw_response=raw_response,
                warnings=response_warnings(parsed),
            )
        except HTTPError as exc:
            return result_from_error(item, self.config, http_error_message(exc), warnings, time.monotonic() - started_at)
        except (OSError, URLError, json.JSONDecodeError, KeyError, IndexError, TypeError) as exc:
            return result_from_error(item, self.config, str(exc), warnings, time.monotonic() - started_at)


def build_prompt(item: ImageAltTextRequest, config: VisionAltTextConfig) -> str:
    context = item.context_text[: config.max_context_chars].strip()
    metadata = []
    if item.existing_title:
        metadata.append(f"Existing title: {item.existing_title}")
    if item.existing_description:
        metadata.append(f"Existing description: {item.existing_description}")
    if context:
        metadata.append(f"Document context: {context}")
    metadata_text = "\n".join(metadata)
    if metadata_text:
        return f"{config.prompt}\n\n{metadata_text}"
    return config.prompt


def endpoint_for_config(config: VisionAltTextConfig) -> str:
    if config.endpoint:
        return config.endpoint
    if config.provider == "ollama":
        return DEFAULT_OLLAMA_ENDPOINT
    if config.provider == "lmstudio":
        return DEFAULT_LMSTUDIO_ENDPOINT
    raise ValueError(f"Unsupported local vision provider: {config.provider}")


def image_data_url(image_path: Path) -> str:
    suffix = image_path.suffix.lower()
    mime_type = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(suffix, "application/octet-stream")
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def lmstudio_response_text(response_data: dict[str, Any]) -> str:
    content = response_data["choices"][0]["message"]["content"]
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        chunks = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                chunks.append(str(item.get("text", "")))
        return "\n".join(chunks).strip()
    return str(content).strip()


def http_error_message(exc: HTTPError) -> str:
    try:
        body = exc.read().decode("utf-8", errors="replace").strip()
    except Exception:
        body = ""
    if body:
        return f"HTTP {exc.code} {exc.reason}: {body}"
    return f"HTTP {exc.code} {exc.reason}"


def parse_model_response(raw_response: str) -> dict[str, str | None]:
    response_text = strip_json_code_fence(raw_response)
    try:
        parsed = json.loads(response_text)
    except json.JSONDecodeError:
        return {
            "alt_text": raw_response.strip() or None,
            "image_kind": None,
            "confidence": "low",
            "review_note": "Model did not return JSON; review required.",
        }

    if not isinstance(parsed, dict):
        return {
            "alt_text": raw_response.strip() or None,
            "image_kind": None,
            "confidence": "low",
            "review_note": "Model returned non-object JSON; review required.",
        }

    confidence = normalize_confidence(parsed.get("confidence"))
    return {
        "alt_text": clean_alt_text(parsed.get("alt_text")),
        "image_kind": clean_alt_text(parsed.get("image_kind")),
        "confidence": confidence,
        "review_note": clean_alt_text(parsed.get("review_note")),
    }


def strip_json_code_fence(value: str) -> str:
    text = value.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].strip().startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text


def normalize_confidence(value: Any) -> str:
    if isinstance(value, int | float):
        if value >= 0.8:
            return "high"
        if value >= 0.45:
            return "medium"
        return "low"
    text = str(value or "low").lower().strip()
    if text in {"high", "medium", "low"}:
        return text
    try:
        return normalize_confidence(float(text))
    except ValueError:
        return "low"


def clean_alt_text(value: Any) -> str | None:
    if value is None:
        return None
    text = " ".join(str(value).split())
    return text or None


def response_warnings(parsed: dict[str, str | None]) -> list[str]:
    warnings = []
    alt_text = parsed.get("alt_text")
    if not alt_text:
        warnings.append("Model did not produce alt text.")
    elif len(alt_text) > 240:
        warnings.append("Generated alt text is long and should be shortened.")
    if parsed.get("confidence") == "low":
        warnings.append("Model confidence is low; human review required.")
    return warnings


def validate_image_request(item: ImageAltTextRequest) -> list[str]:
    warnings = []
    if not item.image_path.exists():
        warnings.append(f"Image path does not exist: {item.image_path}")
    elif item.image_path.suffix.lower() not in SUPPORTED_IMAGE_SUFFIXES:
        warnings.append(f"Unsupported image suffix: {item.image_path.suffix}")
    return warnings


def result_from_error(
    item: ImageAltTextRequest,
    config: VisionAltTextConfig,
    error: str,
    warnings: list[str],
    elapsed_seconds: float,
) -> ImageAltTextResult:
    return ImageAltTextResult(
        source_ref=item.source_ref,
        image_path=str(item.image_path),
        sha256=file_sha256(item.image_path) if item.image_path.exists() else "",
        provider=config.provider,
        model=config.model,
        alt_text=None,
        image_kind=None,
        confidence="low",
        review_note="Alt text generation failed; human review required.",
        existing_title=item.existing_title,
        existing_description=item.existing_description,
        elapsed_seconds=round(elapsed_seconds, 3),
        error=error,
        warnings=warnings,
    )


def atomic_write_bytes(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=path.suffix or ".tmp", dir=str(path.parent), prefix=f"{path.stem}_") as temp_file:
            temp_path = Path(temp_file.name)
        temp_path.write_bytes(content)
        temp_path.replace(path)
    except Exception:
        if temp_path and temp_path.exists():
            temp_path.unlink(missing_ok=True)
        raise
