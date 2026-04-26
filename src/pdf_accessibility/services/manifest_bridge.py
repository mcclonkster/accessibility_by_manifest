from __future__ import annotations

from pathlib import Path

from accessibility_by_manifest.inputs.pdf import build_manifest_from_pdf
from accessibility_by_manifest.inputs.pdf.config import PdfManifestConfig
from accessibility_by_manifest.inputs.pdf.paths import PdfRun, output_paths
from accessibility_by_manifest.normalize import NormalizedAccessibilityDocument
from accessibility_by_manifest.normalize.pdf_accessibility_model import normalize_pdf_manifest_to_accessibility_model
from accessibility_by_manifest.pipeline import ManifestPipelineContext
from pdf_accessibility.models.events import (
    NodeEvent,
    document_metadata_event,
    document_pages_event,
    finding_event,
    normalized_structure_event,
    page_evidence_event,
    region_discovery_event,
    review_task_event,
)
from pdf_accessibility.models.state import (
    AnnotationEvidence,
    BBox,
    Confidence,
    DocumentMetadataEvidence,
    DocumentState,
    Finding,
    FindingClass,
    LinkEvidence,
    NormalizedUnit,
    PageGeometryEvidence,
    RegionState,
    RegionStatus,
    ReviewTask,
    TextBlockEvidence,
)
from pdf_accessibility.utils.ids import event_id, stable_id


NODE_NAME = "manifest_bridge"
BRIDGE_MARKER = "shared_pdf_manifest_bridge_v1"


def load_shared_pdf_events(document: DocumentState) -> list[NodeEvent]:
    manifest = _build_pdf_manifest(document.source_path, document.run_dir)
    shared_document = normalize_pdf_manifest_to_accessibility_model(manifest)
    events: list[NodeEvent] = [
        document_pages_event(
            event_id(NODE_NAME, "pages", document.document_id),
            NODE_NAME,
            int(manifest.get("document_summary", {}).get("total_pages") or len(manifest.get("page_entries", [])) or 0),
        ),
        document_metadata_event(
            event_id(NODE_NAME, "metadata", document.document_id),
            NODE_NAME,
            _document_metadata(manifest, shared_document),
        ),
    ]

    for page_event in _page_events(manifest, document.document_id):
        events.append(page_event)

    regions = _regions_from_units(shared_document.unit_entries)
    if regions:
        events.append(
            region_discovery_event(
                event_id(NODE_NAME, "regions", document.document_id),
                NODE_NAME,
                regions,
            )
        )
    events.append(
        normalized_structure_event(
            event_id(NODE_NAME, "normalized", document.document_id),
            NODE_NAME,
            [_workflow_unit(unit) for unit in shared_document.unit_entries],
        )
    )
    for review_task in _review_tasks(shared_document):
        events.append(
            review_task_event(
                event_id(NODE_NAME, "review", review_task.task_id),
                NODE_NAME,
                review_task,
            )
        )
    events.append(
        finding_event(
            event_id(NODE_NAME, "bridge", document.document_id),
            NODE_NAME,
            Finding(
                finding_id=f"finding-{stable_id(NODE_NAME, document.document_id)}",
                node_name=NODE_NAME,
                finding_class=FindingClass.EVIDENCE,
                target_ref="document",
                message=(
                    "Shared PDF manifest bridge loaded "
                    f"{len(shared_document.unit_entries)} normalized units and {len(shared_document.review_entries)} review tasks."
                ),
                confidence=Confidence.HIGH,
                payload={
                    "bridge_marker": BRIDGE_MARKER,
                    "source_manifest_kind": shared_document.source_manifest_kind,
                    "source_manifest_version": shared_document.source_manifest_version,
                    "shared_model_version": shared_document.model_version,
                },
            ),
        )
    )
    return events


def document_uses_shared_pdf_bridge(document: DocumentState) -> bool:
    metadata = document.metadata
    if metadata is None:
        return False
    return metadata.provenance.get("bridge_marker") == BRIDGE_MARKER


def load_shared_pdf_model(source_path: Path, run_dir: Path) -> NormalizedAccessibilityDocument:
    manifest = _build_pdf_manifest(source_path, run_dir)
    return normalize_pdf_manifest_to_accessibility_model(manifest)


