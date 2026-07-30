# DPA Template — Tier 3 (Hybrid): Sections I+II of 2021/915 + Custom Commercial Section III — English

## What this template is

A wrapper that **incorporates Sections I and II of the Standard Contractual Clauses adopted by Commission Implementing Decision (EU) 2021/915** as the data-protection substance of the agreement, **and replaces Section III** with a commercially negotiated term/termination/liability section. This is permitted under Clause 2(b) of the SCCs because the replacement does not contradict the obligations in Sections I and II.

The Art. 28(7) GDPR compliance presumption attaches to the unmodified Sections I and II text. Replacing Section III preserves the substantive Art. 28 compliance (the (a)–(h) obligations live in Sections I and II) while allowing the parties commercial flexibility on term, exit mechanics, and liability.

## When to use this template

Use Tier 3 (Hybrid) for **the most engagements where 2021/915 is on the table**. It is the practical sweet spot:

- Negotiated B2B contracts where the controller wants the safe-harbor benefit on Section II (where the Art. 28 substance lives) but needs commercial flexibility on Section III (which the Commission text addresses sparingly).
- Strategic vendor relationships with sophisticated liability allocation (super-cap, indemnities, insurance covenants).
- Engagements with multi-year terms, transition obligations, exit assistance — none of which Commission Section III addresses.
- Counterparty has accepted 2021/915 in principle but wants commercial mechanics negotiated.

For maximum safe-harbor posture (no Section III replacement), use **Tier 2 — Strict** (`dpa-strict-en.md`). For purely commercial work without the 2021/915 anchor, use **Tier 1** (`dpa-commercial-en.md`).

## How to use this template

1. Load `references/2021-915-commission-text-en.md` for the clause-by-clause practitioner guide.
2. Confirm the official OJ-EN text (binding) at https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021D0915.
3. Walk Section 1.4 (Choices) and lock in selections.
4. Populate Annexes I–IV from intake (Schedules 1–4 below).
5. **Customise Section III** — the replacement Section III in this template is a starting point at T2 (balanced); adjust per perspective using `references/negotiation-fallbacks.md`.
6. Sign and execute.

The Commission text for Sections I and II is incorporated by reference (Section 1.1 below) and is **not reproduced**. Section III is fully replaced — see Section 4 below.

## Critical drafting principle

**Sections I and II of the SCCs MUST NOT be modified.** All commercial flexibility lives in:
- The Section 1.4 choices (which the SCCs themselves contemplate).
- The completed Annexes (which the SCCs themselves require).
- Section 4 of this DPA (the Section III replacement, permitted under Clause 2(b)).

If you find yourself wanting to modify Section II language (e.g. weaken the instructions clause, narrow the audit right, cap a Section II obligation), Tier 3 is no longer the right tool — switch to Tier 1 (Commercial).

---

# DATA PROCESSING AGREEMENT

This **Data Processing Agreement** (the "**DPA**") is entered into on `{{EFFECTIVE_DATE}}` between:

**`{{CONTROLLER_NAME}}`**, a `{{CONTROLLER_LEGAL_FORM}}` registered under the laws of `{{CONTROLLER_JURISDICTION}}` with registered seat at `{{CONTROLLER_ADDRESS}}` and registration number `{{CONTROLLER_REG_NO}}` (the "**Controller**")

— and —

**`{{PROCESSOR_NAME}}`**, a `{{PROCESSOR_LEGAL_FORM}}` registered under the laws of `{{PROCESSOR_JURISDICTION}}` with registered seat at `{{PROCESSOR_ADDRESS}}` and registration number `{{PROCESSOR_REG_NO}}` (the "**Processor**", together with the Controller, the "**Parties**" and each a "**Party**").

## Recitals

A. The Parties have entered into `{{MAIN_AGREEMENT_TITLE}}` dated `{{MAIN_AGREEMENT_DATE}}` (the "**Main Agreement**") under which the Processor provides certain services to the Controller (the "**Services**").

B. In the course of providing the Services, the Processor processes personal data on behalf of the Controller within the meaning of Article 4(8) GDPR.

C. The Parties have agreed to govern the data-protection substance of their relationship by way of Sections I and II (and Annexes I–IV) of the Standard Contractual Clauses set out in the Annex to **Commission Implementing Decision (EU) 2021/915** of 4 June 2021 (OJ L 199, 7.6.2021, p. 18) (the "**SCC-Decision**" and the "**SCCs**" respectively).

