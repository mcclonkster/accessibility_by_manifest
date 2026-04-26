from __future__ import annotations

from accessibility_by_manifest.outputs.html import write_accessible_html
from pdf_accessibility.models.events import NodeEvent, artifact_record, artifact_registration_event
from pdf_accessibility.models.state import DocumentState
from pdf_accessibility.services.manifest_bridge import load_shared_pdf_model
from pdf_accessibility.utils.ids import event_id, stable_id

NODE_NAME = "write_accessible_html"


def run(document: DocumentState) -> list[NodeEvent]:
    output_path = document.run_dir / "accessible_output.html"
    shared_document = load_shared_pdf_model(document.source_path, document.run_dir)
    write_accessible_html(shared_document, output_path, overwrite=True)
    artifact = artifact_record(
        artifact_id=f"artifact-{stable_id(NODE_NAME, output_path)}",
        name="accessible_output.html",
        path=output_path,
        artifact_type="html",
        producer_node=NODE_NAME,
    )
    return [
        artifact_registration_event(event_id(NODE_NAME, "artifact", document.document_id), NODE_NAME, artifact),
    ]
