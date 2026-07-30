# Scope Exclusions — Art. 2 AI Act

## Overview

The AI Act does not apply to certain categories of AI systems. Art. 2 defines the material, personal, and territorial scope, including exclusions.

---

## Exclusion Categories

### A. Military and National Security — Art. 2(3)

**Exclusion:** The AI Act does not apply to AI systems placed on the market, put into service, or used exclusively for military, defence, or national security purposes, regardless of the type of entity carrying out those activities.

**Key conditions:**
- Must be **exclusively** for military/defence/national security
- Dual-use systems (both military and civilian) are NOT excluded
- The exclusion applies regardless of whether the entity is public or private

**Assessment question:** Is this AI system used exclusively for military, defence, or national security, with no civilian application?

---

### B. Third-Country International Cooperation — Art. 2(4)

**Exclusion:** The AI Act does not apply to AI systems placed on the market, put into service, or used by public authorities of a third country or by international organisations, where those authorities or organisations use AI systems in the framework of international cooperation or agreements for law enforcement and judicial cooperation with the EU or its Member States.

**Key conditions:**
- Used by third-country public authority OR international organization
- Under international cooperation agreement with EU/Member States
- For law enforcement or judicial cooperation purposes
- Adequate personal data protection safeguards must exist

---

### C. Scientific Research — Art. 2(6)

**Exclusion:** The AI Act does not apply to AI systems used for the sole purpose of scientific research and development.

*German: Wissenschaftsprivileg*

**Key conditions:**
- Must be for the **sole purpose** of scientific research
- Applies to both basic and applied research
- If the system transitions from research to deployment/commercialization, the exclusion ends
- Does not cover systems already placed on market or put into service

**Assessment question:** Is this AI system used solely for scientific research, with no commercial deployment or public-facing use?

---

### D. Pre-Market Research and Development — Art. 2(8)

**Exclusion:** The AI Act does not apply to AI systems in the research, testing, and development phase before being placed on the market or put into service.

*German: Forschungs- und Entwicklungsprivileg*

**Key conditions:**
- System must not yet be placed on market or put into service
- R&D activities include testing, validation, and experimentation
- Once the system is deployed for real use (even in limited pilot), the exclusion may no longer apply
- Free-of-charge beta testing with real users may constitute "putting into service"

**Important:** The prohibited practices under Art. 5 still apply during R&D (Art. 2(8) second sentence). You cannot develop a prohibited system even in R&D.

---

### E. Personal/Household Use — Art. 2(10)

**Exclusion:** The AI Act does not apply to AI systems placed on the market, put into service, or used by natural persons for purely personal, non-professional activity.

*German: Haushaltsausnahme*

**Key conditions:**
- Used by natural persons (not organizations)
- Purely personal, non-professional purpose
- Analogous to GDPR household exemption (Art. 2(2)(c) GDPR)
- Does not apply if the personal use has professional implications

**Assessment question:** Is this AI system used exclusively by a private individual for purely personal, non-professional purposes?

---

### F. Free and Open-Source AI Technologies — Art. 2(12) / Art. 53(2)

*German: Freie und quelloffene KI-Technologie*

This is the most complex exclusion with two distinct regimes:

#### Checklist I: Full Exemption for AI Systems — Art. 2(12)

**Three-step verification:**

**STEP 1: Verify AI System Status (Art. 3(1))**

Confirm the technology is an AI system using the 7-criteria test.

**STEP 2: Exclusion Triggers — If ANY is "Yes", exemption does NOT apply:**

| # | Question | If Yes |
|---|----------|--------|
| 1 | Is the AI system classified as high-risk per Art. 6? | Exemption fails |
| 2 | Does it fall under prohibited practices Art. 5? | Exemption fails |
| 3 | Does it trigger transparency obligations Art. 50? | Exemption fails |

**Critical:** Open-source does NOT exempt high-risk, prohibited, or Art. 50 transparency systems.

**STEP 3: Free and Open-Source License Verification (6 questions — ALL must be "Yes"):**

| # | Criterion | Explanation | Test |
|---|-----------|-------------|------|
| 1 | Public accessibility | System is freely/openly available, not restricted | Not behind paywall or closed community |
| 2 | Equal access | All persons have equal access without barriers | No discriminatory registration fees or memberships |
| 3 | No payment | No price charged for system or related services | Core "free" criterion — no monetization |
| 4 | Limited data use | Personal data processed only for security, compatibility, or interoperability | No indirect monetization through data |
| 5 | Full license rights | License permits use, modification, and distribution | Central open-source criterion |
| 6 | Parameter transparency | Parameters, weights, and architecture publicly accessible | Technical transparency requirement |

