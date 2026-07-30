# Playbook Deviation Scoring

Use this file whenever an in-progress contract, counterparty markup, or returned draft is being reviewed.

## Core Rule

If the contract has been changed by the counterparty or revised during negotiation, always compare the current draft back to the normalized playbook. Do not treat the returned draft as a standalone document.

## What To Score

For each materially changed or materially relevant clause family, score:

- playbook status
- deviation score
- likely impact
- color band
- confidence

## Required Status Values

Use one of:

- `aligned`
- `within fallback`
- `watch`
- `material deviation`
- `serious deviation`
- `deal blocker`

## Deviation Score

Use a 0 to 100 scale where higher means further away from the preferred position:

- `0-10`: aligned with preferred position
- `11-25`: within approved fallback
- `26-45`: small gap; watch item
- `46-65`: material deviation; should usually be revised
- `66-85`: serious deviation; likely significant business or legal impact
- `86-100`: deal blocker or unacceptable without explicit approval

## Impact Band And Color Label

Use these color labels in text:

- `Green`: negligible or low impact
- `Yellow`: limited impact; acceptable with awareness
- `Orange`: meaningful impact; likely needs negotiation or approval
- `Red`: serious impact; likely blocker or escalation item

## Likely Impact Labels

Use one of:

- `negligible`
- `low`
- `moderate`
- `high`
- `severe`

## Confidence Levels

Use:

- `High`: the clause text is clear and the playbook position is explicit
- `Medium`: the issue is understandable but there is some ambiguity or missing context
- `Low`: the clause or playbook basis is incomplete, conflicting, or uncertain

## Scoring Heuristics

Raise the score when:

- the clause moves away from the preferred position
- the clause exceeds the last acceptable fallback
- the change creates operational burden
- the change affects security, privacy, finance, compliance, or core commercial economics
- the change creates inconsistency with other clauses

Lower the score when:

- the clause stays within fallback
- the change is drafting-only and does not alter substance
- the change improves clarity without shifting risk materially

## Required Comparison Output

For each meaningful clause, record:

```text
Clause:
Playbook status:
Deviation score:
Impact band:
Color label:
Likely impact:
Why it matters:
Recommended response:
Confidence:
```

## Contract-Level Summary

Also provide an overall playbook comparison summary:

- number of aligned items
- number of fallback items
- number of material deviations
- number of serious deviations
- number of blockers
- overall playbook compatibility score

The overall playbook compatibility score should be `100 - weighted average deviation`, rounded to a whole number.

## Seriousness Rule

If a clause is scored `66` or higher, tell the user plainly that the change is serious and likely needs negotiation, escalation, or explicit approval.
