# Cross-Border Transfers — Audit Reference

Loaded when the audit reaches Step 6 (Cross-border transfers) of the SKILL.md workflow.

A website that uses any of the following is almost certainly transferring personal data across borders, in one direction or the other:

- Cloud hosting (AWS, Google Cloud, Azure, Hetzner, OVH, Yandex Cloud, etc.).
- Analytics (Google Analytics, Yandex Metrica, Matomo Cloud, Mixpanel, Amplitude).
- Customer support tools (Intercom, Zendesk, Freshdesk).
- Email or CRM (Mailchimp, SendGrid, HubSpot, Salesforce, AmoCRM).
- Payment processors (Stripe, Adyen, local AZ banks' gateways).
- Advertising and social media pixels (Meta, Google Ads, TikTok, LinkedIn).

The audit must cover both legs.

## Leg 1 — Outbound from Azerbaijan (Law No. 998-IIIQ)

### Rule

Cross-border transfer of personal data from Azerbaijan is permitted if the destination jurisdiction provides an adequate level of protection, or on grounds recognised by the law (typically: explicit consent of the data subject, performance of a contract with the data subject, compliance with a legal obligation, vital interests, or other statutorily permitted grounds).

### Convention 108

Azerbaijan is a party to Council of Europe Convention 108 (and the Additional Protocol). Transfers to other Convention 108 parties are generally treated as transfers to a jurisdiction with an adequate framework. Convention 108 parties as of the knowledge cutoff include all Council of Europe member states (notably the EU member states, the UK, Turkey, Norway, Iceland, Switzerland), plus several non-European states (Argentina, Uruguay, Mexico, Senegal, Mauritius, Morocco, Tunisia, Cabo Verde, and others). For an up-to-date list, refer the user to the Council of Europe treaty office; do not assert a current list in the audit report without verification.

### Audit checkpoints

- Does the notice identify each cross-border recipient or category of recipient and the destination country?
- For each destination, what is the basis for the transfer (consent / Convention 108 adequacy / other)?
- If consent is the basis, was it informed (specifically identifying the destination and the consequences)?
- For transfers to the United States: as of the knowledge cutoff, the US is not a party to Convention 108, and AZ has no formal adequacy assessment for the US. Transfers to US-based processors (very common for analytics and hosting) should rely on consent or another recognised ground. The EU-US Data Privacy Framework does not apply to AZ-out transfers; it applies only to EU-out transfers.
- For transfers to Russia, Turkey, EU member states, UK, China, India: assess each based on Convention 108 status and any sectoral arrangements. Do not assert current adequacy without verification.

Score gaps as **Red** if a cross-border transfer is plainly happening (e.g., Google Analytics is loaded) and the notice gives no destination or basis.

## Leg 2 — Outbound from EU/EEA to Azerbaijan (GDPR Chapter V)

This leg applies when the AZ-based controller or processor receives personal data from an EU-based source — typically when EU users register on the site and their data is sent to AZ for processing, or when the AZ controller engages an EU processor whose output flows back to AZ.

### Rule

Transfer of personal data from the EU/EEA to a third country requires either an adequacy decision under Art. 45, appropriate safeguards under Art. 46 (Standard Contractual Clauses, Binding Corporate Rules, codes of conduct, certifications), or a derogation under Art. 49.

### Adequacy

As of the knowledge cutoff, the European Commission has **not** issued an adequacy decision for Azerbaijan. Therefore Art. 45 is not available. The audit should not assert otherwise unless the user provides a Commission decision reference.

### Standard Contractual Clauses (SCCs)

The current SCCs are the **2021 modular SCCs** (Commission Implementing Decision (EU) 2021/914 of 4 June 2021). The legacy 2010/87/EU and 2001/497/EC sets are no longer valid for new contracts. Audit checkpoints:

- Are SCCs in place between the EU exporter and the AZ importer?
- Are the correct modules selected (controller-to-controller, controller-to-processor, processor-to-processor, processor-to-controller)?
- Have docking clauses been used where there are multiple parties?
- Has a Transfer Impact Assessment (TIA) been performed per the *Schrems II* judgment (C-311/18) and EDPB Recommendations 01/2020?
- Are supplementary technical, contractual, and organisational measures in place where the TIA identified issues?

You generally cannot verify these from the website alone. Score as `Unverified — request the EU-exporter's transfer documentation`. If the notice does not even mention SCCs while a transfer plainly occurs, score **Red** for the disclosure deficiency.

### Derogations

Art. 49 derogations (explicit consent, contract necessity, important public interest, legal claims) are interpreted narrowly per EDPB Guidelines 2/2018. They are not a substitute for systematic SCC-based transfer programmes.

### Sub-processors

If the AZ controller uses sub-processors located in further third countries (very common when the AZ controller uses, e.g., a US-based SaaS that has its own sub-processors in India and Singapore), the SCCs must be flowed down and each onward transfer must have its own basis. Score as `Unverified` unless the user provides the sub-processor list.

## Audit-table layout for Step 6

A two-table layout works best:

```
### Outbound from AZ (Law No. 998-IIIQ)

| Recipient / category | Destination | Basis stated | Status |
| --- | --- | --- | --- |
| Google Analytics | United States | None stated | Red |
| Hosting (Hetzner) | Germany | Convention 108 adequacy implicit | Amber — explicit disclosure required |

### Outbound from EU/EEA to AZ (GDPR Chapter V)

| Flow | Mechanism (Art. 45 / 46 / 49) | Status |
| --- | --- | --- |
| EU user account data to AZ controller | SCCs (2021) — verify TIA | Unverified |
```

Fill in only the rows the user's site actually has. Do not pad with hypothetical rows.

## What the user should walk away with

After Step 6, the user should know:

1. Which specific cross-border flows are happening (named).
2. Whether each has a stated and plausible legal basis.
3. Which flows need documentation (SCCs, TIA, consent records) that the auditor could not see from the website alone.

Recommend in Step 9 (Prioritised remediation) that the user produce a data-mapping exercise covering every third-party recipient and its destination, if no such mapping is referenced in the materials provided.