D. The Parties have replaced Section III of the SCCs with the commercially negotiated terms in Section 4 of this DPA, as permitted under Clause 2(b) of the SCCs.

## SECTION 1 — INCORPORATION OF SECTIONS I AND II OF THE SCCs

### 1.1 Incorporation by reference

The Parties hereby agree to and adopt **Sections I and II** of the SCCs and **Annexes I, II, III and IV** thereto in their entirety and without modification. These provisions are incorporated into and form an integral part of this DPA. In case of conflict between this Section 1 (or Section 4 below) and Sections I or II of the SCCs, Sections I or II of the SCCs prevail.

### 1.2 Replacement of Section III

The Parties have replaced Section III of the SCCs (Clause 10 — Non-compliance with the Clauses and termination) with the commercially negotiated terms set out in Section 4 of this DPA. This replacement is permitted under Clause 2(b) of the SCCs because Section 4 (a) does not modify any provision of Sections I or II, and (b) addresses the same subject matter as the replaced Section III with terms that do not detract from the rights of data subjects.

### 1.3 Reference text

The Parties acknowledge that the binding text of Sections I and II of the SCCs is the text published in the Official Journal of the European Union at OJ L 199, 7.6.2021, p. 18, accessible via https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021D0915. All EU language versions are equally authentic. In case of doubt, the OJ text governs.

### 1.4 Capacity in which the SCCs are concluded

The SCCs are concluded under Regulation (EU) 2016/679 (General Data Protection Regulation) only. The optional reference to Regulation (EU) 2018/1725 in Clause 1 of the SCCs is not adopted.

### 1.5 Choices made by the Parties

| Choice | Selection |
|---|---|
| Optional Docking Clause (Clause 5) | `{{ENABLED / NOT ENABLED — default: ENABLED}}` |
| Sub-processor authorisation regime (Clause 7.7) | `{{OPTION 1 (specific) / OPTION 2 (general) — default: OPTION 2}}` |
| Time period for sub-processor authorisation request / change notification | `{{30 days — default}}` |

## SECTION 2 — COMPLETED ANNEXES TO THE SCCs

The Annexes to the SCCs are completed as set out in **Schedule 1** (Annex I), **Schedule 2** (Annex II), **Schedule 3** (Annex III) and **Schedule 4** (Annex IV) of this DPA.

## SECTION 3 — INTERNATIONAL TRANSFERS (where applicable)

### 3.1 Acknowledgment

The Parties acknowledge that under Clause 1(f) of the SCCs, the SCCs do not by themselves cover transfers of personal data outside the EEA under Chapter V GDPR.

### 3.2 Transfer mechanism

`{{If transfers are in scope, complete Schedule 5 and identify the mechanism: adequacy decision / Commission Implementing Decision (EU) 2021/914 SCCs / BCRs / derogation under Art. 49 GDPR. If no transfers, mark Schedule 5 "Not applicable".}}`

## SECTION 4 — REPLACEMENT FOR SECTION III OF THE SCCs (Term, Termination, Liability)

> 💼 *This Section 4 replaces Section III of the SCCs (Clause 10) per Section 1.2 above. It is drafted under Clause 2(b) of the SCCs and does not modify any provision of Sections I or II.*

### 4.1 Term

This DPA enters into force on the Effective Date and remains in force for the duration of the Services under the Main Agreement, plus any post-termination period required to give effect to Section 4.4 below.

### 4.2 Termination for material breach

(a) The Controller may terminate this DPA on thirty (30) days' written notice in case of material breach by the Processor of this DPA (including Sections I and II of the SCCs) that has not been cured within the notice period. Where the breach affects the data-protection substance and is not capable of cure, the Controller may terminate immediately on written notice.

(b) The Processor may terminate this DPA on thirty (30) days' written notice in case of material breach by the Controller of its obligations under this DPA that has not been cured within the notice period.

(c) Termination of this DPA on the basis of (a) or (b) above entitles the terminating Party to terminate the corresponding portion of the Main Agreement on the same basis without penalty.

### 4.3 Termination for change in law or supervisory authority intervention

Either Party may terminate this DPA on thirty (30) days' written notice (or such shorter period as required by law) where:

(a) a change in applicable data-protection law renders performance of this DPA materially impossible or unlawful, and the Parties cannot in good faith agree on a contractual amendment within sixty (60) days; or

