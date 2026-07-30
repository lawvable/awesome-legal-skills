---
name: eu-ai-act-fria
description: Assess whether a Fundamental Rights Impact Assessment (FRIA) is required under Article 27 EU AI Act, and structure or draft that assessment for a specific high-risk AI deployment. Covers deployer scope gating (public bodies and private entities providing public services), affected group mapping, Charter rights analysis, proportionality, safeguards evaluation, residual risk, DPIA/FRIA interaction, notification under Article 27(3), and DACH-specific considerations. Use when asked about FRIA obligations, Article 27 scope, fundamental rights and AI, or deployer assessment duties.
---

# Fundamental Rights Impact Assessment (FRIA) - EU AI Act Article 27

Assess whether a deployer must perform a Fundamental Rights Impact Assessment (FRIA) under Article 27 of the EU AI Act, and structure that assessment for a specific high-risk AI use case before the system is put into use.

**Important:** This skill supports a structured legal-compliance workflow. It does **not** replace legal judgment. A FRIA is inherently contextual and should never be treated as a box-ticking exercise. Always identify assumptions, open questions, and contested interpretations explicitly.

**Before you start:** If you have **not** yet confirmed that the system is a **high-risk AI system**, use the **EU AI Act System Classifier** first. Article 27 applies only in the context of **high-risk AI systems** and only for a **subset of deployers**.

## FRIA Workflow

Follow this sequence in order. Do not skip the scope questions.

### Step 1 - Confirm the threshold question: is this a high-risk AI system?

Article 27 only applies where the intended use concerns a **high-risk AI system** within the meaning of the AI Act.

Check:
1. Has the system already been classified as high-risk under Annex III or as a product-safety high-risk system?
2. What is the concrete use case in which the deployer wants to use it?
3. Is the analysis tied to a specific deployment context, not just the tool in abstract?

**If high-risk status is not yet confirmed:** stop here and use the **EU AI Act System Classifier** first.

### Step 2 - Scope: is this deployer actually required to perform a FRIA?

This is the most important gating step.

Article 27 does **not** apply to all deployers of high-risk AI. It applies to deployers that are:
- **Bodies governed by public law**, or
- **Private entities providing public services**, including contexts such as banking, insurance, and healthcare services.

Assess carefully:
1. Is the entity a public authority, municipality, ministry, agency, public university, statutory body, or another body governed by public law?
2. If private: is it providing a **public service** in the relevant context, rather than merely offering a private commercial tool?
3. Is the entity acting as **deployer** (using the system under its authority) rather than as provider/importer/distributor only?
4. Is the use case the deployer's own operational use, not a hypothetical downstream use by others?

**If NO:** document that Article 27 FRIA is not mandatory for this deployer, while separate deployer obligations under Article 26 may still apply.

**If YES:** proceed.

### Step 3 - Timing: when must the FRIA be done?

A FRIA must be carried out:
- **Before first putting the high-risk AI system into use** for the specific use case,
- Again where there is a **significant change** in the system, its purpose, or its use context, and
- At the level of the **specific deployment context/use case**, not only once per system in the abstract.

Check:
1. Has the system already gone live for this use case?
2. Is this a new deployment, pilot, procurement, or operational expansion?
3. Has anything materially changed: model, data, user population, decision logic, human oversight, geography, purpose, or integration?
4. Are there multiple use cases requiring separate or modular FRIAs?

### Step 4 - Define the use case and operational context precisely

Article 27(2) requires the FRIA to be grounded in the deployer's actual processes.

Document:
- Name of the system and provider
- High-risk qualification and legal basis
- Business/administrative process in which the system will be used
- Purpose of use and intended outputs
- Decision points influenced by the system
- Human actors involved
- Whether individuals can be subject to adverse effects, denial of access, differential treatment, surveillance, or exclusion

If the process description is vague, the FRIA will be weak. Push for operational specificity.

### Step 5 - Map affected persons, groups, and rights at stake

Article 27(2) expressly requires the deployer to identify the **categories of natural persons and groups likely to be affected**.

Map:
1. Directly affected individuals
2. Indirectly affected groups
3. Vulnerable groups or groups with structural disadvantages
4. Persons with limited ability to contest outcomes
5. Employees/workers if the system affects workforce decisions or monitoring

