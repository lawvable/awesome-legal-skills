# Benchmarking

Use this rubric to push the review above generic contract-review output before finalizing.

This rubric is designed to exceed the baseline capabilities commonly described in public materials for playbook-based AI review tools: clause detection, issue spotting, automated redlines, playbook comparison, and workflow routing. The review is not complete unless it also shows strong intake discipline, role-aware prioritization, approval routing, failure-mode control, and explicit QA.

## Minimum Threshold

Score each dimension from 1 to 5. Revise the work until every dimension is at least 4.

## Rubric

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Intake completeness | Missing key facts or role context | Most context captured but some key gaps | Contract, role, side, goals, risk posture, and missing docs all clear |
| Playbook rigor | Loose intuition only | Some comparison to standards | Clear normalized playbook with preferred, fallback, and prohibited positions |
| Priority alignment | Static risk list | Some contract-type adjustment | Contract-type, role, side, and business context all shape the result |
| Clause coverage | Obvious clauses only | Main clauses reviewed | Whole agreement reviewed, including exhibits and omissions |
| Redline quality | Generic or broken edits | Reasonable edits with some gaps | Precise drafting, fallback ladder, and consistent integration across clauses |
| Negotiation usefulness | Issues listed only | Some strategy provided | Clear must-win points, fallbacks, leverage notes, and counterparty rationale |
| Approval routing | Bare mention of stakeholders | Some departments named | Specific reviewers and approval triggers tied to clauses |
| Uncertainty handling | Overconfident | Some caveats | Explicit assumptions, confidence levels, and re-check items |
| QA traceability | No evidence of checking | Generic QA statement | Concrete QA verdict tied to the test plan and failure modes |

## Benchmark Questions

Ask these questions before sending the answer:

1. Would an in-house lawyer be able to act on this without rereading the whole contract from scratch?
2. Does the output tell the user what matters most for their role and side of the paper?
3. Are the redlines specific enough to send to the counterparty?
4. Are the fallback positions practical rather than theoretical?
5. Are non-legal reviewers clearly identified where needed?
6. Would the answer still make sense if challenged clause by clause?

If any answer is no, revise the work.

## Required Benchmark Summary

End the review with a concise benchmark summary:

```text
Benchmark Summary:
- Intake completeness: X/5
- Playbook rigor: X/5
- Priority alignment: X/5
- Clause coverage: X/5
- Redline quality: X/5
- Negotiation usefulness: X/5
- Approval routing: X/5
- Uncertainty handling: X/5
- QA traceability: X/5
```

Do not output the final review until all dimensions are 4 or 5.
