# Extract workflow (two-pass)

Sub-workflow called by `direct.md` and `guided.md` (simulated by `tutorial.md`). The routing gate in `SKILL.md` runs Pass 1 before this workflow resumes Pass 2. Returns enriched `ExtractionResult` plus confirmed diagram type.

**Caller contract.** Inputs: `input_source`, `intent_hint`, `mode` (`direct` | `guided` | `tutorial`), `skip_confirmation` (bool), optional `manifest_cache`. When `manifest_cache` is present (the routing gate already ran Pass 1), skip Steps 1-2 and resume at Step 3 with that manifest. Never re-run Pass 1 over a provided `manifest_cache`.

## Step 0 — Input type detection

File path → resolve extension. Pasted text → stdin. Neither → conversation context. Multiple files → run Steps 1-2 per file, merge manifests additively (concatenate entity lists, concatenate hints, union directives), dedup entities by natural key (events by name+date, parties by name, obligations by id).

## Step 1 — Setup check (session-cached)

Load `shared/setup-check.md`. Cache result this session. Missing deps: tutorial mode → pip command; direct mode → one-line message. Second failure → offer pasted-text fallback (md/text needs no third-party libs).

## Step 2 — Pass 1 (deterministic)

**Caller passed `manifest_cache`** → this step is already done by the routing gate; adopt that manifest and go to Step 3. Otherwise run Pass 1 here.

Run orchestrator → returns **manifest**: `extraction_result`, `extraction_hints[]`, `coverage{}`, `matter_type_evidence{}`, `profile_signals{}` (soft profiles privacy/litigation/governance/risk_assessment from raw-text keywords, active `>= 0.34`; never gate Pass 1, only steer Pass 2 directives and selector).

- File: `python scripts/extract_entities.py --input <path> [--pages R] [--sheets A,B]`
- Pasted text: `python scripts/extract_entities.py --stdin` (pipe the text)
- Conversation context: no script. The assistant builds an `ExtractionResult` by inspection and a coverage map (populated vs absent fields) by hand.
- PDF over 50 pages: probe first (`--probe <pdf>`); if large, warn and ask for a page range (genuine-unreadable case, not discretionary interruption). Scanned PDF (manifest entities all empty, no hints): warn "scanned PDF detected," request a paste.
- Privacy/resource defaults: file inputs emit basename-only `input_source`; use `--include-source-path` only for trusted internal provenance. Default caps: 25 MB file, 50 PDF pages, 5000 DOCX paragraphs, 200 DOCX tables, 5000 DOCX table rows, 200 PPTX slides, 5000 PPTX text shapes, 20 XLSX sheets, 1000 XLSX rows/sheet, 50000 XLSX cells/sheet. Override with matching `--max-*` flags only for trusted local inputs.

## Step 3 — Pass 2 (directive-driven enrichment)

Manifest includes deterministic extraction results plus compact `llm_enrichment` evidence for unresolved candidates. `llm_enrichment.directives[]` is the single canonical directive lane; all directive types appear there.

Rules:

- **Read order.** Manifest first, then `llm_enrichment.evidence_packets[]`, then `llm_enrichment.directives[]`. Use snippets referenced by directive `hint_ids` only when needed (`extraction_hints[].snippet` + `context_heading`). No full re-read unless a directive explicitly requires source context. File input → read around `source_ref`/`anchor` only for specific low-confidence candidate.
- **Read policy.** High confidence → no reread. Medium → snippet only. Low → snippet + neighboring block. Contradiction, missing party/date, or incompatible candidate fields may use heading-section window.
- **Directive handlers.** `resolve_candidate` → resolve from evidence packet only; `null_field_classification` → apply risk rubric (`shared/figure-description-schema.md`) per target id; `hint_resolution` → instantiate `suggested_field` (for `freeform_mention` party hints, alias-resolve the mention against an already-promoted party rather than minting a new entity; mint only when it names a genuinely new, source-supported party); `cross_linking` → match obligations↔controls, witnesses↔documents, conditions↔parties; `implicit_inference` → semantic read for `decision_points`, hierarchies, implicit data flows; `directed_inference` → profile-flagged absent field; populate from bounded read of supporting spans only, each entity carrying `evidence_id`+`source_ref`, else add `extraction_warning`; `matter_type_resolution` → pick highest-evidence (tutorial: ask only if tied; direct: never).
- **Patch discipline.** Return JSON Patch operations only; every added or changed entity carries `evidence_id` and `source_ref`; do not restate unchanged entities. For script-built manifests (file or stdin input): write the manifest and the patch to two temp files (operator scratch location), run `python scripts/patch_gate.py --manifest <m.json> --patch <p.json> --apply`, and adopt `enriched_extraction_result` from its JSON output when `ok` is true. On error findings: fix the patch once using the findings' `rule`/`path`/`message` and re-run. On a second failure: drop the failing ops, append an `extraction_warning` naming the dropped fields, apply the surviving ops via the gate, proceed. Conversation-context input (no script manifest): gate does not run; the prose rules above govern.
- **Hierarchy (grouping/nesting).** `extraction_result.hierarchy` carries a deterministic seed from document headings (`source: "deterministic"`). Audit it: drop or relabel nodes that do not match the legal logic; keep depth ≤ 2. Then compose tiers the headings miss (claim → element → evidence, group → subgroup), adding nodes with `source: "llm"` and a `parent` into the tree. Each node: `{id, label, parent, depth, source}`. Patch `hierarchy` like any field; support each composed node from evidence, never invent structure absent from the matter.
- **Anti-hallucination (precision).** Populate only with textual support in supplied evidence/snippet/anchor. No support → leave null + warn. Never invent.
- **Budget.** One pass, no recursion. Stop when directives handled.

## Step 4 — Validation

Check `is_empty()`. Empty, no input text, no hints → halt, request better input. Sparse (fewer than 3 entity arrays populated after Pass 2): `skip_confirmation=true` (direct) → proceed with inline note; tutorial → ask for one-sentence intent description.

## Step 5 — Intent and selection

Build `intent_string` (priority: caller `intent_hint` → matter_type + dominant populated field → "general"). Run `python scripts/diagram_selector.py --extraction-json <enriched JSON>`. Confidence routing: ≥ 0.75 → accept; 0.50-0.74 → state recommendation inline and proceed (no question); < 0.50 → present top 2 and ask (the one allowed interruption in direct mode).

## Step 6 — Pre-confirmation (conditional)

`skip_confirmation=true` → one-line status, proceed. `skip_confirmation=false` (tutorial) → show formatted summary of enriched result, ask "Does this look right?"

## Step 7 — Return to caller

Return enriched `ExtractionResult`, confirmed `diagram_type`, `rationale`, `extraction_warnings[]`, and `coverage` block (so `direct.md` can note absent high-value fields at delivery).
