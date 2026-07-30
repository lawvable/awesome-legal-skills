# Execution Playbook

This file governs how to perform the review. Use it after intake, contract structure parsing, playbook normalization, and priority weighting.

## Review Sequence

Review in this order so high-impact issues are not buried:

1. Document map and completeness
2. Definitions, clause network, and cross-references
3. Parties and order of precedence
4. Business terms and scope
5. Data, privacy, security, service levels, and AI usage
6. IP, license, and ownership
7. Warranties, support, SLAs, and remedies
8. Indemnity and liability
9. Term, renewal, suspension, and termination
10. Compliance and insurance
11. Boilerplate and dispute mechanics
12. Exhibits, schedules, attachments, and incorporated materials
13. Signature blocks and legal names

## Step 1: Build the Document Map

List:

- Main agreement title and date
- Parties
- clause tree and section hierarchy
- key definitions and where they are defined
- cross-references that link major obligations
- All exhibits, schedules, annexes, policies, order forms, or URLs referenced
- Whether the contract includes or references an SLA, security measures, security schedule, AI terms, DPA, BAA, or financial-cloud schedule
- Whether the contract has an EU or EEA nexus and whether a DORA review or DORA applicability screen is required
- Missing referenced documents
- Whether you have a clean and redline version

Do not proceed as if a referenced document does not matter just because it was not supplied.
Do not load the full agreement and full playbook into the model by default if a structured partial-load path is available.

## Step 2: Clause-by-Clause Review Method

For each clause family:

1. Locate the clause and cite the section.
2. Summarize what the clause actually says.
3. Compare it to the normalized playbook or fallback standard.
4. If the draft has returned from the counterparty, score the deviation from the playbook.
5. Surface the regulatory frameworks and extra-territorial regimes that may apply to this clause or deal.
6. Distinguish governing law and dispute mechanics from independent regulatory or compliance obligations.
7. Explain the legal basis, contract-structure reason, or market-practice basis for the preferred position when that basis is material to the recommendation.
8. Explain why it matters to this user's side and role.
9. Assign the risk level from the working priority model.
10. Recommend the preferred position.
11. Draft a redline or drafting change when useful.
12. Provide an acceptable fallback if the preferred position is not available.
13. Identify the right approver or specialist reviewer.
14. Record uncertainty or missing context.

If the clause is missing, say so and explain whether the omission favors or harms the user.

For returned drafts, do not stop at "different from playbook." State whether the difference is serious, moderate, or minor using the deviation score, impact band, color label, and confidence level.

If a clause or deal implicates a regulatory framework, do not merely name the regime. State whether the obligation comes from the contract, from governing law, or from an independent regulatory framework that may apply regardless of the chosen governing law clause.

Load only the relevant clause, its linked definitions, its dependent cross-references, the relevant exhibit section, and the relevant playbook rule set for each comparison pass.

## Step 3: Redline Standard

When proposing edits:

- Prefer narrow edits that solve the real issue.
- Preserve defined terms and internal references.
- Avoid introducing new ambiguity.
- If a full rewrite is needed, explain why the original structure is not salvageable.
- Offer practical fallback language rather than only saying "reject."

## Step 4: Negotiation Logic

After issue spotting, build a negotiation plan:

- Identify must-win points.
- Identify tradeable points.
- Identify acceptable fallback positions.
- Note leverage based on deal value, urgency, paper owner, and commercial importance.
- Draft concise business-facing explanations the user can send to the counterparty.

Do not treat every issue as equally important. The negotiation plan should reflect the priority matrix.
Use the playbook deviation score to separate serious changes from low-impact drafting moves.

## Step 5: Approvals

Create an approval route whenever a clause affects another function. At minimum:

- Security for technical controls and audits
- Privacy for personal data terms
- Finance for pricing, credits, and liability economics
- Product or Engineering for custom scope, implementation, or roadmap commitments
- Compliance for regulated or public-sector obligations

Also trigger specific ancillary-document checks:

- BAA for U.S. healthcare-provider customers where PHI is transmitted, processed, or stored
- DORA applicability screen for EU or EEA nexus deals, and a full DORA review for qualifying financial-sector ICT or cloud arrangements
- enhanced financial-cloud schedule or equivalent addendum for EMEA insurance or financial-sector customers using cloud services
- SLA if service availability, uptime, support, or credits matter
- security measures or security schedule if security obligations are referenced or implied
- AI terms if the offering or contract mentions AI, model use, training, service improvement, or automated decisioning

For DORA review, check at minimum:

- ICT service scope and whether the service may support a regulated financial entity
- audit, access, and information rights
- security control commitments and incident support
- subcontractor or sub-outsourcing controls
- location, data access, and operational resilience commitments
- business continuity, exit, transition, and assistance rights
- concentration-risk, critical dependency, and cooperation language where relevant

If the user is a SaaS company reviewing customer paper, check especially for obligations that bind internal finance, corporate security, privacy, insurance, or product teams. Call out those dependencies explicitly.

## Step 6: No-Shallow-Review Rules

A shallow review is not acceptable. The review is shallow if any of these are true:

- Only the main body was read and exhibits were ignored.
- High-priority clauses were summarized without playbook comparison.
- Definitions, cross-references, or ancillary documents were not loaded with the clause they affect.
- Returned changes were described without scoring their deviation from the playbook.
- Issues were listed without proposed drafting or fallback paths.
- Cross-functional approvals were not considered.
- The answer lacks a record of missing documents or assumptions.
- The model gave generic boilerplate instead of contract-specific analysis.

If the work would be shallow, stop and deepen it before responding.

## Step 7: Special Handling for Missing Inputs

If the contract is present but comparison materials are missing:

- Continue in fallback mode.
- Mark the review as less authoritative than a playbook review.
- Call out which issues would be re-checked once the playbook or standard form is provided.

If parsing or extraction quality is weak:

- lower confidence
- state which clause-network or formatting dependencies may be unreliable
- ask for a cleaner source if the weakness affects core review quality

If only snippets are provided:

- Limit the scope to those snippets.
- State clearly that the contract has not been reviewed end to end.
- Still run intake, priority weighting, failure checks, and QA on the available material.