Then identify which **fundamental rights** are realistically at stake under the **EU Charter of Fundamental Rights**, including where relevant:
- Human dignity
- Respect for private life
- Protection of personal data
- Non-discrimination
- Equality between women and men
- Rights of the child
- Freedom of expression and information
- Freedom to conduct a business
- Consumer protection
- Right to good administration
- Right to an effective remedy and fair trial
- Presumption of innocence and rights of defence
- Healthcare-related rights and social protection depending on context

→ For the detailed rights catalogue and examples, read references/fundamental-rights-catalogue.md.

### Step 6 - Assess specific risks of harm

Article 27(2) requires identification of the **specific risks of harm likely to impact** the identified persons/groups.

Assess, for each relevant right and affected group:
- What harm could occur?
- Through what mechanism?
- Who bears the burden?
- Is the harm temporary or lasting?
- Can it be reversed or remedied?
- Would the affected person even know the system contributed to the outcome?

Use a structured assessment across:
- **Likelihood** of the impact occurring
- **Severity** of the impact if it occurs
- **Reversibility** / ability to remedy or undo the harm
- **Scale** / number of persons affected
- **Proportionality** between the operational goal and the rights impact
- **Necessity** of using AI for this purpose at all

→ For the scoring method and decision framework, read references/fria-methodology.md.

### Step 7 - Evaluate safeguards, human oversight, and data quality measures

Article 27(2) requires a description of:
- **Human oversight measures**, and
- Measures to be taken if risks materialise,
- Plus, for deployers under Article 26(3)(a), measures ensuring compliance with relevant **data quality** requirements.

Check existing safeguards such as:
- Human review before adverse decisions
- Escalation thresholds and override rights
- Clear role allocation and accountability
- Logging and traceability
- Quality checks on input data
- Bias/error monitoring
- User training and operating instructions
- Complaint mechanisms and redress pathways
- Incident response and stop-use procedures
- Procurement controls and contractual commitments from providers

The question is not whether a safeguard exists on paper, but whether it is **effective for this specific risk**.

### Step 8 - Determine residual risk, proportionality, and go/no-go recommendation

After accounting for safeguards, assess the **residual risk**.

Ask:
1. Is the interference with rights justified, necessary, and proportionate in the concrete context?
2. Are there less rights-intrusive alternatives?
3. Are vulnerable groups exposed to disproportionate burdens?
4. Are the oversight and complaint mechanisms strong enough to catch real-world failure?
5. Should the use proceed, proceed only with conditions, or not proceed until mitigations are implemented?

This is the core judgment section. Do not auto-approve because controls exist. Explain the reasoning.

### Step 9 - Notification analysis under Article 27(3)

If the FRIA identifies a **specific risk** to the rights of natural persons or groups of persons, the deployer must notify the relevant **market surveillance authority**.

Where the risk relates to processing of personal data and is relevant under data protection law, the deployer must also notify the competent **data protection authority**.

Check:
1. Did the FRIA identify a specific risk, not merely a generic abstract possibility?
2. Which authority is competent in the relevant Member State and sector?
3. Does the matter also trigger GDPR analysis, consultation, or separate supervisory engagement?
4. What should be notified, with what evidence, and at what stage?

→ For authority mapping and notification structure, read references/notification-requirements.md.

### Step 10 - Check whether a combined FRIA + DPIA is appropriate

Under Article 27(4), the FRIA may be conducted **together with** a GDPR Article 35 Data Protection Impact Assessment (DPIA), where relevant.

Do not merge them blindly. First determine:
- Is personal data processed?
- Is a DPIA independently required under GDPR Article 35?
- Are the main risks privacy/data-protection risks only, or broader rights risks?
- Will a joint structure improve coherence, or obscure the broader fundamental-rights analysis?

**Key point:** A DPIA and a FRIA overlap, but they are not the same thing. A FRIA extends beyond data protection into broader Charter rights, procedural fairness, access, equality, and remedy.

→ For overlap and integration guidance, read references/dpia-fria-interaction.md.

### Step 11 - Add the DACH overlay where relevant

If the deployment is in Germany, Austria, or Switzerland, consider the local governance and constitutional overlay.

In Germany in particular, assess:
- Interaction with the **Grundgesetz** as an additional analytical lens alongside the EU Charter
- Competence of the **BfDI** or **Landesdatenschutzbehörden**
- Potential role of **BNetzA** or sector-specific supervisory authorities
- Public procurement implications (e.g. specification, transparency, award-stage governance)
- **BetrVG** works council participation rights where employees are affected
- Administrative-law principles such as proportionality, equal treatment, and documentation of discretion

