# ENISA Severity Assessment Methodology

**Formula:** `SE = (DPC × EI) + CB`

> **Role of this methodology:** the ENISA score is structured **decision support**. It informs — but never replaces — the statutory tests in Art. 33(1) ("unlikely to result in a risk") and Art. 34(1) ("likely to result in a high risk"). Every score must be bridged to a written Art. 33/34 conclusion (see §4a).

---

## 0. Rapid Orientation Trees (Common Simple Scenarios)

For experienced DPOs who want a rapid preliminary check before the full workflow:

```
ENCRYPTED DEVICE LOST
├── Encryption current (e.g., AES-256)? → NO → Full assessment needed
├── Key secure and stored separately? → NO → Full assessment needed
├── Backup exists? → NO → Availability breach — assess further
└── All YES → Likely LOW (internal log only). Confirm with full assessment if >100 subjects.

MISDIRECTED EMAIL (single recipient)
├── Recalled/deleted before read? → YES, confirmed → Likely LOW (internal log)
├── Contains Art. 9 data? → YES → Full assessment needed (likely HIGH)
├── Contains financial data? → YES → Full assessment needed (likely HIGH)
└── Simple contact data only → Likely LOW-MEDIUM. Document and assess.

RANSOMWARE
├── Exfiltration evidence? → YES → Full assessment needed (likely HIGH/VERY HIGH)
├── Backup restored <24h? → YES, no exfiltration → Assess availability impact
└── No backup / extended downtime → Full assessment needed (likely HIGH)

PHISHING (credentials compromised)
├── Scope limited to single account? → Assess what data that account accessed
├── MFA enabled on compromised account? → YES → Reduced risk, still assess
└── Admin/privileged account? → Full assessment needed immediately
```

**Note:** The decision trees provide preliminary orientation only. Always complete the full ENISA assessment plus the Art. 33/34 Legal Bridge for the definitive classification and documentation.

---

## 1. Data Processing Context (DPC): 1-4

### Base Scores by Category

| Category | Base | Examples |
|----------|------|----------|
| **Simple Data** | 1 | Name, contact details, biographical data, education, professional experience |
| **Behavioral Data** | 2 | Location, traffic data, browsing history, preferences, habits |
| **Financial Data** | 3 | Income, bank statements, credit cards, investments, transactions |
| **Sensitive Data (Art. 9)** | 4 | Health, political opinions, religious beliefs, sexual orientation, biometric, genetic, criminal records |

### Contextual Adjustments (±1-3, capped to final DPC range 1–4)

| Factor | Direction | Examples |
|--------|-----------|----------|
| Volume of data per individual | ↑ +1 to +2 | 1 year of traffic data vs. 1 week |
| Characteristics of controller | ↑ +1 to +2 | Online pharmacy customer list → health assumptions |
| Vulnerable data subjects | ↑ +1 to +3 | Minors, protected witnesses, abuse victims |
| Data invalidity/age | ↓ -1 to -2 | Credit cards expired 10+ years ago |
| Public availability | ↓ -1 to -2 | Data already in public directories |
| Nature reveals less than category | ↓ -1 | Generic health certificate vs. diagnosis |

**Important:** After applying all adjustments, the final DPC score must be **capped at 4.0** (ceiling) and **floored at 1.0** (minimum). Where adjustments would push the score beyond 4.0, note the excess factors as **qualitative aggravating circumstances** in the Strategic Advisory section — they reinforce the severity level but do not change the numeric DPC score.

### Adjustment Examples

| Scenario | Base | Adjustment | Final DPC |
|----------|------|------------|-----------|
| Supermarket customer list (name, phone) | 1 | None | 1 |
| Luxury car dealership customer list | 1 | +1 (financial status assumption) | 2 |
| Online pharmacy customer list | 1 | +2 (health status assumption) | 3 |
| Undercover police officer list | 1 | +3 (critical safety risk) | 4 |
| Dating site user list (name only) | 2 | None | 2 |
| Dating site with sexual preferences | 4 | None | 4 |
| 10-year-old expired credit cards | 3 | -2 (invalid data) | 1 |

