---
name: "dpa-art-28-oliver-schmidt-prietz"
description: "Review, draft, or redline a Data Processing Agreement (DPA / Auftragsverarbeitungsvertrag / AVV) under Art. 28 GDPR, or prepare a Joint Controller Arrangement under Art. 26 GDPR. Supports bilingual output (DE/EN), both controller- and processor-side perspectives, and two review depths — quick (Art. 28(3)(a)–(h) coverage) and negotiation-grade (clause-by-clause risk scoring)."
metadata:
  author: "Oliver Schmidt-Prietz"
  license: "agpl-3.0"
  version: "2026-06-09"
---

# DPA Art. 28 GDPR — Review, Drafting & Redlining

## Purpose

This skill governs all work on **controller–processor contracts (Art. 28 GDPR)** and **joint-controller arrangements (Art. 26 GDPR)**. It produces:

- **Reviews** of existing DPAs (quick or negotiation-grade)
- **Drafts** of new DPAs / AVVs from modular templates (DE / EN)
- **Redlines** in response to counterparty drafts
- **Joint Controller Agreements** (JCA / Art.-26-Vereinbarung)

## Mode router — ALWAYS run first

Before doing anything else, classify the request into ONE of these modes:

| Mode | Trigger pattern | Workflow file |
|---|---|---|
| `REVIEW_QUICK` | "Is this DPA compliant?", "Art. 28(3)(a)–(h) check", short turnaround, sign/no-sign decision needed | `workflows/review-quick.md` |
| `REVIEW_NEG` | "Review this for negotiation", "give me redline points", "what should we push back on", deeper diligence | `workflows/review-negotiation.md` |
| `DRAFT` | "Draft a DPA", "create an AVV", "we need a processor agreement for [X]", greenfield | `workflows/draft.md` |
| `REDLINE` | Counterparty has sent a DPA, user wants tracked-changes / counter-proposals | `workflows/redline.md` |
| `JOINT_CONTROLLER` | "Art. 26", "joint controller", "JCA", or roles screen reveals JC not processor relationship | `workflows/joint-controller.md` |

**If unclear, ASK.** Do not guess between `REVIEW_QUICK` and `REVIEW_NEG` — the depth difference is ~30 min vs ~2–3 h of analytical work, and the output structure is materially different.

**Mode flips during the work are allowed and expected.** If a `REVIEW_QUICK` reveals issues serious enough that the user needs negotiation guidance, surface this and offer to escalate to `REVIEW_NEG`. If a roles screen during `DRAFT` or `REVIEW_*` reveals the parties are actually joint controllers, stop and switch to `JOINT_CONTROLLER`.

## Intake — ALWAYS gather these before producing output

Regardless of mode:

1. **Roles** — Who is controller, who is processor? Confirm explicitly. If both parties might be controllers, run the Art. 26 vs Art. 28 screen in `references/art26-joint-controller.md` BEFORE proceeding.
2. **Perspective** — Which side does the user represent? (controller-favorable / processor-favorable / balanced)
3. **Language** — DE / EN / bilingual? Default: match the language of the source document; if drafting from scratch, ASK.
4. **Tier (DRAFT and REDLINE modes)** — Tier 1 Commercial / Tier 2 Strict (2021/915 incorporated unmodified) / Tier 3 Hybrid (Sections I+II of 2021/915 + custom Section III). Load `references/tier-selection.md` and walk the decision tree if the user has not pre-selected. For REVIEW modes, the tier is whatever the source document is — identify it and continue.
5. **Processing scenario** — Concrete description: subject matter, nature, purpose, data categories, data subjects, duration. Without this, drafting is impossible and review is shallow. If missing, REQUEST it before proceeding.
6. **International transfers** — Will personal data be transferred outside the EEA, or accessed from outside the EEA? If yes, load `references/sccs-module-guide.md` and flag SCC requirements early. Note: 2021/915 (Tiers 2/3) does not by itself cover transfers — pair with 2021/914 if needed.
7. **Sub-processors** — General authorization, specific authorization, or none? This affects clause structure and risk profile. For Tiers 2/3, this maps to Clause 7.7 Option 1/2 of the SCCs.
8. **Special categories / Art. 9 / Art. 10 data** — If yes, enhanced TOMs and stricter purpose limitation needed; flag at intake.

## Hard rules