def _build_pdf_manifest(source_path: Path, run_dir: Path) -> dict:
    bridge_output_dir = run_dir / "_shared_pdf_bridge"
    run = PdfRun(pdf_path=source_path, output_dir=bridge_output_dir)
    context = ManifestPipelineContext(
        config=PdfManifestConfig(
            input_path=source_path,
            output_root=bridge_output_dir,
            overwrite=True,
            dry_run=True,
        ),
        run=run,
        output_paths=output_paths(run),
    )
    return build_manifest_from_pdf(context)


def _document_metadata(manifest: dict, shared_document) -> DocumentMetadataEvidence:
    source_info = dict(manifest.get("document_metadata", {}).get("info") or {})
    keyword_values = shared_document.document.keywords
    if isinstance(keyword_values, list):
        keywords = ", ".join(keyword_values) or None
    else:
        keywords = keyword_values
    pymupdf_metadata = dict(manifest.get("extractor_evidence", {}).get("pymupdf", {}).get("document_metadata") or {})
    return DocumentMetadataEvidence(
        title=shared_document.document.title,
        author=shared_document.document.author,
        subject=shared_document.document.subject,
        keywords=keywords,
        creator=source_info.get("creator"),
        producer=source_info.get("producer"),
        creation_date=shared_document.document.created_at,
        modification_date=shared_document.document.modified_at,
        primary_language=shared_document.document.primary_language,
        pdf_version=pymupdf_metadata.get("format"),
        encrypted=bool(manifest.get("extractor_evidence", {}).get("pymupdf", {}).get("is_encrypted")),
        raw_metadata=source_info,
        provenance={
            "bridge_marker": BRIDGE_MARKER,
            "source_manifest_kind": shared_document.source_manifest_kind,
            "source_manifest_version": shared_document.source_manifest_version,
            "shared_model_version": shared_document.model_version,
        },
    )


def _page_events(manifest: dict, document_id: str) -> list[NodeEvent]:
    raw_blocks_by_page: dict[int, list[dict]] = {}
    for raw_block in manifest.get("raw_block_entries", []):
        raw_blocks_by_page.setdefault(int(raw_block.get("page_number") or 0), []).append(raw_block)

    events: list[NodeEvent] = []
    for page_entry in manifest.get("page_entries", []):
        page_number = int(page_entry.get("page_number") or 0)
        observed_source = dict(page_entry.get("observed_source") or {})
        extractor_evidence = dict(page_entry.get("extractor_evidence", {}).get("pymupdf") or {})
        annotation_evidence = extractor_evidence.get("annotation_evidence") or []
        events.append(
            page_evidence_event(
                event_id(NODE_NAME, "page", page_number, document_id),
                NODE_NAME,
                page_number,
                geometry=PageGeometryEvidence(
                    width=float((observed_source.get("viewport") or {}).get("width") or 0.0),
                    height=float((observed_source.get("viewport") or {}).get("height") or 0.0),
                    rotation=int(observed_source.get("page_rotation") or 0),
                    media_box=_bbox(extractor_evidence.get("mediabox")),
                    crop_box=_bbox(extractor_evidence.get("cropbox")),
                ),
                text_blocks=[_text_block(raw_block) for raw_block in raw_blocks_by_page.get(page_number, [])],
                images=[],
                links=_links(page_number, annotation_evidence),
                annotations=_annotations(page_number, annotation_evidence),
                font_names=sorted(
                    {
                        font_name
                        for raw_block in raw_blocks_by_page.get(page_number, [])
                        for font_name in [raw_block.get("style_hints", {}).get("font_name")]
                        if font_name
                    }
                ),
            )
        )
    return events


def _text_block(raw_block: dict) -> TextBlockEvidence:
    style_hints = dict(raw_block.get("style_hints") or {})
    font_name = style_hints.get("font_name")
    font_size = style_hints.get("font_size")
    return TextBlockEvidence(
        block_id=str(raw_block.get("block_id") or "unknown-block"),
        page_number=int(raw_block.get("page_number") or 0),
        bbox=_bbox(raw_block.get("bbox")) or BBox(left=0.0, top=0.0, right=0.0, bottom=0.0),
        text=str(raw_block.get("text") or ""),
        spans=[],
        font_names=[font_name] if font_name else [],
        font_sizes=[float(font_size)] if isinstance(font_size, int | float) else [],
        source_ref=str(raw_block.get("source_ref") or raw_block.get("block_id") or "unknown-source"),
        extractor=next(iter(dict(raw_block.get("extractor_evidence") or {}).keys()), "pymupdf"),
    )


