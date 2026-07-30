# Incident Qualification Guide

Use this reference to decide whether an event involving an AI system should be treated as a reportable **serious incident** under **Article 73 EU AI Act**.

## 1. First Gate: Is the System Actually High-Risk?

Article 73 only applies to **high-risk AI systems**.

### High-risk routes

#### Route A - Article 6(1)
The system is high-risk if:

- it is intended to be used as a **safety component** of a product, or is itself such a product, covered by **Annex I** legislation; and
- that product/system requires **third-party conformity assessment** before placing on the market or putting into service.

#### Route B - Article 6(2)
The system is high-risk if it falls within an **Annex III** use case.

#### Route C - Check the Article 6(3) exception
Even if the system is in Annex III, it is **not** high-risk where it does **not pose a significant risk of harm** to health, safety, or fundamental rights and does not materially influence decision-making, including where it only:

- performs a narrow procedural task
- improves the result of a completed human activity
- detects patterns/deviations without replacing or influencing the prior human assessment absent proper human review
- performs a preparatory task only

### Important carve-back
If the Annex III system **profiles natural persons**, it remains high-risk.

### Practical warning
A company should not assume Article 6(3) applies just because a human still exists somewhere in the loop. Ask whether the AI output **materially shapes outcomes** in practice.

## 2. Serious-Incident Thresholding

Article 73 relies on the defined concept of a **serious incident** in **Article 3(49)**.

In operational terms, ask whether the event caused, or plausibly contributed to, one of these outcomes:

- death of a person
- serious damage to a person’s health
- serious and irreversible disruption of management/operation of critical infrastructure
- serious breach of fundamental-rights protections

In practical internal triage, also escalate cases involving severe property or environmental harm for immediate legal review, because these often overlap with sector-specific safety regimes and may be framed under the AI Act through the relevant serious-harm/fundamental-rights lens depending on the facts.

## 3. Qualification Decision Tree

### Tree A - Core Article 73 Logic

1. **Was an AI system involved?**
   - No → not Article 73
   - Yes → continue

2. **Is it actually a high-risk AI system?**
   - No → Article 73 not triggered
   - Unclear → urgent classification review
   - Yes → continue

3. **Did an incident occur in operation, output, integration, foreseeable misuse, or human oversight?**
   - No → likely not reportable
   - Yes → continue

4. **Did it cause or plausibly contribute to a severe outcome?**
   - death
   - serious health harm
   - serious fundamental-rights impact
   - critical infrastructure disruption
   - potentially equivalent sectoral severe harm

5. **Is there a causal link or reasonable likelihood of one?**
   - Yes → reportability analysis active
   - No, but facts are incomplete → urgent evidence preservation and reassessment
   - Clearly no → document and monitor

### Tree B - Causation Questions

Use these prompts to assess “causal link” or “reasonable likelihood”:

- Did the AI output directly drive a harmful act or omission?
- Did the system fail to flag a risk it was intended to catch?
- Did the UI or workflow make inappropriate reliance foreseeable?
- Was the incident caused by bad input data the deployer controlled?
- Did integration, versioning, or model drift create the failure mode?
- Would the incident likely have happened without the AI system?
- Did the AI materially influence human decision-making even if a human technically approved the result?

If several answers are yes, “reasonable likelihood” is often already met.

## 4. Examples

### Likely reportable

#### Example 1 - Clinical triage failure
A hospital uses a high-risk clinical AI module embedded in a medical workflow. The system deprioritises a critical case and the patient suffers major health harm.

- High-risk? Likely yes
- Severe harm? Yes
- Causal link? At least reasonably likely
- Action: treat as likely reportable, plus MDR/IVDR vigilance review

#### Example 2 - Hiring system fundamental-rights breach
An Annex III employment AI system materially filters candidates in a discriminatory manner and repeatedly excludes protected groups. The impact is serious, systematic, and tied to the model logic.

- High-risk? Likely yes
- Serious incident? Potentially yes where serious rights impact is evidenced
- Action: escalate immediately; consider AI Act + GDPR + labour implications

#### Example 3 - Critical infrastructure optimisation failure
A system used in critical infrastructure operations generates a faulty recommendation set, causing serious and irreversible operational disruption.

- High-risk? Possibly yes depending on use case
- Serious incident? Likely yes
- Action: immediate escalation; possible 2-day bucket depending on classification of harm

### Often not reportable, but still recordable

#### Example 4 - Minor customer inconvenience
A chatbot adjacent to a regulated workflow produces confusing but non-material guidance, quickly corrected by staff, with no serious harm.

- High-risk? Maybe not
- Serious incident? No
- Action: log as product issue; improve controls

#### Example 5 - Internal draft-support tool in HR
An internal system only reformats recruiter notes and does not influence hiring outcome.

- Annex III context? Maybe adjacent
- Article 6(3) exception? Likely applies
- Serious incident? Unlikely under Article 73

## 5. Edge Cases

### Edge case A - Near miss
No harm happened, but only because a human caught the error seconds before execution.

- If the legal threshold is not met, Article 73 may not be triggered
- But record it in post-market monitoring immediately
- Review whether the same failure could recur with actual harm

### Edge case B - Misuse by deployer
The deployer ignored instructions for use.

- This does **not automatically eliminate** reporting
- The question is whether the AI system still plausibly contributed and whether misuse was reasonably foreseeable

### Edge case C - Human approved the decision
A human clicked approve, but in practice relied entirely on the model.

- Human sign-off alone does not break causation
- Ask whether the AI materially influenced the outcome

### Edge case D - Model issue vs integration issue
The core model may be fine, but the incident came from thresholds, wrappers, prompts, or data pipelines.

- Still potentially reportable if the high-risk AI system as placed on the market or put into service is implicated

## 6. Evidence to Preserve Immediately

- logs and timestamps
- model/version/build identifiers
- input and output samples
- screenshots/video of UI and workflow
- user actions and approvals
- instructions for use applicable at incident time
- deployment configuration
- alerts, tickets, and complaint history
- communications with deployer/customer

## 7. Output Labels to Use

When summarising qualification, use one of these:

- **High confidence reportable serious incident**
- **Likely reportable serious incident**
- **Serious incident not yet established - urgent fact-finding needed**
- **Not a serious incident under current facts**
- **Out of scope because system not high-risk**
