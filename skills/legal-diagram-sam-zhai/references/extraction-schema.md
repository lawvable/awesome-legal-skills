# Extraction schema reference

Load during `extract.md` Pass 2 to resolve hints and know which fields script can populate versus which need LLM enrichment. Field definitions live in `scripts/extraction/schema.py`; this file documents **detection tier** and **signals** per field.

## Contents

- Detection tiers (what the three labels mean)
- Detection-tier summary table
- Field groups
- Special notes

## Detection tiers

- **script-direct**: deterministic layer fully populates field. Accept and verify only.
- **script-hint**: signal fires but script cannot parse structure; emits `ExtractionHint`. Pass 2 resolves hint into entities from snippet.
- **llm-only**: no deterministic signal exists. Manifest always emits a directive; Pass 2 populates from document semantics.

Governing rule: script emits a populated entity only when a pattern fully resolves; otherwise emits a hint. No uncertain entity enters result from script; Pass 2 may populate a field only with textual support in referenced snippet.

## Detection-tier summary

|Field|Tier|Primary signal|Reliable formats|
|---|---|---|---|
|events|script-direct|date regex per sentence|md, docx, xlsx|
|legal_authorities|script-direct|citation regex (case / statute / reg)|all text formats|
|ownership_links|script-direct|`X owns N% of Y`|md, docx|
|parties|script-direct|`Parties:` block or inline `Parties: A (role), B (role)`|md, docx|
|entities|script-direct|corporate-suffix names (Inc/LLC/Corp…), or entity table|docx, xlsx, md|
|tasks, conditions, claim_classes, data_flows, witnesses, ip_assets, negotiation_issues|script-direct **if tabular**, else script-hint|table-header signature, or section heading|docx, xlsx|
|process_steps, investigation_steps|script-direct if numbered list, else script-hint|numbered list + action verb|md, docx, pptx|
|obligations|script-direct|`shall` / `must` / `agrees to` modal|md, docx|
|communications|script-hint|"Notice of" / "demands" + parties|docx, md|
|concepts|script-hint|heading cascade or `(a)(b)(c)` enumeration|docx, md|
|transfers|script-direct|`X pays/wires Y` + amount|md, docx|
|obligations.risk_level|llm-only|language rubric (`shared/figure-description-schema.md`)|n/a|
|decision_points|llm-only|conditional language|n/a|
|relationships.cardinality_*|llm-only|inferred from ownership/role|n/a|

## Field groups

**Temporal** (`events`, `deadlines`, `phases`, `tasks`). Serve categories 4, 5, 13, 14, 24, 26-28. `events` = most format-robust field; recoverable even from PDF. `tasks` and `phases` populate strongly from XLSX deadline tables.

**Parties / entities** (`parties`, `entities`, `ownership_links`, `relationships`). Serve 6, 14, 29. `ownership_links` needs explicit `owns N%` pattern; structures stated only in prose drop to relationship hint. `relationships.cardinality_*` is llm-only.

**Obligations / controls / conditions** (`obligations`, `controls`, `conditions`). Serve 7, 9, 21, 30. `obligations` populate from modal verbs; `risk_level` always llm-only. `controls` and `conditions` populate from tables; otherwise heading hints.

**Process / investigation** (`process_steps`, `investigation_steps`, `decision_points`). Serve 1, 11, 16, 17, 26, 30. Numbered lists populate directly; prose sequences become hints. `decision_points` = llm-only (multi-branch logic).

**Communications** (`communications`). Serve 13, 15, 16. Script-hint: doc-type keyword plus sender/recipient; full message order usually needs Pass 2.

**Concepts / authorities** (`concepts`, `legal_authorities`). Serve 3, 20, 21, 22. `legal_authorities` = strongest script-direct field across all text formats (citation regex). `concepts` hierarchy: script-hint (heading cascade) → llm (implicit prose taxonomy).

**Risk / negotiation** (`risk_items`, `negotiation_issues`). Serve 8, 18, 22. Populate directly from 2-axis table; otherwise hint.

**Financial** (`transfers`, `claim_classes`). Serve 15, 28, 29. `claim_classes` populate from ordered waterfall list or table.

**Privacy / IP** (`data_flows`, `ip_assets`). Serve 10, 25, 30. Both script-direct from tables, script-hint from headings.

**Witnesses** (`witnesses`). Serve 23. Script-direct from witness table, script-hint from narrative mentions.

## Special notes

- `risk_level` and `decision_points` never script-populated; manifest always emits directives for them.
- PDF extraction structurally unreliable; `events[]` and `legal_authorities[]` most recoverable, tables least.
- XLSX strongest for `tasks[]`, `deadlines[]`, and any table-mapped entity; weak for `relationships[]`.
- Conversation-context input has no script tier. The assistant populates everything, using manifest's `absent_fields` list as checklist.
