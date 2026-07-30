---
name: eu-ai-act-report-oliver-schmidt-prietz
description: |
  Generates a formal, structured AI Act compliance assessment report suitable for legal files, audit trails, and regulatory inquiries. This skill should be used when the user asks to "generate an AI Act report", "create a compliance assessment report", "document the AI Act analysis", "create a Prüfbericht", "export as Word document", or wants to consolidate prior AI Act skill outputs into a formal documented assessment.
metadata:
  author: Oliver Schmidt-Prietz
  license: AGPL-3.0
  version: 2026.06.05
---

# EU AI Act Examination Report Generator

Generate a formal, structured AI Act compliance assessment report (Dokumentierter Pruefbericht) suitable for legal files, audit trails, and regulatory inquiries under Regulation (EU) 2024/1689.

## Disclaimer (show at session start, do not block)

> **Important:** This skill produces structured AI Act report templates based on Regulation (EU) 2024/1689. It is not legal advice. Reports should be reviewed and validated by qualified legal counsel before regulatory use. Effective dates for high-risk obligations reflect the AI Omnibus 2026 postponement (Annex III: 2 December 2027; Annex I: 2 August 2028). When report templates reference compliance deadlines, use the Omnibus-postponed values.

---

## When to Search the Web

**Before report generation — search for:**
```
EU AI Act latest Commission guidance enforcement decisions [current year]
EU AI Act [relevant sector] specific guidance [current year]
```

**For legal citation verification — search for:**
```
EU AI Act Regulation 2024/1689 consolidated text corrigenda [current year]
```

---

## Workflow

### Phase 1: Input Collection (Context-First Adaptive Intake)

**Step 1 — Context detection:**

> "Let's generate your AI Act compliance report."
>
> If you've run prior AI Act skills in this conversation, I can extract the outputs. Otherwise, paste your Assessment Context block or describe your situation.

**Step 2 — Coverage analysis (internal — do not show this table to the user):**

Extract up to 11 fields from prior context or narrative:

| # | Field | Source |
|---|-------|--------|
| 1 | System name | Context block "System:" or description |
| 2 | Version | Description or context |
| 3 | Provider/vendor | Description or context |
| 4 | Technology type | Description (ML, NLP, CV, etc.) |
| 5 | Deployment context | Description or prior skill outputs |
| 6 | Data types processed | Description |
| 7 | Integration level | Description (standalone, integrated, API-based) |
| 8 | Organization name | Context block or description |
| 9 | Sector | Context block "Sector:" line |
| 10 | Role | Context block "Role:" line |
| 11 | Jurisdiction / Org size | Context block lines |

If an Assessment Context block is provided, auto-populate all available fields, confirm extractions, and ask only about gaps.

If no prior skill outputs are available — gather essential inputs conversationally:

> "I'll need some details about the AI system and your organization. You can answer in your own words — a paragraph or bullet points covering: what the system does, who built it, how it's used, your organization's name and sector, and where you operate in the EU."

Extract fields from the response. Ask about remaining gaps in a single follow-up.

