from __future__ import annotations

import re

from pikepdf import Array, Stream

from pdf_accessibility.models.state import StructureElementPlan


def marked_content_strategy_note() -> str:
    return "MCID assignment is planned but content streams are not modified in this spike."


TEXT_OBJECT_PATTERN = re.compile(rb"\bBT\b.*?\bET\b", re.DOTALL)


def mark_simple_page_content(page, elements: list[StructureElementPlan]) -> dict[str, object]:
    writable = [
        element
        for element in sorted(elements, key=lambda item: item.mcid if item.mcid is not None else -1)
        if element.mcid is not None and element.pdf_structure_role in {"H", "P", "LI"}
    ]
    if not writable:
        return {
            "page_number": None,
            "status": "skipped_no_writable_elements",
            "written_mcid_count": 0,
            "skipped_mcid_count": 0,
        }

    streams = _content_streams(page)
    if not streams:
        return {
            "page_number": writable[0].page_number,
            "status": "skipped_no_content_stream",
            "written_mcid_count": 0,
            "skipped_mcid_count": len(writable),
        }

    if len(streams) == len(writable) and all(_text_object_count(stream.read_bytes()) == 1 for stream in streams):
        for stream, element in zip(streams, writable, strict=True):
            _wrap_stream(stream, element)
        return {
            "page_number": writable[0].page_number,
            "status": "written_stream_per_element",
            "written_mcid_count": len(writable),
            "skipped_mcid_count": 0,
        }

    if len(streams) == 1:
        data = streams[0].read_bytes()
        matches = list(TEXT_OBJECT_PATTERN.finditer(data))
        if len(matches) == len(writable):
            streams[0].write(_wrap_text_objects(data, matches, writable))
            return {
                "page_number": writable[0].page_number,
                "status": "written_text_objects_in_single_stream",
                "written_mcid_count": len(writable),
                "skipped_mcid_count": 0,
            }

    return {
        "page_number": writable[0].page_number,
        "status": "skipped_complex_stream",
        "written_mcid_count": 0,
        "skipped_mcid_count": len(writable),
    }


def _content_streams(page) -> list[Stream]:
    contents = page.get("/Contents", None)
    if contents is None:
        return []
    if isinstance(contents, Array):
        return [stream for stream in contents if hasattr(stream, "read_bytes") and hasattr(stream, "write")]
    if hasattr(contents, "read_bytes") and hasattr(contents, "write"):
        return [contents]
    return []


def _text_object_count(data: bytes) -> int:
    return len(TEXT_OBJECT_PATTERN.findall(data))


def _wrap_stream(stream: Stream, element: StructureElementPlan) -> None:
    data = stream.read_bytes()
    stream.write(_marked_content_prefix(element) + data + b"\nEMC\n")


def _wrap_text_objects(data: bytes, matches: list[re.Match[bytes]], elements: list[StructureElementPlan]) -> bytes:
    chunks: list[bytes] = []
    position = 0
    for match, element in zip(matches, elements, strict=True):
        chunks.append(data[position : match.start()])
        chunks.append(_marked_content_prefix(element))
        chunks.append(match.group(0))
        chunks.append(b"\nEMC")
        position = match.end()
    chunks.append(data[position:])
    return b"".join(chunks)


def _marked_content_prefix(element: StructureElementPlan) -> bytes:
    role = element.pdf_structure_role or "P"
    return f"/{role} <</MCID {element.mcid}>> BDC\n".encode("ascii")
