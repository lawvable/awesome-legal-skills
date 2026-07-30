# EU AI Act Article 50 Transparency Assessor — Deployment Guide

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Overview

EU AI Act **Article 50 Transparency Assessor** — a standalone-but-suite-aware skill that identifies which
of the Art. 50(1)–(5) transparency duties apply to a system and guides what must be implemented and by
when. It produces two deliverables: a formal **mini-report** and a per-obligation **compliance checklist**
with gap flags.

- **Five duties, two roles** — 50(1) interaction disclosure and 50(2) synthetic-content marking (provider);
  50(3) emotion/biometric notice and 50(4) deepfake/public-interest-text labelling (deployer); 50(5)
  delivery quality (cross-cutting)
- **Trigger + exemption logic** — the average-consumer obviousness test (50(1)), the assistive-function
  exemption (50(2)), the Art. 5 gate (50(3)), and the narrow 50(4) exceptions
- **Implementation depth** — the final Code of Practice's layered marking architecture, the official EU
  labelling icon set, and per-modality placement
- **Dated, Omnibus-aware roadmap** — 2 Aug 2026, the 2 Dec 2026 legacy grace (adopted by Council 29 Jun 2026,
  awaiting OJ), the 22 Jul 2026 signatory deadline, and the 2 Feb 2027 Code interoperability date
- **Standalone but chainable** — ingests the classifier's `ASSESSMENT CONTEXT` block and emits its own
  portable Art. 50 compliance block

## File Structure

```
ai-act-transparency/
├── SKILL.md                              # Main skill instructions (deploy this)
├── CHANGELOG.md                          # Version history
├── evals/
│   └── evals.json                        # Test cases
└── references/
    ├── art50-duties.md                   # The five duties + 50(6) governance
    ├── obviousness-and-exceptions.md     # Obviousness test, exemptions, boundaries, cross-provision interactions
    ├── code-of-practice-final.md         # Final Code of Practice (10 Jun 2026) — provider marking + deployer labelling
    ├── commission-guidelines-art50.md    # Draft Commission Guidelines (8 May 2026)
    ├── eu-labelling-icons.md             # Official EU icon set + design/placement requirements
    ├── timeline-and-grace.md             # Dated roadmap + Digital Omnibus grace (adopted, awaiting OJ)
    ├── implementation-checklists.md      # Provider / deployer / SME action checklists
    ├── report-template-art50.md          # Mini-report, checklist, and portable compliance block templates
    └── sources.md                        # Audit-grade source manifest (URLs, status, last-checked, uncertainty tiers)
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `ai-act-transparency/` folder structure
3. The skill auto-triggers on "Art. 50 transparency obligations", "do we need to label AI content /
   deepfakes", "AI chatbot disclosure", "synthetic content marking", "Kennzeichnungspflicht", or
   "Transparenzpflichten"

### Claude Code / Custom MCP Setup

1. Copy the `ai-act-transparency/` folder to your skills directory:
   ```bash
   cp -r ai-act-transparency/ /path/to/your/skills/user/ai-act-transparency/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Either start fresh or hand over context from a prior skill:

> "We're launching an AI support chatbot and an image generator under our own brand. What Article 50
> transparency duties apply, what do we implement, and by when?"

Or chain from the classifier:

> "Here's the ASSESSMENT CONTEXT block from the classifier — assess our Art. 50 transparency obligations
> and produce the report and checklist."

### Trigger Phrases

- "Check Art. 50 transparency obligations" / "Transparenzpflichten"
- "Do we need to label AI content / deepfakes" / "Kennzeichnungspflicht"
- "AI chatbot disclosure" / "synthetic content marking" / "watermarking"
- "What must we implement under Art. 50 and by when"

### Workflow

| Phase | Description |
|-------|-------------|
| **Phase 1: Intake** | System description + optional `ASSESSMENT CONTEXT` ingestion |
| **Phase 2: Role Determination** | Provider / deployer / both |
| **Phase 3: Trigger Determination** | Per-duty trigger + obviousness/exception test |
| **Phase 4: Implementation Deep-Dive** | What to build per triggered duty |
| **Phase 5: Dated Roadmap** | Omnibus-aware deadlines |
| **Phase 6: Output** | Mini-report + checklist + portable compliance block |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| EU AI Act | Regulation (EU) 2024/1689, Article 50 + recitals 132–137 |
| Deepfake definition | Art. 3(60) |
| Penalty band | Art. 99(4) — Tier 2 (EUR 15M / 3%) |
| Code of Practice on Transparency of AI-Generated Content | Final, 10 June 2026 (Art. 50(7)) |
| Commission Guidelines on Art. 50 | Draft, 8 May 2026 (Art. 96(1)(d)) |
| Digital Omnibus | 50(2) legacy-marking grace to 2 Dec 2026 — adopted (Council final green light 29 Jun 2026), awaiting OJ publication |

## License & Disclaimer

This skill produces structured Art. 50 transparency guidance based on Regulation (EU) 2024/1689, the final
Code of Practice on Transparency of AI-Generated Content, and the Commission's draft Art. 50 Guidelines. It
is not legal advice. The Code is voluntary and adherence is not conclusive evidence of compliance; only the
CJEU can authoritatively interpret Art. 50. Outputs should be reviewed by qualified legal counsel before
regulatory use.

Licensed under AGPL-3.0 — see [LICENSE](../../LICENSE) at the repo root.

---

*Created by Oliver Schmidt-Prietz — OneZero Legal*
