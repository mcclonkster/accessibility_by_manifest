import json
from pathlib import Path

from accessibility_by_manifest.ai import vision_alt_text
from accessibility_by_manifest.ai.vision_alt_text import (
    ImageAltTextRequest,
    VisionAltTextConfig,
    collect_image_requests,
    generate_alt_text_for_images,
    image_data_url,
    parse_model_response,
)


ONE_PIXEL_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
    b"\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01"
    b"\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82"
)


def test_parse_model_response_accepts_json_and_plain_text() -> None:
    parsed = parse_model_response(
        '{"alt_text": "Bar chart showing revenue growth.", "image_kind": "chart", "confidence": "medium", "review_note": "Check values."}'
    )

    assert parsed["alt_text"] == "Bar chart showing revenue growth."
    assert parsed["image_kind"] == "chart"
    assert parsed["confidence"] == "medium"
    assert parsed["review_note"] == "Check values."
    assert parse_model_response("A campus building exterior.")["alt_text"] == "A campus building exterior."


def test_parse_model_response_accepts_fenced_json_and_numeric_confidence() -> None:
    parsed = parse_model_response(
        '```json\n{"alt_text": "Kemper CPA Group logo.", "image_kind": "logo", "confidence": 0.95, "review_note": ""}\n```'
    )

    assert parsed["alt_text"] == "Kemper CPA Group logo."
    assert parsed["image_kind"] == "logo"
    assert parsed["confidence"] == "high"
    assert parsed["review_note"] is None


def test_collect_image_requests_extracts_docx_media(tmp_path: Path) -> None:
    from docx import Document

    image_path = tmp_path / "image.png"
    image_path.write_bytes(ONE_PIXEL_PNG)
    docx_path = tmp_path / "document.docx"
    document = Document()
    document.add_picture(str(image_path))
    document.save(docx_path)
    output_dir = tmp_path / "images"

    requests = collect_image_requests(docx_path, output_dir, overwrite=True)

    assert len(requests) == 1
    assert requests[0].image_path.exists()
    assert requests[0].source_ref == "document.docx:word/media/image1.png"


def test_ollama_provider_posts_generate_payload(monkeypatch, tmp_path: Path) -> None:
    image_path = tmp_path / "image.png"
    image_path.write_bytes(ONE_PIXEL_PNG)
    seen = {}

    def fake_urlopen(http_request, timeout):
        seen["url"] = http_request.full_url
        seen["timeout"] = timeout
        seen["payload"] = json.loads(http_request.data.decode("utf-8"))
        return FakeResponse({"response": '{"alt_text":"Line chart trending upward.","image_kind":"chart","confidence":"medium","review_note":"Review labels."}'})

    monkeypatch.setattr(vision_alt_text.request, "urlopen", fake_urlopen)
    config = VisionAltTextConfig(provider="ollama", model="llava", endpoint="http://localhost:11434/api/generate")

    results = generate_alt_text_for_images([ImageAltTextRequest(image_path=image_path, source_ref="image.png")], config)

    assert seen["url"] == "http://localhost:11434/api/generate"
    assert seen["payload"]["model"] == "llava"
    assert seen["payload"]["images"]
    assert results[0].alt_text == "Line chart trending upward."
    assert results[0].provider == "ollama"


def test_lmstudio_provider_posts_chat_completion_payload(monkeypatch, tmp_path: Path) -> None:
    image_path = tmp_path / "image.png"
    image_path.write_bytes(ONE_PIXEL_PNG)
    seen = {}

    def fake_urlopen(http_request, timeout):
        seen["url"] = http_request.full_url
        seen["timeout"] = timeout
        seen["payload"] = json.loads(http_request.data.decode("utf-8"))
        return FakeResponse(
            {
                "choices": [
                    {
                        "message": {
                            "content": '{"alt_text":"Seal for the college.","image_kind":"logo","confidence":"medium","review_note":"Confirm official name."}'
                        }
                    }
                ]
            }
        )

    monkeypatch.setattr(vision_alt_text.request, "urlopen", fake_urlopen)
    config = VisionAltTextConfig(provider="lmstudio", model="qwen2.5-vl")

    results = generate_alt_text_for_images([ImageAltTextRequest(image_path=image_path, source_ref="image.png")], config)

    assert seen["url"] == "http://localhost:1234/v1/chat/completions"
    assert seen["payload"]["model"] == "qwen2.5-vl"
    content = seen["payload"]["messages"][0]["content"]
    assert content[0]["type"] == "text"
    assert content[1]["type"] == "image_url"
    assert content[1]["image_url"]["url"].startswith("data:image/png;base64,")
    assert "response_format" not in seen["payload"]
    assert results[0].alt_text == "Seal for the college."
    assert results[0].provider == "lmstudio"


def test_lmstudio_json_mode_is_opt_in(monkeypatch, tmp_path: Path) -> None:
    image_path = tmp_path / "image.png"
    image_path.write_bytes(ONE_PIXEL_PNG)
    seen = {}

    def fake_urlopen(http_request, timeout):
        seen["payload"] = json.loads(http_request.data.decode("utf-8"))
        return FakeResponse({"choices": [{"message": {"content": '{"alt_text":"A logo.","confidence":"medium"}'}}]})

    monkeypatch.setattr(vision_alt_text.request, "urlopen", fake_urlopen)
    config = VisionAltTextConfig(provider="lmstudio", model="qwen/qwen3.5-9b", lmstudio_json_mode=True)

    generate_alt_text_for_images([ImageAltTextRequest(image_path=image_path, source_ref="image.png")], config)

    assert seen["payload"]["response_format"] == {"type": "json_object"}


def test_image_data_url_uses_mime_type(tmp_path: Path) -> None:
    image_path = tmp_path / "image.png"
    image_path.write_bytes(ONE_PIXEL_PNG)

    assert image_data_url(image_path).startswith("data:image/png;base64,")


class FakeResponse:
    def __init__(self, payload: dict) -> None:
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return None

    def read(self) -> bytes:
        return json.dumps(self.payload).encode("utf-8")
