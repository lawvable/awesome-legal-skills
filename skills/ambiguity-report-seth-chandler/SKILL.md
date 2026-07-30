---
name: ambiguity-report
description: Turn an interpretive-ambiguity audit of a legal text — contract, statute, regulation, or judicial opinion — into a polished deliverable. Produces a multi-page website (default), a single-page interactive site, a Microsoft Word document, a PowerPoint deck, or a LaTeX/PDF. Use whenever a user has a stress-test result, ambiguity audit, or "where will this be litigated" scenarios and wants to publish, present, or share them. Triggers on "publish the audit," "make a report from this," "turn this into a website / deck / brief / Word doc," "make a Netlify site," "build slides of these ambiguities," "render the scenarios," "package this stress test," "produce a LaTeX version," and similar. Pairs with the ambiguity-stress-test skill (the underlying analysis) but works on any structured or semi-structured ambiguity analysis. Visual design is opinionated but the user can override colors, fonts, and brand label. Most formats need Python and a writable filesystem; single-file HTML works where the host has neither.
metadata:
  author: "Seth J. Chandler"
  author_link: "https://legaled.ai"
  license: "Apache-2.0"
  version: "2026-07-29"
  jurisdiction: "All"
  language: "English"
  requires: "Python 3 (standard library only); docx and pptx skills for those two formats; a LaTeX distribution to compile the PDF"
---

# Ambiguity Report

Take an interpretive-ambiguity analysis of a legal text and turn it into a polished deliverable in one of six formats: multi-page website (the default), single-page interactive website, single-file HTML, Microsoft Word document, PowerPoint deck, or LaTeX source for a PDF.

**Before promising a format, know what this host can do.** Four of the six formats have requirements the host may not meet, and discovering that after the spec is built wastes the user's effort. Run the capability check in Stage 3 first.

The skill's central insight: **the data is the same across formats, the rendering is not.** An ambiguity analysis is a set of scenarios — each with a situation, two opposed positions, a weak point in the text, a likely outcome, and a proposed redraft — anchored to provisions of a source text. Once that data is captured in the canonical spec, the right format follows from how the deliverable will be used.

## Workflow

This skill has four stages. Stages 1–3 are setup; stage 4 is rendering.

- **Stage 1 — Identify the input.** Determine what kind of analysis the user is handing over. Three common shapes: (a) the structured markdown output of the `ambiguity-stress-test` skill; (b) a less-formal report or memo with scenarios identified but not all seven canonical fields filled in; (c) raw prose that names some ambiguities but isn't formatted as scenarios at all. The strategy for each shape differs — see `resources/parsing-unstructured.md`.
- **Stage 2 — Build the canonical spec.** Convert the input into a structured JSON spec that every renderer can consume. The schema is in `resources/data-format.md`. Fill in defaults for missing fields rather than blocking on completeness, and surface to the user what was inferred so they can correct.
- **Stage 3 — Choose the format and design.** Confirm with the user which format they want (default: multi-page website). Capture any design overrides (accent color, fonts, brand label). Most users care only about format and accent color; almost everything else has a sensible default.
- **Stage 4 — Render.** Delegate to the right renderer. The website and LaTeX paths use the bundled generator scripts (`scripts/generate_site.py` and `scripts/generate_latex.py`). The Word and PowerPoint paths delegate to the existing `docx` and `pptx` skills with content structured for those formats. Format-specific guidance lives in `resources/format-{website,docx,pptx,latex}.md`.

## Stage 1 — Identify the input

Look at what the user supplied. Three signatures to watch for:

**Signature A — structured stress-test output.** Markdown with sections titled like "## Scenarios" and individual scenarios under headers like "### S-1 —", each containing labeled fields ("**Anchors:**", "**Defect family:**", "**Weak point:**", "**Likely outcome:**", "**Redraft:**"). Often produced by the ambiguity-stress-test skill. This is the easy case — parse directly into the canonical spec.

