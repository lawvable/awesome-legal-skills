# Generation workflow (shared core)

Diagram-generation core shared by `direct.md` and `guided.md`. Lanes differ only in elicitation and confirmation; generation = identical, lives here once.

**Caller contract.** Inputs: enriched `ExtractionResult`, `intent` string (or fixed Mermaid type), `mode` (`direct` | `guided`), output preferences (HTML flag, path override).

## Step 1 — Select type

Fixed Mermaid type from caller → if type is `mindmap`, apply precision guard per `shared/diagram-type-map.md` § Mindmap scope rule before honouring it. Otherwise proceed directly. Run `python scripts/diagram_selector.py --extraction-json <enriched JSON>` with intent. Keep `recommended_type`, `rationale`, `alternatives`, `confidence`, `density` (the inclusion target consumed at Step 3.4), and `geometry` (the layout-legibility verdict also consumed at Step 3.4).

Confidence gate, **direct mode only** (hard cap 1): < 0.50 → present top 2 and ask once; ≥ 0.50 → proceed. Guided mode never blocks here; already showed digest and offers alternatives at delivery.

## Step 2 — Guards

Load `shared/parser-guards.md`; apply guards for type. For `erDiagram`/`flowchart`, normalise entity names per § Entity name normalization (log each substitution).

## Step 3 — Generate

Emit fenced Mermaid block natively. Cap node-label WIDTH at ~40 chars (a width limit, not a content limit): split long content into more nodes, never drop or merge entities to fit. Self-check: every referenced node declared; no unclosed brackets or quotes; every node and edge label holding a metacharacter (`( ) [ ] { } | : ; # & < > " ,`) double-quoted per `shared/parser-guards.md` § Node and edge labels; reserved-word IDs (`end`, `state`, etc.) normalised; no trailing `%%` comments.

**Grouping and nesting (when `grouping_suggested: true`, or `extraction_result.hierarchy` is populated).** Build containment, `flowchart TB`:
- `hierarchy` populated → nest by node depth: depth 0 = outermost subgraph, depth 1 nested inside its `parent`, depth 2 inside that. Hard cap depth 2; deeper tiers collapse to one summary node (detail → figure description).
- No `hierarchy` → one containment layer keyed by `grouping_axis`. `axis: "era"` → group events by period; chain chronologically within each.
- Each subgraph: unique alphanumeric ID (reuse the `hierarchy` node `id`), human-readable label, `direction TB`. Too many siblings in one subgraph → split by a sub-axis first; collapse to a summary node only as a last resort. "Never shrink" governs font/spacing/canvas, not node count.

**Readability over fit.** Never shrink font, spacing, or canvas to fit, and never over-truncate; these govern presentation, not node count. Size to content; HTML export pans and zooms, so large-but-legible beats small-but-cramped. The ~40-char cap limits label WIDTH only: split content into more nodes rather than dropping or merging it; full verbatim text also lives in the figure description, never as a substitute for a node.

## Step 3.4 — Node density (carry detail in the diagram)

Detail belongs in the diagram, not only the figure description. Set node count by the caller's `intent`, measured against **salient entities** (the populated `ExtractionResult` list fields: parties, events, obligations, deadlines, decision_points, payments, risk_items, conditions, documents):

| Intent | Surface as nodes |
|---|---|
| comprehensive / exhaustive / "everything" | 85-95% of salient entities |
| detailed / thorough | 60-75% |
| overview / "at a glance" / high-level | 30-45% |

Default to **comprehensive** when intent is ambiguous, or when the user asks for both "detailed" and "at a glance" (pan/zoom makes a large diagram glanceable). Worked example: 100 obligations + comprehensive intent → ~85-95 nodes.

**Split before collapse.** When a group has too many siblings, split by a sub-axis (date, party, type). Collapse into a summary node only as a last resort (depth cap hit or genuinely unreadable); then spill every omitted entity verbatim, with its source ref, into the figure description. Never drop an entity silently.

If `diagram_selector` emitted a `density` block, treat its inclusion band as the target: meet it, or state why you deviated.

**Geometry gate (shape, not coverage).** Density sets how many entities become nodes; geometry judges whether those nodes lay out legibly. Breadth, the nodes in the widest rank, drives the squeeze, not the total count: a deep-narrow diagram is fine, a shallow-wide one is unreadable. If `diagram_selector` emitted a `geometry` block, act on its `band`:

- `green` → ship as one diagram.
- `warn` → ship one, fold the limitation (wide rank, deep fan-out) into the figure description; rebalance `direction` or trim cross-edges if easy.
- `split` → split into multiple focused diagrams BEFORE export, along `geometry.split_axis_suggestion` (date, party, type). Keep each child within the green band (each rank ≤ ~6-7 nodes); a child still over band splits again. Each child exports as its own file per `workflows/html-export.md` § Multiple diagrams. This is the escalation rung between subgraph sub-axis split and collapse-to-summary; it redistributes the same entities across more diagrams and never drops one.

Zoom is not a substitute: pan/zoom rescues a deep-narrow diagram, but a wide rank drops the fit-to-frame font below legibility, so a breadth-driven `split` verdict needs an actual split.

**Preview before export (best-effort).** Before offering the HTML report, confirm the fenced Mermaid block rendered without a "Syntax error" in your preview surface (the web-app artifact, or a local Mermaid preview). On the CLI the preview and export engines are the same pinned Mermaid 11; on the web app the preview engine is platform-controlled and may differ from the export engine, so a clean preview is a strong signal, not a guarantee. No preview available → skip this and rely on the export-time render check.

## Step 3.5 — Build semantic map

After fenced Mermaid block assembled, classify all node IDs for HTML export colour layer. Load `shared/node-styles.md`.

1. **Active palette** = base 5 categories + domain extension rows matching `extraction_result.matter_type`.
2. **Deterministic pass**: for each promoted entity in `extraction_result`, look up field in § ExtractionResult field → category mapping table. Map node ID (label used in Mermaid source) to corresponding `sem-*` class. Add `sem-risk-high` to any obligation/deadline node where `risk_level == "high"`.
3. **Residual pass**: for any node ID not yet classified (subgraph labels, connector text, synthesised nodes), classify from active palette only using residual classification prompt in `shared/node-styles.md` § Residual classification. Return JSON only.
4. **Containers (grouped diagrams only)**: when the diagram uses subgraphs, map each subgraph ID to its nesting depth, `0` for the outermost layer, `1` one level in, and so on. Ungrouped diagram → omit or leave empty.
5. **Emit semantic map**:
   ```json
   {
     "meta": { "matter_type": "...", "diagram_type": "...", "active_palette": [...] },
     "nodes": { "NODE_ID": "sem-class", ... },
     "containers": { "SUBGRAPH_ID": 0, ... }
   }
   ```
   Store as `semantic_map_json` and pass to `workflows/html-export.md`. Discard if HTML export declined.

**⛔ Class name constraint.** Only use classes defined in `shared/node-styles.md` § Universal base palette and § Domain extension palettes. The valid classes are: `sem-party`, `sem-authority`, `sem-risk`, `sem-outcome`, `sem-process`, `sem-evidence`, `sem-claim`, `sem-ownership`, `sem-financial`, `sem-control`, `sem-gap`, `sem-dataflow`, `sem-finding`, `sem-ip-asset`, and modifier `sem-risk-high`. Never invent new `sem-*` class names — unlisted classes produce no colour.

**classDef injection (automatic).** `render_html.py` derives Mermaid `classDef` + `class` statements from `semantic_map.nodes` and appends them to the diagram block at render time. This is the primary node-colouring mechanism for `flowchart` and `stateDiagram` types. Do **not** emit `classDef` or `class` statements manually in the Mermaid block — `render_html.py` owns this step.

**Container shading (automatic).** `render_html.py` derives Mermaid `style <subgraph-id> fill:...` statements from `semantic_map.containers`, shading each subgraph by depth tier (light to dark, greyscale, flowchart/graph only; depth beyond tier 2 clamps). Do **not** emit container `style` statements manually. Tier shades: `shared/node-styles.md` § Container tier palette.

## Step 3.6 — Build digest table (always, unless declined)

Build `digest_rows` from `ExtractionResult` for the Source Docs tab in HTML export. **Default = always emit.** Skip only if user has explicitly said "no source table", "no verification table", or equivalent in this session.

