# Cross-Regulation Mapping

Article 73 incident handling should almost never be done in isolation. Use this reference to map overlapping obligations.

## 1. GDPR

### Trigger questions
- Was personal data involved?
- Was there a confidentiality, integrity, or availability issue?
- Did the AI incident lead to unlawful or materially wrong decisions about individuals?
- Are special-category data involved?

### Likely overlap
- **Article 33 GDPR** supervisory authority notification for personal data breaches
- **Article 34 GDPR** communication to affected individuals where high risk exists
- **Article 35 GDPR** DPIA reassessment where the incident shows under-identified risk

### Practical note
An AI output failure is not automatically a personal data breach. But many AI incidents include logging leakage, misrouting, overexposure, data corruption, or unlawful inference that triggers GDPR analysis.

## 2. NIS2 / Cyber Incident Regimes

### Trigger questions
- Is the affected entity covered by NIS2 implementation law?
- Did the incident impact the availability, authenticity, integrity, or confidentiality of systems/data?
- Did an adversary or security flaw contribute?
- Is there operational disruption in essential services or critical infrastructure?

### Practical note
An AI incident can be both a safety/fundamental-rights issue and a cyber incident. Do not let legal teams and security teams work on separate clocks without coordination.

## 3. MDR / IVDR

### Relevant where
- the AI system is a medical device or IVD
- the AI system is a safety component of such a device/workflow

### Article 73 interaction
Under **Article 73(10)**, AI Act reporting is narrowed for those systems and notification goes to the designated national competent authority.

### Practical note
Use one integrated fact pack for both AI Act and MDR/IVDR analysis. The facts should not fork into conflicting timelines.

## 4. Machinery / Product Safety

### Relevant where
- the AI system is part of machinery or another regulated product
- there is physical safety impact, damage, or recall potential

### Practical note
Incident handling may need to align with product-safety corrective actions such as recall, withdrawal, customer notices, or stop-use instructions.

## 5. Employment / Labour / Works Council

### Relevant where
- the system is used in hiring, promotion, performance monitoring, access control, rostering, or workplace surveillance
- workers are affected by incident or field correction

### Germany-specific note
Consider **BetrVG** co-determination/information issues, especially where technical systems monitor behaviour/performance or materially affect personnel decisions.

## 6. Contractual Notice Duties

Check whether the customer contract requires notice of:

- security incidents
- service degradation
- regulatory investigations
- safety issues
- model changes or suspension

These duties often run faster than a formal legal conclusion.

## 7. Insurance and Governance

Ask whether the event must be escalated to:

- cyber insurer
- product liability insurer
- D&O insurer
- audit committee / board
- designated compliance committee

## 8. Simple Notification Matrix

| Regime | Core trigger | Typical clock | Owner |
|---|---|---:|---|
| EU AI Act Art. 73 | serious incident involving high-risk AI | immediate; 2/10/15-day outer limit | legal + product |
| Art. 26(5) deployer | serious incident or risk observed by deployer | immediate / without undue delay | deployer ops + legal |
| GDPR Art. 33 | personal data breach | 72 hours | privacy + security |
| GDPR Art. 34 | high risk to individuals | without undue delay | privacy + comms |
| NIS2 national law | significant cyber/operational incident | varies by national law | security + legal |
| MDR/IVDR vigilance | device-related serious incident | sector-specific | RA/QA + legal |
| Product safety | unsafe product risk | varies | product safety + legal |

## 9. Practical Rule

Create **one fact record**, then branch to multiple legal conclusions. Do not run separate factual investigations for AI Act, GDPR, NIS2, and product safety unless absolutely necessary.
