# Common DPA Defects — Anti-Pattern Library

This file catalogues defects observed repeatedly in commercial DPAs, organised by clause area. It is loaded for `REVIEW_NEG` and `REDLINE` modes. Each entry is structured for direct citation in a review memo:

- **Pattern** — the actual defective wording or structural choice.
- **Why it fails** — the GDPR / Art. 28 anchor.
- **Risk tier** — 1 = blocker (do not sign); 2 = material (negotiate); 3 = polish (acceptable but should fix in next round).
- **Standard fix** — the corrected wording or structural change.

---

## Chapeau / Annex 1 (processing description)

### D1.1 — "Services as set out in the Master Agreement" stub

- **Pattern**: Annex 1 reduced to a single line cross-reference to the main service contract.
- **Why it fails**: Art. 28(3) chapeau requires *subject matter, duration, nature, purpose, type of personal data, categories of data subjects*. A cross-reference to a commercial agreement does not address these data-protection-specific elements. The main service contract addresses commercial deliverables, not data categories.
- **Risk tier**: 1.
- **Standard fix**: Populate Annex 1 with explicit fields: subject matter, duration, nature (operations), purpose (controller's purpose), data categories (with explicit Art. 9 / Art. 10 marker), data subject categories.

### D1.2 — Indefinite duration without termination mechanism

- **Pattern**: "This DPA shall continue for the duration of the Services" with no termination right independent of the main agreement.
- **Why it fails**: Art. 28(3) chapeau requires duration; in practice, the controller must be able to terminate processing if the processor materially breaches Art. 28 obligations even if the main service contract is hard to terminate.
- **Risk tier**: 2.
- **Standard fix**: Tie duration to main agreement BUT include independent termination right for material breach of this DPA, with cure period.

---

## Instructions ((a))

### D2.1 — "As may be necessary to provide the Services"

- **Pattern**: Processor processes "as may be necessary to provide the Services".
- **Why it fails**: This is not an instruction; it is a licence. It defeats the documentation requirement of (a) and the controller's continuing instruction-giving authority.
- **Risk tier**: 1 (controller-side); 3 (processor-side, where this is favorable).
- **Standard fix**: "The Processor shall process the Personal Data only on the documented instructions of the Controller, including those set out in this DPA, the Main Agreement, and such further written instructions as the Controller may issue from time to time."

### D2.2 — Service-improvement / analytics carve-outs

- **Pattern**: "Processor may use de-identified or aggregated data for service improvement, security analytics, benchmarking, or product development".
- **Why it fails**: These are processor purposes, not controller instructions. Under Art. 28(10), they likely make the processor a controller for that derived processing — which means an Art. 28 framing fails for that piece. Also: "de-identified" is not a defined GDPR concept; Art. 11 / Recital 26 anonymisation is a high bar rarely actually met.
- **Risk tier**: 1 if the carve-out is broad (processor-side power grab); 2 if narrow and specific (e.g. genuine threat-intelligence sharing for security purposes).
- **Standard fix**: Either (i) remove the carve-out entirely and require separate authorisation for any such use, or (ii) acknowledge the processor as a separate controller for that processing and require a clear lawful-basis assessment + transparency to data subjects.

### D2.3 — No carve-out for legally compelled processing

- **Pattern**: Strict instruction-only language with no provision for Union/Member State law compelling the processor.
- **Why it fails**: Art. 28(3)(a) explicitly preserves this carve-out *and* imposes a notification duty on the processor; missing this language leaves the processor in legal limbo and silences the notification right.
- **Risk tier**: 2.
- **Standard fix**: Reproduce the Art. 28(3)(a) carve-out and notification duty verbatim.

---

## Confidentiality ((b))

### D3.1 — "Reasonable confidentiality measures"

- **Pattern**: "Processor shall take reasonable measures to ensure confidentiality of personnel processing the Personal Data".
- **Why it fails**: Art. 28(3)(b) requires that authorised persons have **committed themselves** to confidentiality (or are under statutory obligation). "Measures to ensure" is one step removed and does not satisfy the personal commitment requirement.
- **Risk tier**: 2.
- **Standard fix**: "The Processor shall ensure that all persons authorised to process the Personal Data have committed themselves to confidentiality (e.g. through written confidentiality undertakings) or are under an appropriate statutory obligation of confidentiality, and that such confidentiality survives termination of their engagement with the Processor."

---

## Security and TOMs ((c))

### D4.1 — "Industry-standard security"

- **Pattern**: "Processor shall implement industry-standard security measures appropriate to the risk".
- **Why it fails**: Art. 32(1) requires specificity (a) pseudonymisation/encryption, (b) confidentiality/integrity/availability/resilience, (c) restoration, (d) regular testing. "Industry standard" is not measurable, not auditable.
- **Risk tier**: 1.
- **Standard fix**: Concrete TOMs in Annex 2 mapped to Art. 32(1)(a)–(d).

### D4.2 — TOMs locked at signing, no update mechanism

- **Pattern**: Annex 2 contains a TOMs list with no provision for changes; either party's attempt to update requires DPA amendment.
- **Why it fails**: Security is dynamic. Threats evolve; controls evolve. A DPA must accommodate evolution without becoming a one-off freeze-frame.
- **Risk tier**: 2.
- **Standard fix**: "The Processor may update the TOMs from time to time provided the level of security is not materially diminished. Material reductions require the Controller's prior written approval (not unreasonably withheld)."

### D4.3 — TOMs as "we have ISO 27001"

- **Pattern**: Annex 2 consists solely of "Processor maintains ISO/IEC 27001 certification".
- **Why it fails**: ISO 27001 is a management system standard and does not by itself satisfy Art. 32(1) specifics (e.g. encryption at rest is *not* mandated by 27001 but is expected under Art. 32 for many data types).
- **Risk tier**: 2.
- **Standard fix**: Use the ISO 27001 certification as supporting evidence; populate concrete Art. 32-specific TOMs separately.

---

## Sub-processors ((d), Art. 28(2), (4))

### D5.1 — Open-ended affiliates / service providers catch-all

- **Pattern**: "Processor may engage Affiliates and Service Providers to perform the Services."
- **Why it fails**: Art. 28(2) requires *specific* or *general* written authorisation. A catch-all without authorisation regime fails (2). Even framed as "general authorisation", it is missing notification + objection rights.
- **Risk tier**: 1.
- **Standard fix**: "The Controller hereby grants general authorisation for the engagement of Sub-processors listed in Annex 3. The Processor shall notify the Controller in writing at least [30] days before adding or replacing any Sub-processor. The Controller may object on reasonable grounds within [10] business days; if the Parties cannot resolve the objection, the Controller may terminate this DPA and the corresponding part of the Main Agreement on [30] days' notice without penalty."

### D5.2 — Notification to inactive inbox

- **Pattern**: Sub-processor notification to "legal@processor.com" with no acknowledgement requirement; controller bears burden of monitoring.
- **Why it fails**: Functionally toothless. Controller cannot meaningfully exercise objection right if it never sees the notification.
- **Risk tier**: 2.
- **Standard fix**: Notification to a controller-designated address, with a confirmation-of-receipt requirement; failure to confirm receipt restarts the notification period.

### D5.3 — Objection right with no consequence

- **Pattern**: "Controller may object to a new Sub-processor; the Processor will consider such objection in good faith."
- **Why it fails**: Objection without consequence is not a right. Either the objection blocks the engagement, or the controller may terminate without penalty — there must be teeth.
- **Risk tier**: 1.
- **Standard fix**: As D5.1 — termination right on unresolved objection.

### D5.4 — "Same level of protection" instead of "same data protection obligations"

- **Pattern**: Flow-down warranty stated as "Sub-processors shall be bound to provide a level of protection equivalent to that under this DPA".
- **Why it fails**: Art. 28(4) requires the *same* data protection *obligations* — not equivalent protection. The legal benchmark is the obligations themselves, not their effect.
- **Risk tier**: 3.
- **Standard fix**: "The Processor shall ensure that any Sub-processor is bound by data protection obligations no less stringent than those imposed on the Processor under this DPA, in particular providing sufficient guarantees to implement appropriate technical and organisational measures."

### D5.5 — Annex 3 empty despite known sub-processors

- **Pattern**: Annex 3 lists "None at signing"; processor's website lists 8 sub-processors.
- **Why it fails**: Art. 28(2) requires authorisation; an empty Annex 3 means the controller has not authorised the existing sub-processors.
- **Risk tier**: 1.
- **Standard fix**: Populate Annex 3 from processor's actual sub-processor list at signing.

---

## Data subject rights assistance ((e))

### D6.1 — Generic "reasonable assistance"

- **Pattern**: "Processor shall provide reasonable assistance to Controller in responding to data subject requests."
- **Why it fails**: Art. 28(3)(e) specifies "appropriate technical and organisational measures"; vague assistance language fails the specificity requirement and creates response-time disputes.
- **Risk tier**: 2.
- **Standard fix**: Specify (i) forwarding obligation, (ii) response timeline (e.g. within 5 business days of receipt), (iii) format of assistance (data extract, deletion confirmation, etc.), (iv) cost allocation.

### D6.2 — No forwarding obligation

- **Pattern**: Silence on what the processor does if a data subject contacts it directly.
- **Why it fails**: Without forwarding, processor may inadvertently respond substantively (overstepping its role) or fail to alert controller (depriving controller of ability to respond within Art. 12(3) one-month deadline).
- **Risk tier**: 2.
- **Standard fix**: "Where a data subject contacts the Processor directly with a request for the exercise of rights under Chapter III GDPR, the Processor shall forward the request to the Controller without undue delay and shall not respond substantively unless instructed by the Controller."

### D6.3 — All assistance chargeable

- **Pattern**: "All assistance with data subject requests shall be charged at Processor's then-current rates."
- **Why it fails**: Pure cost-shifting fights Art. 28(3)(e)'s intent. While reasonable cost recovery for non-trivial efforts is acceptable, blanket charging undermines the assistance obligation.
- **Risk tier**: 2 (controller-side); 3 (processor-side, often pushed back).
- **Standard fix**: Routine assistance included in service fees; non-routine effort (e.g. request volume above threshold, complex extractions) chargeable at agreed rates.

---

## Other compliance assistance ((f))

### D7.1 — Breach notification timeline weaker than 72 hours net

- **Pattern**: Processor notifies controller "without undue delay and in any event within 72 hours of becoming aware".
- **Why it fails**: Art. 33 GDPR requires controller to notify supervisory authority within 72 hours of *controller's awareness*. If processor uses the full 72 hours, controller has zero time. Best practice: processor's clock allows controller meaningful time to assess and notify.
- **Risk tier**: 1 (controller-side); 3 (processor-side, often pushed back to 48–72 hours).
- **Standard fix**: Processor notifies "without undue delay and in any event within [24] [48] hours of becoming aware". The information set tracks Art. 33(3) elements.

### D7.2 — "Suspected breach" not notifiable

- **Pattern**: Notification triggered only on confirmed breach.
- **Why it fails**: Controller may want early visibility on suspected incidents to preserve evidence and prepare contingency response.
- **Risk tier**: 3 (controller-side ask, often dropped in negotiation).
- **Standard fix**: Two-tier notification — early notice for credibly suspected incidents, plus updates as facts develop.

### D7.3 — DPIA assistance limited to "available information"

- **Pattern**: Processor assists with DPIA "based on information available to it".
- **Why it fails**: Some Art. 35 inputs are uniquely held by the processor (e.g. detailed processing flow, sub-processor architecture). Limiting to "available information" can mean "what the processor feels like sharing".
- **Risk tier**: 2.
- **Standard fix**: Processor provides information necessary for DPIA, including information uniquely within its knowledge, subject to confidential handling by controller.

---

## Deletion and return ((g))

### D8.1 — Default to deletion only

- **Pattern**: "Upon termination, Processor shall delete the Personal Data."
- **Why it fails**: Art. 28(3)(g) gives the *controller* the choice between deletion and return. Default-to-deletion strips that choice.
- **Risk tier**: 1.
- **Standard fix**: "Upon termination, at the Controller's choice exercised in writing within [30] days of termination, the Processor shall return all Personal Data to the Controller in a commonly used format OR delete all Personal Data, in each case including all copies."

### D8.2 — "Legitimate business purposes" retention

- **Pattern**: "Processor may retain Personal Data for legitimate business purposes after termination."
- **Why it fails**: Art. 28(3)(g) allows retention only where required by Union or Member State law. "Legitimate business purposes" is far broader.
- **Risk tier**: 1.
- **Standard fix**: Narrow retention exception to legal-obligation retention only, with specific identification of the law and retention period.

### D8.3 — Backup retention silently permanent

- **Pattern**: Silence on backup deletion; in practice, backups retained indefinitely.
- **Why it fails**: Backups contain personal data. Indefinite retention creates ongoing Art. 5(1)(e) compliance issue and undermines (g).
- **Risk tier**: 2.
- **Standard fix**: "Personal Data in backup systems shall be deleted upon expiry of the standard backup rotation period [specify, e.g. 90 days]; restored backups shall be re-deleted promptly. Until expiry, backups shall be access-restricted and not used for any other purpose."

### D8.4 — No deletion certification

- **Pattern**: Processor deletes without confirming to controller.
- **Why it fails**: Controller has no evidence of compliance for its own records and Art. 30 records of processing.
- **Risk tier**: 3.
- **Standard fix**: "Upon completion of deletion or return, the Processor shall provide written certification to the Controller."

---

## Audit rights ((h))

### D9.1 — Audit reduced to questionnaire

- **Pattern**: "Audit right" satisfied by processor responding to a written questionnaire annually.
- **Why it fails**: Art. 28(3)(h) requires the right to *audits, including inspections*. Questionnaire is information-on-demand, not audit.
- **Risk tier**: 1.
- **Standard fix**: Maintain on-site / remote inspection right, supplemented by routine information-on-demand.

### D9.2 — Third-party certifications as full substitute

- **Pattern**: "Controller's audit right is satisfied by Processor's provision of its current ISO 27001 / SOC 2 reports."
- **Why it fails**: Certifications are evidence of compliance, not a substitute for the audit right itself. Art. 28(3)(h) requires the *right*, even if rarely exercised.
- **Risk tier**: 2.
- **Standard fix**: "Certifications and audit reports shall constitute strong evidence of compliance and shall be the first-line audit mechanism. The Controller retains the right to conduct or mandate inspections (i) on reasonable cause shown, (ii) following a Personal Data Breach, or (iii) at the request of a competent supervisory authority."

### D9.3 — Notice period 90+ days

- **Pattern**: Audit requires 90 days' written notice.
- **Why it fails**: 90 days makes breach-triggered audit useless. Routine audits don't need 90 days either; 30 days is industry-typical.
- **Risk tier**: 2 (controller-side); 3 (processor-side, often holds at 30–60 days).
- **Standard fix**: 30 days for routine; "as soon as practicable" for breach-triggered.

### D9.4 — Cost-shifting onto controller for all audits

- **Pattern**: "Controller shall reimburse Processor's reasonable costs of any audit."
- **Why it fails**: Removes consequence of non-compliance. Where audit reveals material non-compliance, processor should bear costs.
- **Risk tier**: 2.
- **Standard fix**: Each party bears its own costs for routine audits; controller bears third-party-auditor cost; processor bears all costs (including controller's reasonable costs) if audit reveals material non-compliance with this DPA or applicable data protection law.

### D9.5 — Confidentiality obligation that prevents reporting to authorities

- **Pattern**: "Audit findings shall be subject to strict confidentiality and shall not be disclosed to any third party."
- **Why it fails**: Could prevent controller from disclosing findings to its supervisory authority — which would itself be a breach.
- **Risk tier**: 1.
- **Standard fix**: Confidentiality with explicit carve-out for disclosures required by law or to supervisory authorities.

---

## International transfers (Chapter V)

### D10.1 — "The Parties agree to use SCCs" without execution

- **Pattern**: DPA recites that the parties will rely on SCCs but does not attach them, identify the module, or fill the annexes.
- **Why it fails**: SCCs are an *executed* mechanism. A reference is not a transfer mechanism.
- **Risk tier**: 1.
- **Standard fix**: Either execute the SCCs separately (recommended) or attach them as annex with module identified and Annexes I.A/I.B/I.C/II/III filled.

### D10.2 — Wrong module

- **Pattern**: Module 2 (C-P) used where the relationship is actually controller-to-controller.
- **Why it fails**: Module mismatch invalidates the SCCs as a transfer mechanism for that flow.
- **Risk tier**: 1.
- **Standard fix**: Run the four-module decision in `references/sccs-module-guide.md`.

### D10.3 — DPF as sole basis without fallback

- **Pattern**: "Transfers to the US are based on Processor's certification under the EU-US Data Privacy Framework."
- **Why it fails**: Certifications can lapse; DPF itself faces challenges. A transfer mechanism that disappears overnight is fragile.
- **Risk tier**: 2.
- **Standard fix**: DPF as primary mechanism; SCCs as fallback ("If Processor's DPF certification ceases to be effective, the Parties shall execute SCCs Module [2/3] within [30] days, and Processor shall continue safeguards in the meantime.").

### D10.4 — Sub-processor SCCs missed

- **Pattern**: EU processor with non-EU sub-processor; SCCs executed only between controller and processor, not between processor and sub-processor.
- **Why it fails**: Each link in the chain needs its own transfer mechanism. Module 3 SCCs are needed for the processor-to-non-EU-sub-processor flow.
- **Risk tier**: 2.
- **Standard fix**: Processor warrants execution of Module 3 SCCs (or equivalent) with all non-EEA sub-processors; provides copies on request.

---

## Liability

### D11.1 — Liability cap below GDPR fine exposure

- **Pattern**: Processor's aggregate liability capped at 12 months' fees.
- **Why it fails**: Not a GDPR violation per se — but commercially: GDPR fines reach 4% of group turnover, dwarfing 12 months of fees on a typical SaaS contract. The controller carries the regulatory exposure unless the contract reallocates.
- **Risk tier**: 2 (controller-side); 3 (processor-side standard position).
- **Standard fix**: For high-risk processing, separate cap (or supercap) for data-protection liability, often 2–3× annual fees or a fixed amount, with carve-outs for gross negligence / wilful misconduct / breach of confidentiality.

### D11.2 — Indemnity excluding administrative fines

- **Pattern**: Processor indemnifies controller for "third-party claims" only, not for regulatory fines suffered by controller due to processor's breach.
- **Why it fails**: GDPR fines are imposed on controller; processor's breach of Art. 28 may directly cause them. Excluding them from indemnity strips the indemnity of substance.
- **Risk tier**: 2 (controller-side); 1 (processor-side, where this is industry-standard pushback).
- **Standard fix**: Indemnity covers third-party claims AND administrative fines AND data subject compensation claims to the extent caused by processor's breach.

---

## Term and termination

### D12.1 — No DPA-specific termination right

- **Pattern**: DPA termination tied entirely to main agreement; no independent right to terminate the DPA for material breach of Art. 28 obligations.
- **Why it fails**: If the main agreement is hard to exit (multi-year, with break fees), the controller is stuck with a non-compliant processor.
- **Risk tier**: 2.
- **Standard fix**: Independent termination right for material DPA breach with cure period; on termination, controller may also terminate corresponding portion of main agreement.

---

## Structural / hygiene

### D13.1 — Conflicting clauses across DPA and main agreement

- **Pattern**: Main agreement says "Provider may use Customer Data for analytics"; DPA says "Processor shall process only on Controller's instructions".
- **Why it fails**: Internal conflict; the more permissive language often controls in practice.
- **Risk tier**: 2.
- **Standard fix**: Order-of-precedence clause: in case of conflict between DPA and main agreement on data protection matters, the DPA prevails.

### D13.2 — Inconsistent DPA / SCC annexes

- **Pattern**: Annex 3 of DPA lists 6 sub-processors; Annex III of SCCs lists 4.
- **Why it fails**: One of them is wrong by definition.
- **Risk tier**: 2.
- **Standard fix**: Cross-incorporation — DPA annexes serve as SCC annexes, or vice versa.

### D13.3 — Click-through DPA presented as non-negotiable

- **Pattern**: SaaS provider's online DPA, accept-or-leave.
- **Why it fails**: Not a defect of the DPA itself (Art. 28(9) permits electronic form), but a negotiation reality. The DPA may be defective and the controller may have no leverage.
- **Risk tier**: Variable.
- **Standard fix**: Document residual risks; consider side letter to address most material gaps; for high-risk processing, escalate the choice of processor to senior decision-maker.

---

## How to use this list

For `REVIEW_NEG` and `REDLINE` modes, walk the counterparty draft against this list. For each defect identified:

1. Cite the defect by ID (D1.1, D2.1, etc.) for traceability.
2. Quote the specific defective wording from the draft.
3. Note risk tier.
4. Propose the standard fix wording (or a perspective-adjusted variant — see `references/negotiation-fallbacks.md`).

Sort the resulting issue list by risk tier (1 → 3) before presenting; never bury a tier-1 blocker behind tier-3 polish edits.