For each populated field in `ExtractionResult` (obligations, conditions, deadlines, events, parties, decision_points, risk_items), emit one row per entity:

| Field | `row.category` |
|---|---|
| `obligations` | `Obligation` |
| `conditions` | `Condition` |
| `deadlines` | `Deadline` |
| `events` | `Key Event` |
| `parties` | `Party` |
| `decision_points` | `Decision` |
| `risk_items` | `Risk` |
| `documents` | `Document` |
| hint-only / unverified | same category + `unverified: true` |

Row fields: `row_num` (sequential), `category`, `finding` (short label), `party` (or null), `verbatim` (exact text from document — use `extraction_hints[].snippet` or `llm_enrichment.evidence_packets[].text`; never paraphrase), `anchor` (paragraph/section ref from `source_ref` or `anchor` field), `source_doc` (basename of input file).

Mark `unverified: true` for any hint-only entity or any entity where source text could not be confirmed from extraction evidence. These render with ⚠ in the table.

## Step 4 — Deliver (rationale + alternatives)

Use plain-language diagram names from `shared/diagram-type-map.md` § Plain-language names in everything user reads. Never print a Mermaid-internal type name to user.

**If `mode == "guided"`:** show the fenced Mermaid block and sanitizations only. No rationale, no alternatives; the user saw both at Step 2.5.

**If `mode == "direct"`:** full output, no preamble:
1. Fenced Mermaid block inline (block uses technical syntax; expected and fine).
2. Rationale, one plain-language line: "I drew a <plain name> because <selector rationale, rephrased plainly>."
3. Alternatives, one line: "This matter would also work as a <plain alt1> (<what it shows>) or a <plain alt2> (<what it shows>) — want either?" Pull "what it shows" from `shared/figure-description-schema.md` caption patterns. Offer only types a populated driving field supports; never list a type with no backing data.
4. Bullet list of any sanitizations (normalized names, escaped colons, truncated labels).

## Step 5 — Output and GATE B (HTML report) ⛔ BLOCKING

No note file written. The fenced Mermaid block (Step 3-4) renders as an artifact in the Claude web app and as syntax-highlighted code in the CLI.

GATE B = mandatory hard stop. Always fires unless user typed a literal `--html` flag, which pre-answers it as **HTML report**. Never infer the answer from wording; do not skip it. Present **GATE B** as structured choice (the question tool), or numbered plain-text list if host has no choice tool, not a typed Y/n, then STOP, wait for reply. Lead plainly: "Want the full report as a file you can open, print, and share? It pairs the diagram with a table of the exact wording from your document for each item found." Options:

- **HTML report** (recommended, list first)
- **No, just the diagram**

**HTML report** → set `html_export=true`, then load `workflows/html-export.md` (it skips its own opt-in when the flag is set), passing `semantic_map_json` (Step 3.5), `digest_rows` (Step 3.6), and `source_path`. Confirm in plain English when done. **No, just the diagram** → continue to Step 6.

Single HTML decision point for both lanes; do not pre-choose HTML earlier and do not ask twice.

## Step 6 — Refine / branch

Before refine prompt, re-surface a compact reference of diagram contents so users without Mermaid knowledge have concrete handles. Format depends on diagram type:

- **flowchart / stateDiagram / sequenceDiagram**: list subgraph/group names and the main node labels within each, e.g. "**No Written Rule** — Commissioner's Message, Rationale shifted, Not broadcast on WITV · **Minor Court Void** — Ordered charge himself, Presided as judge, Conflict admitted …"
- **erDiagram / classDiagram**: list entity names and their relationships.
- **timeline / gantt**: list section headers and key events/tasks.
- **mindmap**: list top-level branches.
- **other types**: list the primary labelled elements.

Then: "Want to change anything? Describe it in plain English, name an alternative diagram type, or ask for the HTML report." If HTML was declined at GATE B and the user now asks for it, load `workflows/html-export.md`.

Accept plain-English change descriptions ("remove the Arbour point", "rename CM Pitts to Correctional Manager Pitts", "add a node for the settlement offer") → translate to structural edits before re-generating. Re-run guards on any new block. Named alternative type → fresh generation pass. If HTML was exported, re-invoke `workflows/html-export.md` in full (rebuild FigureDescription; never reuse a stale one).
