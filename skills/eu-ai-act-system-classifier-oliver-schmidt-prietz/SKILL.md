---
name: eu-ai-act-classification-oliver-schmidt-prietz
description: |
  Determines whether a technology qualifies as an AI system under Art. 3(1) of the EU AI Act and classifies its risk tier (prohibited, high-risk, GPAI with systemic risk, limited risk, minimal risk). This skill should be used when the user asks to "classify an AI system under the AI Act", "determine the AI Act risk tier", "check if something is an AI system", "assess prohibited practices", "check high-risk classification", "determine Art. 6 exception applicability", or mentions "KI-Verordnung", "Risikoklassifizierung", Art. 5, Annex III, or GPAI systemic risk.
metadata:
  author: Oliver Schmidt-Prietz
  license: AGPL-3.0
  version: 2026.06.05
---

# EU AI Act System Classifier

Determine whether a technology qualifies as an **AI system under Art. 3(1) AI Act** (Regulation (EU) 2024/1689) and classify its risk tier.

## Disclaimer (show at session start, do not block)

> **Important:** This skill provides structured AI system classification guidance based on the EU AI Act (Regulation (EU) 2024/1689), Commission guidelines, and the OECD AI framework. It is not legal advice. Final classification decisions should involve qualified legal counsel with AI Act expertise. Effective dates for high-risk obligations reflect the AI Omnibus 2026 postponement (Annex III: 2 December 2027; Annex I: 2 August 2028).

---

## When to Search the Web

**On activation — always search for:**
```
EU AI Act Commission guidelines AI system definition 2025 2026
EU AI Act high-risk classification guidelines Art. 6 latest
```

**During Annex III assessment — search for:**
```
EU AI Act Annex III delegated acts modifications [current year]
EU AI Act high-risk classification new categories
```

**For GPAI assessment — search for:**
```
EU AI Office GPAI systemic risk threshold FLOP [current year]
EU AI Office GPAI Code of Practice latest
EU AI Act Art. 51 general purpose AI model classification
```

**For open-source exception — search for:**
```
EU AI Act open source exception Art. 2(12) guidance [current year]
EU AI Act Art. 53(2) GPAI open source partial exemption
```

---

## Workflow: Ask Questions ONE AT A TIME

### Phase 1: Scope Gate

**Prior Assessment Context (optional):**
> "If you have previously run another EU AI Act skill, you may paste the Assessment Context block here. This pre-fills several questions and avoids redundant input."

If context is provided, pre-populate applicable fields and skip questions that are already answered. If any field conflicts with user answers, flag the inconsistency.

**Q1 — System Description:**
> "Please provide a brief description of the AI technology or system you want to classify. Include: what it does, how it works (at a high level), who uses it, and in what context."

**Q2 — Scope Exclusion Check (system-description-informed):**

Based on the Q1 system description, assess whether any scope exclusion signals are present:

- If the description signals a potential exclusion (military use, personal/household use, pure R&D, pre-market testing, international law enforcement cooperation) → ask a targeted confirmation question for that specific exclusion only. Example: "Your description mentions this is for internal research only — is this system used **exclusively** for scientific R&D with no deployment to end users? (Art. 2(6))"
- If the description signals an open-source component → ask a targeted question: "You mentioned this uses an open-source model. Is the system itself released under a free and open-source license? (Art. 2(12))"
- If no exclusion signals are present in the description → skip Q2 entirely with a brief note: "Based on your description, no scope exclusions appear to apply. Proceeding with the AI system definition test."
- If genuinely unclear whether an exclusion might apply → present relevant exclusions conversationally (not as a lettered list), focusing only on plausible ones given the system description.

**If a military, international law enforcement, personal use, pure R&D, or pre-market exclusion applies:** Output exclusion analysis with legal basis → STOP.

**If the system is released under a free and open-source license:** Run the dedicated open-source checklist from [references/scope-exclusions.md](references/scope-exclusions.md).
- For AI systems: Apply Checklist I (Art. 2(12)) — 3-step process, 6 verification questions
- For GPAI models: Apply Checklist II (Art. 53(2)) — 3-step process with parameter accessibility check
- If exemption applies → output analysis → STOP
- If exemption does NOT apply (e.g., high-risk, prohibited, or Art. 50 system) → continue to Phase 2

**If no exclusion applies:** Continue to Phase 2.

---

### Phase 2: AI System Definition Test (Art. 3(1))

Read [references/ai-system-definition.md](references/ai-system-definition.md) for the full 7-criteria framework.

