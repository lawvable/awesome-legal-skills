# EU AI Act System Classifier — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/EU-AI-Act-Suite/ai-act-classifier/)**

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Overview

EU AI Act System Classifier — a structured AI Act assessment skill for Claude that provides:

- **Art. 2 scope-exclusion analysis** (military, personal use, pure R&D, pre-market, international law enforcement) with system-description-informed targeting
- **Art. 3(1) AI system definition test** — 7-criteria analysis grounded in Commission guidelines and the OECD AI framework
- **Open-source exemption checklists** — dedicated paths for Art. 2(12) (AI systems) and Art. 53(2) (GPAI models)
- **Art. 5 prohibited-practice screening** with subject-centric reading per Commission Guidelines
- **High-risk classification** — Annex I product safety route + Annex III application-based route
- **Art. 6(3) exception assessment** with Art. 6(4) documentation requirements
- **GPAI model assessment** running in parallel with risk-tier classification — standard GPAI (Art. 53) and systemic-risk GPAI (Art. 55)
- **Art. 50 transparency-obligation triggers** with Code of Practice multi-layered marking guidance
- **Sector-specific guidance** for high-risk Annex III categories (employment, education, biometrics, law enforcement, etc.)
- **Compliance deadline lookup** by risk tier and provider/deployer role
- **Classification Dashboard output** — single-page summary with legal basis, deadlines, and follow-up actions

## File Structure

```
ai-act-classifier/
├── SKILL.md                              # Main skill instructions (deploy this)
├── CHANGELOG.md                          # Version history
├── evals/
│   └── evals.json                        # 3 test cases (with-skill vs. baseline)
└── references/
    ├── ai-system-definition.md           # Art. 3(1) 7-criteria test + worked examples
    ├── scope-exclusions.md               # Art. 2 exclusion checklists (incl. open-source)
    ├── prohibited-practices.md           # Art. 5 prohibitions — full subject-centric analysis
    ├── high-risk-annexes.md              # Annex I + Annex III routes
    ├── art6-exception.md                 # Art. 6(3) exception with Art. 6(4) docs
    ├── gpai-systemic-risk.md             # Art. 51/53/55 GPAI thresholds and obligations
    ├── art50-transparency.md             # Art. 50 transparency + Code of Practice marking
    ├── sector-guidance.md                # Sector-specific high-risk guidance
    ├── jurisdiction-requirements.md      # Member-state-specific implementation notes
    ├── compliance-deadlines.md           # Deadlines by tier + role
    ├── enforcement-framework.md          # Penalties, market surveillance, AI Office
    └── case-studies.md                   # Worked classification examples
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `ai-act-classifier/` folder structure
3. The skill will auto-trigger when you mention AI Act classification, risk tiers, KI-Verordnung, Annex III, prohibited practices, or GPAI systemic risk

### Claude Code / Custom MCP Setup

1. Copy the `ai-act-classifier/` folder to your skills directory:
   ```bash
   cp -r ai-act-classifier/ /path/to/your/skills/user/ai-act-classifier/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Describe the AI technology you want to classify:

> "We're building a CV-screening tool that ranks job applicants for our HR team.
> It uses a fine-tuned LLM to score candidates against job descriptions. Do we
> need to treat this as high-risk under the AI Act?"

The skill will activate and walk you through the classification.

### Trigger Phrases

- "Classify an AI system under the AI Act" / "AI Act risk tier"
- "Is this an AI system?" / "Art. 3(1)" / "Prohibited practice?"
- "High-risk classification" / "Annex III" / "Art. 6 exception"
- "GPAI systemic risk" / "KI-Verordnung" / "Risikoklassifizierung"

> For a pure article-lookup question *without* producing a classification, answer
> it directly from the cited regulation text rather than running the classifier.

### Workflow

| Phase | Description |
|-------|-------------|
| **Phase 1: Scope Gate** | Art. 2 exclusion analysis (military, personal, R&D, pre-market, ILE) + open-source checklist (Art. 2(12) / Art. 53(2)) |
| **Phase 2: AI System Test** | Art. 3(1) 7-criteria definition test grounded in Commission guidelines and OECD framework |
| **Phase 3: Risk Classification** | Steps 1–3 in sequence (Art. 5 → Annex I → Annex III + Art. 6(3) exception); Step 4 GPAI assessment runs **in parallel**; Step 5 Art. 50 transparency check |
| **Phase 4: Classification Dashboard** | Single-page output: risk tier, legal basis, deadlines, obligations summary, next-step recommendations |

## Capabilities Summary

| Feature | Description |
|---------|-------------|
| Scope Exclusion (Art. 2) | System-description-informed targeting — only relevant exclusions surfaced |
| Open-Source Checklist | Dedicated 3-step process for Art. 2(12) AI systems and Art. 53(2) GPAI models |
| AI System Definition | 7-criteria Art. 3(1) test with Commission/OECD guidance |
| Prohibited Practices | Art. 5 screening — subject-centric reading per Commission Guidelines |
| High-Risk: Annex I | Product-safety route (Art. 6(1)) |
| High-Risk: Annex III | Application-based route (Art. 6(2)) with Art. 6(3) exception |
| Art. 6(3) Exception | Documented carve-out with Art. 6(4) registration obligations |
| GPAI Assessment | Parallel track — standard GPAI (Art. 53) + systemic-risk GPAI (Art. 55) |
| Art. 50 Transparency | Interaction, synthetic content, emotion recognition, deepfake labeling |
| Sector Guidance | Targeted guidance for Annex III categories (employment, education, biometrics, etc.) |
| Jurisdiction Notes | Member-state-specific implementation requirements |
| Deadline Lookup | Compliance dates by tier (prohibited / high-risk / GPAI / Art. 50 / minimal) |
| Classification Dashboard | Single-page summary output |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| EU AI Act | Regulation (EU) 2024/1689 |
| Commission Guidelines on AI System Definition | Art. 3(1) interpretation |
| Commission Guidelines on Prohibited AI Practices | Art. 5 enforcement reading |
| Commission Guidelines on High-Risk Classification | Art. 6 + Annex III |
| OECD AI Framework | Underlying technical definition |
| GPAI Code of Practice | Art. 53/55 implementation |
| Art. 50 Code of Practice (Transparency) | Multi-layered marking framework |

## License & Disclaimer

This skill provides structured guidance based on the EU AI Act (Regulation (EU) 2024/1689), Commission guidelines, and the OECD AI framework. It does not constitute legal advice. Final classification decisions should involve qualified legal counsel with AI Act expertise.

Licensed under AGPL-3.0.

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
