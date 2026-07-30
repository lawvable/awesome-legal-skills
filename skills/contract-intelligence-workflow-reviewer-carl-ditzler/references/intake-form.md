# Intake Form

Complete this form before reviewing the contract. Do not skip fields that can materially change the review.

If the user has not yet shared the contract, stop and request it. Ask the user to upload the file or share a link such as Dropbox, Google Drive, OneDrive, SharePoint, Box, or another accessible cloud drive.

## Document Request

Ask for these items up front:

- Contract to review
- Clean version, redline version, or both
- All exhibits, schedules, appendices, order forms, statements of work, policies, and URLs incorporated by reference
- Company playbook, clause library, fallback positions, or standard paper
- Comparable prior agreement or previously negotiated form
- Related DPA, security addendum, security measures, support policy, SLA, AI terms or AI addendum, order form, pricing sheet, or insurance requirements
- Relevant email guidance, ticket notes, or business instructions

## Required Questions

Ask and normalize answers to these questions:

1. What contract should be reviewed, and what document version controls the deal today?
2. Who is the user requesting the review, and what is their role or function?
3. Which party do you represent?
4. Is this first-party paper or third-party paper?
5. What type of contract is this?
6. What is the business objective or deal goal?
7. What are the commercial facts: contract value, payment model, term, renewal, termination timing, exclusivity, and key deliverables?
8. Which business region is the contract being performed in: AMER, APAC, EMEA, or multi-region?
9. Does the contract involve personal data, security commitments, AI use, confidential information, regulated data, or cross-border transfers?
10. Which jurisdictions matter for governing law, venue, data transfers, or compliance?
10A. Does the deal have an EU or EEA nexus through parties, customers, regulated operations, services, hosting, or in-scope affiliates?
11. If the represented party is the customer, what sector or industry is the customer in?
12. What industry is the other party in?
13. Is the service or offering a cloud product or cloud-enabled service?
14. If the customer is a U.S.-based healthcare provider or healthcare services organization, is PHI transmitted, processed, or stored?
15. What is the timeline for signature and which issues are true blockers?
16. What is the user's risk tolerance: aggressive, balanced, or close-the-deal?
17. Are there internal stakeholders who must review or approve? Examples: finance, security, privacy, procurement, product, sales, insurance, compliance, executive sponsor. If known, provide the specific approver names and contact paths, or confirm that the saved default approver map should be used.
18. Are there must-have positions, prohibited terms, or prior negotiated compromises that should govern this review?

## Read-First Rule

If the user has already shared the contract for review, read the contract before asking avoidable intake questions.

When possible, infer these answers from the contract itself first:

- Question 1: what contract is being reviewed and which version appears to control
- Question 5: what type of contract it is

If either answer is unclear after reading the contract, ask the user a short targeted follow-up question instead of guessing.

## Intake Normalization Schema

Record the answers in a structured block using this schema:

```yaml
intake:
  document_set:
    contract: ""
    version_status: "clean|redline|both|unknown"
    exhibits_received: []
    referenced_external_docs: []
    comparison_docs: []
  user:
    user_identity: ""
    represented_party: ""
    user_role: ""
    internal_business_owner: ""
    counterparty: ""
    paper_owner: "first_party|third_party|mixed|unknown"
  contract_profile:
    contract_type: ""
    subtype: ""
    business_region: "AMER|APAC|EMEA|multi|unknown"
    jurisdictions: []
    term: ""
    renewal_model: ""
    signature_deadline: ""
    customer_industry: ""
    other_party_industry: ""
    cloud_service: "yes|no|mixed|unknown"
  commercial_context:
    deal_value: ""
    pricing_model: ""
    deliverables_or_scope: ""
    critical_deadlines: []
    business_goal: ""
  data_and_regulatory:
    personal_data: "yes|no|unknown"
    security_sensitive: "yes|no|unknown"
    ai_or_model_use: "yes|no|unknown"
    regulated_industry: []
    cross_border_data: "yes|no|unknown"
    eu_or_eea_nexus: "yes|no|unknown"
    us_healthcare_customer: "yes|no|unknown"
    phi_in_scope: "yes|no|unknown"
    baa_required: "yes|no|unknown"
    emea_financial_cloud_addendum_required: "yes|no|unknown"
    dora_review_required: "yes|no|unknown"
  negotiation_posture:
    risk_tolerance: "aggressive|balanced|close-the-deal|unknown"
    must_have_terms: []
    prohibited_terms: []
    priority_concerns: []
  approval_map:
    finance: "required|optional|no"
    security: "required|optional|no"
    privacy: "required|optional|no"
    procurement: "required|optional|no"
    product: "required|optional|no"
    compliance: "required|optional|no"
    insurance: "required|optional|no"
    exec: "required|optional|no"
    named_approvers: []
  constraints_and_gaps:
    missing_documents: []
    unanswered_questions: []
    assumptions_allowed: []
```

## Automatic Regulatory And Ancillary-Document Checks

Set these rules explicitly:

- If the customer is a U.S.-based healthcare provider or healthcare services organization and PHI is transmitted, processed, or stored, then a BAA is required.
- If the deal has an EU or EEA nexus, run a DORA applicability screen. If the deal involves ICT or cloud services for an EU or EEA financial-sector or insurance customer, or otherwise appears to support a regulated financial entity's critical or important functions, then perform a DORA review and check for DORA-aligned contractual provisions.
- If the customer is in EMEA, the customer industry is insurance or financial services, Europe is the place of business, and the offering is a cloud service, then an enhanced financial-cloud contractual schedule or addendum with audit, security, and exit provisions is required.
- Always check whether an SLA, security measures or security schedule, and AI terms are included or incorporated.

## Intake Minimums

Do not issue a final full review unless these minimums are known:

- Contract text or a reliable file
- Represented party
- User role or equivalent function
- Contract type

If one of those minimums is missing, ask for it before analyzing.

## Fallback Rules

If a non-critical field is missing:

- Ask the question.
- If the user cannot answer, proceed with the least aggressive assumption.
- Label the assumption clearly.
- Reflect the uncertainty in risk scoring, recommendations, and approval routing.

If a critical comparison document is missing:

- Proceed in fallback review mode.
- Identify which findings may change once the missing document is supplied.

## Intake Completion Check

Before moving to playbook normalization, confirm:

- The controlling agreement version is identified.
- Missing materials are listed.
- The user's role and represented party are explicit.
- The review mode is selected.
- The approval map either names contract-specific approvers or confirms that saved defaults apply.
