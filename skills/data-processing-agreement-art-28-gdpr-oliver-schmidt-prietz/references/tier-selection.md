# Reference: Tier Selection Logic

This file governs the choice between the three DPA template tiers. It is loaded in `workflows/draft.md` at intake item I-T (tier choice) and in `workflows/redline.md` when the counterparty's draft posture is being analysed.

## The three tiers

| Tier | Foundation | Compliance presumption | Commercial flexibility | Files |
|---|---|---|---|---|
| **Tier 1 — Commercial** | Practitioner-style commercial DPA implementing Art. 28(3) directly from the regulation | None | Maximum | `templates/dpa-commercial-{en,de}.md` |
| **Tier 2 — Strict** | Commission Implementing Decision (EU) 2021/915 incorporated by reference, unmodified, with minimal Section IV overlay | Yes — attaches to unmodified Commission text | Minimum (only Section IV overlay) | `templates/dpa-strict-{en,de}.md` |
| **Tier 3 — Hybrid** | Sections I+II of 2021/915 incorporated by reference, custom commercial Section III replacement | Partial — attaches to Sections I+II (where Art. 28(3) substance lives) | Substantial (full Section III replacement under Clause 2(b) SCCs) | `templates/dpa-hybrid-{en,de}.md` |

## Decision tree

Walk these questions in order. Stop at the first definitive answer.

### Q1 — Is the counterparty driving the format?

- **"Use 2021/915 verbatim"** → Tier 2 (Strict).
- **"Use 2021/915 but we need our commercial terms"** → Tier 3 (Hybrid).
- **"Use our standard DPA"** → exit this tree; switch to REDLINE workflow against the counterparty's draft.
- **No counterparty preference** → continue to Q2.

### Q2 — Does the controller need a regulator-defensible safe harbor?

Triggers:
- Public-sector engagement (controller is a public authority subject to enhanced scrutiny).
- Highly regulated sector: financial services, health, critical infrastructure, telecom, public-interest media.
- Post-incident remediation where the paper trail showing safe-harbor instrument is part of the corrective response.
- Anticipated supervisory authority engagement (audit, complaint, prior consultation).
- Internal audit / SOX / DORA / NIS2 controls require demonstrable best-practice contracting.

If yes → continue to Q3 (which flavor of safe harbor?).
If no → continue to Q4.

### Q3 — Strict or Hybrid for safe-harbor scenarios?

- Counterparty is a small/standard processor; Section III mechanics are simple → **Tier 2 (Strict)**.
- Counterparty is a strategic vendor; multi-year relationship; sophisticated commercial terms needed (super-cap, indemnity, insurance covenants, transition assistance) → **Tier 3 (Hybrid)**.
- Public sector engagement where the procurement template imposes specific commercial terms → **Tier 3 (Hybrid)** (use the procurement terms in Section III replacement).
- High-stakes processing with complex liability allocation → **Tier 3 (Hybrid)**.

### Q4 — Is the relationship purely commercial?

- Negotiated B2B SaaS / vendor relationship with no special regulatory exposure → **Tier 1 (Commercial)** is usually right.
- Group-internal arrangement (intra-group processor, sister-entity engagement) → **Tier 1 (Commercial)** is usually right.
- BUT: if the controller side is a regulated entity even in a routine commercial arrangement, escalate to **Tier 3 (Hybrid)** for documentation hygiene.

### Q5 — Defaults when unclear

- For OneZero Legal advisory work, when the client has not specified and the engagement is mid-market commercial: **Tier 3 (Hybrid)** is the safest default — it gives Section II safe-harbor benefit without sacrificing commercial flexibility.
- For pure speed/transaction work where the client wants something signed today: **Tier 1 (Commercial)**.
- Never default to Tier 2 (Strict) without affirmative reason — it is the least flexible tier and only earns its place when safe-harbor posture is the paramount requirement.

## What changes between tiers

| Element | Tier 1 (Commercial) | Tier 2 (Strict) | Tier 3 (Hybrid) |
|---|---|---|---|
| **Art. 28(3) substance** | Drafted in body | Sections I+II of 2021/915 (incorporated, unmodified) | Sections I+II of 2021/915 (incorporated, unmodified) |
| **Audit right (28(3)(h))** | Negotiable wording with T1/T2/T3 ladder | Clause 7.6 SCCs — fixed | Clause 7.6 SCCs — fixed |
| **Sub-processor regime (28(3)(d))** | Negotiable wording (general/specific) with T1/T2/T3 ladder | Clause 7.7 SCCs Option 1 or 2 | Clause 7.7 SCCs Option 1 or 2 |
| **Service-improvement carve-out** | Available as ALT 2 | Not available (would contradict Clause 7.2) | Not available (would contradict Clause 7.2) |
| **Term & termination mechanics** | Negotiable — Section 4 of commercial template | Section IV overlay (minimal) | Section 4 fully customised (replaces Section III SCCs) |
| **Liability cap / indemnity / insurance** | Negotiable (full ALT 1 / ALT 2) | Section IV overlay (default super-cap structure) | Section 4 fully customised |
| **Annexes** | Annex 1 (processing), Annex 2 (TOMs), Annex 3 (sub-processors), Annex 4 (transfers) | SCC Annexes I, II, III, IV completed as Schedules 1–4 | SCC Annexes I, II, III, IV completed as Schedules 1–4 |
| **Hierarchy clause vs main agreement** | Order-of-precedence in body | Clause 4 SCCs (SCCs prevail) | Clause 4 SCCs (SCCs prevail for Sections I–II) |
| **Compliance presumption** | None | Yes — full | Partial — for Sections I+II |
| **Risk if main agreement conflicts** | Order-of-precedence resolves | Clause 4 silently disables conflicts | Clause 4 silently disables Section II conflicts |

## Common misuses to avoid

1. **Picking Tier 2 to "look professional" when commercial flexibility is needed.** Tier 2's compliance presumption is real, but its inflexibility is also real. If the client will end up wanting to modify Section II, Tier 3 is the right tool.

2. **Picking Tier 1 because "we always do it that way" when the client is a regulated entity.** Tier 1 has zero safe-harbor benefit. For regulated engagements, even if commercially routine, Tier 3 is the more defensible choice.

3. **Treating Tier 3 as Tier 2 + free customisation.** Tier 3's customisation is bounded by Clause 2(b) SCCs — Section 4 must not contradict Sections I or II. Practitioners must walk Section 4 against Section II as a final check.

4. **Adding 2021/915 references to a Tier 1 template.** This creates legal incoherence — Tier 1 is drafted under direct Art. 28 reasoning; bolting on 2021/915 references muddles the architecture. If the client wants safe-harbor benefit, switch tier; do not graft.

5. **Using Tier 2 for international transfer scenarios alone.** 2021/915 does not cover Chapter V transfers (Clause 1(f)). The transfer mechanism (typically 2021/914 SCCs) is a separate instrument regardless of which Art. 28 tier is used.

## How this file is loaded

- `workflows/draft.md` — at intake item I-T (tier choice), this file is loaded if the user has not pre-selected a tier.
- `workflows/redline.md` — when analysing a counterparty's draft, this file informs whether to mirror the counterparty's framework (Tier 1/2/3) or counter-propose a different tier.
- `workflows/review-negotiation.md` — informs the issue table where a counterparty's draft sits architecturally (e.g. "this is a Tier 1-style draft purporting to handle 2021/915 territory").
