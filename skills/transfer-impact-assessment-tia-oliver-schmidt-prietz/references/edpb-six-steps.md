# EDPB Six-Step TIA Methodology

Source: EDPB Recommendations 01/2020 on measures that supplement transfer tools to ensure compliance with the EU level of protection of personal data (Version 2.0, adopted 18 June 2021).

This file encodes the regulatory backbone of the TIA. The skill follows these six steps faithfully. The CNIL TIA Guide (final version, January 2025) provides the structured-form implementation; this file provides the methodology.

---

## Step 1: Know Your Transfer

The exporter must have a clear picture of the transfer before assessing it.

**Required information:**
- Exporter identity and role (controller, processor, joint controller)
- Importer identity, role, country, sector
- Categories of personal data (including any Art. 9 special categories)
- Categories of data subjects
- Purpose of the transfer
- Volume and frequency (one-off, periodic, continuous)
- Data format (plaintext, encrypted in transit, encrypted at rest, pseudonymised)
- Onward transfers — does the importer transfer the data further?

**Output:** A structured transfer description that anchors Steps 2–6.

## Step 2: Identify the Transfer Tool

Which Chapter V mechanism is being relied on?

- **Art. 45 — Adequacy decision.** No further safeguards required; TIA not mandatory. Document the decision reference, scope, conditions, and review/expiry dates.
- **Art. 46 — Appropriate safeguards.** Full TIA required.
  - 46(2)(a): legally binding instrument between public authorities
  - 46(2)(b): Binding Corporate Rules (BCR-C or BCR-P)
  - 46(2)(c): Standard Contractual Clauses (SCCs) — 2021 modules 1–4
  - 46(2)(d): SA-approved SCCs
  - 46(2)(e): approved code of conduct
  - 46(2)(f): approved certification mechanism
  - 46(3)(a): ad hoc clauses with SA authorisation
- **Art. 47 — BCRs.** Subset of Art. 46 with SA approval process.
- **Art. 49 — Derogations.** TIA not required, but justification must be documented. See `art49-derogations.md` for the balanced assessment.

## Step 3: Assess Third-Country Law and Practices

Determine whether the legislation and practices in the recipient country impinge on the effectiveness of the transfer tool selected in Step 2.

**The skill structures this in three blocks (informed by CNIL guide tables):**

**Block A — Data protection framework:**
- General data protection law (name, scope)
- Independent supervisory authority
- Data subject rights (access, rectification, deletion, objection)
- Effective remedies and dissuasive sanctions

**Block B — Surveillance and government access laws:**
For each relevant law:
- Scope (entities, data types)
- Powers (targeted vs. bulk, content vs. metadata)
- Four essential guarantees (see `essential-guarantees.md`):
  1. Clear, precise, accessible rules
  2. Necessary and proportionate
  3. Independent oversight
  4. Effective remedies

**Block C — Practical risk assessment (Rosenthal-inspired):**
- Importer's history of government access requests
- Realistic targeting basis (sector, data type, scale)
- Importer's technical access to plaintext
- Realistic interest of third-country authorities in this data

**Conclusion — three-way fork (CNIL methodology):**
1. **Transfer tool effective** → proceed to Step 6.
2. **Transfer tool not effective, supplementary measures needed** → proceed to Step 4.
3. **Transfer tool not effective on paper, BUT no realistic basis to believe problematic law will apply to this transfer in practice** → proceed to Step 6 with thorough documentation of why.

## Step 4: Identify and Adopt Supplementary Measures

Triggered when Step 3 returns conclusion (2). The skill loads `supplementary-measures.md` and auto-suggests measures matched to the identified gaps. Three categories per EDPB Rec 01/2020 Annex 2:

- **Technical** — encryption with exporter-held keys, pseudonymisation, split processing, transport hardening.
- **Contractual** — transparency obligations, challenge/contest clauses, enhanced audit rights, data localisation.
- **Organisational** — access controls, government request handling policies, certifications.

**Critical effectiveness check:** Each measure has "when effective" and "when NOT effective" conditions. If the gap cannot be closed by available measures (e.g., importer must decrypt to process), the skill flags this honestly — the transfer cannot proceed as structured.

## Step 5: Implementation Procedural Steps

Once measures are selected, document the implementation plan:
- Contractual amendments needed (SCC Annex II, side letters)
- Technical deployments (encryption, key management, pseudonymisation pipeline)
- Organisational rollout (policies, training)
- Responsible parties (exporter, importer, both)
- Timeline and milestones

## Step 6: Re-assessment at Appropriate Intervals

A TIA is a living document. Document:
- Next periodic review date (12-month default; shorter for high-risk)
- Event-driven triggers (new surveillance law, SA enforcement, importer government request, certification change)
- Standing triggers (adequacy decision review dates, DPF political fragility)
