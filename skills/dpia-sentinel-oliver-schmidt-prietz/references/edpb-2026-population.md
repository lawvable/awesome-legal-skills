# EDPB 2026 DPIA Template — Population Guide

> For use with the official EDPB template at `references/edpb-2026-template-v1.docx`.

This guide maps each table and placeholder in the official EDPB DPIA template to the assessment data that fills it. Use the OOXML editing workflow (unpack → manipulate → repack) from the docx editing skill.

---

## Workflow

```
1. Copy references/edpb-2026-template-v1.docx to working directory
2. Unpack: python ooxml/scripts/unpack.py template.docx unpacked/
3. Read ooxml.md reference for Document library API
4. Run population script(s) against unpacked/word/document.xml
5. Repack: python ooxml/scripts/pack.py unpacked/ output-dpia.docx
```

---

## Table Index

The template contains 35 tables. Each is identified by its position and first-row content.

| Table | EDPB Section | Operation | Identification Pattern (first row text) |
|-------|-------------|-----------|----------------------------------------|
| 0 | Version history | Skip | `Version`, `Date`, `Adoption information` |
| 1 | 0.1 Controller(s) | Fill cells | `Controller` |
| 2 | 0.2 Processor(s) | Add rows | `Processor`, `Definition of their obligations` |
| 3 | 0.3 Name | Fill cells | `Internal name given to the processing` |
| 4 | 0.4 Planning | Fill cells | `Estimated launch date` |
| 5 | 0.5 DPIA tech sheet | Fill cells | `Current version and version log` |
| 6 | 1.1.a Personal data | Add rows | `Processed personal data (item or element)` |
| 7 | 1.1.b Purposes | Add rows | `Purpose: specific and explicit reasons` |
| 8 | 1.1.c Secondary uses | Add rows | `Secondary or compatible uses` |
| 9 | 1.1.d Nature/scope/context | Fill narrative | `Nature of the processing` |
| 10 | 1.2 Functional description | Add rows | `Processing phase or stage`, `Type of operations` |
| 11 | 1.3 Assets | Add rows | `Means of processing and supporting assets` |
| 12 | 1.4 Codes of conduct | Add rows | `Code of conduct` |
| 13 | 2.1.a Legal basis | Add rows | `Purpose/use`, `Legal basis (Article 6(1) GDPR)` |
| 14 | 2.1.b Art. 9(2) lift | Add rows | `Special category of personal data`, `Reasons to lift` |
| 15 | 2.2.a Minimisation/retention | Add rows | `Justification of the need`, `Recipients`, `Retention period` |
| 16 | 2.2.b Data quality | Add rows | `Quality metrics, requirements or thresholds` |
| 17 | 2.3.a Art. 5 measures | Fill cells | `Compliance with Article 5(1)(a-f)` |
| 18 | 2.3.b Data subject rights | Fill cells | `Data subject rights` |
| 19 | 2.3.c Other GDPR | Fill cells | `Compliance with other GDPR requirements` |
| 20 | 2.3.d DP by design | Fill + add rows | `Data protection by design and by default` |
| 21 | 2.3.e Security | Fill + add rows | `Security of processing (Article 32 GDPR)` |
| 22 | 3.1 Inherent impacts | Add rows | `Threats posed by the processing, as it has been designed` |
| 23 | 3.2 Necessity | Fill narrative | `Evaluate if the envisaged processing is effective` |
| 24 | 3.3 Proportionality | Fill narrative | `Discuss the importance of the processing` |
| 25 | 4.1.a Operational impacts | Add rows | `Threats posed by malfunctions and deviations` |
| 26 | 4.1.b Method | Fill narrative | `Likelihood and severity levels and their meanings` |
| 27 | 4.1.c Inherent risk | Add rows | `Risks to the data subject's rights and freedoms` |
| 28 | 4.2.a Additional measures | Add rows | `Technical, legal/contractual and organisational measures` |
| 29 | 4.2.b Residual risk | Add rows | `Reassessed risks to the data subject's rights` |
| 30 | 4.2.c Plan | Fill narrative | `Specific activities, responsible team, timelines` |
| 31 | 5.1 DPO advice | Fill narrative | `If there is a DPO` |
| 32 | 5.2 Data subjects' views | Fill narrative | `Where appropriate, provide the data subjects'` |
| 33 | 6 Conclusion | Mark decision | `REJECTED`, `CONSULTATION`, `APPROVED` |
| 34 | 6 Justification | Fill narrative | (empty cell after conclusion) |

---

## Operation Types

### Fill Cells

Tables with pre-defined label rows. Locate the row by its label text, then fill the adjacent empty cell.

```python
# Pattern: find row by label, set adjacent cell
from document import Document
doc = Document("unpacked")
# Use get_node to find the text, navigate to parent cell, then sibling cell
node = doc.get_node("xpath", ".//w:t[contains(text(), 'Controller')]")
# Navigate: w:t → w:r → w:p → w:tc (this cell) → next w:tc (target cell)
# Set text in target cell
```

### Add Rows

Tables with a header row and one or more template data rows. Clone the last data row for each additional entry, then fill cell content.

```python
# Pattern: find table, clone last row, fill cells
# 1. Find table by header text
# 2. Get the last w:tr (template row)
# 3. For each data item: deep-clone the template row, clear cell text, set new text
# 4. Insert cloned rows before closing </w:tbl>
# 5. Optionally remove the original empty template row
```

### Fill Narrative

Single-cell tables containing instructional placeholder text. Replace the placeholder text entirely with assessment content.

```python
# Pattern: find cell by placeholder text, replace all w:t content
node = doc.get_node("xpath", ".//w:t[contains(text(), 'Evaluate if the envisaged')]")
# Clear existing text, set assessment narrative
```

### Mark Decision

The conclusion table (Table 33) contains all four decision options as text. Bold or highlight the selected decision, and add ☑ before it (replacing the implicit checkbox space).

---

## Table-by-Table Population

### Table 0 — Version History (skip)

Leave as-is. This is the EDPB document's own version history, not the DPIA's.

### Table 1 — 0.1 Controller(s)

| Row Label | Fill With |
|-----------|-----------|
| Controller | Controller name / legal entity |
| Management units responsible... | Department(s) managing the processing |
| Main establishment/point of contact... | Address, contact person, EU representative |
| Information about the DPO... | DPO name, email, phone |

For joint controllers: clone the entire table, one per controller, adding obligations/tasks row.

### Table 2 — 0.2 Processor(s) and Sub-processor(s)

3 columns: `#` | `Processor` | `Definition of their obligations and tasks`

