---
name: eu-ai-act-obligations-oliver-schmidt-prietz
description: |
  Maps the full set of legal obligations for the EU AI Act based on role + risk tier, producing an actionable compliance matrix with RACI assignments and implementation priorities. This skill should be used when the user asks to "map AI Act obligations", "check what we need to do under the AI Act", "create a compliance checklist", "check deployer obligations", "assess provider duties", or mentions Art. 26, Art. 16-17, AI literacy Art. 4, DPIA, fundamental rights assessment, or "Pflichtenkatalog" under the AI Act.
metadata:
  author: Oliver Schmidt-Prietz
  license: AGPL-3.0
  version: 2026.06.05
---

# EU AI Act Obligations Mapper

Map the full set of legal obligations based on **role + risk tier** under the AI Act (Regulation (EU) 2024/1689), producing an actionable compliance matrix with RACI assignments and implementation priorities.

## Disclaimer (show at session start, do not block)

> **Important:** This skill provides structured AI Act obligations guidance based on the EU AI Act (Regulation (EU) 2024/1689). It is not legal advice. Implementation of compliance measures should involve qualified legal counsel and relevant technical experts. Effective dates for high-risk obligations reflect the AI Omnibus 2026 postponement (Annex III: 2 December 2027; Annex I: 2 August 2028).

---

## When to Search the Web

**On activation — search for:**
```
EU AI Act harmonized standards EN ISO implementing requirements [current year]
EU AI Act conformity assessment notified bodies guidance [current year]
```

**For management systems — search for:**
```
ISO 42001 AI management system alignment EU AI Act [current year]
EU AI Act quality management system requirements guidance
```

**For national rules — search for:**
```
[user's jurisdiction] AI Act national implementation measures [current year]
[user's jurisdiction] AI Act supervisory authority designation
```

**For conformity assessment — search for:**
```
EU AI Act conformity assessment procedures latest guidance
EU AI Act notified body designations [current year]
```

---

## Workflow: Ask Questions ONE AT A TIME

### Phase 1: Input Context (Context-Aware Adaptive Intake)

**Step 1 — Context detection (always first):**

> "Let's map your AI Act obligations."
>
> If you've already done a prior AI Act assessment (risk classification, role determination, or a quick triage), paste the Assessment Context block below. Otherwise, describe your situation in your own words.

**Step 2 — Coverage analysis (internal — do not show this table to the user):**

Map the context block or narrative to these 6 fields:

| # | Field | Source in context block | Fallback |
|---|-------|----------------------|----------|
| 1 | Risk classification | "Classification:" line | Ask |
| 2 | Organizational role | "Role:" line | Ask |
| 3 | Organization size | "Org Size:" line | Ask |
| 4 | Sector | "Sector:" line | Ask |
| 5 | Jurisdiction(s) | "Jurisdiction:" line | Ask |
| 6 | Existing frameworks | Not in context block | Always ask |

If the risk tier has not been classified yet → run a risk-tier classification first (AI-system test under Art. 3(1); prohibited / high-risk / GPAI / limited / minimal).
If the role hasn't been determined yet → determine it first (provider / deployer / importer / distributor under Art. 3 and Art. 25).

**Step 3 — Adaptive follow-up:**

- If context block provided → confirm extracted fields, then ask only about gaps. Fields 1-5 are typically covered; only field 6 (existing frameworks) needs asking.
- If narrative provided → extract what's covered, ask about remaining gaps in a single grouped question.
- If minimal information provided → ask about all missing fields in a single prompt, grouped conversationally.

Existing compliance status is always asked since it's new information not carried in the context block. Frame conversationally:

> "One more thing — which compliance foundations do you already have in place? (Risk management, data quality, QMS, DPIA, incident reporting, AI literacy training, or starting from scratch)"

Maximum 2 interaction turns for intake. If a field remains unclear, mark as `[UNCLEAR — proceeding with cautious assumptions]`.

---

### Phase 2: Obligation Mapping

Based on role + risk tier, load the applicable obligation set.

Read the relevant reference files:

**Deployer + High-Risk** → Read [references/high-risk-deployer-obligations.md](references/high-risk-deployer-obligations.md)
**Provider + High-Risk** → Read [references/high-risk-provider-obligations.md](references/high-risk-provider-obligations.md)
**Any role + Low-Risk/Minimal** → Read [references/low-risk-obligations.md](references/low-risk-obligations.md)
**Non-high-risk Annex III (Art. 6(3) exception)** → Read [references/art6-4-documentation.md](references/art6-4-documentation.md)
**GPAI provider** → Read [references/gpai-obligations.md](references/gpai-obligations.md)
**FRIA-triggering deployer** → Read [references/fria-template.md](references/fria-template.md) for Art. 27 FRIA methodology and fillable template
**Provider conformity assessment** → Read [references/conformity-assessment.md](references/conformity-assessment.md) for Art. 43 track selection, EU Declaration, and CE marking
**Provider post-market monitoring** → Read [references/post-market-monitoring.md](references/post-market-monitoring.md) for Art. 72 monitoring system design and serious incident reporting
**EU database registration** → Read [references/eu-database-registration.md](references/eu-database-registration.md) for Art. 49 registration process (provider and deployer tracks)
**All roles** → Art. 4 AI competence obligation always applies

**Obligation count preview:**

> "Based on your role as **[Role]** of a **[risk tier]** system, you have **N obligations** across K categories. I'll walk through them in 4 batches."

**Batched assessment (4 batches replacing per-obligation questioning):**

Present obligations grouped by category. For each batch, show a table with all obligations in that category and ask the user to respond to the entire batch at once:

| Batch | Category | Typical obligations |
|-------|----------|-------------------|
| 1 | Technical Measures | Use per instructions, monitoring, input data, log retention, data quality |
| 2 | Organizational Measures | Oversight persons, inform affected persons, employee info, AI competence, incident reporting, registration, authority cooperation |
| 3 | Management Systems | Risk management, data quality mgmt, QMS, post-market monitoring |
| 4 | Impact Assessments | DPIA, FRIA |

For each batch, present a table:

> **Batch [X] of 4: [Category]**
>
> | # | Obligation | Legal Basis | Priority | Status |
> |---|-----------|-------------|----------|--------|
> | 1 | [obligation] | [article] | [Immediate/Short-term/Ongoing] | Already in place / Partially addressed / Not yet addressed |
>
> "For each obligation, indicate: already in place, partially addressed, or not yet addressed. You can respond with just the numbers (e.g., '1,3 = in place; 2,4 = partial; 5 = not addressed')."

**Progress indicator** after each batch: "Batch [X] of 4 complete. [N] obligations remaining."

**Smart defaults:** If the user indicated "starting from scratch" in Phase 1, default all obligations to "not yet addressed" and confirm: "Since you're starting from scratch, I've marked all obligations as not yet addressed. Any exceptions?"

Target: 4-5 interaction turns instead of 20+.

Flag priority levels: **critical timeline obligations first** (e.g., Art. 26(6) 6-month log retention must be operational from day one).

#### GDPR Cross-Reference Checks

Read [references/gdpr-crosswalk.md](references/gdpr-crosswalk.md).

At relevant obligation points, suggest existing GDPR skills:

| Obligation | Trigger | Suggestion |
|-----------|---------|------------|
| Art. 26(9) DPIA | High-risk deployer | "Perform a DPIA incorporating the provider's Art. 13 information about system capabilities and limitations" |
| Art. 26(11) inform affected persons | Deployer transparency | "Prepare a combined AI Act/GDPR transparency notice covering Art. 26(11) and Art. 13/14 GDPR" |
| Art. 10 data governance | Provider data quality | "Conduct a data inventory review mapping AI training data against GDPR data quality and minimization principles" |
| Art. 26(7) employee information | Workplace AI | "Prepare employee AI transparency documentation combining Art. 26(7) and GDPR Art. 13/14 requirements" |
| Art. 26(5) serious incidents | Incident detected | "Establish a dual incident reporting procedure covering both AI Act (Art. 73) and GDPR (Art. 33/34) timelines" |
| Personal data processing | Any AI processing personal data | "Review your GDPR Art. 28 processor agreement to include AI Act cooperation provisions (Art. 25(2))" |

### Obligation Priority Decision Tree

```
         ┌─────────────────────────┐
         │ ROLE + RISK TIER        │
         └────────────┬────────────┘
                      │
    ┌─────────────────┼──────────────────┐
    │                 │                  │
    ▼                 ▼                  ▼
┌─────────┐   ┌──────────────┐   ┌──────────────┐
│ PROVIDER│   │   DEPLOYER   │   │ GPAI MODEL   │
│         │   │              │   │ PROVIDER     │
└────┬────┘   └──────┬───────┘   └──────┬───────┘
     │               │                  │
     ▼               ▼                  ▼
 High-Risk?      High-Risk?        Systemic Risk?
 ├─ YES:         ├─ YES:           ├─ YES:
 │ Art. 8-17     │ Art. 26         │ Art. 53 + 55
 │ Art. 17 QMS   │ Art. 27 FRIA    ├─ NO:
 │ Art. 9 Risk   │ Art. 26(9) DPIA │ Art. 53
 │ Art. 43 CA    │ Art. 49(3) Reg  └────────────
 │ Art. 49 Reg   └────────────
 │               ├─ NO (Art. 50):
 ├─ NO           │ Art. 50 only
 │ (Art. 50):    ├─ NO (Minimal):
 │ Art. 50       │ Art. 4 only
 │ +Art. 6(4)    └────────────
 │ if Annex III
 └────────────

 ALL ROLES: Art. 4 AI Competence (always applies)
```

