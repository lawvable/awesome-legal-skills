# Contract Intelligence & Workflow Reviewer

A contract intelligence, contract review, and contract operations workflow skill for Claude and Codex.

The goal is not to replace review of a contract by a legal professional. The goal is to help legal, legal operations, procurement, compliance, privacy, security, and business teams review contracts using a structured workflow rather than ad hoc prompting.

The skill helps reviewers in a contract review to understand what is likely signnificant, unusual, and missing, and where negotiation may be needed, who should be involved in approvals, and what actions should happen next.

## What This Skill Is

This skill combines:

- Contract review
- Contract intelligence
- Playbook-driven analysis
- Clause comparison
- Deviation scoring
- Negotiation planning
- Approval routing
- Workflow state management
- Contract operations controls
- Quality assurance and benchmarking

Rather than producing a simple list of issues, the skill follows a structured workflow intended to mirror how mature legal departments and legal operations teams manage contract review.

The skill can be used by legal, procurement, compliance, privacy, security, and business teams to improve consistency, issue spotting, negotiation preparation, approval coordination, and overall contract review quality.

## What This Skill Is Not

This skill is not a Contract Lifecycle Management (CLM) platform.

While the skill includes concepts commonly found in CLM systems, including workflow states, approval routing, playbook management, contract intelligence, and review artifacts, it does not provide the underlying infrastructure typically found in enterprise CLM platforms.

Examples include:

- Contract repositories
- Enterprise databases
- E-signature platforms
- Automated workflow engines
- Renewal tracking systems
- Obligation management systems
- Reporting dashboards
- Enterprise integrations

The skill is best viewed as complementary to CLM platforms such as Ironclad, Agiloft, DocuSign CLM, Sirion, ContractPodAI, Icertis, Conga, and similar solutions.

## What It Reviews

This skill reviews contracts from legal, business, operational, compliance, privacy, security, technology, and AI perspectives rather than focusing solely on contract language.

Examples include:

- Commercial terms
- Legal risks
- Operational obligations
- Compliance requirements
- Privacy and data protections
- Information security requirements
- Intellectual property provisions
- Vendor and third-party risks
- AI-related provisions
- Governance and reporting obligations
- Missing protections
- Ambiguous language
- Internal approval requirements
- Negotiation considerations

The skill identifies issues, explains why they matter, provides recommendations, and suggests next actions.

## Workflow Capabilities

The skill supports a structured contract workflow that may include:

1. Setup
2. Intake
3. Triage
4. Review
5. Redline
6. Negotiation
7. Internal Approvals
8. Signature Ready
9. Closed

Depending on available information, the skill may also:

- Normalize playbooks
- Compare contracts to standards
- Score deviations
- Generate negotiation plans
- Identify approval requirements
- Produce machine-readable action outputs
- Create review artifacts
- Generate executive summaries

## Intended Users

This skill may be useful for:

- Legal departments
- Legal Operations teams
- Procurement teams
- Contract managers
- Compliance professionals
- Privacy teams
- Security teams
- Commercial operations teams
- Business stakeholders involved in contract review

## Output

Depending on the documents and instructions provided, the skill may generate:

- Executive summaries
- Key terms and obligations
- Risk assessments
- Clause-by-clause findings
- Playbook comparison summaries
- Deviation scoring
- Negotiation plans
- Proposed redlines
- Approval routing recommendations
- Questions for internal stakeholders
- Escalation items requiring attorney review
- Action plans and next-step recommendations

## Considerations

Outputs should always be reviewed by appropriate legal, compliance, privacy, security, procurement, or business stakeholders.

The skill can identify issues and provide analysis, but it cannot determine business risk tolerance, negotiation strategy, legal conclusions, or regulatory requirements for every jurisdiction and situation.

Attorney review remains essential for significant transactions, regulatory matters, strategic agreements, and high-risk negotiations.

## Token Usage Warning

This skill is intentionally comprehensive and ***may consume a significant number of tokens***.

Unlike a simple contract-review prompt, this skill applies multiple workflow stages, review controls, playbook requirements, approval-routing logic, quality checks, benchmarking criteria, and output structures before generating a final review.

Token consumption can increase when:

- Reviewing long agreements
- Reviewing multiple agreements
- Processing large playbooks
- Comparing multiple contract versions
- Reviewing exhibits and schedules
- Processing incorporated documents
- Performing clause-by-clause analysis
- Generating detailed redlines
- Creating negotiation plans
- Producing approval packages
- Generating structured review artifacts
- Producing comprehensive reports

Large contracts combined with large playbooks can consume substantial context windows and result in higher LLM costs.

When token efficiency is needed, consider:

- Reviewing individual sections separately
- Using a triage review first
- Limiting supporting documents
- Requesting targeted analysis
- Reducing output detail

## Best Results

For the most complete review:

- Provide the full agreement whenever possible.
- Include exhibits, schedules, attachments, and referenced documents.
- Provide the applicable playbook if available.
- Provide templates or standard paper if available.
- Identify the represented party.
- Provide relevant business context.
- Identify specific concerns or negotiation objectives.

The quality of the review improves significantly when both the contract and the organization's review standards are available.

## Notes on CLM Capabilities

During development I explored how far AI Skills could be pushed beyond traditional contract review.

The result includes a number of features commonly associated with contract intelligence, operations, and contract lifecycle processes, including:

- Structured intake
- Playbook management
- Contract intelligence extraction
- Workflow states
- Approval routing
- Deviation scoring
- Negotiation planning
- Quality assurance controls
- Review artifacts
- Machine-readable actions

While these capabilities are often portions of a CLM system, I found that current Skills and LLM platforms are still not well suited for many CLM capabilities that depend on persistent systems and enterprise platforms, such as:

- Contract repositories
- Structured contract records
- **Persistent contract metadata**
- Workflow engines
- Obligation management
- Renewal management
- Reporting and dashboards
- Enterprise integrations (especially Salesforce)
- Cross-system syncs

As a result, this project focuses on contract intelligence, contract review, workflow guidance, and decision support rather than attempting to replace a dedicated CLM platform. That said, the framework may serve as a foundation for experimentation as models mature and improve support for broader CLM capabilities.

## Disclaimer

This skill provides analysis, recommendations, workflow guidance, and decision-support information.

It does not provide legal advice and should not be relied upon as a substitute for advice from qualified legal counsel.
