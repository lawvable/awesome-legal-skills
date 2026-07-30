"""Plain-text adapter: parse raw text (NOT a path) into NormalizedDoc.

No heavy third-party imports; pure stdlib.
"""
from __future__ import annotations
import re

from . import NormalizedDoc, DocBlock

_BLANK_SPLIT = re.compile(r"\n\s*\n")


def _looks_like_heading(text: str) -> bool:
    """Heuristic: short ALL-CAPS line, or short line ending with ':'."""
    stripped = text.strip()
    if not stripped or len(stripped) > 80:
        return False
    if stripped.endswith(":"):
        return True
    letters = [c for c in stripped if c.isalpha()]
    if letters and all(c.isupper() for c in letters):
        return True
    return False


def parse(src: str, **opts) -> NormalizedDoc:
    text = src if isinstance(src, str) else str(src)
    doc = NormalizedDoc(source_format="text")

    paragraphs = [p.strip() for p in _BLANK_SPLIT.split(text)]
    paragraphs = [p for p in paragraphs if p]

    if not paragraphs and text.strip():
        paragraphs = [text.strip()]

    current_heading = None
    for idx, para in enumerate(paragraphs):
        if _looks_like_heading(para):
            current_heading = para.rstrip(":").strip()
            doc.blocks.append(
                DocBlock(
                    text=current_heading,
                    block_type="heading",
                    idx=idx,
                    anchor=f"b{idx}",
                    parent_heading=None,
                )
            )
        else:
            doc.blocks.append(
                DocBlock(
                    text=para,
                    block_type="paragraph",
                    idx=idx,
                    anchor=f"b{idx}",
                    parent_heading=current_heading,
                )
            )

    return doc
