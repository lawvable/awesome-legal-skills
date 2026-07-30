# AI Act Output Templates

Three structured templates for AI Act compliance documentation, each serving a different audience and purpose. They integrate with the full assessment workflow (classification → role determination → obligation mapping → report) and can be used in preliminary mode (after a quick triage) or final mode (for the formal report).

---

## When to Use Which Template

| Template | Audience | Purpose | When |
|----------|----------|---------|------|
| **1. Classification Record (Prüfprotokoll)** | Compliance team, legal counsel, auditors | Formal audit trail documenting the classification decision | After completing the risk-tier classification |
| **2. Compliance Register Entry** | GRC team, compliance officers, project managers | Living compliance tracking document per AI system | After completing the obligation mapping |
| **3. Management Briefing (Entscheidungsvorlage)** | Board, C-level, senior management | Decision document requesting management action | When escalation or budget approval needed |

**Preliminary mode** (after a quick triage): Mark all outputs as "PRELIMINARY — Full assessment recommended" and reduce detail level.

---

## Template 1: AI Act Classification Record (Prüfprotokoll)

### Purpose

Structured audit trail documenting the classification of an AI system under the EU AI Act. Designed for compliance files, regulatory inquiries, and internal audit. More rigorous than a summary memo — structured as a formal, versioned record with explicit reasoning for each determination.

