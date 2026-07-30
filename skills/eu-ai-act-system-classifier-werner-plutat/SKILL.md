---
name: eu-ai-act-classification
description: Classify an AI system under the EU AI Act (Regulation (EU) 2024/1689, KI-Verordnung) and determine compliance obligations. Walks Art. 3(1) AI system definition (7-criteria test), Art. 2 scope exclusions, Art. 5 prohibited practice screening, Annex I product safety, Annex III high-risk use cases (biometrics, critical infrastructure, education, employment, credit scoring, insurance, law enforcement, migration, justice), Art. 6(3) narrow procedural exception, Art. 51-56 GPAI with the 10^25 FLOP systemic risk threshold, and Art. 50 transparency triggers (deepfakes, emotion recognition, synthetic content). Roles: provider (Anbieter), deployer (Betreiber), importer, distributor, Art. 25 quasi-provider. DACH: Betriebsrat, BaFin, BSI, BNetzA, BfDI. Use when asked to classify an AI system or model, run a Risikoklassifizierung, assess Annex III high-risk status, screen Art. 5 prohibited practices, check the Art. 6(3) exception, classify a medical device, medical imaging, credit scoring, HR or CV screening, employment screening, biometric identification, emotion recognition, deepfake, content moderation, fraud detection, recommender, chatbot, generative AI or foundation model system, run an AI vendor or procurement compliance review, or determine GPAI obligations.
---

# EU AI Act Risk Classification

Classify AI systems under Regulation (EU) 2024/1689 and determine obligations by role.

**Important:** This skill provides compliance workflow support, not legal advice. Always cite specific EU AI Act articles. Where facts are incomplete, state assumptions explicitly and ask targeted follow-up questions.

## Classification Workflow

Follow this decision tree strictly in order. Stop at the first match.

### Step 1 — Scope Check

Confirm the AI system falls within scope:
- Is it placed on the market or put into service in the EU?
- Who is the provider, deployer, importer, distributor, or authorized representative?
- Does a territorial or subject-matter exclusion apply (military, national security, pure research)?

If out of scope, document why and stop.

### Step 2 — Gate 1: Prohibited Practices (Article 5)

Check every Article 5 category. If any match → **PROHIBITED**. Stop unless a narrow law enforcement exception applies.

Categories (check all eight):
1. Manipulation/deception causing significant harm
2. Exploitation of vulnerabilities (age, disability, socio-economic)
3. Social scoring with disproportionate/unrelated adverse treatment
4. Individual predictive policing based solely on profiling
5. Untargeted facial image scraping for recognition databases
6. Emotion recognition in workplace/education (narrow exceptions)
7. Biometric categorisation inferring sensitive characteristics
8. Real-time remote biometric identification in public spaces for law enforcement (narrow exceptions)

→ For the complete checklist with examples and edge cases, read [references/prohibited-practices.md](references/prohibited-practices.md).

### Step 3 — Gate 2: High-Risk (Annex I + Annex III)

**Annex I path:** Is the AI a product or safety component under EU harmonisation legislation (e.g., MDR, Machinery Regulation) subject to third-party conformity assessment? → **HIGH-RISK**

**Annex III path:** Does the intended purpose fall within one of the eight high-risk use-case categories?

| # | Category | Quick examples |
|---|----------|---------------|
| 1 | Biometrics | Remote identification, verification, categorisation |
| 2 | Critical infrastructure | Energy grid control, water systems, traffic management |
| 3 | Education | Admissions, grading, learning access decisions |
| 4 | Employment | CV screening, promotion, termination, task allocation |
| 5 | Essential services | Credit scoring, insurance pricing, housing, welfare |
| 6 | Law enforcement | Risk assessment, evidence evaluation, profiling |
| 7 | Migration & border | Border risk assessment, document verification |
| 8 | Justice & democracy | Judicial assistance, electoral process systems |

→ For all categories with examples and edge cases, read [references/high-risk-annex-iii.md](references/high-risk-annex-iii.md).

**Article 6(3) exception:** Even if an Annex III use case matches, a system is NOT high-risk if it:
- performs a narrow procedural task,
- improves the result of a previously completed human activity,
- detects decision patterns without replacing human assessment, or
- performs a preparatory task for an assessment listed in Annex III,

AND the system does not pose a significant risk of harm to health, safety, or fundamental rights.

If claiming this exception, document the reasoning thoroughly.

### Step 4 — GPAI Models (Articles 51–56)

