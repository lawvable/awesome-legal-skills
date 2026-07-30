# Quick Assessment Decision Tree

Condensed classification logic for rapid triage. This reference supports the /ai-act-quick skill with simplified decision gates.

---

## 6-Step Gate Sequence

```
┌──────────────────────────────────────────────────────────┐
│ GATE 1: SCOPE CHECK (Art. 2)                             │
│                                                           │
│ EU connection?                                            │
│ ├── No EU connection at all → Likely OUT OF SCOPE         │
│ ├── Military/defence only → OUT OF SCOPE (Art. 2(3))      │
│ ├── Personal/household only → OUT OF SCOPE (Art. 2(10))   │
│ ├── Pure research only → OUT OF SCOPE (Art. 2(6))         │
│ ├── Pre-market R&D only → OUT OF SCOPE (Art. 2(8))        │
│ └── Any other → IN SCOPE → Continue                       │
└────────────────────────┬─────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────┐
│ GATE 2: AI SYSTEM TEST (Art. 3(1)) — Simplified          │
│                                                           │
│ Three quick questions:                                    │
│ (1) Machine-based system? [virtually always yes for SW]   │
│ (2) Infers or generates beyond deterministic rules?       │
│     - ML predictions, NLP, generation, recommendations    │
│     - If purely rule-based (no learning/inference) → NO   │
│ (3) Output influences environment (decisions, content)?   │
│                                                           │
│ All three YES → Likely AI system                          │
│ Any NO → Likely NOT AI system (but verify with full test) │
└────────────────────────┬─────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────┐
│ GATE 3: PROHIBITED PRACTICE SCREEN (Art. 5)              │
│                                                           │
│ Quick flags — check if system does any of:                │
│                                                           │
│ □ Manipulates behavior below conscious awareness          │
│ □ Exploits vulnerable groups (children, elderly, disabled)│
│ □ Scores people on social behavior for unrelated purposes │
│ □ Predicts individual crime risk from profiling alone     │
│ □ Scrapes facial images from internet/CCTV untargeted     │
│ □ Recognizes emotions in workplace or school              │
│ □ Categorizes people by race/religion/politics biometrics │
│ □ Real-time biometric ID in public spaces for police      │
│                                                           │
│ Any flagged → POSSIBLE PROHIBITED PRACTICE                │
│   → Recommend immediate /ai-act-classifier run            │
│   → Recommend immediate legal counsel                     │
│ None flagged → Continue                                   │
└────────────────────────┬─────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────┐
│ GATE 4: HIGH-RISK CHECK (Art. 6 + Annex I/III)           │
│                                                           │
│ SECTOR-BASED QUICK TRIGGERS:                              │
│                                                           │
│ Healthcare / medical devices                              │
│ └── AI in medical device → Likely Annex I Nr. 11-12      │
│ └── AI in patient care decisions → Check Annex III Nr. 5  │
│                                                           │
│ Financial services                                        │
│ └── Credit scoring → Annex III Nr. 5(a)                   │
│ └── Insurance risk (life/health) → Annex III Nr. 5(b)     │
│ └── Fraud detection → Explicitly EXCLUDED from 5(a)       │
│                                                           │
│ Human resources / employment                              │
│ └── Recruitment/screening → Annex III Nr. 4(a)            │
│ └── Performance monitoring → Annex III Nr. 4(b)           │
│ └── Promotion/termination decisions → Annex III Nr. 4(b)  │
│ └── Task allocation by behavior → Annex III Nr. 4(b)      │
│                                                           │
│ Education                                                 │
│ └── Admissions/access → Annex III Nr. 3(a)                │
│ └── Grading/assessment → Annex III Nr. 3(b)               │
│ └── Exam proctoring → Annex III Nr. 3(c)                  │
│                                                           │
│ Law enforcement / justice                                 │
│ └── Risk assessment → Annex III Nr. 6                     │
│ └── Judicial research/application → Annex III Nr. 8(a)    │
│ └── Election influence → Annex III Nr. 8(b)               │
│                                                           │
│ Critical infrastructure                                   │
│ └── Safety component → Annex III Nr. 2                    │
│ └── AI in product → Check Annex I                         │
│                                                           │
│ Public administration                                     │
│ └── Benefit eligibility → Annex III Nr. 5(c)              │
│ └── Emergency dispatch → Annex III Nr. 5(d)               │
│                                                           │
│ Biometrics (any sector)                                   │
│ └── Remote identification → Annex III Nr. 1(a)            │
│ └── Categorization → Annex III Nr. 1(b)                   │
│ └── Emotion recognition → Annex III Nr. 1(c) or Art. 5    │
│                                                           │
│ Consumer / retail / other                                 │
│ └── Chatbot/virtual assistant → Likely Art. 50 only       │
│ └── Recommendation engine → Likely minimal risk           │
│ └── Content generation → Art. 50(2) transparency          │
│                                                           │
│ Annex I/III triggered → LIKELY HIGH-RISK                  │
│   Quick Art. 6(3) check:                                  │
│   - Is it a narrow procedural task? (formatting, filing)  │
│   - Does it profile individuals? If yes → no exception    │
│   → If exception unclear → flag for full analysis         │
│ No Annex I/III trigger → Continue                         │
└────────────────────────┬─────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────┐
│ GATE 5: GPAI CHECK                                        │
│                                                           │
│ Does the system use a general-purpose AI model?           │
│                                                           │
│ GPAI indicators:                                          │
│ □ Built on a foundation model (GPT, Claude, Gemini, etc.) │
│ □ General-purpose: can perform diverse tasks not limited   │
│   to a single domain                                      │
│ □ Trained on broad data at scale                          │
│                                                           │
│ If GPAI model detected:                                   │
│ ├── Provider of the GPAI model → Art. 53 obligations      │
│ ├── Systemic risk? (>10^25 FLOP or designated)            │
│ │   └── Yes → Art. 53 + Art. 55 obligations               │
│ └── Deployer using GPAI-based system → check if system    │
│     itself is high-risk (Gates 3-4 still apply)           │
│                                                           │
│ No GPAI → Continue                                        │
└────────────────────────┬─────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────┐
│ GATE 6: TRANSPARENCY TRIGGERS (Art. 50)                   │
│                                                           │
│ □ System interacts directly with persons?                 │
│   → Art. 50(1): Must disclose AI interaction              │
│ □ System generates synthetic content (text/image/audio)?  │
│   → Art. 50(2): Must mark content as AI-generated         │
│ □ System performs emotion recognition?                    │
│   → Art. 50(3): Must disclose to affected persons         │
│ □ System generates deep fakes?                            │
│   → Art. 50(4): Must label as artificially generated      │
│                                                           │
│ Any trigger → LIMITED RISK (Art. 50 obligations)          │
│ No triggers → MINIMAL RISK (Art. 4 only)                  │
└──────────────────────────────────────────────────────────┘
```