Walk through 7 criteria **one at a time**, providing examples for each:

**Criterion 1 — Machine-based operation:**
> "Is this system operated by machine-based processes (maschinengestütztes System)? This includes any software or hardware that processes information computationally."

**Criterion 2 — Degree of autonomy (Autonomiegrad):**
> "What degree of autonomy does the system exhibit? Use the ISO 22989 scale:
> - Level 0: No automation — fully human-controlled
> - Level 1: Assistance — system suggests, human decides
> - Level 2: Partial automation — some subfunctions automated, human controls overall
> - Level 3: Conditional automation — autonomous in specific contexts, human ready to intervene
> - Level 4: High automation — operates parts of mission without intervention
> - Level 5: Full automation — completes entire mission without intervention
> - Level 6: True autonomy — adapts goals without oversight"

**Criterion 3 — Adaptability after deployment:**
> "Can the system adapt its behavior after deployment? Does it learn from new data, user interactions, or environmental feedback? (Note: this includes continuous learning, online learning, and reinforcement from human feedback.)"

**Criterion 4 — Explicit or implicit goals:**
> "Does the system have defined goals — either explicitly programmed (e.g., 'classify images') or implicitly learned through training data (e.g., learned optimization objectives)?"

**Criterion 5 — Inference capability:**
> "Does the system derive outputs through inference — i.e., making predictions, drawing conclusions, or generating recommendations beyond simple deterministic rules? This distinguishes AI from traditional rule-based software."

**Criterion 6 — Output generation:**
> "What outputs does the system generate? This includes:
> - Predictions (e.g., risk scores, forecasts)
> - Content (e.g., text, images, audio, video)
> - Recommendations (e.g., product suggestions, decision support)
> - Decisions (e.g., automated approvals, classifications)"

**Criterion 7 — Environmental influence:**
> "Does the system's output influence physical or virtual environments? Examples: controlling physical devices, modifying user interfaces, filtering content, triggering automated processes."

**AI System Determination Output:**

After all 7 criteria, output:

```markdown
### AI System Definition Analysis (Art. 3(1))

| # | Criterion | Met? | Reasoning |
|---|-----------|------|-----------|
| 1 | Machine-based operation | [Yes/No] | [brief reasoning] |
| 2 | Degree of autonomy | [Level X] | [brief reasoning] |
| 3 | Adaptability after deployment | [Yes/No] | [brief reasoning] |
| 4 | Explicit or implicit goals | [Yes/No] | [brief reasoning] |
| 5 | Inference capability | [Yes/No] | [brief reasoning] |
| 6 | Output generation | [Yes/No] | [brief reasoning] |
| 7 | Environmental influence | [Yes/No] | [brief reasoning] |

**Determination:** [This system IS / IS NOT an AI system under Art. 3(1) AI Act]
**Confidence:** [High / Medium / Low — explain if not High]
```

If NOT an AI system → output determination with reasoning → STOP.
If YES → continue to Phase 3.

---

### Phase 3: Risk Classification

Read the relevant reference files for each step.

**Step 1: Prohibited Practice Screening (Art. 5) — Analyst-Driven Pre-Filtering**

Read [references/prohibited-practices.md](references/prohibited-practices.md).

> "I will now screen against the 8 categories of prohibited AI practices under Art. 5."

**Internal relevance scoring (do not show this step to the user):**

Based on the Q1 system description, silently categorize each of the 8 prohibited practices as:
- **Not applicable** — system description clearly does not involve this practice
- **Possibly relevant** — system description has some signals worth examining
- **Likely relevant** — system description strongly suggests this practice may apply

**Present findings as a single assessment table (all 8 shown for transparency):**

| # | Prohibition | Article | Relevance | Reasoning |
|---|------------|---------|-----------|-----------|
| 1 | Subliminal, manipulative, or deceptive techniques | Art. 5(1)(a) | [assessment] | [brief reasoning based on system description] |
| 2 | Exploitation of vulnerabilities (age, disability, social/economic) | Art. 5(1)(b) | [assessment] | [brief reasoning] |
| 3 | Social scoring by public authorities or on their behalf | Art. 5(1)(c) | [assessment] | [brief reasoning] |
| 4 | Individual criminal offense risk assessment/prediction (without factual basis) | Art. 5(1)(d) | [assessment] | [brief reasoning] |
| 5 | Untargeted facial recognition database scraping | Art. 5(1)(e) | [assessment] | [brief reasoning] |
| 6 | Emotion recognition in workplace and education | Art. 5(1)(f) | [assessment] | [brief reasoning] |
| 7 | Biometric categorization for sensitive characteristics | Art. 5(1)(g) | [assessment] | [brief reasoning] |
| 8 | Real-time remote biometric identification in public (law enforcement) | Art. 5(1)(h) | [assessment] | [brief reasoning] |

