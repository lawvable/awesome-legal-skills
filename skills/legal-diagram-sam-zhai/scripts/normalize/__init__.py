from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, Tuple
import re

DEFAULT_LIMITS = {
    "max_file_bytes": 25 * 1024 * 1024,
    "max_pdf_pages": 50,
    "max_docx_paragraphs": 5000,
    "max_docx_tables": 200,
    "max_docx_table_rows": 5000,
    "max_pptx_slides": 200,
    "max_pptx_text_shapes": 5000,
    "max_xlsx_sheets": 20,
    "max_xlsx_rows_per_sheet": 1000,
    "max_xlsx_cells_per_sheet": 50000,
}

@dataclass
class DocBlock:
    text: str
    block_type: str                       # heading | paragraph | list_item | table_cell | table_row
    idx: int = 0
    level: Optional[int] = None
    style: Optional[str] = None
    anchor: str = ""
    parent_heading: Optional[str] = None
    heading_path: List[str] = field(default_factory=list)
    list_ordinal: Optional[str] = None
    table_coords: Optional[Tuple[int, int]] = None
    lang: str = "en"                      # effective language; set by the W3.1 block pass

@dataclass
class DocTable:
    headers: List[str]
    rows: List[List[str]]
    anchor: str
    caption: Optional[str] = None

@dataclass
class NormalizedDoc:
    blocks: List[DocBlock] = field(default_factory=list)
    tables: List[DocTable] = field(default_factory=list)
    headings_tree: Dict[str, Any] = field(default_factory=dict)
    source_format: str = "text"
    truncated: bool = False
    structure_metrics: Dict[str, int] = field(default_factory=dict)
    warning_codes: List[str] = field(default_factory=list)

_MARKDOWN_HINTS = [
    re.compile(r"^#{1,6}\s+", re.M),
    re.compile(r"^\s*(?:[-*]|\d+\.)\s+", re.M),
    re.compile(r"^\s*\|.+\|\s*$", re.M),
]

def normalize(src: str, kind: str, **opts) -> NormalizedDoc:
    if kind in ("md", "txt"):
        from .md_adapter import parse as p
    elif kind == "docx":
        from .docx_adapter import parse as p
    elif kind == "pdf":
        from .pdf_adapter import parse as p
    elif kind in ("xlsx", "xls", "csv"):
        from .xlsx_adapter import parse as p
    elif kind == "pptx":
        from .pptx_adapter import parse as p
    else:
        from .text_adapter import parse as p
    doc = p(src, **opts)
    _finalize_doc(doc)
    return doc


def normalize_stdin_text(text: str) -> NormalizedDoc:
    if looks_like_markdown(text):
        from .md_adapter import parse_text
        doc = parse_text(text, source_format="md_stdin")
    else:
        from .text_adapter import parse
        doc = parse(text)
    _finalize_doc(doc)
    return doc


def looks_like_markdown(text: str) -> bool:
    return sum(1 for rx in _MARKDOWN_HINTS if rx.search(text or "")) >= 1


def _finalize_doc(doc: NormalizedDoc) -> None:
    if not getattr(doc, "structure_metrics", None):
        blocks = list(getattr(doc, "blocks", []) or [])
        doc.structure_metrics = {
            "headings": sum(1 for b in blocks if getattr(b, "block_type", "") == "heading"),
            "lists": sum(1 for b in blocks if getattr(b, "block_type", "") == "list_item"),
            "tables": len(list(getattr(doc, "tables", []) or [])),
            "paragraphs": sum(1 for b in blocks if getattr(b, "block_type", "") == "paragraph"),
            "blocks": len(blocks),
        }
    if not getattr(doc, "warning_codes", None):
        doc.warning_codes = []
    if not getattr(doc, "blocks", None) and not getattr(doc, "tables", None):
        doc.warning_codes.append("SOURCE_UNPARSEABLE_OR_EMPTY")


def limit_value(opts: Dict[str, Any], name: str) -> int:
    raw = opts.get(name, DEFAULT_LIMITS[name])
    if raw is None:
        return 0
    value = int(raw)
    if value < 0:
        raise ValueError(f"{name} must be non-negative")
    return value


def mark_truncated(doc: NormalizedDoc, code: str) -> None:
    doc.truncated = True
    if code not in doc.warning_codes:
        doc.warning_codes.append(code)
