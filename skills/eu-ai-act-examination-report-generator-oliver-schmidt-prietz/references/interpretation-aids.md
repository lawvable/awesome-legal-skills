# Interpretation Aids — Assessment Frameworks

## 1. Autonomy Scale (ISO 22989)

| Level | German | English | Description | Example |
|-------|--------|---------|-------------|---------|
| 0 | Keine Automatisierung | No automation | Operator controls completely | Manual data entry |
| 1 | Assistenz | Assistance | System suggests, human decides | Spell checker, autocomplete |
| 2 | Teilautomatisierung | Partial automation | Some subfunctions automated, human controls overall | Auto-formatting |
| 3 | Bedingte Automatisierung | Conditional automation | Autonomous in specific contexts, human ready to intervene | Chatbot with escalation |
| 4 | Hohe Automatisierung | High automation | Parts of mission without intervention | Autopilot with monitoring |
| 5 | Volle Automatisierung | Full automation | Entire mission without intervention | Fully autonomous pipeline |
| 6 | Autonomie | True autonomy | Adapts goals without oversight | Self-directed AI (theoretical) |

**Application:** Level 1+ satisfies Art. 3(1) criterion 2. Most commercial AI systems operate at Levels 2-4.

---

## 2. Substantial Modification — 7 Examples

| # | Modification Type | German | Likely Substantial? | Reference |
|---|------------------|--------|-------------------|-----------|
| 1 | Operating system change | Betriebssystem-Aenderung | Yes (if affects behavior) | ErwGr 128 |
| 2 | Software architecture overhaul | Softwarearchitektur | Yes | ErwGr 128 |
| 3 | Training data adaptation | Anpassung der Trainingsdaten | Depends on scope | Case-by-case |
| 4 | Algorithm change | Aenderung des Algorithmus | Yes | Core change |
| 5 | Scope/domain expansion | Erweiterung des Anwendungsbereichs | Yes (purpose change) | Art. 25(1)(c) |
| 6 | External component integration | Integration externer Komponenten | Depends | Case-by-case |
| 7 | Hardware upgrade | Hardware-Upgrade | Yes (if affects behavior) | ErwGr 128 |

**Key exception:** Self-learning adaptations foreseen and covered by the original conformity assessment are NOT substantial modifications (Art. 25(4)).

---

## 3. Finetuning Graduation Matrix

| Technique | Parameter Impact | Risk Level | Likely Substantial? |
|-----------|-----------------|------------|-------------------|
| PEFT/LoRA/QLoRA/Adapter | < 1% parameters | LOW | No (usually) |
| Prefix tuning/Prompt tuning | External parameters only | LOW | No |
| Layer-wise finetuning (top layers) | 5-30% parameters | MEDIUM | Case-by-case |
| Layer-wise finetuning (deep layers) | 30-50% parameters | MEDIUM-HIGH | Likely yes |
| Full finetuning | All parameters | HIGH | Yes (usually) |
| Full retraining with new data | All parameters + new data | HIGH | Yes |
| Architecture modification + retrain | Structural + all parameters | VERY HIGH | Yes |

**Meta-factors to assess:**
1. Extent of parameter change (Umfang der Parameteraenderung)
2. Foreseeability (Vorhersehbarkeit)
3. Risk assessment impact (Risikobewertung)
4. Technical/organizational complexity (Komplexitaet)

---

## 4. Open-Source Checklists Summary

### Checklist I: AI Systems — Art. 2(12) Full Exemption

| Step | Question | Required Answer |
|------|----------|----------------|
| **Step 1** | Is it an AI system (Art. 3(1))? | Yes (to proceed) |
| **Step 2a** | Is it high-risk (Art. 6)? | No (to qualify) |
| **Step 2b** | Is it prohibited (Art. 5)? | No (to qualify) |
| **Step 2c** | Does it trigger Art. 50? | No (to qualify) |
| **Step 3.1** | Publicly accessible? | Yes |
| **Step 3.2** | Equal access without barriers? | Yes |
| **Step 3.3** | No price charged? | Yes |
| **Step 3.4** | Personal data only for technical purposes? | Yes |
| **Step 3.5** | License permits use, modification, distribution? | Yes |
| **Step 3.6** | Parameters/weights/architecture public? | Yes |

**All Step 3 = Yes AND all Step 2 = No → FULL EXEMPTION**

### Checklist II: GPAI Models — Art. 53(2) Partial Exemption

| Step | Question | Required Answer |
|------|----------|----------------|
| **Step 1** | Is it a GPAI model (Art. 3(63))? | Yes (to proceed) |
| **Step 2a** | Weights publicly accessible? | Yes |
| **Step 2b** | Architecture fully disclosed? | Yes |
| **Step 2c** | Execution info provided? | Yes |
| **Step 2d** | Downloadable without authentication? | Yes |
| **Step 2e** | Unrestricted use (private + commercial)? | Yes |
| **Step 2f** | Modification permitted? | Yes |
| **Step 3a** | No payment-based distribution? | Yes (micro-enterprise exception) |
| **Step 3b** | No personal data exploitation? | Yes |
| **Step 3c** | NOT classified as systemic risk? | Yes (no systemic risk) |

