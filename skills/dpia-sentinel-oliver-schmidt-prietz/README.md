# DPIA Sentinel — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/GDPR-DPIA-Sentinel/)**

## Overview

GDPR Data Protection Impact Assessment Sentinel — a structured DPIA guidance skill for Claude that provides:

- **Threshold assessment** against Art. 35(3) mandatory triggers and EDPB nine-criteria analysis
- **Multi-jurisdictional blacklist/whitelist checks** across 7 EU Member States (DE, FR, IE, BE, NL, IT, PL)
- **EDPB 2026 DPIA Template support** — generate documents in the official harmonised EU format (Sections 0–6)
- **Two-track risk model** — inherent-by-design risks (Track A) and operational risks (Track B) per EDPB methodology
- **5×5 risk assessment** with modulating factors, from the data subject's perspective
- **Implementation status tracking** for all measures (Planned / Partially Implemented / Implemented)
- **Necessity and proportionality** as separate upstream assessment gates
- **Asset inventory** for risk-relevant processing infrastructure
- **Art. 36 prior consultation** decision support with four-outcome verdict
- **AI dual-phase analysis** per EDPB Opinion 28/2024 (training vs. deployment)
- **Audit-ready .docx document generation** via template population (EDPB 2026 format, custom 12-section report, threshold memo, executive summary, Art. 36 package)

## File Structure

```
dpia-skill/
├── SKILL.md                              # Main skill instructions (deploy this)
├── CHANGELOG.md                          # Version history
└── references/
    ├── edpb-criteria.md                  # EDPB nine criteria + multi-jurisdictional framework
    ├── edpb-2026-template.md             # EDPB 2026 DPIA template field-by-field spec
    ├── edpb-2026-template-v1.docx        # Official EDPB template .docx (populatable)
    ├── edpb-2026-population.md           # Table-by-table population guide for the template
    ├── edpb-2026-explainer.md            # EDPB 2026 methodology reference
    ├── dpia-custom-template-v1.docx      # Custom 12-section DPIA template .docx (populatable)
    ├── dpia-custom-population.md         # Population guide for custom template
    ├── scoring.md                        # 5×5 risk scoring + modulating factors + two tracks
    ├── risk-catalog.md                   # Common DPIA risks by processing type (Track A+B)
    ├── templates.md                      # Document templates (5 formats)
    ├── sources.md                        # Regulatory source references
    └── jurisdictions/
        ├── de-dsk.md                     # Germany — DSK blacklist
        ├── fr-cnil.md                    # France — CNIL blacklist
        ├── ie-dpc.md                     # Ireland — DPC blacklist
        ├── be-apd.md                     # Belgium — APD blacklist
        ├── nl-ap.md                      # Netherlands — AP blacklist
        ├── it-garante.md                 # Italy — Garante blacklist
        ├── pl-uodo.md                    # Poland — UODO blacklist
        └── whitelists.md                 # FR, CZ, ES, AT whitelist exemptions
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `dpia-skill/` folder structure
3. The skill will auto-trigger when you mention DPIA, DSFA, Art. 35, or describe high-risk processing

### Claude Code / Custom MCP Setup

1. Copy the `dpia-skill/` folder to your skills directory:
   ```bash
   cp -r dpia-skill/ /path/to/your/skills/user/dpia-skill/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Just describe your processing activity:

> "We're planning to deploy an AI system that scores job applicants based on their CVs
> and video interviews. The system will be used across Germany, France, and the Netherlands.
> Do we need a DPIA?"

The skill will activate and guide you through the assessment.

### Trigger Phrases

- "Do I need a DPIA?" / "DSFA" / "Datenschutz-Folgenabschaetzung"
- "Art. 35" / "impact assessment" / "high-risk processing"
- "We want to deploy AI for..." / "profiling" / "large-scale monitoring"
- "Generate a DPIA report"

### Assessment Flow

| Phase | Description |
|-------|-------------|
| **Threshold** | Art. 35(3) triggers + nine-criteria analysis + national blacklist checks |
| **Description** | Systematic processing description per Art. 35(7)(a) |
| **Asset Inventory** | Risk-relevant assets grouped by type (EDPB 2026, Section 1.3) |
| **Necessity** | Effectiveness + least-intrusive test (upstream gate) |
| **Proportionality** | Benefits vs. impact balancing (upstream gate) |
| **Inherent Risks** | Track A (by-design) + Track B (operational), 5×5 matrix + modulating factors |
| **Mitigation** | Technical, organizational, and legal measures with implementation status |
| **Residual Risk** | Overall verdict: APPROVED / CONDITIONALLY APPROVED / CONSULT SA / REJECTED |
| **Documentation** | Audit-ready .docx generation (EDPB 2026 or custom format) |

## Document Types

| Template | Description |
|----------|-------------|
| EDPB 2026 DPIA Report | Official harmonised format (Sections 0–6, recognized by all EU SAs) |
| Full DPIA Report (custom) | Custom 12-section assessment with threshold analysis + annexes |
| Threshold Justification Memo | 2-3 page document explaining why a DPIA is NOT required |
| Executive Summary | 1-2 page board/leadership summary |
| Art. 36 Consultation Package | Submission package for SA prior consultation |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| GDPR Article 35 | DPIA obligation |
| GDPR Article 36 | Prior consultation |
| EDPB DPIA Template v1.0 (March 2026) | Harmonised EU-wide DPIA structure |
| EDPB Guidelines WP 248 rev.01 | DPIA methodology and nine criteria |
| EDPB Opinion 28/2024 | DPIA for AI processing |
| EDPB Guidelines 01/2025 | Pseudonymisation as risk reducer |
| National SA Art. 35(4) lists | Mandatory DPIA blacklists (7 jurisdictions) |

## Version History

See [CHANGELOG.md](CHANGELOG.md) for full version history.

## License & Disclaimer

This skill provides structured guidance based on publicly available GDPR regulatory materials. It does not constitute legal advice. All DPIA decisions should involve your DPO (Art. 35(2)) and qualified legal counsel.

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
