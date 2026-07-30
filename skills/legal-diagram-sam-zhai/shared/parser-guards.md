# Parser guards (shared)

Apply guards for active diagram type before emitting block. After generation (all types): every referenced node declared, no unclosed brackets or quotes, every label with a metacharacter double-quoted, labels within budget, one diagram per block.

## Node and edge labels (all bracket/shape types)

Default rule: wrap every node label and every edge label in double quotes whenever it holds anything beyond letters, digits, spaces, and simple hyphens. When unsure, quote. Quoting never changes the rendered glyph; it is always safe.

Mermaid reads bare `(` `)` `[` `]` `{` `}` `|` `#` `:` `;` `&` `<` `>` `"` `,` inside a label as grammar. An unquoted legal citation breaks the parse.

- Correct: `N1["§ 237(a)(2)(A)(iii)"]` and `S1 -->|"per § 237(a)(2)(A)"| S2`
- Wrong: `N1[§ 237(a)(2)(A)(iii)]` (first `(` starts a shape token, Syntax error)

Render-level traps inside an already-quoted label, parse-clean but wrong output, verified on the pinned Mermaid 11.x:

- Literal double-quote: write `#quot;` (e.g. `the #quot;Acquirer#quot;`); a bare `"` closes the string early. Curly quotes `“ ”` are safe.
- Literal `<`: silently truncates the label (read as a tag start); write `&lt;`, or surround with spaces (`a < b`). `>` and `&` auto-escape inside quotes.
- Emphasis: plain `**bold**` renders literally. Bold/italic render only inside a Mermaid markdown-string (backtick-wrapped label text).
- Line break: use `<br>` (works under `securityLevel:'strict'`; `\n` also converts to a break). Prefer splitting into more nodes over long multi-line labels.
- Edge-label pipe: a raw `|` in edge-label text closes the label; keep the label quoted and replace a literal pipe with `/` or `&#124;`.

These label rules are type-specific in two places: `mindmap` and `requirementDiagram` do NOT accept the plain double-quote escape (see their rows).

|Type|Guards|
|---|---|
|`requirementDiagram`|`id:` values alphanumeric only (replace hyphens with `_`, log). Zero indentation inside `{}`. All `requirement` blocks before `element` blocks. The `text:` value cannot hold a comma, a second colon, or a semicolon (grammar ends the value there); rephrase ("pay then notify", "under s.7(2)") or move verbatim wording to the figure description. Quoting does NOT rescue `text:`.|
|`gantt`|`dateFormat` line before `title` and before any `section`. Consistent date format; placeholder dates if missing. Milestone: `:milestone, YYYY-MM-DD, 0d`. A missing or misordered `dateFormat` parses clean but renders BLANK, so the preview check cannot catch it; verify the line is present and ordered by inspection.|
|`state diagram`|Use the current state diagram syntax, never the older shorthand. States + transitions non-empty; warn if skeletal.|
|`mindmap`|Exactly 2 spaces per level, no circular parents. Plain indentation for plain-text leaves. A leaf whose text holds `( ) [ ]` or other shape delimiters MUST use the explicit `id["Claim (a)(2)"]` form; a bare or merely double-quoted leaf with parens breaks the parse. The "no brackets" guidance applies only to plain-text leaves.|
|`sequenceDiagram`|`autonumber` when >5 messages. Declare `participant` aliases at top. Message text after `:` may hold colons, commas, and parens, but NOT a semicolon (it ends the statement); rewrite `;` to a comma or split the message. Participant names must not hold `;`.|
|`erDiagram`|Normalise entity IDs (below): SPACES in an entity ID break node resolution; hyphens parse but normalise to `_` for cross-viewer safety. Relationship labels: quote only when they hold punctuation or specials; a single multi-word label (`A \|\|--o{ B : places order`) parses unquoted. Both cardinality ends required.|
|`flowchart`|Cap label WIDTH at ~40 chars (a width limit, not a content limit; ellipsis if needed): split long content into more nodes, never drop or merge entities to fit; long verbatim text also → figure description. Node IDs alphanumeric; normalise names (below), reserved words included. `&` is the multi-node operator: an unquoted `&` in a party name silently splits the node, so quote any label with `&`. Subgraph titles with specials use the `id["Title (Phase 2)"]` form; a bare unquoted title with parens, colons, or commas breaks. When `grouping_suggested`: containment from `hierarchy` (depth ≤ 2) or one layer keyed by `grouping_axis`; subgraph IDs alphanumeric + unique; `direction TB` per tier; cross-boundary edges allowed, labelled, few.|
|`timeline`|Section headers = bare dates or month names, with NO colon. A colon mid-event-text is fine (it follows the date separator, e.g. `2020 : Filed: served on Acme`). The hazard is event text that STARTS with a colon: prefix a word. Do not blanket-escape colons to `&#58;`; that mangles readable text.|
|`quadrantChart`|x/y scores floats in `[0.0, 1.0]`. Axis labels (`x-axis`/`y-axis`) must hold NO colon (a colon there breaks the parse). Point labels may hold colons; double-quote any point label with `( )`, `:`, or a comma, e.g. `"Claim (a)(2)": [0.3, 0.6]`.|

## Grouping and readability

Applies when selector sets `grouping_suggested` (set by the density signal or the geometry gate; see `workflows/generation.md` Step 3.4).