**All criteria met → PARTIAL EXEMPTION (documentation + transparency only)**

---

## 5. Art. 6(3) Exception Decision Framework

```
ANNEX III TRIGGERED
        │
        ▼
Does system perform profiling (Art. 4(4) GDPR)?
├── YES → EXCEPTION CANNOT APPLY → HIGH-RISK
└── NO → Continue
        │
        ▼
Does ANY condition (a)-(d) apply?
│
├── (a) Narrow procedural task?
│   Questions: Is task narrow? Mechanical? No substantive judgment?
│   Examples: OCR, format conversion, data extraction
│
├── (b) Improving previously completed human activity?
│   Questions: Human already decided? AI only enhances quality/format?
│   Examples: Grammar check on written decision, formatting
│
├── (c) Detecting decision patterns (without replacing)?
│   Questions: Analyzes past decisions? Flags deviations? No auto-correction?
│   Examples: Audit tools, consistency analysis for quality assurance
│
└── (d) Preparatory task to assessment?
    Questions: Prepares info for human? Human makes final decision?
    Examples: Case law research, data compilation for review
        │
        ▼
At least one condition met?
├── NO → EXCEPTION DOES NOT APPLY → HIGH-RISK
└── YES → Continue
        │
        ▼
Does system pose significant risk of harm?
├── YES → EXCEPTION DOES NOT APPLY → HIGH-RISK
└── NO → EXCEPTION APPLIES → NOT HIGH-RISK
              │
              └── BUT: Must document per Art. 6(4) + register (Art. 49(2))
```

---

## 6. Risk Tier Summary

| Tier | Legal Basis | Obligations | Penalty |
|------|------------|-------------|---------|
| **Prohibited** | Art. 5 | BANNED — cannot deploy | EUR 35M / 7% |
| **High-Risk (Annex I)** | Art. 6(1) | Full Chapter III requirements | EUR 15M / 3% |
| **High-Risk (Annex III)** | Art. 6(2) | Full Chapter III requirements | EUR 15M / 3% |
| **GPAI Systemic Risk** | Art. 51 | Art. 53 + Art. 55 | EUR 15M / 3% |
| **GPAI Standard** | Art. 53 | Art. 53 transparency/documentation | EUR 15M / 3% |
| **Limited Risk** | Art. 50 | Transparency obligations only | EUR 15M / 3% |
| **Minimal Risk** | N/A | Art. 4 AI competence only | N/A |

---

## 7. Transition Timeline

| Date | What Becomes Effective |
|------|----------------------|
| 1 Aug 2024 | AI Act enters into force |
| 2 Feb 2025 | Prohibited practices (Art. 5), AI competence (Art. 4) |
| 2 Aug 2025 | GPAI obligations (Art. 51-56), governance bodies |
| 2 Feb 2026 | Penalties applicable for Art. 5 and Art. 4 violations |
| **2 Dec 2027** *(Omnibus-postponed from 2 Aug 2026)* | High-risk Annex III obligations, deployer obligations (Art. 26) |
| **2 Aug 2028** *(Omnibus-postponed from 2 Aug 2027)* | High-risk Annex I obligations |

---

## 8. Commission Guidelines Published (as of assessment)

| # | Guideline | Date | Status | Verified |
|---|-----------|------|--------|----------|
| 1 | AI System Definition | 6 Feb 2025 | Final — C(2025) 924 | Confirmed |
| 2 | Prohibited AI Practices (Art. 5) | 4 Feb 2025 | Final | Confirmed |
| 3 | GPAI Code of Practice | 10 Jul 2025 | Final — endorsed by Commission + AI Board 1 Aug 2025 | Confirmed Feb 2026 |
| 4 | GPAI Model Provider Guidelines (Art. 51-55) | 18 Jul 2025 | Final — adopted by Commission | Confirmed Feb 2026 |
| 5 | AI-Generated Content Marking (Art. 50) | 17 Dec 2025 | 1st Draft — further draft expected Mar 2026, final expected Jun 2026 | Confirmed Feb 2026 |
| 6 | High-Risk Classification (Art. 6) | Deadline: 2 Feb 2026 | **Delayed** — Commission missed deadline, final draft expected late Feb/Mar 2026 | Verified 13 Feb 2026 |

**Note:** Dates verified as of 13 Feb 2026. Always web-search to confirm current status before relying on these dates — Commission timelines shift. Guideline #6 (high-risk classification) is particularly critical as it was overdue at time of verification.

**Always search for the latest state of these guidelines, especially #6 (high-risk classification).**
