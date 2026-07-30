# Failure Modes

Run this checklist after the review draft is complete and before the final answer is sent.

## Intake Failures

| Failure | What It Looks Like | Mandatory Fix |
|---|---|---|
| Missing party identity | Recommendations do not reflect which side the user represents. | Re-check intake and revise priorities. |
| Missing role context | Advice ignores whether the user is legal, procurement, sales, privacy, or security. | Re-run priority weighting with role overlay. |
| Missing controlling document | Analysis references the wrong version or ignores the redline. | Identify the controlling version and restate assumptions. |

## Reading Failures

| Failure | What It Looks Like | Mandatory Fix |
|---|---|---|
| Exhibit blindness | Main agreement reviewed but schedules or policies ignored. | Build document map and review attachments. |
| Defined term drift | Redlines or comments use terms inconsistently. | Re-check definitions and dependent clauses. |
| Cross-reference miss | A clause is changed without checking linked sections. | Verify every impacted cross-reference. |
| Missing incorporated docs | URLs, policies, order forms, or DPAs are ignored. | Flag missing docs and assess the risk of that gap. |

## Analysis Failures

| Failure | What It Looks Like | Mandatory Fix |
|---|---|---|
| Generic issue spotting | Output could have been written without reading this contract. | Tie every issue to a clause citation and contract fact. |
| Loose playbook comparison | Contract is judged against intuition instead of normalized positions. | Rebuild clause comparison against the playbook schema. |
| Unscored returned markup | Counterparty changes are described without deviation scoring or impact labeling. | Re-score the returned draft against the playbook. |
| Context dilution | Too much contract and playbook text is loaded at once and mid-document issues are missed. | Re-run with structured partial loading and clause-network retrieval. |
| Missing ancillary-document trigger | SLA, security schedule, AI terms, BAA, DORA, or financial-cloud schedule need is not checked. | Re-run ancillary-document checks from intake and document map. |
| Static prioritization | Every issue is treated the same regardless of role or paper side. | Re-apply priority matrix. |
| Hallucinated market standard | Output claims a provision is nonstandard without support. | Replace with playbook-based or user-based reasoning. |
| Missing omission analysis | Absent clauses are not identified. | Add missing-clause analysis for the relevant contract type. |

## Redline Failures

| Failure | What It Looks Like | Mandatory Fix |
|---|---|---|
| Over-editing | Low-risk clauses are heavily rewritten without benefit. | Narrow the edit to the real risk. |
| Broken drafting | Redline breaks grammar, defined terms, or structure. | Re-draft for legal and linguistic coherence. |
| No fallback | Output says to reject without giving a backup path. | Add acceptable fallback positions. |
| Inconsistent edits | Multiple clauses conflict after revisions. | Harmonize the redlines across the agreement. |

## Negotiation Failures

| Failure | What It Looks Like | Mandatory Fix |
|---|---|---|
| No concession ladder | Everything is labeled critical. | Distinguish must-win, tradeable, and low-leverage points. |
| No business rationale | User cannot explain the ask to the counterparty. | Add one-line negotiation rationale for each major issue. |
| Missing leverage analysis | Strategy ignores urgency, paper owner, or deal value. | Update negotiation plan with leverage factors. |

## Approval Failures

| Failure | What It Looks Like | Mandatory Fix |
|---|---|---|
| Missed security review | Security schedule reviewed as purely legal language. | Route to security. |
| Missed privacy review | DPA or AI-use terms lack privacy escalation. | Route to privacy. |
| Missed finance review | Pricing mechanics or liability economics lack finance approval. | Route to finance. |
| Missed product review | Scope or roadmap commitments lack product review. | Route to product or engineering. |

## Output Failures

| Failure | What It Looks Like | Mandatory Fix |
|---|---|---|
| No missing-docs list | User cannot tell what would improve confidence. | Add missing docs and open questions. |
| No uncertainty statement | The answer sounds certain despite missing context. | Add confidence notes and assumptions. |
| No QA trace | Final answer does not show that quality gates were run. | Add QA and benchmark summary. |
| No seriousness signal | User cannot tell which returned changes are serious versus minor. | Add deviation score, impact band, color label, and confidence. |
| No region or sector trigger summary | User cannot tell whether BAA, DORA, SLA, security schedule, AI terms, or financial-cloud schedule checks were run. | Add ancillary-document and regulatory-trigger summary. |

## Stop Conditions

Do not finalize the review if any blocker remains in these categories:

- Wrong party or role assumptions
- Unreviewed exhibits or incorporated docs
- Missing analysis of critical clauses
- Broken or conflicting redlines
- Missing required cross-functional approvals
