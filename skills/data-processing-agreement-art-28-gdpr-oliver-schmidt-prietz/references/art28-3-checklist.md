# Art. 28(3) GDPR — Canonical Checklist

This is the **source of truth** for what a DPA must contain. Every review and every draft is benchmarked against this file.

Article 28(3) GDPR sets out **two layers** of requirements:

1. **The chapeau** (introductory paragraph): the contract must set out the subject matter and duration of the processing, the nature and purpose of the processing, the type of personal data, the categories of data subjects, and the obligations and rights of the controller. These are usually placed in **Annex 1** of the DPA — but they must exist somewhere.
2. **Eight specific obligations** lit. (a) through (h): substantive duties of the processor.

A DPA missing any chapeau element OR any (a)–(h) obligation **fails Art. 28(3)** and is invalid as a processor agreement, regardless of how detailed the rest of the document is.

---

## Layer 1 — Chapeau elements

| # | Element | Where typically addressed | Must specify |
|---|---|---|---|
| C1 | Subject matter of the processing | Recitals / § 1 / Annex 1 | What service or activity gives rise to the processing (not the data type — the activity) |
| C2 | Duration of the processing | § Termination / Annex 1 | Tied to main service contract OR fixed term OR indefinite-with-termination-mechanism |
| C3 | Nature of the processing | Annex 1 | Operations performed (collection, storage, transmission, deletion, etc.) |
| C4 | Purpose of the processing | Annex 1 | Controller's purpose (NOT the processor's commercial purpose) |
| C5 | Type of personal data | Annex 1 | Data categories (identifiers, contact data, financial data, etc.); flag Art. 9 / Art. 10 separately |
| C6 | Categories of data subjects | Annex 1 | Employees, customers, prospects, end users, minors, etc. |
| C7 | Obligations and rights of the controller | Body + Annex 1 | At minimum: instruction-giving right, audit right, termination right, notification rights |

**Common defect**: Annex 1 reduced to a single line ("services as set out in the Master Agreement"). This fails C3, C4, C5, C6 simultaneously and is the single most frequent Art. 28(3) defect in commercial DPAs.

---

## Layer 2 — The eight obligations (a)–(h)

### (a) Documented instructions only

> "processes the personal data only on documented instructions from the controller, including with regard to transfers of personal data to a third country or an international organisation, unless required to do so by Union or Member State law to which the processor is subject; in such a case, the processor shall inform the controller of that legal requirement before processing, unless that law prohibits such information on important grounds of public interest"

**Mandatory drafting elements**:
- Processor processes only on **documented** instructions (the DPA itself is the foundational instruction).
- Mechanism for issuing further instructions (form, recipient, response time).
- Carve-out for processing required by Union / Member State law, with notification duty to the controller.
- Specific reference to **transfers** — instructions must cover them too.

**EN canonical phrasing**:
> "The Processor shall process the Personal Data only on the documented instructions of the Controller, including with regard to transfers of Personal Data to a third country or an international organisation, unless required to do so by Union or Member State law to which the Processor is subject; in such a case, the Processor shall inform the Controller of that legal requirement before the relevant processing, unless that law prohibits such information on important grounds of public interest."

**DE canonical phrasing**:
> "Der Auftragsverarbeiter verarbeitet die personenbezogenen Daten ausschließlich auf dokumentierte Weisung des Verantwortlichen, einschließlich in Bezug auf die Übermittlung personenbezogener Daten an ein Drittland oder eine internationale Organisation, sofern er hierzu nicht durch das Recht der Union oder der Mitgliedstaaten, dem er unterliegt, verpflichtet ist; in einem solchen Fall teilt der Auftragsverarbeiter dem Verantwortlichen diese rechtlichen Anforderungen vor der Verarbeitung mit, sofern das betreffende Recht eine solche Mitteilung nicht wegen eines wichtigen öffentlichen Interesses verbietet."

**Common defects**:
- Vague instruction wording ("as may be necessary to perform the services") — defeats documentation requirement.
- Processor unilaterally widens permitted purposes ("for service improvement", "for security analytics") — these are NOT instructions, they are processor purposes that may convert it into a controller (see Art. 28(10)).
- No notification duty on legally compelled processing.
- Silence on transfers — if the processor can transfer at its discretion, (a) is broken.

**Risk tier if missing/weak**: 1 (blocker)

---

### (b) Confidentiality of authorised persons

> "ensures that persons authorised to process the personal data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality"

**Mandatory drafting elements**:
- Confidentiality commitment (contractual undertaking) OR statutory confidentiality (e.g. professional secrecy).
- Applies to all persons authorised to process — includes employees AND contractors.
- Confidentiality survives termination of the employment / engagement.

**Common defects**:
- "Reasonable confidentiality measures" — too vague.
- Limited to employees only, missing contractors / agency staff.
- No survival clause.

