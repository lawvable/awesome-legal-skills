# Format — LaTeX → PDF

The LaTeX path produces a self-contained `.tex` file that compiles to a polished PDF. Suitable for an academic audience, a law review submission, or any context where typeset typography matters.

## Generator

```bash
python scripts/generate_latex.py \
  --spec <output-dir>/spec.json \
  --out <output-dir>/report.tex
```

The script emits a single `.tex` file with all preamble inline (no `\input` of external files needed). The user compiles with their preferred LaTeX engine — `latexmk -pdf`, `pdflatex` (twice for cross-references), or `xelatex` if they want non-default fonts.

## Document class and packages

Default: `article` class, 11pt, letterpaper. The preamble loads:

- `geometry` — 1in margins
- `xcolor` — for the color palette
- `tcolorbox` — for the two-sides position panels and the redraft callouts
- `enumitem` — for cleaner lists
- `titlesec` — for heading customization
- `hyperref` — for cross-references and clickable anchors
- `microtype` — for typographic polish
- `fontspec` (if xelatex) — for custom fonts; otherwise the script uses Latin Modern

The colors are bound to LaTeX color definitions named after the spec keys (`accentColor`, `deptColor`, `advColor`, etc.). Family colors are named `famScopeBg`, `famScopeFg`, etc.

## Document structure

The LaTeX document mirrors the website's information architecture but in linear form.

**Title block.**
```latex
\title{\textsc{\small Interpretive-Ambiguity Stress-Test}\\[1em]
       {\Huge \textsf{Where {\source name} will be fought over}}\\[0.5em]
       \large \textit{{page subtitle}}}
\date{{audit_date}}
```

**Front matter.**
- Title.
- A brief lede block (one paragraph from `meta.page_subtitle`).
- A scenario-list table of contents (custom — not the standard `\tableofcontents` but a styled list).

**Part I — The source.**
- `\section*{The source}` with `\addcontentsline` so it appears in the TOC.
- Render the source text using `\subsection` for top-level sections and indented blocks for subprovisions. Each provision in a `quote` environment with the label in bold.
- Anchored provisions get marginal numbered badges via `\marginpar`. The badge is a `\tcbox` with the scenario number.

**Part II — The scenarios.**
- `\section*{The {N} fights}`
- For each scenario:
  - `\subsection*{S-N · {title}}`
  - Tagline in italics below.
  - Anchors and families on a single line as `\fbox`'d small text.
  - **The situation:** in a styled `tcolorbox` with thin gray border, sand-colored fill.
  - **Two-sides panel:** two side-by-side `tcolorbox`es (use `tcbraster` for layout). Left: Position A. Right: Position B. Each has a colored top border, the actor name in `\textsc`, and the argument body.
  - **Weak point:** a description-list entry. `\textbf{Weak point.} \itshape ...`
  - **Likely outcome:** same pattern.
  - **Redraft:** a `tcolorbox` with yellow tint, label "Proposed amendment" in small caps, body in italic.
  - `\rule` separator before the next scenario.

**Part III — Redrafts.**
- `\section*{Proposed amendments}`
- Brief lede about the package.
- For each scenario's redraft:
  - `\subsection*{R-N · {short title}}`
  - Target provision in italic small caps under the heading.
  - Problem statement.
  - Proposal in a `tcolorbox` (same style as the in-scenario redraft).

**Part IV — Coverage list (if present).**
- `\section*{Additional ambiguities flagged}`
- `\description`-style list: bold label, then note.

**Part V — Methodology (if present).**
- `\section*{Methodology}`
- Subsections for each `methodology.*` key.
- Provenance line as italic footer.

## Footnotes for analytical depth

Where appropriate, push secondary detail to footnotes rather than crowding the main text. For example, the "likely outcome" paragraph might have a footnote citing the specific canon, or the redraft might footnote the source of the language.

This is what LaTeX is for. Lean into it.

## Cross-references

Use `\label` and `\autoref`:
- Each scenario heading: `\label{scen:N}`
- Each source provision: `\label{prov:ID}` where ID is the provision ID from spec
- Each redraft heading: `\label{redraft:N}`

Then "see Scenario S-2" becomes `see \autoref{scen:2}` and the hyperref package makes it clickable in the PDF.

## tcolorbox styles

Define three styles in the preamble for re-use:

```latex
\tcbset{
  situationbox/.style={
    colback=panelColor, colframe=accentSoft,
    boxrule=0.5pt, arc=2pt,
    left=10pt, right=10pt, top=8pt, bottom=8pt,
  },
  positionA/.style={
    colback=deptBg, colframe=deptColor,
    boxrule=0pt, leftrule=0pt, rightrule=0pt, bottomrule=0pt, toprule=2pt,
    arc=2pt, left=10pt, right=10pt, top=8pt, bottom=8pt,
  },
  positionB/.style={
    colback=advBg, colframe=advColor,
    boxrule=0pt, leftrule=0pt, rightrule=0pt, bottomrule=0pt, toprule=2pt,
    arc=2pt, left=10pt, right=10pt, top=8pt, bottom=8pt,
  },
  redraftbox/.style={
    colback=redraftBg, colframe=redraftBorder,
    boxrule=0.5pt, arc=2pt,
    left=10pt, right=10pt, top=8pt, bottom=8pt,
  }
}
```

## Compilation

The generator does not compile the PDF. The user compiles. Suggest:

```bash
latexmk -pdf report.tex
```

If `latexmk` is not available:

```bash
pdflatex report.tex
pdflatex report.tex   # second pass for cross-references
```

If the compilation fails (e.g., `tcolorbox` not installed), surface the error to the user and suggest installing the missing package. The MacTeX / TeX Live distributions include `tcolorbox` by default; very minimal LaTeX installations may not.

## Alternative document classes

The default is `article`. Future expansions could expose:

- **Tufte-LaTeX** — for sidenotes and a wider margin layout. Best when the analysis has heavy commentary that wants to live in the margin.
- **Beamer** — LaTeX equivalent of PowerPoint. Use the pptx path instead unless the user specifically wants Beamer output.
- **Memoir** — for book-length deliverables. Overkill for most ambiguity audits.

Not currently supported in the V1; if the user asks for one of these, note that it's future work and offer the article-class output.

## Font customization

If the user provides a `design.primary_font` that LaTeX can find (e.g., a TrueType installed on the system), instruct them to compile with `xelatex` instead of `pdflatex`. The script can detect this from the font choice and add a comment at the top of the `.tex` file:

```latex
% Compile with xelatex (custom fonts requested)
```

Otherwise stick with Latin Modern (the default of pdflatex).

## What this format does well

LaTeX produces typeset PDFs that print cleanly, embed cross-references, and support footnotes naturally. Best when the deliverable will be printed, archived, or submitted to a journal.

## What this format does poorly

LaTeX is not interactive. No filtering, no click-to-highlight, no live cross-pane. For exploratory reading, the website is far better.
