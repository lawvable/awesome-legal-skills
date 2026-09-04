---
name: eu-ai-act-fria
description: Assess whether a Fundamental Rights Impact Assessment (FRIA) is required under Article 27 EU AI Act, and structure or draft that assessment for a specific high-risk AI deployment. Covers deployer scope gating (public bodies and private entities providing public services), affected group mapping, Charter rights analysis, proportionality, safeguards evaluation, residual risk, DPIA/FRIA cross-referencing under the amended Article 27(4), the unconditional notification duty under Article 27(3), and DACH-specific considerations. Use when asked about FRIA obligations, Article 27 scope, fundamental rights and AI, or deployer assessment duties.
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
1. Has the system been classified as high-risk under **Art. 6(2)**, that is Annex III? Art. 27 applies only to Art. 6(2) systems. **Art. 6(1) product-safety high-risk systems are outside Art. 27 entirely**, and Annex III **point 2** (critical infrastructure) is expressly excepted.
2. What is the concrete use case in which the deployer wants to use it?
3. Is the analysis tied to a specific deployment context, not just the tool in abstract?

**If high-risk status is not yet confirmed:** stop here and use the **EU AI Act System Classifier** first.

### Step 2 - Scope: is this deployer actually required to perform a FRIA?

This is the most important gating step.

Article 27 does **not** apply to all deployers of high-risk AI. Art. 27(1) sets two alternative gates:
- **Gate A, status-based:** the deployer is a **body governed by public law** or a **private entity providing public services**, deploying any in-scope Annex III system, or
- **Gate B, system-based:** the deployer, public or private, deploys an Annex III **point 5(b)** system (creditworthiness evaluation or credit scoring) or **point 5(c)** system (risk assessment and pricing in life and health insurance). A bank scoring credit or an insurer pricing life or health cover owes a FRIA regardless of any public-service character.

In both gates, Annex III **point 2** systems are excepted, and the system must be high-risk under **Art. 6(2)**.

Assess carefully:
1. Is the entity a public authority, municipality, ministry, agency, public university, statutory body, or another body governed by public law?
2. If private: is it providing a **public service** in the relevant context, or is it deploying a point 5(b) or 5(c) system, which triggers the duty on its own?
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

Article 27(1)(a) and (b) require the FRIA to be grounded in the deployer's actual processes and intended period and frequency of use. (Article 27(2) is a different rule: it makes the duty attach to first use, allows reliance on previously conducted assessments in similar cases, and requires updating when elements change.)

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

Article 27(1)(c) expressly requires the deployer to identify the **categories of natural persons and groups likely to be affected** in the specific context of use.

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

Article 27(1)(d) requires identification of the **specific risks of harm likely to have an impact** on the identified persons or groups, taking into account the provider's Art. 13 instructions.

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

Article 27(1)(e) and (f) require a description of:
- the implementation of **human oversight measures**, according to the instructions for use, and
- the **measures to be taken where risks materialise**, including the arrangements for internal governance and complaint mechanisms.

There is no data-quality element in Art. 27. The deployer's duty to ensure input data is relevant and sufficiently representative is a separate obligation under **Art. 26(4)**, in so far as the deployer exercises control over the input data; cover it in the deployer-obligations track, not as FRIA content.

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

**Notification is not conditional on finding a risk.** Article 27(3) requires that, once the assessment under Article 27(1) has been performed, the deployer notify the **market surveillance authority** of its results, submitting the filled-out template referred to in Article 27(5) as part of the notification. A FRIA that concludes the risks are adequately mitigated is still notified. The only carve-out in the text is the case referred to in Article 46(1), where deployers may be exempt from the duty to notify. Article 27(3) was **not** amended by Regulation (EU) 2026/1744, which touched only paragraphs 4 and 5.

Where the assessment also concerns processing of personal data and is relevant under data protection law, engagement with the competent **data protection authority** may be required separately, for example prior consultation under Article 36 GDPR. That is a GDPR duty, not part of Article 27(3).

Check:
1. Has the Article 27(1) assessment been completed? If yes, the notification duty is triggered regardless of the outcome.
2. Does the Article 46(1) case apply, so that the exemption from notifying may be available?
3. Which market surveillance authority is competent in the relevant Member State and sector?
4. Has the AI Office template under Article 27(5) been published? Until it is, agree the submission format with the authority and record that the template was not yet available.
5. Does the matter also trigger GDPR analysis, prior consultation, or separate supervisory engagement?
6. What should be notified, with what evidence, and at what stage?

→ For authority mapping and notification structure, read references/notification-requirements.md.

### Step 10 - Check whether a combined FRIA + DPIA is appropriate

Article 27(4) as replaced by Regulation (EU) 2026/1744 states the rule precisely: where an Art. 27 obligation is already met through a DPIA conducted under Art. 35 GDPR or Art. 27 of Directive (EU) 2016/680, the deployer may **include cross-references to the relevant sections** of that DPIA, or **include the relevant parts of it**, in the FRIA. That is a cross-referencing and incorporation rule; running the two assessments as one combined process can be operationally sensible, but what the paragraph authorises is the cross-reference.

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
1. What is the AI system, and has it already been confirmed as **high-risk under Art. 6(2)** (Annex III)? Art. 6(1) product systems are outside Art. 27, and Annex III point 2 is excepted.
2. What is the exact **use case** for this deployer?
3. Is the deployer a **public body** or a **private entity providing a public service** (Gate A)?
4. Independently of question 3: is the system an Annex III **point 5(b)** creditworthiness/credit-scoring or **point 5(c)** life/health-insurance system? If yes, **every** deployer owes the FRIA (Gate B).
5. Is the entity acting as **deployer**, not provider only?

