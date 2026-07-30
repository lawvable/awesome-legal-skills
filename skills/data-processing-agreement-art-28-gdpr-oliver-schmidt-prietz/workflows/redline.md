# Workflow: REDLINE

The user has received a counterparty's DPA draft (typically a SaaS provider's standard or a corporate counterparty's first draft) and wants a marked-up response with tracked changes and rationale.

This workflow combines REVIEW_NEG analysis with a redline-ready output format. Target turnaround: 3–5 hours, depending on length.

## Step 1 — Scope and intake

- Confirm: this is REDLINE — counterparty has sent a draft, user wants a marked-up response.
- Confirm perspective. **The redlines must serve the user's perspective consistently** — never propose changes that favor the counterparty.
- Negotiation context:
  - Standard SaaS click-through (low negotiating room → focus only on tier-1 issues + side letter)
  - Mid-size vendor (typical pushback expected on tier-2 items)
  - Strategic vendor (full negotiation room → can pursue T1 positions)
  - Internal negotiation (sister entity / group company → cooperate-style redlines)
- Time-pressure context: redlines for a deal closing this week look different from redlines for a 6-month negotiation.
- Load:
  - `references/art28-3-checklist.md`
  - `references/common-defects.md`
  - `references/negotiation-fallbacks.md`
  - `references/sccs-module-guide.md` if transfers in scope
  - The relevant template (`templates/dpa-commercial-{en,de}.md`, `templates/dpa-strict-{en,de}.md`, or `templates/dpa-hybrid-{en,de}.md`) as a benchmark for what the *ideal* DPA from the user's perspective looks like — pick the tier matching the counterparty draft's architecture (use `references/tier-selection.md` to identify it)

## Step 2 — Diagnostic pass

Before redlining, run REVIEW_NEG Steps 3–6 as a diagnostic. This produces:
- Issue table with tiers.
- Annex review.
- Cross-cutting observations.

The diagnostic is internal — not delivered to the user as separate output. It feeds the redline.

## Step 3 — Triage by negotiating room

Apply the negotiating-room context to the issue list:

### High negotiating room (strategic vendor / greenfield)
- Push T1 on all tier-1 and tier-2 items.
- Push T2 on tier-3 items.
- Side letter not required.

### Standard negotiating room (typical commercial)
- Push T1 on tier-1 items, signal willingness to land at T2.
- Push T2 on tier-2 items, signal willingness to land at T2/T3.
- Drop tier-3 items unless trivially correctable (formatting / typo / cross-reference).

### Low negotiating room (click-through, dominant vendor)
- Push tier-1 items as essential changes.
- Group tier-2 items into a side letter for the user's records or address via internal risk acceptance.
- Drop tier-3 items.

## Step 4 — Redline production

For each clause being redlined, produce:

1. **Original clause text** (verbatim from counterparty draft).
2. **Marked-up version** — additions in **bold**, deletions in ~~strikethrough~~. Preserve clause numbering.
3. **Rationale** (1–2 sentences) — why the change is needed, citing Defect ID where applicable.
4. **Fallback markers** (T2 / T3) — separate alternative wordings flagged for the negotiator.

### Marking conventions

- **`**bold**`** for additions.
- **`~~strikethrough~~`** for deletions.
- **`[Comment: ... ]`** for negotiator notes (do not send to counterparty as-is; strip before sharing externally — but useful for internal review).

### When to redline vs. side-letter

**Redline** when:
- Tier-1 issue.
- Defect is in mandatory Art. 28(3) content.
- Issue is structural (cannot be addressed by an additional document).

**Side letter** when:
- Tier-2 issue and counterparty's standard DPA is locked.
- Issue can be addressed via supplemental commitment without re-opening the body.
- The counterparty's signature on the side letter is more politically achievable than a body redline.

**Drop** when:
- Tier-3 issue and negotiating room is low.
- Pursuing it costs more goodwill than the substantive value.

## Step 5 — Side-letter drafting (if used)

If a side letter is the right tool for residual issues:

1. **Title**: "Side Letter to Data Processing Agreement dated [date] between [Controller] and [Processor]" / "Nebenvereinbarung zum Auftragsverarbeitungsvertrag".
2. **Recitals**: brief statement that the Parties have entered into the DPA on [date] and wish to clarify / supplement specific aspects.
3. **Operative clauses**: each addressing one residual issue, with clear cross-reference to the DPA clause it modifies or supplements.
4. **Order of precedence**: in case of conflict between the side letter and the DPA, the side letter prevails.
5. **Signatures**: same signatories as the DPA.

Common side-letter contents:
- Enhanced sub-processor objection rights.
- Faster breach notification timeline.
- Specific TOMs commitments.
- Audit logistics (e.g. controller's preferred third-party auditor named in advance).
- Insurance certificate delivery.
- Specific data retention / deletion timeline.

## Step 6 — Cover memo

The redlined DPA is delivered with a cover memo:

```markdown
# Cover Memo — DPA Redline Response

## To
[Counterparty name and contact]

## From
[User / firm]

## Date
[date]

## Subject
Comments and proposed amendments to the [Controller / Processor] DPA dated [date]

## Summary
[3–5 sentences: overall posture, headline asks, expected discussion points, request for [redlined response / call / signature].]

## Material changes (tier 1)
1. [§ X.X — Issue — Proposed change]
2. ...

## Material changes (tier 2)
1. [§ X.X — Issue — Proposed change]
2. ...

## Polish (tier 3, if any retained)
1. ...

## Side letter
[If used: brief summary of side-letter content. Otherwise: "No side letter required."]

## Process
[Proposed next step: counterparty to redline, call, signature on agreed form, etc.]

## Practitioner's note (internal)
[For internal user only — strip before sending externally. Walk-back conditions: which redlines we will hold to, which we can concede in exchange.]
```

## Step 7 — Output assembly

```markdown
# DPA Redline — [Counterparty] / [Controller]

## Cover memo
[Per Step 6]

---

## Marked-up DPA

[Full counterparty draft with marks applied. Preserve original numbering. Include only clauses that have changes — do not reproduce unchanged clauses unless they provide context.]

### § [X] [Original heading]

**Original**:
[Verbatim original text]

**Proposed**:
[Marked-up version]

**Rationale**: [1-2 sentences]
**Fallback (T2)**: [if different from proposed]
**Walk-back (T3)**: [Only mark for tier-1 items]

---

## Side letter (if used)
[Per Step 5]

---

## Practitioner's note (internal)
[Walk-back map; expected counterparty pushback; sequence for the negotiation.]
```

**Note on output volume**: a redline document should focus on the changed clauses, not reproduce the entire DPA. The cover memo + marked-up sections + side letter is sufficient. The negotiator can apply the marks to the original document directly.

## Quality gates before delivering

- [ ] Roles confirmed.
- [ ] Perspective consistently applied — no clauses redlined in favor of the counterparty.
- [ ] All tier-1 items addressed.
- [ ] Tier-2 / 3 items handled per negotiating-room context.
- [ ] Marks are unambiguous (clear additions, clear deletions, no nested-mark soup).
- [ ] Rationale is short and citation-backed (Defect IDs, Art. 28 references).
- [ ] Side letter (if used) does not duplicate body content.
- [ ] Cover memo is clear about asks and process.
- [ ] Internal practitioner's note not accidentally left in external version.

## Anti-pattern guardrails

- **Do not redline 60 clauses for a click-through SaaS DPA.** The counterparty will not engage. Pick the 5–8 that matter.
- **Do not propose alternative wording without explaining the substantive issue.** The counterparty's lawyer needs to understand why, not just see a marked-up version.
- **Do not use comments in the marked-up version that you would not want the counterparty to read.** Internal commentary goes in the practitioner's note.
- **Do not redline boilerplate** (governing law, notices) unless there is a substantive issue. Boilerplate redlines invite reciprocal boilerplate redlines and slow the negotiation.
- **Do not propose a redline that contradicts another redline.** Read the marked-up version end-to-end before delivering.
