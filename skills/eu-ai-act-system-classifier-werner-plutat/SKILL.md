---
name: eu-ai-act-classification
description: Classify AI systems under the EU AI Act (Regulation (EU) 2024/1689) and determine compliance obligations. Use when asked to assess AI risk level, check if an AI system is prohibited, determine high-risk status, identify GPAI model obligations, map provider/deployer responsibilities, or build an AI Act compliance roadmap. Covers the full classification decision tree (Prohibited → High-Risk → Limited → Minimal → GPAI), obligations by role (provider, deployer, importer, distributor), compliance timelines, and DACH-specific considerations (German works council, BaFin, BSI, BNetzA). Triggers on phrases like "classify this AI system", "is this high-risk under the AI Act", "AI Act risk assessment", "EU AI Act compliance", "prohibited AI practice", "GPAI obligations", "AI Act timeline".
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

Categories (check all ten: the original eight, plus Art. 5(1)(ba) non-consensual intimate material and (bb) CSAM, both applying from 2 December 2026):
1. Manipulation/deception causing significant harm
2. Exploitation of vulnerabilities (age, disability, socio-economic)
3. Social scoring with disproportionate/unrelated adverse treatment
4. Individual predictive policing based solely on profiling
5. Untargeted facial image scraping for recognition databases
6. Emotion recognition in workplace/education (narrow exceptions)
7. Biometric categorisation inferring sensitive characteristics
8. Real-time remote biometric identification in public spaces for law enforcement (narrow exceptions)
9. Non-consensual intimate material: generating or manipulating realistic intimate or sexually explicit depictions of an identifiable person without their explicit consent (Art. 5(1)(ba), from 2 Dec 2026)
10. Child sexual abuse material within the meaning of Directive 2011/93/EU, subject to the national "without right" defence (Art. 5(1)(bb), from 2 Dec 2026)

→ For the complete checklist with examples and edge cases, read [references/prohibited-practices.md](references/prohibited-practices.md).

### Step 3 — Gate 2: High-Risk (Annex I + Annex III)

**Annex I path:** Is the AI a product or safety component under EU harmonisation legislation (e.g., MDR, IVDR) subject to third-party conformity assessment? → **HIGH-RISK**

> **Annex I Section A vs Section B.** For products covered by Section B, Regulation (EU) 2024/1689 applies only to the extent set out in its Article 2(2), so the full Chapter III regime does not attach. Regulation (EU) 2026/1744 moved the Machinery Regulation (EU) 2023/1230 from Section A to Section B with effect from 27 July 2026, so AI-enabled machinery now follows the sectoral route. Note that Article 2(2) was itself rewritten by the same act: for Section B products only Article 6(1), the new Article 60a and Articles 102 to 112 apply, with Articles 57 to 59 applying only in so far as the high-risk requirements have been integrated into that sectoral legislation.

> **The safety-component gateway narrowed on 27 July 2026.** Before concluding HIGH-RISK on the Annex I path, apply the new Article 6(1a) to (1c) and the amended Article 3(14):
>
> - **Article 3(14)** now ties "safety component" to intended purpose: a component fulfils a safety function where its intended purpose is to prevent or mitigate risks to the health and safety of persons or property. Mere integration into a regulated product does not make it one.
> - **Article 6(1a)**: systems used solely for non-safety related aspects of user assistance, performance optimisation, service efficiency, automation, convenience or quality control do **not** qualify as safety components.
> - **Article 6(1b)**: despite 1a, a system whose failure or malfunctioning would endanger health and safety **does** qualify.
> - **Article 6(1c)**: a product required to undergo third-party conformity assessment **solely** for risks other than health and safety, for example radio spectrum or electromagnetic interference, does not satisfy Article 6(1)(b).
>
> Practical effect: several systems that previously classified as high-risk by virtue of sitting inside a regulated product now fall outside Article 6(1). Document which limb you relied on.

**Annex III path:** Does the intended purpose fall within one of the eight high-risk use-case categories?

