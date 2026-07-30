# Negotiation Fallbacks — Tiered Positions

This file is loaded for `REVIEW_NEG` and `REDLINE` modes. It maps the most-negotiated DPA clauses to **tiered positions** for both perspectives:

- **T1 (opening)** — strongest credible position for the perspective.
- **T2 (compromise)** — typical landing zone.
- **T3 (walk-back)** — minimum acceptable; below this, do not sign.

Use the tier system to plan the negotiation: open at T1, expect to land at T2, hold the line at T3. The opposite party's T2 is usually adjacent to your T2 — that is where the deal lives.

---

## Sub-processor regime

### Controller-favorable

| Tier | Position |
|---|---|
| **T1** | Specific authorisation per sub-processor; processor may not engage any new sub-processor without prior written controller consent (not unreasonably withheld). |
| **T2** | General authorisation for the list in Annex 3; 30 days' prior notice for additions; controller may object on reasonable grounds; if dispute unresolved, controller may terminate without penalty. |
| **T3** | General authorisation; 14 days' notice; objection right with termination as sole remedy; flow-down warranty + processor remains fully liable. |

### Processor-favorable

| Tier | Position |
|---|---|
| **T1** | General authorisation; processor publishes sub-processor list on its trust page; controller subscribes for change notifications; objection right for material breach only. |
| **T2** | General authorisation; 30 days' notice; objection on reasonable data-protection grounds; processor offers either (a) alternative sub-processor or (b) controller may terminate affected service portion. |
| **T3** | Specific authorisation for an enumerated list in Annex 3; general authorisation for affiliates of sub-processors; new categories of sub-processors require notice + controller objection. |

**Likely landing zone**: Controller T2 ≈ Processor T2. The hard fights are over (a) notification mechanism (active vs. passive subscription), (b) objection grounds (any reasonable vs. data-protection-specific), and (c) termination consequences (full main agreement vs. affected portion only).

---

## Audit rights

### Controller-favorable

| Tier | Position |
|---|---|
| **T1** | Controller (or its mandated auditor) may conduct on-site or remote audit annually + on cause; 30 days' notice (zero days for breach-triggered); processor bears costs; full access to records and personnel. |
| **T2** | Annual audit by mutually-agreed auditor with reasonable confidentiality; certifications accepted as supporting evidence; on-cause audit right preserved; each party bears own costs except processor bears costs if material non-compliance found. |
| **T3** | Annual audit via certifications + processor's questionnaire; on-cause audit right (cause = breach, supervisory authority request, demonstrated material concern); 60 days' notice; controller bears third-party-auditor cost. |

### Processor-favorable

| Tier | Position |
|---|---|
| **T1** | Audit right satisfied by processor's annual SOC 2 / ISO 27001 reports; written questionnaire on request, 90-day response; no on-site inspections except by court order. |
| **T2** | Certifications + questionnaire as primary; on-site inspection on cause shown, 60 days' notice, by mutually-agreed independent auditor under NDA, controller bears costs, no disruption to operations, finding-related confidentiality. |
| **T3** | On-site inspection right; 30 days' notice (zero for breach); controller bears costs except material non-compliance; non-disruption + confidentiality (with carve-out for SA disclosure). |

**Likely landing zone**: Controller T2 ≈ Processor T2/T3. The fight is over (a) whether on-site is preserved or replaced, (b) cost allocation when no non-compliance is found, (c) confidentiality scope.

---

## Breach notification timeline (Art. 33 assistance under (f))

### Controller-favorable

| Tier | Position |
|---|---|
| **T1** | Processor notifies within 12 hours of becoming aware of any actual or suspected breach; full Art. 33(3) information set in initial notice. |
| **T2** | 24 hours for confirmed; 48 hours for suspected; updates as facts develop; Art. 33(3) information set required by hour 48 at the latest. |
| **T3** | 48 hours for confirmed; reasonable updates as facts develop; Art. 33(3) information set required by hour 72. |

### Processor-favorable

