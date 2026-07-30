---
name: gpai-code-of-practice
description: Assess compliance with the EU General-Purpose AI (GPAI) Code of Practice under the AI Act (Regulation (EU) 2024/1689, KI-Verordnung) Articles 51-56. Covers GPAI model identification (Art. 3(63)), systemic risk model designation (Art. 3(65), Art. 51, 10^25 FLOP training compute threshold), upstream provider obligations under Art. 53 (transparency, technical documentation, copyright policy and EU rights reservation, training data summary template), additional systemic risk obligations under Art. 55 (model evaluation benchmarks, adversarial red-teaming, AI Office incident notification under Art. 55(1)(c), cybersecurity), AI Office notification (Art. 52), downstream provider duties (Art. 25 quasi-provider), and Art. 53(2) open-source LLM exemption. Maps the 12 GPAI Code of Practice commitments across transparency, copyright, and safety-and-security chapters. DACH: BaFin, BSI, BNetzA, Betriebsrat. Use when asked about GPAI provider obligations, LLM or foundation model compliance, the Art. 51 systemic risk threshold, Art. 53 transparency requirements, Art. 55 systemic-risk obligations, AI Office notification, downstream Art. 25 duties, Art. 53(2) open-source exemption, or generative AI provider compliance under the EU AI Act.
---

# GPAI Code of Practice Compliance

Assess compliance with the EU General-Purpose AI Code of Practice (Final Version, July 2025) and underlying AI Act obligations (Articles 51–56).

**Important:** This skill provides compliance workflow support, not legal advice. The Code of Practice is voluntary — providers can demonstrate compliance through alternative means. Always cite specific articles, commitments, and measures. Where facts are incomplete, state assumptions explicitly and ask targeted follow-up questions.

## Compliance Workflow

Follow this decision tree strictly in order.

### Step 1 — Scope: Are You a GPAI Model Provider?

Determine whether the entity falls within scope.

**Definition (Article 3(63) + GPAI Guidelines):** A GPAI model is one "trained with a large amount of data" that displays "significant generality" and is "capable of competently performing a wide range of distinct tasks." Indicative threshold: trained with >10^23 FLOPs and capable of generating text, audio, images, or video.

Check:
1. Does the entity develop or have developed a GPAI model and place it on the EU market under its own name/trademark?
2. Or does the entity modify/fine-tune an existing GPAI model significantly? (Indicative: ≥1/3 of original training compute or ≥1/3 of 10^23 FLOPs)
3. Is the model placed on the EU market or put into service in the EU?

**If YES to any** → The entity is a GPAI model provider. Proceed to Step 2.
**If NO** → May still be a downstream provider/deployer with separate obligations. Document why GPAI provider status does not apply and stop.

**Key distinction:** The release mode (API, open weights, enterprise licence) does not affect whether a model is GPAI. It affects which exemptions apply.

### Step 2 — Open-Source Exemption Check

Check whether the partial exemption under Article 53(2) applies:

- Is the model released under a free and open-source licence?
- Are the parameters (weights), model architecture info, and usage info publicly available?

**If YES to both:**
- **Exempt from** Transparency obligations (Article 53(1)(a) and (b)) — no technical documentation or downstream provider information required
- **Still required:** Copyright policy (Article 53(1)(c)), training data summary (Article 53(1)(d))
- **Exception to exemption:** If the model has systemic risk (Step 3), ALL obligations apply regardless of open-source status

**If NO** → All obligations apply. Proceed to Step 3.

### Step 3 — Systemic Risk Classification (Article 51)

Determine whether the GPAI model has systemic risk:

| Criterion | Threshold | Source |
|-----------|-----------|--------|
| Compute-based presumption | Training compute >10^25 FLOPs | Article 51(2) |
| Commission designation | High-impact capabilities or equivalent impact based on Annex XIII criteria | Article 51(1)(b) |

**If systemic risk → TWO obligation tiers apply:**
- Tier 1: All GPAI provider obligations (Articles 53–54) — Transparency + Copyright chapters
- Tier 2: Additional systemic risk obligations (Article 55) — Safety & Security chapter

**If no systemic risk → Tier 1 only.**

→ Currently ~5–15 companies worldwide have models meeting the systemic risk threshold.

### Step 4 — Tier 1: All GPAI Provider Obligations

Assess compliance with each obligation. The Code of Practice provides the compliance framework through two chapters:

#### Chapter 1: Transparency (Commitment 1, Measures 1.1–1.3)