After presenting the table, ask: "Do any flagged items need discussion, or should I explore any I marked 'Not applicable'?"

Deep-dive only on items marked "Possibly relevant" or "Likely relevant," or on any items the user asks about, using [references/prohibited-practices.md](references/prohibited-practices.md) for detailed edge cases, boundary analysis, gray zone scenarios, and multi-category interactions.

**If ANY prohibition is flagged:**

```
WARNING — PROHIBITED AI PRACTICE DETECTED

Art. 5(1)([x]) AI Act: [description]

This AI system falls within the scope of a PROHIBITED practice.
Deployment, placing on market, or putting into service is PROHIBITED.

Legal basis: Art. 5(1)([x]), Recital [XX]
Penalty: Art. 99(3) — up to EUR 35,000,000 or 7% of total worldwide annual turnover

IMMEDIATE ACTION REQUIRED: Consult qualified legal counsel.
```

→ STOP (unless user wants to explore exceptions listed in Art. 5).

**Step 2: High-Risk Check — Annex I (Product Safety)**

Read [references/high-risk-annexes.md](references/high-risk-annexes.md).

> "Is this AI system a safety component of a product, or is it itself a product, covered by the EU harmonization legislation listed in Annex I?"

Screen all 18 Annex I product categories. If YES → high-risk under Art. 6(1).

**Step 3: High-Risk Check — Annex III (Application-Based) — Auto-Pre-Screen**

For sector-specific Annex III analysis, read [references/sector-guidance.md](references/sector-guidance.md). For worked classification examples, see [references/case-studies.md](references/case-studies.md).

**Auto-assessment (internal — based on Q1 system description):**

Using sector, use case, and deployment context signals from the system description, automatically map the system to relevant Annex III categories. Categorize each as:
- **Relevant** — system description clearly signals this category (e.g., HR screening tool → Employment)
- **Potentially relevant** — indirect signals warrant closer examination
- **Not applicable** — no signals in description connect to this category

**Present auto-assessment table (all 8 categories shown for transparency):**

> "Based on your system description, here is my initial Annex III relevance assessment:"

| # | Category | Key Applications | Relevance | Reasoning |
|---|----------|-----------------|-----------|-----------|
| 1 | Biometrics | Remote biometric identification, emotion recognition, categorization | [assessment] | [reasoning from system description] |
| 2 | Critical infrastructure | Management/operation of critical digital/physical infrastructure | [assessment] | [reasoning] |
| 3 | Education & vocational training | Access determination, admission, assessment, monitoring | [assessment] | [reasoning] |
| 4 | Employment, workers management, self-employment | Recruitment, screening, evaluation, monitoring, termination | [assessment] | [reasoning] |
| 5 | Access to essential services | Creditworthiness, insurance, social benefits, emergency dispatch | [assessment] | [reasoning] |
| 6 | Law enforcement | Risk assessment, polygraphs, evidence reliability, profiling, crime analytics | [assessment] | [reasoning] |
| 7 | Migration, asylum, border control | Risk assessment, application examination, detection | [assessment] | [reasoning] |
| 8 | Administration of justice & democratic processes | Legal research, sentencing, dispute resolution, elections | [assessment] | [reasoning] |

> "Do you agree with this assessment, or should I re-examine any categories?"

User confirms or overrides. If the system description contradicts a user override (e.g., user says "Not applicable" for Employment but system processes CVs), flag the contradiction and assess fully regardless.

Detailed assessment proceeds only for categories marked "Relevant" or "Potentially relevant" (or any the user asks to examine).

**If Annex III hit → Check Art. 6(3) exception:**

Read [references/art6-exception.md](references/art6-exception.md).

> "An Annex III category was triggered. Now checking the Art. 6(3) exception — does this system perform only a 'narrow procedural task' or 'complementary human activity' that does not replace or influence human assessment?"

Apply 4 exception conditions:
1. System performs narrow procedural task
2. System improves result of previously completed human activity
3. System detects decision-making patterns without replacing/influencing human assessment
4. System performs preparatory task to an assessment relevant to Annex III use cases

**Special re-exception:** Art. 6(3) last sentence — exception does NOT apply if the system performs profiling of natural persons (Art. 4(4) GDPR).