```markdown
# AI Act Classification Record (Prüfprotokoll)

## Document Control

| Field | Value |
|-------|-------|
| **Record ID** | [CLR-YYYY-NNN] |
| **AI System Name** | [system name and version] |
| **Assessment Date** | [DD MMM YYYY] |
| **Assessment Version** | [v1.0 / v1.1 / etc.] |
| **Assessor** | [name, role, organization] |
| **Reviewer** | [name, role — if reviewed] |
| **Review Date** | [DD MMM YYYY — if reviewed] |
| **Next Review Due** | [DD MMM YYYY — recommended annually or on significant change] |
| **Status** | [DRAFT / UNDER REVIEW / FINAL] |
| **Classification** | [PRELIMINARY / FINAL] |

---

## 1. System Identification

| Field | Detail |
|-------|--------|
| System name | [name] |
| Version/release | [version] |
| Provider/vendor | [provider name, country] |
| Technology type | [ML, NLP, CV, generative AI, etc.] |
| Deployment context | [brief description of use case] |
| Deployment jurisdiction(s) | [EU Member State(s) / CH / other] |
| Sector | [healthcare, finance, HR, etc.] |
| Data types processed | [personal data / non-personal / mixed] |
| Users | [who operates the system] |
| Affected persons | [who is affected by the system's outputs] |

---

## 2. Scope Determination (Art. 2)

| # | Exclusion | Article | Applicable? | Reasoning |
|---|----------|---------|-------------|-----------|
| 1 | Military/defence | Art. 2(3) | [Yes/No] | [reasoning] |
| 2 | Third-country international cooperation | Art. 2(4) | [Yes/No] | [reasoning] |
| 3 | Scientific research exclusively | Art. 2(6) | [Yes/No] | [reasoning] |
| 4 | Pre-market R&D | Art. 2(8) | [Yes/No] | [reasoning] |
| 5 | Personal/household use | Art. 2(10) | [Yes/No] | [reasoning] |
| 6 | Free and open-source | Art. 2(12) | [Yes/No] | [reasoning] |

**Scope Result:** [AI Act applies / Excluded under Art. 2([x])]

[If open-source: Checklist I or II analysis attached as Annex]

---

## 3. AI System Test (Art. 3(1))

| # | Criterion | Met? | Evidence / Reasoning |
|---|-----------|------|---------------------|
| 1 | Machine-based operation | [Yes/No] | [reasoning with specific technical detail] |
| 2 | Degree of autonomy | [ISO 22989 Level X] | [reasoning with specific autonomy assessment] |
| 3 | Adaptability after deployment | [Yes/No] | [reasoning — continuous learning, RLHF, etc.] |
| 4 | Explicit or implicit goals | [Yes/No] | [reasoning — training objectives, optimization targets] |
| 5 | Inference capability | [Yes/No] | [reasoning — prediction, classification, generation] |
| 6 | Output generation | [Yes/No] | [reasoning — output types: predictions, content, decisions] |
| 7 | Environmental influence | [Yes/No] | [reasoning — how outputs affect physical/virtual environment] |

**AI System Determination:** [IS / IS NOT an AI system under Art. 3(1)]
**Confidence Level:** [High / Medium / Low]
**If Medium/Low — explain:** [what creates uncertainty]

---

## 4. Risk Classification Cascade

### 4.1 Prohibited Practice Screening (Art. 5)

| # | Category | Article | Result | Reasoning |
|---|----------|---------|--------|-----------|
| 1 | Subliminal/manipulative/deceptive | Art. 5(1)(a) | [Clear / Possibly / Flagged] | [reasoning] |
| 2 | Exploitation of vulnerabilities | Art. 5(1)(b) | [Clear / Possibly / Flagged] | [reasoning] |
| 3 | Social scoring | Art. 5(1)(c) | [Clear / Possibly / Flagged] | [reasoning] |
| 4 | Criminal risk prediction (profiling) | Art. 5(1)(d) | [Clear / Possibly / Flagged] | [reasoning] |
| 5 | Untargeted facial recognition scraping | Art. 5(1)(e) | [Clear / Possibly / Flagged] | [reasoning] |
| 6 | Emotion recognition (workplace/education) | Art. 5(1)(f) | [Clear / Possibly / Flagged] | [reasoning] |
| 7 | Biometric categorization (sensitive) | Art. 5(1)(g) | [Clear / Possibly / Flagged] | [reasoning] |
| 8 | Real-time remote biometric ID (public) | Art. 5(1)(h) | [Clear / Possibly / Flagged] | [reasoning] |

**Prohibited Practice Result:** [No prohibition identified / FLAGGED — Art. 5(1)([x]) — requires legal review]

### 4.2 High-Risk — Annex I (Product Safety)

**Applicable Annex I legislation:** [Nr. X — [legislation name] / Not applicable]
**Safety component?** [Yes / No / N/A]
**Third-party conformity assessment required?** [Yes / No / N/A]
**Art. 6(1) Result:** [High-risk / Not high-risk via Annex I]

### 4.3 High-Risk — Annex III (Application-Based)

| # | Category | Applicable? | Sub-Category | Reasoning |
|---|----------|-------------|-------------|-----------|
| 1 | Biometrics | [Yes/No] | [1a/1b/1c] | [reasoning] |
| 2 | Critical infrastructure | [Yes/No] | | [reasoning] |
| 3 | Education & training | [Yes/No] | [3a/3b/3c] | [reasoning] |
| 4 | Employment & workers | [Yes/No] | [4a/4b] | [reasoning] |
| 5 | Essential services | [Yes/No] | [5a/5b/5c/5d] | [reasoning] |
| 6 | Law enforcement | [Yes/No] | [6a-6e] | [reasoning] |
| 7 | Migration & border | [Yes/No] | [7a-7d] | [reasoning] |
| 8 | Justice & democracy | [Yes/No] | [8a/8b] | [reasoning] |

**Annex III Result:** [Category [X] triggered / No Annex III category applicable]

### 4.4 Art. 6(3) Exception Analysis (if Annex III triggered)

| Condition | Applicable? | Reasoning |
|-----------|-------------|-----------|
| (a) Narrow procedural task | [Yes/No] | [reasoning] |
| (b) Improves completed human activity | [Yes/No] | [reasoning] |
| (c) Detects patterns without replacing/influencing | [Yes/No] | [reasoning] |
| (d) Preparatory task to Annex III assessment | [Yes/No] | [reasoning] |

**Profiling re-exception check:** Does the system perform profiling (Art. 4(4) GDPR)? [Yes/No]
If Yes → Art. 6(3) exception does NOT apply regardless of above.

**Art. 6(3) Result:** [Exception applies — not high-risk / Exception does not apply — HIGH-RISK]

### 4.5 GPAI Assessment

**GPAI model involved?** [Yes — model name / No]
**Systemic risk (Art. 51)?** [Yes — above 10^25 FLOP / No / Unknown]
**GPAI Result:** [Not GPAI / GPAI standard (Art. 53) / GPAI systemic risk (Art. 53 + 55)]

### 4.6 Art. 50 Transparency Triggers

| Obligation | Article | Triggered? | Reasoning |
|-----------|---------|------------|-----------|
| Interaction disclosure | Art. 50(1) | [Yes/No] | [reasoning] |
| Synthetic content marking | Art. 50(2) | [Yes/No] | [reasoning] |
| Emotion recognition disclosure | Art. 50(3) | [Yes/No] | [reasoning] |
| Deep fake labeling | Art. 50(4) | [Yes/No] | [reasoning] |

---

## 5. Role Determination Summary

| Aspect | Determination |
|--------|--------------|
| Primary role | [Provider / Deployer / Importer / Distributor] |
| Legal basis | [Art. 3([x])] |
| Quasi-provider risk | [None / Low / Medium / High] |
| Art. 25 trigger | [N/A / Art. 25(1)(a/b/c)] |

[Brief reasoning — or reference to the separate role-determination output]

---

## 6. Classification Result

| Dimension | Determination |
|-----------|--------------|
| **AI System (Art. 3(1))** | [Yes / No] |
| **Risk Tier** | [Prohibited / High-Risk / GPAI-Systemic / Limited / Minimal] |
| **Classification Basis** | [Art. 5(1)(x) / Annex I Nr. X / Annex III Nr. X / Art. 50 / None] |
| **Applicable Deadline** | [2 Feb 2025 / 2 Aug 2025 / 2 Dec 2027 (Annex III, Omnibus-postponed) / 2 Aug 2028 (Annex I, Omnibus-postponed)] |
| **Enforcement Penalty Tier** | [Tier 1: EUR 35M/7% / Tier 2: EUR 15M/3% / Tier 3: EUR 7.5M/1%] |

---

## 7. Assumptions & Limitations

**Assumptions made:**
- [List any assumptions about the system's functionality, deployment, or use]

**Information gaps:**
- [List any information that was not available or could not be verified]

**Limitations of this assessment:**
- [Scope limitations, e.g., "based on documentation provided, not technical audit"]
- Assessment based on regulations as of [date]; subsequent guidance may affect conclusions
- This assessment does not constitute legal advice

---

## 8. Assessor Declaration

This classification record was prepared based on the information available at the assessment date. All determinations include documented reasoning. Areas of uncertainty are explicitly flagged. This record should be reviewed and validated by qualified legal counsel before being used for regulatory purposes.

**Assessor:** [name]
**Date:** [date]
**Signature:** _______________

**Reviewer:** [name]
**Date:** [date]
**Signature:** _______________
```

