# Output Formats

Use this structure for final answers. Keep it concise, but do not omit required sections.

## Standard Final Review Format

```text
Review Status
- Mode:
- Workflow State:
- Next Recommended State:
- Documents Reviewed:
- Missing Documents / Open Questions:

Action Decision
- Recommended next action:
- Why this is the right next step:
- Human approval required:
- Approved destination or tool:

Intake Recap
- Represented Party:
- User Role:
- Paper Owner:
- Contract Type:
- Business Goal:
- Risk Posture:
- Required Internal Reviewers:

Playbook Comparison Summary
- Overall playbook compatibility score:
- Aligned items:
- Within fallback:
- Material deviations:
- Serious deviations:
- Blockers:

Ancillary Document And Regulatory Trigger Summary
- SLA present or required:
- Security measures or schedule present or required:
- AI terms present or required:
- BAA required:
- DORA review required:
- Financial-cloud schedule required:
- Trigger confidence:

Regulatory And Legal Basis Summary
- Relevant regulatory frameworks:
- Extra-territorial regimes:
- Governing law:
- Independent regulatory obligations:
- Legal basis or market-practice basis for key positions:
- Confidence:

Priority Model Summary
- Top Critical Clauses:
- High-Priority Clauses:
- Deprioritized Items:

Executive Summary
- Overall risk view:
- Signature blockers:
- Main negotiation points:

Issue Table
| Clause | Playbook Status | Deviation Score | Impact Band | Color | Risk | Why It Matters | Regulatory / Legal Basis | Recommended Position | Suggested Redline | Acceptable Fallback | Approver / Reviewer | Confidence |

Negotiation Plan
- Must-win points:
- Tradeable points:
- Business-facing rationale:
- Leverage notes:

Approval Required Before Execution
| Function | Trigger | What Needs Review | Approver | Contact / Target | Blocking? |

Machine-Readable Action Packet
- Action type:
- State transition:
- Destination:
- Required approvals:
- Notification mode:
- Saved artifacts:

QA Verdict
- Blockers:
- Accuracy:
- Completeness:
- Remaining caveats:

Benchmark Summary
- Intake completeness:
- Playbook rigor:
- Priority alignment:
- Clause coverage:
- Redline quality:
- Negotiation usefulness:
- Approval routing:
- Uncertainty handling:
- QA traceability:
```

## Triage Format

Use only for quick screens or incomplete documents. Still include:

- Review status and scope limit
- Intake recap
- Top issues only
- Playbook compatibility snapshot
- Regulatory and legal basis snapshot
- Next recommended action
- Missing documents
- Required internal reviewers
- What remains before a full review

## Redline Guidance

If the user asks specifically for redlines, include either:

- Inline proposed wording, or
- A clause-by-clause redline set with preferred and fallback language

Do not provide redlines without explaining why the edit matters.

## Automation Artifacts

When filesystem saving is enabled, also generate:

- `action-packet.yaml`
- `review-summary.json`
- `approval-routing.json`
- `workflow-state.yaml`
- `metrics.yaml`
- `playbook-comparison.csv`