**Risk tier**: 2 (material)

---

### (c) Security of processing (Art. 32)

> "takes all measures required pursuant to Article 32"

**Mandatory drafting elements**:
- Reference to Art. 32 measures (technical and organisational).
- **Concrete TOMs in Annex 2** — Art. 32 by reference is not enough; must specify pseudonymisation, encryption, confidentiality / integrity / availability / resilience, restoration, regular testing.
- Mechanism for updating TOMs (processor cannot unilaterally degrade; controller cannot unilaterally inflate without cost allocation).

**Common defects**:
- "Industry-standard security" with no specifics — fails Art. 32(1) which requires specificity.
- TOMs locked at signing with no update mechanism — security is dynamic.
- TOMs that map only to ISO 27001 controls without addressing Art. 32(1)(a) pseudonymisation/encryption explicitly.

**Risk tier**: 1 (blocker if Annex 2 empty/generic)

---

### (d) Sub-processors (engaging another processor)

> "respects the conditions referred to in paragraphs 2 and 4 for engaging another processor"

**Cross-references**:
- Art. 28(2): no sub-processor without prior **specific** or **general** written authorisation; if general, processor must inform of intended changes and give controller a chance to object.
- Art. 28(4): same data protection obligations flowed down to sub-processor, and processor remains fully liable.

**Mandatory drafting elements**:
- Authorisation regime stated explicitly: specific (per sub-processor) OR general (with notification + objection).
- If general: notification mechanism (form, recipient, lead time — typically 30 days), objection mechanism, consequences of objection (termination right, reasonable cooperation to find alternative).
- Flow-down obligation: processor warrants that sub-processor is bound by the same Art. 28(3) obligations.
- Processor's continuing liability for sub-processor's acts and omissions.
- **Annex 3 with current sub-processors at signing**.

**Common defects**:
- Open-ended sub-processor catch-all ("Processor may engage Affiliates and Service Providers") — fails Art. 28(2).
- No notification mechanism, or notification to a generic legal@ inbox without acknowledgement.
- Objection right with no consequence — controller objects, processor proceeds anyway.
- Missing flow-down warranty.
- Empty Annex 3 despite known sub-processors (CDN, hosting, support providers, analytics).
- "Same level of protection" instead of "same data protection obligations" — the latter is the GDPR standard.

**Risk tier**: 1 (blocker if no authorisation regime); 2 (material if regime weak)

---

### (e) Assistance with data subject rights

> "taking into account the nature of the processing, assists the controller by appropriate technical and organisational measures, insofar as this is possible, for the fulfilment of the controller's obligation to respond to requests for exercising the data subject's rights laid down in Chapter III"

**Mandatory drafting elements**:
- Assistance with all Chapter III rights: information (Art. 13/14), access (Art. 15), rectification (Art. 16), erasure (Art. 17), restriction (Art. 18), portability (Art. 20), objection (Art. 21), automated decision-making (Art. 22).
- Specific assistance mechanisms: how requests are forwarded, response times, format of assistance.
- Cost allocation: who bears the cost of assistance (controller-favorable: included in service; processor-favorable: time-and-materials beyond minor effort).
- Forwarding obligation: if data subject contacts processor directly, processor must forward without responding substantively (unless instructed).

**Common defects**:
- Generic "shall provide reasonable assistance" — what is reasonable, on what timeline?
- No forwarding obligation — processor may inadvertently respond to requests directed at controller.
- Cost shifting via "all assistance is chargeable" — fights Art. 28(3)(e) intent.

**Risk tier**: 2 (material); 1 (blocker if no assistance obligation at all)

---

### (f) Assistance with controller's other obligations (Art. 32–36)

> "assists the controller in ensuring compliance with the obligations pursuant to Articles 32 to 36 taking into account the nature of processing and the information available to the processor"

**Mandatory drafting elements**:
- Art. 32 (security of processing) — see (c).
- Art. 33 (notification of breach to supervisory authority) — processor must notify controller without undue delay; usually 24–72 hours specified, with information set required (Art. 33(3) elements).
- Art. 34 (communication of breach to data subjects) — processor assistance with data and content.
- Art. 35 (DPIA) — processor provides information necessary for DPIA.
- Art. 36 (prior consultation) — processor provides information for consultation with supervisory authority.

