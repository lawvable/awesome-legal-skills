# Priority Matrix

Use this matrix after intake and before clause review. The goal is to decide what matters most for this specific user, not for an abstract lawyer.

## Priority Model

Assign each clause family a working priority based on:

1. Contract type
2. Which side the user represents
3. User role or function
4. Deal context
5. Cross-functional impact

Use these working levels:

- `Critical`: likely blocker, mandatory redline or approval
- `High`: should be negotiated or approved with awareness
- `Medium`: improve if leverage permits
- `Low`: cosmetic or low-leverage item

## Global Always-Review Clauses

These clauses are always at least `High` unless clearly irrelevant:

- Parties and contract structure
- Scope and deliverables
- Fees and payment mechanics
- Term and termination
- Confidentiality and permitted use
- Data and security obligations
- IP ownership and license scope
- Warranties, disclaimers, and service levels
- Indemnity
- Limitation of liability
- Governing law and disputes
- Assignment and change of control
- Exhibits and incorporated documents

## NDA Matrix

### User Represents Discloser

| Clause Family | Priority | Notes |
|---|---|---|
| Definition of Confidential Information | Critical | Avoid narrow definitions and exclusions that gut protection. |
| Permitted Use | Critical | Limit use to stated purpose only. |
| Residuals | Critical | Usually resist residuals unless approved. |
| Disclosure Recipients | High | Limit to need-to-know and bind recipients. |
| Security Standard | High | Require reasonable safeguards if sensitive data is shared. |
| Return or Destruction | High | Needed if information lifecycle matters. |
| Compelled Disclosure | High | Require notice and cooperation where lawful. |
| Term of Confidentiality | Critical | Trade secrets and highly sensitive information may require longer survival. |
| Publicity / Use of Name | Medium | Important where branding risk exists. |
| Injunctive Relief | Medium | Helpful, not always decisive. |

### User Represents Recipient

| Clause Family | Priority | Notes |
|---|---|---|
| Definition of Confidential Information | Critical | Prevent overbroad coverage of trivial or already-known information. |
| Residuals | High | Important for product and engineering teams. |
| Permitted Use | High | Ensure internal evaluation or service delivery use is workable. |
| Return or Destruction | High | Preserve legal retention, backups, and compliance needs. |
| Term of Confidentiality | Critical | Avoid impractical perpetual obligations except for trade secrets. |
| Non-Solicit / Non-Compete | Critical | Usually outside NDA scope. |
| Data or AI Use Restrictions | High | Confirm whether model training, telemetry, or analytics are implicated. |

## SaaS MSA Matrix

### User Represents SaaS Provider Reviewing Customer Paper

| Clause Family | Priority | Notes |
|---|---|---|
| Scope / Order of Precedence | Critical | Prevent hidden obligations through exhibits or policies. |
| Fees / Payment / Offsets | Critical | Protect invoice timing, non-payment remedies, and no broad setoff. |
| Service Levels / Credits | High | Credits should be sole remedy unless approved otherwise. |
| Security Commitments | Critical | Route detailed controls to security. |
| DPA / Privacy / Data Transfers | Critical | Route to privacy if personal data is involved. |
| AI / Model Training / Usage Restrictions | High | Critical if product uses AI features or telemetry. |
| IP Ownership / Feedback | Critical | Preserve provider ownership of platform and derivatives. |
| Warranties | High | Resist open-ended performance promises or roadmap commitments. |
| Indemnity | Critical | Narrow provider indemnity; watch customer misuse carveouts. |
| Liability Cap / Carveouts | Critical | Protect fee-based caps and narrow carveouts. |
| Audit Rights | High | Avoid unlimited audits, technical penetration rights, or cost-shifting. |
| Insurance | Medium | Escalate if levels exceed policy reality. |
| Termination / Transition Assistance | High | Avoid perpetual post-termination obligations. |
| Benchmarking / MFN / Price Holds | Critical | Business and finance approval required. |

### User Represents Customer Buying SaaS on Vendor Paper

| Clause Family | Priority | Notes |
|---|---|---|
| Scope / Order Form Accuracy | Critical | Confirm product, services, and implementation commitments. |
| Security Commitments | Critical | Security review usually required. |
| DPA / Privacy / Data Use | Critical | Privacy review usually required. |
| Availability / SLA / Support | Critical | Tie obligations to business need. |
| Termination Rights / Refunds | High | Include exit rights for chronic breach and insolvency. |
| Data Return / Deletion / Portability | Critical | Often missed and highly material. |
| IP / License Scope | High | Ensure internal affiliates and contractors can use. |
| Indemnity | High | Require vendor IP and privacy or security indemnity if appropriate. |
| Liability Cap | Critical | Avoid caps that are too low relative to risk and spend. |
| Audit / Compliance Rights | High | Important in regulated environments. |
| Subprocessors / Subcontractors | High | Route to privacy and security as needed. |

## Vendor Services Agreement Matrix

### User Represents Customer Hiring a Service Provider