**Step 3.5: High-risk depth assessment (mandatory if Annex I OR Annex III hits)**

If Step 2 (Annex I) or Step 3 (Annex III) produced a hit — or the case is borderline and requires the Commission Guidelines depth analysis — perform a full high-risk depth assessment before finalising the verdict. Work through the Art. 6 classification grounded in the Commission's draft Art. 6(5) classification guidelines: (1) confirm the Annex I product / Annex III area trigger; (2) apply the Art. 6(3) exception conditions (narrow procedural task, complementary human activity, no replacement of human assessment, preparatory task — subject to the profiling re-exception); (3) document whether the system is a safety component or a product itself; (4) produce a structured decision block (tier + reasoning + cited Annex/Article); and (5) capture the result as a JSON interchange artefact and a short practitioner memo. Only once this depth analysis is complete should you consolidate the final risk-tier classification.

Because high-risk classification is the most consequential tier and the most-recently-updated by Commission guidance, give it the deepest treatment: if any input is ambiguous (e.g., whether the deployment falls inside an Annex III area, or whether the Art. 6(3) exception genuinely applies), state the assumption explicitly and flag it for human review rather than resolving it silently.

**Step 4: GPAI Model Check**

Read [references/gpai-systemic-risk.md](references/gpai-systemic-risk.md).

> "Is this system based on, or does it incorporate, a general-purpose AI model (Art. 3(63))? If so, does the underlying model pose systemic risk (Art. 3(65), Art. 51)?"

- If GPAI model without systemic risk → transparency obligations (Art. 53)
- If GPAI model WITH systemic risk → full Art. 55 obligations apply
- Apply FLOP threshold: 10^25 floating point operations (Art. 51(2))

**Search for latest GPAI classifications and threshold updates.**

**Step 5: Transparency Obligations Check (Art. 50)**

> "Does this system trigger any transparency obligations under Art. 50?"

| Obligation | Trigger | Article |
|------------|---------|---------|
| Interaction disclosure | System interacts directly with natural persons | Art. 50(1) |
| Synthetic content marking | System generates synthetic audio, image, video, text | Art. 50(2) |
| Emotion recognition disclosure | System performs emotion recognition | Art. 50(3) |
| Deepfake labeling | System generates deep fakes | Art. 50(4) |

For detailed implementation guidance — including the Code of Practice's multi-layered marking framework (metadata + watermarking), deployer labelling requirements, exceptions, boundary analysis, and interaction with other AI Act provisions — see [references/art50-transparency.md](references/art50-transparency.md).

---

### Classification Flow Decision Tree

> **Note: GPAI assessment runs in parallel with Steps 1–3.** Step 4 (GPAI Model?) is shown sequentially in the tree below for readability, but GPAI determination is independent of the risk-tier path. A high-risk AI system can simultaneously be a GPAI model with systemic risk — in which case **both regimes apply**. Always evaluate Step 4 on every system, regardless of the outcome of Steps 1–3.

```
                    ┌─────────────────┐
                    │  SCOPE GATE     │
                    │  Art. 2 Check   │
                    └────────┬────────┘
                             │
                   Exclusion applies?
                    ├── YES → STOP (out of scope)
                    └── NO
                             │
                    ┌────────▼────────┐
                    │ AI SYSTEM TEST  │
                    │ Art. 3(1)       │
                    │ 7 Criteria      │
                    └────────┬────────┘
                             │
                    Is it an AI system?
                    ├── NO → STOP (not an AI system)
                    └── YES
                             │
              ┌──────────────▼──────────────┐
              │ RISK CLASSIFICATION          │
              │ (assess in order)            │
              └──────────────┬──────────────┘
                             │
                ┌────────────▼────────────┐
                │ Step 1: Art. 5          │
                │ Prohibited Practices?   │
                ├── YES → PROHIBITED      │
                └── NO                    │
                             │
                ┌────────────▼────────────┐
                │ Step 2: Annex I         │
                │ Product Safety?         │
                ├── YES → HIGH-RISK       │
                │         (Art. 6(1))     │
                └── NO                    │
                             │
                ┌────────────▼────────────┐
                │ Step 3: Annex III       │
                │ Application-Based?      │
                ├── YES ──┐               │
                └── NO    │               │
                  │       ▼               │
                  │  Art. 6(3) Exception? │
                  │  ├── NO → HIGH-RISK   │
                  │  │    (Art. 6(2))     │
                  │  └── YES → NOT high   │
                  │       (Art. 6(4) doc) │
                  │                       │
                ┌─▼───────────────────────┐
                │ Step 4: GPAI Model?     │
                ├── Systemic risk         │
                │   → Art. 53 + 55        │
                ├── Standard GPAI         │
                │   → Art. 53             │
                └── No GPAI               │
                             │
                ┌────────────▼────────────┐
                │ Step 5: Art. 50         │
                │ Transparency Trigger?   │
                ├── YES → LIMITED RISK    │
                └── NO → MINIMAL RISK     │
                          (Art. 4 only)   │
                └─────────────────────────┘
```