---

## 2. Ease of Identification (EI): 0.25-1.00

### Scoring Levels

| Score | Level | Description |
|-------|-------|-------------|
| **0.25** | Negligible | Extremely difficult to match data to individual; possible only under specific conditions |
| **0.50** | Limited | Identification requires significant effort or access to additional sources |
| **0.75** | Significant | Identification achievable with moderate effort or commonly available information |
| **1.00** | Maximum | Direct identification possible from breached data alone; no special research needed |

### EI by Identifier Type

| Identifier | EI = 0.25 | EI = 0.50 | EI = 0.75 | EI = 1.00 |
|------------|-----------|-----------|-----------|-----------|
| **Full Name** | Common name, large population | Few share name nationally | Few share name in small city | + Date of birth + email |
| **ID/Passport/SSN** | Number alone, no reference DB access | — | + reveals DOB, + email | + name from reference DB |
| **Phone/Address** | Not in public register | Not public, small city | — | In public register |
| **Email** | No name, not searchable online | — | Searchable in social networks | Contains name + searchable |
| **Picture** | Unclear/distant image | Unclear + location clues | Clear photo, no other info | Clear + linked to location/group |
| **Codes/Aliases** | No link without reference DB | — | Alias reveals first name + email | Reveals full name or DB access |

---

## 3. Circumstances of Breach (CB): 0-2 (Additive)

Points are **ADDITIVE** — multiple circumstances can apply.

### Loss of Confidentiality

| Score | Circumstance |
|-------|--------------|
| 0 | Data exposed to risk without evidence of access |
| +0.25 | Data disclosed to limited known recipients |
| +0.50 | Data disclosed to unknown number of recipients or publicly |

### Loss of Integrity

| Score | Circumstance |
|-------|--------------|
| 0 | Data altered but original recovered before use |
| +0.25 | Data altered, possibly used incorrectly, recoverable |
| +0.50 | Data altered, possibly used incorrectly, NOT recoverable |

### Loss of Availability

| Score | Circumstance |
|-------|--------------|
| 0 | Data recoverable without difficulty (backup exists) |
| +0.25 | Temporal unavailability (recovery requires effort/time) |
| +0.50 | Permanent unavailability (no recovery possible) |

### Malicious Intent

| Score | Circumstance |
|-------|--------------|
| 0 | Accidental (human error, technical failure, misconfiguration) |
| +0.50 | Intentional (theft, hacking, insider attack, data sale) |

---

## 4. Severity Calculation & Verdicts

### Calculate: `SE = (DPC × EI) + CB`

| SE Score | Level | Impact Description | Presumptive action (subject to Art. 33/34 legal test) |
|----------|-------|--------------------|--------------------------------------------------------|
| **< 2** | LOW | Minor inconveniences (time re-entering info, annoyance) | Presumption: internal log only (Art. 33(5)) |
| **2 – < 3** | MEDIUM | Significant inconveniences overcome with difficulty (extra costs, denial of services, stress) | Presumption: notify SA (Art. 33) |
| **3 – < 4** | HIGH | Significant consequences with serious difficulty (misappropriation, blacklisting, property damage, job loss) | Presumption: notify SA + data subjects (Art. 33 & 34) |
| **≥ 4** | VERY HIGH | Significant/irreversible consequences (financial distress, long-term harm, death risk) | Presumption: notify SA + subjects + consider public communication |

The score creates a **presumption or recommendation, not an automatic legal duty**. The statutory triggers remain Art. 33(1) and Art. 34(1).

---

## 4a. The Legal Bridge (score → facts → conclusion)

Every assessment must translate the score into the legal tests, in writing:

```
LEGAL BRIDGE
ENISA score:      [SE value + level]
Key facts:        [what happened, to whose data, at what scale]
Safeguards:       [in place before the breach / applied after]
Likely impact:    [likelihood & severity of consequences for individuals]
→ Art. 33(1):     [NOTIFY SA / NO — unlikely to result in a risk, because …]
→ Art. 34(1):     [NOTIFY SUBJECTS / NO — no high risk, because … /
                   NO — exception Art. 34(3)(a)/(b)/(c) applies, because …]
```

