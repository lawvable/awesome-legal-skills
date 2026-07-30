# FRIA and DPIA Interaction - Article 27 AI Act and Article 35 GDPR

This reference explains how a **Fundamental Rights Impact Assessment (FRIA)** under Article 27 AI Act relates to a **Data Protection Impact Assessment (DPIA)** under Article 35 GDPR.

## Core Rule

Article 27(4) AI Act allows a FRIA to be conducted **together with** a DPIA where the conditions for a DPIA are met.

This means:
- a combined process is permitted,
- duplication should be avoided where sensible,
- but the FRIA must still cover its own broader subject matter.

A DPIA is **not automatically sufficient** as a FRIA.

## Main Difference in One Sentence

- **DPIA:** focuses on risks arising from the **processing of personal data**.
- **FRIA:** focuses on risks to **fundamental rights more broadly**, including but not limited to data protection.

## Where They Overlap

A DPIA and a FRIA overlap heavily when a high-risk AI system processes personal data and affects individuals in a significant way.

### Shared themes
- description of the processing / use case,
- purpose and operational context,
- affected persons,
- risk identification,
- mitigation measures,
- governance and accountability,
- review and updating.

### Typical overlap areas
- privacy,
- data protection,
- transparency,
- accuracy and data quality,
- security,
- monitoring and incident handling,
- human oversight for consequential decisions.

## What a FRIA Adds Beyond a DPIA

A FRIA extends beyond data protection into broader Charter rights and practical public-interest concerns.

### Areas often covered by FRIA but not fully by DPIA
- non-discrimination and equality impacts,
- access to essential services,
- dignity and dehumanisation concerns,
- fair administration and due process,
- access to effective remedy,
- effects on children or vulnerable groups,
- broader proportionality/necessity of using AI in the context,
- public-law and constitutional concerns.

A DPIA may mention some of these, but usually not with the same structure or depth.

## When a Combined FRIA + DPIA Usually Makes Sense

Use a joint structure where:
- the system processes personal data extensively,
- a DPIA is clearly required,
- the FRIA and DPIA concern the same use case,
- the project team can maintain a single governance process without losing analytical clarity.

### Common good-fit examples
- healthcare triage or diagnostic support,
- public-benefit or anti-fraud systems,
- insurance underwriting using personal data,
- banking risk or eligibility systems,
- employee-related high-risk AI in public-sector or public-service settings.

## When Separate Documents May Be Better

Use separate but cross-referenced documents where:
- the DPIA already exists and is mature,
- different teams own data protection and broader rights compliance,
- the broader rights issues are much more significant than the pure data-protection issues,
- the organisation needs a governance document specifically addressed to Article 27.

## Practical Joint Structure

If combining the assessments, structure the document in modules so both legal regimes remain visible.

### Recommended combined outline

1. Executive summary
2. System / use case overview
3. Roles and legal bases
4. High-risk AI qualification and Article 27 scope
5. GDPR processing description and DPIA trigger analysis
6. Affected groups and stakeholder mapping
7. Fundamental rights analysis (FRIA section)
8. Data protection risk analysis (DPIA section)
9. Safeguards, oversight, governance, and controls
10. Residual risks and proportionality
11. Notification / consultation analysis
12. Decision, approvals, and review cycle

This structure keeps the FRIA visible instead of hiding it inside privacy sections.

## Trigger Questions

### Ask whether a DPIA is likely required
- Is personal data processed?
- Is special-category data involved?
- Is there systematic and extensive evaluation of personal aspects?
- Are automated or high-impact decisions involved?
- Is there monitoring of publicly accessible areas or large-scale sensitive processing?
- Do national blacklists/whitelists from supervisory authorities apply?

If yes, a DPIA may be required independently of the FRIA.

### Ask whether a FRIA is required
- Is the system high-risk under the AI Act?
- Is the deployer a body governed by public law or a private entity providing a public service?
- Is the system being put into use in a specific deployment context?

If yes, Article 27 may require a FRIA independently of the DPIA.

## Consultation and Authority Interface

Do not confuse the authority pathways.

### DPIA-side
Under GDPR, a high residual risk can trigger **prior consultation** with the supervisory authority where the controller cannot sufficiently mitigate the risk.

### FRIA-side
Under Article 27(3), identifying a **specific risk** to the rights of natural persons or groups can trigger notification to the **market surveillance authority**, and where relevant, also the competent **data protection authority**.

These are related but not identical triggers.

## Drafting Tips for a Combined Assessment

A good combined FRIA + DPIA should:
- use one factual description of the system and use case,
- avoid duplicating risk scenarios word-for-word,
- distinguish clearly between privacy/data risks and broader rights risks,
- maintain separate conclusions where the legal triggers differ,
- show one integrated action plan and review cycle.

## Common Mistakes

Avoid these errors:
1. Treating the DPIA as automatically satisfying Article 27.
2. Discussing only privacy while ignoring equality, remedy, or access issues.
3. Hiding the FRIA trigger analysis inside a generic AI governance memo.
4. Forgetting that public-service and public-body deployers may face both regimes at once.
5. Failing to explain the difference between GDPR consultation and AI Act notification.

## Recommended Practical Approach

If both assessments are relevant:
- prepare **one integrated evidence base**,
- maintain **distinct legal sections** for FRIA and DPIA,
- use **one shared risk/action table** where possible,
- obtain review from both privacy and broader legal/governance stakeholders,
- and record explicitly that the document is intended to satisfy both Article 27 AI Act and Article 35 GDPR requirements.
