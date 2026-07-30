# Workflow: DRAFT

Greenfield drafting of a new DPA from the modular templates. Target: produce a complete, signature-ready DPA tailored to the user's processing scenario.

**This workflow assumes the user is starting from a blank page** (or wants to replace a defective DPA entirely). For incorporating counterparty redlines into an existing draft, use `redline.md`.

## Step 1 — Intake checklist

The drafting cannot start until these are nailed down. If any are missing, request from the user before proceeding. Do not invent.

### Mandatory intake

| # | Field | Notes |
|---|---|---|
| I-T | **Tier** | Tier 1 (Commercial) / Tier 2 (Strict, 2021/915 unmodified) / Tier 3 (Hybrid, Sections I+II of 2021/915 + custom Section III). Walk decision tree in `references/tier-selection.md` if user has not pre-selected. Default for OneZero Legal advisory work: Tier 3. |
| I1 | Controller — full legal name, registered seat, registration number, signatory | |
| I2 | Processor — same | |
| I3 | Underlying main agreement — title, date, brief description | The DPA references the main agreement |
| I4 | Subject matter of processing | One paragraph |
| I5 | Duration | Tied to main agreement / fixed term / indefinite |
| I6 | Nature of processing | Operations: collection, storage, hosting, transmission, deletion, etc. |
| I7 | Purpose of processing | Controller's purpose |
| I8 | Categories of personal data | List — flag Art. 9 / Art. 10 separately |
| I9 | Categories of data subjects | List |
| I10 | Special categories or Art. 10 data | Yes/no — if yes, enhanced TOMs needed |
| I11 | International transfers | Yes/no; if yes: importer country, mechanism (SCCs / DPF / adequacy), TIA status |
| I12 | Sub-processors at signing | List with name, location, activity; or "none" |
| I13 | Sub-processor authorisation regime | Specific / general |
| I14 | Perspective | Controller-favorable / processor-favorable / balanced |
| I15 | Language | DE / EN / bilingual |
| I16 | Governing law and venue | |
| I17 | TOMs document | Provided / use template scaffold / refer to processor's standard TOMs document |

### Conditional intake

| # | Field | When |
|---|---|---|
| C1 | Liability cap arrangement | If user wants to deviate from main agreement's cap |
| C2 | Insurance requirement | If applicable |
| C3 | Specific carve-outs the user wants | E.g. analytics, security telemetry |
| C4 | Existing certifications to recognise | ISO 27001, SOC 2, CSA STAR, BSI C5 |

If the user provides "we'll use the processor's standard DPA as a starting point", switch to `redline.md`. The DRAFT workflow is for genuinely greenfield drafting.

## Step 2 — Template selection (tier × language)

The tier choice (intake item I-T) determines which template variant to load. Six DPA template variants exist — three tiers × two languages — plus the bilingual modes for client deliverables. For Joint Controller arrangements, branch instead to `templates/jca-{en,de}.md` and switch workflows.

| Tier | EN | DE |
|---|---|---|
| Tier 1 — Commercial | `templates/dpa-commercial-en.md` | `templates/dpa-commercial-de.md` |
| Tier 2 — Strict (2021/915 unmodified) | `templates/dpa-strict-en.md` | `templates/dpa-strict-de.md` |
| Tier 3 — Hybrid (Sections I+II of 2021/915 + custom Section III) | `templates/dpa-hybrid-en.md` | `templates/dpa-hybrid-de.md` |
| Joint Controller (Art. 26) | `templates/jca-en.md` | `templates/jca-de.md` |

For **Tier 2 and Tier 3**, also load `references/2021-915-commission-text-{en,de}.md` (matching language) — this is the practitioner's clause map; the binding text is the OJ. For **Tier 3**, also load `references/negotiation-fallbacks.md` — the Section III replacement is fully customisable.

**Bilingual format options** (where I15 = bilingual):
- **Side-by-side columns**: each clause has DE in the left column and EN in the right column. Best for client deliverables and signed documents.
- **Sequential**: full DE version followed by full EN version, with clause numbering identical. Best for templates that will be split per execution.

**Default for OneZero Legal client deliverables**: side-by-side, with a recital noting that in case of conflict, the [DE/EN] version shall prevail. Ask user which language prevails.

### Tier-aware quality gates before populating

- **Tier 2 (Strict)**: confirm the user understands that Sections I, II, III of the 2021/915 SCCs are unmodified. The only customisation surface is (a) Section 1.4 choices (Docking, Clause 7.7 Option 1/2, time period), (b) the Annexes (Schedules 1–4), (c) Section 4 commercial overlay. Liability ALT 1 / ALT 2 in Section 4.3 is the only material commercial decision.
- **Tier 3 (Hybrid)**: confirm Sections I and II will not be modified. Section 4 (replacement for Section III) is fully customisable. Walk Section 4 against Section II as a final consistency check before delivery — if Section 4 narrows a Section II obligation, the architecture has been violated and the user should consider Tier 1 instead.
- **Tier 1 (Commercial)**: full latitude on every clause; choose ALT 1 / ALT 2 throughout per perspective using `references/negotiation-fallbacks.md`.

## Step 3 — Populate intake into the template

Walk the template top-to-bottom and replace placeholders:

- `{{CONTROLLER}}`, `{{PROCESSOR}}`, `{{MAIN_AGREEMENT}}`, etc. are filled from intake.
- Annex 1: populate from I4–I9.
- Annex 2: populate from I17 (or use scaffold with explicit "TO BE COMPLETED" markers if processor's TOMs document is not yet available).
- Annex 3: populate from I12 with full sub-processor table.
- Annex 4: populate ONLY if I11 = yes; otherwise omit Annex 4 and remove the corresponding cross-references in the body.

## Step 4 — Apply perspective adjustments

For each negotiated clause, select the position from `references/negotiation-fallbacks.md` matching the user's perspective:

| Topic | Apply T1 of perspective |
|---|---|
| Sub-processor regime | Per perspective |
| Audit rights | Per perspective |
| Breach notification timeline | Per perspective |
| Liability cap | Per perspective |
| Indemnification | Per perspective |
| TOMs change mechanism | Per perspective |
| Deletion / return | Per perspective (note: choice is non-negotiable per Art. 28(3)(g)) |
| Service-improvement carve-out | Per perspective |

For balanced/neutral drafts, use T2 throughout (the typical landing zone).

## Step 5 — Special-category and Art. 10 adjustments

If I10 = yes:
- Annex 2 must include heightened TOMs: enhanced encryption, stricter access controls, mandatory pseudonymisation where feasible, segregated processing environments, enhanced logging and monitoring.
- Body must include explicit statement that processor acknowledges the special-category status and the heightened security requirement.
- Sub-processor flow-down must require sub-processor's TOMs to match the heightened standard.
- Consider mandatory DPIA reference (Art. 35) and processor's assistance obligations.

If I10 covers Art. 10 (criminal records / offences), confirm legal basis (Art. 10 limits processing to authorities or specific Member State law).

## Step 6 — Transfers and SCC integration (if I11 = yes)

If transfers in scope:
1. Identify SCC module from `references/sccs-module-guide.md` Step 2 (Quick Decision Rule).
2. Choose docking architecture:
   - Option A — Standalone SCCs separately executed; DPA references their existence.
   - Option B — SCCs incorporated as Annex 4 of the DPA.
   For OneZero Legal client deliverables, prefer Option A unless the user requests otherwise.
3. Annex 4 (or separate SCCs annex set):
   - Annex I.A (parties) — populate.
   - Annex I.B (description of transfer) — mirror DPA Annex 1.
   - Annex I.C (competent SA) — fill per Clause 13 logic.
   - Annex II (TOMs) — mirror DPA Annex 2.
   - Annex III (sub-processors) — mirror DPA Annex 3 if Module 2/3.
4. TIA: reference an existing TIA document or note the obligation to conduct one.
5. If DPF in play: include fallback to SCCs if certification lapses.

## Step 7 — Quality gate walk-through

Run the SKILL.md "Quality gates" section as a final check:

- [ ] Roles confirmed and JC screen passed.
- [ ] All chapeau elements addressed in Annex 1.
- [ ] All eight (a)–(h) obligations covered in body.
- [ ] Sub-processor mechanism defined.
- [ ] Audit rights specified.
- [ ] Deletion/return choice mechanism preserves controller's choice.
- [ ] Transfers handled (or not in scope).
- [ ] Special categories addressed (if applicable).
- [ ] Liability allocation reflects perspective.
- [ ] Language consistent.

## Step 8 — Drafting notes

Append a separate **Drafting notes** section to the output containing:

1. **Open items** — fields the user needs to complete (e.g. signatory names, exact dates, TOMs document attachment, sub-processor list confirmation).
2. **Alternatives left in** — clauses where the draft includes alternative wordings for the user to choose between (mark these clearly with `[ALT 1]` / `[ALT 2]`).
3. **Assumptions made** — scenario assumptions used in absence of explicit input (e.g. "assumed standard 30-day breach notification window").
4. **Recommended next steps** — sign-off path, internal review (DPO, GC, business sponsor), insurance certificates to obtain, etc.

## Step 9 — Output assembly

The output structure:

```markdown
# Data Processing Agreement / Auftragsverarbeitungsvertrag — Draft v[1]

[Full DPA per template, populated]

---

## Annex 1 — Description of Processing
[Populated]

## Annex 2 — Technical and Organisational Measures
[Populated or scaffold with markers]

## Annex 3 — Sub-processors
[Populated or "None at signing" with notification mechanism]

## Annex 4 — International Transfers (only if applicable)
[SCC integration]

---

# Drafting Notes

## Open items
[List]

## Alternatives in the draft
[List, with cross-reference to clause numbers]

## Assumptions
[List]

## Recommended next steps
[List]

## Practitioner's note
[2–4 sentences summarising what the user should do to take this from draft to executed.]
```

## Quality gates before delivering

- [ ] All intake items reflected in the draft.
- [ ] Bilingual draft (if applicable) has parallel content; clauses do not diverge in substance.
- [ ] No `{{PLACEHOLDER}}` markers remain except where intentional alternatives or open items.
- [ ] Annex 1 is concrete (not "as set out in main agreement").
- [ ] Annex 2 either populated or marked clearly as scaffold-pending-TOMs.
- [ ] Annex 3 populated.
- [ ] Annex 4 present-and-consistent OR absent-and-no-cross-references-orphaned.
- [ ] Drafting notes section is present and lists all open items.

## Anti-pattern guardrails

- **Do not deliver a "draft" with empty annexes labeled "to be filled by the user".** That is not a drafted DPA. Either populate from intake or insist on additional intake.
- **Do not use "DPA" as a section heading in DE drafts.** Use "AV-Vertrag" or "Auftragsverarbeitungsvertrag".
- **Do not insert ™, ®, or marketing names** into clauses; use legal names of parties only.
- **Do not commit to specific timelines (24h, 30 days)** that you have not confirmed with the user. Use bracketed placeholders if the user has not specified.
- **Do not produce a 60-page DPA when the processing is narrow** (e.g. simple newsletter sending). Match the document's complexity to the processing's risk profile.