→ For DACH-specific analysis, read references/dach-specific.md.

## Quick Question Set

Use these questions at intake before drafting the FRIA:

**System and Scope**
1. What is the AI system, and has it already been confirmed as **high-risk**?
2. What is the exact **use case** for this deployer?
3. Is the deployer a **public body** or a **private entity providing a public service**?
4. Is the entity acting as **deployer**, not provider only?

**Operational Context**
5. In which process or decision workflow will the system be used?
6. What outputs does the system generate, and how are they used in practice?
7. How often will the system be used, over what time period, and at what scale?
8. Who are the human decision-makers or reviewers around the system?

**Affected Persons and Rights**
9. Which persons or groups are likely to be affected directly or indirectly?
10. Are vulnerable groups, children, patients, customers, benefit applicants, job candidates, or employees involved?
11. Which fundamental rights could realistically be interfered with?
12. What is the worst plausible harm for each key group?

**Safeguards and Governance**
13. What human oversight measures exist in real operation?
14. What complaint, appeal, or redress mechanisms exist?
15. What happens if the system produces an error, bias, or adverse outcome?
16. Are there data quality controls, logging, audits, or monitoring processes?

**DPIA / Notification / Change**
17. Is personal data processed, and has a DPIA been done or planned?
18. Has the use already started, or is this assessment still pre-deployment?
19. Has anything significantly changed since the last assessment?
20. Has the FRIA identified a **specific risk** that may require notification?

If key answers are missing, state assumptions and identify them as blockers or legal-risk gaps.

## Reference Files

Load these as needed during the assessment:

| File | When to read |
|------|-------------|
| references/fundamental-rights-catalogue.md | Mapping the rights at stake - Charter rights, practical AI impact examples |
| references/fria-methodology.md | Running the assessment - scoring, proportionality, residual risk, decision logic |
| references/dpia-fria-interaction.md | Determining whether/how to combine a FRIA with a GDPR DPIA |
| references/notification-requirements.md | Determining whether notification is required and how to structure it |
| references/dach-specific.md | Germany/Austria/Switzerland overlay - authorities, procurement, works council, constitutional lens |
| references/templates.md | Producing practical outputs - FRIA report, matrix, notifications, management briefing |

## Output Format

Every FRIA engagement should produce these deliverables:

1. **FRIA Scope Memo** - short determination of whether Article 27 applies, including deployer status, high-risk status, use-case boundary, timing, and whether a FRIA is mandatory.

2. **FRIA Report / Draft FRIA** - structured assessment covering Article 27(2) elements: process description, intended use period/frequency, affected groups, rights at stake, specific risks of harm, oversight measures, mitigation/governance measures, residual risk, and notification analysis.

3. **Rights Impact Matrix** - practical table mapping affected groups, relevant rights, risk mechanisms, inherent risk, existing safeguards, residual risk, and required actions.

4. **Management Briefing** - one-page decision note for leadership explaining whether deployment can proceed, under what conditions, and what must happen before go-live.

5. **Notification Pack (if required)** - draft notice to the market surveillance authority and, where relevant, the competent data protection authority.

→ For templates and model wording, read references/templates.md.

## Key Compliance Notes

- **This is a deployer obligation, not a provider obligation.**
- **Not all deployers are in scope.** The threshold question is whether the deployer is a public body or a private entity providing a public service.
- **The FRIA is use-case specific.** One system may require multiple FRIAs if used in materially different contexts.
- **Do not confuse FRIA with DPIA.** A DPIA may cover some of the same ground but will rarely be sufficient on its own.
- **Current timeline:** Article 27 obligations are currently scheduled to apply from **2 August 2026** under current law. The Digital Omnibus simplification package (Commission proposal December 2025) progressed to a Council/Parliament provisional political agreement on 7 May 2026; under that agreement, Annex III high-risk obligations (which include the Article 27 FRIA trigger) would shift to **2 December 2027**. The agreement is **not yet adopted law** — pending formal adoption and Official Journal publication. Apply the law as enacted unless and until amendments are formally adopted and in force.

## Disclaimer

This skill provides structured workflow support for Article 27 of Regulation (EU) 2024/1689 (EU AI Act). It does not constitute legal advice. Whether an entity is a body governed by public law, a private provider of public services, or whether a specific risk requires notification may depend on national law, sector rules, procurement structures, and supervisory practice. The analysis should be reviewed by qualified counsel, especially before deployment, authority engagement, or high-impact operational decisions.
