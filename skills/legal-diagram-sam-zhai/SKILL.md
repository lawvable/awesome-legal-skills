---
name: legal-diagram
version: '1.2.0'
description: 'Use when a user needs a legal or legal-adjacent Mermaid diagram from a document, pasted text, matter description, process, timeline, party map, obligation map, corporate structure, funds flow, or compliance workflow. Trigger on: "diagram this contract", "visualise this deal/matter", "map the parties", "create a timeline of events", "make an org chart", "obligation checklist", "export as HTML diagram". Not for general-purpose non-legal diagrams, pure graphic design, image generation, or legal advice.'
argument-hint: '[file path | "pasted text" | matter description] [diagram type] [--guided] [--direct] [--html] [--tutorial]'
---

# /legal-diagram

Standalone skill: turn legal material into a context-appropriate Mermaid diagram, with an optional downloadable HTML figure. A structure-preserving Python engine extracts a typed ground truth; directive-driven LLM enrichment fills the gaps; a selector picks the diagram type; the diagram is generated natively.

## Routing gate

Every real diagram request runs in this fixed order: first-run check, ingest, build-mode gate, generate, report gate. Non-diagram intents short-circuit at Step 0.

Three human gates = mandatory hard stops: GATE 0 (tutorial offer), GATE A (build mode), GATE B (HTML report). Gate discipline, no exceptions:

- Present each as structured choice (the question tool). No such tool → numbered plain-text list. Either way, STOP, wait for reply.
- Never skip a gate. Never infer its answer from wording. Never generate past an unanswered gate. Detailed, specific, or named-diagram request = still a request, not a gate answer.
- Only a literal typed flag may pre-answer: `--direct`/`--guided` (GATE A), `--html` (GATE B), `--tutorial` (tutorial). Nothing else counts.

### Step 0 — Intent and first-run

Check explicit short-circuits first:

1. **Tutorial** signals: "tutorial", "show me how", "first time", "demo", "walk me through", `--tutorial`. → Load `workflows/tutorial.md`. Stop here.
2. **Setup** signals: "check setup", "install deps", "is setup ready". → Load `shared/setup-check.md`, run `check_setup.py`, report. Stop here.

Otherwise this is a real diagram request (a file, pasted text, or a matter description). Detect first-run:

Run `python scripts/first_run.py`. Parse `{state}`: `returning`, `first_run`, or `unknown`. Script absent, non-zero exit, or no JSON → treat as `unknown`.

- `returning` (confirmed) → no offer; user ran skill before. Continue to Step 1.
- `first_run`, `unknown`, or anything not a confirmed `returning` → **GATE 0** (hard stop): "First time here. Want a quick tutorial, or go straight to your diagram?" Options: **Start tutorial** (recommended, list first) / **Skip, straight to my diagram**. Present as structured choice, or numbered plain-text list if host has no choice tool, then STOP, wait for reply. After answer, run `python scripts/first_run.py --mark` to record offer (best-effort; on `unknown` state with no writable disk, mark may not persist, fine). Then: tutorial → load `workflows/tutorial.md`, stop; skip → continue to Step 1.

`unknown` defaults to offering, not suppressing: surface the choice, do not decide for user. Suppress only on confirmed `returning`. Tutorial stays reachable any time by keyword.

### Step 1 — Ingest before choosing a lane

Detect input: file path, pasted text, or conversation/matter description. Load `shared/setup-check.md` (session-cached).

**Multi-file scope gate** (2+ files) ⛔: mandatory hard stop unless user already stated scope. Present as structured choice, or numbered plain-text list if host has no choice tool, then STOP, wait for reply. Options: **One combined diagram** / **One per document**. Never infer scope from wording. Store `diagram_scope`. Single file, or scope user explicitly stated → skip.

Run Pass 1 only (deterministic manifest, no LLM): `workflows/extract.md` Steps 0-2. Store the result as `manifest_cache` and pass it to the chosen lane so Pass 1 never re-runs. Matter-description-only input (no docs) has no Pass 1 counts; proceed without them.

### Step 2 — GATE A: build mode (after ingestion) ⛔ BLOCKING

GATE A = mandatory hard stop. ALWAYS fires unless user typed a literal `--direct` or `--guided` flag. Do not load a lane and do not generate any diagram until GATE A answered.

**Only a literal flag pre-answers.** Sole answer-carrier = exact token `--direct` or `--guided` in user's message. Present → state resolved mode in one line ("Build mode: direct (flag)") and load the lane. User's own recorded choice, not a model decision.

