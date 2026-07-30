# EU AI Act Examination Report Generator — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/EU-AI-Act-Suite/ai-act-report/)**

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Overview

EU AI Act Examination Report Generator — produces a formal, structured AI Act compliance assessment report suitable for legal files, audit trails, and regulatory inquiries:

- **9-section report structure** — introduction, system description, scope-exclusion check, scope of application, intended purpose, risk classification, applicable obligations, risk flags, conclusion
- **Context-first adaptive intake** — consumes prior assessment outputs (classification, role determination, obligation mapping, quick triage) when available
- **Input validation phase** — explicit Phase 1.5 to flag missing or inconsistent context before drafting
- **Citation-grounded prose** — legal citations index keeps article references consistent
- **Jurisdiction checklists** for Member-State-specific compliance items
- **Quality-check phase** before delivery (Phase 3)
- **Word document export** with formatted output (Phase 4)
- **Output templates** for assessment, gap analysis, regulator submission, and internal memo

## File Structure

```
ai-act-report/
├── SKILL.md                              # Main skill instructions (deploy this)
├── CHANGELOG.md                          # Version history
├── evals/
│   └── evals.json                        # Test cases
└── references/
    ├── report-template.md                # 9-section master template
    ├── output-templates.md               # Variant templates (assessment, gap, regulator, memo)
    ├── legal-citations-index.md          # Article-reference index for consistency
    ├── interpretation-aids.md            # Commission/EDPB interpretation hooks
    ├── jurisdiction-checklists.md        # Member-State-specific compliance items
    ├── compliance-timeline.md            # Deadline anchors per tier
    ├── docx-formatting.md                # Word output formatting spec
    └── case-studies.md                   # Worked report examples
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `ai-act-report/` folder structure
3. The skill will auto-trigger on "generate AI Act report", "Prüfbericht", "create compliance assessment", or "export as Word"

### Claude Code / Custom MCP Setup

1. Copy the `ai-act-report/` folder to your skills directory:
   ```bash
   cp -r ai-act-report/ /path/to/your/skills/user/ai-act-report/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Either start fresh or hand over context from prior skill output:

> "Generate a formal AI Act compliance report for our HR screening system.
> I've already run the classifier (high-risk, Annex III Nr. 4) and the roles
> skill (we're the deployer). Please assemble the full Prüfbericht and
> export it as a Word document."

The skill will validate the context, draft the 9-section report, run a quality check, and offer .docx export.

### Trigger Phrases

- "Generate AI Act report" / "Prüfbericht" / "Compliance assessment report"
- "Document the AI Act analysis" / "Export as Word"
- "Create a formal AI Act assessment"

### Workflow

| Phase | Description |
|-------|-------------|
| **Phase 1: Input Collection** | Context-first adaptive intake — consumes prior skill outputs if present |
| **Phase 1.5: Input Validation** | Explicit gate flagging missing or inconsistent inputs before drafting |
| **Phase 2: Report Generation** | 9-section template populated with citations and jurisdiction overlays |
| **Phase 3: Quality Check** | Pre-delivery review for consistency and completeness |
| **Phase 4: Word Export** | Optional formatted .docx output |

## Report Structure

| Section | Content |
|---------|---------|
| 1. Introduction | Purpose, scope of the assessment, methodology note |
| 2. System Description | Functionality, deployment context, users |
| 3. Preliminary Check — Scope Exclusions (Art. 2) | Military, R&D, personal, ILE, open-source checks |
| 4. Scope of Application | Territorial scope (Art. 2), addressee analysis |
| 5. Intended Purpose (Art. 3(12)) | Provider-declared intended use |
| 6. Risk Classification | Tier verdict with Art. 5 / Annex I / Annex III / GPAI / Art. 50 analysis |
| 7. Applicable Obligations | Role × tier obligation map with legal citations |
| 8. Risk Flags & Recommendations | Open issues, follow-up actions, monitoring items |
| 9. Conclusion | Summary verdict + next steps |

## Capabilities Summary

| Feature | Description |
|---------|-------------|
| 9-Section Template | Audit-ready structure for legal files and regulator submissions |
| Context Consumption | Reads prior classification / role-determination / obligation-mapping / quick-triage outputs |
| Input Validation Gate | Phase 1.5 explicitly flags missing/inconsistent inputs |
| Citation Index | Consistent article references across sections |
| Jurisdiction Overlays | Member-State-specific compliance items |
| Quality Check | Phase 3 pre-delivery review |
| Word Export | Formatted .docx output for archiving and distribution |
| Output Variants | Assessment, gap analysis, regulator submission, internal memo |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| EU AI Act | Regulation (EU) 2024/1689 |
| Art. 2, 3, 5, 6, 50–55 | Citation anchors for each report section |
| Commission Guidelines | Used in interpretation aids |
| National implementation | Jurisdiction-specific checklist data |

## License & Disclaimer

This skill produces structured AI Act report templates based on Regulation (EU) 2024/1689. It is not legal advice. Reports should be reviewed and validated by qualified legal counsel before regulatory use.

Licensed under AGPL-3.0.

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
