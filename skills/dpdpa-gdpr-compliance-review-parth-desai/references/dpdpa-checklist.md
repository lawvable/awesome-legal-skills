# DPDPA 2023 — Clause Checklist

Digital Personal Data Protection Act 2023 (India). In force from notified date.
Key enforcer: Data Protection Board of India (DPBI).

---

## §6 — Notice (Consent Request)

**Required elements in notice:**
- [ ] Identity of Data Fiduciary
- [ ] Categories of personal data to be collected
- [ ] Purpose of processing, in clear plain language
- [ ] How to withdraw consent (must be as easy as giving it)
- [ ] How to exercise rights (§11–§14)
- [ ] Contact for Grievance Officer

**Suspect patterns:**
- Vague purpose: "for business purposes", "to improve services" — flag as ⚠️
- Bundled consent (consent tied to service use with no opt-out) — flag as 🔴
- No withdrawal mechanism described — flag as 🔴

---

## §7 — Legitimate Uses (Processing without Consent)

Lawful without consent only for:
- State / government functions
- Compliance with law or court order
- Medical emergency / epidemic
- Employment-related necessity (limited)
- Mergers / acquisitions under law

**Suspect patterns:**
- Commercial entities claiming §7 for routine processing — flag as 🔴
- "Legitimate interest" language (GDPR concept) used in DPDPA context — flag as ⚠️ (not a valid DPDPA basis)

---

## §8 — Obligations of Data Fiduciary

### §8(1) — Accuracy
- [ ] Must ensure data is accurate and complete for its purpose

### §8(2)–(3) — Data Processors
- [ ] Written contract with Data Processor required
- [ ] Processor may only act on Fiduciary's instructions
- Suspect: Processor contract missing or processor given discretionary data use rights — 🔴

### §8(5) — Security Safeguards
- [ ] Reasonable security measures must be described or referenced
- Suspect: No security clause / bare mention with no specifics — ⚠️

### §8(6) — Breach Notification
- [ ] Must notify DPBI and affected Data Principals of breach
- [ ] No defined timeline in the Act (rules to prescribe) — check Rules when notified
- Suspect: Notification limited to "material" or "significant" breaches only — ⚠️

### §8(7) — Retention / Erasure
- [ ] Must erase data when purpose is fulfilled or consent withdrawn
- [ ] Retention period must be specified (or reference to applicable law)
- Suspect: "We retain as long as necessary" without defining period — ⚠️
- Suspect: No erasure mechanism — 🔴

### §8(10) — Grievance Officer
- [ ] Contact details of Grievance Officer must be published/available
- [ ] Must respond to complaints within prescribed period (rules to prescribe)

---

## §9 — Children's Data

**Highest risk tier.** Flag immediately.
- [ ] Verifiable parental/guardian consent required for children under 18
- [ ] No behavioural tracking / targeted advertising to children
- [ ] No processing that harms children's well-being
- Suspect: Age-gate is purely self-declared (checkbox) — 🔴
- Suspect: Any profiling or targeted ad clause not excluding under-18 — 🔴

---

## §11 — Right to Access Information
- [ ] Data Principal can request: categories processed, entities shared with, summary of processing

## §12 — Right to Correction and Erasure
- [ ] Mechanism to correct inaccurate data
- [ ] Mechanism to erase data on withdrawal of consent

## §13 — Right to Grievance Redressal
- [ ] Mechanism for complaints to Fiduciary
- [ ] Escalation to DPBI if unresolved

## §14 — Right to Nominate
- [ ] Data Principal may nominate someone to exercise rights upon death/incapacity

---

## §16 — Cross-Border Transfers

- [ ] Transfer only to countries on approved whitelist (to be notified by Central Government)
- [ ] No transfers to blacklisted countries
- Suspect: Blanket global transfer clause with no jurisdiction restrictions — ⚠️
- Suspect: Transfer to countries not yet on approved list — ⚠️ (flag pending Rules notification)

---

## Significant Data Fiduciary (SDF) Obligations

If entity likely to be designated SDF (high volume / sensitive data):
- [ ] Data Protection Officer (DPO) appointment
- [ ] Periodic Data Protection Impact Assessment (DPIA)
- [ ] Periodic audit by independent auditor
- [ ] No profiling of children

---

## Sensitive Personal Data (SPD) — Heightened Scrutiny

Any clause touching the following = automatic HIGH risk:
- Health / medical data
- Financial data
- Biometric data
- Caste or tribe
- Religious or political belief
- Sexual orientation

Check: Is explicit consent obtained separately? Is purpose narrowly defined?
