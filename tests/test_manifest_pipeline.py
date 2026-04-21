from __future__ import annotations

from dataclasses import dataclass

from accessibility_by_manifest.pipeline import ManifestPipeline, ManifestPipelineContext


@dataclass(frozen=True)
class Config:
    dry_run: bool = False


@dataclass(frozen=True)
class Run:
    name: str


def test_manifest_pipeline_flows_from_input_to_manifest_to_output() -> None:
    written: list[dict[str, str]] = []

    def paths_for_run(run: Run) -> str:
        return f"{run.name}.json"

    def build_manifest(context: ManifestPipelineContext[Config, Run, str]) -> dict[str, str]:
        return {"source": context.run.name, "target": context.output_paths}

    def write_outputs(context: ManifestPipelineContext[Config, Run, str], manifest: dict[str, str]) -> None:
        written.append({"path": context.output_paths, "source": manifest["source"]})

    pipeline = ManifestPipeline(
        output_paths_for_run=paths_for_run,
        build_manifest=build_manifest,
        write_outputs=write_outputs,
        success_message=lambda manifest: f"wrote {manifest['target']}",
    )

    result = pipeline.run(Config(), Run("input"))

    assert result.ok is True
    assert result.message == "wrote input.json"
    assert result.manifest == {"source": "input", "target": "input.json"}
    assert written == [{"path": "input.json", "source": "input"}]


def test_manifest_pipeline_dry_run_builds_manifest_without_outputs() -> None:
    wrote_output = False

    def write_outputs(context: ManifestPipelineContext[Config, Run, str], manifest: dict[str, str]) -> None:
        nonlocal wrote_output
        wrote_output = True

    pipeline = ManifestPipeline(
        output_paths_for_run=lambda run: f"{run.name}.json",
        build_manifest=lambda context: {"source": context.run.name},
        write_outputs=write_outputs,
        success_message=lambda _: "done",
    )

    result = pipeline.run(Config(dry_run=True), Run("input"))

    assert result.ok is True
    assert result.message == "Dry run completed. No files were written."
    assert result.manifest == {"source": "input"}
    assert wrote_output is False
