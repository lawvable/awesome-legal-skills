# Node styles — semantic colour system

Load at Step 3.5 of `workflows/generation.md` (semantic map build) and Step 2 of `workflows/html-export.md`.

## Universal base palette (always active, all diagram types)

|Category|CSS class|Fill|Stroke|Accessibility pattern|
|---|---|---|---|---|
|Party / Stakeholder|`sem-party`|`#C9D6E3`|`#8FA8BE`|none|
|Authority / Rule|`sem-authority`|`#CAD2C5`|`#8A9E84`|diagonal hatch|
|Risk / Concern|`sem-risk`|`#D6B8B8`|`#A87878`|cross-hatch|
|Outcome / Position|`sem-outcome`|`#CFCFCF`|`#909090`|dots|
|Process Step|`sem-process`|`#F5F3EE`|`#B0A898`|none (default neutral)|

Risk modifier (additive, stacks with any category): `sem-risk-high` — applied to any node from an obligation or deadline with `risk_level: "high"`; darkens stroke to `#8B4444`, stroke-width 2.5.

## Domain extension palettes (keyed on `matter_type`)

Load matching row(s) when `extraction_result.matter_type` matches. Unknown or absent `matter_type` → base palette only.

|matter_type|Category|CSS class|Fill|Stroke|Pattern|
|---|---|---|---|---|---|
|litigation|Evidence / Record|`sem-evidence`|`#D8D3E8`|`#9888B8`|dots|
|litigation|Claim Element|`sem-claim`|`#DDD2C2`|`#A89878`|diagonal hatch|
|corporate|Ownership Link|`sem-ownership`|`#D3DDE8`|`#7898B8`|diagonal hatch|
|corporate|Financial Node|`sem-financial`|`#E6D3A3`|`#B89840`|dots|
|compliance|Control|`sem-control`|`#D4E8D3`|`#78A878`|diagonal hatch|
|compliance|Gap|`sem-gap`|`#E8D6B8`|`#B89860`|cross-hatch|
|privacy|Data Flow|`sem-dataflow`|`#D8E8E3`|`#78A898`|dots|
|employment|Finding|`sem-finding`|`#E3D8E8`|`#9878A8`|dots|
|ip|IP Asset|`sem-ip-asset`|`#D8E3D8`|`#789878`|diagonal hatch|
|tax, bankruptcy|Financial Node|`sem-financial`|`#E6D3A3`|`#B89840`|dots|

## ExtractionResult field → category mapping (deterministic lookup)

Apply before any LLM classification. A node ID matching a promoted entity from a known field is assigned deterministically — no inference needed.

|ExtractionResult field|Base category|Matter-type override|
|---|---|---|
|`parties`|`sem-party`|—|
|`entities`|`sem-party`|—|
|`legal_authorities`|`sem-authority`|—|
|`controls`|`sem-authority`|compliance → `sem-control`|
|`risk_items`|`sem-risk`|—|
|`claim_classes`|`sem-risk`|litigation → `sem-claim`|
|`decision_points`|`sem-risk`|—|
|`events`, `process_steps`, `phases`, `tasks`, `investigation_steps`|`sem-process`|—|
|`obligations`, `deadlines`, `conditions`|`sem-process`|+ `sem-risk-high` if `risk_level: "high"`|
|`documents`, `witnesses`|`sem-process`|litigation → `sem-evidence`|
|`ownership_links`, `transfers`|`sem-process`|corporate/tax → `sem-ownership` or `sem-financial`|
|`data_flows`, `communications`|`sem-process`|privacy → `sem-dataflow`|
|`states`, `transitions`|`sem-process`|—|
|`concepts`, `negotiation_issues`|`sem-risk`|—|
|`ip_assets`|`sem-process`|ip → `sem-ip-asset`|
|Inferred conclusion / outcome nodes|`sem-outcome`|—|

## Residual classification (LLM pass)

Nodes not matched by field lookup above (subgraph labels, connector bridging text, synthesised nodes, outcome summary nodes) → classify by LLM. Constrain LLM to **active category set only** (base 5 + domain extensions for current `matter_type`). Bounds active set to ≤10 categories; keeps classification consistent across sessions.

Prompt snippet to include in Step 3.5:
> Classify each unlisted node ID using only the active categories below. Return JSON only — no prose.
> Active categories: [list `sem-*` class names from active palette]
> Format: `{"NODE_ID": "sem-class", "NODE_ID": "sem-class sem-risk-high"}`
> Rules: (1) use the exact class names; (2) classes are space-separated and additive; (3) if genuinely ambiguous, assign `sem-process`.

## Semantic map JSON schema

Generation step emits this object as `semantic_map_json` and passes it to HTML export step:

```json
{
  "meta": {
    "matter_type": "litigation",
    "diagram_type": "flowchart",
    "active_palette": ["sem-party", "sem-authority", "sem-risk", "sem-outcome", "sem-process", "sem-evidence", "sem-claim"]
  },
  "nodes": {
    "CLAIM": "sem-claim",
    "ISSUE1": "sem-claim",
    "NWR1": "sem-authority",
    "NWR2": "sem-authority",
    "SEC": "sem-outcome",
    "RELIEF": "sem-outcome",
    "NWRC": "sem-outcome sem-risk-high"
  }
}
```

`meta.active_palette` drives legend; list all classes used in `nodes`, deduplicated, base categories first.

## CSS class naming contract

- Prefix: always `sem-`
- Classes additive: a node can carry `sem-process sem-risk-high`
- Primary class (first) determines fill colour and pattern; modifier classes adjust stroke only
- Never invent new class names outside this reference — add to this file if a new category is needed

## Container tier palette

Subgraph containers (grouping or nesting) shade by nesting depth, not by semantic category. Greyscale, so they never collide with the coloured node `sem-*` fills. `render_html.py` emits `style <subgraph-id> fill:...` from `semantic_map.containers` (flowchart/graph only); depth beyond tier 2 clamps to tier 2.

|Tier|Depth|Fill|Stroke|
|---|---|---|---|
|0|outermost|`#F7F7F5`|`#D8D8D2`|
|1|one level in|`#ECECE6`|`#C8C8C0`|
|2|two levels in|`#E0E0D8`|`#B8B8AE`|

Contract: tier shades are greyscale only; never reuse a node `sem-*` fill. Containers encode depth, not category.
