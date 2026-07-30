# Workflow: REVIEW_NEG

A clause-by-clause negotiation-grade review. Target turnaround: 2–4 hours of analytical work, depending on length.

**This workflow is for the question "what should we negotiate?"** — produce a redline-ready issue list with risk tiers, fallback positions, and walk-away conditions. If the user only needs sign/no-sign guidance, use `review-quick.md`.

## Step 1 — Scope, perspective, references

- Confirm: REVIEW_NEG, not REVIEW_QUICK.
- Confirm perspective explicitly. The negotiation positions in the output depend on this. If user is unsure, ASK — do not default.
- Confirm the negotiation context: greenfield negotiation / response to counterparty draft / annual review of existing DPA.
- Load:
  - `references/art28-3-checklist.md` (always)
  - `references/common-defects.md` (mandatory for this mode)
  - `references/negotiation-fallbacks.md` (mandatory for this mode)
  - `references/sccs-module-guide.md` (if transfers in scope)
  - `references/art26-joint-controller.md` if any role ambiguity

## Step 2 — Roles screen

Same as REVIEW_QUICK Step 2. If JC indicators trigger, halt and switch modes.

## Step 3 — Read once for understanding

Before scoring, read the entire DPA once for structure and intent. Note:
- How is it structured (single body vs. body + annexes)?
- Where are the "soft spots" — vague language, unusual carve-outs, asymmetric burdens?
- What is the tone — controller-favorable / processor-favorable / mutual?
- Are there inconsistencies between sections?
- Is there an order-of-precedence clause vs. the main agreement?

This pass shapes the negotiation framing — without it, the clause-by-clause scoring lacks context.

## Step 4 — Clause-by-clause scoring

For each clause in the DPA, produce a row in the issue table. Use the structure:

| # | Clause ref | Topic | Verbatim quote | Issue | Defect ID | Tier | Proposed fix | Fallback (T2) | Walk-back (T3) |
|---|---|---|---|---|---|---|---|---|---|

Where:

- **Clause ref**: section number from the source document (e.g. "§ 4.2" or "Section 5.3(b)").
- **Topic**: which Art. 28(3) element or cross-cutting topic.
- **Verbatim quote**: the actual wording from the source — pulled out, not paraphrased. For long clauses, quote the operative phrase plus enough context for the issue to be self-evident. Paraphrase loses precision and the reader cannot evaluate the issue without the original text. If the clause is too long to quote in full in the table, quote the operative fragment in the table and reference the full clause in a footnote.
- **Issue**: what is wrong (gap, weakness, asymmetry, conflict).
- **Defect ID**: cross-reference to `common-defects.md` (e.g. D5.1) where applicable.
- **Tier**: 1 = blocker (do not sign without changing); 2 = material (negotiate); 3 = polish (acceptable but should fix).
- **Proposed fix**: T1 from `negotiation-fallbacks.md` for user's perspective.
- **Fallback (T2)**: realistic landing zone.
- **Walk-back (T3)**: minimum acceptable; below this, do not sign.

**Order of analysis** (for time efficiency):
1. Chapeau / Annex 1 first — if defective, marks subsequent clauses as inheriting issues.
2. (a)–(h) in order.
3. Cross-cutting (Art. 28(2), Art. 28(4), Art. 28(9), Art. 28(10)).
4. Annexes (1, 2, 3, 4) in order.
5. Liability and indemnity (always significant for the user).
6. Term, termination, survival.
7. Boilerplate (governing law, dispute resolution, notices) — usually tier 3.

## Step 5 — Annex deep-dive

Annexes carry a disproportionate share of substance. For each:

### Annex 1 (processing description)
- Are all chapeau elements present?
- Is the description specific enough for a reader to understand the actual processing?
- Are sensitive data flagged with safeguards?
- If Annex 1 is generic, this taints the entire DPA — escalate to tier 1.

### Annex 2 (TOMs)
- Mapped to Art. 32(1)(a)–(d)?
- Concrete and measurable, or aspirational?
- Encryption: at rest, in transit, both?
- Access controls: how granular?
- Logging and monitoring: what events captured, retention period?
- Pseudonymisation strategy?
- Sub-processor TOMs flow-down covered?
- Update mechanism?

### Annex 3 (sub-processors)
- Current list complete?
- Identifying information sufficient (legal name, location, processing activity)?
- Cross-reference to processor's public sub-processor list (often a website page)?
- Notification mechanism specified?

### Annex 4 (transfers / SCCs)
- Module identified correctly?
- Annexes I.A / I.B / I.C / II / III populated?
- TIA referenced or attached?
- Fallback if DPF certification lapses?
- Sub-processor SCC chain addressed (Module 3)?

## Step 6 — Cross-document verification (contradiction check)

A contradiction-check is a different cognitive task from clause-scoring and benefits from being run as its own pass. Walk these axes explicitly:

### 6.1 — DPA vs Main Agreement
- Order-of-precedence clause present? If not, look for substantive conflicts.
- Common conflicts: main agreement permits "use of Customer Data for analytics" while DPA mandates instruction-only processing; main agreement liability cap incompatible with DPA liability allocation; main agreement term mismatched with DPA survival.
- A conflicting main agreement clause typically wins in litigation unless the DPA explicitly governs.

### 6.2 — DPA body vs Annexes
- Does § 6 (sub-processors) reference Annex 3, and is Annex 3 actually populated?
- Does § 5 (TOMs) reference Annex 2, and is Annex 2 concrete and Art.-32-mapped?
- Annex 1 (processing description): is the duration / data category / data subjects description in Annex 1 consistent with the body's recitals and the actual scope of the Services?
- Defined terms: is every defined term used in the body actually defined? Is the definition consistent across body and annexes?