**Worked bridge example** (continuing Example 1, ransomware with backup, SE = 3.75 HIGH):

> ENISA score: 3.75 (HIGH) — presumption: notify SA + subjects.
> Key facts: hospital ransomware; health data of 5,000 patients encrypted by attacker; backup restored within 24h; no exfiltration evidence so far, but forensic review incomplete.
> Safeguards: offline backups (effective); data at rest unencrypted (gap).
> Likely impact: temporary unavailability materialised (care delays possible); confidentiality impact unconfirmed but plausible given attacker access — for Art. 9 data, plausible disclosure cannot be ruled "unlikely".
> → Art. 33(1): NOTIFY SA — cannot conclude "unlikely to result in a risk" while exfiltration is unexcluded and availability was lost for 24h.
> → Art. 34(1): NOTIFY SUBJECTS — high risk is likely if disclosure occurred; given Art. 9 data and ongoing forensics, communicate now and supplement, rather than wait. No Art. 34(3) exception: data was not encrypted at rest (a), no subsequent measure eliminates the disclosure risk (b), individual communication is feasible (c).

**Divergence rule:** if the legal conclusion departs from the score's presumption — in either direction — the reasons must be stated in the bridge and recorded in the Internal Compliance Log. A LOW score with vulnerable subjects and credible threat context can still require notification; a MEDIUM score where access is forensically excluded may justify non-notification, documented.

---

## 4b. Borderline Score Guidance

Scores near thresholds require extra scrutiny:

| Score Range | Guidance |
|-------------|----------|
| **1.8 – 2.0** | Document thoroughly why you believe LOW is justified; SA may disagree |
| **2.8 – 3.0** | Consider whether any uncaptured factors push into HIGH; lean conservative |
| **3.8 – 4.0** | Assess whether public communication is warranted even below 4.0 threshold |

When a score is within 0.25 of a threshold, explicitly note this in the assessment and recommend the user discuss the borderline classification with their DPO or legal counsel.

---

## 5. Encryption Assessment

### Logic Tree

```
IF Encrypted + Algorithm Current + Key Secure + Key Stored Separately + Backup Exists:
    → Confidentiality risk = MINIMAL
    → Art. 34 exemption: LIKELY AVAILABLE (High Confidence)
    → BUT still assess: Was availability impacted? For how long?

IF Encrypted + Algorithm Current + Key Secure + Backup Exists:
    → Confidentiality risk = LOW
    → Art. 34 exemption: POSSIBLY AVAILABLE (Medium Confidence)
    → Flag: Key storage separation not confirmed

IF Encrypted + Key Compromised OR Key Stored With Data:
    → Treat as unencrypted data
    → Art. 34 exemption: NOT AVAILABLE
    → Full risk assessment required

IF Encrypted + No Backup:
    → Availability breach occurred regardless of encryption
    → May still require notification despite encryption
    → Art. 34 exemption does NOT apply to availability loss
```

### Questions to Ask

1. Was the data encrypted at rest with state-of-the-art algorithms (e.g., AES-256)?
2. Is the encryption key compromised or potentially accessible?
3. Was the key stored separately from the encrypted data?
4. Was the key generated in a way that it cannot be ascertained by available technological means?
5. How long did the attacker have potential access? (relevant for brute-force risk)

**Critical Caveat:** Encryption only potentially exempts from *data subject* notification (Art. 34). You may still need to notify the *supervisory authority* (Art. 33) and must always document internally (Art. 33(5)).

---

## 6. Worked Examples

### Example 1: Ransomware with Backup
- **Scenario:** Hospital ransomware, 5000 patients, health data encrypted, backup restored in 24h
- **DPC:** 4 (health data)
- **EI:** 0.75 (names + patient IDs)
- **CB:** 0.25 (temporal unavailability) + 0.50 (malicious) = 0.75
- **SE:** (4 × 0.75) + 0.75 = 3.75 → **HIGH**
- **Presumptive verdict (confirm via Art. 33/34 bridge — see §4a):** Notify SA + Subjects