- **Never produce a DPA or review without confirming roles.** Mis-classifying a controller–controller relationship as controller–processor produces an invalid agreement and creates liability exposure on both sides.
- **Never paste templates verbatim without scenario tailoring.** Annex 1 (processing description) MUST reflect the actual processing — generic placeholders defeat Art. 28(3) chapeau.
- **Never omit Annex 2 (TOMs).** A DPA without specified TOMs fails Art. 28(3)(c) + Art. 32. If the user does not have TOMs ready, advise them to obtain the processor's TOMs document or use the template scaffold as a starting point, but flag this as an open item — never sign-off on an empty Annex 2.
- **Sub-processor list (Annex 3) cannot be empty if sub-processors exist.** "None at signing" is acceptable only if literally none; otherwise list them by name, location, processing activity, and safeguards.
- **International-transfer language is binding only if SCCs are actually executed.** Do not draft "the Parties agree to use the SCCs" without specifying module, signature mechanism (separate signature vs. docking via DPA), and Annexes I.A / I.B / I.C / II / III.
- **Joint-controller scenarios are NOT processor scenarios.** If the screen flags JC, switch to `JOINT_CONTROLLER` mode. Papering a JC arrangement as a DPA is a substantive defect, not a drafting choice.
- **Never advise "sign as is" after a quick review unless every Art. 28(3) item is PASS, no transfers in scope, and the user understands the residual liability allocation.** Default posture is "sign with documented residual risk" or "request changes".
- **Bilingual output ≠ machine translation.** When producing parallel DE/EN, use German legal-style register on the DE side ("der Verantwortliche", "der Auftragsverarbeiter", "Sie"-form for declarations) and standard commercial register on the EN side. Do not back-translate one from the other.

## Reference loading order

When entering any mode, load files in this order:

1. **Always** — `references/art28-3-checklist.md` (canonical Art. 28 requirements).
2. **Mode-dependent**:
   - `REVIEW_QUICK` → + the workflow file. That is enough.
   - `REVIEW_NEG` → + `references/common-defects.md` + `references/negotiation-fallbacks.md`. If the source draft is 2021/915-based, also + `references/2021-915-commission-text-{en,de}.md` (matching language).
   - `DRAFT` → + `references/tier-selection.md` (always); + the relevant template file (`templates/dpa-{commercial,strict,hybrid}-{en,de}.md` or `templates/jca-{en,de}.md`); + `references/2021-915-commission-text-{en,de}.md` if Tier 2 or Tier 3.
   - `REDLINE` → + `references/negotiation-fallbacks.md` + `references/tier-selection.md` + the relevant template as benchmark; + 2021/915 reference if counterparty draft is 2021/915-based.
   - `JOINT_CONTROLLER` → switch to `references/art26-joint-controller.md` and `templates/jca-{lang}.md`. The Art. 28 checklist is no longer the primary lens.
3. **Conditional** — Load `references/sccs-module-guide.md` whenever international transfers are in scope OR the source DPA mentions SCCs / Drittlandübermittlung / Standardvertragsklauseln. Note: 2021/915 (Art. 28) and 2021/914 (Chapter V) are different instruments — `sccs-module-guide.md` covers 2021/914, `2021-915-commission-text-{en,de}.md` covers 2021/915.

## Output structure by mode

### REVIEW_QUICK output

