"""W4.1 PDF table adapter tests: pdfplumber hybrid, degradation, cell-cap.

Standalone-runnable: python scripts/tests/test_pdf_tables.py
Also discoverable by pytest. No pytest fixtures; no parametrize (plain loops
keep the bare __main__ runner working, W0 convention).
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTRACT = ROOT / "extract_entities.py"

sys.path.insert(0, str(ROOT))


# ---------------------------------------------------------------------------
# Synthetic PDF factory
# ---------------------------------------------------------------------------

def _make_table_pdf(tmp_dir: str) -> str:
    """Author a PDF with body text and a drawn ruled table that pdfplumber detects.

    Layout (all on page 1):
    - Heading text: "Test Agreement"
    - Body paragraph: "This agreement sets out the obligations of each party."
    - Ruled table, 2 columns × 2 rows (header + 1 data):
        Party | Obligation
        Seller | must deliver goods

    Cell boundaries are drawn with draw_rect so pdfplumber's line-intersection
    algorithm detects a table; text is inserted inside each cell boundary.
    """
    import fitz  # PyMuPDF

    doc = fitz.open()
    page = doc.new_page(width=612, height=792)

    # Heading (larger font so the adapter infers it as a heading)
    page.insert_text((50, 60), "Test Agreement", fontsize=16)

    # Body paragraph
    page.insert_text((50, 90), "This agreement sets out the obligations of each party.", fontsize=11)

    # Ruled table: two columns, header row + one data row
    col0 = (50, 250)   # left, right x
    col1 = (250, 450)
    row0 = (110, 140)  # top, bottom y (header)
    row1 = (140, 170)  # top, bottom y (data)

    for left, right in (col0, col1):
        for top, bottom in (row0, row1):
            page.draw_rect(
                fitz.Rect(left, top, right, bottom),
                color=(0, 0, 0),
                fill=None,
                width=0.5,
            )

    # Cell text
    page.insert_text((col0[0] + 5, row0[1] - 8), "Party", fontsize=10)
    page.insert_text((col1[0] + 5, row0[1] - 8), "Obligation", fontsize=10)
    page.insert_text((col0[0] + 5, row1[1] - 8), "Seller", fontsize=10)
    page.insert_text((col1[0] + 5, row1[1] - 8), "must deliver goods", fontsize=10)

    path = os.path.join(tmp_dir, "table_test.pdf")
    doc.save(path)
    doc.close()
    return path


def _make_large_table_pdf(tmp_dir: str, n_rows: int) -> str:
    """Author a PDF with a table that has n_rows data rows (+ 1 header row).

    Each row has two cells: Party | Obligation.
    Uses a compact row height so all rows fit on one page up to ~200 rows.
    """
    import fitz

    doc = fitz.open()
    row_h = 15
    # Ensure page is tall enough for all rows
    page_height = max(792, 80 + (n_rows + 2) * row_h + 50)
    page = doc.new_page(width=612, height=page_height)

    page.insert_text((50, 50), "Large Table Agreement", fontsize=14)

    col0 = (50, 250)
    col1 = (250, 450)

    y_top = 70
    all_rows = [("Party", "Obligation")] + [(f"Party{i}", f"must do item {i}") for i in range(n_rows)]

    for r_idx, (c0_text, c1_text) in enumerate(all_rows):
        top = y_top + r_idx * row_h
        bottom = top + row_h
        for left, right in (col0, col1):
            page.draw_rect(fitz.Rect(left, top, right, bottom), color=(0, 0, 0), fill=None, width=0.5)
        page.insert_text((col0[0] + 3, bottom - 3), c0_text, fontsize=8)
        page.insert_text((col1[0] + 3, bottom - 3), c1_text, fontsize=8)

    path = os.path.join(tmp_dir, "large_table_test.pdf")
    doc.save(path)
    doc.close()
    return path


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_table_blocks_present_and_page_anchored() -> None:
    """NormalizedDoc from a table-bearing PDF carries DocTable entries with page1 anchor."""
    from normalize import normalize

    with tempfile.TemporaryDirectory() as tmp:
        pdf_path = _make_table_pdf(tmp)
        doc = normalize(pdf_path, "pdf")

    assert doc.tables, "expected at least one DocTable from the table-bearing PDF"
    t = doc.tables[0]
    assert t.anchor == "page1", f"expected anchor='page1', got {t.anchor!r}"
    # Headers must include Party and Obligation columns
    headers_lower = [h.lower() for h in t.headers]
    assert any("party" in h for h in headers_lower), f"Party column missing from headers: {t.headers}"
    assert any("obligation" in h for h in headers_lower), f"Obligation column missing from headers: {t.headers}"
    # At least one data row
    assert t.rows, "expected at least one data row"
    all_cells = [c for row in t.rows for c in row]
    assert any("seller" in c.lower() for c in all_cells), f"Seller not found in rows: {t.rows}"


def test_text_blocks_still_present() -> None:
    """Text blocks extracted by PyMuPDF remain intact after pdfplumber table pass."""
    from normalize import normalize

    with tempfile.TemporaryDirectory() as tmp:
        pdf_path = _make_table_pdf(tmp)
        doc = normalize(pdf_path, "pdf")

    block_texts = [b.text for b in doc.blocks]
    joined = " ".join(block_texts).lower()
    assert "test agreement" in joined, f"heading text missing from blocks: {block_texts[:5]}"
    assert "obligations of each party" in joined, f"body text missing from blocks: {block_texts[:5]}"


def test_extraction_table_candidate_has_page_provenance() -> None:
    """End-to-end: extraction engine yields at least one candidate from a table row with page provenance."""
    with tempfile.TemporaryDirectory() as tmp:
        pdf_path = _make_table_pdf(tmp)
        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        proc = subprocess.run(  # audit-ok: dangerous-python: fixed command, sys.executable + own scripts, no user input
            [sys.executable, str(EXTRACT), "--input", pdf_path, "--matter_type", "deal"],
            text=True,
            capture_output=True,
            env=env,
            timeout=60,
        )
    assert proc.returncode == 0, proc.stderr
    import json
    data = json.loads(proc.stdout)
    # Candidate manifest must have at least one table-sourced candidate.
    # Discriminate on table_coords (non-None only for rows from _table_source_ref);
    # plain text-block candidates carry page but not table_coords, so this filter
    # cannot pass vacuously when zero tables are detected.
    cm = data.get("candidate_manifest", {})
    candidates = cm.get("candidates", [])
    table_candidates = [
        c for c in candidates
        if c.get("source_ref", {}).get("table_coords") is not None
    ]
    assert table_candidates, (
        "expected at least one candidate with table_coords provenance (table row source_ref)"
    )
    # PDF table rows anchor to "page{N}" so page must be populated.
    paged = [c for c in table_candidates if c.get("source_ref", {}).get("page") is not None]
    assert paged, f"expected page-anchored table candidates; got: {[c.get('source_ref') for c in table_candidates[:3]]}"


def test_pdfplumber_absent_graceful_degradation() -> None:
    """When pdfplumber is not importable, parse succeeds with empty tables and PDF_TABLES_UNAVAILABLE code."""
    import importlib
    import sys as _sys

    # Sabotage pdfplumber import by temporarily inserting None sentinel
    _original = _sys.modules.get("pdfplumber", _SENTINEL := object())
    _sys.modules["pdfplumber"] = None  # type: ignore[assignment]

    # Also unload the pdf_adapter module so it re-executes the import
    _adapter_key = "normalize.pdf_adapter"
    _adapter_mod = _sys.modules.pop(_adapter_key, None)
    # Force re-import of normalize.pdf_adapter with pdfplumber sabotaged
    try:
        from normalize import normalize

        with tempfile.TemporaryDirectory() as tmp:
            pdf_path = _make_table_pdf(tmp)
            doc = normalize(pdf_path, "pdf")

        assert not doc.tables, f"expected empty tables list, got: {doc.tables}"
        assert "PDF_TABLES_UNAVAILABLE" in doc.warning_codes, (
            f"expected PDF_TABLES_UNAVAILABLE in warning_codes: {doc.warning_codes}"
        )
        # Absence is NOT truncation
        assert not doc.truncated, (
            "doc.truncated must be False when pdfplumber is simply absent"
        )
        # Text blocks must still be present (PyMuPDF path unchanged)
        block_texts = [b.text for b in doc.blocks]
        joined = " ".join(block_texts).lower()
        assert "test agreement" in joined, f"heading text missing from blocks: {block_texts[:5]}"
    finally:
        # Restore pdfplumber import state
        if _original is _SENTINEL:
            _sys.modules.pop("pdfplumber", None)
        else:
            _sys.modules["pdfplumber"] = _original  # type: ignore[assignment]
        # Restore pdf_adapter so subsequent tests use the real one
        if _adapter_mod is not None:
            _sys.modules[_adapter_key] = _adapter_mod
        else:
            _sys.modules.pop(_adapter_key, None)
        # Force re-import so the real module is active
        importlib.invalidate_caches()


def test_cell_cap_triggers_truncation() -> None:
    """A table exceeding the per-table cell cap is truncated with PDF_TABLE_CELL_LIMIT_REACHED."""
    from normalize import normalize

    with tempfile.TemporaryDirectory() as tmp:
        # Build a table with 20 data rows so we can use a low cap of 10 cells
        pdf_path = _make_large_table_pdf(tmp, n_rows=20)
        # Pass max_xlsx_cells_per_sheet=10: 1 header row (2 cells) + data rows
        # The cap covers cells across the whole table, so 10 cells = 5 rows of 2 cols
        doc = normalize(pdf_path, "pdf", max_xlsx_cells_per_sheet=10)

    # The cap bounds DATA cells per table: rows x cols <= cap (header row exempt).
    assert doc.tables, "expected at least one table"
    t = doc.tables[0]
    assert len(t.rows) * max(len(t.headers), 1) <= 10, (
        f"table not capped: rows={len(t.rows)}, cols={len(t.headers)}"
    )
    assert doc.truncated, "doc.truncated must be True when cell cap is hit"
    assert "PDF_TABLE_CELL_LIMIT_REACHED" in doc.warning_codes, (
        f"expected PDF_TABLE_CELL_LIMIT_REACHED in warning_codes: {doc.warning_codes}"
    )


if __name__ == "__main__":
    tests = [
        value for name, value in sorted(globals().items())
        if name.startswith("test_") and callable(value)
    ]
    for test in tests:
        test()
    print(f"{len(tests)} tests passed")