Add one row per processor/sub-processor. Number sequentially (1, 2, ... N).

**Data source:** Processing description → processor chain.

### Table 3 — 0.3 Name of the Processing

| Row Label | Fill With |
|-----------|-----------|
| Internal name... | Processing activity name (from ROPA) |
| Current version... | Version history of the processing itself |

### Table 4 — 0.4 Planning

| Row Label | Fill With |
|-----------|-----------|
| Estimated launch date | Date or "TBD" |
| Estimated end date or expiration conditions | Date, conditions, or "Ongoing" |

### Table 5 — 0.5 DPIA Technical Sheet

8 rows to fill:

| Row | Fill With |
|-----|-----------|
| Current version and version log | "v1.0 — [date]" + any prior versions |
| Team involved in conducting this DPIA | Names, roles (consider RACI matrix) |
| Guidelines, standards, codes of conduct... | "EDPB Guidelines WP 248 rev.01, EDPB DPIA Template v1.0 (March 2026), [national guidance]" |
| Reasons to conduct the DPIA | See checkbox handling below |
| Scope of this DPIA | What is included/excluded and why |
| Completion date | Date |
| Formal validation date | Date (requires responsible official sign-off) |
| Is the DPIA intended to be published... | Select option, fill "How?" if applicable |

**Checkbox handling for "Reasons to conduct the DPIA":** This row contains multiple text blocks with checkbox-style indentation. To mark a reason as selected, insert "☑ " before the selected items and "☐ " before unselected items. The text blocks are:

Art. 35(3) mandatory triggers:
- Systematic and extensive evaluation... (automated profiling)
- Processing on a large scale of special categories...
- Systematic monitoring of a publicly accessible area...

EDPB criteria:
- Evaluation or scoring
- Automated-decision making with legal or similar significant effect
- Systematic monitoring
- Sensitive data or data of a highly personal nature
- Data processed on a large scale
- Matching or combining datasets
- Data concerning vulnerable data subjects
- Innovative use or applying new technological or organisational solutions
- When the processing prevents data subjects from exercising a right

Other triggers:
- National law requirement (fill explanation)
- DPO opinion
- Data subjects' opinion
- Code of conduct requirement
- Other (fill explanation)
- Existing processing that changed (fill explanation)

**Publication intent:** Replace placeholder text after "Yes it is going to be published: How?" or "Yes, it is going to be shared externally: How?" with actual details.

### Table 6 — 1.1.a Processed Personal Data

4 columns: `#` | `Processed personal data (item or element)` | `Explanation` | `Special category`

