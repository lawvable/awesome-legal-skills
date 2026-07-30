# GDPR for Azerbaijani Websites — Audit Reference

Loaded when the audit reaches Step 1 (applicability determination) and Step 4 (GDPR findings) of the SKILL.md workflow.

## Source

- Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 (the "GDPR").
- EDPB Guidelines, in particular:
  - Guidelines 3/2018 on the territorial scope of the GDPR (Art. 3).
  - Guidelines 05/2020 on consent under Regulation 2016/679.
  - Guidelines 07/2020 on the concepts of controller and processor.
- *Planet49* (C-673/17, CJEU, 1 October 2019) — pre-ticked boxes are not valid consent.

## Step 1 — Is GDPR applicable to this AZ-based controller?

GDPR Art. 3 lays out two main bases on which a non-EU controller is caught.

### Art. 3(1) — Establishment in the EU

Does the AZ business have an "establishment" in the EU? An establishment exists where there is a stable arrangement to carry out economic activity, however minimal. A subsidiary, branch, sales representative on EU soil, or a person acting as a representative of the controller is enough. A bare server in the EU is generally not enough; a person doing business in the EU on behalf of the AZ entity generally is. If yes → GDPR applies to processing in the context of that establishment.

### Art. 3(2)(a) — Offering goods or services to data subjects in the EU

Audit signals that the site is offering goods or services to EU users:

- Prices listed in EUR or another EU member-state currency.
- Translation into an EU member-state language that is not also a local AZ language (so: Russian alone is ambiguous; German, French, Spanish, Italian, Polish, etc. are strong signals).
- Country selector that lists EU member states.
- Shipping to EU addresses, EU phone-number formatting, or domain extensions of EU member states.
- Marketing campaigns explicitly targeted at EU users (paid placement, EU influencer partnerships).
- Customer-facing content referring to EU consumers, GDPR, or "European customers".

Mere accessibility of the site from the EU is not enough. The test is "targeting".

### Art. 3(2)(b) — Monitoring behaviour of data subjects in the EU

Audit signals that the site is monitoring EU users:

- Analytics, advertising, or personalisation that tracks users while in the EU.
- Behavioural profiling for any purpose where the user is in the EU.
- Cookies set to support advertising networks operating in the EU.

This basis can apply even when the site is not "offering" anything for sale.

### Output of the applicability analysis

In the report, give a single sentence conclusion: GDPR **applies / does not apply / unclear pending facts**, with the article basis named. If unclear, list what facts would resolve it.

If GDPR does not apply, skip Step 4 entirely. The cookie/ePrivacy analysis (Step 5) may still apply if EU visitors land on the site.

## Step 4 — GDPR findings checklist

Use this checklist to populate the GDPR findings table. Each item is a row.

### Identity and accountability

- **Art. 13(1)(a)** — Identity and contact details of the controller (and, where applicable, the representative). The notice must give the legal entity, not just a brand.
- **Art. 27** — Where a non-EU controller is caught by Art. 3(2), it must appoint a representative established in the EU, with name and contact published. Missing Art. 27 representative for an AZ controller targeting EU users is **Red**.
- **Art. 37 / 13(1)(b)** — DPO contact, where appointed (mandatory in the cases listed in Art. 37(1); voluntary appointment also creates this disclosure obligation).

### Purposes and lawful basis

- **Art. 13(1)(c)** — Purposes of processing and the lawful basis under Art. 6 (and Art. 9(2) for special categories). Each purpose should be tied to a basis. Bundled "legitimate interests" without an identifiable interest is **Amber**.
- **Art. 13(1)(d)** — If the lawful basis is legitimate interests, the specific interests pursued by the controller (or a third party) must be stated.

### Recipients and transfers

- **Art. 13(1)(e)** — Recipients or categories of recipients of the personal data, including processors, sub-processors, and third parties.
- **Art. 13(1)(f) / Art. 46–49** — International transfer disclosures. If data leaves the EU/EEA (analytics, hosting, CRM, support, payment), the notice must identify the safeguard relied on (SCCs, BCRs, adequacy decision, or Art. 49 derogation). For transfers to AZ, no adequacy decision currently exists — flag accordingly.

### Retention

- **Art. 13(2)(a)** — Retention period or criteria. "As long as necessary" alone is **Yellow**. Specific periods per purpose are Green.

### Data subject rights

- **Art. 13(2)(b)** — Existence of the rights to access, rectification, erasure, restriction, objection, and portability. Each right must be named.
- **Art. 13(2)(c)** — Right to withdraw consent where consent is the basis.
- **Art. 13(2)(d)** — Right to lodge a complaint with a supervisory authority. The notice should at least mention the right; named authority is better.

### Source and obligations

- **Art. 13(2)(e)** — Whether providing the data is a statutory or contractual requirement and the consequences of not providing.
- **Art. 14** — Where data is obtained from a source other than the data subject, the additional disclosures in Art. 14 (especially the source) apply.

### Automated decision-making

- **Art. 13(2)(f) / Art. 22** — Existence of automated decision-making producing legal or similarly significant effects, meaningful information about the logic, and the significance and envisaged consequences. Missing this when the site clearly profiles users (credit decisions, dynamic pricing tied to identity, automated content moderation with consequences) is **Red**.

### Consent specifics

- **Art. 7 + EDPB 05/2020** — Where consent is the basis: freely given, specific, informed, unambiguous; demonstrable; granular per purpose; withdrawable as easily as given. For consent obtained through a cookie banner, the consent must be obtained before non-essential trackers fire.

### Security and breaches

- **Art. 32** — Security measures referenced in the notice (high-level is fine).
- **Arts. 33 and 34** — Breach notification process referenced. Site-level wording is usually short; a sentence saying breaches are notified to the supervisory authority and, where required, to data subjects, is sufficient.

### Records and DPIAs

- **Art. 30** — Cannot be assessed from the site. Note as `Unverified — request controller's Art. 30 record`.
- **Art. 35** — Same. Note as `Unverified — request controller's DPIA register`.

## Common Red-grade findings for AZ controllers under GDPR

These are the recurring issues to look for first:

1. No Art. 27 EU representative appointed despite Art. 3(2)(a) targeting.
2. Cookies/trackers fire on first page load before consent is obtained.
3. International transfers stated as "we may share with service providers worldwide" with no safeguard identified.
4. Lawful basis listed as "your consent" for cookies set automatically, including strictly-necessary ones, betraying confusion about the consent framework.
5. Special-category data (health, biometrics) collected with no Art. 9 basis identified.
6. Single-button "Got it" cookie banner with no "Reject" parallel.