### Quality Checklist — Classification Record

- [ ] All 7 AI system criteria individually assessed with reasoning
- [ ] All 8 prohibited practice categories screened with reasoning
- [ ] All 8 Annex III categories screened with specific sub-category
- [ ] Art. 6(3) exception analyzed if Annex III triggered (including profiling re-exception)
- [ ] GPAI model assessment included
- [ ] Art. 50 transparency triggers assessed
- [ ] All legal article citations accurate and complete
- [ ] Assumptions and limitations explicitly documented
- [ ] Assessment version and review date recorded
- [ ] Confidence levels stated where determination is not clear-cut

---

## Template 2: AI Compliance Register Entry (Compliance-Register-Eintrag)

### Purpose

Living compliance tracking document for a specific AI system. Designed to track obligation status, implementation progress, and evidence for ongoing compliance management. Suitable for integration with GRC (Governance, Risk, Compliance) tools.

```markdown
# AI Compliance Register Entry

## System Metadata

| Field | Value |
|-------|-------|
| **Register ID** | [REG-YYYY-NNN] |
| **AI System Name** | [system name] |
| **Classification Record Ref** | [CLR-YYYY-NNN — link to Prüfprotokoll] |
| **Risk Tier** | [High-Risk / GPAI / Limited / Minimal] |
| **Classification Basis** | [Annex I Nr. X / Annex III Nr. X / Art. 50 / GPAI] |
| **Organization Role** | [Provider / Deployer / Quasi-Provider] |
| **Deployment Jurisdiction(s)** | [Member State(s)] |
| **Deployment Date** | [DD MMM YYYY] |
| **Register Created** | [DD MMM YYYY] |
| **Last Updated** | [DD MMM YYYY] |
| **Compliance Owner** | [name, role] |
| **Next Review Date** | [DD MMM YYYY] |

---

## Obligation Tracker

### Technical Obligations

| # | Obligation | Article | Status | Owner | Deadline | Evidence Location | Notes |
|---|-----------|---------|--------|-------|----------|-------------------|-------|
| T1 | Use system per operating instructions | Art. 26(1) | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| T2 | Ensure input data relevance | Art. 26(4) | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| T3 | Monitor system operation | Art. 26(5) | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| T4 | Retain auto-generated logs (6 months) | Art. 26(6) | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| T5 | Risk management system | Art. 9 | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| T6 | Data quality management | Art. 10 | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| T7 | Technical documentation | Art. 11 | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| T8 | Record-keeping (logging) | Art. 12 | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| T9 | Transparency and information | Art. 13 | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| T10 | Human oversight measures | Art. 14 | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| T11 | Accuracy, robustness, cybersecurity | Art. 15 | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |

### Organizational Obligations

| # | Obligation | Article | Status | Owner | Deadline | Evidence Location | Notes |
|---|-----------|---------|--------|-------|----------|-------------------|-------|
| O1 | Assign qualified oversight persons | Art. 26(2) | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| O2 | Inform affected persons | Art. 26(11) | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| O3 | Inform employees/works council | Art. 26(7) | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| O4 | AI competence training | Art. 4 | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| O5 | Incident reporting procedure | Art. 26(5)/73 | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| O6 | EU database registration | Art. 49 | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| O7 | Cooperation with authorities | Art. 26(12) | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |
| O8 | Post-market monitoring | Art. 72 | [Done/In Progress/Open/N/A] | [name] | [date] | [link/path] | |

### Impact Assessments

| # | Assessment | Article | Status | Completion Date | Review Due | Evidence Location |
|---|-----------|---------|--------|-----------------|------------|-------------------|
| A1 | DPIA | Art. 26(9) + GDPR Art. 35 | [Done/In Progress/Open/N/A] | [date] | [date] | [link/path] |
| A2 | FRIA | Art. 27 | [Done/In Progress/Open/N/A] | [date] | [date] | [link/path] |

### Management Systems

| # | System | Article | Status | Last Audit | Next Audit | Evidence Location |
|---|--------|---------|--------|------------|------------|-------------------|
| M1 | Risk management system | Art. 9 | [Operational/Setup/Planned/N/A] | [date] | [date] | [link/path] |
| M2 | Quality management system | Art. 17 | [Operational/Setup/Planned/N/A] | [date] | [date] | [link/path] |
| M3 | Post-market monitoring | Art. 72 | [Operational/Setup/Planned/N/A] | [date] | [date] | [link/path] |

### National/Jurisdictional Obligations

| # | Obligation | Jurisdiction | Legal Basis | Status | Owner | Evidence |
|---|-----------|-------------|-------------|--------|-------|----------|
| N1 | [e.g., Betriebsvereinbarung] | [DE] | [BetrVG §87(1) Nr. 6] | [Done/In Progress/Open] | [name] | [link/path] |
| N2 | [e.g., CSE consultation] | [FR] | [L. 2312-38] | [Done/In Progress/Open] | [name] | [link/path] |
| N3 | [e.g., BaFin model governance] | [DE] | [MaRisk] | [Done/In Progress/Open] | [name] | [link/path] |

---

## GDPR Coordination Status

| AI Act Obligation | GDPR Parallel | Status | DPO Involved? |
|------------------|---------------|--------|---------------|
| Art. 10 data governance | Art. 25 DPbD | [Aligned/Gap/N/A] | [Yes/No] |
| Art. 26(9) DPIA | Art. 35 GDPR | [Aligned/Gap/N/A] | [Yes/No] |
| Art. 26(11) inform persons | Art. 13/14 GDPR | [Aligned/Gap/N/A] | [Yes/No] |
| Art. 26(7) employee info | Art. 13/14 GDPR | [Aligned/Gap/N/A] | [Yes/No] |
| Art. 73 incident reporting | Art. 33/34 GDPR | [Aligned/Gap/N/A] | [Yes/No] |

---

## Implementation Progress

| Category | Total | Done | In Progress | Open | N/A | Completion % |
|----------|-------|------|-------------|------|-----|-------------|
| Technical | [X] | [X] | [X] | [X] | [X] | [X%] |
| Organizational | [X] | [X] | [X] | [X] | [X] | [X%] |
| Assessments | [X] | [X] | [X] | [X] | [X] | [X%] |
| Management Systems | [X] | [X] | [X] | [X] | [X] | [X%] |
| National | [X] | [X] | [X] | [X] | [X] | [X%] |
| **Overall** | **[X]** | **[X]** | **[X]** | **[X]** | **[X]** | **[X%]** |

---

## Risk Assessment (Residual Risk After Measures)

| Risk Dimension | Pre-Mitigation | Measures Taken | Residual Risk | Acceptable? |
|---------------|---------------|----------------|---------------|-------------|
| Safety risk | [High/Medium/Low] | [measures] | [High/Medium/Low] | [Yes/No] |
| Fundamental rights risk | [High/Medium/Low] | [measures] | [High/Medium/Low] | [Yes/No] |
| Compliance risk | [High/Medium/Low] | [measures] | [High/Medium/Low] | [Yes/No] |
| Enforcement risk | [High/Medium/Low] | [measures] | [High/Medium/Low] | [Yes/No] |

---

## Change Log

| Date | Version | Change | Changed By |
|------|---------|--------|-----------|
| [date] | 1.0 | Initial register entry created | [name] |
| [date] | 1.1 | [description of change] | [name] |
```

