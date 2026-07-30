# Custom DPIA Report — Population Guide

How to populate `dpia-custom-template-v1.docx` with assessment data. Uses the OOXML editing workflow from the docx skill: unpack → Python scripts with Document library → repack.

## Setup

```bash
# 1. Read the docx skill's OOXML reference (ooxml.md) first
# 2. Unpack the template
python ooxml/scripts/unpack.py references/dpia-custom-template-v1.docx /tmp/dpia-custom
# 3. After all edits, repack
python ooxml/scripts/pack.py /tmp/dpia-custom output-dpia.docx
```

## Template Structure

- **21 tables** with header rows (dark navy `1B3A5C` background)
- **Placeholder text `____`** marks fields to fill (213 instances)
- **`[bracketed text]`** marks narrative placeholders to replace with content
- **Risk tables** use color-coded cell shading: Low=`E8F5E9`, Medium=`FFF8E1`, High=`FFF3E0`, Very High=`FFEBEE`
- **Header:** `____ — DPIA-YYYY-NNN — CONFIDENTIAL` (replace with org name + reference)
- **Footer:** Page numbers auto-generated

## Table Index

Tables are identified by their first header-row cell text.

| # | First Header Cell | Section | Operation |
|---|-------------------|---------|-----------|
| T1 | "Field" | Cover page | Fill Cells |
| T2 | "Version" | Document Control | Add Rows |
| T3 | "Verdict" | 1.3 Recommendation | Fill Cells |
| T4 | "Trigger" | 2.1 Art. 35(3) | Fill Cells |
| T5 | "#" | 2.2 Nine Criteria | Fill Cells |
| T6 | "Jurisdiction" | 2.3 Jurisdictional Scope | Add Rows |
| T7 | "Field" (Controller) | 3.1 Controller Info | Fill Cells |
| T8 | "Purpose" | 3.3 Legal Basis | Add Rows |
| T9 | "Category" | 3.4 Data Categories | Add Rows |
| T10 | "Group" | 3.5 Data Subjects | Add Rows |
| T11 | "Entity" | 3.9 Recipients | Add Rows |
| T12 | "Data Category" | 3.11 Retention | Add Rows |
| T13 | "Risk ID" | 5.2 Risk Register | Add Rows |
| T14 | "L \\ S" | 5.3 Inherent Heat Map | Fill Cells |
| T15 | "Risk ID" (2nd) | 6.1 Mitigation Measures | Add Rows |
| T16 | "Risk Level" | 7.1 Residual Summary | Fill Cells |
| T17 | "L \\ S" (2nd) | 7.2 Residual Heat Map | Fill Cells |
| T18 | "Verdict" (2nd) | 7.3 Overall Position | Fill Cells |
| T19 | "Field" (DPO) | 9 DPO Opinion | Fill Cells |
| T20 | "Field" (Review) | 11 Review | Fill Cells |
| T21 | "Role" | 12 Sign-Off | Fill Cells |

## Operation Types

### Fill Cells
Replace `____` placeholder text in existing cells with assessment data. Table structure stays fixed.

### Add Rows
Clone the first data row (row after header), then populate cloned rows with data. Remove template placeholder rows after.

### Fill Narrative
Replace `[bracketed placeholder]` paragraphs with assessment narrative text.

### Heat Map Population
Add Risk ID text to heat map cells at the correct L×S coordinates. The heat maps are 6-column tables (row label + 5 severity columns). Rows descend from L=5 to L=1.

## Table-by-Table Instructions

### T1 — Cover Page Info
| Row | "Value" Column Content |
|-----|----------------------|
| Processing Activity | Activity name from description phase |
| Controller | Controller name |
| Reference | DPIA-YYYY-NNN format reference |
| Version | Document version |
| Date | Assessment date |
| Classification | Keep CONFIDENTIAL or adjust |
| Status | DRAFT → FINAL when approved |

### T2 — Document Control
Clone data row for each version entry. Columns: Version | Date | Author | Changes | Approved By.

### T3 — Recommendation Verdict (Section 1.3)
Fill "Verdict" cell with one of: `APPROVED` / `CONDITIONALLY APPROVED` / `CONSULT SA` / `REJECTED`. Apply shading:
- APPROVED → `E8F5E9` (green)
- CONDITIONALLY APPROVED → `FFF8E1` (yellow)
- CONSULT SA → `FFF3E0` (orange)
- REJECTED → `FFEBEE` (red)

Fill "Justification" cell with summary text.