**Everything else → present the gate and STOP.** Detailed, specific, or named-diagram request ("comprehensive diagram of this exact case", "make an org chart") = a request, NOT a gate answer. Never infer build mode from wording. Lead with what Pass 1 found, plain language: "Found [N parties, M events, ...]. How should I build it?" (omit counts for no-docs input). Present as structured choice, or numbered plain-text list if host has no choice tool, then wait for reply. Options, fixed order:

- **Guided, step by step**
- **Direct, just make it**

Do not reorder options, do not mark one implied from wording. Order fixed; choice is user's.

On choice: load `workflows/direct.md` or `workflows/guided.md`, passing `manifest_cache`, `input_source`, and `diagram_scope`. Both lanes share `workflows/generation.md` for the build; GATE B (HTML report) fires there.

**User-facing language (casual-friendly).** Never show Mermaid-internal type names to user. Use the plain-language names in `shared/diagram-type-map.md` § Plain-language names — "timeline", "org chart", "flowchart", "obligation checklist", and so on. Accept plain-word requests too ("make me an org chart") and map them through the same glossary. Legal vocabulary is fine; technical diagram vocabulary stays internal.

**Output language (EN/FR).** Gates, digest, elicitation, and rationale render in the user's prompt language (EN or FR; FR diagram names per the glossary's FR column). Extracted evidence and diagram labels stay verbatim source language, never translated. HTML export chrome follows via `render_html.py --ui-lang en|fr`.

## Scripts

All script commands run from the skill root (the folder containing this `SKILL.md`). Resolve the skill root once, then invoke scripts as `python scripts/<name>.py`.

| Script                        | Role                                                                                    |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| `scripts/check_setup.py`      | Dependency check → `{ok, missing[], installed[], optional{}}`                           |
| `scripts/first_run.py`        | First-run state → `{state}` (`returning`/`first_run`/`unknown`); `--mark` consumes flag |
| `scripts/extract_entities.py` | Orchestrator: normalize → detect → manifest JSON                                        |
| `scripts/diagram_selector.py` | Enriched extraction + intent → recommended type                                         |
| `scripts/patch_gate.py`       | Pass 2 patch gate: validates and applies LLM JSON Patch → `{ok, findings[], enriched_extraction_result}` |
| `scripts/eval_pass2.py`       | Pass 2 eval grader: scores LLM patch against label expectations → `{ok, results[], score}` |
| `scripts/render_html.py`      | Mermaid + FigureDescription → standalone HTML                                           |

`scripts/normalize/` (format adapters) and `scripts/extraction/` (candidate harvesters, resolver, and materializer) are libraries used by the orchestrator. Install deps once: `pip install -r requirements.txt -c constraints.txt` for release-verified versions, or omit `-c constraints.txt` for broad compatibility testing.

## Workflow loading map

| Intent/Need                                                  | File                       |
| ------------------------------------------------------------ | -------------------------- |
| First-run walkthrough + setup gate                           | `workflows/tutorial.md`    |
| Interactive default lane (digest/elicit → menu)              | `workflows/guided.md`      |
| Power-user lane (read all signals, hard cap 1)               | `workflows/direct.md`      |
| Shared generation core (select → guard → generate → deliver) | `workflows/generation.md`  |
| Two-pass extraction (called by both lanes)                   | `workflows/extract.md`     |
| Pass 2 quality eval (execute enrichment, grade against labels) | `workflows/eval-pass2.md`  |
| No-docs intake sets + delivery pattern                       | `shared/elicitation.md`    |
| Standalone HTML figure export                                | `workflows/html-export.md` |

## Reference loading map

| Intent/Need                                                       | File                                  |
| ----------------------------------------------------------------- | ------------------------------------- |
| Dependency-check procedure                                        | `shared/setup-check.md`               |
| Per-type guards, entity normalization, parser bugs                | `shared/parser-guards.md`             |
| FigureDescription fields, captions, legends, risk rubric, caveats | `shared/figure-description-schema.md` |
| 30 legal categories → Mermaid type                                | `shared/diagram-type-map.md`          |
| Semantic node categories, palette, CSS class naming               | `shared/node-styles.md`               |
| Field catalogue + detection tiers + signals                       | `references/extraction-schema.md`     |

## Output

Output is CLI display only: the fenced Mermaid block renders as an artifact in the Claude web app and as syntax-highlighted code in the CLI. No note file is written. After the block, GATE B offers an HTML report as a selectable choice; the export escapes matter text, runs Mermaid in strict mode, uses vendored Mermaid when present, and loads the pinned CDN fallback only when explicitly enabled. Full output rules: `workflows/generation.md` § Step 5.

## Boundaries

Mermaid is for thinking, planning, explaining, and generating structure. It is not legal advice, not a court-ready exhibit, and not a substitute for legal writing. Every diagram carries a caveat line. Confidential material stays in tools approved for that matter.
