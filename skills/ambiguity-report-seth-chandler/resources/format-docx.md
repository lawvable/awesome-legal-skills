# Format — Microsoft Word document

The Word path produces a single `.docx` suitable for review by a litigator, legislator, or counsel — readable in Word with proper heading navigation, tracked changes for redrafts, and footnoted analysis.

## Delegation to the docx skill

This skill does not implement docx generation directly. Instead, it delegates to the existing `docx` skill (loaded via the Skill tool). The docx skill uses `python-docx` under the hood and knows the patterns for headings, styles, tables, and tracked changes.

**Workflow.**
1. Read the spec.
2. Invoke the `docx` skill (or read its SKILL.md if it's not directly invocable from here).
3. Build the document by walking the spec, applying the document structure below.
4. Save to `<output-dir>/report.docx`.
5. Deliver the file to the user by whatever mechanism the host provides; if none exists, state the output path.

## Document structure

The Word document mirrors the multi-page website's information architecture but as a linear read-through.

**Cover / title page.**
- Title: `meta.title`
- Subtitle: `meta.subtitle`
- Kicker (small caps): `meta.kicker`
- Below: `meta.audit_date`, `meta.profile`
- Page break.

**Executive summary.**
- One paragraph from `meta.page_subtitle`.
- A bulleted list of the scenarios (S-N · title · anchor).
- Page break.

**The source.**
- Heading 1: "The [Statute/Contract/Regulation/Opinion]" (use `meta.profile` to pick the right noun)
- Render `source.name` as a section title.
- For each section / subprovision: heading style (Heading 2 for top-level, Heading 3 for sub), then the text. Style provision labels (e.g., "(b)(7)") in bold.
- For provisions with anchored scenarios, add a footnote at the end of the provision listing the scenarios that attack it: "Scenarios: S-1, S-2, S-3."
- Page break.

**The scenarios.**
- Heading 1: "The N Fights" or "The N Scenarios" (singular/plural by count).
- For each scenario:
  - Heading 2: "S-N · {title}"
  - Tagline paragraph in italics.
  - Bold "Situation:" label, then `situation` text.
  - **Two-column table** for positions: two columns, single row. Column 1: Position A header (bold colored text — use `design.dept_color`), actor in italics, then argument. Column 2: same for Position B. Table borders subtle. This is the visual equivalent of the website's two-sides panel.
  - Bold "Weak point:" label, then text.
  - Bold "Likely outcome:" label, then text.
  - **Redraft block:** a one-row table with a single cell, light yellow background, italic body text. Label "Proposed amendment" in small caps above.
  - Anchor pills as inline text: "Anchored to: §(b)(7)". Family pills as italicized text: "*Defect family: Scope / coverage*".
  - Horizontal rule.
- Page break before each new scenario if the previous one extends past mid-page.

**Redrafts appendix.**
- Heading 1: "Proposed Amendments"
- Brief paragraph explaining the package.
- For each scenario's redraft:
  - Heading 2: "R-N · {short title} — amends {anchor}"
  - Problem paragraph (derived from the weak point or a short summary).
  - **Proposal block** in the same yellow-bordered table style.
  - Cross-reference back to the scenario: "See S-N."
- Page break.

**Coverage list appendix (if `coverage_list` present).**
- Heading 1: "Additional ambiguities flagged"
- Brief intro.
- Each item as a bullet: bold label, then note.

**Methodology appendix (if `methodology` present).**
- Heading 1: "Methodology"
- For each section in `methodology`, a Heading 2 with the section name, then the paragraphs.
- Provenance line as a small italic line at the end.

## Style choices

**Typography.** Use Word's built-in heading styles (Title, Heading 1, Heading 2, Heading 3, Normal). Modify the underlying styles rather than direct formatting — this keeps the document navigable in Word's outline view and allows the user to restyle by changing styles.

**Heading style overrides.** Match the website's typographic feel where Word permits:
- Title: serif (Georgia or Cambria), 32pt, color = `meta.title` accent (slight color, not black).
- Heading 1: serif, 24pt, semibold.
- Heading 2: serif, 18pt, regular.
- Heading 3: serif, 14pt, semibold.
- Body: sans-serif (Calibri or Inter if available), 11pt.

**Colors.** Render Position A header in `design.dept_color`. Render Position B header in `design.adv_color`. Apply these as font color on the table headers. Backgrounds: keep tables borderless or with very light gray borders; the colored band on the top of each cell signals the side.

**Anchor pills.** In Word, render as small inline text with subtle background shading. Use Word's character highlighting at minimum; better: a one-row, one-cell table inline. Keep it simple.

**Family pills.** Similar — small inline italic colored text. Use the family color from `design.family_palette` if exposed, otherwise default.

## Tracked changes for redrafts

If the document is for a drafter who will negotiate the redrafts, use Word's tracked-changes feature: insert the proposed amendment text as a tracked insertion attributed to "Ambiguity Audit." This makes the redraft visually distinct and lets the drafter accept/reject in their normal flow.

Whether to use tracked changes is a user choice — ask if the user is a drafter who will negotiate. Default off; the yellow-bordered callout is sufficient for review.

## Cross-references

Word supports cross-references via bookmarks. Set a bookmark at each scenario heading (`scenario_N`) and at each redraft heading (`redraft_N`). The "See S-N" links use these bookmarks so clicking jumps to the target. Same for source-text provisions — bookmark each provision by its ID and let scenario references jump to the source.

## Page setup

- Margins: 1 inch all sides.
- Page numbers: bottom-right.
- Header: `meta.title` in small caps, left-aligned.
- Footer: `meta.audit_date`, right-aligned.

## Saving

Save as `report.docx` in the output directory. If the user supplied a specific filename, honor it.

## Common asks

**"Just the scenarios, no source, no appendix."** Skip the source section and the methodology/redrafts appendices. Produce a leaner brief.

**"Include the redrafts as a separate document."** Produce two files: `report.docx` (the analysis) and `redrafts.docx` (just the amendment package, formatted as a legislative submission).

**"Format for a CLE handout."** Reduce the structure — single column, no two-column tables for positions (use inline labels instead), larger font. Mention to the user that the rendering will be less visually rich.

## What this format does well

Word is the natural medium for tracked-changes review, marginal comments, and printable handoffs. The format is best when the recipient will read in Word, mark it up, or print it.

## What this format does poorly

Word doesn't handle highly interactive content. There's no equivalent to the website's click-to-filter or the SPA's cross-highlighting. Treat the Word doc as a *snapshot* — the website is for exploration, the doc is for delivery.
