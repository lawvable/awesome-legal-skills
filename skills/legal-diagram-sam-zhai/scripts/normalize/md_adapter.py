"""Markdown adapter: structure-preserving parse of Markdown into NormalizedDoc.

Paragraph joining (W6 T2 Defect A fix):
    Standard Markdown separates paragraphs with blank lines.  Hard-wrapped
    prose (line break within a paragraph, no intervening blank line) is joined
    into a single block so that sentence segmentation sees complete sentences
    instead of truncated line fragments.  This mirrors the GitHub Flavored
    Markdown and CommonMark paragraph rule: a blank line terminates a paragraph;
    a bare line break is a soft wrap within the same paragraph.

List-item continuation (W6 T2 Defect F fix):
    Only indented lines may continue a list item.  A flush-left non-list line
    after a list item starts a new paragraph block (structural safety over
    CommonMark lazy continuation; prevents obligation-text absorption).

Fenced code blocks (W6 T2 Defect F fix):
    Fence-delimited regions (``` or ~~~) are consumed silently.  Fence lines
    act as paragraph-join breakers so surrounding prose is emitted separately.
"""
from __future__ import annotations
import re

from . import NormalizedDoc, DocBlock, DocTable

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
_ORDERED_RE = re.compile(r"^\s*(\d+\.)\s+(.*)$")
_UNORDERED_RE = re.compile(r"^\s*([-*])\s+(.*)$")
_FENCE_RE = re.compile(r"^(`{3,}|~{3,})")


def _split_row(line: str) -> list:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _is_separator_row(line: str) -> bool:
    cells = _split_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{1,}:?", c) for c in cells if c != "")


def _is_structural_line(line: str) -> bool:
    """Return True for lines that cannot continue a paragraph (heading, list, table, blank, fence)."""
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith("|"):
        return True
    if _HEADING_RE.match(stripped):
        return True
    if _ORDERED_RE.match(line) or _UNORDERED_RE.match(line):
        return True
    if _FENCE_RE.match(stripped):
        return True
    return False


def parse(src: str, **_opts) -> NormalizedDoc:
    with open(src, "r", encoding="utf-8") as fh:
        return parse_text(fh.read(), source_format="md")


def parse_text(text: str, *, source_format: str = "md") -> NormalizedDoc:
    lines = text.splitlines()
    doc = NormalizedDoc(source_format=source_format)
    heading_stack: list[tuple[int, str]] = []
    heading_counter = 0
    sub_counter = 0
    idx = 0
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.lstrip().startswith("|"):
            table_lines = []
            while i < n and lines[i].lstrip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            if table_lines:
                headers = [h for h in _split_row(table_lines[0]) if h != ""]
                data_rows = []
                for tl in table_lines[1:]:
                    if _is_separator_row(tl):
                        continue
                    data_rows.append(_split_row(tl))
                anchor = f"§{heading_counter}#t{len(doc.tables)}"
                doc.tables.append(DocTable(headers=headers, rows=data_rows, anchor=anchor, caption=_current_heading(heading_stack)))
            continue
        m = _HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            heading_counter += 1
            sub_counter = 0
            text_value = m.group(2).strip()
            while heading_stack and heading_stack[-1][0] >= level:
                heading_stack.pop()
            heading_stack.append((level, text_value))
            doc.blocks.append(
                DocBlock(
                    text=text_value,
                    block_type="heading",
                    idx=idx,
                    level=level,
                    anchor=f"§{heading_counter}",
                    parent_heading=_parent_heading(heading_stack),
                    heading_path=[h for _, h in heading_stack],
                )
            )
            idx += 1
            i += 1
            continue
        mm = _ORDERED_RE.match(line) or _UNORDERED_RE.match(line)
        if mm:
            sub_counter += 1
            # Collect continuation lines into the list item text.
            # Only indented lines (leading whitespace) may continue a list item.
            # A flush-left non-list line starts a new block (structural safety over
            # CommonMark lazy-continuation; prevents obligation text absorption).
            item_lines = [mm.group(2).strip()]
            j = i + 1
            while j < n:
                next_line = lines[j].rstrip()
                if not next_line.strip():
                    break
                if _HEADING_RE.match(next_line) or next_line.lstrip().startswith("|"):
                    break
                if _ORDERED_RE.match(next_line) or _UNORDERED_RE.match(next_line):
                    break
                if _FENCE_RE.match(next_line.strip()):
                    break
                # Only accept indented continuation (leading whitespace required).
                if not next_line[0:1].strip() == "":
                    break
                item_lines.append(next_line.strip())
                j += 1
            doc.blocks.append(
                DocBlock(
                    text=" ".join(item_lines),
                    block_type="list_item",
                    idx=idx,
                    anchor=f"§{heading_counter}#{sub_counter}",
                    parent_heading=_current_heading(heading_stack),
                    heading_path=[h for _, h in heading_stack],
                    list_ordinal=mm.group(1),
                )
            )
            idx += 1
            i = j
            continue
        # Fenced code block: consume opening fence, content, and closing fence.
        # The fence region is silently skipped -- its content is not text to extract.
        fm = _FENCE_RE.match(line.strip())
        if fm:
            fence_marker = fm.group(1)
            i += 1
            while i < n:
                fence_line = lines[i].rstrip()
                i += 1
                if _FENCE_RE.match(fence_line.strip()) and fence_line.strip().startswith(fence_marker[0]):
                    break
            continue
        # Paragraph: collect consecutive non-blank, non-structural lines into one block.
        para_lines = [line.strip()]
        i += 1
        while i < n:
            next_line = lines[i].rstrip()
            if not next_line.strip():
                break
            if _is_structural_line(next_line):
                break
            para_lines.append(next_line.strip())
            i += 1
        sub_counter += 1
        doc.blocks.append(
            DocBlock(
                text=" ".join(para_lines),
                block_type="paragraph",
                idx=idx,
                anchor=f"§{heading_counter}#{sub_counter}",
                parent_heading=_current_heading(heading_stack),
                heading_path=[h for _, h in heading_stack],
            )
        )
        idx += 1
    return doc


def _current_heading(stack: list[tuple[int, str]]) -> str | None:
    return stack[-1][1] if stack else None


def _parent_heading(stack: list[tuple[int, str]]) -> str | None:
    return stack[-2][1] if len(stack) > 1 else None