| Obligation | AI Act Source | Code Measure | Key Requirements |
|-----------|--------------|-------------|-----------------|
| Technical documentation | Art. 53(1)(a), Annex XI | Measure 1.1 | Model Documentation Form — licensing, architecture, training, datasets, compute, energy |
| Downstream provider info | Art. 53(1)(b), Annex XII | Measure 1.2 | Capabilities, limitations, integration info — deliver within 14 days of request |
| Documentation integrity | Art. 53(1)(a)–(b) | Measure 1.3 | Accurate, tamper-proof, securely stored for ≥10 years |
| Training data summary | Art. 53(1)(d) | GPAI Template | Mandatory public disclosure — data sources, types, volumes, compliance measures |

→ For complete transparency requirements and the Model Documentation Form, read [references/transparency-obligations.md](references/transparency-obligations.md).

#### Chapter 2: Copyright (Commitment 1, Measures 1.1–1.7)

| Obligation | Code Measure | Key Requirements |
|-----------|-------------|-----------------|
| Copyright policy | Measure 1.1 | Draw up, publish summary, define accountability |
| Lawful access only | Measure 1.2 | No circumventing paywalls; exclude piracy sites |
| Rights reservations | Measure 1.3 | Comply with robots.txt and machine-readable opt-outs |
| Record-keeping | Measure 1.4 | Maintain records of crawling and rights compliance |
| Output safeguards | Measure 1.5 | Technical measures to minimise infringing outputs |
| Terms of service | Measure 1.6 | Prohibit unauthorised copyright use by users |
| Complaints handling | Measure 1.7 | Designated contact point, fair complaint process |

→ For complete copyright requirements, read [references/copyright-obligations.md](references/copyright-obligations.md).

### Step 5 — Tier 2: Systemic Risk Obligations (Article 55)

**Only if the model has systemic risk (Step 3).** Assess compliance with the Safety & Security chapter (Commitments 1–10):

| Commitment | Focus | Key Requirements |
|-----------|-------|-----------------|
| 1 | Safety & Security Framework | Create, implement, update, notify AI Office |
| 2 | Systemic risk identification | Structured process + risk scenarios |
| 3 | Systemic risk analysis | Evaluations, modelling, monitoring |
| 4 | Risk acceptance determination | Acceptance criteria + proceed/stop decision |
| 5 | Safety mitigations | Lifecycle safety measures |
| 6 | Security mitigations | Cybersecurity for model + infrastructure |
| 7 | Model Reports | Pre-market report to AI Office, keep updated |
| 8 | Responsibility allocation | Clear roles, resources, risk culture |
| 9 | Serious incident reporting | Track, document, report within deadlines |
| 10 | Additional documentation | Record-keeping (10 years), public transparency |

→ For complete systemic risk requirements, read [references/systemic-risk-framework.md](references/systemic-risk-framework.md).

### Step 6 — DACH-Specific Considerations

If the provider or deployer operates in Germany, Austria, or Switzerland, check additional requirements:

- BNetzA as designated market surveillance authority for GPAI in Germany
- BSI alignment for cybersecurity (systemic risk models)
- Works council implications (BetrVG §87(1) No. 6) for internal GPAI deployment
- Austrian/Swiss territorial scope specifics

→ For DACH overlay details, read [references/dach-specific.md](references/dach-specific.md).

## Quick Start: Top 5 Actions for GPAI Providers

If a provider needs to move fast, these are the five highest-impact actions in priority order:

1. **Determine your status and sign the Code** — Are you a GPAI model provider? If yes, sign the Code of Practice. Non-signatories face heavier scrutiny and must prove compliance through alternative means. This is the single highest-leverage decision.

2. **Publish your training data summary** — Mandatory under Article 53(1)(d), no exemption, must be public. Use the Commission's GPAI Template. This is the most visible obligation — absence is immediately noticeable.

3. **Draft and publish your copyright policy** — Required for ALL providers including open-source. Must be operational, not a legal placeholder. Designate a complaints contact point. (See [references/copyright-obligations.md](references/copyright-obligations.md) for what a good policy looks like.)

4. **Complete the Model Documentation Form** — Technical documentation covering architecture, training, datasets, compute. Must be ready for AI Office requests. 14-day response window for downstream providers.

5. **If systemic risk: build your Safety & Security Framework** — This is the biggest lift. Start with Commitments 1–4 (Framework → Risk ID → Analysis → Acceptance). The Model Report (Commitment 7) depends on having these in place first.

