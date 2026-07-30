# Workflow: REVIEW_QUICK

A fast, sign/no-sign-grade compliance review benchmarked against Art. 28(3)(a)–(h). Target turnaround: 30–45 minutes.

**This workflow is for the question "is this DPA compliant enough for me to sign?"** — not for negotiation strategy. If the user wants to know what to push back on or how to redline, use `review-negotiation.md` instead.

## Step 1 — Confirm scope and load reference

- Confirm with user: this is a quick review for sign/no-sign decision (not a deep negotiation).
- Confirm perspective (controller / processor).
- Load `references/art28-3-checklist.md` (mandatory).
- If the source mentions transfers, SCCs, third country, Drittland: also load `references/sccs-module-guide.md`.

## Step 2 — Roles screen (≤ 5 minutes)

Apply the screen test from `references/art26-joint-controller.md`. If 3+ "joint control" indicators, **stop the review** — surface the misclassification finding and recommend switching to `joint-controller.md`. A quick "compliance" review of a misclassified document is a category error.

## Step 3 — Walk the chapeau (C1–C7)

Locate Annex 1 (or the equivalent description). For each chapeau element, mark:

| Code | Element | Verdict |
|---|---|---|
| C1 | Subject matter |  |
| C2 | Duration |  |
| C3 | Nature |  |
| C4 | Purpose |  |
| C5 | Type of personal data |  |
| C6 | Categories of data subjects |  |
| C7 | Controller's rights and obligations |  |

Verdict = `PASS` / `WEAK` / `GAP` / `DEFECT`.

If Annex 1 is "Services as set out in the Master Agreement" (defect D1.1), mark C3, C4, C5, C6 all as `DEFECT` immediately and continue.

## Step 4 — Walk (a)–(h)

For each obligation, locate the relevant clause(s) in the body and mark:

| Code | Obligation | Verdict |
|---|---|---|
| (a) | Documented instructions only |  |
| (b) | Confidentiality of authorised persons |  |
| (c) | Security (Art. 32) + Annex 2 |  |
| (d) | Sub-processors (regime + Annex 3) |  |
| (e) | Data subject rights assistance |  |
| (f) | Breach / DPIA / consultation assistance |  |
| (g) | Deletion / return at end |  |
| (h) | Audits and inspections |  |

Speed test (per item, ≤ 3 minutes):
- Find the clause.
- Compare to the canonical phrasing in `references/art28-3-checklist.md`.
- Mark verdict.
- Note the *one* most material issue if `WEAK` / `GAP` / `DEFECT`.

## Step 5 — Cross-cutting checks

- **Sub-processor list (Annex 3)**: empty, populated, or "none at signing"? If empty but processor known to use sub-processors, mark `DEFECT`.
- **TOMs (Annex 2)**: present and concrete (`PASS`); present but generic / "industry standard" (`WEAK`); absent (`DEFECT`).
- **Transfers**:
  - Are transfers in scope?
  - If yes, mechanism identified (SCCs / DPF / adequacy)?
  - If SCCs: correct module? Annexes I.A/I.B/I.C/II/III filled?
  - If DPF: certification status (caveat: can lapse, fallback advised)?
  - TIA referenced (mandatory for SCCs)?

## Step 6 — Headline issues

From all `GAP` and `DEFECT` markings, identify the **top 3** by impact. These are the issues that drive the recommendation.

## Step 7 — Recommendation

Based on the verdict pattern:

| Pattern | Recommendation |
|---|---|
| All chapeau and (a)–(h) `PASS`; transfers handled; no special-category processing | **Sign** |
| Mostly `PASS` with 1–2 `WEAK` items; no `DEFECT` | **Sign with documented residual risks** (advise user to record acceptances internally) |
| 1+ `WEAK` items + 1 `GAP` item that is non-blocking | **Sign with side letter** (side letter addresses the `GAP`) |
| Any `DEFECT` in chapeau OR in (a), (c), (d) sub-processor regime, or (g) controller's choice | **Do not sign without changes** |
| 3+ items at `WEAK` or worse in critical areas, OR transfers with no mechanism, OR Annex 2 empty | **Escalate to REVIEW_NEG** |

## Step 8 — Output assembly

Produce the output in this exact structure (no deviations):

```markdown
# DPA Quick Review — [Counterparty Name]

## Executive summary
[3–5 sentences. State overall posture (compliant / has gaps / defective). State headline issues. State recommendation.]

## Scope
- Roles: [Controller / Processor — confirm]
- Perspective: [Controller-side / Processor-side]
- Date of source document: [date]
- Transfers in scope: [yes / no]
- Special categories / Art. 10 data: [yes / no]

## Chapeau (Annex 1 / processing description)

| Code | Element | Verdict | Evidence (clause ref + verbatim quote or "missing") | Note |
|---|---|---|---|---|
| C1 | Subject matter | | | |
| ... | | | | |

## Art. 28(3)(a)–(h) coverage

| Code | Obligation | Verdict | Evidence (clause ref + verbatim quote or "missing") | Note |
|---|---|---|---|---|
| (a) | Documented instructions | | | |
| ... | | | | |

## SCC / transfer adequacy
[Skip if no transfers. Otherwise: module, annexes, TIA, fallback.]

## Top 3 issues to fix

1. [Issue 1] — [tier; what it means]
2. [Issue 2] — [tier; what it means]
3. [Issue 3] — [tier; what it means]

## Recommendation
[One of: Sign / Sign with documented residual risks / Sign with side letter / Do not sign without changes / Escalate to REVIEW_NEG]

## Practitioner's note
[For client deliverables: 2–4 sentences on what the user should do next concretely. For internal use: 1 sentence.]
```

## Quality gates before delivering

- [ ] Roles confirmed at the top.
- [ ] All chapeau elements addressed (no skipped rows).
- [ ] All (a)–(h) addressed (no skipped rows).
- [ ] If transfers: SCC adequacy section present.
- [ ] Top 3 issues are actually the highest-impact items (not the easiest to find).
- [ ] Recommendation matches the verdict pattern (do not say "sign" if any `DEFECT` is present in critical areas).
- [ ] Practitioner's note ends the document.

## Time budget guardrail

If the review crosses 60 minutes, stop and ask the user if they want to escalate to `REVIEW_NEG`. A quick review that takes 90 minutes is mis-scoped.