---

## Quick Role Determination

```
ROLE QUICK CHECK

Organization role → Role mapping:

Developed in-house + deploy → PROVIDER (Art. 3(3))
Purchased/licensed + deploy → DEPLOYER (Art. 3(4))
Modified/finetuned → Check quasi-provider risk:
    ├── Changed purpose → QUASI-PROVIDER (Art. 25(1)(c))
    ├── Own brand/name → QUASI-PROVIDER (Art. 25(1)(a))
    ├── Full retraining → Likely QUASI-PROVIDER (Art. 25(1)(b))
    ├── Partial finetuning → Possible QUASI-PROVIDER (needs full Art. 25 analysis)
    └── Config only → DEPLOYER (not substantial modification)
Distribute/import → DISTRIBUTOR (Art. 3(7)) or IMPORTER (Art. 3(6))
Evaluating → No role yet — use this assessment to inform procurement decision
```

---

## Quick Obligation Mapping

### If Likely HIGH-RISK — Provider

| Priority | Top Obligations | Article |
|----------|----------------|---------|
| Immediate | AI competence measures | Art. 4 |
| Critical | Risk management system | Art. 9 |
| Critical | Quality management system | Art. 17 |
| Critical | Technical documentation | Art. 11 |
| Critical | Conformity assessment | Art. 43 |
| High | EU database registration | Art. 49 |
| High | Post-market monitoring | Art. 72 |