For worked obligation mapping examples, see [references/case-studies.md](references/case-studies.md).

---

### Phase 3: Implementation Roadmap

Group obligations by timeline:

**1. IMMEDIATE (before deployment / already overdue if deployed):**
- Use system per operating instructions (Art. 26(1))
- Monitoring system in place (Art. 26(5))
- Qualified oversight persons assigned (Art. 26(2))
- Log retention mechanism active (Art. 26(6))
- AI competence measures (Art. 4)

**2. SHORT-TERM (within 3 months of deployment):**
- Risk management system operational (Art. 9)
- Data quality management (Art. 10)
- Registration in EU database (Art. 49)
- DPIA completed (Art. 26(9))
- FRIA completed if required (Art. 27)
- Employee information (Art. 26(7))

**3. ONGOING (continuous):**
- System monitoring (Art. 26(5))
- Logging and record-keeping (Art. 12, Art. 26(6))
- Incident reporting (Art. 26(5) third sentence)
- Authority cooperation (Art. 26(12))
- Post-market monitoring data contribution

**4. PERIODIC (regular intervals):**
- Risk reassessment (Art. 9 — recommended annually)
- AI competence training updates (Art. 4)
- Documentation review and update
- Testing and validation (Art. 15)

Read [references/technical-measures.md](references/technical-measures.md), [references/organizational-measures.md](references/organizational-measures.md), and [references/management-systems.md](references/management-systems.md) for detailed requirements.

For the full compliance timeline with quarterly action calendar, resource estimates by organization size, and dependency mapping between activities, reference [references/compliance-roadmap.md](references/compliance-roadmap.md).

---

### Phase 4: Obligations Matrix Output

