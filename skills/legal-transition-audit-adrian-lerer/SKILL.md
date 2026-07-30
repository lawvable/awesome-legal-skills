---
name: "legal-transition-audit-ignacio-adrian-lerer"
description: "Audits the transition from legal AI output to reliance, recommendation, execution, or real-world commitment. Use it before an AI-generated analysis, memo, contract review, compliance finding, or workflow output is acted upon to check whether authority, evidence, mandate, uncertainty, procedure, and review conditions remain sufficient."
license: agpl-3.0
metadata:
  author: "Ignacio Adrián Lerer"
  license: "agpl-3.0"
  version: "2026-06-03"
---

# Legal Transition Audit

## What This Skill Does

This skill audits the step between legal AI output and real-world consequence.

It is designed for the moment when an analysis may become reliance, a recommendation may become action, or an automated workflow may affect rights, duties, deadlines, assets, filings, communications, or institutional decisions.

It does not replace legal analysis. It governs the transition from analysis to action.

## Core Question

Should this output be allowed to move into reliance, recommendation, execution, or commitment now?

## Transition States

Use one of these states:

- `PROCEED`: the transition is supported and may move forward.
- `QUALIFY`: the output may be used only with visible limits, caveats, or assumptions.
- `ESCALATE`: the transition requires human, specialist, client, institutional, or procedural review.
- `REFUSE`: the transition must not occur because material conditions are missing or invalid.

## Audit Protocol

### 1. Identify the Proposed Transition

State what movement is being proposed:

- draft to final;
- analysis to recommendation;
- recommendation to client advice;
- review to approval;
- approval to signature;
- finding to filing;
- output to automated execution;
- internal assessment to external communication;
- legal conclusion to operational or financial consequence.

If no transition is specified, classify the output as analysis only.

### 2. Consequence Mapping

Identify what changes if the transition occurs:

- rights, duties, liabilities, deadlines, payments, assets, or records;
- court, regulator, client, counterparty, employee, consumer, shareholder, or public-facing effect;
- irreversible or difficult-to-reverse consequence;
- reputational, compliance, privilege, confidentiality, or procedural impact.

The stronger the consequence, the stronger the transition controls must be.

### 3. Evidence Sufficiency

Check whether the output has enough evidentiary support for the proposed transition.

Ask:

- Are source documents, legal authorities, and factual premises identified?
- Are material citations current and verifiable?
- Are missing facts visible?
- Are assumptions separated from verified facts?
- Are conflicts or contrary authorities disclosed?
- Is the conclusion stronger than the evidence permits?

If evidence is insufficient, the output may not proceed without qualification, escalation, or refusal.

### 4. Authority and Mandate

Check whether the system, user, or institution has authority to make the transition.

Ask:

- Who authorized the transition?
- What is the source and scope of the mandate?
- Does the mandate cover this jurisdiction, matter, client, entity, risk, or action?
- Has authority expired, been revoked, exceeded, or become contested?
- Does the transition require approval by a lawyer, client, board, supervisor, court, regulator, or other institutional actor?

Do not allow an output to create authority for itself.

### 5. Procedure and Timing

Check whether procedural conditions remain satisfied at the moment of transition.

Ask:

- Are deadlines, limitation periods, procedural steps, notices, approvals, or waiting periods still valid?
- Has the legal or factual context changed since the output was generated?
- Has a new document, instruction, evidence item, policy, or authority superseded the basis of the output?
- Is the transition occurring after interruption, handoff, delegation, restoration, or reentry?

If conditions have changed, re-test before action.

### 6. Uncertainty and Contestability

Check whether uncertainty remains visible and contestable before reliance.

Material uncertainty includes:

- unresolved factual disputes;
- ambiguous legal standards;
- conflicting authorities;
- stale or unverified sources;
- jurisdictional mismatch;
- unclear client objectives;
- unresolved privilege or confidentiality issue;
- model/tool limitations that affect the conclusion.

If uncertainty is hidden by fluent prose, do not proceed.

### 7. Transition Decision

Assign a transition state:

- `PROCEED` only if evidence, authority, procedure, timing, and uncertainty controls are sufficient.
- `QUALIFY` if the output may be used with explicit limits.
- `ESCALATE` if a responsible person or institution must decide.
- `REFUSE` if the transition would be unsupported, unauthorized, procedurally defective, or materially misleading.

## Output Format

```markdown
## Legal Transition Audit

Transition State: PROCEED | QUALIFY | ESCALATE | REFUSE

### Proposed Transition
| From | To | Consequence | Status |
|---|---|---|---|

### Transition Conditions
| Condition | Finding | State |
|---|---|---|
| Evidence sufficiency |  |  |
| Authority and mandate |  |  |
| Procedure and timing |  |  |
| Uncertainty visibility |  |  |
| Contestability |  |  |

### Blocks or Qualifications
| Issue | Effect on transition | Required action |
|---|---|---|

### Permitted Use
- May be used for:
- Must not be used for:
- Required before further action:
```

## Non-Negotiable Rules

- Do not move from output to action merely because the output is plausible or well written.
- Do not allow uncertainty to disappear at the point of reliance.
- Do not treat authority, mandate, evidence, or procedure as historical facts only; they must remain valid when the transition occurs.
- Do not execute, file, sign, send, approve, or advise on the basis of an output whose transition state is `ESCALATE` or `REFUSE`.
- The transition itself is the object of review.