**Signature B — semi-structured report.** Numbered ambiguities or issues in prose, each with a paragraph or two of explanation. The seven canonical fields may not all be present — the "situation" and "weak point" might be merged; the redraft might be missing entirely. Extract what's there, flag what's missing, and either infer reasonable defaults or ask the user. See `resources/parsing-unstructured.md`.

**Signature C — raw prose.** A memo, a draft, or a transcript discussing "places this text is unclear." No formal scenario structure. The skill must do more work: identify candidate ambiguities, split into discrete scenarios, propose a defect family for each. Confirm the extraction with the user before rendering — the rendered output is only as good as the structure.

In all three cases, the source text (the statute / contract / regulation / opinion being audited) needs to be identified. If the input does not include the full source text, ask the user to provide it. The skill can render scenarios without the source, but the result is much weaker — the source is the spine of the document.

## Stage 2 — Build the canonical spec

The spec schema is documented fully in `resources/data-format.md`. The top-level shape:

```
{
  "meta": { title, subtitle, kicker, audit_date, profile, brand_short, brand_sub },
  "design": { accent_color, accent_soft, dept_color, adv_color, ... },
  "source": { name, sections: [ { id, label, subhead, text, subprovisions: [...] } ] },
  "families": [ { key, label, description, diagnostic } ],
  "scenarios": [ { id, title, tagline, anchors, families, situation, positions, weak_point, likely_outcome, redraft } ],
  "coverage_list": [ { label, note } ],
  "methodology": { workflow, filter, profile, scope, research, provenance }
}
```

Build this iteratively: start with the source text and the scenarios (the two most important), then add the optional sections (families, coverage list, methodology) if the input supplied them or if the user wants them. The `families` block is auto-derivable from the family keys used in scenarios; supply a default label table and let the user override descriptions.

**Anchor IDs.** Every scenario links to one or more provisions of the source. Anchor IDs must match the IDs assigned to provisions in `source.sections`. Use a consistent scheme — for statutes, ID by subdivision marker (`a`, `b1`, `b2`, `b6B`, `c`); for contracts, by clause number (`s2_1`, `s2_1_a`); for opinions, by paragraph or holding-fragment (`p3`, `holding_1`).

Save the spec to `<output-dir>/spec.json` before rendering. This makes the rendering deterministic and re-runnable when the user wants design tweaks without rebuilding the analysis.

## Stage 3 — Choose the format and design

### Capability check — do this first

Establish what the host can do before offering anything. Three questions, answered once:

1. **Can it run Python 3 and write files?** The two website renderers and the LaTeX renderer are bundled scripts; without script execution and a writable directory, none of them can run.
2. **Are the `docx` and `pptx` skills available?** Those two formats delegate to them.
3. **Is a LaTeX distribution installed?** Only relevant if the user wants a compiled PDF rather than the `.tex` source.

Do not guess. Where a capability is uncertain, the cheapest test is to attempt the smallest version of it and see. Then offer the user only the formats that will actually complete, and say briefly why any others are unavailable — "no Python here, so the multi-page site is out; single-file HTML gives you the same content in one page" is a better experience than a failure five minutes in.

If nothing but plain text is possible, say so plainly rather than half-rendering. A user told at the outset can go elsewhere; a user told at the end has lost the work.

### The six options

| Format | Requires | When to use |
|--------|----------|-------------|
| Multi-page website (default where available) | Python 3 + filesystem | Citeable per-scenario URLs; reference site readers will come back to; deployable to Netlify or any static host. |
| Single-page interactive website | Python 3 + filesystem | Dashboard view of everything at once; cross-linking by click; good for an in-house tool or an exhibit. |
| Single-file HTML | Nothing | One self-contained `.html` file, written directly without the scripts. The universal fallback, and the right answer whenever the deliverable needs to be emailed or opened by someone who will not unzip a folder. See `resources/format-inline-html.md`. |
| Microsoft Word document | `docx` skill | A litigator or legislator who will read in Word; reviewable with tracked changes; printable. |
| PowerPoint deck | `pptx` skill | A meeting, a CLE, a pitch — one scenario per slide, family color on the band, speaker notes carrying the analysis. |
| LaTeX source | Python 3 + filesystem | A typeset deliverable for an academic audience; footnotes for analysis; submission-quality typography. Produces `.tex`; compiling it to PDF needs a LaTeX distribution on the user's machine. Do not promise a PDF before confirming one is installed. |

