---
name: client-instruction-schedule
description: Build a client instruction schedule — a plain-English, Scott Schedule-style Word table that gathers a struggling client's evidence and instructions issue by issue, with a one-page covering note. Use whenever the user asks for a "client instruction schedule", "instruction schedule", "client questionnaire", "schedule of questions for the client", "get instructions from the client on the papers", or says the client is overwhelmed and needs the case broken into manageable questions. Also trigger when asked to turn case papers into a structured request for client input. Do NOT use for court-facing Scott Schedules, pleadings, witness statements, or advice letters — this skill produces a client-facing working document only. Output is always a .docx draft for solicitor review, never a final document.
license: Apache-2.0
metadata:
  author: Serhan Handani
  jurisdiction: UK (England & Wales)
  category: litigation
  language: en
---

# Client Instruction Schedule

## Purpose

Clients in document-heavy disputes often freeze when asked open-endedly for "their comments". This skill produces a **client instruction schedule**: a landscape Word table borrowing the discipline of a Scott Schedule, but written *to the client* in plain English, with one row per disputed issue and specific, mostly closed questions. It is paired with a short covering note telling the client how to complete it. Positions are sourced precisely to statements, letters and exhibit pages, so that a court-facing Scott Schedule can later be drafted from it far more easily (the client's plain-English answers will still need to be turned into pleaded positions — the schedule is a quarry, not a conversion).

## Important limits

This skill drafts a working document for a solicitor to review, amend and approve. It does not give legal advice, it must not be sent to a client without human review, and every draft it produces carries a banner saying so. The solicitor remains responsible for the accuracy of every position, reference and question in the schedule. Four further limits apply:

- **Confidentiality first.** The skill reads an entire litigation folder, including counsel's advice. Before running it, check the firm's AI and confidentiality policy permits loading these papers into the tool in use, and anonymise or exclude material where policy requires.
- **Witness evidence (PD 57AC).** The schedule uses mostly closed questions and shows the client the other side's position before asking for their recollection. If any answer may later feed a trial witness statement, the solicitor should consider Practice Direction 57AC before sending: putting the opponent's account to the client may be criticised as leading on important disputed matters. Consider generalising or removing the "other side's position" column for contested recollection issues, and keep a record of what documents the client was shown.
- **Client suitability.** Confirm with the supervising solicitor that a written schedule suits this client. Some overwhelmed clients are vulnerable clients for whom this format is the wrong tool and a phone attendance is the right one.
- **Residual risk.** The verification steps below reduce, but do not eliminate, the risk of hallucinated references, unfair paraphrase and silently omitted issues. The coverage map (step 3) exists so the reviewing solicitor can see what was left out, not only what went in.

## Jurisdiction and register

English law (England & Wales). UK spelling. £ for currency. **No CPR jargon or statutory citations in anything the client must read or complete** — "the court's disclosure order", not "the Order of ICCJ [X] under CPR 3.1(7)". Document references (e.g. "Mr [X]'s 2nd statement, para 22") are fine: they are what makes later conversion to a Scott Schedule possible. Practitioners elsewhere can adapt the register, but the plain-English discipline is the point everywhere.

## Workflow

### 1. Read everything, identify by content

- Read every document in the case folder. **Identify documents by their content, never by filename** — filenames lie (exhibit bundles stamped with the wrong witness's initials, cover sheets certifying the wrong exhibit name). Content-based identification can also be wrong: record the basis for each identification in the report-back (step 10) so the solicitor can check it.
- Note any document that is **referenced in the papers but absent from the folder** (a statement that mentions an exhibit not supplied, correspondence referring to an enclosure). List these in the report-back — the folder cannot be assumed complete.
- Scanned PDFs with no text layer must be OCR'd (`pdftoppm` at 200dpi + `tesseract`, pages in parallel). Verify OCR'd figures and quotations against the page image before relying on them.
- Hash files (`md5sum`) to find duplicates before reading.
- Note every internal inconsistency found in the papers (dates, exhibit labels, misquoted figures) — these become highlighted solicitor notes (step 6), not silent corrections.

### 2. Extract the disputed issues

List every issue on which the client's input — an answer, a recollection, or a document — is actually needed. Sources: witness statements on both sides (paragraph by paragraph), counsel's advice (especially "we need instructions on…" passages), solicitors' letters to the client with unanswered requests, and the client's own partial responses. Exclude:

- procedural and legal argument (no client input needed);
- costs and strategy points;
- anything already answered in the papers — but exclude only where a **complete** answer exists and can be cited; cite it in the exclusions list (step 3).

Decision points awaiting the client (e.g. "do you agree to instruct an accountant?") count as rows; broad strategy decisions belong in the covering note or a separate advice, not the schedule.

### 3. Build a coverage map (source-to-row)

The most dangerous failure of this workflow is a silently missed issue: the reviewing solicitor sees a polished table and has no way to see what was dropped. So, before drafting, produce a **source-to-row map**: every witness-statement paragraph raising a factual dispute, every "we need instructions on…" passage in counsel's advice, and every unanswered request in correspondence must appear as either (a) a schedule row, or (b) an entry in an "Issues considered and excluded" list with a one-line reason each. That exclusions list goes **into the schedule document itself**, as a solicitor-notes appendix after the table (same highlighting convention as step 6), not only into the chat report — the artefact under review must carry its own account of what it left out.

### 4. Cross-check against what is already held

For each issue, check whether the material about to be requested already exists in the folder. **Never ask the client for a document the firm already holds** — instead ask them to *identify the relevant entries* in it (e.g. "the bank statements are already with us (exhibit X) — point us to the matching entries"). The "Evidence we already hold" column is the enforcement mechanism: filling it honestly exposes any lazy request.

### 5. Build the schedule (.docx)

Landscape A4, Times New Roman 12, generated with the `docx` npm package (tested with docx@9.6.1; see `references/build-schedule-example.js` for a complete working script). One table, header row repeating (`tableHeader: true`), **native Word automatic numbering for issue numbers (a `numbering` config with `LevelFormat.DECIMAL`) — never typed digits**. Key `docx` package points: set `columnWidths` on the table AND `width` on every cell, both in DXA; use `ShadingType.CLEAR` for shading (never `SOLID`); for landscape pass portrait A4 dimensions plus `orientation: PageOrientation.LANDSCAPE`. Eight columns (widths in DXA summing to ≤15398 for 0.5" margins):

| # | Column | Content rules |
|---|--------|---------------|
| 1 | Issue | Auto number + bold short label (3–8 words) |
| 2 | Our position | 1–2 plain-English sentences |
| 3 | The other side's position | Equally short, but sourced precisely: statement + paragraph, letter + date, exhibit + stamped page |
| 4 | Evidence we already hold | Document references for everything relevant already on file |
| 5 | What we need from you | Specific, concrete, mostly closed questions ("Did you attend the meeting on [date]? Who else was there?"). Never "please comment". Tell the client "cannot recall" is an acceptable answer |
| 6 | Your response | Blank, generously sized |
| 7 | Documents you are sending | Blank — the client lists enclosures per row |
| 8 | Priority | High / Medium / Low, so the client can triage rather than freeze |

Above the table: title, "Draft NN" line, one italic instruction line (High rows first), then any highlighted solicitor notes.

**Priority guidance:** High = goes to the core dispute, limitation-sensitive, or a decision blocking next steps. Medium = matters but can follow. Low = context or already well-documented.

### 6. Accuracy conventions

- Where any position, date, amount or attribution is unclear from the papers: insert `[UNCLEAR — PLEASE REVIEW]` — never guess, never fabricate a fact, reference or quotation. Other flags: `[DATE TBC]`, `[AMOUNT TO BE CONFIRMED]`, `[SOLICITOR TO VERIFY]`.
- Inconsistencies in the source papers (conflicting statement dates, mislabelled exhibits) go in **bold, yellow-highlighted paragraphs above the table**, prefixed `[SOLICITOR TO VERIFY — DELETE BEFORE SENDING TO CLIENT: …]`.
- Every page carries a header banner: `AI-ASSISTED DRAFT — FOR SOLICITOR REVIEW — NOT YET APPROVED OR SENT`, and a footer with client name, draft number, date and page X of Y.

### 7. Covering note (.docx, one page)

Separate portrait document, same font, letter form addressed to the client by first name. Contents: what the schedule is; how each row works; numbered how-to list (High rows first; where to write answers and list documents; closed answers with a sentence of explanation; "cannot recall" is proper; staged return is fine); timescale with `[    ]` for the solicitor to set; a costs-saving encouragement; sign-off. Same draft banner. Calm tone — the client is engaged but overwhelmed.

### 8. Verify before delivering

1. Validate both files against the OOXML schema if a validator is available; at minimum, open them and check they render. Note: the `docx` package emits an invalid `<w:highlightCs>` element for highlighted runs — strip it from `word/document.xml` (unzip → `sed 's|<w:highlightCs w:val="yellow"/>||g'` → rezip) or schema validation fails.
2. Convert to PDF and **look at every page** (`soffice` → `pdftoppm`): check column headers don't wrap badly, numbering renders, highlights show.
3. Programmatically confirm native numbering (numPr present, no typed leading digits in cell text).
4. For each row, **re-read the cited paragraph or page** and confirm the position as summarised is a fair paraphrase — not merely that the cited document exists. Quote-check every figure, date and quotation verbatim against the source (against the page image where the source was OCR'd).
5. Re-check the coverage map (step 3): confirm every mapped source item appears as a row or a listed exclusion, and that the exclusions appendix is present in the document.
6. Check priorities: confirm every limitation-sensitive or decision-blocking issue is marked High, and record the priority reasoning in the report-back.

### 9. Save and name

- Suggested convention: `<case>-client-instruction-schedule-draft-NN-YYYY-MM-DD.docx` and `<case>-client-covering-note-draft-NN-YYYY-MM-DD.docx` (ISO date = date of drafting), saved to the matter's drafts area — never to any folder holding final or filed documents. Adapt to the firm's own naming and filing conventions.
- If the firm keeps a blank precedent version for human completion (covering letter page then schedule), that precedent need not carry the AI-draft banner; AI-generated drafts must always carry the banner and solicitor notes described above.

### 10. Report back

Finish by listing: the issues found (grouped by priority, with the reasoning for each High marking); the coverage map, including every issue considered and excluded and why; documents referenced in the papers but absent from the folder; the basis on which each document was identified; every inconsistency flagged; and open questions for the solicitor.

## Reference files

- `references/schedule-data-example.js` — example row data from a **fictional** dispute (Frayne v Kestrel, an invented barn-conversion case), showing the register and sourcing style each column needs.
- `references/build-schedule-example.js` — complete working build script for the schedule document.

## Disclaimer

This skill is provided for use by legal professionals. It does not provide legal advice, and its output is a draft requiring review by a qualified solicitor before any use. The author accepts no liability for reliance on unreviewed output.