```markdown
## AI Act Compliance Obligations Matrix
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Role: [Role]  |  Risk Tier: [Tier]  |  Basis: [legal basis]
Organization: [name]  |  Date: [date]

### Technical Measures
| # | Obligation | Legal Basis | Priority | Status | RACI | Effort |
|---|-----------|-------------|----------|--------|------|--------|
| 1 | Use system per operating instructions | Art. 26(1) | Immediate | [ ] | IT=R, Legal=A | Low |
| 2 | Monitor system operation | Art. 26(5) | Immediate | [ ] | IT=R, Compliance=A | Medium |
| 3 | Ensure input data relevance | Art. 26(4) | Immediate | [ ] | IT=R, Business=A | Medium |
| 4 | Retain auto-generated logs (6 months) | Art. 26(6) | Immediate | [ ] | IT=R, Legal=A | Low |
| 5 | Data quality management | Art. 10 | Short-term | [ ] | IT=R, Data=A | High |

### Organizational Measures
| # | Obligation | Legal Basis | Priority | Status | RACI | Effort |
|---|-----------|-------------|----------|--------|------|--------|
| 1 | Assign qualified oversight persons | Art. 26(2) | Immediate | [ ] | HR=R, Legal=A | Medium |
| 2 | Inform affected persons | Art. 26(11) | Immediate | [ ] | Legal=R, Comms=A | Medium |
| 3 | Inform employees/works council | Art. 26(7) | Short-term | [ ] | HR=R, Legal=A | Medium |
| 4 | AI competence training | Art. 4 | Short-term | [ ] | HR=R, Mgmt=A | Medium |
| 5 | Incident reporting procedure | Art. 26(5) s.3 | Immediate | [ ] | Legal=R, IT=C | High |
| 6 | Register use in EU database | Art. 49(3) | Short-term | [ ] | Legal=R | Low |
| 7 | Cooperate with authorities | Art. 26(12) | Ongoing | [ ] | Legal=R, Mgmt=A | Low |

### Management Systems Required
| System | Legal Basis | Scope | Existing? |
|--------|------------|-------|-----------|
| Risk Management | Art. 9 | Continuous lifecycle risk assessment | [ ] |
| Data Quality Mgmt | Art. 10 | Training/validation/test data governance | [ ] |
| Quality Management | Art. 17 | Processes, procedures, compliance concept | [ ] |
| Post-Market Monitoring | Art. 72 | Monitoring throughout lifetime | [ ] |

### Impact Assessments Required
| Assessment | Legal Basis | When | Status |
|-----------|------------|------|--------|
| DPIA | Art. 26(9) + Art. 35 GDPR | Before deployment | [ ] |
| Fundamental Rights Assessment | Art. 27 | Before deployment (public bodies + certain private) | [ ] |

### GDPR Cross-References
| AI Act Obligation | GDPR Parallel | Recommended Action |
|------------------|---------------|----------------|
| Art. 26(9) DPIA | Art. 35 GDPR | Perform DPIA per Art. 35 GDPR incorporating Art. 13 information |
| Art. 26(11) inform persons | Art. 13/14 GDPR | Draft combined AI Act + GDPR transparency notice |
| Art. 10 data governance | Art. 25 GDPR (DPbD) | Conduct data inventory and governance review |
| Art. 26(7) employee info | Art. 13/14 GDPR | Prepare employee AI transparency documentation |
| Incident reporting | Art. 33/34 GDPR | Establish dual AI Act/GDPR incident reporting procedure |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUMMARY:
TOTAL: [X] obligations | [Y] immediate | [Z] require legal judgment
Timeline: [X] already compliant | [Y] gaps identified | [Z] not yet assessed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ASSESSMENT CONTEXT (paste into next skill)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
System: [name]
Classification: [risk tier]
Basis: [legal basis]
Role: [role]
Quasi-Provider: [risk level]
Sector: [sector]
Jurisdiction: [list]
Org Size: [size]
Art. 50: [applicable triggers]
GPAI: [yes/no, systemic risk]

NEXT STEPS:
→ Generate formal assessment documentation (classification rationale + obligation matrix)
→ Address [Y] immediate gaps as priority
→ Establish management systems within [timeline]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Critical Reminders

1. **Art. 4 AI competence applies to ALL roles and ALL risk tiers** — even minimal risk systems
2. **Art. 26(6) log retention (6 months)** — must be in place from day one of deployment
3. **Art. 26(9) DPIA** — must be completed BEFORE deployment, not after
4. **Art. 27 FRIA** — required for public bodies, private entities providing public services, and deployers of insurance risk assessment (Annex III Nr. 5(b)) and social benefits eligibility (Annex III Nr. 5(c)) systems
5. **Art. 26(5) incident reporting** — "without undue delay" to provider and authority
6. **SME proportionality** — Art. 62 requires authorities to consider SME capabilities
7. **Transition periods vary** — prohibited practices (Feb 2025), GPAI (Aug 2025), high-risk Annex III (**Dec 2027** — Omnibus-postponed from Aug 2026), high-risk Annex I (**Aug 2028** — Omnibus-postponed from Aug 2027). The AI Omnibus is a legislative-in-progress instrument; verify the current status of the postponement via a web search before relying on these dates.
8. **Search for latest harmonized standards** — technical implementation standards are still being developed
9. **Enforcement exposure** — factor in the penalty tiers when prioritising gaps: up to €35M / 7% of worldwide annual turnover for Art. 5 prohibited-practice violations, and €15M / 3% for other infringements (Art. 99). Enforcement runs through national market-surveillance authorities and, for GPAI, the AI Office.
10. **Jurisdiction-specific obligations** — reference [references/regulatory-overlays.md](references/regulatory-overlays.md) for per-country employment law, financial regulator, and data protection overlay requirements that apply in addition to AI Act obligations
11. **Compliance timeline & resources** — reference [references/compliance-roadmap.md](references/compliance-roadmap.md) for quarterly action calendar, resource estimation by organization size, and phased compliance roadmap template

## Part of the EU AI Act suite

This skill works on its own, but it's designed to interlock with my other EU AI Act skills — install any individually, or use them together for an end-to-end workflow:

- **EU AI Act Quick Assessment** — 15–25 min preliminary triage
- **EU AI Act System Classifier** — risk-tier classification across all five tiers
- **EU AI Act High-Risk Classifier** — depth Annex I / Annex III assessment
- **EU AI Act Role Determination** — provider / deployer / importer / distributor (incl. Art. 25)
- **EU AI Act Examination Report Generator** — audit-ready compliance report
- **EU AI Act Knowledge Base** — Q&A over the Act + Commission guidelines

Each is available as a separate skill — install only what you need.