**Operational Context**
6. In which process or decision workflow will the system be used?
7. What outputs does the system generate, and how are they used in practice?
8. How often will the system be used, over what time period, and at what scale?
9. Who are the human decision-makers or reviewers around the system?

**Affected Persons and Rights**
10. Which persons or groups are likely to be affected directly or indirectly?
11. Are vulnerable groups, children, patients, customers, benefit applicants, job candidates, or employees involved?
12. Which fundamental rights could realistically be interfered with?
13. What is the worst plausible harm for each key group?

**Safeguards and Governance**
14. What human oversight measures exist in real operation?
15. What complaint, appeal, or redress mechanisms exist?
16. What happens if the system produces an error, bias, or adverse outcome?
17. Are there data quality controls, logging, audits, or monitoring processes?

**DPIA / Notification / Change**
18. Is personal data processed, and has a DPIA been done or planned?
19. Has the use already started, or is this assessment still pre-deployment?
20. Has anything significantly changed since the last assessment?
21. Has the Article 27(1) assessment been completed, so that the Article 27(3) notification duty is triggered? Note this duty applies to the results of every completed FRIA, not only to those identifying a specific risk. Does the Article 46(1) exemption case apply?

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

2. **FRIA Report / Draft FRIA** - structured assessment covering the Article 27(1)(a) to (f) elements: process description, intended use period/frequency, affected groups, rights at stake, specific risks of harm, oversight measures, mitigation/governance measures, residual risk, and notification analysis.

3. **Rights Impact Matrix** - practical table mapping affected groups, relevant rights, risk mechanisms, inherent risk, existing safeguards, residual risk, and required actions.

4. **Management Briefing** - one-page decision note for leadership explaining whether deployment can proceed, under what conditions, and what must happen before go-live.

5. **Notification Pack** - for every completed FRIA unless the Article 46(1) exemption applies: draft notice to the market surveillance authority with the completed Article 27(5) template. Assess any data-protection-authority engagement separately under data-protection law.

→ For templates and model wording, read references/templates.md.

## Key Compliance Notes

- **This is a deployer obligation, not a provider obligation.**
- **Not all deployers are in scope.** The gates are alternative: a public-law body or private public-service entity for any in-scope Annex III system, or any deployer, public or private, of an Annex III point 5(b) creditworthiness/credit-scoring or point 5(c) life/health-insurance system. Art. 6(1) product systems and Annex III point 2 are outside Art. 27.
- **The FRIA is use-case specific.** One system may require multiple FRIAs if used in materially different contexts.
- **Do not confuse FRIA with DPIA.** A DPIA may cover some of the same ground but will rarely be sufficient on its own.
- **Current timeline:** Article 27 obligations apply from **2 December 2027**. The Digital Omnibus simplification package amending the EU AI Act was adopted on 8 July 2026 and published in the Official Journal on 24 July 2026 as Regulation (EU) 2026/1744, entering into force on 27 July 2026. It deferred Annex III high-risk obligations (which include the Article 27 FRIA trigger) from 2 August 2026 to **2 December 2027**. Article 50 transparency obligations and the start of Commission GPAI enforcement powers were not deferred and continue to apply from 2 August 2026. Apply the law as amended in force.

- **Article 27(4) and (5) were both replaced on 27 July 2026** by Regulation (EU) 2026/1744, and they change how the FRIA may be produced:
  - **Paragraph 4, DPIA cross-referencing.** Where an obligation under Article 27 is already met through a data protection impact assessment under Article 35 GDPR or Article 27 of Directive (EU) 2016/680, the deployer may include cross-references to the relevant sections of that DPIA, or include the relevant parts of it, in the FRIA. What the paragraph authorises is the cross-reference or incorporation of relevant DPIA parts; whether to run the two assessments as one combined process remains an operational choice the text neither requires nor presumes. Step 10 of this skill should be read with that in mind.
  - **Paragraph 5, the AI Office template.** The AI Office is to develop a template questionnaire, expressly including through an automated tool, to help deployers comply in a simplified manner, and that template is to allow the same DPIA cross-references. Until it is published, this skill's own question set stands in for it. When it appears, prefer the official template and keep this skill as the reasoning layer around it.

## Disclaimer

This skill provides structured workflow support for Article 27 of Regulation (EU) 2024/1689 (EU AI Act). It does not constitute legal advice. Whether an entity is a body governed by public law, a private provider of public services, or how the Article 27(3) notification is to be submitted before the Article 27(5) template exists may depend on national law, sector rules, procurement structures, and supervisory practice. The analysis should be reviewed by qualified counsel, especially before deployment, authority engagement, or high-impact operational decisions.
