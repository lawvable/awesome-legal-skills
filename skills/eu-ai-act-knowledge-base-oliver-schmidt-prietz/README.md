# EU AI Act Knowledge Engine — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/EU-AI-Act-Suite/ai-act-knowledge/)**

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Overview

EU AI Act Knowledge Engine — an authoritative regulatory Q&A skill grounded in 70 official EU source documents:

- **Article-level citations** from the full text of Regulation (EU) 2024/1689
- **Full preamble + 13 Titles** covered by structured reference files (Titles I–XIII)
- **Commission guidelines** on AI system definition, prohibited practices, high-risk classification, and Digital Omnibus
- **EDPB/EDPS opinions** including Opinion 28/2024 (AI-DPIA interplay) and 2026 joint opinion
- **Codes of Practice** — GPAI Code (3 versions), Transparency Code (drafts + overview)
- **FRIA materials** — Art. 27 text, Danish Institute guide, ECNL practical guide
- **Harmonised standards** — Art. 40 framework, prEN 18286, JTC 21 roadmap
- **Sector-specific guidance** for banking, medical devices, staffing, healthcare, law enforcement
- **National implementation tracking** — German AI bill, regulatory sandboxes, national service desks
- **Incident reporting templates** — GPAI serious incident, Art. 73 high-risk draft guidance

## File Structure

```
ai-act-knowledge/
├── SKILL.md                          # Main skill instructions (deploy this)
├── CHANGELOG.md                      # Version history
└── references/                       # 70 reference files across 15 subdirectories
    ├── core/                         # Regulation text by Title (I–XIII) + preamble + Annex III + decision trees
    ├── guidelines/                   # Commission guidelines (AI system definition, prohibited, GPAI, omnibus)
    ├── codes-of-practice/            # GPAI Code + Transparency Code (multiple versions)
    ├── opinions/                     # EDPB/EDPS opinions (2021, 2026, 28/2024)
    ├── standards/                    # Art. 40 harmonised standards, prEN 18286, JTC 21
    ├── fria/                         # Art. 27 FRIA — text + practical guides
    ├── governance/                   # AI Office FAQ, AI Pact, enforcement, timeline
    ├── national/                     # National implementation (DE bill, sandboxes, service desks)
    ├── sector-specific/              # Banking, medical devices, staffing
    ├── cybersecurity/                # ENISA advisories
    ├── law-enforcement/              # Europol AI policing
    ├── compliance-guides/            # AI literacy, SME guide, copyright/TDM, whistleblowing
    ├── impact-assessments/           # Commission IA + supporting study + healthcare 2026
    └── templates/                    # GPAI training data, serious incident, high-risk draft
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `ai-act-knowledge/` folder structure
3. The skill will auto-trigger when you ask about AI Act articles, requirements, penalties, GPAI obligations, FRIA, or any AI Act topic

### Claude Code / Custom MCP Setup

1. Copy the `ai-act-knowledge/` folder to your skills directory:
   ```bash
   cp -r ai-act-knowledge/ /path/to/your/skills/user/ai-act-knowledge/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Ask any AI Act question:

> "What does Art. 27 require for a Fundamental Rights Impact Assessment, and
> when does it apply to deployers of high-risk systems?"

The skill will route to the right reference files and produce a cited answer.

### Trigger Phrases

- "Explain Art. X" / "What does Article X say?" / "AI Act requirements"
- "GPAI obligations" / "High-risk AI" / "Prohibited AI practices"
- "AI Act and GDPR" / "Fundamental rights impact assessment" / "AI literacy"
- "KI-Verordnung" / "Hochrisiko-KI" / "GPAI-Verhaltenskodex"

> For assessment workflows that produce a classification decision (rather than a
> knowledge answer), ask for a structured risk-tier classification.

### Workflow

| Step | Description |
|------|-------------|
| **1. Classify Question** | Topic Router determines which reference subdirectory(ies) to consult |
| **2. Load References** | Read targeted reference files (article text, guidelines, opinions, codes) |
| **3. Synthesise** | Produce answer with article-level citations and cross-references to related provisions |

## Capabilities Summary

| Feature | Description |
|---------|-------------|
| Article-Level Q&A | Direct answers grounded in the full regulation text (preamble + 13 Titles) |
| Commission Guidelines | AI system definition, prohibited practices, high-risk, Digital Omnibus |
| EDPB/EDPS Opinions | 2021 joint, 2026 joint, Opinion 28/2024 (AI-DPIA) |
| Codes of Practice | GPAI Code (3 versions), Transparency Code (drafts + overview) |
| FRIA Materials | Art. 27 text + Danish Institute and ECNL practical guides |
| Harmonised Standards | Art. 40 framework, prEN 18286, JTC 21 roadmap |
| Sector Guidance | Banking, medical devices, staffing, healthcare, law enforcement |
| National Implementation | German AI bill, regulatory sandboxes, Member State service desks |
| Incident Templates | GPAI serious incident reporting, Art. 73 high-risk draft |
| Cross-Framework | AI Act ↔ GDPR, ENISA cybersecurity overlays |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| EU AI Act | Regulation (EU) 2024/1689 (full text + recitals) |
| Commission Guidelines | AI system definition, Art. 5 prohibitions, Art. 6 high-risk, Digital Omnibus |
| EDPB Opinion 28/2024 | DPIA for AI processing |
| EDPB-EDPS Joint Opinions | 2021 and 2026 |
| GPAI Code of Practice | Art. 53/55 implementation framework |
| Art. 50 Code of Practice | Transparency labeling framework |
| Art. 40 Harmonised Standards | JTC 21 framework, prEN 18286 |
| ENISA Advisories | AI cybersecurity, standardisation |

## License & Disclaimer

This skill provides structured AI Act regulatory information based on Regulation (EU) 2024/1689 and official EU institutional sources. It is not legal advice. Specific compliance decisions should involve qualified legal counsel with AI Act expertise.

Licensed under AGPL-3.0.

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