### If Likely HIGH-RISK — Deployer

| Priority | Top Obligations | Article |
|----------|----------------|---------|
| Immediate | AI competence measures | Art. 4 |
| Immediate | Use per operating instructions | Art. 26(1) |
| Immediate | Assign oversight persons | Art. 26(2) |
| Immediate | Activate logging (6-month retention) | Art. 26(6) |
| Critical | DPIA (before deployment) | Art. 26(9) |
| High | Inform employees (if workplace) | Art. 26(7) |
| High | EU database registration | Art. 49(3) |
| High | FRIA (if public body / public services / insurance / social benefits) | Art. 27 |

### If Likely LIMITED RISK (Art. 50)

| Priority | Top Obligations | Article |
|----------|----------------|---------|
| Immediate | AI competence measures | Art. 4 |
| From 2 Aug 2026 (50(2) legacy marking: 2 Dec 2026) | Transparency disclosure(s) | Art. 50(1)-(4) |

### If Likely MINIMAL RISK

| Priority | Top Obligations | Article |
|----------|----------------|---------|
| Immediate | AI competence measures | Art. 4 |
| Voluntary | Codes of conduct | Art. 95 |

---

## Jurisdiction Quick Flags

Trigger jurisdiction-specific flags based on deployment country:

| Country | Quick Flags |
|---------|------------|
| **DE** | Works council co-determination (BetrVG §87) if workplace AI; BaFin model governance if finance; BSI/KRITIS if critical infrastructure |
| **AT** | Works council dignity consent (ArbVG §96) if workplace AI; FMA requirements if finance |
| **CH** | EU market access compliance needed; nDSG Art. 21 automated decision rights; FINMA if finance |
| **FR** | CSE consultation before deployment if workplace AI; CNIL AI guidance; ACPR/AMF if finance; platform worker rules if gig economy |
| **NL** | Works council consent (WOR Art. 27) if monitoring tech; AP algorithmic framework; DNB/AFM if finance |
| **IT** | Trade union agreement or labor inspectorate auth (Art. 4 Statuto) if workplace monitoring; Garante enforcement active; Decreto Trasparenza |
| **ES** | AESIA oversight; Ley Rider if platform workers; AEPD sandbox; BdE/CNMV if finance |

For full jurisdiction details → [references/jurisdiction-flags.md]

---

## Urgency Assessment

```
COMPLIANCE URGENCY CALCULATOR

Current date: [use actual date]
Applicable deadline: [from classification]

Days remaining: [calculate]

URGENCY LEVELS:
├── OVERDUE (deadline passed) → Immediate action; potential enforcement exposure
├── CRITICAL (< 90 days) → Full assessment + implementation sprint
├── HIGH (90-180 days) → Full assessment + structured implementation
├── MEDIUM (180-365 days) → Plan and begin implementation
└── LOW (> 365 days) → Strategic planning; early preparation advantage

For Art. 5 (prohibited practices): OVERDUE since 2 Feb 2025
For Art. 4 (AI competence): OVERDUE since 2 Feb 2025
For GPAI obligations: OVERDUE since 2 Aug 2025
For Art. 50 (transparency): Deadline 2 Aug 2026 — 50(1)/(3)/(4) + 50(2) new systems; legacy generative-AI 50(2) marking 2 Dec 2026 (Omnibus grace). NOT overdue, NOT postponed with high-risk.
For Annex III high-risk: Deadline 2 Dec 2027 (Omnibus-postponed from 2 Aug 2026)
For Annex I high-risk: Deadline 2 Aug 2028 (Omnibus-postponed from 2 Aug 2027)
```
