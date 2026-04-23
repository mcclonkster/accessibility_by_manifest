from __future__ import annotations

from accessibility_by_manifest.inputs.docx.paths import DocxOutputPaths
from accessibility_by_manifest.normalize.docx import normalize_docx_manifest_to_ir
from accessibility_by_manifest.outputs.manifest import write_json_manifest


def write_docx_manifest_outputs(output_paths: DocxOutputPaths, manifest: dict, overwrite: bool) -> None:
    write_json_manifest(output_paths.manifest_json, manifest, overwrite)
    write_json_manifest(output_paths.normalized_manifest_json, normalize_docx_manifest_to_ir(manifest), overwrite)