### T4 — Art. 35(3) Triggers
Three fixed rows. For each trigger:
- "Applies?" column: `Yes` or `No`
- "Analysis" column: reasoning text

### T5 — Nine Criteria
Nine fixed rows. For each criterion:
- "Met?" column: `Yes` / `No` / `Partially`
- "Reasoning" column: analysis text

Also replace `Criteria met: ____ / 9` paragraph below table.

### T6 — Jurisdictional Scope
Add one row per relevant jurisdiction. Columns: Jurisdiction | Why Relevant | Blacklist Checked | Match? | Entry Reference.

### T7 — Controller Information
Three fixed rows. Fill "Details" column: controller name, DPO contact, EU representative.

### T8 — Legal Basis per Purpose
Add one row per processing purpose. Columns: Purpose | Art. 6 Basis | Justification.
Also replace `Art. 9(2) exception` paragraph if applicable.

### T9 — Data Categories
Add one row per data category. Columns: Category | Special (Art. 9)? | Details.

### T10 — Data Subjects
Add one row per data subject group. Columns: Group | Vulnerable? | Approximate Number.

### T11 — Recipients
Add one row per recipient/processor. Columns: Entity | Role | Location | Transfer Mechanism.

### T12 — Retention Periods
Add one row per data category. Columns: Data Category | Retention Period | Justification.

### T13 — Inherent Risk Register (Section 5.2)
Add one row per risk. Columns:
- Risk ID: e.g., `DISC-01`, `SURV-02`
- Track: `A` or `B`
- Description: risk description
- Rights Category: affected right
- L: likelihood (1–5)
- S: severity (1–5)
- Score: L × S
- Modulating Factors: aggravating/mitigating factors or "None"
- Adjusted Level: `Low` / `Medium` / `High` / `Very High`

Apply cell shading to "Adjusted Level" cell based on level.

### T14 — Inherent Risk Heat Map (Section 5.3)
The 5×5 grid already has L×S scores and color shading. To populate: append Risk IDs to the cell text at matching coordinates.

Example: Risk `DISC-01` with L=3, S=4 → find cell at row L=3, column S=4 (which shows "12") → change to "12\nDISC-01".

Heat map layout (row index after header):
- Row 1: L=5 (columns: S=1→5, S=2→10, S=3→15, S=4→20, S=5→25)
- Row 2: L=4
- Row 3: L=3
- Row 4: L=2
- Row 5: L=1

### T15 — Mitigation Measures (Section 6.1)
Add one row per risk. Columns:
- Risk ID | Risk | Inherent (score) | Measures | Type (Tech/Org/Legal) | Status (Planned/Partial/Implemented) | Res. L | Res. S | Res. Score | Res. Level

Apply shading to "Res. Level" cell.

### T16 — Residual Risk Summary (Section 7.1)
Four fixed rows (Very High, High, Medium, Low — pre-shaded). Fill:
- "Count" column: number of risks at each level
- "Risk IDs" column: comma-separated list

### T17 — Residual Heat Map (Section 7.2)
Same as T14 but with residual risk positions. Same grid structure.

### T18 — Overall Position Verdict (Section 7.3)
Same as T3. Fill verdict + justification, apply verdict-color shading.

### T19 — DPO Opinion (Section 9)
Five fixed rows. Fill "Details" column: DPO name, recommendation, concerns, controller response, divergence.

### T20 — Review and Monitoring (Section 11)
Three fixed rows. Fill "Details" column: next review date, review cycle, review owner.

### T21 — Approval and Sign-Off (Section 12)
Five fixed rows (DPIA Author, DPO, Processing Owner, IT Security, Senior Management). Fill "Name" and "Date" columns. "Signature" column left blank for wet/digital signature.

## Narrative Placeholders

These `[bracketed text]` paragraphs should be replaced with assessment content:

| Section | Placeholder Text | Source |
|---------|-----------------|--------|
| 1.1 | [2–3 paragraph plain-language description...] | Description phase |
| 1.2 | [Top risks identified...] | Risk assessment |
| 1.4 | [DPO recommendation summary] | DPO consultation |
| 2.4 | [Why DPIA was conducted...] | Threshold assessment |
| 3.2 | [Processing purposes] | Description phase |
| 3.6 | [Where data is collected from] | Description phase |
| 3.7 | [Collection → Storage → Processing...] | Description phase |
| 3.7 | [Data flow diagram placeholder...] | Diagram (if available) |
| 3.8 | [Systems, platforms, algorithms...] | Description phase |
| 3.10 | [Transfer mechanisms...] | Description phase |
| 3.12 | [How Arts. 12–22 rights are facilitated] | Description phase |
| 4.1 | [Is each data element necessary?...] | Necessity assessment |
| 4.2 | [Benefits vs. intrusion analysis...] | Proportionality assessment |
| 4.3 | [LIA balancing test...] | Legal basis analysis |
| 4.4 | [Assessment of data minimisation...] | Necessity assessment |
| 4.5 | [Necessity and proportionality verdict...] | Necessity/proportionality gates |
| 6.2 | [Detailed description of technical measures] | Mitigation phase |
| 6.3 | [Detailed description of organisational measures] | Mitigation phase |
| 6.4 | [Detailed description of legal/contractual measures] | Mitigation phase |
| 7.4 | [Detailed justification...] | Residual risk assessment |
| 8 | [Decision: Prior consultation required?...] | Art. 36 check |
| 10 | [Decision: Consultation conducted?...] | Data subject consultation |
| 11 | [Material change in processing...] | Review setup |
| A–D | [Annex placeholders] | Supporting documentation |

## Header/Footer Replacement

Replace in `word/header1.xml`:
- `____` → organisation name
- `DPIA-YYYY-NNN` → actual reference number
- `CONFIDENTIAL` → actual classification (if different)

Footer is auto-generated (page numbers). The "Generated with DPIA Sentinel" text stays.

## OOXML Code Patterns

### Find table by header text
```python
from document import Document
doc = Document("word/document.xml")
tables = doc.get_nodes("//w:tbl")
for tbl in tables:
    first_cell_text = doc.get_text(doc.get_nodes(".//w:tc[1]", tbl)[0])
    if "Risk ID" in first_cell_text:
        # Found the risk register table
        break
```

### Replace placeholder text in cell
```python
for node in doc.get_nodes("//w:t"):
    if doc.get_text(node) == "____":
        doc.set_text(node, "replacement value")
        break
```

### Clone data row and populate
```python
table = ...  # found via header text
rows = doc.get_nodes("w:tr", table)
template_row = rows[1]  # first data row (after header)

import copy
new_row = copy.deepcopy(template_row)
cells = doc.get_nodes("w:tc", new_row)
for i, value in enumerate(["R-01", "A", "Description...", ...]):
    text_nodes = doc.get_nodes(".//w:t", cells[i])
    if text_nodes:
        doc.set_text(text_nodes[0], value)

table.addnext(new_row)  # or insert at specific position
```

### Apply risk-level cell shading
```python
RISK_COLORS = {"Low": "E8F5E9", "Medium": "FFF8E1", "High": "FFF3E0", "Very High": "FFEBEE"}

def shade_cell(doc, cell, level):
    tc_pr = doc.get_nodes("w:tcPr", cell)
    if not tc_pr:
        tc_pr = doc.create_element("w:tcPr")
        cell.insert(0, tc_pr)
    else:
        tc_pr = tc_pr[0]
    shd = doc.create_element("w:shd", {
        "w:val": "clear", "w:color": "auto", "w:fill": RISK_COLORS[level]
    })
    existing = doc.get_nodes("w:shd", tc_pr)
    if existing:
        tc_pr.remove(existing[0])
    tc_pr.append(shd)
```

### Replace narrative placeholder paragraph
```python
for para in doc.get_nodes("//w:p"):
    text = doc.get_text(para)
    if text.startswith("[") and text.endswith("]"):
        # Replace with assessment narrative
        runs = doc.get_nodes("w:r", para)
        for r in runs[1:]:
            para.remove(r)
        text_node = doc.get_nodes("w:t", runs[0])[0]
        doc.set_text(text_node, "Assessment narrative goes here...")
        break
```

## Data Source Mapping

| Assessment Phase | Populates |
|-----------------|-----------|
| Threshold assessment | T4, T5, T6, Section 2.4 narrative |
| Description | T1, T7, T8, T9, T10, T11, T12, Section 3 narratives |
| Necessity/Proportionality | Section 4 narratives |
| Inherent risk assessment | T13, T14 |
| Mitigation measures | T15, Section 6 narratives |
| Residual risk assessment | T16, T17, T18, Section 7.4 narrative |
| Art. 36 check | Section 8 narrative |
| DPO consultation | T19, Section 1.4 narrative |
| Data subject views | Section 10 narrative |
| Review setup | T20 |
| Final approval | T3, T18, T21, T1 (status), T2 |
| Executive summary | Section 1 narratives |
