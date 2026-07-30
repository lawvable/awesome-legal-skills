---
name: "enforcement-action-analysis-amir-fadavi"
description: "Analyze any OFAC or OFSI enforcement action — by URL, pasted text, or uploaded document — and produce a structured root cause analysis as a formatted Excel (.xlsx) spreadsheet. Use this skill whenever a user names, links to, pastes, or uploads an OFAC or OFSI enforcement action and asks for any of the following: root cause analysis, compliance gaps, what went wrong, lessons learned, organizational self-assessment, or remediation planning. Also trigger when a user asks \"analyze this enforcement action\", \"what were the root causes\", \"turn this into a checklist\", or \"how do I make sure this doesn't happen to us\". Outputs a single-sheet .xlsx table with six columns: Root Cause | What Went Wrong | How It Went Wrong | What Could Have Stopped It | Is my organization immune to this? (Yes/No/Partial) | Notes."
metadata:
  author: "Amir Fadavi"
  license: "mit"
  version: "2026-06-10"
---

# Enforcement Action Analysis Skill

Produces a structured root cause analysis of any OFAC or OFSI enforcement action as a formatted Excel spreadsheet. The output is a six-column table designed to be used as a working document by compliance officers, in-house counsel, external counsel, and consultants — at financial institutions and non-financial firms alike.

---

## Input

The user will provide the enforcement action in one of three ways:

1. **URL** — fetch and parse the document (PDF or HTML)
2. **Pasted text** — use the text directly from the conversation
3. **Uploaded file** — read from `/mnt/user-data/uploads/`

If none is provided, ask the user to supply the enforcement action before proceeding.

---

## Step 1 — Extract the Case Facts

Before identifying root causes, extract the following from the enforcement action:

- **Subject** (name of the settling party)
- **Regulator** (OFAC or OFSI; include department/division if stated)
- **Date** of settlement or enforcement release
- **Settlement amount**
- **Sanctions program** (e.g., Iran, Russia, Cuba) and specific regulations cited
- **Violation period**
- **Number of apparent violations**
- **Egregious / non-egregious**
- **Voluntarily self-disclosed?**

Use this to name the output file and populate the sheet title cell.

---

## Step 2 — Identify Root Causes

Read the full enforcement action — especially the **Description of the Apparent Violations**, the **Aggravating Factors**, and the **Compliance Considerations** sections. These are the primary source material for root causes.

Identify **all distinct root causes**. A root cause is a discrete compliance failure — a gap in policy, process, training, technology, or judgment — that contributed to the violation. Do not consolidate unrelated failures to keep the table short. Typical enforcement actions yield 2–5 root causes; complex cases (e.g., commodity trading, multi-party evasion schemes) may yield more.

**For each root cause, draft three things:**

### Column: What Went Wrong
One to three sentences describing the specific failure as it occurred in this case. Factual, grounded in the enforcement action text. No generic compliance language.

### Column: How It Went Wrong
One to three sentences explaining the underlying compliance failure mechanism — why the organization's program did not catch this. Draw from:
- Aggravating factors stated by the regulator
- Compliance Considerations section
- OFAC's Compliance Framework root cause taxonomy (listed below)
- Logical inference from the facts

### Column: What Could Have Stopped It
Two to four sentences describing concrete controls that would have prevented or detected the violation. Be specific to the facts of the case. Always reflect OFAC's Compliance Considerations section — these are the regulator's own stated expectations and must not be omitted.

---

## OFAC Root Cause Taxonomy (reference)

From OFAC's Compliance Framework appendix. Use as a checklist when identifying root causes:

- Lack of a formal sanctions compliance program
- Inadequate policies and procedures (including failure to update for new business lines)
- Misapplication of OFAC's regulations (including "form over substance" errors)
- Failure to update or use automated screening tools
- Screening tool not configured to cover relevant lists (e.g., SSI/non-SDN lists)
- Failure to identify and escalate red flags
- Lack of due diligence on customers, intermediaries, or counterparties
- Decentralized compliance function with inconsistent application
- Inadequate sanctions compliance training
- Failure to conduct ongoing monitoring of existing relationships
- New business line entered without updating compliance program

---

## Step 3 — Build the Spreadsheet

Use **openpyxl** (Python). Do not use any other library for file creation.

### Sheet structure

- **Row 1:** Title cell (merged A1:F1) — `Root Causes of Apparent Violations — [Subject] ([Regulator], [Date])`
- **Row 2:** Column headers
- **Rows 3+:** One row per root cause

### Column layout

| Col | Header | Width (chars) |
|-----|--------|--------------|
| A | Root Cause | 22 |
| B | What Went Wrong | 38 |
| C | How It Went Wrong | 42 |
| D | What Could Have Stopped It | 46 |
| E | Is my organization immune to this? | 22 |
| F | Notes | 28 |

### Styling

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

NAVY   = "1B3A6B"
STEEL  = "A8C4E0"
LIGHT  = "EEF2F9"
WHITE  = "FFFFFF"
INK    = "1A1A2E"
GREY   = "D0D8E4"

