# Pass 2 eval workflow

Operator procedure for evaluating Pass 2 enrichment quality. Measures the LLM patch against user-owned expected-patch labels; raw counts, no thresholds. One run per frozen fixture; grading aggregates across all nine.

## Purpose

Assess Pass 2 patch quality by executing the enrichment procedure on frozen manifests and grading the output patches against label expectations (required, bonus, forbidden). Returns per-fixture scores and summary table; drives iteration on directives and evidence packaging. Not a test harness (tests live in `scripts/tests/`), but a structured eval run for operator review.

## Eval run procedure

For each fixture in `scripts/tests/eval/manifests/`:

1. **Read the manifest.** Load `scripts/tests/eval/manifests/<fixture>.frozen.json`. Note the `llm_enrichment.directives[]` array and `llm_enrichment.evidence_packets[]` list (manifest is the frozen canonical; never re-run Pass 1).

2. **Execute Pass 2 exactly per workflows/extract.md Step 3.** Follow the read order, directive handlers, and patch discipline as if the manifest came from a script run:
   - Read manifest first, then `llm_enrichment.evidence_packets[]`, then `llm_enrichment.directives[]`.
   - Use snippets referenced by directive `hint_ids` only when needed (from `extraction_hints[].snippet` + `context_heading`).
   - Apply patch discipline: return RFC 6902 JSON Patch operations only. Every added or changed entity carries `evidence_id` and `source_ref`.
   - Do NOT apply enrichment to any real output; the patch is the artifact under test. Write the patch to a temp file for grading.

3. **Run the grader.** Execute `python scripts/eval_pass2.py --manifest scripts/tests/eval/manifests/<fixture>.frozen.json --patch <patch.json> --labels scripts/tests/eval/labels/<fixture>.pass2-labels.json`. Capture the JSON output. Exit 0 = graded; exit 1 = patch gate blocked the patch (`ok: false`, see `gate_findings[]`); exit 2 = malformed input.

4. **Collect per-fixture results.** Record: `ok` status (true/false), `gate_findings[]` (findings from patch gate), `labelled` (whether labels are complete), `vacuous` (true if labels carry `labelled: false`), `score` object (required_pass/required_total/bonus_pass/bonus_total/forbidden_violations).

5. **Build summary table** after all nine fixtures. Columns: fixture | gate status | required_pass/required_total | bonus_pass/bonus_total | forbidden violations | vacuous.

## Label file format

User-owned ground truth for Pass 2 expectations. Schema version: `legal-diagram-pass2-labels-v1`.

Top-level structure:

```json
{
  "schema_version": "legal-diagram-pass2-labels-v1",
  "fixture": "<fixture-name>",
  "frozen_manifest_sha256": "<hex-digest>",
  "labelled": false,
  "expectations": [],
  "forbidden": [],
  "todo": []
}
```

Field meanings:
- `schema_version`: Fixed to `legal-diagram-pass2-labels-v1`.
- `fixture`: Fixture identifier (e.g., `en_spa_contract`). Must match frozen manifest filename.
- `frozen_manifest_sha256`: SHA-256 hex digest of the frozen manifest bytes. Grader emits `labels_stale` warn on mismatch; triggers refreeze (see Refreeze procedure).
- `labelled`: Boolean. True = operator has reviewed all expectations and forbidden rules for this fixture. False = incomplete; grader emits `vacuous: true` in output, indicating scores are placeholder.
- `expectations`: Array of expected-patch entries (see Expectation entry schema below).
- `forbidden`: Array of forbidden-entity rules (see Forbidden entry schema below).
- `todo`: Optional array of operator hints for the next label session (if `labelled: false`). Not used by grader; for operator reference only.
- `_sha_audit`: Security-audit suppression note carried on the sha line (the hex digest false-positives the base64 scanner). Grader ignores it; keep it on the same physical line as `frozen_manifest_sha256` when refreezing.

### Expectation entry schema

Operator specifies an outcome the patch should deliver:

```json
{
  "id": "E1",
  "credit": "required",
  "kind": "field_filled",
  "path": "/parties/0/name",
  "predicate": {},
  "note": "party name must be present"
}
```

Field meanings:
- `id`: Unique identifier (e.g., `E1`, `E2`, ...). Operator-assigned; no constraints on format, but unique within fixture.
- `credit`: `required` or `bonus`. Required = must pass for overall accept; bonus = credit towards higher quality. Grader sums separately.
- `kind`: One of `field_filled`, `value_matches`, `entity_added`, `unchanged`. Determines predicate shape:
  - `field_filled`: Checks that a path is populated (not null, not empty string/list/dict). Predicate `{}` (ignored).
  - `value_matches`: Checks that the value at path matches a constraint. Predicate carries exactly one of: `equals` (deep equality), `one_of` (value in list), `regex` (full-match on string value). Example: `{"equals": "Active"}` or `{"one_of": ["Active", "Inactive"]}` or `{"regex": "[0-9]{4}"}`.
  - `entity_added`: Checks that a new entity appears in an array post-patch. Predicate shape: `{"array": "obligations", "match": {"field": "value", ...}}`. `array` is the entity array name within `extraction_result` (e.g. `obligations`, `parties`), not a pointer. The match dict specifies fields the new entity must carry; all match fields exact. Entity must be net-new vs frozen; if it carries an `evidence_id`, the id must resolve to a known packet or hint (the patch gate already requires `evidence_id` on whole-entity adds, so gate-passed patches always carry one). `path` is unused for this kind; set it to `""`.
  - `unchanged`: Checks that the value at path deep-equals the frozen manifest's value at the same path. Predicate `{}` (ignored).