---

### Phase 4: Classification Dashboard Output

After completing all phases, output:

```markdown
## AI Act Classification Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
System:          [name]
Date:            [date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI System (Art. 3(1)):     [YES/NO] — [confidence]
Risk Tier:                 [Prohibited/High-Risk/GPAI-Systemic/Limited/Minimal]
Classification Basis:      [Art. 5(1x) / Annex I Nr. X / Annex III Nr. X / Art. 50 / None]
Art. 6(3) Exception:       [Applicable/Not Applicable/N/A]
Scope Exclusions:          [None / Art. 2(x) applies]
GPAI Model:                [Yes — systemic risk / Yes — standard / No / N/A]
Transparency (Art. 50):    [Applicable — Art. 50(1)-(4) / None]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FLAGS:
[flags if any — examples:]
[PROHIBITED PRACTICE — Art. 5(1)(x) — immediate legal review required]
[QUASI-PROVIDER RISK — modifications may trigger Art. 25]
[GPAI SYSTEMIC RISK — Art. 55 obligations apply]
[PROFILING DETECTED — Art. 6(3) exception excluded per last sentence]
[OPEN-SOURCE — partial exemption conditions met/not met]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ASSESSMENT CONTEXT (paste into next skill)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
System: [name]
Classification: [risk tier]
Basis: [legal basis]
Role: [from prior assessment or TBD]
Quasi-Provider: [from prior assessment or TBD]
Sector: [sector]
Jurisdiction: [list]
Org Size: [size]
Art. 50: [applicable triggers]
GPAI: [yes/no, systemic risk]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NEXT STEPS:
→ Determine the organizational role (provider / deployer / importer / distributor)
→ Map the applicable obligations to that role and risk tier
→ Generate formal assessment documentation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Critical Reminders

1. **Art. 5 prohibitions are absolute** — no exception for existing deployments (grace period ended 2 Feb 2025)
2. **High-risk classification can change** — Commission may adopt delegated acts modifying Annex III (Art. 7)
3. **GPAI systemic risk threshold may be updated** — Commission may update 10^25 FLOP threshold (Art. 51(2))
4. **Art. 6(3) exception is narrow** — profiling always re-triggers high-risk even if exception would otherwise apply
5. **Open-source is not a blanket exemption** — high-risk, prohibited, and Art. 50 systems are not exempted
6. **Always search for latest guidance** — Commission guidelines are actively being published through 2026
7. **Document reasoning** — all classification decisions should be documented per Art. 6(4) for non-high-risk systems
8. **Enforcement context** — reference [references/enforcement-framework.md](references/enforcement-framework.md) for penalty tiers (EUR 35M/7% for Art. 5 violations) and enforcement risk assessment
9. **Jurisdiction-specific requirements** — reference [references/jurisdiction-requirements.md](references/jurisdiction-requirements.md) for national authority, employment law, and sector regulator requirements per deployment jurisdiction
10. **Compliance timeline** — reference [references/compliance-deadlines.md](references/compliance-deadlines.md) for applicable deadlines and quarterly action calendar
11. **Art. 50 transparency detail** — reference [references/art50-transparency.md](references/art50-transparency.md) for the full Art. 50 framework including the Code of Practice's multi-layered marking architecture, deployer labelling requirements, exceptions, and boundary analysis

## Part of the EU AI Act suite

This skill works on its own, but it's designed to interlock with my other EU AI Act skills — install any individually, or use them together for an end-to-end workflow:

- **EU AI Act Quick Assessment** — 15–25 min preliminary triage
- **EU AI Act High-Risk Classifier** — depth Annex I / Annex III assessment
- **EU AI Act Role Determination** — provider / deployer / importer / distributor (incl. Art. 25)
- **EU AI Act Obligations Mapper** — obligations by role and risk tier
- **EU AI Act Examination Report Generator** — audit-ready compliance report
- **EU AI Act Knowledge Base** — Q&A over the Act + Commission guidelines

Each is available as a separate skill — install only what you need.
