# AI Act Decision Trees

Quick-reference decision trees for the three most common classification questions. Read this file when users ask "Is this an AI system?", "What risk tier?", or "Are we the provider or deployer?".

| Aspect | Detail |
|--------|--------|
| Document | Derived from Regulation (EU) 2024/1689, Art. 2–6, 50–51, and EC Guidelines |
| Institution | Compiled from multiple official EU sources |
| Source URL | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 |

*German: KI-Verordnung — Entscheidungsbaeume fuer Klassifizierung*

---

## Decision Tree A: Is This an AI System? (Art. 3(1))

> **Interpretive note:** The Commission's Guidelines on AI System Definition (Feb 2025) are non-binding soft law. Boundary cases below reflect the Commission's current interpretation, not settled law. Where marked "borderline" or "likely", legal counsel should make the final determination.

```
START: Does the system meet ALL of these criteria?
│
├─ 1. Machine-based system?
│     (software, hardware, or embedded — excludes purely human processes)
│     └─ NO → NOT an AI system. Stop.
│
├─ 2. Designed to operate with varying levels of autonomy?
│     (some degree of independent operation — even if human-initiated)
│     └─ NO → NOT an AI system. May be conventional software.
│
├─ 3. May exhibit adaptiveness after deployment?
│     ("may" — capability, not requirement; includes static models)
│     └─ Note: Static models that do not adapt still qualify if other criteria met.
│
├─ 4. Receives input and infers how to generate outputs?
│     (infers = beyond simple predefined rules or fixed logic)
│     ├─ Simple if/then rules → NOT an AI system
│     ├─ Statistical model, ML, neural network → YES
│     └─ Expert system with inference engine → LIKELY YES
│
├─ 5. Generates outputs (predictions, content, recommendations, decisions)?
│     └─ NO → NOT an AI system. Stop.
│
└─ 6. Can influence physical or virtual environments?
      (directly or through information to human decision-makers)
      └─ NO → NOT an AI system. Stop.

ALL YES → This IS an AI system under Art. 3(1).
```

**Boundary cases** (all interpretive — not legally settled):

| Technology | Likely Classification | Reasoning | Certainty |
|------------|----------------------|-----------|-----------|
| Conventional software (ITSM, ERP without ML) | NOT AI | No inference beyond predefined rules | High |
| RPA without ML | NOT AI | Executes scripted steps, no inference | High |
| Spreadsheet with statistical formulas | NOT AI | No inference, deterministic computation | High |
| Rule-based chatbot without ML | **Borderline** | May lack inference criterion — depends on complexity | Low |
| Search engine with ranking algorithm | **Likely AI** | Infers relevance, generates ranked output | Medium |
| Recommendation system (collaborative filtering) | **Likely AI** | Infers preferences, generates recommendations | Medium-High |

**Cite:** Art. 3(1) AI Act; EC Guidelines on AI System Definition (Feb 2025)
**Files:** `guidelines/ai-system-definition.md`, `core/regulation-title-I-general.md`

---

## Decision Tree B: Risk Classification

> **Interpretive note:** The Art. 6(3) exception and Annex III area boundaries involve significant legal judgment. The Commission's practical guidelines on high-risk classification are still in preparation (expected 2026). Until published, the assessment below follows the regulation text and available Commission guidance.