**Enforcement timeline:** AI Office enforcement actions begin **2 August 2026** in current law. Legacy GPAI models (placed on the market before 2 August 2025) have until **2 August 2027**. The 7 May 2026 provisional Council/Parliament agreement on the Digital Omnibus leaves these GPAI dates **unchanged**; only Annex III high-risk and Annex I dates would shift if formally adopted. Until adoption plus Official Journal publication, current-law dates remain authoritative.

---

## Quick Question Set

Use these questions at intake to gather the information needed for assessment:

**Model & Provider**
1. What is the model? What are its capabilities (text, image, audio, video generation)?
2. Who developed it? Who places it on the EU market?
3. Estimated training compute (FLOPs)?
4. Is it open-source? If so, what licence? Are weights publicly available?

**Distribution & Use**
5. How is the model distributed (API, download, integrated product)?
6. Who are the downstream providers/deployers integrating this model?
7. Is the model fine-tuned or modified from a base model? By how much?

**Training Data**
8. What data sources were used for training?
9. Is web-scraped data involved? How are rights reservations handled?
10. What copyright compliance measures are in place?

**Risk & Compliance**
11. Has the model been designated as having systemic risk?
12. What documentation currently exists (model cards, technical docs)?
13. Has the provider signed the Code of Practice?
14. What cybersecurity measures protect the model and infrastructure?

If answers are incomplete, state assumptions explicitly and flag gaps.

## Reference Files

Load these as needed based on assessment progress:

| File | When to read |
|------|-------------|
| [references/transparency-obligations.md](references/transparency-obligations.md) | Assessing Transparency chapter — Model Documentation Form, Annex XI/XII requirements |
| [references/copyright-obligations.md](references/copyright-obligations.md) | Assessing Copyright chapter — policy, crawling, rights reservations, complaints |
| [references/systemic-risk-framework.md](references/systemic-risk-framework.md) | Model has systemic risk — all 10 Safety & Security commitments with measures |
| [references/compliance-timeline.md](references/compliance-timeline.md) | Building a compliance roadmap — all deadlines, enforcement dates, grace periods |
| [references/dach-specific.md](references/dach-specific.md) | Provider/deployer in Germany/Austria/Switzerland — BNetzA, BSI, works council |
| [references/templates.md](references/templates.md) | Producing deliverables — gap assessment, compliance memo, executive summary templates |

## Output Format

Every GPAI Code of Practice assessment produces three deliverables:

1. **Compliance Gap Assessment** — Systematic evaluation of each applicable commitment and measure, identifying gaps, current status (compliant/partial/non-compliant), and remediation actions with priority and timeline.

2. **GPAI Compliance Memo** — Formal record documenting the provider determination, scope analysis, applicable obligations, Code of Practice adherence status, cited articles and measures, and key assumptions.

3. **Executive Summary** — One-page summary for leadership with provider status, obligation tier, key gaps, enforcement timeline, and recommended next steps.

→ For complete templates, read [references/templates.md](references/templates.md).

## Enforcement & Penalties

| Violation | Maximum Fine | AI Act Source |
|-----------|-------------|---------------|
| Systemic risk obligations (Art. 55) | €15M or 3% global annual turnover | Art. 101(2) |
| General GPAI obligations (Art. 53) | €7.5M or 1% global annual turnover | Art. 101(3) |
| Incorrect/misleading information to AI Office | €7.5M or 1% global annual turnover | Art. 101(3) |

For SMEs and startups, the lower of the two amounts applies.

**Enforcement note:** While GPAI obligations apply since 2 August 2025, the AI Office's formal enforcement actions (requests for information, access to models, model recalls) begin 2 August 2026. This grace period is for working with the AI Office toward compliance — not a safe harbour.

Non-signatories to the Code of Practice face "a larger number of requests for information and requests for access" and must demonstrate compliance through alternative, potentially more burdensome means (Articles 53(4), 55(2), 56).

## Disclaimer

This skill provides structured compliance workflow support based on Regulation (EU) 2024/1689 and the GPAI Code of Practice (Final Version, July 2025). It does not constitute legal advice. The Code of Practice is a voluntary compliance tool — adherence creates a presumption of compliance but is not conclusive evidence. Assessment outcomes should be reviewed by qualified legal counsel. The EU AI Act is subject to delegated acts, implementing acts, harmonised standards (expected 2027+), and ongoing AI Office guidance that may affect interpretation.
