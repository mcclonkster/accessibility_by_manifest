from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any


def safe_value(value: Any, *, max_depth: int = 5) -> Any:
    if max_depth < 0:
        return repr(value)
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, bytes):
        return {
            "type": "bytes",
            "length": len(value),
            "preview_hex": value[:64].hex(),
        }
    if isinstance(value, Mapping):
        return {safe_key(key): safe_value(item, max_depth=max_depth - 1) for key, item in value.items()}
    if hasattr(value, "items") and callable(value.items):
        try:
            return {safe_key(key): safe_value(item, max_depth=max_depth - 1) for key, item in value.items()}
        except Exception:
            pass
    if hasattr(value, "read_bytes") and callable(value.read_bytes):
        try:
            stream_bytes = value.read_bytes()
        except Exception as exc:
            stream_bytes = None
            stream_error = str(exc)
        else:
            stream_error = None
        if stream_bytes is None and stream_error and "object of type" in stream_error:
            return str(value)
        return {
            "type": type(value).__name__,
            "object_ref": object_reference(value),
            "keys": safe_value(list(value.keys()), max_depth=max_depth - 1) if hasattr(value, "keys") else None,
            "byte_length": len(stream_bytes) if stream_bytes is not None else None,
            "preview_hex": stream_bytes[:128].hex() if stream_bytes is not None else None,
            "read_error": stream_error,
        }
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [safe_value(item, max_depth=max_depth - 1) for item in value]
    ref = object_reference(value)
    if ref:
        return {"object_ref": ref}
    indirect_reference = safe_getattr(value, "indirect_reference")
    if indirect_reference is not None:
        return safe_value(indirect_reference, max_depth=max_depth - 1)
    return str(value)


def safe_key(value: Any) -> str:
    if isinstance(value, str):
        return value
    return str(value)


def object_reference(value: Any) -> str | None:
    idnum = safe_getattr(value, "idnum")
    generation = safe_getattr(value, "generation")
    if idnum is not None and generation is not None:
        return f"{idnum} {generation} R"
    objgen = safe_getattr(value, "objgen")
    if isinstance(objgen, tuple) and len(objgen) == 2 and objgen != (0, 0):
        return f"{objgen[0]} {objgen[1]} R"
    return None


def safe_getattr(value: Any, name: str) -> Any:
    try:
        return getattr(value, name)
    except Exception:
        return None