(b) a competent supervisory authority issues a binding order, decision, or determination that prohibits or materially restricts the processing under this DPA.

### 4.4 Consequences of termination — return or deletion of personal data

(a) Upon termination of this DPA, the Processor shall, at the choice of the Controller exercised in writing within thirty (30) days of termination:

(i) return all personal data to the Controller in a commonly used, machine-readable format; or
(ii) delete all personal data in its possession or control,

in each case including all copies in production, archive, and backup systems, and shall provide written certification of compliance to the Controller.

(b) Personal data in backup systems shall be deleted upon expiry of the standard backup rotation period (which shall not exceed ninety (90) days from termination); restored backups shall be re-deleted promptly. Until expiry, backups shall be access-restricted and not used for any other purpose.

(c) The Processor may retain personal data only to the extent and for such period as required by Union or Member State law to which the Processor is subject. The Processor shall identify the law and the retention period to the Controller in advance, ensure such personal data is access-restricted and used only for the legally required purpose, and delete the personal data on expiry of the retention period.

> ℹ️ *This Section 4.4 reproduces the substance of Clause 10 of the SCCs (deletion-or-return at controller's choice) but with operational detail (timeline, certification, backup handling) the Commission text does not address. It does not detract from the SCCs.*

### 4.5 Transition assistance

For a period of up to `{{60–180}}` days following termination, the Processor shall provide reasonable transition assistance at the Controller's request, including data export, knowledge transfer, and parallel-running of services where practicable. Transition assistance is `{{included in fees / chargeable at agreed rates as set out in the Main Agreement}}`.

### 4.6 Liability allocation

`[ALT 1: controller-favorable]` Notwithstanding any contrary provision in the Main Agreement, the Processor's aggregate liability for damages arising out of or in connection with breaches of this DPA (including Sections I and II of the SCCs), breaches of applicable data-protection law, or personal data breaches shall be capped at an amount equal to two (2) times the fees paid or payable by the Controller under the Main Agreement in the twelve (12) months preceding the event giving rise to liability. This cap is in addition to (not in lieu of) the general liability cap under the Main Agreement and shall not apply to liability for: (a) gross negligence or wilful misconduct; (b) breach of confidentiality; (c) infringement of third-party intellectual property rights; or (d) any liability that cannot be limited or excluded under applicable law.

`[ALT 2: processor-favorable]` The Processor's aggregate liability for damages arising out of or in connection with breaches of this DPA shall be subject to the general liability cap under the Main Agreement.

### 4.7 Indemnification

The Processor shall indemnify the Controller against third-party claims, regulatory fines, and data subject compensation claims (and the Controller's reasonable costs of defence) to the extent caused by the Processor's breach of this DPA (including Sections I and II of the SCCs) or of applicable data-protection law.

### 4.8 Insurance

The Processor shall maintain cyber and data-protection insurance with limits commensurate with the liability exposure under this DPA, and shall provide a certificate of insurance to the Controller on request.

### 4.9 Cost allocation for assistance

`{{Routine assistance under Clauses 8 and 9 of the SCCs is included in the Service fees. Non-routine assistance may be charged at the Processor's reasonable rates with the Controller's prior agreement.}}`

### 4.10 Notices

Notices under this DPA shall be given in writing to the addresses set out at the head of this DPA, or to such other address as a Party may notify to the other in writing. Notices are effective on receipt.

### 4.11 Amendments

(a) Amendments to this DPA shall be in writing and signed by both Parties.

(b) Amendments to Sections I and II of the SCCs are not permitted; only the Annexes (Schedules 1–4) may be updated as set out in Clause 2(a) of the SCCs.

(c) Amendments to this Section 4 are permitted under Clause 2(b) of the SCCs provided they do not contradict Sections I or II.

### 4.12 Severability

If any provision of this Section 4 is held invalid or unenforceable, the remaining provisions of this Section 4 shall continue in full force. Severability of the SCCs is governed by the SCCs themselves.

### 4.13 Governing law and jurisdiction

This DPA is governed by the law of `{{GOVERNING_LAW}}`. The courts of `{{VENUE}}` have exclusive jurisdiction.

### 4.14 Survival

The following provisions survive termination of this DPA: Clause 7.4(b) of the SCCs (confidentiality of personnel) on a perpetual basis; Section 4.4 (return/delete obligations) until performed; Section 4.6 (liability) for the duration of the applicable limitation period; Section 4.7 (indemnification) on the same basis; Section 4.13 (governing law); and any other provision that by its nature is intended to survive.

### 4.15 Order of precedence

(a) In case of conflict between this Section 4 and Sections I or II of the SCCs (or Annexes I–IV thereto), Sections I or II (or the Annexes) prevail per Clause 4 of the SCCs.

(b) In case of conflict between this DPA (including the incorporated SCCs and this Section 4) and the Main Agreement on data-protection matters, this DPA prevails.

## Signatures

For the **Controller**:
Name: ___________________
Position: ___________________
Date: ___________________
Signature: ___________________

For the **Processor**:
Name: ___________________
Position: ___________________
Date: ___________________
Signature: ___________________

---

# Schedule 1 — Annex I to the SCCs (List of Parties)

| Role | Name | Address | Contact person | Signature and date |
|---|---|---|---|---|
| Controller | `{{CONTROLLER_NAME}}` | `{{CONTROLLER_ADDRESS}}` | `{{CONTROLLER_CONTACT}}` | (signed at end of DPA) |
| Processor | `{{PROCESSOR_NAME}}` | `{{PROCESSOR_ADDRESS}}` | `{{PROCESSOR_CONTACT}}` | (signed at end of DPA) |

# Schedule 2 — Annex II to the SCCs (Description of the Processing)

(Same structure as the Strict-tier template — completed from intake. See `dpa-strict-en.md` Schedule 2 for the field structure if needed.)

**Subject matter**: `{{SUBJECT_MATTER}}`

**Duration**: For the duration of the Services under the Main Agreement, plus any post-termination period under Section 4.4 of this DPA.

**Nature of the processing**: `{{NATURE}}`

**Purpose(s)**: `{{PURPOSE}}`

**Categories of personal data**:
- `{{Categories — list}}`
- Special categories under Art. 9 GDPR: `{{yes / no — if yes, specify}}`
- Personal data relating to criminal convictions and offences under Art. 10 GDPR: `{{yes / no}}`

**Categories of data subjects**: `{{list}}`

**Frequency**: `{{continuous / periodic / one-off}}`

**Retention**: `{{tied to Main Agreement, plus Section 4.4}}`

# Schedule 3 — Annex III to the SCCs (Technical and Organisational Measures)

(Same eight-section structure as the Strict template: pseudonymisation/encryption; CIA + resilience; restoration; testing; personnel; sub-processor oversight; sensitive data; measures to assist the Controller. Populate from intake or use the scaffold from `dpa-strict-en.md` Schedule 3 as starting point.)

# Schedule 4 — Annex IV to the SCCs (List of Sub-processors)

(Populate or mark "None at signing" — same structure as `dpa-strict-en.md` Schedule 4.)

# Schedule 5 — International Transfers (only if applicable)

(Same as `dpa-strict-en.md` Schedule 5.)

---

# Drafting Notes (delete before signature)

- This is the **most commonly appropriate** of the three tiers for negotiated B2B work.
- Confirm Sections I and II of the SCCs are referenced unmodified — any temptation to edit them means switching to Tier 1.
- Section 4 (replacement for Section III) can be tailored substantially: liability scope, transition mechanics, insurance, indemnification — adjust per perspective via `references/negotiation-fallbacks.md`.
- For Schedules 2, 3, 4, 5: see the scaffold in `dpa-strict-en.md` for full field detail.
- Verify the binding OJ-EN text against `references/2021-915-commission-text-en.md` clause map before signing.

# Practitioner's note (for OneZero Legal client deliverables)

Tier 3 (Hybrid) is the practical sweet spot for most engagements where 2021/915 is on the table. The data-protection substance (Sections I + II + Annexes I–IV) carries the Art. 28(7) compliance presumption; Section III is replaced with commercially negotiated mechanics (term, termination, liability, indemnification, insurance, transition) that the Commission text does not adequately address.

The architecture is defensible to a supervisory authority: Sections I and II are unmodified (compliance presumption preserved); Section 4 of this DPA is permitted under Clause 2(b) SCCs because it does not contradict Sections I or II (which the SA can verify by reading Section 4 and confirming no Section II obligation is narrowed).

The Hierarchy clause (Clause 4 SCCs) still governs: where Section 4 of this DPA were to conflict with Sections I or II, the SCCs prevail. Practitioners should walk Section 4 against Section II clause-by-clause as a final check before signing — a stray indemnity exclusion or liability cap that effectively narrows a Section II obligation would create a tension the SA might pick up.