**Design tokens.** Five values cover 95% of customization needs: `accent_color` (the primary brand color — red-orange burnt-sienna by default), `accent_soft` (a lighter complement, auto-derived if not supplied), `dept_color` (Position A side panel — slate blue by default), `adv_color` (Position B side panel — usually mirrors accent), and `background_color` (warm cream by default). Fonts default to Fraunces / Inter / Crimson Pro on the web, system serifs in Word, and Latin Modern in LaTeX. Family color palette is fixed but can be overridden via `design.family_palette`.

If the user specifies a brand context — "for a corporate audit," "in our firm's colors," "for a state legislator" — match the palette to that. A corporate audit reads cleaner with navy + slate; legislative work reads better with the warmer default; academic work can lean to monochrome.

## Stage 4 — Render

Each format has its own reference file with detailed instructions. Read the relevant one before rendering. The rough invocations:

**Website** (multi or single page) — bundled script:
```bash
python scripts/generate_site.py \
  --spec <output-dir>/spec.json \
  --out <output-dir>/site \
  --mode multi    # or "single"
```
The script emits a complete static site (HTML + CSS) ready to upload to Netlify. See `resources/format-website.md`.

**Single-file HTML** — no script. Write one self-contained `.html` file directly from the spec, inlining the stylesheet and every scenario. This is the fallback when Python is unavailable, and a legitimate first choice whenever the deliverable has to survive being emailed. Full instructions in `resources/format-inline-html.md`.

**Word document** — delegate to the `docx` skill. Read `resources/format-docx.md` for the document structure (title page, executive summary, statute-as-block, scenarios as level-2 sections, redrafts appendix, methodology appendix). Build via the docx skill's python-docx pattern.

**PowerPoint deck** — delegate to the `pptx` skill. Read `resources/format-pptx.md` for the slide structure (title, statute overview, one slide per scenario with family-color band, redrafts slide, methodology slide). Speaker notes carry the analysis. Build via the pptx skill's tooling.

**LaTeX** — bundled script:
```bash
python scripts/generate_latex.py \
  --spec <output-dir>/spec.json \
  --out <output-dir>/report.tex
```
The script emits a self-contained `.tex` file using the article class with a clean preamble. **The deliverable is the `.tex`.** Compiling it to PDF requires a LaTeX distribution — `latexmk -pdf report.tex`, or pdflatex run twice. Attempt the compile only where a distribution is present; where it is not, hand over the `.tex` and say plainly that it needs LaTeX to typeset, rather than reporting a failed PDF. See `resources/format-latex.md`.

**All formats at once.** If the user asks for all formats from one invocation, run the renderers in sequence and present each output. This is useful when a deliverable is going to a mixed audience (the litigator wants the Word doc, the colleague wants the link to the site, the meeting wants the deck).

## Output organization

Default output directory: `<source-name>-ambiguity/` in the workspace folder if one is connected, otherwise in the temporary outputs folder. Within it:

```
<source-name>-ambiguity/
├── spec.json              # The canonical spec — re-renderable
├── site/                  # If website was requested (multi or single)
├── site.zip               # The site folder, zipped for delivery
├── report.html            # If single-file HTML was requested
├── report.docx            # If Word was requested
├── deck.pptx              # If PowerPoint was requested
├── report.tex             # If LaTeX was requested
└── report.pdf             # Only if a LaTeX distribution was present and compilation succeeded
```

Deliver each produced file to the user by whatever mechanism the host provides — a file-presentation or file-sending tool if one exists, otherwise state the output paths plainly.