| # | Category | Quick examples |
|---|----------|---------------|
| 1 | Biometrics | Remote identification (1:1 verification of a claimed identity is expressly excluded), categorisation by sensitive attributes, emotion recognition |
| 2 | Critical infrastructure | Energy grid control, water systems, traffic management |
| 3 | Education | Admissions, grading, learning access decisions |
| 4 | Employment | CV screening, promotion, termination, task allocation |
| 5 | Essential services | Public-benefit eligibility, credit scoring (fraud detection excluded), life and health insurance pricing, emergency triage |
| 6 | Law enforcement | Risk assessment, evidence evaluation, profiling |
| 7 | Migration & border | Border risk assessment, examination of asylum/visa/residence applications (travel-document verification excluded) |
| 8 | Justice & democracy | Judicial assistance, electoral process systems |

→ For all categories with examples and edge cases, read [references/high-risk-annex-iii.md](references/high-risk-annex-iii.md).

**Article 6(3) exception:** Even if an Annex III use case matches, a system is NOT high-risk if it does not pose a significant risk of harm to health, safety or fundamental rights, including by not materially influencing the outcome of decision making, and one of these conditions is met:
- it performs a narrow procedural task,
- it improves the result of a previously completed human activity,
- it detects decision-making patterns or deviations from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment without proper human review, or
- it performs a preparatory task for an assessment relevant for the purposes of the use cases listed in Annex III.

**Profiling override, check this FIRST:** notwithstanding those conditions, an Annex III system is **always** high-risk where it performs profiling of natural persons (Art. 6(3), third subparagraph). If the system profiles people, the exception is unavailable and the analysis stops here.

If claiming this exception, document the reasoning thoroughly (Art. 6(4)), and note the Art. 49(2) registration duty for systems relying on it.

### Step 4 — GPAI Models (Articles 51–56)

Independent of system-level risk. A minimal-risk app can use a GPAI model with its own obligations. Downstream providers/deployers must still verify vendor evidence and ensure documentation is sufficient for their specific use case and risk profile.

Check:
- Is a general-purpose AI model involved (broad capability, not narrow-purpose)?
- Who is the GPAI model provider vs. downstream provider?
- Does the model meet systemic risk thresholds (compute-based criteria or designation by the Commission)?

→ For GPAI obligations and systemic risk details, read [references/gpai-obligations.md](references/gpai-obligations.md).

### Step 5 — Gate 3: Limited Risk (Article 50)

If not prohibited or high-risk, check Article 50 transparency duties. Who owes each duty differs by paragraph:
- **Art. 50(1), provider:** systems intended to interact directly with natural persons must be designed so people are informed they are dealing with AI, unless this is obvious to a reasonably well-informed, observant and circumspect person in the circumstances. The obviousness exception belongs to this paragraph only.
- **Art. 50(2), provider:** synthetic audio, image, video or text output must be marked in a machine-readable format as artificially generated or manipulated.
- **Art. 50(3), deployer:** emotion recognition and biometric categorisation systems require informing the exposed persons.
- **Art. 50(4), deployer:** deepfakes must be disclosed, as must AI-generated or manipulated text published to inform the public on matters of public interest, subject to the stated carve-outs.

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
| Prohibited practices | €35M or 7% global annual turnover, whichever is higher for an undertaking |
| High-risk system obligations | €15M or 3% global annual turnover, whichever is higher for an undertaking |
| Incorrect/misleading information | €7.5M or 1% global annual turnover, whichever is higher for an undertaking |

For SMEs, including startups, the lower of the amount or percentage applies to each Article 99 fine. For SMCs, that lower-of rule applies only to the fines in Article 99(4) and (5), not to prohibited-practice fines under Article 99(3).

## Disclaimer

This skill provides structured compliance workflow support based on Regulation (EU) 2024/1689. It does not constitute legal advice. Classification outcomes should be reviewed by qualified legal counsel before being relied upon for compliance decisions. The EU AI Act is subject to delegated acts, implementing acts, and guidance from the EU AI Office that may affect interpretation.
