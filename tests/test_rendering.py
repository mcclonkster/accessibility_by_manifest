from pathlib import Path

import pytest

from accessibility_by_manifest.errors import RenderError
from accessibility_by_manifest.inputs.pptx.config import PptxManifestConfig
from accessibility_by_manifest.inputs.pptx.rendering import render_slide_images


def test_render_failure_is_warning_when_images_are_optional(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    def fail_render(*args: object, **kwargs: object) -> object:
        raise RenderError("boom")

    monkeypatch.setattr("accessibility_by_manifest.inputs.pptx.rendering._render_slide_images", fail_render)
    config = PptxManifestConfig(input_path=tmp_path / "deck.pptx", require_slide_images=False)

    result = render_slide_images(tmp_path / "deck.pptx", tmp_path / "images", config)

    assert result.images_by_slide == {}
    assert result.warnings[0].code == "SLIDE_IMAGE_RENDER_FAILED"


def test_render_failure_raises_when_images_are_required(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    def fail_render(*args: object, **kwargs: object) -> object:
        raise RenderError("boom")

    monkeypatch.setattr("accessibility_by_manifest.inputs.pptx.rendering._render_slide_images", fail_render)
    config = PptxManifestConfig(input_path=tmp_path / "deck.pptx", require_slide_images=True)

    with pytest.raises(RenderError):
        render_slide_images(tmp_path / "deck.pptx", tmp_path / "images", config)