**Zip the site folder before handing it over.** A multi-page site is dozens of files, and delivering a loose directory to someone working in a chat window is its own small frustration. Produce `site.zip` alongside `site/`, deliver the zip, and point at `site/index.html` as the entry point. The user can unzip and drag the folder to Netlify Drop, or upload it to any static host, to deploy. Single-file HTML needs none of this — it is one file by design.

## What this skill does not do

- It does not perform the ambiguity analysis itself. That is the job of `ambiguity-stress-test`. This skill turns analysis into a deliverable; it does not generate scenarios from a bare legal text.
- It does not edit the source text — only quotes it.
- It does not verify citations or check current law. If the underlying analysis relies on case law that may have changed, the skill should add a research note to the methodology section but cannot itself confirm currency. Cite-checking would be a separate pass.
- It does not produce printed-paper layouts. The LaTeX path produces a screen-readable PDF; print-specific layout (booklet format, court submission formats) is the province of more specialized skills like `scotus-amicus`.

## When the user asks for design tweaks

Re-render from the saved `spec.json` with the new design tokens. Do not re-parse the input. This is what makes the spec file worth saving — design iteration is fast and deterministic.

## Bundled resources

Read the two or three files the job actually needs; do not read all six.

- `resources/data-format.md` — the canonical spec schema. Read this in Stage 2 before building the spec.
- `resources/parsing-unstructured.md` — heuristics for extracting scenarios from less-structured input. Read this in Stage 1 if the input is Signature B or C.
- `resources/format-website.md` — how the website renderer works, deployment to Netlify, the design system.
- `resources/format-inline-html.md` — the single-file HTML fallback, written directly without the scripts. Read this whenever the host cannot run Python, or the deliverable must travel as one attachment.
- `resources/format-docx.md` — Word document structure, delegated to the docx skill.
- `resources/format-pptx.md` — PowerPoint structure, delegated to the pptx skill.
- `resources/format-latex.md` — LaTeX preamble, document class, compilation.
- `scripts/generate_site.py` — the website renderer. Python 3, standard library only.
- `scripts/generate_latex.py` — the LaTeX renderer. Python 3, standard library only.
- `assets/site-style.css` and `assets/latex-preamble.tex` — the stylesheets the two renderers read. `generate_site.py` resolves `assets/site-style.css` relative to its own location, so keep the `scripts/` and `assets/` folders as siblings.

## Limitations and risks

This skill formats an analysis someone else produced. It does not evaluate whether that analysis is correct, and a polished deliverable makes a weak audit look authoritative. Nothing it produces is legal advice.

**It inherits every defect in its input.** Wrong scenarios render as beautifully as right ones. Where fields were missing, the skill fills defaults and surfaces what it inferred — read those notes before circulating the result.

**It does not check citations or currency.** If the underlying analysis rests on case law that has moved, the deliverable will reproduce the error. The methodology section can carry a research note; the skill cannot itself confirm anything.

**Most formats need a capable host.** Both website renderers and the LaTeX renderer are Python scripts that write files; Word and PowerPoint delegate to the `docx` and `pptx` skills. Where none of that is available, single-file HTML still works and requires nothing — which is why the capability check in Stage 3 comes before the format conversation rather than after it.

**The PDF needs a LaTeX distribution.** The script emits `.tex`; compiling to PDF requires `latexmk`, `pdflatex`, or `xelatex` on the machine. Absent one, the `.tex` file is still the deliverable — do not present that as a failure.

**The script-generated website loads fonts from Google Fonts.** Those pages call an external service when opened, and fall back to system fonts offline or behind a restrictive network. Where that matters — a confidential audit, an air-gapped review — either override the font tokens in the spec with a local stack, or use single-file HTML, which by design embeds no web fonts and makes no outbound request.

**Quoted source text travels with the deliverable.** A rendered audit reproduces passages of the instrument it analyses. Check before publishing a site or sharing a deck built from a confidential draft.

The two scripts use only the Python standard library. They make no network calls, spawn no subprocesses, and write only inside the output directory the caller names.