1. **Executive summary** (3–5 sentences): overall compliance posture and headline issues.
2. **Art. 28(3)(a)–(h) coverage table**: each obligation marked `PASS` / `WEAK` / `GAP` / `DEFECT` with one-line reason.
3. **Chapeau & framing** (subject matter, duration, nature, purpose, data types, categories of data subjects, controller's rights and obligations) — present or missing?
4. **SCC adequacy** (if transfers in scope): correct module? Annexes filled? TIA referenced?
5. **Top 3 issues** to fix.
6. **Recommendation**: sign / sign with side letter / do not sign without changes / escalate to `REVIEW_NEG`.

### REVIEW_NEG output

1. Executive summary + posture recommendation.
2. Roles confirmation + scenario summary (locked-in for the rest of the analysis).
3. **Clause-by-clause table**: clause # | obligation in scope | current text gist | issue | risk tier (1 = blocker / 2 = material / 3 = polish) | proposed fix.
4. **Annex review**:
   - Annex 1 (processing description) — sufficient detail for Art. 28(3) chapeau?
   - Annex 2 (TOMs) — concrete, measurable, mapped to Art. 32(1)(a)–(d)?
   - Annex 3 (sub-processors) — list current and define notification/objection mechanism?
   - Annex 4 (transfers + SCCs) — module, Annexes I–III, TIA?
5. **Negotiation strategy**: must-have / should-have / nice-to-have, sequenced for the actual negotiation.
6. **Walk-away conditions** — clauses where the user should not sign even after best-efforts negotiation.

### DRAFT output

1. Complete DPA / AVV main body in requested language(s).
2. Annex 1 — populated from intake.
3. Annex 2 — template scaffold OR populated if TOMs provided.
4. Annex 3 — populated or "none at signing" with notification mechanism.
5. Annex 4 — only if transfers in scope; correct SCC module incorporated.
6. **Drafting notes** (separate section): clauses left as alternatives, scenario assumptions made, follow-ups required from the user.

### REDLINE output

1. **Marked-up version**: additions in **bold**, deletions in ~~strikethrough~~. Always reproduce the counterparty's clause numbering for traceability.
2. **Cover memo**: changes summary; rationale by clause; fallback positions (T1 / T2 / T3); expected counterparty pushback per change.
3. **Side-letter draft** if used to address residual gaps not worth re-opening the main DPA over.

### JOINT_CONTROLLER output

1. **Roles analysis** — why this is JC, not processor; EDPB 07/2020 anchors cited.
2. **JCA main body** in requested language.
3. **Allocation matrix**: who handles what (data subject rights, breach notification to authorities, breach notification to data subjects, security, DPIA, transfers, complaints, audits).
4. **Public summary** under Art. 26(2) — short, plain-language, made available to data subjects (often via privacy notice).
5. Recital indicating that data subjects may exercise rights against either party irrespective of the allocation.

## Quality gates — verify before delivery

- [ ] Roles confirmed and Art. 28 vs Art. 26 screen passed.
- [ ] All Art. 28(3) chapeau elements addressed (subject matter, duration, nature, purpose, data types, categories of data subjects, controller's rights and obligations).
- [ ] All eight (a)–(h) obligations covered.
- [ ] Sub-processor mechanism defined (general or specific consent + notification + objection right).
- [ ] Audit rights specified (frequency, scope, cost allocation, third-party-auditor option, confidentiality).
- [ ] Deletion/return choice mechanism defined (Art. 28(3)(g)) with retention carve-outs for legal obligations.
- [ ] If transfers: SCC module identified, Annexes I.A/I.B/I.C/II/III in scope, TIA referenced.
- [ ] If special categories / Art. 10 data: enhanced TOMs flagged.
- [ ] Liability allocation reflects the user's perspective (not generic boilerplate).
- [ ] Language consistent throughout (no mixed-language clauses unless bilingual format with parallel columns).
- [ ] Practitioner's note appended for client deliverables — what the user should do next.

## Style & tone

- **German output**: formal legal register; "Sie"-form not used (legal entities are referred to as "der Verantwortliche" / "der Auftragsverarbeiter"); standard term is **Auftragsverarbeitungsvertrag** or **AV-Vertrag**, not "DPA".
- **English output**: standard commercial-contract register; defined terms in **bold** at first use; active voice for obligations ("The Processor shall ...").
- **No marketing language. No em dashes.** Active voice for processor obligations; passive only where standard contract idiom requires it.
- **For OneZero Legal client deliverables**: end every output with a **Practitioner's note** paragraph — what the user should actually do next (sign / push back / request information / escalate).

## Out of scope (do not silently expand into these)

- Standalone TOMs drafting beyond the Annex 2 scaffold (use Art. 32-specific guidance).
- Full TIA (Transfer Impact Assessment) documents — flag the requirement and reference TIA Skill if available.
- DPIA documents — reference the DPIA Navigator skill.
- Records of Processing (Verzeichnis von Verarbeitungstätigkeiten) — separate task.
- Substantive data-subject-rights workflows — reference dedicated skill if available.

If the user asks for any of the above, surface that this skill ends at the DPA boundary and offer to switch.

## Related GDPR skills

This skill works standalone, but pairs well with my other EU data-protection skills — install any on its own or combine them:

- **DPIA Sentinel** — Art. 35 Data Protection Impact Assessments
- **GDPR Breach Sentinel** — Art. 33/34 breach response & notification
- **Privacy Notice Generator** — Art. 13/14 privacy notices
- **Transfer Impact Assessment (TIA)** — Chapter V transfer assessments
- **Legitimate Interest** — Art. 6(1)(f) LIA / balancing test