- **Depth cap 2.** Nesting follows `extraction_result.hierarchy`; hard cap depth 2 (three levels). Deeper tiers collapse to a summary node. Each tier sets `direction`; subgraph IDs unique across all tiers.
- **Size to content, never shrink.** "Never shrink" governs font, spacing, and canvas, not node count. Never compress font or spacing to fit; the HTML viewer pans and zooms, so large-but-legible is correct and cramped is not. Prefer adding nodes over removing detail.
- **Breadth, not count, drives the squeeze.** A diagram fails legibility when one rank (layer) is too wide, not when the total node count is high. A deep-narrow graph is fine; a shallow-wide graph squeezes. The geometry gate flags `band: split` on breadth (verified crossover near 7-8 nodes per rank at a fit-to-frame view).
- **Split before collapse.** A group with too many siblings, or a `split` geometry verdict, splits by a sub-axis (date, party, type) first; for a multi-diagram split see `workflows/generation.md` Step 3.4. Collapse members into a single summary node only as a last resort (depth cap reached or genuinely unreadable); when you do, spill every omitted entity verbatim, with its source ref, into the figure description. Never drop an entity silently.
- **Cross-boundary edges.** Allowed, but label every wall-crossing edge; keep few. Mermaid routing degrades there.

## Entity name normalization

Before `erDiagram`/`flowchart`: node IDs reject spaces; reserved words and hyphens also normalised. Apply in order; log each substitution to user ("Entity name normalised: 'Operating Sub A' → 'OperatingSubA'"):

1. Accents transliterated (NFD-decompose, strip combining marks; node ID only, label keeps accents verbatim): `Société Générale Ltée` → `Societe Generale Ltee`.
2. Spaces removed: `Operating Sub A` → `OperatingSubA`.
3. Hyphens removed: `Sub-A` → `SubA` (cosmetic cross-viewer safety; a hyphen parses but normalise anyway).
4. Leading digit → prefix `E`: `1stFinance` → `E1stFinance`.
5. Collision → numeric suffix: two `OperatingSubA` → `OperatingSubA1`, `OperatingSubA2`.
6. Reserved-word ID → prefix `N_`: `end`, `subgraph`, `class`, `click`, `style`, `graph`, `default`, `direction`, `state` → `N_end`, etc. A bare lowercase `end` as an ID breaks the flowchart parser.

Keep original name in display label: erDiagram relationship label (double-quoted when it holds specials), or flowchart node text `Node["Operating Sub A"]` with ID normalized. Labels containing `«»`, apostrophes, parens, or `,` take the double-quoted form: `SGL["Société Générale Ltée (« l'Acheteuse »)"]`.

## Confirmed bugs (project-verified)

- All bracket types: an unquoted `(` `)` `{` `}` `"` or `|` inside a node or edge label is lexed as a shape/grammar token and throws a Syntax error. Double-quote any label with a metacharacter; for a literal `"` use `#quot;`, for `<` use `&lt;`.
- `flowchart`: a bare lowercase `end` as a node ID breaks the parser; use `End` or `N_end`. An unquoted `&` in a label silently splits one node into two (the multi-node operator); quote it.
- `flowchart`/all types: a trailing `%%` after a statement breaks the parse; comments are valid only on their own line. Do not emit inline comments; put annotation in a label or the figure description.
- `flowchart`: subgraph-to-subgraph links combined with per-subgraph `direction` statements are valid and render on the pinned Mermaid 11.x; they FAILED on the former 10.9.1 pin ("Syntax error"). Keep the engine pinned at 11.x (`render_html.py` `MERMAID_VERSION`).
- `requirementDiagram`: a hyphen in an `id:` value throws `Expecting 'NEWLINE', got 'LINE'` (the `-` is lexed as the `LINE` token). Use `PRIV001`, not `PRIV-001`. The `text:` value also breaks on a comma, a second colon, or a semicolon; quoting does not help, so rephrase.
- `requirementDiagram`: properties inside `{}` must be flush-left; indentation mis-tokenises and fails.
- `gantt`: a missing `dateFormat`, or `dateFormat` after `title`, parses clean but renders blank silently; the parse-based preview will not catch it, so confirm the `dateFormat` line by inspection.
- `timeline`: only event text that STARTS with a colon, or a colon in a section header, breaks the parser; a colon mid-event-text is fine. Do not blanket-escape colons to `&#58;`.
- `sequenceDiagram`: a semicolon in message text or a participant name ends the statement and breaks the parse; commas, colons, and parens in message text are safe.
- `quadrantChart`: a colon in an axis label breaks the parse; point labels tolerate colons but quote any with parens or commas.
- `mindmap`: inconsistent indentation collapses the hierarchy (2 spaces per level throughout); a leaf with parens needs the `id["..."]` form, since the plain double-quote escape fails here.
- `erDiagram`: SPACES in entity IDs break node resolution; hyphens parse (normalise anyway). Relationship labels need quoting only when they hold specials.
- `stateDiagram`: use the current state diagram syntax (older shorthand mis-renders). Verified against the pinned Mermaid 11.x baseline.
- All types: the label cap is a WIDTH limit only. Long labels overflow, so truncate the label and split content into more nodes; never drop or merge entities to fit. The figure description holds the long verbatim text as a supplement to the diagram, not the only home for detail.

## Platform note

Fenced ` ```mermaid ` renders in any Mermaid-capable Markdown viewer (GitHub, VS Code, Obsidian, the Claude web app). HTML export prefers vendored Mermaid; uses pinned CDN fallback only when explicitly enabled. `Sankey`/`architecture`/`kanban` render unevenly; selector substitutes a portable primary (`shared/diagram-type-map.md`).
