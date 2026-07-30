# YC SaaS Drafter — Intake Questions

Ask in order. Apply branching as noted. Collect all answers into a config before proceeding to document assembly.

---

## Q1: Company & Customer Basics

Ask as a single group:

> "Let's set up the deal. I need:
> 1. Your company's full legal name (e.g., 'Acme, Inc.')
> 2. State of incorporation (e.g., Delaware)
> 3. Where is the company's principal place of business? (city, state — this
>    drives the governing law default)
> 4. The customer's full legal name
> 5. Effective date for the agreement (or say TBD if you don't have one)"

- `company_name`: full legal entity name
- `state_of_incorporation`: e.g., "Delaware"
- `principal_place_of_business`: e.g., "San Francisco, California" — state portion drives governing law default
- `customer_name`: full legal entity name
- `effective_date`: date or `[TBD — Effective Date]`

---

## Q2: Product Description

> "Describe your product in one or two sentences — this goes in the Order Form
> to define what the customer is buying. Keep it broad, factual, and concise.
> Don't overpromise."
>
> **Example:** "Moveworks develops and makes available a SaaS-based AI product
> that uses machine learning, conversational AI, and process automation to
> resolve IT issues."
>
> **Example:** "Acme provides a cloud-based project management platform that
> enables teams to plan, track, and collaborate on work."

→ `product_description`: 1-2 sentences

The Services field in the Order Form will read:
`[product_description] (the "Service(s)").`

---

## Q3: Fee Structure

> "What's the pricing structure for this deal? Pick the closest match:"
>
> **A) Flat monthly/annual** — Single fixed fee for platform access, regardless
>    of usage or team size. (e.g., "$5,000 per month")
>
> **B) Per-seat / per-user** — Monthly fee multiplied by the number of licensed
>    users. (e.g., "$50 per user per month, 100 users")
>
> **C) Usage-based / consumption** — Charges tied to a measurable metric like
>    API calls, GB stored, or transactions processed. (e.g., "$0.01 per API
>    call, estimated 500,000 calls/month")
>
> **D) Monthly minimum + overage** — Committed baseline monthly fee, plus
>    additional charges if usage exceeds allocation. (e.g., "$3,000/month
>    includes 10,000 units; $0.50 per additional unit")
>
> **E) Prepaid capacity (annual true-up)** — Customer prepays for an annual
>    usage allocation; usage reconciled at year-end. (e.g., "$60,000/year
>    covers 100,000 units")
>
> **F) Tiered pricing** — Fixed fee per tier with included capacity. Moving
>    between tiers changes the monthly cost. (e.g., "Professional tier at
>    $2,000/month, includes 50 users and 100GB")
>
> **G) Hybrid (base + usage)** — Flat platform fee plus variable consumption
>    charges. (e.g., "$1,000/month platform fee + $0.05 per transaction")
>
> **H) Performance/outcome-based** — Fee tied to customer results. (e.g.,
>    "5% of attributed revenue, minimum $2,000/month")

→ `fee_type`: "flat" | "per_seat" | "usage" | "minimum_plus_overage" | "prepaid_capacity" | "tiered" | "hybrid" | "performance"

Then ask for the specific amounts based on the selected type:

> "What are the specific numbers? (fee amount, unit price, seat count,
> minimums, overages — whatever applies to your structure)"

→ `fee_details`: free text describing the specifics

**Branching — Service Capacity:**
- If fee type is per_seat, usage, minimum_plus_overage, prepaid_capacity, tiered, or hybrid → ask:
  > "What's the included capacity or usage limit? And what happens when the
  > customer exceeds it — overage charges, automatic tier upgrade, or service
  > throttling?"
  → `service_capacity`: description of limits
  → `overage_terms`: description of what happens on excess
- If fee type is flat or performance → Service Capacity section is removed from Order Form.

---

## Q4: Initial Term

> "Initial service term? Default is one year."
>
> Options: One year (default) | Two years | Three years | Other: ___

→ `initial_term`: "One" | "Two" | "Three" | custom text

---

## Q5: Implementation Services

