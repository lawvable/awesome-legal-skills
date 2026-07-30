# Notification Requirements under Article 27(3)

This reference explains the notification logic for Article 27(3) AI Act after a Fundamental Rights Impact Assessment (FRIA).

## Legal Trigger

Article 27(3) provides that where the FRIA identifies a **specific risk** to the rights of natural persons or groups of persons, the deployer must notify the relevant **market surveillance authority**.

Where the identified risk relates to the processing of personal data and falls within the competence of a data protection authority, the deployer must also notify the competent **data protection authority**.

## Key Interpretive Point

The trigger is not every theoretical or abstract risk.

The FRIA should ask whether it has identified a **specific risk** in the concrete deployment context. In practice, this usually means a sufficiently concrete, evidence-based, use-case-specific risk that is material enough to warrant authority awareness.

## Working Test for “Specific Risk”

Treat a risk as potentially notifiable where most of the following are true:
- the risk is tied to the actual deployment, not a generic possibility,
- affected persons/groups can be identified,
- the harm mechanism is clear,
- the impact may be serious, repeated, or hard to reverse,
- current safeguards do not fully neutralise the issue,
- the matter is relevant to compliance, safety, equality, privacy, or procedural rights in a significant way.

## Notification Decision Questions

1. What is the exact risk scenario?
2. Which persons or groups are affected?
3. Which right(s) are implicated?
4. How severe and likely is the risk?
5. What safeguards already exist?
6. Why is the risk still specific enough to elevate to an authority?
7. Does the risk also engage data protection law?
8. Is any other authority already involved (sector regulator, procurement authority, works council, DPO)?

## Likely Notification Scenarios

Examples where notification analysis is especially important:
- persistent discrimination indicators affecting access to public services,
- healthcare AI with patient-safety and equality concerns,
- public-benefit or anti-fraud systems creating significant procedural unfairness,
- systems affecting children or vulnerable populations,
- high-impact personal-data processing creating unresolved residual risks,
- situations where meaningful remedy or oversight is weak.

## Relevant Authorities

### 1. Market surveillance authority

This is the primary AI Act authority for Article 27(3) notification.

The competent authority depends on Member State designation and may vary by sector. Always verify the currently designated authority in the relevant jurisdiction.

### 2. Data protection authority

Notify the competent supervisory authority as well where the specific risk is relevant to personal-data processing and falls within GDPR/data protection competence.

This may be especially relevant where:
- a DPIA indicates high residual risk,
- special-category data is involved,
- systemic profiling or monitoring occurs,
- data quality or fairness issues affect rights materially.

## Germany / DACH Practical Direction

In Germany, notification analysis may involve:
- **BNetzA** in its AI Act market-surveillance role where designated/competent,
- the **BfDI** for federal public bodies,
- the relevant **Landesdatenschutzbehörde** for state-level or private controllers,
- sector authorities in regulated fields such as finance or health.

Always check the current allocation of competence at the time of assessment.

## Timing

The AI Act does not turn Article 27(3) into a “wait and see” obligation.

Good practice:
- assess the trigger during the FRIA,
- escalate internally before go-live,
- prepare the notification pack before launch if the trigger is met,
- and update or supplement the notification if the facts change materially.

## Suggested Notification Contents

A notification should normally include:
- deployer identity and contact details,
- system name, provider, version, and high-risk basis,
- description of the use case,
- summary of affected persons/groups,
- identified rights and risk scenarios,
- severity / likelihood / reversibility assessment,
- existing safeguards and why risk remains specific/material,
- mitigation plan and timeline,
- whether the use has started or is paused,
- point of contact for follow-up.

Keep the narrative factual and specific. Avoid generic statements such as “AI may affect rights.”

## Internal Escalation Before External Notification

Before notifying externally, the deployer should normally ensure internal escalation to:
- legal/compliance,
- data protection officer,
- AI governance owner,
- operational owner,
- senior management or accountable sponsor,
- and, where relevant, procurement or HR/works council stakeholders.

This should not become a reason for delay. The goal is coordinated, defensible notification.

## Relationship to Other Duties

Notification under Article 27(3) may sit alongside, but is distinct from:
- GDPR prior consultation,
- personal-data breach notification,
- serious-incident reporting,
- sector-specific notification duties,
- procurement disclosure obligations,
- internal escalation under vendor/customer contracts.

Do not collapse all of these into one label.

## Practical Drafting Standard

A good Article 27(3) notification position should answer three things clearly:
1. **Why this risk is specific**
2. **Why it matters for rights in this deployment**
3. **What the deployer is doing about it**

## Caution

Where the notification question is close, document both sides of the interpretation and escalate for legal review. The FRIA should preserve the reasoning trail even if the organisation ultimately concludes that notification is not required.