Add one row per personal data item. For the special category column:
- If not special: set text to "No"
- If special: set text to "Yes:" followed by the applicable category text (e.g., "Data concerning health")

**Data source:** Description phase → data categories.

### Table 7 — 1.1.b Purposes

3 columns: `#` | `Purpose` | `Personal data involved + justification`

Add one row per processing purpose. Cross-reference data items from Table 6.

### Table 8 — 1.1.c Secondary Uses

3 columns: `#` | `Secondary or compatible uses` | `Personal data involved + conditions + compatibility assessment`

Add rows only if secondary uses exist. If none, add a single row: "No secondary or compatible uses identified."

### Table 9 — 1.1.d Nature, Scope, Context

3 narrative rows:

| Row | Fill With |
|-----|-----------|
| Nature of the processing | Operations involved, technologies used |
| Scope of the processing | Volume, scale, frequency, duration from data subject perspective |
| Context of the processing | Use cases, business process, relationship with data subjects, vulnerable groups |

After the table, there are two Yes/No questions with placeholder text:
- "Is this a cross-border processing?" → Replace "☐ No" / "☐ Yes (justification and details): ____________"
- "Is personal data going to be transferred...?" → Same pattern

Mark the applicable option with ☑ and fill justification if Yes.

### Table 10 — 1.2 Functional Description

4 columns: `#` | `Processing phase or stage` | `Type of operations` | `Explanation`

Add one row per lifecycle phase. The "Type of operations" column contains checkboxes for:
- Collection / Use / Storage / Sharing and Transfer / Deletion and Destruction

Mark applicable types with ☑, others with ☐.

**Data source:** Description phase → data lifecycle (Collection → Use → Storage → Sharing → Deletion).

### Table 11 — 1.3 Means of Processing / Assets

3 columns: `Processing phase or stage` | `Means of processing and supporting assets` | `Explanation`

Add one row per asset group. Group by: hardware/infrastructure, software, APIs/models, personnel, sites/premises, organisational assets.

**Data source:** Asset Inventory phase.

### Table 12 — 1.4 Codes of Conduct

3 columns: `#` | `Code of conduct` | `Explanation`

Add rows for applicable codes. Mark checkbox: "Compliance is likely to be required" or "Compliance is necessary or beneficial" with ☑ and fill "Why?".

### Table 13 — 2.1.a Legal Basis

3 columns: `Purpose/use` | `Legal basis (Art. 6(1) GDPR)` | `Justification`

Add one row per purpose (from Table 7) + secondary use (from Table 8). The legal basis column contains Art. 6(1)(a-f) as checkbox options. Mark the applicable basis with ☑.

For Art. 6(1)(f) legitimate interest: fill the justification column with the LIA balancing test result.

### Table 14 — 2.1.b Reasons to Lift Processing Prohibition

3 columns: `Special category data item` | `Art. 9(2) reason` | `Justification`

Only populate if special category data exists (from Table 6). The Art. 9(2) column contains (a)-(j) as checkbox options. Mark applicable reason with ☑.

### Table 15 — 2.2.a Data Minimisation and Retention

6 columns: `Data item` | `Need justification` | `Recipients` | `Recipient justification` | `Retention period` | `Retention justification`

Add one row per data item from Table 6.

**Data source:** Necessity phase → data minimisation review.

### Table 16 — 2.2.b Data Quality

3 columns: `Data item` | `Quality metrics/requirements/thresholds` | `Justification`

Add one row per data item where quality is relevant (especially for AI/ML systems, automated decisions).

### Tables 17–21 — 2.3.a–e Measures Supporting Compliance

All follow the same 4-column pattern: `Requirement/Principle` | `List of measures` | `Discussion` | `Implementation status`

**Table 17 — Art. 5 measures:** 8 pre-defined rows (fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity/confidentiality, accountability). Fill columns 2-4 for each.

**Table 18 — Data subject rights:** 5 pre-defined rows (information Arts. 12-14, access/portability Arts. 15+20, rectification/erasure Arts. 16-17+19, object/restriction Arts. 18-19+21, no automated decisions Art. 22). Fill columns 2-4.

**Table 19 — Other GDPR:** 3 pre-defined rows (consent Art. 7, processors Art. 28, international transfers Chapter V). Fill columns 2-4.

**Table 20 — DP by design:** 2 template rows. Add rows for each Art. 25 measure.

**Table 21 — Security:** 2 template rows. Add rows for each Art. 32 measure (pseudonymisation, encryption, C-I-A-R, recovery, etc.).

**Implementation status handling:** Each row has three status options as text: "Planned" / "Partially implemented" / "Implemented". Bold the applicable status. Alternatively, prefix with ☑/☐.

