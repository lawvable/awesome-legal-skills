# Reference: Commission Implementing Decision (EU) 2021/915 — Clause Map (EN)

This file is a **practitioner's clause-by-clause guide** to the Standard Contractual Clauses adopted by Commission Implementing Decision (EU) 2021/915 of 4 June 2021 on standard contractual clauses between controllers and processors under Article 28(7) GDPR (OJ L 199, 7.6.2021, p. 18).

## Why this file is a guide, not a reproduction

The Commission text is binding in its official OJ version. Tier 2 (Strict) and Tier 3 (Hybrid) templates **incorporate the Commission text by reference** rather than retyping it — this is mainstream practice at EU practices because (a) it is impossible to introduce drift errors, (b) counterparty counsel can verify the binding text against the OJ in seconds, and (c) the compliance presumption under Art. 28(7) GDPR attaches to the Commission text *as published in the OJ*, not to copies.

This file therefore tells you, for each Commission clause: what it does, where the official text lives, what choices the parties must make in the Annexes, and the drafting traps. It does not reproduce the binding text. To consult the binding text:

- **Official EN text**: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021D0915
- **Official DE text**: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021D0915
- **All EU language versions are equally authentic.**

## Document structure

The Annex to the Decision contains:

- **Section I** — Clauses 1 to 5 (purpose, invariability, interpretation, hierarchy, optional docking)
- **Section II** — Clauses 6 to 9 (description; obligations of the parties; assistance to the controller; breach notification)
- **Section III** — Clause 10 (non-compliance and termination)
- **Annex I** — List of parties (signed)
- **Annex II** — Description of the processing
- **Annex III** — Technical and organisational measures (TOMs), including measures to assist the controller
- **Annex IV** — List of sub-processors (where general written authorisation has been given)

## Section I — Clauses 1 to 5

### Clause 1 — Purpose and scope

**What it does.** Anchors the SCCs to Art. 28(3) and (4) GDPR. Confirms the SCCs apply to processing as specified in Annex II. Confirms Annexes I to IV are integral. **Confirms the SCCs do not by themselves cover Chapter V transfers (Clause 1(f)).**

**Choices.** Clause 1 in the official text presents an optional reference to Regulation (EU) 2018/1725 (EUDPR) where one party is a Union institution. **Default for private-sector contracts: GDPR-only; do not adopt the EUDPR cross-reference.**

**Trap.** Clause 1(f) is the single most overlooked provision. If the relationship involves transfers outside the EEA, Decision 2021/915 alone is **not sufficient** — pair with Decision 2021/914 (international-transfer SCCs). See `references/sccs-module-guide.md` and Annex Note 4 in the wrapper templates.

### Clause 2 — Invariability of the Clauses

**What it does.** The Parties undertake **not to modify** the Clauses, except for completing or updating the Annexes. Adding the SCCs to a broader contract or adding clauses that do not contradict them is permitted.

**Choices.** None — this clause is the foundation of the compliance presumption.

**Trap.** Editing Section II clauses voids the compliance presumption. The commercial overlay in the wrapper templates is permitted under Clause 2(b) because it sits outside Sections I–III and does not contradict them. Anything that would cap or override a Section II obligation is impermissible.

### Clause 3 — Interpretation

**What it does.** Defined terms align with GDPR; the Clauses are read in light of GDPR and not in a way that prejudices data subjects' rights.

**Choices.** None.

### Clause 4 — Hierarchy

**What it does.** In case of conflict between the Clauses and any related agreement (existing or later), **the Clauses prevail**.

**Choices.** None.

**Trap.** Clause 4 means the Clauses **prevail over the main service agreement**. Practitioners must check the main agreement for service-improvement licences, broad data-use grants, marketing carve-outs, or liability provisions that would otherwise conflict — Clause 4 silently disables them. This is desirable for the controller but worth a margin note on the cover memo to the client.

### Clause 5 — Optional — Docking clause

**What it does.** Permits new entities to accede to the Clauses by completing and signing Annex I.

**Choices.** `[ENABLED]` or `[NOT ENABLED]`. **Default: ENABLED** unless parties have a clear reason to exclude future accession.

**Trap.** None significant. If enabled, ensure Annex I is structured to accept additional party blocks.

## Section II — Clauses 6 to 9

### Clause 6 — Description of processing(s)

**What it does.** Cross-references Annex II for the operative description of processing operations, categories of personal data, and purposes.

**Choices.** None in Clause 6 itself; the substance is in Annex II (subject matter, nature, duration, purpose, data categories, data subject categories, retention).

**Trap.** Annex II must be concrete. A cross-reference of the form "Services as set out in the Master Agreement" fails Art. 28(3) chapeau. See `references/art28-3-checklist.md` defect D1.1.

### Clause 7 — Obligations of the Parties

The eight sub-clauses of Clause 7 implement the bulk of Art. 28(3)(a)–(h):

