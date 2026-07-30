# GDPR — Clause Checklist

General Data Protection Regulation (EU) 2016/679. Enforced from 25 May 2018.
Fines: up to €20M or 4% global turnover (Art. 83(5)).

---

## Art. 5 — Principles (Check All Documents)

| Principle | What to check |
|-----------|--------------|
| Lawfulness, fairness, transparency | Lawful basis stated? Privacy notice clear? |
| Purpose limitation | Purpose defined narrowly? Re-use covered? |
| Data minimisation | Only necessary data collected? |
| Accuracy | Mechanism to correct/update? |
| Storage limitation | Retention period defined? |
| Integrity & confidentiality | Security measures described? |
| Accountability | Controller can demonstrate compliance? |

Suspect: Document asserts principles without operational mechanisms — ⚠️

---

## Art. 6 — Lawful Basis

Must identify ONE valid basis:
- [ ] **Consent** (Art. 6(1)(a)) → must satisfy Art. 7
- [ ] **Contract** (Art. 6(1)(b)) → must be necessary for performance
- [ ] **Legal obligation** (Art. 6(1)(c))
- [ ] **Vital interests** (Art. 6(1)(d))
- [ ] **Public task** (Art. 6(1)(e))
- [ ] **Legitimate interests** (Art. 6(1)(f)) → must include balancing test; not available for public authorities

Suspect patterns:
- Multiple bases listed without specifying which applies to which processing — ⚠️
- Legitimate interests claimed without balancing test / LIA documented — ⚠️
- "Contractual necessity" claimed for analytics/marketing — 🔴

---

## Art. 7 — Conditions for Consent

- [ ] Freely given (not bundled with service terms unless strictly necessary)
- [ ] Specific (per purpose)
- [ ] Informed (linked to privacy notice)
- [ ] Unambiguous indication (no pre-ticked boxes)
- [ ] As easy to withdraw as to give
- [ ] Records of consent maintained

Suspect: "By continuing to use this service you consent..." — 🔴
Suspect: Withdrawal requires written request / account deletion — 🔴

---

## Art. 8 — Children's Consent

- [ ] Age of digital consent: 16 (or lower if Member State law, min 13)
- [ ] Verifiable parental consent for under-16 processing
- Suspect: Age verified only by self-declaration — ⚠️

---

## Art. 9 — Special Category Data (Highest Risk)

Automatic HIGH risk flag for:
- Racial/ethnic origin, political opinions, religious beliefs, trade union membership
- Genetic data, biometric data (for ID purposes)
- Health data, sex life / sexual orientation

Requires:
- [ ] **Explicit** consent (Art. 9(2)(a)), or other Art. 9(2) basis
- [ ] Separate, prominent consent mechanism
- Suspect: Processed under "legitimate interests" — 🔴 (not a valid Art. 9 basis)
- Suspect: Mixed with ordinary personal data without separate treatment — ⚠️

---

## Art. 10 — Criminal Conviction Data

- [ ] Only processed under official authority or with suitable safeguards
- Suspect: Background check clause with no safeguard / legal basis — 🔴

---

## Art. 13/14 — Transparency (Privacy Notice Checks)

For data collected directly (Art. 13) or indirectly (Art. 14), notice must include:
- [ ] Controller identity + contact
- [ ] DPO contact (if applicable)
- [ ] Purposes + lawful basis
- [ ] Legitimate interests (if relied on)
- [ ] Recipients / categories of recipients
- [ ] Third country transfers + safeguards
- [ ] Retention period or criteria
- [ ] All data subject rights
- [ ] Right to withdraw consent
- [ ] Right to lodge complaint with supervisory authority
- [ ] Whether provision is statutory/contractual + consequences of not providing

Suspect: Notice exists but omits 3+ required elements — ⚠️
Suspect: Notice inaccessible, not linked at point of collection — ⚠️

---

## Art. 15-22 — Data Subject Rights

| Right | Art. | Mechanism required? |
|-------|------|---------------------|
| Access | 15 | Yes — response within 1 month |
| Rectification | 16 | Yes |
| Erasure ("Right to be forgotten") | 17 | Yes — with exceptions |
| Restriction | 18 | Yes |
| Data portability | 20 | Yes (if consent or contract basis + automated processing) |
| Object | 21 | Yes — especially to direct marketing (absolute right) |
| Not subject to automated decision-making | 22 | Yes |

Suspect: Rights listed but no operational mechanism (email/form/portal) — ⚠️
Suspect: Response time exceeds 1 month without mentioning extension right — 🔴
Suspect: Right to object to direct marketing not mentioned — 🔴

---

## Art. 28 — Data Processor Agreements (DPA)

Controller-Processor contracts MUST include:
- [ ] Process only on documented instructions
- [ ] Confidentiality obligations on staff
- [ ] Appropriate security (Art. 32)
- [ ] Sub-processor requirements (prior written consent)
- [ ] Assist controller with data subject rights
- [ ] Assist with security, breach notification, DPIA
- [ ] Delete/return data at end of engagement
- [ ] Provide audit assistance

Suspect: DPA clause exists but missing 3+ required elements — ⚠️
Suspect: Processor given right to use data for its own purposes — 🔴
Suspect: Sub-processor approval is blanket/pre-given without list — ⚠️

---

## Art. 32 — Security

- [ ] Pseudonymisation / encryption where appropriate
- [ ] Ability to restore availability (resilience)
- [ ] Regular testing of security measures
- [ ] Risk-appropriate measures (consider nature, scope, context, likelihood of harm)

Suspect: "Industry standard security" with no specifics — ⚠️
Suspect: No mention of encryption for sensitive data — ⚠️

---

## Art. 33/34 — Breach Notification

- [ ] Notify supervisory authority within **72 hours** of becoming aware (Art. 33)
- [ ] Notify data subjects without undue delay if high risk (Art. 34)
- [ ] Notification to contain: nature, categories/approx. number affected, DPO contact, likely consequences, remediation measures

Suspect: Notification obligation only to "material" breaches — ⚠️
Suspect: 72-hour timeline not reflected — 🔴
Suspect: No obligation to notify data subjects — 🔴

---

## Art. 35 — DPIA

Required for high-risk processing (systematic profiling, large-scale special category, systematic monitoring of public areas):
- [ ] DPIA conducted before processing starts
- [ ] Consult supervisory authority if residual risk high (Art. 36)

Suspect: High-risk processing described but no DPIA mentioned — ⚠️

---

## Art. 37-39 — DPO

Required if: public authority, large-scale systematic monitoring, large-scale special category processing:
- [ ] DPO designated and contact published
- [ ] DPO independent, expert in data protection law
- [ ] DPO accessible to data subjects

---

## Art. 44-49 — International Transfers

Transfers outside EEA only if:
- [ ] **Adequacy decision** (Art. 45) — approved countries include UK, Japan, India (pending), etc.
- [ ] **Standard Contractual Clauses** (SCCs) (Art. 46(2)(c)) — 2021 SCCs required
- [ ] **Binding Corporate Rules** (Art. 47)
- [ ] Other Art. 46 safeguards

Suspect: Transfer to non-adequate country with no SCCs / BCRs — 🔴
Suspect: Old (pre-2021) SCCs referenced — ⚠️
Suspect: Blanket "worldwide" transfer with no mechanism — 🔴
