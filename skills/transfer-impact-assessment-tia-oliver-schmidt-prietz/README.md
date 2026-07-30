# TIA (Transfer Impact Assessment) — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/GDPR-Transfer-Impact-Assessment/)**

## Overview

GDPR Transfer Impact Assessment skill — structured Chapter V transfer guidance for Claude. Combines:

- **EDPB Recommendations 01/2020** six-step methodology (regulatory backbone)
- **CNIL TIA Guide** (final version, January 2025) — structured assessment tables and three-way Step 3 conclusion
- **EDPB Recommendations 02/2020** — four essential guarantees framework for surveillance-law assessment
- **EDPB Guidelines 05/2021** — three cumulative criteria for transfer qualification, with 12 example scenarios
- **Rosenthal method** influence — pragmatic Step 3 Block C ("realistic risk to this data") without statistical probability calculations
- **12 pre-built country profiles** — US (non-DPF), US (DPF), UK, India, China, Brazil, Australia, Singapore, Turkey, UAE, South Africa, Russia + generic questionnaire
- **Balanced Art. 49 treatment** — EDPB Guidelines 2/2018 + OLG München (21 U 3882/25 e, 2026) judicial counter-position
- **Audit-ready output** — Markdown report + .docx formal document + JSON delta for RoPA interchange

## File Structure

```
skills/tia/
├── SKILL.md                              # Main skill instructions (deploy this)
├── CHANGELOG.md                          # Version history
├── README.md                             # This file
├── evals/
│   └── evals.json                        # 12 behavioural test cases
└── references/
    ├── edpb-six-steps.md                 # EDPB Rec 01/2020 methodology
    ├── essential-guarantees.md           # EDPB Rec 02/2020 four-pillar framework
    ├── transfer-qualification.md         # EDPB Guidelines 05/2021 — 3 criteria + 12 examples
    ├── art49-derogations.md              # Art. 49 balanced assessment (EDPB + judicial)
    ├── supplementary-measures.md         # Catalog (technical / contractual / organisational)
    ├── schrems-ii-holdings.md            # C-311/18 key holdings + implications
    ├── tia-template.md                   # Document template structure
    ├── interchange-delta.md              # RoPA delta format
    ├── sources.md                        # Regulatory source references
    └── country-profiles/
        ├── us-non-dpf.md                # USA outside DPF
        ├── us-dpf.md                    # USA DPF-certified
        ├── uk-post-adequacy.md          # UK (adequacy renewed Dec 2025)
        ├── in.md                        # India
        ├── cn.md                        # China
        ├── br.md                        # Brazil
        ├── au.md                        # Australia
        ├── sg.md                        # Singapore
        ├── tr.md                        # Turkey
        ├── ae.md                        # UAE (DIFC / ADGM / mainland)
        ├── za.md                        # South Africa
        ├── ru.md                        # Russia
        └── generic-assessment.md        # Guided questionnaire for unlisted countries
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent).
2. Upload the entire `tia/` folder structure.
3. The skill triggers on "TIA", "Transfer Impact Assessment", "Schrems II", "third-country transfer", "Art. 46", "Art. 49", and similar terms.

### Claude Code / Custom Setup

```bash
# Symlink the skill from the monorepo
ln -s ~/CLAUDE_PROJECTS/SKILLS/claude-skills/skills/tia ~/.claude/skills/tia
```

## Usage

### Quick Start

Example prompts that trigger the skill:

- "We're using SCCs Module 2 to transfer HR data to our payroll processor in India. Do I need supplementary measures?"
- "I need a TIA for our US cloud provider — they're DPF-certified."
- "Is remote support access from our Indian sub-processor considered a Chapter V transfer?"
- "Can we rely on Art. 49(1)(b) for our global SaaS user data flows to the US?"

### Trigger Phrases

- "TIA", "Transfer Impact Assessment"
- "Schrems II", "Chapter V"
- "Art. 44 / 45 / 46 / 47 / 49"
- "transfer to [country]" (US, India, China, etc.)
- "SCCs assessment", "BCRs"
- "supplementary measures"
- "DPF transfer", "EU-US Data Privacy Framework"
- "adequacy decision"
- "essential guarantees"
- "Drittlandsübermittlung", "Drittlandtransfer"

### Assessment Modes

| Mode | When | Output |
|---|---|---|
| Single transfer assessment | One known transfer | Markdown + .docx TIA |
| Batch / registry | Multiple transfers | Registry + per-transfer pipeline + Transfer Risk Summary |
| Discovery (standalone) | No RoPA, multiple transfers | Discovery walkthrough → registry → assessments |
| RoPA import | Has RoPA sidecar | Import transfers → assess each |
| Adequacy fast-track | Destination has adequacy | Lightweight assessment + monitoring triggers |
| Art. 49 path | Derogation potentially applies | Balanced assessment (EDPB + judicial) |
| Transfer qualification only | "Is this even a transfer?" | Qualification finding |
| Review / update | Existing TIA + legal change | Re-assessment of affected sections |

## Outputs

| Format | Purpose |
|---|---|
| Markdown TIA Report | In-session preview, working document |
| .docx Formal TIA Document | Compliance file, CNIL-style tables, sign-off block |
| JSON Delta | RoPA interchange — patches `tia_ref`, `tia_status`, `supplementary_measures[]`, dates |
| Transfer Risk Summary | One-page executive overview for batch assessments |

## Regulatory Basis

| Document | Reference | Purpose |
|---|---|---|
| GDPR Chapter V | Arts. 44–49 | Statute |
| Schrems II | CJEU C-311/18 (16 July 2020) | Adequacy + TIA obligation |
| EDPB Rec 01/2020 | v2.0 (18 June 2021) | Six-step methodology |
| EDPB Rec 02/2020 | (10 November 2020) | Essential guarantees |
| EDPB Guidelines 05/2021 | v2.0 (14 February 2023) | Transfer qualification |
| EDPB Guidelines 2/2018 | (25 May 2018) | Art. 49 derogations (EDPB view) |
| CNIL TIA Guide | January 2025 (final) | Practical structured tables |
| OLG München, 21 U 3882/25 e | (11 May 2026) | Art. 49(1)(b) for global services |
| Implementing Decision (EU) 2023/1795 | (10 July 2023) | EU-US DPF adequacy |

## Cross-Skill Integration

| Skill | Direction | What flows |
|---|---|---|
| RoPA | Inbound | Read sidecar; filter third-country transfers; pre-populate Step 1 |
| RoPA | Outbound | Emit delta file per assessed transfer (conforming to RoPA inbound schema v1.0) |
| DPIA Sentinel | Flag only | If Step 3 reveals high-risk processing, flag for Art. 35 DPIA consideration (no auto-trigger) |

## Version History

See [CHANGELOG.md](CHANGELOG.md) for full version history.

## License & Disclaimer

AGPL-3.0. See repository LICENSE.

**This skill provides structured GDPR Chapter V guidance based on EDPB Recommendations, CNIL guidance, and emerging case law. It is not legal advice. Involve your DPO and qualified counsel for final decisions, especially where the skill flags a transfer for suspension or restructuring. The skill's country profiles reflect the law and practice as of the "Last verified" date stated in each profile — verify current status before formal use.**

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
