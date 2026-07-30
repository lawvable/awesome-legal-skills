# Tutorial workflow

First-run walkthrough. Detects setup, runs one worked example end to end with simulated extraction. `check_setup.py` and `render_html.py` called for real; extraction uses hardcoded scenario data so lesson never depends on parser quality.

## Stage 1 — Setup gate

Run procedure in `shared/setup-check.md`. Missing deps → print pip line, halt ("Re-run /legal-diagram tutorial after installing"). Crash → surface stderr, name likely cause, halt. Clean → "Setup complete.", go to Stage 2.

## Stage 2 — Path selection

Present: `[L] Litigation` — contract dispute chronology (timeline); `[C] Corporate` — entity ownership structure (erDiagram). Ask user to type L or C. Invalid → re-prompt once, then default to L (note choice).

## Stage 3 — Run the worked example

Use chosen scenario (below) and walk these steps aloud:

1. **Narrate** the scenario.
2. **Simulated manifest summary** (hardcoded, not from script): matter_type, entity counts, one illustrative directive, one illustrative hint. One line: script produced this TODO list and the assistant now executes it (the two-pass idea).
3. **Simulated plain-language digest** — render scenario's populated fields as a guided-mode digest, exactly as a real user would see it. Use scenario's hardcoded data; format per `workflows/guided.md` § Step 2 rendering table. Scenario L: show Parties & roles, Key events (chronological), Legal obligations. Scenario C: show Entities, Ownership, Relationships. After each section, close with: "Does this look right? Correct a name, add something I missed, or remove anything — then I'll suggest a diagram type." Simulate user responding "looks good" and continue. Step exists so users see what guided-mode digests look like before running one for real.
4. **Simulated type confirmation** — show `diagram_selector.py` recommendation as user would see it: **Recommended:** [plain name] — [one-sentence rationale]. **Alternatives:** [alt1] ([what it shows]) · [alt2] ([what it shows]). Simulate user confirming recommendation and continue.
5. **Print the quirk** for that type (`shared/parser-guards.md`).
6. **Generate** the fenced block from the scenario; apply the guard; validate inline.
7. **Offer HTML export**: "Export as standalone HTML? Y/N (default Y)." On Y: build hardcoded FigureDescription, run `render_html.py`, report path. On failure, note mermaid.live; do not abort.
8. **Recap**, 7 steps: setup checked, document normalised, signals detected, manifest directives executed, digest walked through and confirmed, type chosen, diagram generated.

### Scenario L — Litigation (timeline)

VendorCo v. ClientCorp MSA dispute: Jan 2026 signed, Feb performance begins, Mar defects reported, Apr cure plan, May payment withheld, May breach notice. Summary: 2 parties, 6 events; directive = `risk_level` on breach-notice obligation; hint = process-sequence from cure-plan clause. Selector: `timeline`, "6 events, litigation". Digest shows: Parties & roles (VendorCo — vendor/supplier; ClientCorp — client/customer), Key events (6 dated entries, chronological), Legal obligations (VendorCo to perform per MSA — risk: high). Not found: witnesses, IP assets — flag as absent, note irrelevant to matter type. Diagram slug: `tutorial-litigation-timeline`.

### Scenario C — Corporate (erDiagram)

ParentCo owns 100% OperatingSubA, 80% OperatingSubB; MinorityInvestor owns 20% OperatingSubB; OperatingSubA party to Customer MSA; OperatingSubB borrower under Credit Agreement. Summary: 5 entities, 3 ownership links, 2 relationships; directive = cross-linking; enrichment = cardinality. Selector: `erDiagram`, alt `flowchart TD`. Digest shows: Entities (ParentCo — holding company; OperatingSubA — wholly owned subsidiary; OperatingSubB — majority-owned subsidiary; MinorityInvestor — 20% shareholder; Customer — MSA counterparty; Lender — credit agreement lender), Ownership (3 links with percentages), Relationships (2 contract links). At step 6, normalise names inline ("Operating Sub A" → "OperatingSubA"), log each, add one-paragraph erDiagram-vs-flowchart comparison. Diagram slug: `tutorial-corporate-erdiagram`.

## Exit

Point user to fast path: "Next time, just paste a matter, drop a file path, or name a diagram. No tutorial needed."
