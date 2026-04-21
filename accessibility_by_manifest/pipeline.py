from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Generic, TypeVar


ConfigT = TypeVar("ConfigT")
RunT = TypeVar("RunT")
PathsT = TypeVar("PathsT")
ManifestT = TypeVar("ManifestT")


@dataclass(frozen=True)
class ManifestPipelineContext(Generic[ConfigT, RunT, PathsT]):
    config: ConfigT
    run: RunT
    output_paths: PathsT


@dataclass(frozen=True)
class ManifestPipelineResult(Generic[RunT, PathsT, ManifestT]):
    run: RunT
    output_paths: PathsT
    ok: bool
    message: str
    manifest: ManifestT | None = None


class ManifestPipeline(Generic[ConfigT, RunT, PathsT, ManifestT]):
    """Run one document through input extraction, manifest creation, and outputs."""

    def __init__(
        self,
        *,
        output_paths_for_run: Callable[[RunT], PathsT],
        build_manifest: Callable[[ManifestPipelineContext[ConfigT, RunT, PathsT]], ManifestT],
        write_outputs: Callable[[ManifestPipelineContext[ConfigT, RunT, PathsT], ManifestT], None],
        success_message: Callable[[ManifestT], str],
        dry_run_message: str = "Dry run completed. No files were written.",
        error_message: Callable[[Exception], str] = str,
    ) -> None:
        self.output_paths_for_run = output_paths_for_run
        self.build_manifest = build_manifest
        self.write_outputs = write_outputs
        self.success_message = success_message
        self.dry_run_message = dry_run_message
        self.error_message = error_message

    def run(self, config: ConfigT, run: RunT) -> ManifestPipelineResult[RunT, PathsT, ManifestT]:
        paths = self.output_paths_for_run(run)
        context = ManifestPipelineContext(config=config, run=run, output_paths=paths)
        try:
            manifest = self.build_manifest(context)
            if getattr(config, "dry_run", False):
                return ManifestPipelineResult(
                    run=run,
                    output_paths=paths,
                    ok=True,
                    message=self.dry_run_message,
                    manifest=manifest,
                )
            self.write_outputs(context, manifest)
            return ManifestPipelineResult(
                run=run,
                output_paths=paths,
                ok=True,
                message=self.success_message(manifest),
                manifest=manifest,
            )
        except Exception as exc:
            return ManifestPipelineResult(
                run=run,
                output_paths=paths,
                ok=False,
                message=self.error_message(exc),
            )