- `path`: JSON Pointer into the enriched `extraction_result`, not the manifest root (RFC 6901, with `/` escaped as `~1` and `~` escaped as `~0`). Example: `/parties/0/name` or `/hierarchy/0`.
- `predicate`: Constraint object shape depends on `kind`:
  - `field_filled`: `{}`.
  - `value_matches`: exactly one key (`equals`, `one_of`, `regex`). No nesting.
  - `entity_added`: `{"array": "<entity array name>", "match": {<field-match>}}`.
  - `unchanged`: `{}`.
- `note`: Operator commentary; grader ignores (for operator reference).

### Forbidden entry schema

Operator specifies entities or paths that must not change:

```json
{
  "id": "F1",
  "kind": "no_entity_added",
  "array": "parties",
  "match": {"name": "Acme Corp"},
  "note": "hallucination trap: Acme not mentioned"
}
```

Field meanings:
- `id`: Unique identifier (e.g., `F1`, `F2`, ...).
- `kind`: One of `no_entity_added` or `path_untouched`.
  - `no_entity_added`: Checks that no new entity matching a profile appears in the array. Uses the top-level `array` and `match` fields. Entity violates if it is net-new post-patch (beyond those in the frozen manifest) and all match fields are exact.
  - `path_untouched`: Checks that a path value is unchanged (deep equality vs frozen). Triggers violation if the value is changed or the path is removed. Adding a previously absent path does not fire this rule; guard paths that exist in the frozen manifest. Uses the top-level `path` field.
- `array` (for `no_entity_added`): entity array name within `extraction_result` (e.g. `parties`, `obligations`), not a pointer.
- `match` (for `no_entity_added`): Field constraints; entity violates if all match fields are present and exact.
- `path` (for `path_untouched`): JSON Pointer into `extraction_result` to the guarded value.
- `note`: Operator commentary.

## Label session procedure

Operator fills expectations and forbidden per fixture:

1. **Open the label file** for one fixture (e.g., `en_spa_contract.pass2-labels.json`). Start with `labelled: false`.

2. **Read the frozen manifest.** Understand the extraction baseline (parties, events, obligations, etc. from Pass 1).

3. **Read the directives.** Review `llm_enrichment.directives[]` to see what Pass 2 enrichment is intended.

4. **Execute Pass 2 (as an operator, by hand, using the procedure in Eval run procedure Step 2).** Decide what patches you would make.

5. **Populate `expectations[]`.** For each outcome you expect:
   - Assign a unique `id`.
   - Choose `credit` tier (required for must-have, bonus for nice-to-have).
   - Specify the `kind` and `path`.
   - Write the `predicate` (omit for `field_filled` and `unchanged`; provide match for `value_matches` and `entity_added`).
   - Add a `note` (why this matters).

6. **Populate `forbidden[]`.** For each hallucination trap or invariant:
   - Assign a unique `id`.
   - Choose `kind` (`no_entity_added` or `path_untouched`).
   - Provide `array`/`match` (for `no_entity_added`) or `path` (for `path_untouched`).
   - Add a `note`.

7. **Special case: en_spa_contract "todo" stubs.** Read the `todo` array (hints H4 and H14). If present, label session addresses them first: review the evidence for those hints, decide the expected outcome, and move those entries from `todo` into `expectations[]` with appropriate predicates.

8. **Label validation.** Ensure:
   - All `expectations[].id` are unique within the fixture.
   - All `forbidden[].id` are unique within the fixture.
   - Every `path` is syntactically valid JSON Pointer (starts with `/`, escapes `~` and `/`).
   - Predicates match the declared `kind`.
   - Remove `todo` array before setting `labelled: true`.

9. **Set `labelled: true`.** Never set `labelled: true` until:
   - All expectations and forbidden rules have been reviewed for validity in the current manifest.
   - Operator has confirmed that the labels capture the intended enrichment outcomes.

10. **Save and commit.** Label values are operator-owned ground truth. Agents may only transcribe what the operator dictates in the label session; no agent authoring of label content.

## Refreeze procedure

When Pass 1 evolves and the frozen manifests regenerate:

1. **Detect staleness.** Run grader; if any fixture emits `labels_stale` warn, the manifest has changed.

2. **Copy new golden over frozen.** Replace `scripts/tests/eval/manifests/<fixture>.frozen.json` with the new golden manifest.

3. **Update frozen SHA.** Compute SHA-256 of the new manifest bytes. Update `frozen_manifest_sha256` in the fixture's label file to match.

4. **Review expectation validity.** In a new label session, review every expectation and forbidden entry. Check:
   - Does the path still exist in the new manifest (JSON Pointer matches)?
   - Do the entity array paths and field names still match?
   - Are the predicates still meaningful (e.g., `value_matches` regex still applicable)?

5. **Keep labelled: true only after review.** If any entry is invalid, fix or remove it. Only after validation set `labelled: true`.

6. **Document refreeze.** Add a note in the fixture's label file or operator log: date, reason (e.g., "Pass 1 enrichment_hints schema update"), changes made.