### 6.3 — DPA vs SCCs (where in scope)
- Does Annex 3 of DPA list the same sub-processors as Annex III of SCCs?
- Do Annex 1 of DPA and Annex I.B of SCCs describe the same processing?
- Do Annex 2 of DPA and Annex II of SCCs describe the same TOMs?
- Module choice consistent with the actual roles?
- Order-of-precedence between DPA and SCCs (SCCs should prevail per Clause 5).

### 6.4 — Internal consistency within each annex
- Annex 2 (TOMs): are measures referenced in narrative also reflected in the structured list? E.g., "encryption at rest" mentioned in body but absent from TOMs schedule.
- Annex 3 (sub-processors): does the list match the processor's public sub-processor page or its DPA recitals?

Flag every contradiction with a clear citation to both locations. Inconsistencies are tier-2 by default and tier-1 if they create operational impossibility (e.g., DPA references Annex 4 but Annex 4 is missing).

## Step 7 — Cross-cutting strategic analysis

Beyond clause-by-clause, assess:

- **Risk allocation**: does liability flow track responsibility flow? Common asymmetry: processor controls security (creates breach risk) but liability cap is paltry; controller bears the regulatory exposure. Flag this as a structural issue, not just a clause issue.
- **Operational frictions**: are the processor's notification / response timelines workable for the controller's actual internal processes?
- **Audit feasibility**: would the controller actually be able to use the audit right as drafted, or is it nominal only?
- **Termination realism**: if the controller wanted to leave, could it actually exit cleanly?
- **Conflict-of-laws**: are the governing law and venue choice workable?
- **Currently irrelevant clauses**: future-proofing for transfers, AI Act, NIS2, sectoral overlays — flag if user might need them within 12 months.

## Step 8 — Negotiation strategy

Group the issues into a sequenced strategy:

### Must-have (will not sign without)
- All tier-1 items.
- Any tier-2 item that the user has decided is non-negotiable for this engagement.

### Should-have (open with, expect to land at T2)
- Tier-2 items where T2 is realistic.

### Nice-to-have (raise but don't fight)
- Tier-3 items.

### Consider trading
- Items where the user can concede in exchange for must-have wins.

### Walk-away conditions
- Specific clauses where T3 is the floor; if the counterparty does not accept T3, the deal is off.
- This is typically: TIA / SCC adequacy on transfers; sub-processor objection right; controller's choice on deletion/return; minimum audit right; minimum breach notification timeline.

## Step 9 — Output assembly

```markdown
# DPA Negotiation Review — [Counterparty Name]

## Executive summary
[5–8 sentences: overall posture, headline issues, recommended approach, walk-away conditions if any are likely to bind.]

## Scope and posture
- Roles: [Controller / Processor — confirm]
- Perspective: [explicit]
- Counterparty draft posture: [controller-favorable / processor-favorable / mutual / aggressive / standard SaaS]
- Negotiating room: [greenfield / standard click-through / large-account customisable]
- Transfers: [yes / no, mechanism]
- Special categories: [yes / no]

## Issue table

[Full table per Step 4 — sorted by tier (1 → 3), then by clause number within tier. Verbatim quotes in the "Verbatim quote" column, not paraphrases.]

## Annex review

### Annex 1 (processing description)
[Findings]

### Annex 2 (TOMs)
[Findings]

### Annex 3 (sub-processors)
[Findings]

### Annex 4 (transfers / SCCs)
[Findings, or: "Not applicable — no transfers in scope."]

## Synthesis

### Liability and structural risk
[Risk allocation observations: does liability flow track responsibility flow? Operational frictions, audit feasibility, termination realism. Issues that are not single-clause defects but structural asymmetries.]

### Cross-document inconsistencies
[Findings from Step 6 — DPA vs Main Agreement, DPA body vs Annexes, DPA vs SCCs, internal annex consistency. Cite both locations for each contradiction.]

### Negotiation weaknesses
[Where the counterparty has structurally undermined controller oversight: poor sub-processor objection mechanism, audit right reduced to nominal, breach notification timeline that gives controller no working window, etc. These are the issues that will hurt the controller in operations even if no single clause is technically defective.]

## Negotiation strategy

### Must-have
- [list]

### Should-have
- [list]

### Nice-to-have
- [list]

### Consider trading
- [list]

### Walk-away conditions
- [list]

## Practitioner's note
[3–5 sentences on what the user should do next: open with this redline; sequence the negotiation; engage [DPO / GC / business sponsor] for [specific items]; consider [side letter / escalation / alternative vendor].]
```

## Quality gates before delivering

- [ ] Roles confirmed; JC screen run.
- [ ] All clauses scored — none silently skipped.
- [ ] All annexes reviewed in their own subsections.
- [ ] Risk tiers assigned consistently with the user's perspective (don't tag tier-1 items that are favorable to the user).
- [ ] Each tier-1 item has both a proposed fix AND a walk-back position.
- [ ] Negotiation strategy is sequenced realistically — must-haves are achievable, not maximalist.
- [ ] Practitioner's note ends the document with concrete next steps.

## Anti-pattern guardrails

- **Do not produce 40 redline candidates if 8 are tier-1 and 32 are tier-3.** The negotiator will lose focus and the deal will degrade. Highlight the 8 and append the rest as "polish for round 2".
- **Do not cite Art. 28 letter-by-letter mechanically.** A negotiation review needs commercial judgement; pure compliance scoring is what REVIEW_QUICK does.
- **Do not write "the Processor should also consider" recommendations** if the user is the controller. Stay in perspective.
