# EDPB Case Matching Reference

Based on EDPB Guidelines 01/2021 - Examples regarding data breach notification.

---

## Ransomware Cases (01-04)

### Case 01: Ransomware with Proper Backup
**Scenario:** Small manufacturing company, ransomware encrypts employee data (30 employees), backup restored within hours, no evidence of exfiltration.

| Factor | Assessment |
|--------|------------|
| Notify SA | NO |
| Notify Subjects | NO |
| Reasoning | No confidentiality breach, minimal availability impact, backup available |

**Key differentiators:** If backup unavailable or exfiltration suspected → upgrade to Case 02/03.

---

### Case 02: Ransomware without Proper Backup
**Scenario:** Agricultural company, ransomware encrypts business data including customer/supplier info, no backup, data lost.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES |
| Reasoning | Permanent availability loss, business relationships affected |

**Key differentiators:** If only internal data (no third-party data) → may reduce subject notification.

---

### Case 03: Ransomware with Exfiltration at Hospital
**Scenario:** Hospital ransomware, health data exfiltrated before encryption, 5000+ patients affected.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES |
| Reasoning | High-risk data (health), confidentiality breach confirmed, large scale |

**Key differentiators:** This is the severe case - always requires full notification.

---

### Case 04: Ransomware without Exfiltration at Hospital
**Scenario:** Hospital ransomware, no evidence of exfiltration, backup restored, 2-day service disruption.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | Depends on impact |
| Reasoning | Health data + availability loss warrants SA notification; subject notification depends on actual impact to care |

**Key differentiators:** If patient care was affected → notify subjects.

---

## Data Exfiltration Cases (05-07)

### Case 05: Exfiltration of Hashed Passwords
**Scenario:** Web hosting service, database with usernames and hashed passwords stolen, 1.2M users.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES |
| Reasoning | Scale + credential data; even hashed passwords pose risk |

**Key differentiators:** Strong hashing (bcrypt, Argon2) may reduce urgency but not eliminate notification.

---

### Case 06: Exfiltration of Non-Encrypted Credentials
**Scenario:** Online marketplace, unencrypted passwords + personal data stolen, 1500 users.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES (urgent) |
| Reasoning | Immediate risk of account compromise and identity theft |

**Key differentiators:** Urgency is highest; recommend immediate password reset forced.

---

### Case 07: Sensitive Data Exfiltration
**Scenario:** Insurance company, health data exfiltrated (diagnoses, claims), 2000 customers.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES |
| Reasoning | Art. 9 special category data, high risk of discrimination/harm |

**Key differentiators:** Health + financial combined = very high risk.

---

## Internal Human Risk Cases (08-09)

### Case 08: Exfiltration by Employee
**Scenario:** Departing employee copies customer database (2000 records) to personal device.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | Likely YES |
| Reasoning | Intentional, unknown use of data |

**Key differentiators:** If data recovered and employee confirms no use/sharing → may reduce subject notification.

---

### Case 09: Accidental Transmission of Data
**Scenario:** Employee accidentally sends spreadsheet with 89 students' grades to wrong class group.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES |
| Reasoning | Minors (vulnerable), educational data disclosed to known recipients |

**Key differentiators:** Known recipients + quick action to delete may reduce severity assessment.

---

## Lost/Stolen Devices (10-12)

### Case 10: Stolen Device with Encrypted Data
**Scenario:** Company laptop stolen, full disk encryption (AES-256), strong password, no key compromise.

| Factor | Assessment |
|--------|------------|
| Notify SA | NO |
| Notify Subjects | NO |
| Reasoning | Encryption renders data unintelligible |

**Key differentiators:** If encryption weak or key potentially compromised → treat as Case 11.

---

### Case 11: Stolen Device without Encryption
**Scenario:** Unencrypted USB drive lost, contains 500 customer records with contact + financial data.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES |
| Reasoning | Financial data accessible, unknown who has device |

**Key differentiators:** Contact data only → may not require subject notification.

---

### Case 12: Stolen Paper Documents
**Scenario:** Briefcase stolen containing paper files with 20 clients' tax records.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES |
| Reasoning | Financial data, no technical protection possible for paper |

