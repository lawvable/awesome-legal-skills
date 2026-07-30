# Test Plan

Run this QA plan before sending the final answer. The review fails if any blocker check fails.

## Blocker Checks

All of the following must pass:

- Intake minimums satisfied
- Review mode identified
- Document map completed
- All available exhibits and incorporated materials accounted for
- Top priority clause families reviewed
- Clause citations included for material findings
- Playbook comparison or fallback basis stated for each major issue
- Returned changes scored against the playbook with impact band, color label, and confidence
- Ancillary-document checks completed for SLA, security schedule or measures, AI terms, and required regulatory addenda
- Redlines do not break defined terms or cross-references
- Required approvals routed to the right functions
- Missing documents and assumptions disclosed
- Final answer follows the output format

## Accuracy Checks

Verify:

- Party names are correct and consistent
- Defined terms are used exactly as written
- Liability caps, carveouts, fees, dates, and notice periods are copied accurately
- Order of precedence is respected
- Comparison against playbook does not invert the user's position
- Deviation score and seriousness signal match the actual clause movement
- BAA, DORA, and financial-cloud schedule triggers are identified correctly when the intake facts require them

## Completeness Checks

Confirm review coverage for the clause families relevant to the contract type:

- Structure and parties
- Commercial scope
- Financial terms
- Data and security
- IP and license
- Warranty, support, SLA
- Indemnity and liability
- Term and termination
- Compliance and insurance
- Boilerplate
- Attachments
- Playbook delta scoring for returned drafts
- Clause-network parsing, definitions, and cross-reference handling

## Adversarial Scenarios

Use these as prompts for self-checking whether common misses are present:

- Hidden auto-renewal with short opt-out window
- Liability cap that looks fee-based but is expanded by carveouts
- DPA or security schedule conflicts with main agreement
- Data-use clause that permits model training or broad service improvement
- Acceptance criteria moved into a statement of work instead of the main agreement
- A cap or indemnity that changes between the main agreement and order form
- Assignment restriction triggered by change of control
- Audit rights or benchmarking rights buried in an exhibit
- Customer paper that quietly requires the vendor to comply with future unilateral policy changes
- Vendor paper that disclaims all warranties while promising implementation outcomes elsewhere

## QA Verdict

Summarize QA at the end of the work product using:

```text
QA Verdict:
- Blockers: pass/fail
- Accuracy: pass/fail
- Completeness: pass/fail
- Remaining caveats: ...
```

If any category fails, revise the review before responding.
