---
name: "legal-mdl-audit-ignacio-adrian-lerer"
description: "Audits legal AI outputs and workflows for honest compression: unnecessary complexity, false simplicity, excessive caveats, hidden uncertainty and poor cost per legally acceptable output."
license: agpl-3.0
metadata:
  author: "Ignacio Adrián Lerer"
  license: "agpl-3.0"
  version: "2026-05-31"
---

# Legal MDL Audit

## What this skill does

This skill reviews whether a legal AI answer, prompt, workflow, benchmark result, contract review, memo, compliance report, or agent chain is as simple as it can safely be.

It is inspired by Minimum Description Length: good legal reasoning should explain more with less structure, but never by hiding material uncertainty.

## Audit categories

Classify the material as:

- APPROVE: lean and still legally safe.
- APPROVE WITH CONSTRAINTS: complexity is justified, but reliance needs stated limits.
- REWRITE: the output is too complex, repetitive, expensive, or hard to audit.
- QUARANTINE: the output is falsely simple and hides material uncertainty.

## Checklist

Review:

1. Rules: how many legal propositions are needed?
2. Exceptions: how many carve-outs or qualifications are doing real work?
3. Conditions: what facts, dates, forums, sources or procedural states must hold?
4. Sources: are citations enough, excessive, or missing?
5. Uncertainty: what must remain visible?
6. Workflow cost: how many model/tool/human steps were needed?
7. Output value: did added complexity improve legal acceptability?

## Output format

Return:

1. Verdict.
2. Complexity drivers.
3. Hidden uncertainty or omitted hard cases.
4. What can be simplified.
5. What must not be removed.
6. Safer shorter version, if requested.

## Rules

- Do not reward short answers that erase legal uncertainty.
- Do not reward long answers that add caveats without improving reliance.
- Prefer cost per legally acceptable output over cost per token or API call.
- Preserve source gaps, authority boundaries and human-review gates.
