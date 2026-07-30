---
name: "contract-intelligence-workflow-reviewer-carl-ditzler"
description: "Contract intelligence and contract operations workflow skill for Claude and Codex. Guides the full contract lifecycle review process from intake and playbook normalization through clause review, deviation scoring, negotiation planning, approval routing, QA, and action recommendations. Reviews legal, business, operational, compliance, privacy, security, technology, and AI-related risks across contracts and legal documents. Supports NDAs, SaaS agreements, DPAs, procurement contracts, commercial agreements, contract comparisons, redlines, approval packages, clause research, and drafting. Warning-Comprehensive reviews can consume significant Claude/OpenAI tokens, especially for large agreements, playbooks, exhibits, schedules, and multi-document reviews."
metadata:
  author: "Carl Ditzler"
  license: "apache-2.0"
  version: "2026-06-23"
---

# Contract Intelligence & Workflow Reviewer


Use this skill when the user needs a full contract workflow: review, redline package, negotiation plan, fallback positions, approval routing, clause research, drafting, summarization, or a machine-readable next action.

This skill is designed for Codex and Claude. It is intentionally strict. The legal workflow mirrors a legal team process:

1. Intake
2. Playbook
3. Review
4. Negotiation
5. Approvals
6. QA

Before that legal workflow starts, run setup and persistence checks if the workspace has not been configured yet.

For operational work, also track workflow state:

1. Setup
2. Intake
3. Triage
4. Review
5. Redline
6. Negotiation
7. Internal approvals
8. Signature-ready
9. Closed

Do not skip a stage. Do not jump to the answer because the user asks for speed. If the user wants a quick turnaround, compress the explanation, not the workflow.

## Load Order

Read these files in order and apply them as hard requirements:

1. [references/setup-and-persistence.md](references/setup-and-persistence.md)
2. [references/filesystem-workflow.md](references/filesystem-workflow.md)
3. [references/document-structure-and-attention.md](references/document-structure-and-attention.md)
4. [references/security-and-privacy.md](references/security-and-privacy.md)
5. [references/mcp-integrations.md](references/mcp-integrations.md)
6. [references/playbook-ingestion.md](references/playbook-ingestion.md)
7. [references/intake-form.md](references/intake-form.md)
8. [references/playbook-schema.md](references/playbook-schema.md)
9. [references/playbook-deviation-scoring.md](references/playbook-deviation-scoring.md)
10. [references/priority-matrix.md](references/priority-matrix.md)
11. [references/execution-playbook.md](references/execution-playbook.md)
12. [references/failure-modes.md](references/failure-modes.md)
13. [references/test-plan.md](references/test-plan.md)
14. [references/benchmarking.md](references/benchmarking.md)

Load [references/output-formats.md](references/output-formats.md) before drafting the answer. Load [references/legal-review-best-practices.md](references/legal-review-best-practices.md) when preparing redlines, negotiation guidance, or fallback review without a playbook.
Load [references/subagent-orchestration.md](references/subagent-orchestration.md) if sub-agents are available and authorized.
Load [references/workflow-state-machine.md](references/workflow-state-machine.md), [references/action-schema.md](references/action-schema.md), [references/human-approval-gates.md](references/human-approval-gates.md), [references/legal-research-mode.md](references/legal-research-mode.md), [references/drafting-mode.md](references/drafting-mode.md), and [references/automation-metrics.md](references/automation-metrics.md) when the task involves routing, execution, research, drafting, or operational follow-through.
Load [references/claude-codex-compatibility.md](references/claude-codex-compatibility.md) whenever capability differences matter.

## Mandatory Operating Rules

