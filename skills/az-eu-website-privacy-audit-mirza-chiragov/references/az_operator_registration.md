# AZ Operator Registration — Audit Reference

Loaded when the audit reaches the "Operator registration assessment (AZ)" section of the report (Step 8 in the SKILL.md workflow).

## What this is

Under Law No. 998-IIIQ, operators of certain categories of personal data information systems must register the system in the **State Register of personal data information systems** maintained by the competent Azerbaijani authority. Categories of information systems are defined by subordinate regulation (Cabinet of Ministers decree).

Because the regulatory architecture has been reorganised (the registration function has moved between agencies over time), refer in the audit report to "the competent Azerbaijani authority" and note "verify current name with the user / Ministry of Digital Development and Transport". Do not invent or assert a specific current agency name unless the user provides it.

## Why this matters for a website audit

Most commercial websites that collect personal data through forms, accounts, KYC flows, or analytics tied to identifiable users are operating an information system in the regulatory sense. The audit therefore needs to determine, at minimum:

1. Whether the user's processing is plausibly covered by registration requirements.
2. Whether the privacy notice references the operator's registration status (system category, registration number, or analogous identifier).
3. Whether the controller has the basic record-keeping that registration presupposes.

You cannot definitively confirm registration from the site alone — confirmation requires a check against the State Register. State that limitation explicitly in the report.

## Audit checkpoints

### Likely-registrable indicators

Increase the likelihood the user must register if **any** of these are true:

- The site has user accounts (login/password).
- KYC, identity verification, or onboarding for regulated activity (financial services, telecom, ride-hailing, marketplaces with payouts).
- Health, biometric, or other special-category data is collected.
- Children under 18 are a foreseeable user group.
- The processing is at non-trivial scale (mass-market consumer site, cross-border traffic, marketing database).
- Cross-border data transfer is part of the normal operation.

If three or more of these are present, score the registration question as **Likely required — verify with the State Register**.

### Lower-risk indicators

Decrease the likelihood if **all** of these are true:

- The site is a static informational page with no forms, no accounts, and no analytics tied to identifiable users.
- Contact is via a non-identifying channel (general phone number, mailing address).
- No cross-border processing.

Even then, do not assert "registration not required" — note the assessment as **Possibly not required — verify with counsel**.

### Site signals to look for

- A statement in the privacy notice that the controller is registered in the State Register, with a system identifier.
- A separate "Information about personal data processing" page that mirrors the disclosures registrations typically include.
- The Azerbaijani-language version of the policy is often more complete than the English version for this disclosure. Compare them.

## Findings-table entries to produce in the audit

In Step 8 of the report, produce a small table:

| Question | Finding | Status |
| --- | --- | --- |
| Does the site's processing fall within categories of information systems requiring registration? | Likely / Possibly / Unlikely / Unverified | — |
| Does the privacy notice reference registration? | Yes / No | Green / Amber / Red |
| Is the controller's legal identity disclosed sufficiently to permit registration verification? | Yes / No | Green / Red |

End with a single sentence recommending whether the user should verify registration status with the competent authority before going further.

## What you do not do here

- Do not advise on the actual application procedure, fees, or timelines for registration — those are outside the assessment scope.
- Do not assert that the user is or is not currently registered.
- Do not name the current regulator with certainty (architecture has changed).