### Quality Checklist — Compliance Register Entry

- [ ] All applicable obligations listed with correct article references
- [ ] Each obligation has a named owner
- [ ] Deadlines align with AI Act timeline phases
- [ ] Evidence locations point to accessible documents/systems
- [ ] GDPR coordination assessed with DPO involvement confirmed
- [ ] National/jurisdictional obligations included per deployment country
- [ ] Progress percentages calculated correctly
- [ ] Next review date set (maximum 12 months)
- [ ] Change log initialized

---

## Template 3: Management Briefing (Entscheidungsvorlage)

### Purpose

Decision document for board/C-level audience. Maximum 2 pages. Summarizes AI Act classification, compliance status, financial exposure, and requests specific management action. Designed for formal decision-making processes with sign-off requirements.

```markdown
# AI Act Compliance — Management Briefing
## [System Name] — Entscheidungsvorlage

**Date:** [DD MMM YYYY]
**Prepared by:** [name, role]
**For:** [board / executive committee / [specific decision-maker]]
**Decision required by:** [DD MMM YYYY]
**Classification:** [CONFIDENTIAL / INTERNAL]

---

### System & Classification at a Glance

| | |
|---|---|
| **System** | [system name — one-line description] |
| **Risk Classification** | ■ PROHIBITED  □ HIGH-RISK  □ GPAI  □ LIMITED  □ MINIMAL |
| **Organization Role** | [Provider / Deployer / Quasi-Provider] |
| **Compliance Deadline** | [DD MMM YYYY — e.g., 2 Dec 2027 for Annex III, 2 Aug 2028 for Annex I (per AI Omnibus 2026)] |
| **Current Compliance** | [X]% complete — [Y] of [Z] obligations addressed |

[Use filled ■ for the applicable risk tier; empty □ for others]

---

### Business Impact

[2-3 sentences describing what this system does for the organization and why it matters commercially]

**If non-compliant:** [specific business risk — e.g., "System must be withdrawn from EU market, affecting [X] customers and [Y] revenue"]

---

### Top 5 Compliance Obligations

| # | Obligation | Effort | Deadline | Status |
|---|-----------|--------|----------|--------|
| 1 | [Most critical obligation] | [X person-days] | [date] | [Red/Amber/Green] |
| 2 | [Second obligation] | [X person-days] | [date] | [Red/Amber/Green] |
| 3 | [Third obligation] | [X person-days] | [date] | [Red/Amber/Green] |
| 4 | [Fourth obligation] | [X person-days] | [date] | [Red/Amber/Green] |
| 5 | [Fifth obligation] | [X person-days] | [date] | [Red/Amber/Green] |

---

### Financial Exposure

| Category | Amount | Basis |
|----------|--------|-------|
| **Maximum penalty (non-compliance)** | EUR [X]M or [X]% turnover | Art. 99([X]) AI Act |
| **Estimated compliance investment** | EUR [range] | Internal estimate |
| **Revenue at risk (if withdrawn)** | EUR [X] p.a. | Current system contribution |
| **Compliance ROI** | Investment / penalty ratio: 1:[X] | Compliance cost vs. penalty exposure |

---

### Strategic Options

| Option | Description | Pro | Con | Cost | Risk |
|--------|-------------|-----|-----|------|------|
| **A: Full compliance** | Implement all required measures by deadline | Full market access; legal certainty | Investment required; resource allocation | EUR [X] | Low |
| **B: Phased compliance** | Prioritize critical obligations; defer others | Spreads cost; addresses highest risks first | Residual compliance gaps; enforcement risk | EUR [X] (initial) | Medium |
| **C: System modification** | Modify system to reduce risk tier (e.g., remove high-risk features) | Lower compliance burden | Reduced functionality; possible business impact | EUR [X] | Medium |
| **D: Discontinue** | Withdraw system from EU market | Eliminates compliance obligation | Revenue loss; operational impact | EUR [X] (lost revenue) | N/A |

---

### Recommendation

[1-2 sentences recommending specific option with brief justification]

---

### Decision Required

| Decision Point | Options |
|---------------|---------|
| **Approve compliance approach** | Option [A/B/C/D] as described above |
| **Authorize budget** | EUR [X] for compliance implementation |
| **Designate compliance owner** | [Proposed name/role] to lead implementation |
| **Set review cadence** | [Monthly/quarterly] progress reporting to [committee] |

**Decision:**  □ Approved  □ Approved with modifications  □ Deferred  □ Rejected

**Decision-maker:** _______________  **Date:** _______________

---

### Timeline to Next Milestone

```
[Current date] ─────► [Key milestone] ─────► [Compliance deadline]
      │                     │                        │
  Decision needed      [Description]          Full compliance
   [date]               [date]                  [date]
```

---

*Prepared by [name] | Full assessment documentation: [CLR-YYYY-NNN] | Register: [REG-YYYY-NNN]*
*This briefing does not constitute legal advice. Based on information available as of [date].*
```

### Quality Checklist — Management Briefing

- [ ] Maximum 2 pages when rendered
- [ ] Risk classification clearly indicated with visual marker
- [ ] Financial exposure includes both penalty and revenue risk
- [ ] All options include pros, cons, and cost
- [ ] Clear recommendation with justification
- [ ] Decision section with sign-off line
- [ ] References to full documentation (Classification Record, Register)
- [ ] No technical jargon without explanation
- [ ] Deadline prominently displayed
- [ ] Compliance percentage clearly stated