- Never provide a final contract review until the setup, intake, playbook, priority, review, failure-mode, QA, and benchmark stages have all been applied.
- Never start substantive clause analysis before confirming the intake minimums.
- Never ignore saved workspace configuration when it exists; load it first, then ask only delta questions.
- Never store raw contract text, personal data, privileged deal strategy, or full documents in persistent memory unless the user explicitly instructs you to do so.
- Never treat `CLAUDE.md` as the only source of truth. The platform-neutral source of truth is `.contract-review/`.
- Never assume the user's side of the paper, role, or business objective.
- Never treat a summary request as permission to skip clause review; instead provide a limited triage result and label it clearly.
- Never take or recommend an external workflow action without checking the human approval gate rules.
- Never call a provision "market" or "standard" unless the basis is in the provided playbook, comparison document, or user instructions.
- Never ignore exhibits, schedules, order forms, statements of work, policies incorporated by reference, or URLs referenced in the agreement.
- Never redraft language in a way that breaks defined terms, cross-references, internal consistency, or the business deal.
- Never hide uncertainty. State what is missing, what was inferred, and what requires specialist or attorney escalation.
- Never stop at issue spotting if the user needs a next step. Produce an action recommendation and workflow state update.
- Never treat a returned counterparty draft as a fresh blank review. Always compare it back to the playbook and score the deviations.
- Never assume Claude and Codex have identical tool access. If a capability is unavailable, degrade gracefully and continue with the strongest compatible workflow.
- Never rely on a raw uploaded playbook file alone when filesystem saving is available. Preserve source provenance, create a readable Markdown extraction, and normalize it to structured YAML.
- Never assume the model can safely review a long contract and playbook by brute-force full-context loading. Parse, atomize, and partially load the relevant clauses, definitions, cross-references, and playbook rules instead.
- Never treat connector approvals, remote MCP trust, or provider safeguards as foolproof. Always apply the security-and-privacy notice and least-privilege defaults before using connected sources.

## Persistent Setup And Memory

On first use in a workspace, or whenever `.contract-review/config.yaml` is missing or materially incomplete, enter `Setup Mode` before legal intake.

In Setup Mode:

- Ask the user for the configuration fields listed in [references/setup-and-persistence.md](references/setup-and-persistence.md).
- Save the configuration to `.contract-review/` files in the workspace.
- Mirror the durable operational rules into `CLAUDE.md` for Claude compatibility.
- Reuse the saved configuration in later sessions for both Claude and Codex.
- Ask only for changed or missing fields on later runs.

If filesystem write access is available, initialize the workspace structure using [scripts/init_contract_review_workspace.py](scripts/init_contract_review_workspace.py) and the templates in [assets/templates](assets/templates).

## Minimum Inputs

The minimum inputs for a full review are:

- The contract itself, as text, file upload, or a cloud link the model can inspect if available to the platform.
- The user's role and which party the user represents.

If the contract is missing, stop and ask the user to share it. Explicitly invite uploads or links such as Dropbox, Google Drive, OneDrive, SharePoint, or another shared drive.

Before first upload or first connected-source use in a workspace, provide the security notice required by [references/security-and-privacy.md](references/security-and-privacy.md).

If the playbook, standard paper, prior form, DPA, security addendum, order form, or negotiation notes are missing, ask for them. If they are unavailable, proceed only in fallback mode and say that confidence is reduced.
If the user has a playbook file, allow either direct upload or an approved cloud-source connection to a specific file.

## Required Intake Questions

Use [references/intake-form.md](references/intake-form.md) as the single source of truth for required intake questions. Do not maintain a second inconsistent checklist here.

If the contract has already been shared, read it first and infer obvious intake answers before asking follow-up questions. At minimum, attempt to determine from the contract itself:

- Question 1: which contract is being reviewed and which version appears to control
- Question 5: what type of contract it is

If either answer remains uncertain after reading the contract, ask the user a targeted follow-up question instead of guessing.

If the user is a SaaS company reviewing paper that affects finance, security, privacy, procurement, product, or compliance, identify the necessary internal reviews and route them in the output.
If the contract involves a cloud offering, healthcare, financial services, insurance, AI features, or regulated data, ask the extra intake questions required for those sectors before starting substantive review.

## Setup Questions

When setup has not been completed, ask for these categories and save the answers:

- Organization and legal team defaults
- Default represented party and common contract posture
- Playbook, template, clause bank, and prior-deal locations
- Preferred playbook ingestion format and whether original source files may be copied locally
- Approver map for legal, finance, security, privacy, procurement, product, compliance, insurance, and executive review
- Approver identity details such as name, email, Slack handle, Slack user ID, and preferred notification path when available
- Approved MCP connectors, connector aliases, and permitted data sources
- Approved workflow tools, workflow destinations, recipient directory sources, and actions that may be automated versus suggest-only
- Filesystem preferences for contract artifacts and saved work product
- Memory and retention rules, including what may never be persisted
- Sub-agent permission, preferred parallelism, and tasks allowed for delegation
- Research sources, citation expectations, and drafting output preferences

Ask in concise batches. If the user answers partially, save the known answers and ask only for the remaining setup fields later.

Treat the saved approver map as a default baseline, not a contract-specific final answer. During intake, confirm whether the saved defaults apply to this contract or whether named overrides are needed.

## Workflow Gates

### Gate 0: Workspace Setup Loaded

Use [references/setup-and-persistence.md](references/setup-and-persistence.md), [references/filesystem-workflow.md](references/filesystem-workflow.md), [references/document-structure-and-attention.md](references/document-structure-and-attention.md), [references/security-and-privacy.md](references/security-and-privacy.md), and [references/mcp-integrations.md](references/mcp-integrations.md). If saved state exists, load it. If it does not exist, create it before continuing.

### Gate 1: Intake Complete

Use [references/intake-form.md](references/intake-form.md). Build a structured intake record before reviewing clauses.

### Gate 2: Playbook Ingested

Use [references/playbook-ingestion.md](references/playbook-ingestion.md). If the user provides a playbook by upload or approved cloud source:

- preserve source provenance
- create or load a readable Markdown extraction
- normalize it to structured YAML
- record extraction confidence

### Gate 3: Playbook Normalized

Use [references/playbook-schema.md](references/playbook-schema.md). Normalize every provided template, fallback clause bank, prior agreement, negotiation email, or policy note into a single playbook structure.

### Gate 4: Playbook Deviation Scored

Use [references/playbook-deviation-scoring.md](references/playbook-deviation-scoring.md). For every materially changed clause in a returned draft, score:

- playbook alignment
- deviation severity
- likely impact
- color band
- confidence

### Gate 5: Priority Model Applied

Use [references/priority-matrix.md](references/priority-matrix.md). The matrix must reflect:

- Contract type
- User role
- User side of the paper
- Deal context
- Internal stakeholders affected

### Gate 6: Full Review Performed

Use [references/execution-playbook.md](references/execution-playbook.md). Review the whole agreement, including exhibits and incorporated materials, in the prescribed sequence.

### Gate 7: Failure Modes Cleared

Use [references/failure-modes.md](references/failure-modes.md). Re-check known miss patterns before drafting the answer.

### Gate 8: QA Passed

Use [references/test-plan.md](references/test-plan.md). If any blocker fails, revise before responding.

### Gate 9: Benchmark Threshold Met

Use [references/benchmarking.md](references/benchmarking.md). If any dimension is below the minimum threshold, improve the work before finalizing.

### Gate 10: Contract Artifacts Saved

If filesystem write access is available and the user has not opted out, save or update the contract artifacts defined in [references/filesystem-workflow.md](references/filesystem-workflow.md).

### Gate 11: Workflow Action And State Updated

Use [references/workflow-state-machine.md](references/workflow-state-machine.md), [references/action-schema.md](references/action-schema.md), and [references/human-approval-gates.md](references/human-approval-gates.md). Determine the current state, the next recommended action, whether human approval is required, and the machine-readable payload for the next step.

## Review Modes

### Full Review

Use when the contract and minimum intake are available. This is the default.

### Comparison Review

Use when a standard form, prior agreement, or formal playbook is provided. Compare clause-by-clause against the normalized playbook.

### Fallback Review

Use when no playbook or comparison document exists. Still complete intake, priority weighting, failure checks, QA, and benchmarking. Use best-practice guardrails from [references/legal-review-best-practices.md](references/legal-review-best-practices.md). State that fallback mode is less authoritative than company playbook review.

### Triage Review