Independent of system-level risk. A minimal-risk app can use a GPAI model with its own obligations. Downstream providers/deployers must still verify vendor evidence and ensure documentation is sufficient for their specific use case and risk profile.

Check:
- Is a general-purpose AI model involved (broad capability, not narrow-purpose)?
- Who is the GPAI model provider vs. downstream provider?
- Does the model meet systemic risk thresholds (compute-based criteria or EU AI Office designation)?

→ For GPAI obligations and systemic risk details, read [references/gpai-obligations.md](references/gpai-obligations.md).

### Step 5 — Gate 3: Limited Risk (Article 50)

If not prohibited or high-risk, check Article 50 transparency duties:
- AI-generated content or interaction → disclose AI involvement
- Deepfakes/synthetic media → label or watermark
- Emotion recognition systems → inform affected individuals
- Biometric categorisation → inform affected individuals

### Step 6 — Default: Minimal Risk

No AI Act-specific obligations. Recommend:
- AI literacy training (horizontal obligation under the Act)
- Security and privacy by design
- Proportionate documentation for auditability
- Voluntary codes of conduct

## Quick Question Set

Use these questions at the start (and whenever facts are missing) to gather the information needed for classification. For borderline cases or uncertainty, escalate early to qualified legal counsel and document assumptions.

**System & Purpose**
1. What does the AI system do? What are its inputs and outputs?
2. What is the intended purpose? What decisions does it support or make?

**Impact & Context**
3. Does it make or materially influence decisions about individuals in education, employment, essential services, law enforcement, migration, or justice?
4. Who is affected — customers, employees, citizens, patients?
5. Is it customer-facing? Is there meaningful human oversight in practice?

**Technical**
6. Does it use biometrics, emotion recognition, or infer sensitive attributes?
7. What data categories are processed, including special category data?
8. Is a GPAI model used? Which provider? What compliance evidence is available?

**Organisational**
9. Who is the provider vs. deployer? Where is it deployed?
10. Is it a product or safety component under EU harmonisation legislation?

If answers are incomplete, state assumptions explicitly and flag gaps.

## Reference Files

Load these as needed based on the classification result:

| File | When to read |
|------|-------------|
| [references/prohibited-practices.md](references/prohibited-practices.md) | Evaluating Article 5 — complete checklist with examples and edge cases |
| [references/high-risk-annex-iii.md](references/high-risk-annex-iii.md) | Evaluating Annex III — all 8 categories with examples, edge cases, and the Article 6(3) exception |
| [references/gpai-obligations.md](references/gpai-obligations.md) | System uses a GPAI model — Articles 51–56, systemic risk thresholds, downstream duties |
| [references/obligations-matrix.md](references/obligations-matrix.md) | After classification — provider/deployer/importer/distributor responsibilities by risk level |
| [references/timeline.md](references/timeline.md) | Building a compliance roadmap — all deadlines with practical planning guidance |
| [references/dach-specific.md](references/dach-specific.md) | Deployer is in Germany/Austria/Switzerland — works council, BaFin, BSI, BNetzA, sector-specific overlaps |
| [references/templates.md](references/templates.md) | Producing deliverables — classification memo, risk register entry, executive summary templates |

## Output Format

Every classification produces three deliverables:

1. **Classification Memo** — Formal assessment documenting the decision tree walkthrough, classification result, cited articles, and key assumptions. This is the primary legal record.

2. **Risk Register Entry** — Structured entry for the organisation's AI risk register with system name, classification, key obligations, deadlines, and responsible parties.

3. **Executive Summary** — One-page summary for leadership with classification result, key obligations, timeline, and recommended next steps.

**Always consider horizontal obligations** such as AI literacy/training (Article 4) as part of the compliance roadmap, even for minimal-risk systems.

→ For complete templates, read [references/templates.md](references/templates.md).

## Penalties Overview

Flag these in every assessment to ensure appropriate escalation:

| Violation | Maximum fine |
|-----------|-------------|
| Prohibited practices | €35M or 7% global annual turnover |
| High-risk system obligations | €15M or 3% global annual turnover |
| Incorrect/misleading information | €7.5M or 1% global annual turnover |

For SMEs and startups, the lower of the two amounts applies.

## Disclaimer

This skill provides structured compliance workflow support based on Regulation (EU) 2024/1689. It does not constitute legal advice. Classification outcomes should be reviewed by qualified legal counsel before being relied upon for compliance decisions. The EU AI Act is subject to delegated acts, implementing acts, and guidance from the EU AI Office that may affect interpretation.
