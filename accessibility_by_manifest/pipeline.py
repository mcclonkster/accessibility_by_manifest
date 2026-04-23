from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Generic, TypeVar

from accessibility_by_manifest.util.logging import get_logger, run_log


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
        log_path = getattr(paths, "log_file", None)
        if log_path is not None:
            with run_log(log_path, overwrite=getattr(config, "overwrite", False)):
                return self._run_with_context(context)
        return self._run_with_context(context)

    def _run_with_context(self, context: ManifestPipelineContext[ConfigT, RunT, PathsT]) -> ManifestPipelineResult[RunT, PathsT, ManifestT]:
        logger = get_logger("pipeline")
        try:
            logger.info("Pipeline run started: run=%r output_paths=%r", context.run, context.output_paths)
            logger.info("Building manifest")
            manifest = self.build_manifest(context)
            logger.info("Manifest build completed")
            if getattr(context.config, "dry_run", False):
                logger.info("Dry run completed; skipping output writes")
                return ManifestPipelineResult(
                    run=context.run,
                    output_paths=context.output_paths,
                    ok=True,
                    message=self.dry_run_message,
                    manifest=manifest,
                )
            logger.info("Writing outputs")
            self.write_outputs(context, manifest)
            logger.info("Output writes completed")
            return ManifestPipelineResult(
                run=context.run,
                output_paths=context.output_paths,
                ok=True,
                message=self.success_message(manifest),
                manifest=manifest,
            )
        except Exception as exc:
            logger.exception("Pipeline run failed")
            return ManifestPipelineResult(
                run=context.run,
                output_paths=context.output_paths,
                ok=False,
                message=self.error_message(exc),
            )