**Key differentiators:** Paper = always unencrypted; treat as sensitive.

---

## Mispostal Cases (13-16)

### Case 13: Postal Mail to Wrong Address
**Scenario:** Insurance document with health data sent to wrong address, returned unopened.

| Factor | Assessment |
|--------|------------|
| Notify SA | NO |
| Notify Subjects | NO |
| Reasoning | Returned unopened = no actual disclosure |

**Key differentiators:** If opened or not returned → upgrade to Case 14/15.

---

### Case 14: Postal Mail Opened
**Scenario:** Bank statement sent to wrong address, recipient opened and read contents before returning.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES |
| Reasoning | Financial data disclosed to known third party |

**Key differentiators:** Single recipient, likely low malicious intent → may document and monitor.

---

### Case 15: Sensitive Medical Results Misdirected
**Scenario:** Lab results (HIV test) sent to wrong patient by mistake.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES (both parties) |
| Reasoning | Highly sensitive health data, wrong recipient knows correct recipient's data |

**Key differentiators:** HIV/mental health/genetic = highest sensitivity category.

---

### Case 16: Batch Mailing Error
**Scenario:** 15,000 invoices sent with wrong recipient addresses (each person received someone else's invoice).

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES |
| Reasoning | Scale + each invoice discloses financial relationship |

**Key differentiators:** Large scale systematically increases risk.

---

## Social Engineering Cases (17-18)

### Case 17: Identity Theft / Impersonation
**Scenario:** Caller impersonates customer, obtains their account details (address, last 4 digits, transaction history).

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES (the impersonated individual) |
| Reasoning | Targeted attack, specific individual at risk |

**Key differentiators:** Notify the victim, not the attacker (obviously).

---

### Case 18: Email Exfiltration via Phishing
**Scenario:** Employee falls for phishing, attacker accesses email for 3 weeks, 100+ contacts exposed.

| Factor | Assessment |
|--------|------------|
| Notify SA | YES |
| Notify Subjects | YES |
| Reasoning | Extended access period, unknown what was read/copied |

**Key differentiators:** Duration of access increases severity; if access detected within hours → may reduce.

---

## Using This Reference

### Analogy Warning (read before matching)

- The Guidelines 01/2021 cases are **illustrative analogies, not binding decisions**. They show how the EDPB reasoned on stylised facts — they do not decide your case.
- **Factual differences matter.** An analogy never substitutes for the Art. 33/34 legal test applied to the actual facts (see the Legal Bridge in SKILL.md).
- **ENISA and EDPB examples can diverge.** Where they conflict, document both and lean conservative (see "When Cases Conflict with ENISA" below).
- **Channel matters:** a misdirected *email* is only *analogised* to the postal cases (13–16) and Case 09 — it is not directly covered by them. State the differences expressly: emails may be recallable, read receipts and server logs can evidence (non-)access, and digital copies persist and forward in ways paper does not.
- Where an example suggests no notification but your facts are uncertain, preserve the conservative reasoning in writing rather than adopting the example's outcome.

### Matching Process

1. Identify the **category** (Ransomware, Exfiltration, Human Risk, Lost Device, Mispostal, Social Engineering)
2. Find the **closest case** within that category
3. Note the **EDPB recommendation** for that case
4. Identify **key differences** between your scenario and the case
5. Assess whether differences **increase or decrease** risk
6. Compare to your **ENISA calculation** - they should align

### Output Format

> "This scenario most closely resembles **EDPB Case [XX]: [Brief Description]** — as an analogy, not a binding precedent.
>
> EDPB recommendation in that case: SA notification [YES/NO], Subject notification [YES/NO]
>
> Your situation differs in: [Key differences]
>
> Limits of the analogy: [e.g., different channel/medium, scale, data category, evidence of access]
>
> This comparison [SUPPORTS / SUGGESTS RECONSIDERING] your calculated severity verdict of [LEVEL]. The Art. 33/34 Legal Bridge on your facts remains decisive."

### When Cases Conflict with ENISA

If EDPB case suggests different outcome than ENISA calculation:
- Document both assessments
- Lean toward more conservative (higher notification) approach
- Note the discrepancy in Internal Compliance Log
- Consider consulting legal counsel