### Example 2: Misdirected Email
- **Scenario:** Single email with salary info sent to wrong employee, recalled within 1 hour
- **DPC:** 3 (financial)
- **EI:** 1.00 (full name + salary)
- **CB:** 0.25 (limited known recipient) + 0 (accidental) = 0.25
- **SE:** (3 × 1.00) + 0.25 = 3.25 → **HIGH**
- **Presumptive verdict (confirm via Art. 33/34 bridge):** Notify SA + Subject — but the bridge may justify less if disclosure is verifiably contained (cf. EDPB mispostal cases)

### Example 3: Lost Encrypted Laptop
- **Scenario:** Laptop with 200 customer records, full disk encryption, key not compromised
- **DPC:** 1 (contact data)
- **EI:** 0.25 (encryption renders negligible)
- **CB:** 0 (data not actually accessed)
- **SE:** (1 × 0.25) + 0 = 0.25 → **LOW**
- **Presumptive verdict (confirm via Art. 33/34 bridge):** Internal log only

---

## 7. Borderline Score Worked Examples

These examples illustrate cases near severity thresholds where judgment calls matter most.

### Example 4: Near LOW/MEDIUM Threshold (SE = 1.75 – 2.0)
- **Scenario:** Marketing agency sends newsletter to 150 recipients with all email addresses visible in CC (instead of BCC)
- **DPC:** 1 (email addresses only — simple contact data)
- **EI:** 1.00 (email addresses are direct identifiers)
- **CB:** 0.25 (disclosed to limited known recipients — the other subscribers) + 0 (accidental) = 0.25
- **SE:** (1 × 1.00) + 0.25 = 1.25 → **LOW**
- **But consider:** If the newsletter topic reveals sensitive information (e.g., subscribers to a mental health newsletter), DPC should be adjusted upward (+1 to +2), potentially pushing SE to 2.25–3.25 → MEDIUM or HIGH
- **Lesson:** The nature of the mailing list matters enormously for DPC adjustment

### Example 5: Near MEDIUM/HIGH Threshold (SE = 2.75 – 3.0)
- **Scenario:** HR SaaS provider (processor) suffers breach; employee records of 3 client companies exposed. Data includes names, salaries, and performance ratings. 500 employees affected. Accidental exposure via misconfigured API endpoint, discovered within 12 hours.
- **DPC:** 3 (salary = financial data)
- **EI:** 1.00 (full names + employee IDs)
- **CB:** 0.25 (exposed via API, unclear if anyone accessed) + 0 (accidental) = 0.25
- **SE:** (3 × 1.00) + 0.25 = 3.25 → **HIGH**
- **Argument for MEDIUM:** If access logs confirm zero external access during exposure window, one could argue CB should be 0 (exposed to risk without evidence of access), giving SE = 3.0 — right at the boundary
- **Recommendation:** At this boundary, lean toward HIGH (notify subjects). The inclusion of performance ratings alongside salaries creates potential for workplace harm that justifies the conservative approach

### Example 6: Near HIGH/VERY HIGH Threshold (SE = 3.75 – 4.0)
- **Scenario:** Insurance company data exfiltration by external attacker. Health data (diagnoses + claims history) for 2,000 customers stolen. Data includes names, policy numbers, and ICD-10 diagnosis codes. Confirmed exfiltration to external server.
- **DPC:** 4 (health data — Art. 9)
- **EI:** 1.00 (full names + policy numbers)
- **CB:** 0.50 (disclosed to unknown recipients) + 0.50 (malicious intent) = 1.00
- **SE:** (4 × 1.00) + 1.00 = 5.00 → **VERY HIGH**
- **Note:** This is clearly VERY HIGH. But consider a variation: same breach but only 15 individuals affected, and the ICD-10 codes are for common conditions (flu, routine checkups). Here you might argue DPC adjustment of -1 (nature reveals less than category suggests), giving SE = (3 × 1.00) + 1.00 = 4.00 — exactly at the VERY HIGH threshold. In this case, the small scale might justify staying at HIGH, but the malicious exfiltration argues for VERY HIGH. Document both analyses.