| Sub-clause | Topic | Maps to Art. 28(3) |
|---|---|---|
| 7.1 | Instructions | (a) |
| 7.2 | Purpose limitation | (a) |
| 7.3 | Duration | chapeau |
| 7.4 | Security of processing + confidentiality | (b), (c) |
| 7.5 | Sensitive data | reinforces (c) |
| 7.6 | Documentation and compliance + audits | (h) |
| 7.7 | Use of sub-processors | (d), Art. 28(2), (4) |
| 7.8 | International transfers | (a), Chapter V |

#### 7.1 Instructions

**What it does.** Processor processes only on documented instructions; carve-out for Union/Member State law with notification duty; processor must inform controller if instructions infringe GDPR.

**Choices.** None — the text is fixed.

**Trap.** This is the clause that most commercial DPAs weaken via "as may be necessary to provide the Services" language. The Commission text does not allow that latitude — which is precisely why the strict tier exists.

#### 7.2 Purpose limitation

**What it does.** Processing only for the specific purpose(s) set out in Annex II.

**Choices.** None.

**Trap.** Practitioners sometimes try to add "service improvement" or "analytics" carve-outs in the main agreement. Clause 4 (Hierarchy) defeats them. If the processor needs such uses, that is a Tier 1 (Commercial) decision, not a Tier 2 (Strict) one.

#### 7.3 Duration

**What it does.** Processing only for the duration specified in Annex II.

**Choices.** None in the body; specify duration in Annex II (typically tied to the main service contract).

#### 7.4 Security of processing

**What it does.** Implementation of TOMs in Annex III; Art. 32-style risk calibration; access on need-to-know basis; confidentiality of authorised personnel (statutory or contractual).

**Choices.** None in the body; substance is in Annex III.

**Trap.** Annex III must be concrete. ISO 27001 alone is supporting evidence, not a TOMs description. See defect D4.1 / D4.3 in `references/common-defects.md`.

#### 7.5 Sensitive data

**What it does.** Where the processing involves Art. 9 / Art. 10 data, the processor applies specific restrictions and/or additional safeguards.

**Choices.** None in the body; specify the additional safeguards in Annex III, Section 7 (Sensitive Data) of the wrapper TOMs scaffold.

**Trap.** Silence on additional safeguards in Annex III when sensitive data is in scope = failure of Clause 7.5.

#### 7.6 Documentation and compliance (audits)

**What it does.** Demonstrate compliance; respond promptly to controller's inquiries; provide information necessary to demonstrate compliance; permit and contribute to audits, including inspections, by the controller or an independent auditor; certifications may be taken into account; results of audits available to supervisory authorities on request.

**Choices.** None in the body. Operational details (notice period, frequency, cost allocation) belong in Annex III Section "Measures for ensuring accountability".

**Trap.** Practitioners may try to limit audits to written questionnaires only. The Commission text expressly preserves on-site inspections — a contractual cap (e.g. "audit means questionnaire only") would contradict 7.6 and is therefore impermissible under Clause 2(a).

#### 7.7 Use of sub-processors

**What it does.** Two options: (1) prior specific written authorisation, or (2) general written authorisation with advance notice of changes giving controller time to object. Sub-processor contract must impose, **in substance, the same** data protection obligations. Processor remains fully liable.

**Choices.**
- **OPTION 1** (specific) or **OPTION 2** (general) — pick one in the wrapper template.
- **Time period** for authorisation request (Option 1) or change notification (Option 2) — wrapper default: **30 days** for Option 2.
- **Annex IV** — list of sub-processors authorised at signing (always populated under Option 2; populated incrementally under Option 1).

**Trap.** "None at signing" in Annex IV when the processor in fact uses sub-processors is a defect. See D5.5 in `references/common-defects.md`.

#### 7.8 International transfers

**What it does.** Confirms the processor only transfers to a third country / international organisation on documented instructions, and only where compliance with Chapter V GDPR is ensured.

**Choices.** None in the body; the **mechanism** for Chapter V compliance (adequacy / 2021/914 SCCs / BCRs / derogation) belongs alongside the SCCs as a separate instrument. See `references/sccs-module-guide.md`.

**Trap.** A common misreading is "2021/915 covers transfers." It does not — Clause 1(f) and Clause 7.8 explicitly say so.

### Clause 8 — Assistance to the controller

**What it does.** Two layers of assistance: (1) data subject rights — forwarding requests received directly, supporting the controller's response; (2) Art. 32–36 — security, breach notification (Arts. 33–34), DPIA (Art. 35), prior consultation (Art. 36).

**Choices.** None in the body. The wrapper template's TOMs scaffold (Annex III) includes "Measures to assist the controller" sub-section where operational specifics live.

**Trap.** Cost allocation for assistance is silent in the Commission text. Wrapper templates default to "routine assistance included; non-routine recoverable at agreed rates" — this is a Section IV overlay, not a Section II modification.

