# Word Document Formatting Specifications

Styling and structural specifications for generating professional .docx exports of AI Act compliance reports. Uses the `docx-js` library (JavaScript/TypeScript).

**Style:** Clean professional — neutral, authoritative, suitable for legal files, audit trails, and regulatory submissions.

---

## Prerequisites

Before generating a .docx file, read the full docx-js reference from the docx-processing skill:
`~/.claude/skills/docx-processing-anthropic/references/docx-js.md`

This file provides the docx-js API, critical formatting rules, and common pitfalls. The specifications below build on that foundation.

---

## 1. Document-Level Settings

### Page Setup

| Property | Value | docx-js (DXA) |
|----------|-------|---------------|
| Paper size | A4 (210 x 297 mm) | Default |
| Top margin | 2.54 cm (1 inch) | 1440 |
| Bottom margin | 2.54 cm (1 inch) | 1440 |
| Left margin | 2.54 cm (1 inch) | 1440 |
| Right margin | 2.54 cm (1 inch) | 1440 |
| Orientation | Portrait | Default |

A4 usable width: 9360 DXA (with 1-inch margins).

### Default Font

```javascript
styles: {
  default: {
    document: {
      run: { font: "Calibri", size: 22, color: "333333" } // 11pt, dark gray
    }
  }
}
```

---

## 2. Typography Hierarchy

### Heading Styles

Override built-in Word heading styles for TOC compatibility:

```javascript
paragraphStyles: [
  {
    id: "Title", name: "Title", basedOn: "Normal",
    run: { size: 36, bold: true, color: "000000", font: "Calibri" }, // 18pt
    paragraph: { spacing: { before: 0, after: 300 }, alignment: AlignmentType.LEFT }
  },
  {
    id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
    run: { size: 36, bold: true, color: "000000", font: "Calibri" }, // 18pt
    paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 }
  },
  {
    id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
    run: { size: 28, bold: true, color: "222222", font: "Calibri" }, // 14pt
    paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 }
  },
  {
    id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
    run: { size: 24, bold: true, color: "333333", font: "Calibri" }, // 12pt
    paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 }
  }
]
```

### Body Text

| Element | Font | Size | Color | Spacing |
|---------|------|------|-------|---------|
| Body text | Calibri | 11pt (22) | #333333 | after: 120 |
| Emphasis | Calibri Bold | 11pt (22) | #333333 | — |
| Legal citation | Calibri Italic | 11pt (22) | #555555 | — |
| Disclaimer text | Calibri Italic | 10pt (20) | #666666 | — |
| Table cell text | Calibri | 10pt (20) | #333333 | — |
| Table header text | Calibri Bold | 10pt (20) | #333333 | — |

Line spacing: 1.15 (276 in docx-js `line` property, which uses 240ths of a line).

```javascript
paragraph: { spacing: { line: 276 } } // 1.15 line spacing
```

---

## 3. Table Styling

### Standard Assessment Table

Used for all assessment matrices, obligation trackers, screening tables.

```javascript
const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };
const headerShading = { fill: "F2F2F2", type: ShadingType.CLEAR };
```

| Property | Value |
|----------|-------|
| Borders | 1pt solid #CCCCCC (light gray) |
| Header row fill | #F2F2F2 (very light gray) |
| Header text | Bold, 10pt |
| Data row fill | None (white) |
| Cell margins | top: 60, bottom: 60, left: 120, right: 120 |
| Vertical align | VerticalAlign.CENTER for header, VerticalAlign.TOP for data |

### Metadata Table (key-value pairs)

Used for document control blocks, system identification, classification summaries.

| Property | Value |
|----------|-------|
| Left column (label) | Bold, width ~35% |
| Right column (value) | Normal weight, width ~65% |
| Borders | Same as standard |
| No header row shading | Both rows use white background |

### Dashboard/Summary Table

Used for the final classification result and flags section.

| Property | Value |
|----------|-------|
| Borders | 2pt solid #999999 (darker gray, slightly heavier) |
| Header shading | #E8E8E8 |
| Full-width single-column rows for section headers | Span all columns, bold, #F5F5F5 fill |

---

## 4. Headers and Footers

### Header (all pages except cover)

```javascript
headers: {
  default: new Header({
    children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
      spacing: { after: 0 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" } },
      children: [
        new TextRun({ text: "[Report Title]", font: "Calibri", size: 16, color: "999999" }), // 8pt
        new TextRun({ text: "\t" }),
        new TextRun({ text: "[Date]", font: "Calibri", size: 16, color: "999999" })
      ]
    })]
  })
}
```

### Footer (all pages)

```javascript
footers: {
  default: new Footer({
    children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
      border: { top: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" } },
      children: [
        new TextRun({ text: "Confidential", font: "Calibri", size: 16, color: "999999", italics: true }),
        new TextRun({ text: "\t" }),
        new TextRun({ text: "Page ", font: "Calibri", size: 16, color: "999999" }),
        new TextRun({ children: [PageNumber.CURRENT], font: "Calibri", size: 16, color: "999999" }),
        new TextRun({ text: " of ", font: "Calibri", size: 16, color: "999999" }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], font: "Calibri", size: 16, color: "999999" })
      ]
    })]
  })
}
```