### Table 22 — 3.1 Inherent-by-Design Impacts (Track A)

5 columns: `#` | `Threats posed by processing as designed` | `How materialised?` | `Risk sources` | `Impact on rights/freedoms`

Add one row per Track A risk identified during the assessment.

**Data source:** Inherent Risks phase → Track A entries from `risk-catalog.md`.

### Table 23 — 3.2 Necessity (narrative)

Single cell. Replace placeholder with necessity assessment: is the processing effective and least intrusive? Evidence of alternatives considered.

### Table 24 — 3.3 Proportionality (narrative)

Single cell. Replace placeholder with proportionality analysis: importance + benefits vs. impact on rights/freedoms. Balancing conclusion.

### Table 25 — 4.1.a Operational Impacts (Track B)

4 columns: `Threats from malfunctions/deviations` | `How materialised?` | `Risk sources` | `Impacts`

Add one row per Track B risk. Must include at minimum:
1. Illegitimate access scenario
2. Undesired modification scenario
3. Data disappearance scenario

**Data source:** Inherent Risks phase → Track B entries from `risk-catalog.md`.

### Table 26 — 4.1.b Method (narrative)

Single cell. Replace placeholder with methodology declaration:
- Scales: 5-level likelihood (Negligible → Maximum) and severity (Negligible → Maximum)
- Risk formula: L × S → score (1-25) → level (Low/Medium/High/Very High)
- Modulating factors: aggravating/mitigating contextual adjusters (±1 tier shift)
- Acceptance thresholds: Low = acceptable, Medium = action recommended, High = action required, Very High = fundamental redesign / Art. 36
- Reference: "Based on DPIA Sentinel scoring methodology, aligned with EDPB Guidelines WP 248 rev.01"

### Table 27 — 4.1.c Inherent Risk Assessment

7 columns: `#` | `Risks` | `Likelihood` | `Severity` | `Modulating factors` | `Risk level` | `Acceptable?`

Add one row per risk (combining Track A from Table 22 and Track B from Table 25).

**Data source:** Risk register from assessment → inherent risk scores + modulating factors.

Color-code risk level cells: Low=#E8F5E9, Medium=#FFF8E1, High=#FFF3E0, Very High=#FFEBEE. Apply via `<w:shd>` on the cell properties:
```xml
<w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="E8F5E9"/></w:tcPr>
```

### Table 28 — 4.2.a Additional Mitigating Measures

5 columns: `#` | `Measures` | `Mitigated risks (from 4.1.c)` | `Appropriateness/effectiveness` | `Implementation status`

Add one row per additional mitigation measure. Implementation status: bold the applicable tier.

### Table 29 — 4.2.b Residual Risk Assessment

7 columns: `#` | `Risks` | `Additional measures` | `Residual likelihood` | `Residual severity` | `Residual risk level` | `Acceptable?`

Add one row per risk that had additional mitigations. Color-code residual risk level cells.

### Table 30 — 4.2.c Plan (narrative)

Single cell. Implementation roadmap: activities, responsible team, timelines, monitoring/review schedule.

### Table 31 — 5.1 DPO Advice (narrative)

Single cell. DPO opinion + how advice was implemented.

### Table 32 — 5.2 Data Subjects' Views (narrative)

Single cell. Data subjects' input + explanation of participation (or why not included).

### Table 33 — 6 Conclusion and Decision

Single cell containing all four decision options as text blocks. To mark the selected decision:

1. Find the text block for the selected outcome (e.g., "APPROVED")
2. Bold the entire text block for that outcome
3. For CONDITIONALLY APPROVED: replace "Condition 1: ___" and "Condition 2: ___" placeholders with actual conditions
4. For CONSULTATION: mark sub-reason (residual risks still high / national law requirement)

Decision options in order:
- `REJECTED: The processing must be abandoned.`
- `CONSULTATION: The processing will be consulted with the SA`
- `APPROVED: The processing may proceed [immediately].`
- `CONDITIONALLY APPROVED: The processing may proceed only after the following conditions are met:`

### Table 34 — 6 Justification (narrative)

Single cell. Optional justification for the decision. Fill if the controller wants to document reasoning.

---

## Placeholder Text Replacements

13 `_____` placeholder patterns exist in the template body (outside tables). These are free-text fields within running text.