**Common defects**:
- Breach notification timeline weaker than 72 hours total (counting controller's response time) — leaves controller insufficient time to meet its own Art. 33 deadline. Best practice: processor notifies within 24–48 hours of becoming aware.
- "Suspected breach" notification not required — controller may want this for early warning.
- DPIA assistance limited to "available information" too narrowly — processor must be willing to gather information that only it has.
- Cost allocation overreach — assistance should not be a profit centre, but processor-favorable position is reasonable cost recovery for non-trivial efforts.

**Risk tier**: 1 (blocker for Art. 33 breach notification timeline); 2 (material for Art. 35–36)

---

### (g) Deletion or return at end of processing

> "at the choice of the controller, deletes or returns all the personal data to the controller after the end of the provision of services relating to processing, and deletes existing copies unless Union or Member State law requires storage of the personal data"

**Mandatory drafting elements**:
- **Choice belongs to the controller** — not the processor. Common defect: "Processor will delete unless Controller requests return" reverses the default.
- Deletion of all copies, including in backups (with reasonable retention period for backup rotation typical at 30–90 days, after which restored copies must be re-deleted).
- Carve-out for legal retention obligations — narrow, with specific reference to the law requiring retention and a reasonable period.
- Certification of deletion / return mechanism (written confirmation upon request).
- Timeline: typically 30–60 days from termination.

**Common defects**:
- Default to deletion only, no return option — controller cannot extract its data.
- Retention "for legitimate business purposes" — exceeds Art. 28(3)(g) which only allows legal-obligation retention.
- No certification.
- Backup retention silently permanent.

**Risk tier**: 1 (blocker if controller's choice not preserved); 2 (material if backup handling unclear)

---

### (h) Audits and inspections

> "makes available to the controller all information necessary to demonstrate compliance with the obligations laid down in this Article and allow for and contribute to audits, including inspections, conducted by the controller or another auditor mandated by the controller"

**Mandatory drafting elements**:
- Information-on-demand obligation: processor provides documentation sufficient to demonstrate Art. 28 compliance.
- Audit right: controller may audit OR mandate a third-party auditor.
- Frequency: typically 1× per year, plus ad hoc on reasonable cause (e.g. after a breach, regulatory request).
- Scope: limited to processing under this DPA; protection of confidential information of other customers; non-disruption of operations.
- Notice period: typically 30 days; reduced to "as soon as practicable" or zero days for breach-triggered audits.
- Cost allocation: typically each party bears its own costs for routine audits; controller bears third-party auditor cost; processor bears cost if audit reveals material non-compliance.
- **Acceptable substitutes**: third-party certifications (ISO 27001, SOC 2 Type II, ISAE 3000) and audit reports may satisfy information-on-demand obligation but cannot fully replace on-site audit right.

**Common defects**:
- "Audit right" reduced to written-questionnaire-only with 6-month response time — toothless.
- Third-party certifications presented as full substitute for audit right — paragraph (h) requires the right itself, even if rarely exercised.
- Notice periods of 90+ days for routine, with no breach-triggered exception.
- Cost-shifting onto controller for all audits including those triggered by demonstrated non-compliance.
- Confidentiality obligations on audit findings that prevent reporting to supervisory authorities.

**Risk tier**: 1 (blocker if audit right denied entirely); 2 (material if heavily restricted)

---

## Cross-cutting obligations (not (a)–(h) but mandated elsewhere)

### Art. 28(2) — sub-processor authorisation regime

See (d) above — but note this is a **separate** Art. 28 violation if no authorisation regime exists at all, even if (d) flow-down language is present.

### Art. 28(4) — flow-down

Sub-processor must be bound by **same data protection obligations as set out in the contract** between controller and processor, in particular providing sufficient guarantees to implement appropriate TOMs.

Drafting note: the cleanest way to satisfy Art. 28(4) is for the sub-processor agreement to incorporate by reference the controller-processor DPA's processor obligations.

### Art. 28(9) — written form

Contract or other legal act must be in writing, including in electronic form. Click-through DPAs are valid in principle if execution is auditable.

### Art. 28(10) — processor exceeding instructions

If processor processes outside the controller's instructions and determines purposes/means itself, it becomes a controller for that processing. Drafting note: include an explicit clause acknowledging this and disclaiming any intent for the processor to act as controller — useful in tail-risk scenarios.

---

## How to use this checklist

### For REVIEW_QUICK
Walk through C1–C7 and (a)–(h). Mark each PASS / WEAK / GAP / DEFECT. The output table mirrors this structure 1:1.

### For REVIEW_NEG
Same walk-through, but for each WEAK / GAP / DEFECT, consult `references/common-defects.md` and `references/negotiation-fallbacks.md` for the standard fix and tiered fallback positions.

### For DRAFT
The template files (`templates/dpa-commercial-{en,de}.md`, `templates/dpa-strict-{en,de}.md`, `templates/dpa-hybrid-{en,de}.md`) already implement all of the above for their respective tier. Validate the populated draft by walking through this checklist as a final quality gate, regardless of which tier was used.

### For REDLINE
Walk through this checklist against the counterparty's draft; every WEAK / GAP / DEFECT becomes a redline candidate. Sort the candidates by risk tier (1 → 3) before redlining — never put tier-3 polish edits ahead of tier-1 blockers.
