# Azerbaijani Law on Personal Data No. 998-IIIQ — Audit Reference

This file is loaded when the audit reaches Step 3 (AZ Law findings) or Step 1 (scoping) of the SKILL.md workflow. It is **not** a textbook of the law — it is a working checklist for website audits, with the article anchors needed to fill the findings table.

## Source

- Statute: Law of the Republic of Azerbaijan No. 998-IIIQ "On Personal Data", adopted 11 May 2010, with subsequent amendments.
- Subordinate acts: Cabinet of Ministers Decrees implementing the State Register of personal data information systems and the categories of personal data information systems.
- Related instrument: Council of Europe Convention 108 (1981) and Protocol CETS 223 ("Convention 108+"). Azerbaijan is a party to Convention 108.
- Sectoral overlays not covered here: electronic communications law, banking secrecy, health data sectoral rules, AML/CFT. Flag if relevant but do not score them under this skill.

If you cite an article number in the audit report, you must be confident it is the correct article in the **current** consolidated text. If you are not certain of the exact pinpoint, write "Law No. 998-IIIQ, provision on [topic]" instead of guessing. See the anti-hallucination rules in SKILL.md.

## Core requirements to audit

Use this as the spine of the AZ Law findings table in Step 3. Each entry includes the requirement, what to look for on the site, and how to score it.

### 1. Legal basis for processing

- **Requirement.** Personal data may be processed only on a legal basis recognised by the law — typically the data subject's consent, performance of a contract to which the subject is a party, compliance with a legal obligation of the controller (operator), protection of vital interests, or another statutorily permitted ground.
- **Audit checkpoint.** The privacy notice should state the legal basis for each processing purpose. A blanket "we process your data with your consent" without distinguishing purposes is **Amber**.
- **Red flag.** Processing of biometric, health, criminal-record, religious, ethnic, or sex-life data without an explicit basis for the sensitive category.

### 2. Categories of personal data and definitions

- **Requirement.** The law distinguishes ordinary personal data from "special category" data (sensitive). Special-category data includes data revealing racial or ethnic origin, religious or philosophical beliefs, health, sex life, criminal-record data, and biometric data.
- **Audit checkpoint.** If the site collects any of these (account photo used for ID, fitness data, KYC liveness check, religious community sign-up), the notice should identify the category and the applicable legal ground.

### 3. Information to be provided to the data subject

The privacy notice should disclose, at minimum:

- Identity and contact details of the operator (controller).
- Purposes of processing, separately stated.
- Categories of personal data processed.
- Recipients or categories of recipients, including processors and any cross-border recipients.
- Retention periods or the criteria to determine them.
- Rights of the data subject and how to exercise them.
- Whether the data is collected directly or from third parties, and from where.
- Whether automated decision-making, including profiling, takes place.

Missing items go in the findings table individually — do not collapse them into one "incomplete notice" row.

### 4. Data subject rights

Audit that the notice names and provides a working channel for each of:

- Right to be informed.
- Right of access to one's own data.
- Right to rectification of inaccurate data.
- Right to deletion / erasure of data processed unlawfully or no longer needed.
- Right to block (suspend) processing on stated grounds.
- Right to object to processing in defined situations.
- Right to withdraw consent at any time, where consent is the basis.

"Working channel" means a specific email address, postal address, or in-product form. "Contact us" with no method is **Amber**. No channel at all is **Red**.

### 5. Consent

- **Form.** Consent must be informed, specific, and freely given. Where consent is the basis, the operator bears the burden of proof.
- **Audit checkpoint.** If the site relies on consent (most do for marketing and non-essential cookies), check that:
  - The consent action is unambiguous (an active step, not pre-ticked).
  - Each purpose has its own consent or the bundled consent is justified.
  - Withdrawal is as easy as granting.
  - A consent record is implied (you cannot verify the back-end from the site alone — note this as `Unverified`).
- Consent of a minor: where the data subject is under 18, parental or guardian consent is generally required. If the site is plausibly used by minors and has no age gate, mark **Red**.

### 6. Security of processing

- **Requirement.** The operator must take organisational and technical measures to protect personal data against unauthorised access, alteration, disclosure, loss, or destruction.
- **Audit checkpoint.** The notice should at least state that the operator implements such measures. Specifics (encryption in transit, access controls, staff training) earn a higher score. Silence is **Amber**.

### 7. Operator obligations and registration

- See `az_operator_registration.md`. Score registration status separately in Step 8 of the audit.

### 8. Cross-border transfer

- See `cross_border_transfers.md` (outbound-from-AZ section).

### 9. Breach notification

- The current Law and implementing acts contemplate notification of incidents to the competent authority within defined timeframes for certain categories of information systems. The exact deadline depends on the system category. Do not assert a specific number of hours unless the user provides the controller's system-category determination. Score as **Yellow** if the notice mentions a breach-response process and **Amber/Red** if there is none and the controller appears to operate a registrable system.

### 10. Processor relations

- The law recognises that processing may be entrusted to a third party, in which case the operator remains responsible and a written agreement should be in place.
- **Audit checkpoint.** The site cannot show you contracts, but the notice should at least identify categories of processors (hosting, analytics, payment, customer support). Naming none and clearly using third-party services is **Amber**.

### 11. Controller identification

- **Audit checkpoint.** The legal entity name (in Azerbaijani and, ideally, transliterated), the registered address, and a contact address must be findable on the site — typically in the privacy notice or the imprint. A trading name only, with no legal entity, is **Red** for the AZ Law's identification requirement and also for GDPR Art. 13(1)(a) where applicable.

## Scoring quick guide for AZ Law findings

| Symptom | Default score |
| --- | --- |
| Provision present, accurate, and complete | Green |
| Provision present but generic ("we process your data lawfully") | Amber |
| Provision missing in a notice the user has shown you | Red |
| Cannot determine from the materials provided | `Unverified` |
| Topic does not apply (e.g., children, biometrics, automated decisions not used) | Grey |

## What this reference does not cover

- Employment-context data processing (separate sectoral rules).
- Health data in the medical-records sense (separate sectoral rules).
- AML/CFT obligations that may compel processing.
- Telecommunications metadata.

If the audit touches these areas, flag them and recommend specialist review rather than scoring under this skill.