thin = Side(style='thin', color=GREY)
border = Border(left=thin, right=thin, top=thin, bottom=thin)
wrap = Alignment(wrap_text=True, vertical='top')
center_wrap = Alignment(wrap_text=True, vertical='center', horizontal='center')
```

**Title row (row 1, merged A1:F1):**
- Merge cells A1:F1
- Font: Arial 14pt bold, color `WHITE`
- Fill: `NAVY`
- Alignment: left, vertical center
- Row height: 30

**Header row (row 2):**
- Font: Arial 11pt bold, color `WHITE`
- Fill: `NAVY`
- Alignment: wrap, vertical top
- Border: all sides thin `GREY`
- Row height: 30

**Data rows (row 3+):**
- Column A: Font Arial 10pt bold color `NAVY`, fill `LIGHT`, border, wrap top-left
- Columns B–D: Font Arial 10pt color `INK`, fill `WHITE`, border, wrap top-left
- Column E: Font Arial 10pt color `INK`, fill `WHITE`, border, center-aligned — value: `☐ Yes / ☐ No / ☐ Partial`
- Column F: Font Arial 10pt color `INK`, fill `WHITE`, border, wrap top-left — empty
- Row height: set to 15 * (estimated line count) — minimum 60, use `sheet.row_dimensions[r].height`

**Column A label format:** `RC[N]: [Short Title]` — e.g., `RC1: SDN-Only Screening`

### Output path

```
/mnt/user-data/outputs/[SubjectName]_OFAC_RootCause_Analysis.xlsx
```

Use underscores, no spaces. Sanitize special characters.

### Full code template

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import math

wb = Workbook()
ws = wb.active
ws.title = "Root Cause Analysis"

NAVY, LIGHT, WHITE, INK, GREY = "1B3A6B", "EEF2F9", "FFFFFF", "1A1A2E", "D0D8E4"
thin   = Side(style='thin', color=GREY)
border = Border(left=thin, right=thin, top=thin, bottom=thin)
wrap   = Alignment(wrap_text=True, vertical='top')
cwrap  = Alignment(wrap_text=True, vertical='center', horizontal='center')

col_widths = [22, 38, 42, 46, 22, 28]
headers    = ["Root Cause", "What Went Wrong", "How It Went Wrong",
              "What Could Have Stopped It", "Is my organization immune to this?", "Notes"]

# Title row
ws.merge_cells("A1:F1")
t = ws["A1"]
t.value     = "Root Causes of Apparent Violations — [Subject] ([Regulator], [Date])"
t.font      = Font(name="Arial", size=14, bold=True, color=WHITE)
t.fill      = PatternFill("solid", fgColor=NAVY)
t.alignment = Alignment(horizontal='left', vertical='center')
ws.row_dimensions[1].height = 30

# Header row
for i, h in enumerate(headers, 1):
    c = ws.cell(row=2, column=i, value=h)
    c.font      = Font(name="Arial", size=11, bold=True, color=WHITE)
    c.fill      = PatternFill("solid", fgColor=NAVY)
    c.alignment = cwrap
    c.border    = border
ws.row_dimensions[2].height = 30

# Column widths
for i, w in enumerate(col_widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

# rows = list of (rc_label, what_went_wrong, how_it_went_wrong, what_could_have_stopped)
rows = []  # populated from analysis

for r, (rc, ww, hw, stop) in enumerate(rows, start=3):
    data = [rc, ww, hw, stop, "☐ Yes  /  ☐ No  /  ☐ Partial", ""]
    max_lines = 1
    for i, val in enumerate(data, 1):
        c = ws.cell(row=r, column=i, value=val)
        c.border    = border
        c.font      = Font(name="Arial", size=10, bold=(i == 1),
                           color=NAVY if i == 1 else INK)
        c.fill      = PatternFill("solid", fgColor=LIGHT if i == 1 else WHITE)
        c.alignment = cwrap if i == 5 else wrap
        if val and i < 5:
            lines = math.ceil(len(str(val)) / col_widths[i-1]) + str(val).count('\n')
            max_lines = max(max_lines, lines)
    ws.row_dimensions[r].height = max(60, max_lines * 15)

wb.save("/mnt/user-data/outputs/[Filename].xlsx")
print("Done.")
```

---

## Step 4 — Present the File

Call `present_files` with the output path. One line of context is enough (e.g., "Four root causes for the FTI case — ready to download.").

---

## Quality checks before presenting

- Every root cause row has all four text columns populated (no blanks in B–D)
- "What Could Have Stopped It" reflects OFAC's Compliance Considerations where applicable
- Root causes are distinct — no two rows describe the same underlying failure
- Column A labels follow `RC[N]: [Short Title]` format
- Title cell matches: `Root Causes of Apparent Violations — [Subject] ([Regulator], [Date])`
- Column E contains the checkbox string in every data row
- File written to `/mnt/user-data/outputs/` and presented via `present_files`