> "Will you provide implementation services as part of this deal —
> onboarding, setup, training, custom development, data migration?"
>
> - **Yes** → "What's the one-time implementation fee?"
> - **No** → skip

→ `implementation_services`: true | false
→ `implementation_fee`: dollar amount or `[TBD — Implementation Fee]`

**If YES — flag for lawyer:** Implementation services create IP ownership
questions. When a vendor builds custom work for a customer, who owns it?
This is a complicated negotiation point, similar to DPA. The skill flags
it in the memo: "Implementation services included. Discuss IP ownership of
custom deliverables with counsel before sending."

---

## Q6: Pilot Period

> "Is there a free trial or pilot period before the paid term starts?"
>
> - **Yes** → "How long is the pilot, and is there a fee?"
> - **No** → skip

→ `pilot`: true | false
→ `pilot_duration`: e.g., "Sixty (60) days"
→ `pilot_fee`: dollar amount, "$0" for free, or `[TBD — Pilot Fee]`

---

## Q7: Distributed Software

> "Is your product purely browser-based / cloud-hosted SaaS, or does it
> include software that gets installed on the customer's devices or
> on-premises servers?"
>
> - **Cloud-only** (no software installed on customer side)
> - **Includes distributed software** (desktop app, on-premises agent,
>   mobile SDK, browser extension with local components, etc.)

→ `distributed_software`: true | false

This drives whether the on-premises software license sentence in Section 2.1
stays or gets removed.

---

## Q8: Derivative Data Ownership

> "When your product processes the customer's data, does it produce derived
> outputs that get delivered back to the customer? If so, should the customer
> own those outputs?"
>
> **Examples of derivative data the customer might own:**
> - Reports, dashboards, or analytics generated from their data
> - AI/LLM outputs (generated text, images, summaries) based on their inputs
> - Transformed or enriched datasets delivered back to them
>
> **Examples where the company typically retains derivative data:**
> - Anonymized training data used to improve ML models
> - Aggregate benchmarks (e.g., "your usage is in the top 10% of customers")
> - Internal product telemetry and performance metrics
>
> - **Customer owns derivatives** → agreement grants ownership of raw data
>   AND derived outputs
> - **Company retains derivatives** → customer owns raw data only; company
>   retains rights to aggregate and derived data

→ `customer_owns_derivatives`: true | false

**If false → flag for lawyer:** Derivative data ownership is frequently
negotiated. The memo will note: "Customer does not own derivative data per
current draft. Discuss with counsel — counterparty may push to own all
outputs generated from their data."

---

## Q9: ML & Data Usage

> "Section 3.3 of the agreement grants your company the right to collect and
> analyze data relating to the use and performance of the service, and to use
> that data to improve the service and disclose it in aggregate form. This is
> standard SaaS language and is always included."
>
> "Does your company also train machine learning models on customer content
> — not just usage metrics, but the actual documents, images, text, or other
> content customers put into the product?"
>
> - **No** — Standard analytics only. Section 3.3 as-is is sufficient.
> - **Yes** — ML models learn from customer content to improve accuracy.

→ `ml_trains_on_content`: true | false

**If yes → flag for lawyer:** ML training on customer content is a core
business decision with significant legal implications. The memo will flag:
"Company trains ML models on customer content. Attorney must review Section
3.3 data rights language to confirm it matches actual data practices and
will withstand customer scrutiny."

---

## Q10: Data Retention on Termination

> "When the agreement ends, how long do you retain the customer's data before
> deleting it? The agreement will commit to making data available for
> retrieval and then deleting it after a specified period."
>
> - **30 days** (standard — customer has 30 days to retrieve, then deleted)
> - **60 days**
> - **90 days**
> - **Other:** ___

→ `data_retention_days`: 30 | 60 | 90 | custom number

**Flag for lawyer:** The specific retention and deletion timeline should be
reviewed by counsel to ensure it aligns with the company's actual data
infrastructure and any regulatory requirements.

---

## Q11: Auto-Renewal & Notice Period