**Step 3 — Report-specific fields (always asked, since they're unique to the report):**

> "A few report-specific details:"
> - Client/matter reference (optional)
> - Prepared by (name/role)
> - Date of assessment

Maximum 2 interaction turns for intake. If a field remains unclear, mark as `[UNCLEAR — to be confirmed]`.

---

### Phase 1.5: Input Validation

Before generating the report, cross-check stated inputs for consistency:

**Classification Cross-Check:**
If stated risk tier is "minimal" or "limited" but system description mentions:
- Recruitment, CV screening, performance evaluation → flag as potentially high-risk — Annex III Nr. 4 (Employment): recruitment, screening, evaluation, or termination
- Credit scoring, insurance risk assessment → flag as potentially high-risk — Annex III Nr. 5 (Essential services): credit scoring, insurance, or benefit eligibility
- Medical diagnosis, patient triage → flag as potentially high-risk — medical AI under Annex I (product safety) or Annex III Nr. 5
- Biometric identification → flag as potentially high-risk — Annex III Nr. 1 (Biometrics): identification or categorization
- Student assessment, admissions → flag as potentially high-risk — Annex III Nr. 3 (Education): assessment or admissions
- Benefits eligibility → flag as potentially high-risk — Annex III Nr. 5(c) (Social benefits): eligibility evaluation
→ If flag: "⚠ Classification inconsistency: [concern]. Please confirm or re-do the risk-tier classification."

**Role Cross-Check:**
- If "deployer" but description mentions "we developed/built/proprietary" → flag provider
- If "deployer" but description mentions own brand, modified purpose, significant retraining → flag quasi-provider
→ If flag: "⚠ Role inconsistency: [concern]. Please confirm or re-do the role determination."

**Completeness Cross-Check:**
- High-risk stated but no DPIA mentioned → flag "DPIA required (Art. 26(9))"
- FRIA-triggering category but no FRIA mentioned → flag "FRIA required (Art. 27)"

Proceed to Phase 2 after validation confirmed or flags acknowledged.

---

### Phase 2: Report Generation

**Template Selection:**

> "Which output format would you like?"
> - (a) **Full Assessment Report** — comprehensive report following the standard template (default)
> - (b) **Classification Record (Prüfprotokoll)** — formal audit trail for the classification decision
> - (c) **Compliance Register Entry** — living compliance tracking document for GRC integration
> - (d) **Management Briefing (Entscheidungsvorlage)** — 2-page decision document for board/C-level
> - (e) **Multiple** — generate more than one format

For templates (b), (c), (d): Read [references/output-templates.md](references/output-templates.md) for the template structures, quality checklists, and when-to-use guidance.

For template (a) — the full assessment report:

Read [references/report-template.md](references/report-template.md) for the full template structure.
Read [references/legal-citations-index.md](references/legal-citations-index.md) for citation accuracy.
Read [references/interpretation-aids.md](references/interpretation-aids.md) for assessment frameworks.
Read [references/case-studies.md](references/case-studies.md) for sample report excerpts (high-risk, Art. 6(3) exception, minimal risk).

Generate the report following this structure:

```markdown
# AI Act Compliance Assessment Report
## [System Name] — [Date]

---

**Report Reference:** [reference number]
**Prepared by:** [name, role]
**Organization:** [organization name]
**Date:** [date]
**Status:** [Draft / Final]

---

### 1. Introduction

**1.1 Purpose of Assessment**
This report documents the assessment of [system name] under Regulation (EU) 2024/1689 (EU AI Act). The assessment determines: (a) whether the system qualifies as an AI system under Art. 3(1), (b) the applicable risk classification, (c) the organization's role in the AI value chain, and (d) the resulting legal obligations.

**1.2 Scope**
[Description of assessment scope — what is included and excluded]

**1.3 Methodology**
Assessment based on:
- EU AI Act (Regulation (EU) 2024/1689) — all articles, recitals, and annexes
- Commission Guidelines on AI System Definition (C(2025) 924 final, 6 Feb 2025)
- Commission Guidelines on Prohibited AI Practices (4 Feb 2025)
- [Other applicable Commission guidelines]
- OECD AI Framework (AI system definition alignment)
- ISO 22989:2022 (AI concepts and terminology)
- [Any additional sources consulted, including web search results]

**1.4 Limitations**
- Based on information provided by [client/organization]
- Subject to evolving regulatory interpretation
- Does not constitute legal advice
- [Any specific limitations]

---

### 2. System Description

**2.1 General Information**

| Field | Detail |
|-------|--------|
| System name | [name] |
| Version | [version] |
| Provider/vendor | [name] |
| Technology type | [ML, NLP, CV, etc.] |
| Deployment date | [date or planned] |

**2.2 Technical Description**
[Brief technical description of how the system works]

**2.3 Deployment Context**
[How and where the system is used, who uses it, who is affected]

**2.4 Data Flows**
[What data goes in, what comes out, where data is stored]

---

### 3. Preliminary Check — Scope Exclusions (Art. 2)

| # | Exclusion | Article | Applicable? | Reasoning |
|---|----------|---------|-------------|-----------|
| 1 | Military/defence/national security | Art. 2(3) | [Yes/No] | [reasoning] |
| 2 | Third-country international cooperation | Art. 2(4) | [Yes/No] | [reasoning] |
| 3 | Scientific research exclusively | Art. 2(6) | [Yes/No] | [reasoning] |
| 4 | Pre-market R&D | Art. 2(8) | [Yes/No] | [reasoning] |
| 5 | Personal/household use | Art. 2(10) | [Yes/No] | [reasoning] |
| 6 | Free and open-source | Art. 2(12) | [Yes/No] | [reasoning] |

**Result:** [AI Act applies / Exclusion under Art. 2([x]) applies]

[If open-source: include Checklist I or II analysis]

---

### 4. Scope of Application

**4.1 Material Scope — AI System Determination (Art. 3(1))**

| # | Criterion | Met? | Reasoning |
|---|-----------|------|-----------|
| 1 | Machine-based operation | [Yes/No] | [reasoning] |
| 2 | Degree of autonomy | [Level X] | [reasoning] |
| 3 | Adaptability after deployment | [Yes/No] | [reasoning] |
| 4 | Explicit or implicit goals | [Yes/No] | [reasoning] |
| 5 | Inference capability | [Yes/No] | [reasoning] |
| 6 | Output generation | [Yes/No] | [reasoning] |
| 7 | Environmental influence | [Yes/No] | [reasoning] |

**Determination:** [IS / IS NOT an AI system under Art. 3(1)]
**Confidence:** [High/Medium/Low]

**4.2 Personal Scope — Role Determination**

| Aspect | Determination |
|--------|--------------|
| Primary role | [Provider/Deployer/Importer/Distributor] |
| Legal basis | [Art. 3(x)] |
| Quasi-provider risk | [None/Low/Medium/High] |
| Art. 25 scenario | [N/A or applicable scenario] |

[Detailed reasoning for role determination]

**4.3 Territorial Scope**

| Aspect | Detail |
|--------|--------|
| Provider establishment | [EU/non-EU] |
| Deployer establishment | [EU Member State(s)] |
| AI output used in EU | [Yes/No] |
| Territorial basis | [Art. 2(1)(a)/(b)/(c)] |

---

### 5. Intended Purpose (Art. 3(12))

**Provider's documented intended purpose:**
[As stated in provider's documentation]

**Actual deployment context:**
[How the system is actually used]

**Alignment assessment:**
[Match/Deviation — if deviation, assess Art. 25(1)(c) implications]

---

### 6. Risk Classification

**6.1 Prohibited Practices Screening (Art. 5)**

| # | Category | Article | Applicable? | Reasoning |
|---|----------|---------|-------------|-----------|
| 1 | Subliminal/manipulative/deceptive | Art. 5(1)(a) | [No/Possibly/Yes] | [reasoning] |
| 2 | Exploitation of vulnerabilities | Art. 5(1)(b) | [No/Possibly/Yes] | [reasoning] |
| 3 | Social scoring | Art. 5(1)(c) | [No/Possibly/Yes] | [reasoning] |
| 4 | Criminal risk prediction (profiling) | Art. 5(1)(d) | [No/Possibly/Yes] | [reasoning] |
| 5 | Untargeted facial recognition scraping | Art. 5(1)(e) | [No/Possibly/Yes] | [reasoning] |
| 6 | Emotion recognition (workplace/education) | Art. 5(1)(f) | [No/Possibly/Yes] | [reasoning] |
| 7 | Biometric categorization (sensitive) | Art. 5(1)(g) | [No/Possibly/Yes] | [reasoning] |
| 8 | Real-time remote biometric ID (public) | Art. 5(1)(h) | [No/Possibly/Yes] | [reasoning] |

**Result:** [No prohibited practice identified / PROHIBITED — Art. 5(1)([x])]

**6.2 High-Risk Assessment**

**6.2.1 Annex I — Product Safety**
[Assessment against 18 Annex I categories]
**Result:** [Not applicable / Applicable — Annex I Nr. [X]]

**6.2.2 Annex III — Application-Based**

| # | Category | Applicable? | Sub-category | Reasoning |
|---|----------|-------------|-------------|-----------|
| 1 | Biometrics | [Yes/No] | | |
| 2 | Critical infrastructure | [Yes/No] | | |
| 3 | Education & training | [Yes/No] | | |
| 4 | Employment & workers | [Yes/No] | | |
| 5 | Essential services | [Yes/No] | | |
| 6 | Law enforcement | [Yes/No] | | |
| 7 | Migration & border | [Yes/No] | | |
| 8 | Justice & democracy | [Yes/No] | | |

**Result:** [Not applicable / Applicable — Annex III Nr. [X]]

**6.2.3 Art. 6(3) Exception Analysis**
[If Annex III triggered: analyze Art. 6(3) conditions (a)-(d)]
[Profiling re-exception check]
**Result:** [Exception applies — not high-risk / Exception does not apply — HIGH-RISK]

**6.3 GPAI / Systemic Risk Assessment**
[If applicable: GPAI model assessment, FLOP threshold, systemic risk indicators]
**Result:** [Not GPAI / GPAI standard / GPAI with systemic risk]

**6.4 Transparency Obligations (Art. 50)**

| Obligation | Article | Applicable? |
|-----------|---------|-------------|
| Interaction disclosure | Art. 50(1) | [Yes/No] |
| Synthetic content marking | Art. 50(2) | [Yes/No] |
| Emotion recognition disclosure | Art. 50(3) | [Yes/No] |
| Deep fake labeling | Art. 50(4) | [Yes/No] |

---

### 7. Applicable Obligations

[Obligation summary matrix — from a prior obligation-mapping step, or generated here based on the classification and role]

**7.1 Obligation Summary**

| Category | Count | Immediate | Short-term | Ongoing |
|----------|-------|-----------|------------|---------|
| Technical measures | [X] | [Y] | [Z] | [W] |
| Organizational measures | [X] | [Y] | [Z] | [W] |
| Management systems | [X] | — | [Y] | [Z] |
| Impact assessments | [X] | [Y] | — | — |
| **Total** | **[X]** | **[Y]** | **[Z]** | **[W]** |

**7.2 Critical Timeline Obligations**
[List obligations with nearest deadlines]

**7.3 Management Systems Required**
[List required management systems]

---

### 8. Risk Flags & Recommendations

**8.1 Identified Risks Requiring Legal Judgment**
[List any areas where the assessment cannot reach a definitive conclusion]

**8.2 Recommendations**

| # | Recommendation | Priority | Responsible |
|---|---------------|----------|-------------|
| 1 | [recommendation] | [High/Medium/Low] | [role] |
| 2 | [recommendation] | [High/Medium/Low] | [role] |

**8.3 GDPR Cross-References**
[List applicable GDPR obligations and suggested skills]

---

### 9. Conclusion

**Overall Classification:**
[System name] is classified as a **[risk tier]** AI system under the EU AI Act, with the organization acting as **[role]**.

**Compliance Readiness:**
[Assessment of current compliance status — Ready / Partially Ready / Not Ready]

**Key Actions:**
1. [Most important action]
2. [Second most important action]
3. [Third most important action]

---

**Prepared by:** [name]
**Date:** [date]
**Reviewed by:** [name, if applicable]

**Disclaimer:** This assessment is based on the information provided and current interpretation of the EU AI Act (Regulation (EU) 2024/1689) as of the assessment date. It does not constitute legal advice. The regulatory landscape is evolving — Commission guidelines, delegated acts, and harmonized standards may affect this assessment. Periodic reassessment is recommended.
```

---

### Phase 3: Quality Check

After generating the report, verify:

1. **Citation completeness:** Every legal determination has an article reference
2. **Reasoning documented:** Each Yes/No determination includes reasoning
3. **Flags raised:** All areas requiring human legal judgment are explicitly flagged
4. **GDPR cross-references:** Applicable GDPR obligations are identified
5. **Follow-up actions:** Clear next steps are specified
6. **Limitations stated:** Any uncertainties or information gaps are documented

Suggest follow-up actions:
- DPIA per Art. 35 GDPR if not yet completed
- Obligation implementation tracking
- Periodic reassessment schedule
- Legal counsel review of flagged areas

---

### Phase 4: Word Document Export (Optional)

**Note:** This phase requires Claude Code (CLI) with file system access. It is not available on claude.ai or mobile.

After Phase 3 Quality Check is complete, offer the Word document export:

> "Would you like me to also export this as a professionally formatted Word document (.docx)?"

If the user declines or the environment does not support file generation → skip this phase.

If yes:

**Prerequisite:** The `docx-processing-anthropic` skill must be installed at `~/.claude/skills/docx-processing-anthropic/`. If the skill directory does not exist, inform the user: "Word document export requires the docx-processing skill. Install it first, then re-run this phase."

**Step 1 — Confirm details:**
> "I'll generate a Word document. Where should I save it?"

Default: current working directory. Use the naming convention: `AI-Act-[Template]-[SystemName]-[YYYY-MM-DD].docx`

**Step 2 — Generate the document:**

Read [references/docx-formatting.md](references/docx-formatting.md) for styling specifications, typography, table formatting, cover page structure, and per-template structural guidance.

Read the docx-js API reference from the docx-processing skill (`~/.claude/skills/docx-processing-anthropic/references/docx-js.md`) for the full library API and critical formatting rules.

Generate a JavaScript file that:
1. Creates a cover page (own section, no header/footer) with report type, system name, metadata, and disclaimer
2. Adds a Table of Contents (except for Management Briefing template)
3. Converts all report sections using the heading hierarchy (H1 → HeadingLevel.HEADING_1, etc.)
4. Renders all assessment tables with consistent styling (light gray header rows, thin gray borders)
5. Adds headers (report title + date) and footers ("Confidential" + page numbers) on all pages except cover
6. Includes the disclaimer as final paragraph

Run the JavaScript file to produce the .docx. Verify the file was created successfully.

**Step 3 — Confirm delivery:**
> "Word document saved to: `[file path]`"

---

## Critical Reminders

1. **This report is a documentation aid** — it does not replace legal judgment on complex classification questions
2. **Flag uncertainty honestly** — marking "Possibly" is better than forcing a wrong determination
3. **Include all search results** — if web search revealed new guidance, cite it in the methodology section
4. **Art. 6(4) documentation requirement** — providers of Annex III systems classified as non-high-risk under Art. 6(3) must document their assessment before placing on market (Art. 6(4)). This includes documenting which condition (a)-(d) is met, the harm assessment, and confirming no profiling. Include this Art. 6(4) documentation (which exception limb is met + harm assessment + no-profiling confirmation) in the report where the exception was relied on.
5. **Version control** — include date and version; reassess when circumstances change
6. **Dual language terms** — preserve German legal terms alongside English for EU legal context
7. **Include compliance timeline** — reference [references/compliance-timeline.md](references/compliance-timeline.md) for applicable deadlines, quarterly action calendar, and phased compliance roadmap in Section 8 (Recommendations)
8. **Jurisdiction-specific recommendations** — reference [references/jurisdiction-checklists.md](references/jurisdiction-checklists.md) for per-country compliance checklists and employment law overlay when generating recommendations
9. **Enforcement context** — when assessing financial exposure (especially for the Management Briefing template), use the Art. 99 penalty tiers: up to €35M / 7% of worldwide annual turnover for Art. 5 prohibited-practice violations, and €15M / 3% for other infringements, enforced via national market-surveillance authorities (and the AI Office for GPAI)

## Part of the EU AI Act suite

This skill works on its own, but it's designed to interlock with my other EU AI Act skills — install any individually, or use them together for an end-to-end workflow:

- **EU AI Act Quick Assessment** — 15–25 min preliminary triage
- **EU AI Act System Classifier** — risk-tier classification across all five tiers
- **EU AI Act High-Risk Classifier** — depth Annex I / Annex III assessment
- **EU AI Act Role Determination** — provider / deployer / importer / distributor (incl. Art. 25)
- **EU AI Act Obligations Mapper** — obligations by role and risk tier
- **EU AI Act Knowledge Base** — Q&A over the Act + Commission guidelines

Each is available as a separate skill — install only what you need.
