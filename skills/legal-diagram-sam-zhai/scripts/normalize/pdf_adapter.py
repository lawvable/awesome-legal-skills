"""PDF adapter: parse text spans into NormalizedDoc with font-size heading inference.

Heavy import (PyMuPDF / fitz) is LAZY: imported inside parse(), never at module top.
pdfplumber is an optional lazy import for the table pass only; its absence degrades
to text-only behaviour with warning code PDF_TABLES_UNAVAILABLE.
"""
from __future__ import annotations

from . import DocTable, NormalizedDoc, DocBlock, limit_value, mark_truncated


def parse(src: str, pages=None, **opts) -> NormalizedDoc:
    import fitz  # lazy heavy import

    doc = NormalizedDoc(source_format="pdf")
    pdf = fitz.open(src)
    try:
        total = pdf.page_count
        max_pages = limit_value(opts, "max_pdf_pages")
        page_indices = list(pages) if pages is not None else list(range(total))
        if max_pages and len(page_indices) > max_pages:
            page_indices = page_indices[:max_pages]
            mark_truncated(doc, "PDF_PAGE_LIMIT_REACHED")

        idx = 0
        current_heading_path: list[str] = []
        for page_no in page_indices:
            page = pdf[page_no]
            data = page.get_text("dict")
            anchor = f"page{page_no + 1}"

            # Collect line-level spans with their max font size and bold flag.
            lines = []
            sizes = []
            for block in data.get("blocks", []):  # pyright: ignore[reportAttributeAccessIssue]
                for line in block.get("lines", []):
                    spans = line.get("spans", [])
                    line_text = "".join(s.get("text", "") for s in spans).strip()
                    if not line_text:
                        continue
                    max_size = max((s.get("size", 0.0) for s in spans), default=0.0)
                    is_bold = any(
                        bool(s.get("flags", 0) & 16) for s in spans
                    )
                    lines.append((line_text, max_size, is_bold))
                    sizes.append(max_size)

            if not lines:
                continue

            # Heading threshold: largest font on the page.
            max_page_size = max(sizes) if sizes else 0.0
            body_size = _median(sizes) if sizes else 0.0

            for line_text, size, is_bold in lines:
                is_heading = (
                    max_page_size > 0
                    and (size >= max_page_size - 0.1)
                    and (size > body_size or is_bold)
                )
                if is_heading:
                    current_heading_path = [line_text]
                doc.blocks.append(
                    DocBlock(
                        text=line_text,
                        block_type="heading" if is_heading else "paragraph",
                        idx=idx,
                        anchor=anchor,
                        heading_path=list(current_heading_path),
                    )
                )
                idx += 1
    finally:
        pdf.close()

    # Table pass: pdfplumber detects ruled tables; degrades gracefully if absent.
    _extract_tables(src, page_indices, doc, opts)

    return doc


def _extract_tables(src: str, page_indices: list[int], doc: NormalizedDoc, opts: dict) -> None:
    """Run the pdfplumber table pass, appending DocTable entries to doc.tables.

    Absent pdfplumber → logs PDF_TABLES_UNAVAILABLE and returns; does NOT set
    doc.truncated (absence is not truncation).  A table exceeding the cell cap
    triggers mark_truncated with PDF_TABLE_CELL_LIMIT_REACHED.
    """
    try:
        # sys.modules["pdfplumber"] = None makes this import raise ImportError
        # directly, so the except clause covers both missing and sabotaged installs.
        import pdfplumber  # optional lazy import
    except ImportError:
        if "PDF_TABLES_UNAVAILABLE" not in doc.warning_codes:
            doc.warning_codes.append("PDF_TABLES_UNAVAILABLE")
        return

    # Reuse the XLSX per-sheet cell cap as the per-table cap.
    cell_cap = limit_value(opts, "max_xlsx_cells_per_sheet")

    with pdfplumber.open(src) as pdf_pl:
        for page_no in page_indices:
            if page_no >= len(pdf_pl.pages):
                continue
            anchor = f"page{page_no + 1}"
            page = pdf_pl.pages[page_no]
            raw_tables = page.extract_tables() or []
            for raw in raw_tables:
                if not raw:
                    continue
                # First non-empty row becomes the header; subsequent rows are data.
                headers = [str(cell or "").strip() for cell in raw[0]]
                data_rows = raw[1:]

                if cell_cap:
                    n_cols = max(len(headers), 1)
                    max_rows = cell_cap // n_cols
                    if len(data_rows) > max_rows:
                        data_rows = data_rows[:max_rows]
                        mark_truncated(doc, "PDF_TABLE_CELL_LIMIT_REACHED")

                rows = [[str(cell or "").strip() for cell in row] for row in data_rows]
                doc.tables.append(DocTable(headers=headers, rows=rows, anchor=anchor))


def _median(values) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2.0
