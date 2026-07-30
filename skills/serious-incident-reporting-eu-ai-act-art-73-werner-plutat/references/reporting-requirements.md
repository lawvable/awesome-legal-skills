# Reporting Requirements Under Article 73

This reference translates **Article 73 EU AI Act** into an operational reporting checklist.

## 1. Who Must Report?

### Providers
Under **Article 73(1)**, providers of high-risk AI systems placed on the Union market must report any serious incident to the market surveillance authorities of the Member State where the incident occurred.

### Deployers
Deployers also matter operationally because **Article 26(5)** requires them to:

- immediately inform the provider first, then importer/distributor and the relevant market surveillance authority when they identify a serious incident
- suspend use where a live risk exists
- rely on Article 73 mutatis mutandis if the provider cannot be reached

## 2. To Whom?

### Main rule
Report to the **market surveillance authority of the Member State where the incident occurred**.

### Germany
Use **BNetzA** as the primary practical AI Act entry point in Germany, then check for sector-specific overlays.

### Austria
Confirm the competent national authority for the AI Act and the affected sector. Where time is short, do not delay fact-gathering while waiting for perfect routing certainty.

### Switzerland
Article 73 is an EU Member State reporting regime. Swiss-only incidents are not Article 73 notifications as such, but may still trigger contractual, product-safety, or data-protection duties and may matter for EU field-safety analysis.

## 3. When?

### Standard deadline - Article 73(2)
The report must be made:

- **immediately** after the provider has established a causal link or a reasonable likelihood of such a link; and
- **not later than 15 days** after the provider or, where applicable, the deployer becomes aware of the serious incident.

### Faster deadline - Article 73(3)
For:

- a **widespread infringement**, or
- a serious incident of the type in **Article 3(49)(b)**

report:

- immediately; and
- **not later than 2 days** after awareness.

### Death case - Article 73(4)
If the serious incident involves the **death of a person**:

- report immediately after causal relationship is established or as soon as it is suspected; and
- **not later than 10 days** after awareness.

## 4. Incomplete Initial Reports

Under **Article 73(5)**, an initial report may be incomplete if necessary to ensure timely reporting.

### Practical use
Send the first report on time with:

- system identifier
- provider details
- event summary
- harm summary
- awareness date
- preliminary causation view
- immediate containment actions
- note that investigation is ongoing and follow-up will be submitted

## 5. What Information Should Be Included?

There is no one perfect statutory template in the article text, so build a regulator-ready package.

### A. Provider details
- legal entity name
- address
- contact person and role
- phone/email
- authorised representative if relevant

### B. System details
- product/system name
- version/build/release date
- intended purpose
- high-risk classification basis
- CE marking / registration / technical file references if available
- deployment context and affected customer/deployer

### C. Incident details
- incident date/time
- awareness date/time
- Member State/location
- narrative chronology
- whether incident is ongoing or contained

### D. Harm details
- death / serious health damage / rights impact / critical infrastructure disruption
- number of affected persons or entities
- severity and current status
- whether vulnerable persons, workers, or public services were affected

### E. Causation and fault hypotheses
- established causal link / reasonable likelihood / under investigation
- suspected failure mode
- relevant inputs, overrides, or misuse
- role of human oversight

### F. Measures already taken
- suspension, rollback, access restriction
- deployer/customer warnings
- patch or hotfix
- additional human review
- evidence preservation

### G. Next steps
- investigation owner
- expected follow-up report date
- further corrective actions planned

## 6. Cross-Border Incidents

Use a simple routing logic:

- **Single-state harm** → notify that State
- **Multi-state harm** → map every affected Member State and determine whether parallel notifications are prudent
- **Central platform / distributed impact** → do not assume provider headquarters controls the reporting venue; focus on where the incident occurred and where harm materialised

## 7. Sector-Specific Overlays

### Medical devices / IVD
Under **Article 73(10)**, for high-risk AI systems that are safety components of devices, or are themselves devices, under MDR/IVDR, notification of serious incidents is limited to those in **Article 3(49)(c)** and goes to the designated national competent authority.

### Equivalent Union reporting regimes
Under **Article 73(9)**, if equivalent Union legislative reporting obligations apply to Annex III high-risk systems, AI Act serious incident notifications are limited to those in **Article 3(49)(c)**.

### Practical takeaway
Do not assume Article 73 disappears entirely. Instead, identify whether the AI Act notification scope is narrowed and what the parallel sector regime requires.

## 8. Suggested Internal Deadline Discipline

### Within 4 hours of awareness
- freeze evidence
- assign legal + product incident owner
- confirm high-risk classification status
- identify possible deadline bucket

### Within 24 hours
- complete initial qualification
- identify affected Member State(s)
- prepare draft initial notification
- decide whether deployers/customers must be informed immediately

### Within 48 hours
- send if the 2-day bucket applies
- otherwise be ready with at least an initial report if material facts are already clear

### Before day 10
- ensure death-related incidents are reported

### Before day 15
- ensure all standard-bucket incidents are reported even if the report is still partially incomplete

## 9. Suggested Wording for Deadline Conclusions

- **Report immediately; 2-day outer limit applies.**
- **Report immediately; 10-day outer limit applies due to fatality.**
- **Report immediately; 15-day outer limit applies.**
- **Serious incident threshold not yet met, but preserve evidence and reassess daily.**