| Tier | Position |
|---|---|
| **T1** | Processor notifies "without undue delay and in any event within 72 hours of becoming aware of a confirmed breach". |
| **T2** | 48 hours for confirmed breach; suspected events handled internally; information set per Art. 33(3) "to the extent reasonably available". |
| **T3** | 24 hours for confirmed; suspected events flagged at processor's discretion if material; updates within reasonable time. |

**Likely landing zone**: 24–48 hours for confirmed; "credibly suspected" notification often dropped or made qualitative. Information set tracking Art. 33(3) is non-negotiable for serious counterparties.

---

## Liability cap for data-protection breaches

### Controller-favorable

| Tier | Position |
|---|---|
| **T1** | Uncapped for processor's data-protection breaches; or supercap at 3× annual fees with no general cap applying. |
| **T2** | Supercap at 2× annual fees for data-protection breaches; carve-outs for gross negligence, wilful misconduct, breach of confidentiality, infringement of third-party IP. |
| **T3** | Standard cap (12 months' fees) but with carve-outs for the items above. |

### Processor-favorable

| Tier | Position |
|---|---|
| **T1** | Single aggregate cap for all liabilities including data-protection at 12 months' fees (or fixed amount); excludes regulatory fines and data subject claims. |
| **T2** | Standard 12-month cap with separate supercap for data-protection at 1.5–2× for direct losses; regulatory fines and data subject claims included in supercap. |
| **T3** | Supercap at 2× for data-protection liabilities; regulatory fines and data subject claims included up to supercap; gross negligence / wilful misconduct uncapped. |

**Likely landing zone**: Supercap at 2× fees including regulatory fines, with uncapped exposure for gross negligence / wilful misconduct.

---

## Indemnification

### Controller-favorable

| Tier | Position |
|---|---|
| **T1** | Processor indemnifies controller for all third-party claims, regulatory fines, data subject compensation, and reasonable costs (including legal fees) caused by processor's breach of this DPA or applicable data protection law. |
| **T2** | Same as T1 but capped under the DP supercap (so indemnity does not exceed the agreed exposure). |
| **T3** | Indemnity for third-party claims and data subject claims; regulatory fines covered only to the extent processor's breach demonstrably caused them. |

### Processor-favorable

| Tier | Position |
|---|---|
| **T1** | No indemnification — each party bears its own losses; controller is responsible for its own regulatory exposure. |
| **T2** | Mutual indemnification for third-party claims caused by the indemnifying party's breach; regulatory fines on the party fined; both subject to liability cap. |
| **T3** | Processor indemnifies for third-party claims and data subject claims caused by processor breach; regulatory fines under the DP supercap. |

**Likely landing zone**: Processor indemnifies for third-party claims, data subject claims, and regulatory fines under the DP supercap; controller bears its own fines for matters not caused by processor's breach.

---

## TOMs change mechanism

### Controller-favorable

| Tier | Position |
|---|---|
| **T1** | TOMs may not be changed without controller's prior written approval. |
| **T2** | Processor may update TOMs provided level of security is not materially diminished; controller approval required for material reductions; controller informed of all changes. |
| **T3** | Processor may update TOMs provided level of security is not diminished; annual notification of changes. |

### Processor-favorable

| Tier | Position |
|---|---|
| **T1** | Processor maintains current TOMs as published; updates at processor's discretion. |
| **T2** | Processor may update TOMs at its discretion; will not materially reduce; published changes act as notice. |
| **T3** | Processor may update with no material reduction; specific notification on material changes. |

**Likely landing zone**: Processor T2 ≈ Controller T3. Critical detail: controller must have *something* to point to if processor degrades security; "no material reduction" is the workable standard.

---

## Deletion / return choice (g)

### Controller-favorable

| Tier | Position |
|---|---|
| **T1** | Controller chooses; export in commonly-used machine-readable format at no additional cost; certification of deletion within 30 days; backups deleted at end of standard rotation (≤90 days). |
| **T2** | Same as T1 but reasonable export-cost recovery for non-standard formats. |
| **T3** | Choice preserved; export in processor's standard format; certification on request; backup retention up to standard rotation. |

### Processor-favorable

| Tier | Position |
|---|---|
| **T1** | Processor's standard return + delete process; export in processor's preferred format; certification on request; legal-hold and backup carve-outs. |
| **T2** | Choice preserved per Art. 28(3)(g); export in processor's standard format; reasonable cost recovery for non-standard exports; backup retention up to 180 days. |
| **T3** | Choice preserved; standard format; certification on request; backup retention up to 90 days. |

**Likely landing zone**: Choice preserved (this is non-negotiable); cost recovery for non-standard exports; backup rotation 90–180 days.

---

## Service-improvement / analytics carve-out

This is the single most contentious clause in modern SaaS DPAs.

### Controller-favorable

| Tier | Position |
|---|---|
| **T1** | No carve-out. All processor processing is on documented controller instructions. |
| **T2** | Narrow carve-out for security analytics and abuse prevention only; processor confirms it does not act as controller for any other purpose. |
| **T3** | Carve-out for security analytics and aggregated/de-identified statistical use only; processor warrants the de-identification process meets a defined standard (e.g. EDPB anonymisation guidance); processor acts as separate controller for such derived data. |

### Processor-favorable

| Tier | Position |
|---|---|
| **T1** | Broad carve-out for "service improvement, security, fraud prevention, product development, and benchmarking using aggregated and de-identified data". |
| **T2** | Carve-out for "service improvement, security analytics, and benchmarking using aggregated and de-identified data"; processor acts as separate controller. |
| **T3** | Carve-out for security analytics + aggregated statistical use only; processor warrants de-identification; processor acts as separate controller. |

**Likely landing zone**: Narrow carve-out for security analytics + aggregate-only stats; processor acknowledged as separate controller for that piece; controller's data not used for model training without explicit additional consent.

**Practitioner note**: when reviewing AI-vendor DPAs in 2025–2026, watch for "model training" carve-outs hidden in service-improvement language. These are typically not acceptable for any controller dealing with personal data of identifiable individuals without an explicit legal basis and transparency to data subjects.

---

## Insurance

(Not strictly an Art. 28 element but routinely negotiated alongside.)

### Controller-favorable

| Tier | Position |
|---|---|
| **T1** | Cyber insurance policy with limits ≥ supercap; named insured includes controller; processor provides certificate; coverage includes regulatory defence and breach response. |
| **T2** | Cyber insurance with limits ≥ liability cap; certificate on request; processor maintains for term + 2 years tail. |
| **T3** | Cyber insurance with reasonable limits for processing volume; certificate on request. |

### Processor-favorable

| Tier | Position |
|---|---|
| **T1** | Insurance is processor's internal matter; no contractual obligation. |
| **T2** | Cyber insurance maintained at reasonable levels; certificate on request. |
| **T3** | Cyber insurance with limits aligned to liability exposure under the contract; certificate on request. |

**Likely landing zone**: Cyber insurance maintained at levels aligned to liability exposure; certificate on request; tail coverage for serious processing.

---

## Survival on termination

| Element | Survival recommendation |
|---|---|
| Confidentiality | Indefinite (or aligned with main agreement) |
| Deletion / return obligation under (g) | Until completed; certification then ends the obligation |
| Audit right | Limited tail (e.g. 1 year post-termination, only as to processing during the term) |
| Liability and indemnity | Aligned with main agreement; data-protection supercap survives until limitation period expires |
| Confidentiality of audit findings | Indefinite |

---

## How to use this file

In `REVIEW_NEG`:
1. Identify the defect (using `references/common-defects.md`).
2. Look up the relevant clause in this file.
3. Identify what tier the counterparty's draft sits at.
4. Propose the next tier up for the user's perspective as the redline.
5. Note T2 as the realistic landing zone; flag the T3 walk-back boundary.

In `REDLINE`:
1. For each redline, indicate the tier ladder ("opening at T1, fallback to T2 if pushed").
2. Mark the user's T3 boundary so the negotiator knows when to walk away rather than concede further.

Always respect the user's explicit perspective. If the user is processor-side, the controller-favorable column is the *opposing* position to anticipate, not the position to draft.
