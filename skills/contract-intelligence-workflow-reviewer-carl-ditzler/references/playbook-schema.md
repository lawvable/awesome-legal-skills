# Playbook Schema

Normalize every source of guidance into a single clause-based playbook before doing the final review.

If the playbook was uploaded or fetched from a cloud source, normalize from the saved `source.md` extraction and preserve a link back to the source metadata.

Guidance sources can include:

- Formal legal playbooks
- Standard contract templates
- Prior negotiated agreements
- Approved fallback clause banks
- Email instructions from counsel or business teams
- Procurement requirements
- DPA or security positions

## Normalization Rules

- Merge all guidance into one canonical playbook table.
- If two sources conflict, note the conflict and identify which source controls.
- If there is no formal playbook, create a provisional playbook from the user's explicit goals plus the fallback best-practice standards.
- Separate legal requirements, business preferences, and pure drafting preferences.
- Do not invent internal positions that were not provided. When in doubt, mark the clause as requiring confirmation.

## Clause Record Schema

Create one record per clause family using this schema:

```yaml
playbook_clause:
  clause_family: ""
  clause_variants: []
  priority_level: "critical|high|medium|low"
  business_owner: ""
  legal_owner: ""
  preferred_position: ""
  acceptable_fallback: ""
  last_resort_position: ""
  prohibited_terms: []
  rationale:
    legal: ""
    commercial: ""
    operational: ""
  approval_trigger: []
  specialist_review_trigger: []
  negotiation_notes: []
  sample_redline: ""
  counterparty_explanation: ""
  jurisdiction_notes: []
  dependencies: []
  comparison_basis: "playbook|template|prior_deal|fallback_best_practice"
```

## Mandatory Clause Families

Cover these clause families when applicable:

- Parties, affiliates, definitions, and order of precedence
- Scope, services, deliverables, acceptance, change orders
- Fees, payment terms, taxes, credits, expense controls
- Term, renewal, suspension, termination, transition
- Confidentiality, residuals, publicity, use of names
- Data use, DPA, security, incident notice, subprocessors, AI or model training, data location
- IP ownership, license grants, feedback, custom work product, open source
- Representations, warranties, disclaimers, SLAs, support, service levels
- Indemnities and defense control
- Limitation of liability and damage carveouts
- Insurance
- Audit rights, records, benchmarking, MFN, most-favored pricing
- Compliance, sanctions, anti-bribery, accessibility, industry-specific requirements
- Assignment, change of control, subcontracting
- Governing law, venue, dispute resolution, injunctive relief
- Entire agreement, amendment, waiver, notices, force majeure

## Comparison Output

For each clause family, classify the contract against the playbook using one of:

- `aligned`
- `acceptable fallback`
- `needs revision`
- `deal blocker`
- `missing from contract`
- `missing from playbook`

When the contract is a returned draft or counterparty markup, also run the deviation scoring workflow and map the result into the stricter operational status values from the playbook deviation scoring reference.

## Escalation Logic

A clause needs escalation if any of the following is true:

- The contract exceeds the playbook's last acceptable fallback.
- The clause affects a department outside legal.
- The guidance sources conflict.
- The reviewer lacks enough context to assess the clause reliably.
- The clause is missing and the absence creates material risk.

## Provisional Playbook

If no playbook exists, create a provisional playbook using:

1. User's must-have terms
2. User's prohibited terms
3. Role- and contract-type priorities from the priority matrix
4. Best-practice guidance from the legal review best-practices reference

Mark the resulting playbook as provisional and lower confidence accordingly.