### Clause 9 — Notification of personal data breach

**What it does.** Two scenarios — breaches affecting data processed by the controller (sub-clause 9.1) and breaches affecting data processed by the processor (sub-clause 9.2). For the latter, processor notifies controller "without undue delay" with the Art. 33(3) information set; assists with controller's Art. 34 communications to data subjects where required.

**Choices.** None in the body. The wrapper template's Annex III "Measures to assist the controller" sub-section may specify operational timelines (e.g. 48 hours) consistent with EDPB Guidelines 9/2022 — these supplement, not replace, the "without undue delay" standard.

**Trap.** The Commission text's "without undue delay" predates EDPB Guidelines 9/2022. Adding a numerical deadline (e.g. 48 hours) in Annex III is permitted under Clause 2(b) as an additional safeguard. Replacing "without undue delay" in the body with a specific number would void the presumption.

## Section III — Clause 10 (non-compliance and termination)

**What it does.** Sets out the controller's right to suspend or terminate processing in case of processor non-compliance with the Clauses; processor's obligations on termination (return or delete personal data at controller's choice).

**Choices.** None in the body of Clause 10.

**Trap (and the reason for Tier 3 / Hybrid).** Clause 10's termination mechanics are sparse and do not address commercial concerns: term, termination for convenience, transition assistance, post-termination liability, governing law, dispute resolution. **Tier 2 (Strict)** keeps Clause 10 untouched and adds a Section IV overlay for the commercial mechanics. **Tier 3 (Hybrid)** replaces Section III entirely with a commercially negotiated termination/term/liability section while keeping Sections I–II locked.

The substantive Art. 28(3)(g) obligation (deletion or return at controller's choice) **cannot be modified** in either tier — it is part of Section II via Clause 7.6 and Clause 10's interaction.

## Annexes I–IV

The Annexes carry the operational substance and are the parts the parties always complete:

| Annex | Content | Notes |
|---|---|---|
| **Annex I** | List of parties | Signed by each party with role (controller / processor) |
| **Annex II** | Description of processing | Mirrors Art. 28(3) chapeau (subject matter, nature, duration, purpose, data categories, data subjects). Should be concrete; defect D1.1 if reduced to a cross-reference. |
| **Annex III** | TOMs + measures to assist the controller | Mapped to Art. 32(1)(a)–(d) and to assistance under Clauses 8 and 9. Concrete and measurable. |
| **Annex IV** | List of sub-processors | Required if Clause 7.7 Option 2 is selected. Empty if Option 1 (and updated as authorisations are granted). |

## Annex Note 4 — Coupling with international-transfer SCCs (2021/914)

If the relationship involves transfers outside the EEA, the wrapper template must address Chapter V GDPR via a **separate instrument**:

- **Adequacy decision** (no SCCs needed; document the decision relied on).
- **2021/914 SCCs** — pick the correct Module (Module 2 for controller-to-processor, Module 3 for processor-to-sub-processor), populate Annexes I.A / I.B / I.C / II / III, conduct TIA.
- **BCRs / derogations** — case by case.

In practice: 2021/915 governs the controller-processor substance; 2021/914 governs the cross-border element. Both can be executed as separate documents, or 2021/914 can be attached to the 2021/915 wrapper as an additional schedule. The 2021/915 Annexes II and III may be cross-referenced from 2021/914 Annexes I.B and II respectively to avoid divergence.

See `references/sccs-module-guide.md` for the module decision and TIA logic.

## Practitioner traps — quick reference

1. **Modifying Section II = losing the compliance presumption.** All commercial flexibility lives in the Annexes (drafting choices) and the Section IV overlay.
2. **Forgetting Chapter V.** 2021/915 alone does not cover transfers — Clause 1(f) is explicit.
3. **Empty or generic Annex II / III / IV.** The Annexes carry the substantive Art. 28(3) compliance; thin Annexes mean the Decision's safe-harbor effect rests on nothing operational.
4. **Conflicting main agreement.** Clause 4 silently disables conflicts — desirable but worth flagging on the cover memo.
5. **Clause 7.7 Option choice.** Defaulting to Option 2 (general authorisation) without populating Annex IV is a defect.
6. **Sensitive data without Annex III safeguards.** Clause 7.5 obligation goes unmet.
7. **"Without undue delay" without operational specifics in Annex III.** Permissible but soft; EDPB Guidelines 9/2022 expects clarity.

## Where this file is loaded

- `templates/dpa-strict-en.md` (Tier 2) — load this file in full when drafting.
- `templates/dpa-hybrid-en.md` (Tier 3) — load this file plus `references/negotiation-fallbacks.md` (for the replacement Section III).
- `workflows/draft.md` — load this file when intake item I-T (tier choice) = 2 or 3.
- `workflows/review-negotiation.md` — load this file when reviewing a counterparty's 2021/915-based draft, alongside `references/art28-3-checklist.md`.