| Clause Family | Priority | Notes |
|---|---|---|
| Scope / Deliverables / Milestones | Critical | Define what must be delivered and when. |
| Acceptance | Critical | Include objective acceptance mechanics. |
| Change Orders | High | Prevent scope creep and unapproved spend. |
| Fees / Expenses | High | Control invoicing and expense reimbursement. |
| IP Ownership / Work Product | Critical | Ownership and license-back must be clear. |
| Personnel / Subcontracting | High | Restrict delegation where service quality matters. |
| Confidentiality / Data Security | High | Security and privacy may both need review. |
| Warranties / Re-performance | Critical | Make remedies meaningful. |
| Indemnity | High | IP, confidentiality, and bodily injury or property damage may matter. |
| Liability Cap | Critical | Confirm cap is aligned to project risk. |
| Termination / Transition | High | Preserve convenience exit if project risk is high. |

### User Represents Service Provider Reviewing Customer Paper

| Clause Family | Priority | Notes |
|---|---|---|
| Scope / Deliverables | Critical | Avoid vague outcome warranties disguised as scope. |
| Acceptance | High | Deemed acceptance may be important. |
| Change Orders | Critical | No extra work without signed change order. |
| IP Ownership | Critical | Protect provider tools, know-how, and pre-existing IP. |
| Fees / Payment | Critical | Guard against broad holdbacks, setoff, or pay-when-paid logic. |
| Indemnity | High | Narrow to provider fault and specific risk areas. |
| Liability Cap | Critical | Avoid uncapped exposure for commercial services. |
| Insurance | Medium | Escalate if requirements exceed actual coverage. |
| Staffing Commitments | Medium | Resist named-person immobility unless essential. |

## DPA / Privacy Overlay

Raise to `Critical` when personal data, cross-border transfers, regulated data, targeted advertising, model training, or customer data analytics are involved:

- Purpose limitation and processing instructions
- Controller or processor role allocation
- Subprocessor rights and notice
- International transfers
- Security measures
- Incident notice timing
- Retention and deletion
- Audit and certification rights
- Use of data for model training, service improvement, or de-identification

## Region And Sector Overlay

Raise to `Critical` and require explicit ancillary-document checks when:

- the customer is a U.S.-based healthcare provider or healthcare services organization and PHI is transmitted, processed, or stored
- the deal has an EU or EEA nexus and may involve ICT or cloud services to a financial-sector or insurance entity
- the customer is in EMEA, the customer is in insurance or financial services, Europe is the place of business, and the offering is a cloud service

When the first condition is true:

- raise BAA, HIPAA privacy and security, subcontractor controls, incident notice, and data-use restrictions to at least `Critical`

When the second condition is true:

- run a DORA applicability screen and, if triggered, raise DORA-relevant operational resilience, audit, subcontracting, exit, and incident-support provisions to at least `Critical`

When the third condition is true:

- raise audit rights, security controls, subcontractor oversight, data location, resilience, exit assistance, transition, and business continuity provisions to at least `Critical`

## Role Adjustment Overlay

Apply these role-based adjustments after choosing the contract-type matrix:

- `Commercial legal / counsel`: maintain base priorities across all core clauses.
- `Procurement`: raise fees, benchmarking, term flexibility, vendor commitments, and audit economics.
- `Sales / revenue owner`: raise speed-to-close items, use rights, implementation timing, and renewal blockers; do not lower core risk clauses without calling it out.
- `Privacy counsel`: raise all data clauses to at least `Critical`.
- `Security`: raise security schedules, incident notice, audit rights, encryption, and subcontractor controls to at least `Critical`.
- `Finance`: raise fees, taxes, credits, caps tied to fees, payment terms, revenue recognition issues, and refund mechanics.
- `Product / engineering`: raise scope, integrations, roadmap commitments, acceptance, change control, AI feature restrictions, and support obligations.

## Approval Routing Matrix

Route the clause for review or approval when these triggers appear:

| Trigger | Reviewer |
|---|---|
| Personal data, DPA, data transfers, retention, model training | Privacy |
| Security exhibit, audit, penetration tests, incident timing, BCP or DR | Security |
| Pricing commitments, credits, payment timing, taxes, broad offsets, MFN | Finance |
| Scope, integrations, custom work, roadmap, acceptance criteria | Product or Engineering |
| Insurance limits, unusual indemnities, uncapped risk | Insurance or Risk |
| Regulated obligations, public sector, sanctions, accessibility, anti-bribery | Compliance |
| Exclusivity, strategic restraints, unusual commercial concessions | Executive or business owner |
| U.S. healthcare customer with PHI in scope | Privacy, Security, Compliance |
| EU or EEA nexus with possible DORA implications | Security, Compliance, Legal, relevant business owner |
| EMEA financial or insurance customer using cloud services | Security, Compliance, Legal, relevant business owner |

## Final Priority Output

Before clause review, produce a short working summary:

- Review mode
- Top 5 critical clause families for this deal
- Required internal reviewers
- Any clause families intentionally deprioritized and why