**Result:** If ALL 6 criteria met AND no Step 2 exclusion triggers → Full exemption under Art. 2(12)

**Recitals:** 102, 103

---

#### Checklist II: Partial Exemption for GPAI Models — Art. 53(2)

**Three-step verification:**

**STEP 1: Verify GPAI Model Status (Art. 3(63))**

Confirm the model is a general-purpose AI model.

**STEP 2: Free and Open-Source License Verification**

**A. Public accessibility of all parameters:**

| Parameter | Description | Publicly Accessible? |
|-----------|-------------|---------------------|
| Weights (Gewichte) | Numeric values from training | Must be public |
| Model Architecture (Modellarchitektur) | Structure/layers/connections | Must be fully disclosed |
| Execution Information (Modellausführung) | Dependencies, requirements, instructions | Must be provided |

**B. Permission for use, modification, distribution:**

| Right | Description | Present? |
|-------|-------------|----------|
| Access for everyone (Zugang für jedermann) | Downloadable without authentication | Must be Yes |
| Unrestricted use (Nutzung ohne Einschränkungen) | Private and commercial use permitted | Must be Yes |
| Modification right (Möglichkeit zur Änderung) | Users can modify and adapt | Must be Yes |

**C. No harmful monetization:**

| Criterion | Description | Met? |
|-----------|-------------|------|
| No payment-based distribution | Not distributed for payment (micro-enterprise exception) | Must be Yes |
| No personal data exploitation | No data use beyond technical necessity | Must be Yes |

**STEP 3: No Systemic Risk**

| Check | Description | Result |
|-------|-------------|--------|
| Model NOT classified as GPAI with systemic risk | Per Art. 3(65), Art. 55 | Must NOT have systemic risk |

**Scope of partial exemption:**
- **Exempted from:** Technical documentation obligations (Art. 53(1)(a-b)), transparency information to downstream providers (Art. 53(1)(c-d))
- **Still required:** Collaboration obligations (Art. 25(2)), copyright transparency, training data specification, all other provider duties

---

#### Key Differences Between Exemptions

| Aspect | Full Exemption (Art. 2(12)) | Partial Exemption (Art. 53(2)) |
|--------|----------------------------|-------------------------------|
| Applies to | AI Systems | GPAI Models |
| Scope | Complete exemption from AI Act | Partial — only specific documentation obligations |
| Blockers | High-risk, prohibited, Art. 50 | Systemic risk |
| Remaining obligations | None | Collaboration, copyright, training data |

---

## Territorial Scope — Art. 2(1)

The AI Act applies to:
1. **Providers** placing on market or putting into service AI systems in the EU, regardless of establishment
2. **Deployers** established in the EU or in a place where EU law applies
3. **Providers and deployers** in third countries where AI system **output is used in the EU**
4. **Importers and distributors** of AI systems
5. **Product manufacturers** placing on market/putting into service AI systems together with their product
6. **Authorized representatives** of providers established outside the EU

**Key principle:** Even third-country providers/deployers are covered if the AI system's output is intended to be used within the EU.

---

## Summary: Exclusion Decision Tree

```
Is the system excluded from the AI Act?
│
├─ Military/defence/national security exclusively? (Art. 2(3))
│   └─ YES → EXCLUDED
│
├─ Third-country authority under international agreement? (Art. 2(4))
│   └─ YES → EXCLUDED
│
├─ Solely for scientific research? (Art. 2(6))
│   └─ YES → EXCLUDED (but Art. 5 still applies)
│
├─ Pre-market R&D phase? (Art. 2(8))
│   └─ YES → EXCLUDED (but Art. 5 still applies)
│
├─ Purely personal/household use? (Art. 2(10))
│   └─ YES → EXCLUDED
│
├─ Free and open-source? (Art. 2(12))
│   ├─ Is it high-risk, prohibited, or Art. 50? → NOT EXCLUDED
│   └─ Passes 6-criterion checklist? → EXCLUDED
│
└─ None of the above → NOT EXCLUDED, AI Act applies
```
