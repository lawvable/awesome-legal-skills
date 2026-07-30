---
name: "decision-ownership-audit-ignacio-adrian-lerer"
description: "Audits AI-assisted legal, compliance, governance, and institutional decisions before reliance to determine whether the responsible human or institution has enough access to the evidence, reasoning basis, uncertainty, authority, and review path to genuinely own the decision rather than merely approve, sign, or transmit it."
license: agpl-3.0
metadata:
  author: "Ignacio Adrián Lerer"
  license: "agpl-3.0"
  version: "2026-06-03"
---

# Decision Ownership Audit

## What This Skill Does

This skill audits whether a person or institution can responsibly rely on an AI-assisted legal or governance output before approving, signing, filing, sending, enforcing, or otherwise acting on it.

It does not ask only whether the output is correct, plausible, well written, or formally reviewed. It asks whether the responsible actor has enough access to the basis of the decision to stand behind it as a professional or institutional judgment.

Use it for legal memos, litigation strategy, contract review, compliance decisions, regulatory responses, board materials, risk approvals, due diligence conclusions, policy determinations, and other outputs that may move from analysis into reliance.

## Core Question

Can the responsible human or institution genuinely own this decision, or are they merely ratifying an output whose basis they cannot inspect, contest, or correct?

## Audit Protocol

### 1. Responsible Actor Identification

Identify who is expected to own the decision.

Classify the actor as:

- lawyer or legal team;
- client or business decision-maker;
- compliance officer;
- board, committee, or management body;
- public authority or institutional officer;
- automated or semi-automated workflow with a named human sponsor.

If no responsible actor is identifiable, the output is not ready for reliance.

### 2. Decision Surface

State what the actor is being asked to do with the output:

- read only;
- use as background;
- rely on for professional analysis;
- recommend a course of action;
- approve, sign, file, send, or enforce;
- execute through an automated system;
- affect third-party rights, duties, assets, deadlines, or legal position.

Higher-consequence uses require stronger ownership conditions.

### 3. Evidence Access

Check whether the actor can inspect the evidence supporting each material conclusion.

The output should expose:

- source documents or legal authorities;
- relevant clauses, facts, sections, pages, or records;
- missing evidence;
- conflicting evidence;
- source reliability or currency concerns;
- whether a conclusion is based on the document, external law, inference, professional judgment, or policy.

If the evidence cannot be inspected, mark the decision as ownership-deficient.

### 4. Reasoning Access

Check whether the actor can reconstruct the reasoning path at the level required for the decision.

The output should show:

- the legal or operational issue;
- the rule, standard, mandate, or criterion applied;
- the material facts used;
- the inference from facts to conclusion;
- alternatives considered;
- why rejected alternatives were rejected;
- the limits of the analysis.

Do not treat a post-hoc explanation, summary, confidence score, or fluent conclusion as sufficient by itself.

### 5. Uncertainty Visibility

Identify uncertainty that affects ownership:

- contested legal interpretation;
- missing facts;
- stale or unverified legal authority;
- ambiguous document language;
- dependency on assumptions;
- jurisdictional mismatch;
- unresolved factual or evidentiary conflict;
- model, retrieval, or tool limitations.

Uncertainty must be visible enough to influence the decision before reliance occurs.

### 6. Authority and Competence

Check whether the actor has authority and competence for the specific decision.

Ask:

- Does the actor have mandate, role, or delegation to make this decision?
- Does the mandate cover this matter, jurisdiction, client, entity, or transaction?
- Has the mandate expired, been limited, or been superseded?
- Does the actor need specialist review?
- Does the decision require client, board, court, regulator, partner, or supervisor approval?

Formal responsibility is not enough if the actor lacks authority or practical competence.

### 7. Contestability and Correction

Check whether the actor can challenge and correct the output before action.

The workflow should allow:

- requesting source support;
- correcting facts;
- changing assumptions;
- escalating uncertain issues;
- rejecting unsupported conclusions;
- preserving an audit trail of material changes.

If the workflow allows only accept/send/execute, ownership is weak.

## Verdicts

Use one of these states:

- `PASS`: the responsible actor can inspect evidence, reasoning, uncertainty, authority, and review path before reliance.
- `REVIEW`: minor gaps exist, but the output is not yet being used for consequential action.
- `ESCALATE`: specialist, supervisory, client, institutional, or procedural review is required before reliance.
- `BLOCK`: the output is being used for consequential action while the responsible actor cannot inspect or contest its material basis.

## Output Format

```markdown
## Decision Ownership Audit

Verdict: PASS | REVIEW | ESCALATE | BLOCK

### Responsible Actor
| Actor | Expected role | Decision surface | Status |
|---|---|---|---|

### Ownership Conditions
| Condition | Finding | Status |
|---|---|---|
| Evidence access |  |  |
| Reasoning access |  |  |
| Uncertainty visibility |  |  |
| Authority and competence |  |  |
| Contestability and correction |  |  |

### Ownership Gaps
| Gap | Why it matters | Required fix |
|---|---|---|

### Reliance State
- What can be relied on now:
- What cannot be relied on yet:
- What must be reviewed or escalated:

### Required Next Step
```

## Non-Negotiable Rules

- Do not equate signature, approval, or human review with genuine decision ownership.
- Do not treat fluency, confidence, or a polished explanation as evidence of ownership.
- Do not allow consequential reliance when evidence, reasoning, authority, or uncertainty is inaccessible.
- If the responsible actor cannot inspect and contest the material basis, say so directly.
- The goal is not to eliminate AI assistance; it is to prevent formal accountability without substantive ownership.