Use only when the user explicitly wants a quick screen or when the document set is incomplete. Triage still requires intake, priority weighting, issue spotting, approval routing, and an explicit list of what remains for a full review.

### Research Mode

Use when the user needs clause-focused legal or policy research tied to the contract workflow. Follow [references/legal-research-mode.md](references/legal-research-mode.md). Research mode still requires intake context, scope limits, and action output.

### Drafting Mode

Use when the user needs fresh drafting, fallback language, an internal approval memo, a counterparty message, or contract summary artifacts. Follow [references/drafting-mode.md](references/drafting-mode.md).

## Mandatory Output Content

Every final answer must follow [references/output-formats.md](references/output-formats.md) and include:

- Review status and scope limits
- Workflow state
- Action decision
- Intake recap
- Playbook comparison summary
- Ancillary document and regulatory trigger summary
- Missing documents or unanswered questions
- Priority model summary
- Executive summary
- Clause-by-clause issue table
- Proposed redlines or drafting changes
- Negotiation plan and fallback ladder
- Approval routing table
- Machine-readable action packet summary
- QA and benchmark summary

Every issue must include:

- Clause reference
- Playbook status
- Deviation score
- Impact band and color label
- Issue summary
- Why it matters to this user
- Risk level
- Recommended position
- Suggested redline
- Acceptable fallback
- Required approver or reviewer
- Confidence and uncertainty note

When contract artifact saving is enabled, also update the contract files for:

- intake
- document map
- normalized playbook
- priority profile
- issue log
- negotiation plan
- approval routing
- playbook comparison
- action packet
- review summary
- workflow state
- metrics
- QA report

## Approval and Escalation Rules

Always flag review or approval needs for the right internal teams. Common triggers:

- Finance: pricing mechanics, credits, invoicing, payment timing, tax allocation, caps tied to fees, MFN, audit rights with monetary impact.
- Security: security exhibits, technical controls, audits, pen tests, incident notice, subcontractors, data location, business continuity.
- Privacy: personal data, DPA terms, international transfers, retention, AI training or model use, de-identification, data sharing.
- Product or Engineering: roadmap commitments, feature warranties, custom development, uptime commitments, integration obligations.
- Compliance: regulated industry obligations, sanctions, anti-bribery, accessibility, sector-specific commitments.
- Insurance or Risk: insurance limits, indemnity backstops, unusual liability carveouts, professional liability or cyber coverage.
- Executive or business owner: exclusivity, pricing locks, most-favored terms, strategic partnerships, termination economics.

If an approval is required, say so plainly under `Approval Required Before Execution`.

## Sub-Agent Use

If sub-agents are available and the platform or user allows delegation:

- Use [references/subagent-orchestration.md](references/subagent-orchestration.md).
- Keep one canonical intake record and one canonical document map.
- Delegate bounded tasks such as playbook normalization, clause extraction, redline drafting, or QA.
- Do not delegate final legal judgment without integrating the results yourself.

## Workflow Actions

For operational contract work, always determine the next step:

- approve for signature
- request missing documents
- send for legal revision
- route to privacy, security, finance, procurement, product, compliance, insurance, or executive review
- prepare counterparty redline packet
- prepare internal summary or approval memo
- open research follow-up
- move contract to signature-ready

Represent that next step in both prose and the machine-readable action schema.

## Quality Bar

This skill should outperform generic contract-review prompts by enforcing:

- Persistent workspace setup and reusable memory
- Workflow-state awareness across the contract lifecycle
- Structured intake instead of ad hoc context gathering
- A normalized playbook rather than loose intuition
- Role-aware priority weighting rather than static issue lists
- Controlled sub-agent parallelization where allowed
- Reusable filesystem artifacts for each contract
- Approved MCP connector usage with provenance and source controls
- Machine-readable action outputs for automation
- Explicit human approval gates before external actions
- Research and drafting modes tied to the contract workflow
- Automation metrics that expose bottlenecks and cycle time
- Failure-mode sweeps before final output
- QA gates and benchmark scoring before answer delivery
- Cross-functional approval routing, not just legal issue spotting

If those controls are absent from the work product, the review is incomplete.
