---
name: gpai-code-of-practice
description: Assess compliance with the EU General-Purpose AI (GPAI) Code of Practice under the AI Act (Regulation (EU) 2024/1689). Use when asked to determine GPAI model provider obligations, assess Code of Practice compliance, evaluate transparency or copyright requirements for GPAI models, check systemic risk obligations, build a GPAI compliance roadmap, or prepare for AI Office requests. Covers all three Code chapters (Transparency, Copyright, Safety & Security), the 12 commitments and their measures, systemic risk classification (Article 51), provider obligations (Articles 53 and 55), open-source exemptions, enforcement timeline, Commission/AI Office supervision, and DACH-specific overlays such as BSI cybersecurity and works council implications. Triggers on phrases like "GPAI compliance", "Code of Practice assessment", "GPAI model obligations", "systemic risk evaluation", "AI Act transparency requirements", "GPAI copyright policy", "general-purpose AI compliance".
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

#### Chapter 2: Copyright (Commitment 1, Measures 1.1–1.5)

| Obligation | Code Measure | Key Requirements |
|-----------|-------------|-----------------|
| Copyright policy | Measure 1.1 | Draw up, publish summary, define accountability |
| Lawful access only | Measure 1.2 | No circumventing paywalls; exclude piracy sites |
| Rights reservations | Measure 1.3 | Comply with robots.txt and machine-readable opt-outs |
| Output safeguards and user controls | Measure 1.4 | Technical safeguards plus acceptable-use, terms, or equivalent controls |
| Complaints handling | Measure 1.5 | Designated contact point and diligent, non-arbitrary complaint process |

Recommended evidence such as crawl logs and rights-reservation records supports compliance, but it is not a separate numbered Copyright measure.

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

- Commission/AI Office supervision of Chapter V GPAI obligations under Article 88; assess BNetzA and sector authorities separately for downstream AI systems and national overlays
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

**Enforcement timeline:** AI Office enforcement actions begin **2 August 2026**. Legacy GPAI models (placed on the market before 2 August 2025) have until **2 August 2027**. The Digital Omnibus amending the EU AI Act, adopted on 8 July 2026 and published in the Official Journal on 24 July 2026 as Regulation (EU) 2026/1744, leaves these GPAI dates **unchanged**; only the Annex III and Annex I high-risk application dates were deferred. The GPAI dates here remain authoritative.

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
| [references/dach-specific.md](references/dach-specific.md) | Provider/deployer in Germany/Austria/Switzerland — AI Office supervision, national interfaces, BSI, works council |
| [references/templates.md](references/templates.md) | Producing deliverables — gap assessment, compliance memo, executive summary templates |

## Output Format

Every GPAI Code of Practice assessment produces three deliverables:

1. **Compliance Gap Assessment** — Systematic evaluation of each applicable commitment and measure, identifying gaps, current status (compliant/partial/non-compliant), and remediation actions with priority and timeline.

2. **GPAI Compliance Memo** — Formal record documenting the provider determination, scope analysis, applicable obligations, Code of Practice adherence status, cited articles and measures, and key assumptions.

3. **Executive Summary** — One-page summary for leadership with provider status, obligation tier, key gaps, enforcement timeline, and recommended next steps.

→ For complete templates, read [references/templates.md](references/templates.md).

## Enforcement & Penalties

Art. 101(1) sets **one** ceiling for GPAI providers: fines up to **3% of annual total worldwide turnover in the preceding financial year or EUR 15 000 000, whichever is higher**, where the Commission finds the provider intentionally or negligently:

| Conduct covered | AI Act Source |
|-----------------|---------------|
| Infringed the relevant provisions of the Regulation (Arts. 53 and 55 obligations included) | Art. 101(1)(a) |
| Failed to comply with a request for a document or information under Art. 91, or supplied incorrect, incomplete or misleading information | Art. 101(1)(b) |
| Failed to comply with a measure requested under Art. 93 | Art. 101(1)(c) |
| Failed to make access to the model available for an evaluation under Art. 92 | Art. 101(1)(d) |

There are no separate 3% and 1% tiers for GPAI providers, and **no SME-lower rule in Art. 101**: Art. 99(6) applies by its own terms only to "each fine referred to in this Article", meaning Art. 99 operator fines, not Commission fines on GPAI providers. (The SMC cap added by Regulation (EU) 2026/1744 as Art. 99(6a) is likewise confined to Art. 99.)

**Enforcement note:** While GPAI obligations apply since 2 August 2025, the AI Office's formal enforcement actions (requests for information, access to models, model recalls) begin 2 August 2026. This grace period is for working with the AI Office toward compliance — not a safe harbour.

Non-signatories to the Code of Practice face "a larger number of requests for information and requests for access" and must demonstrate compliance through alternative, potentially more burdensome means (Articles 53(4), 55(2), 56).

## What changed for the codes on 27 July 2026 (Article 56(6))

Regulation (EU) 2026/1744 replaced Article 56(6) and removed the Commission's power to
approve a code of practice by implementing act and give it general validity across the
Union. The same act removed implementing-act empowerments in Article 50(7) and Article 72(3) too, though they were different powers: Article 50(7) keeps a fallback power to set common rules where a code is found inadequate, and the Article 72(3) power concerned a harmonised post-market-monitoring template, now replaced by Commission guidance including a template due 2 September 2027.

What the Commission does now: it monitors and evaluates, together with the Board, whether
participants are achieving the codes' objectives; it assesses, taking utmost account of the
Board's opinion, whether the codes cover the obligations in Articles 53 and 55; and it
publishes that adequacy assessment.

Three practical consequences for a provider relying on a code:

1. **No presumption of conformity.** The recitals state plainly that these codes have
   limited legal effect and in particular do not grant a presumption of conformity. Any
   advice or template that treats adherence as presumptive compliance is now wrong.
2. **Reliance still works, through a different route.** A provider may rely on a code
   assessed as adequate under Article 56(6), via Article 53(4) and, for systemic-risk models,
   Article 55(2), to demonstrate compliance. (Recital 41 of the amending act cites "53(4)
   and 54(2)"; Article 54(2) governs authorised representatives, so the operative pair is
   53(4) and 55(2).) The evidentiary weight comes from the published adequacy
   assessment, not from an implementing act.
3. **Document the delta.** Because adherence no longer carries a presumption, keep the
   mapping from each code commitment to the underlying Article 53 or 55 obligation, so
   compliance can be shown directly if the code is later assessed as inadequate.

The substantive GPAI obligations in Articles 51 to 55 and Annexes XI to XIII were not
amended, and the GPAI dates did not move: enforcement powers and fines from 2 August 2026,
and the Article 111(3) transition for models placed on the market before 2 August 2025
still runs to 2 August 2027.

## Disclaimer

This skill provides structured compliance workflow support based on Regulation (EU) 2024/1689 and the GPAI Code of Practice (Final Version, July 2025). It does not constitute legal advice. The Code of Practice is a voluntary compliance tool. Adherence does **not** create a presumption of conformity: the presumption attaches to harmonised standards, not to codes of practice. Regulation (EU) 2026/1744 (in force 27 July 2026) made this explicit and removed the general-validity approval route; see the note on Article 56(6) above. Assessment outcomes should be reviewed by qualified legal counsel. The EU AI Act is subject to delegated acts, implementing acts, harmonised standards, and ongoing AI Office guidance that may affect interpretation; verify the current official standardisation timeline rather than assuming an adoption date.