```
START: Confirmed AI system under Art. 3(1)
│
├─ STEP 1: Scope Check (Art. 2)
│  Is the system excluded from the AI Act entirely?
│  • Military/defence use (Art. 2(3))
│  • R&D before placing on market (Art. 2(6))
│  • Personal/household use (Art. 2(10))
│  • Open-source with no prohibited/high-risk use (Art. 2(12))
│  • Third-country use with no EU-impacting output (Art. 2(1))
│  └─ YES to any → OUT OF SCOPE. Stop.
│
├─ STEP 2: Prohibited Practice Screen (Art. 5)
│  Does the system fall under any of these 8 prohibitions?
│  (a) Subliminal manipulation
│  (b) Exploitation of vulnerabilities
│  (c) Social scoring by public authorities
│  (d) Individual criminal risk assessment (solely based on profiling)
│  (e) Untargeted facial image scraping
│  (f) Emotion recognition in workplace/education
│  (g) Biometric categorisation (race, politics, union, religion, sexual orientation)
│  (h) Real-time remote biometric ID in public (law enforcement — narrow exceptions)
│  └─ YES → PROHIBITED (Art. 5). Highest penalties: EUR 35M or 7% turnover.
│
├─ STEP 3: High-Risk Assessment (Art. 6 + Annexes I & III)
│  ├─ Path A: Annex I product legislation (Art. 6(1))
│  │  Is the AI system a safety component of, or itself, a product
│  │  covered by EU harmonisation legislation in Annex I?
│  │  (medical devices, machinery, toys, vehicles, aviation, etc.)
│  │  AND requires third-party conformity assessment?
│  │  └─ YES → HIGH-RISK
│  │
│  ├─ Path B: Annex III areas (Art. 6(2))
│  │  Does the system fall into one of 8 high-risk areas?
│  │  1. Biometrics (beyond Art. 5 prohibitions)
│  │  2. Critical infrastructure management
│  │  3. Education and vocational training
│  │  4. Employment, workers management, self-employment access
│  │  5. Essential services access (credit, insurance, public benefits)
│  │  6. Law enforcement
│  │  7. Migration, asylum, border control
│  │  8. Administration of justice and democratic processes
│  │  └─ YES → Check Art. 6(3) exception below
│  │
│  └─ Art. 6(3) Exception: NOT high-risk if ALL conditions met:
│     (a) Performs narrow procedural task, AND
│     (b) Improves result of previously completed human activity, AND
│     (c) Does not replace human assessment (no material override risk), AND
│     (d) Does not profile natural persons
│     PLUS: NEVER applicable if the AI system performs profiling (Art. 6(3) last sentence)
│     └─ All conditions met → NOT high-risk despite Annex III listing
│
├─ STEP 4: GPAI Check (Art. 51–56)
│  Is this a general-purpose AI model?
│  (trained with large amounts of data using self-supervision at scale,
│   capable of competently performing a wide range of tasks)
│  ├─ NO → Continue to Step 5
│  ├─ YES, cumulative FLOP ≤ 10^25 → GPAI standard obligations (Art. 53)
│  └─ YES, cumulative FLOP > 10^25 → GPAI with systemic risk (Art. 51(2), Art. 55)
│     (or designated by Commission decision based on other criteria)
│
└─ STEP 5: Transparency Triggers (Art. 50)
   Does the system:
   (a) Interact directly with natural persons? → disclose AI nature
   (b) Generate synthetic audio/image/video/text? → mark as AI-generated
   (c) Perform emotion recognition? → inform subjects
   (d) Generate deepfakes? → label as artificially generated
   └─ YES to any → LIMITED RISK (transparency obligations apply)
   └─ NO to all → MINIMAL RISK (no specific obligations, voluntary codes only)

FINAL CLASSIFICATION:
┌─────────────────────┬──────────────────────────────────────┐
│ Risk Tier           │ Key Obligations                       │
├─────────────────────┼──────────────────────────────────────┤
│ PROHIBITED          │ Cannot be placed on EU market          │
│ HIGH-RISK           │ Full Title III requirements (Art. 8-49)│
│ GPAI — systemic     │ Art. 53 + Art. 55 (Code of Practice)  │
│ GPAI — standard     │ Art. 53 only                          │
│ LIMITED RISK        │ Art. 50 transparency                   │
│ MINIMAL RISK        │ No mandatory obligations               │
└─────────────────────┴──────────────────────────────────────┘
```

**Cite:** Art. 2, 5, 6, 50, 51 AI Act
**Files:** `core/regulation-title-I-general.md`, `core/regulation-title-II-prohibited.md`, `core/regulation-title-III-high-risk.md`, `core/annex-iii-high-risk.md`, `core/regulation-title-V-gpai.md`, `core/regulation-title-IV-transparency.md`

---

## Decision Tree C: Provider or Deployer?

> **Interpretive note:** The distinction between "substantial modification" (Art. 3(23)) and routine configuration is not yet clearly defined in binding guidance. The Commission's guidelines on substantial modification are in preparation (expected 2026). The thresholds below follow the regulation text and available MDCG/compliance guidance.

```
START: Who are you in relation to the AI system?
│
├─ Did you DEVELOP or have developed the AI system?
│  └─ YES → PROVIDER (Art. 3(3))
│     Obligations: Art. 16-25 (full provider requirements)
│
├─ Did you put your NAME/TRADEMARK on it?
│  └─ YES → PROVIDER (Art. 3(3)) — even if you didn't develop it
│
├─ Did you SUBSTANTIALLY MODIFY it after market placement?
│  └─ YES → NEW PROVIDER (Art. 25) — full provider obligations triggered
│     See: compliance-guides/modifying-ai-classification.md
│
├─ Are you USING it under your authority (not personal use)?
│  └─ YES → DEPLOYER (Art. 3(4))
│     Obligations: Art. 26 (deployer requirements)
│
├─ Are you IMPORTING it into the EU?
│  └─ YES → IMPORTER (Art. 3(6))
│     Obligations: Art. 23
│
├─ Are you DISTRIBUTING it in the EU (without importing)?
│  └─ YES → DISTRIBUTOR (Art. 3(7))
│     Obligations: Art. 24
│
└─ Did you CHANGE THE INTENDED PURPOSE of a high-risk system?
   └─ YES → QUASI-PROVIDER → becomes new Provider (Art. 25(1)(c))

⚠ MULTI-ROLE: An entity can hold multiple roles simultaneously.
  Example: A company that develops AND deploys its own AI system
  is both Provider (Art. 16-25) AND Deployer (Art. 26).
```

**Cite:** Art. 3(3)–(7), Art. 25, Art. 28 AI Act
**Files:** `core/regulation-title-I-general.md`, `core/regulation-title-III-high-risk.md`, `compliance-guides/modifying-ai-classification.md`