> "The YC default is auto-renewal — the agreement automatically renews for
> additional terms of the same length unless either party gives notice.
> What notice period?"
>
> - **30 days** (YC default)
> - **60 days** (common for larger deals)
> - **90 days** (enterprise standard)
> - **No auto-renewal** — agreement ends at term, renewed only by mutual
>   written agreement

→ `auto_renewal`: true | false
→ `renewal_notice_days`: 30 | 60 | 90

---

## Q12: Governing Law

> "Governing law defaults to the state where your company's principal place
> of business is — [state from Q1]. Want to keep that or change it?"

→ `governing_law`: defaults to state extracted from `principal_place_of_business`

---

## Q13: Marketing Formulation

> "The agreement includes this default marketing language:"
>
> *'Customer agrees that Company may refer to Customer's name and trademarks
> in Company's marketing materials and website; however, Company will not use
> Customer's name or trademarks in any other publicity (eg, press releases,
> customer references, and case studies) without Customer's prior written
> consent (which may be by email).'*
>
> "Is this sufficient for this deal, or do you need to adjust it?"
>
> - **Sufficient** — keep as-is
> - **Need more** — want press release rights or reference account commitment
> - **Need less** — customer is sensitive, want to remove or restrict further

→ `marketing_formulation`: "default" | "more" | "less"

If "more" or "less", ask what specifically they want. Flag in memo for
attorney review if adjusted.

---

## Q14: SLA Availability Commitment

> "What uptime commitment are you making in the SLA?"
>
> - **99.9%** — ~8.7 hours downtime per year. Standard for most SaaS.
> - **99.95%** — ~4.4 hours per year. For mission-critical applications.
> - **99.99%** — ~52 minutes per year. Infrastructure-grade. Only commit
>   to this if your engineering team confirms the architecture supports it.

→ `availability_tier`: "99.9" | "99.95" | "99.99"

**Default:** 99.9%

---

## Q15: Support Details

Ask as a group:

> "For the support section of the SLA, I need:"
>
> 1. Support email address (e.g., support@company.com)
> 2. Support phone number (or TBD)
> 3. Support hours (default: 9am-5pm Pacific, weekdays)
> 4. Do you use a shared communication channel with customers?
>    (e.g., shared Slack channel, Microsoft Teams) — if so, what platform?

→ `support_email`: email address or `[TBD — Support Email]`
→ `support_phone`: phone number or `[TBD — Support Phone]`
→ `support_hours`: default "9:00 am Pacific Time through 5:00 pm Pacific Time on weekdays"
→ `communication_tool`: e.g., "Slack" | "Microsoft Teams" | "none"

---

## Summary Confirmation

Before producing the document, present all decisions:

> "Here's what I'll draft:
>
> **Parties:** [Company] → [Customer]
> **Service:** [product description]
> **Fees:** [fee type] — [fee details]
> **Initial term:** [term]
> **Implementation:** [included at $X / not included]
> **Pilot:** [included, X days at $X / not included]
> **Distributed software:** [yes — license included / no — cloud only]
> **Derivative data:** [customer owns / company retains]
> **ML training on content:** [yes — flagged for lawyer / no]
> **Data retention:** [X days] after termination
> **Auto-renewal:** [yes, X-day notice / no]
> **Governing law:** [state]
> **Marketing:** [default / adjusted]
> **SLA:** [X]% uptime
> **Support:** [email], [phone], [hours], [tool]
>
> **Always applied to every draft:**
> - Renamed to 'Customer Agreement' throughout
> - 'United States' removed from IP indemnity patent scope
> - Customer indemnity clause (§2.3) removed
> - Data privacy & security section (§2.5) added
> - Warranty remedy, customer warranty, and beta disclaimer added (§6)
> - New marketing language replaces YC press release clause
> - Consolidated SLA + Support as Exhibit B (no separate Exhibit C)
> - All YC drafting annotations and notes stripped
>
> **Flagged for your lawyer:**
> - [DPA — almost certainly needed, raise with counsel]
> - [Implementation IP — if applicable]
> - [Derivative data — if company retains]
> - [ML training — if trains on content]
> - [Data retention timeline — confirm with counsel]
>
> Does that look right, or do you want to change anything?"

Wait for confirmation before proceeding to document assembly.