| Location (surrounding text) | Replace With |
|-----------------------------|-------------|
| "Explanation: ___" (national law trigger) | National law reference + explanation |
| "Other (...): ___" (other trigger reasons) | Specific reason text |
| "How? ___" (existing processing change) | Description of change |
| "How? ___" (publication details) | Publication method/scope |
| "How? ___" (external sharing details) | Sharing method/recipients |
| "Yes (justification and details): ___" (cross-border) | Jurisdictions + justification |
| "Yes (justification and details): ___" (transfers) | Transfer destinations + mechanisms |
| "Why?: ___" (codes of conduct required) | Legal obligation reference |
| "Why?: ___" (codes of conduct beneficial) | Benefit explanation |
| "Condition 1: ___" (conditional approval) | First condition text |
| "Condition 2: ___" (conditional approval) | Second condition text |

To replace: find the `<w:t>` element containing `_____` characters, replace the underscores with actual text. Preserve the surrounding text and run formatting.

---

## OOXML Patterns

### Finding a table by header text

```python
from lxml import etree
tree = etree.parse("unpacked/word/document.xml")
ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

# Find all tables
tables = tree.findall(".//w:tbl", ns)

# Match by first-row text content
for tbl in tables:
    first_row = tbl.find(".//w:tr", ns)
    if first_row is not None:
        texts = [t.text for t in first_row.findall(".//w:t", ns) if t.text]
        combined = " ".join(texts)
        if "Processed personal data" in combined:
            target_table = tbl
            break
```

### Cloning a data row

```python
import copy

# Get rows in target table
rows = target_table.findall("w:tr", ns)
template_row = rows[-1]  # Last row is the template

for item in data_items:
    new_row = copy.deepcopy(template_row)
    cells = new_row.findall("w:tc", ns)
    for i, cell in enumerate(cells):
        # Clear existing text
        for t in cell.findall(".//w:t", ns):
            t.text = ""
        # Set new text in first text run
        first_t = cell.find(".//w:t", ns)
        if first_t is not None:
            first_t.text = item[i]
    target_table.append(new_row)

# Remove original empty template row
target_table.remove(template_row)
```

### Setting cell shading (risk level colors)

```python
color_map = {
    "Low": "E8F5E9",
    "Medium": "FFF8E1",
    "High": "FFF3E0",
    "Very High": "FFEBEE"
}

tc = risk_level_cell
tc_pr = tc.find("w:tcPr", ns)
if tc_pr is None:
    tc_pr = etree.SubElement(tc, f"{{{ns['w']}}}tcPr")
    tc.insert(0, tc_pr)

shd = tc_pr.find("w:shd", ns)
if shd is None:
    shd = etree.SubElement(tc_pr, f"{{{ns['w']}}}shd")

shd.set(f"{{{ns['w']}}}val", "clear")
shd.set(f"{{{ns['w']}}}color", "auto")
shd.set(f"{{{ns['w']}}}fill", color_map[risk_level])
```

### Replacing placeholder text

```python
for t_elem in tree.findall(".//w:t", ns):
    if t_elem.text and "____" in t_elem.text:
        # Replace underscores with actual content
        t_elem.text = t_elem.text.replace("_" * len_underscores, replacement_text)
```

### Marking checkboxes

The template uses plain text spaces before options. To mark a checkbox:

```python
# Find the text element for the option
for t_elem in tree.findall(".//w:t", ns):
    if t_elem.text and "Planned" in t_elem.text:
        # Prefix with checkbox character
        t_elem.text = "☑ " + t_elem.text.lstrip()
        break
```

For unselected options in the same group, prefix with "☐ ".

---

## Data Source Mapping

| Assessment Phase | Populates Tables |
|-----------------|-----------------|
| Intake | 1 (controller), 2 (processors), 3 (name), 4 (planning), 5 (tech sheet) |
| Description | 6 (data items), 7 (purposes), 8 (secondary uses), 9 (nature/scope/context), 10 (functional), 12 (codes of conduct) |
| Asset Inventory | 11 (assets) |
| Necessity | 13 (legal basis), 14 (Art. 9 lift), 15 (minimisation), 16 (quality), 23 (necessity narrative) |
| Proportionality | 24 (proportionality narrative) |
| Mitigations (baseline) | 17–21 (compliance measures 2.3.a–e) |
| Inherent Risks — Track A | 22 (design impacts), 27 (risk table — Track A rows) |
| Inherent Risks — Track B | 25 (operational impacts), 27 (risk table — Track B rows) |
| Risk Method | 26 (method narrative) |
| Mitigations (additional) | 28 (additional measures) |
| Residual Risk | 29 (residual risk table) |
| Implementation Plan | 30 (plan narrative) |
| Art. 36 Check | 31 (DPO), 32 (data subjects) |
| Documentation | 33 (conclusion), 34 (justification) |