---

## 5. Cover Page

Minimal and clean. First section of the document, followed by a section break.

Structure (top to bottom, vertically spaced):

1. **Report type** — e.g., "AI Act Compliance Assessment Report" (18pt, bold, black)
2. **Horizontal rule** — thin gray line
3. **System name** — large (24pt, bold)
4. **Metadata block** (table without borders):
   - Organization: [name]
   - Date: [date]
   - Prepared by: [name, role]
   - Reference: [ref number]
   - Status: [Draft / Final]
5. **Disclaimer** — italic, 10pt, gray, bottom of page

Use vertical spacing (paragraph `spacing.before`) to push content down from top. The cover page should feel spacious, not cramped.

```javascript
// Cover page is its own section with no header/footer
{
  properties: {
    page: { margin: { top: 2880, right: 1440, bottom: 1440, left: 1440 } } // Extra top margin
  },
  headers: { default: new Header({ children: [new Paragraph({ children: [] })] }) }, // Empty header
  footers: { default: new Footer({ children: [new Paragraph({ children: [] })] }) }, // Empty footer
  children: [ /* cover page content */ ]
}
```

---

## 6. Per-Template Structural Notes

### Template A: Full Assessment Report

9 sections. Use `HeadingLevel.HEADING_1` for main sections (1-9), `HEADING_2` for sub-sections (6.1, 6.2, etc.), `HEADING_3` for sub-sub-sections (6.2.1, 6.2.2).

Key structural elements:
- Cover page (own section)
- Table of Contents (after cover, before Section 1)
- Section 3 (Scope Exclusions): 6-row assessment table
- Section 4.1 (AI System Test): 7-row criteria table
- Section 6.1 (Art. 5 screening): 8-row screening table
- Section 6.2.2 (Annex III): 8-row category table
- Section 7 (Obligations): multi-table matrix (Technical, Organizational, Management, Assessments, GDPR)
- Section 8 (Recommendations): numbered priority table
- Final disclaimer paragraph

Page breaks before: Sections 1, 3, 6, 7, 8, 9.

### Template B: Classification Record (Pruefprotokoll)

8 sections. Document Control metadata table at top. Heavy use of assessment tables throughout. Assessor/Reviewer signature block at end.

Key structural elements:
- Document Control table (no borders, key-value)
- Section 4.1-4.6: cascading risk classification tables
- Section 6: Classification Result summary table (dashboard style)
- Signature block: lines for assessor and reviewer

Page breaks before: Sections 1, 4, 6, 8.

### Template C: Compliance Register Entry

Tracker-style document. System Metadata table at top. 4 obligation tracker tables (Technical, Organizational, Assessments, Management Systems). Progress summary table. Change log.

Key structural elements:
- System Metadata (key-value table)
- 4 obligation tracker tables with Status column
- GDPR Coordination table
- Implementation Progress summary (with completion percentages)
- Residual Risk table
- Change Log table

Page breaks before: Obligation Tracker, GDPR Coordination, Implementation Progress.

### Template D: Management Briefing (Entscheidungsvorlage)

Maximum 2 pages when rendered. Compact layout. "At a Glance" summary table. Financial Exposure table. Strategic Options comparison table. Decision/sign-off block.

Key structural elements:
- No TOC (too short)
- Classification "at a glance" table (dashboard style with visual markers)
- Top 5 obligations table (RAG status)
- Financial Exposure table (3-row)
- Strategic Options table (4 options with Pro/Con/Cost/Risk)
- Decision block with checkbox lines
- Timeline visualization as formatted text (not ASCII art)

No page breaks — must fit in 2 pages. Use tighter spacing (paragraph after: 80 instead of 120).

---

## 7. File Naming Convention

```
AI-Act-[Template]-[SystemName]-[YYYY-MM-DD].docx
```

Examples:
- `AI-Act-Assessment-Report-TalentScreenAI-2026-03-15.docx`
- `AI-Act-Pruefprotokoll-TalentScreenAI-2026-03-15.docx`
- `AI-Act-Compliance-Register-TalentScreenAI-2026-03-15.docx`
- `AI-Act-Management-Briefing-TalentScreenAI-2026-03-15.docx`

Sanitize system name: replace spaces with hyphens, remove special characters.

---

## 8. Generation Checklist

Before generating the .docx:

- [ ] All report content is finalized in markdown (Phase 3 Quality Check passed)
- [ ] Read docx-js.md from docx-processing skill for API reference
- [ ] System name available for cover page and file name
- [ ] Date and preparer information available
- [ ] Template type confirmed (A, B, C, or D)

During generation:

- [ ] Cover page renders with correct metadata
- [ ] TOC included (except Management Briefing)
- [ ] All tables use consistent border and shading styles
- [ ] All headings use HeadingLevel (not custom styles) for TOC compatibility
- [ ] Headers/footers display on all pages except cover
- [ ] Page breaks placed before major sections
- [ ] Disclaimer text included at end
- [ ] File saved with correct naming convention
- [ ] No `\n` characters in any TextRun (use separate Paragraphs)
- [ ] All table cells use ShadingType.CLEAR (never SOLID)
- [ ] Bullet lists use LevelFormat.BULLET (never unicode symbols)