def _links(page_number: int, annotation_evidence: list[dict]) -> list[LinkEvidence]:
    links: list[LinkEvidence] = []
    for index, entry in enumerate(annotation_evidence):
        if entry.get("kind") != "link":
            continue
        links.append(
            LinkEvidence(
                link_id=f"link-{stable_id(page_number, index, entry.get('url'), entry.get('dest'))}",
                page_number=page_number,
                bbox=_bbox(entry.get("rect")),
                uri=entry.get("url"),
                target=str(entry.get("dest")) if entry.get("dest") is not None else None,
                source_ref=f"manifest_bridge:page:{page_number}:link:{index}",
                extractor="shared_pdf_manifest",
            )
        )
    return links


def _annotations(page_number: int, annotation_evidence: list[dict]) -> list[AnnotationEvidence]:
    annotations: list[AnnotationEvidence] = []
    for index, entry in enumerate(annotation_evidence):
        if entry.get("kind") != "annotation":
            continue
        annotations.append(
            AnnotationEvidence(
                annotation_id=f"annotation-{stable_id(page_number, index, entry.get('annotation_subtype'))}",
                page_number=page_number,
                bbox=_bbox(entry.get("rect")),
                annotation_type=entry.get("annotation_subtype"),
                contents=entry.get("raw_info", {}).get("content") if isinstance(entry.get("raw_info"), dict) else None,
                source_ref=f"manifest_bridge:page:{page_number}:annotation:{index}",
                extractor="shared_pdf_manifest",
            )
        )
    return annotations


def _regions_from_units(units) -> list[RegionState]:
    regions: list[RegionState] = []
    for unit in units:
        page_number = unit.page_numbers[0] if unit.page_numbers else 0
        if page_number <= 0:
            continue
        regions.append(
            RegionState(
                region_id=f"region-{unit.unit_id}",
                page_number=page_number,
                bbox=_workflow_bbox(unit.bbox),
                status=RegionStatus.ACCESSIBILITY_REVIEWED,
                current_role=_region_role(unit.unit_type),
                confidence=_confidence(unit.confidence),
                source_refs=list(unit.source_refs),
                evidence_basis=list(unit.evidence_basis),
            )
        )
    return regions


def _workflow_unit(unit) -> NormalizedUnit:
    return NormalizedUnit(
        unit_id=unit.unit_id,
        unit_type=unit.unit_type,
        page_numbers=list(unit.page_numbers),
        bbox=_workflow_bbox(unit.bbox),
        text=unit.text,
        source_refs=list(unit.source_refs),
        evidence_basis=list(unit.evidence_basis),
        confidence=_confidence(unit.confidence),
        reading_order_index=unit.reading_order_index,
        needs_review=unit.needs_review,
    )


def _review_tasks(shared_document) -> list[ReviewTask]:
    return [
        ReviewTask(
            task_id=entry.task_id,
            issue_code=entry.issue_code,
            severity=entry.severity,
            target_ref=entry.target_ref,
            reason=entry.reason,
            suggested_action=entry.suggested_action,
            confidence_context=dict(entry.confidence_context),
            blocking=entry.blocking,
            resolved=entry.resolved,
            source_finding_ids=list(entry.source_refs),
        )
        for entry in shared_document.review_entries
    ]


def _region_role(unit_type: str) -> str:
    return {
        "heading": "heading_candidate",
        "paragraph": "paragraph_candidate",
        "table": "table_candidate",
        "table_cell": "table_candidate",
        "figure": "figure_candidate",
        "artifact": "artifact",
        "list_item": "paragraph_candidate",
    }.get(unit_type, "unknown")


def _confidence(value: str) -> Confidence:
    try:
        return Confidence(str(value).lower())
    except ValueError:
        return Confidence.MEDIUM


def _bbox(value) -> BBox | None:
    if value is None:
        return None
    if hasattr(value, "left"):
        return BBox(
            left=float(value.left),
            top=float(value.top),
            right=float(value.right),
            bottom=float(value.bottom),
        )
    if isinstance(value, (list, tuple)) and len(value) == 4 and all(item is not None for item in value):
        return BBox(left=float(value[0]), top=float(value[1]), right=float(value[2]), bottom=float(value[3]))
    return None


def _workflow_bbox(value) -> BBox | None:
    return _bbox(value)
