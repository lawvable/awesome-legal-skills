# YC SaaS Drafter — Supplementary Language

Pre-written clause text for the YC Form SaaS Agreement. Each block has an
anchor ID referenced by the decision matrix. Insert the specified language
at the indicated location — do not paraphrase or rewrite these clauses.

Blocks are organized into two categories:
- **Always-apply** — inserted into every draft regardless of intake
- **Conditional** — inserted only when the decision matrix calls for it

---

## ALWAYS-APPLY BLOCKS

### #DATA-PRIVACY — Section 2.5: Data Privacy & Security

**Insert as:** New Section 2.5, after existing Section 2.4.

> (a) Company will maintain a security program materially in accordance with
> industry standards that is designed to (i) ensure the security and integrity
> of Customer Data (defined below), (ii) protect against threats or hazards to
> the security or integrity of Customer Data; and (iii) prevent unauthorized
> access to Customer Data. In furtherance of the foregoing, Company will
> maintain the administrative, physical and technical safeguards to protect
> the security of Customer Data that are described in the applicable
> documentation. Company's security safeguards include measures for preventing
> access, use, modification or disclosure of Customer Data by Company
> personnel except (a) to provide the Product and prevent or address service
> or technical problems, (b) as required by applicable law, or (c) as
> Customer expressly permits in writing or under this Agreement. Company will
> not materially diminish the protections provided in this Section during the
> term of this Agreement. To the extent that Company processes any Personal
> Data (as defined in the DPA referenced below) contained in Customer Data
> that is subject to the GDPR (as defined in the DPA), on Customer's behalf,
> in the provision of the Product, the parties will execute a Data Processing
> Addendum ("DPA"), and attach such DPA to this Agreement.

---

### #WARRANTY-REMEDY — Section 6.1: Exclusive Warranty Remedy

**Insert:** At the end of Section 6.1 (the company warranty), immediately
after "professional and workmanlike manner" and BEFORE the "EXCEPT AS
EXPRESSLY SET FORTH..." disclaimer paragraph.

> For material breach of the foregoing express warranty, Customer's exclusive
> right remedy shall be the re-performance of the deficient product or, if
> Company cannot re-perform such deficient product as warranted, Customer
> shall be entitled to terminate the applicable Order Form and recover a pro
> rata portion of the fees paid to Company for such deficient product.

---

### #CUSTOMER-WARRANTY — Section 6.2: Customer Warranty

**Insert as:** New Section 6.2, after the company warranty and disclaimer.

> Customer warrants that it has all rights necessary to provide any
> information, data, or other materials that it provides hereunder and to
> permit Company to use the same as contemplated hereunder.

---

### #BETA-DISCLAIMER — Section 6.3: Beta Products Disclaimer

**Insert as:** New Section 6.3, after the customer warranty. ALL CAPS.

> FROM TIME TO TIME, CUSTOMER MAY HAVE THE OPTION TO PARTICIPATE IN A
> PROGRAM WITH COMPANY WHERE CUSTOMER GETS TO USE ALPHA OR BETA PRODUCTS,
> FEATURES, OR DOCUMENTATION (COLLECTIVELY, "BETA PRODUCTS") OFFERED BY
> COMPANY. THE BETA PRODUCTS ARE NOT GENERALLY AVAILABLE AND ARE PROVIDED
> "AS IS". COMPANY DOES NOT PROVIDE ANY INDEMNITIES, SERVICE LEVEL
> COMMITMENTS, OR WARRANTIES, EXPRESSED OR IMPLIED, INCLUDING WARRANTIES OF
> MERCHANTABILITY, TITLE, NON-INFRINGEMENT, AND FITNESS FOR A PARTICULAR
> PURPOSE, IN RELATION THERETO. CUSTOMER OR COMPANY MAY TERMINATE CUSTOMER'S
> ACCESS TO THE BETA PRODUCTS AT ANY TIME.

---

### #MARKETING-DEFAULT — Section 9: Marketing Language

**Replace:** The YC bracketed press release / reference account language
near the end of Section 9 (starting with "The parties shall work together
in good faith to issue at least one mutually agreed upon press release...").

> Customer agrees that Company may refer to Customer's name and trademarks
> in Company's marketing materials and website; however, Company will not
> use Customer's name or trademarks in any other publicity (eg, press
> releases, customer references, and case studies) without Customer's prior
> written consent (which may be by email).

---

### #EXHIBIT-B-CONSOLIDATED — Exhibit B: Service Level and Support Terms

**Replace:** Both Exhibit B (Service Level Terms) and Exhibit C (Support
Terms) from the YC template with this single consolidated exhibit. Remove
all references to "Exhibit C" throughout the document. Section 1.2 should
reference "Exhibit B" for support terms.

Variable placeholders shown in `[brackets]` — substitute from intake values.

> **EXHIBIT B**
>
> **Service Level and Support Terms**
>
> **Service Level Agreement**
>
> **Availability Commitment.**
> The Product will be Available [99.9]% of the time, measured on a calendar
> monthly basis (the "Availability Commitment"). "Availability" means that
> the Product is available to Customer's employees or other personnel.
> Availability measures will not include downtime resulting from:
>
> - Upgrades: Customer will receive prior notice by email of Company's
>   upgrade windows, which will be scheduled between 5pm and midnight Pacific
>   Time to the extent feasible. Downtime due to upgrades will not exceed 2
>   hours per month.
>
> - Pre-scheduled maintenance periods: Customer will receive at least 24
>   hours prior notification by email of pre-scheduled maintenance periods.
>   Maintenance shall be scheduled between 5pm and midnight Pacific Time.
>   Downtime due to pre-scheduled maintenance will not exceed 2 hours per
>   month.
>
> - Emergency maintenance periods: Customer will receive prior notification
>   by email on a commercially reasonable efforts basis. These maintenance
>   periods will involve applying critical security patches and other
>   emergency repairs to Company's infrastructure.
>
> The Availability Commitment does not apply to any downtime resulting from:
>
> - Account suspension or termination due to Customer's breach of the
>   Agreement;
> - Disengagement of functionality of the Product due to Customer's request;
> - Force Majeure Events; or
> - Customer's or its third-party service provider's equipment, software or
>   other technology.
>
> Company will provide Customer with reports on Availability upon request.
>
> **Credit.**
> If Company fails to achieve the above Availability for the Product,
> Customer may claim a credit based on a monthly pro-rated amount of the
> annual subscription fee, as provided below.
>
> [INSERT TABLE — Credit Schedule]
>
> | Percentage Availability Per Month | Credit |
> |---|---|
> | [99.9] - 100.0% | 0% |
> | 99.0 - [99.89]% | 5% |
> | 97.0 - 98.99% | 10% |
> | 94.0 - 96.99% | 20% |
> | Below 94.0% | 50% |
>
> **Table formatting note:** This MUST be rendered as a proper table in the
> .docx output — not inline text. The credit thresholds in the first row
> align with the Availability Commitment (e.g., if commitment is 99.95%,
> the 0% credit row becomes "99.95 - 100.0%" and the 5% row starts at
> "99.0 - 99.94%").
>
> Customer will not be entitled to a credit if it is in breach of its
> Agreement with Company, including payment obligations. To receive a credit,
> Customer must file a claim within five (5) days following the end of the
> month in which the Availability Commitment was not met by contacting
> Company at [support@company.com] with a complete description of the
> downtime, how Customer was adversely affected, and for how long.
>
> The credit remedy set forth in this Service Level Agreement is Customer's
> sole and exclusive remedy for the unavailability of the Product.
>
> **Customer Support**
>
> Company live technical support business hours will start at [9:00 am
> Pacific Time] and run until [5:00 pm Pacific Time] on weekdays. Technical
> support can be contacted via email at [support@company.com] or via shared
> channels in the customer communication platform.
>
> **Communication Channels:**
>
> [INSERT TABLE — Communication Channels]
>
> | EMAIL | PHONE | COMMUNICATION TOOL |
> |---|---|---|
> | [support@company.com] | [phone number] | [Shared Company channel] |
>
> **Table formatting note:** Render as a proper table in the .docx output.
> If `communication_tool` is "none", remove the COMMUNICATION TOOL column.
>
> Live technical support will not be available on Christmas Day (December 25)
> and New Year's Day (January 1). The current Company holidays are set forth
> below:
>
> - Presidents Day (third Monday of February)
> - Memorial Day (last Monday of May)
> - Independence Day (July 4)
> - Labor Day (first Monday of September)
> - Thanksgiving Day (fourth Thursday in November)
> - Christmas Eve (December 24)
> - New Year's Eve (December 31)

**Variable substitutions in Exhibit B:**

| Placeholder | Intake Field | Default |
|---|---|---|
| `[99.9]` (availability %) | `availability_tier` | 99.9 |
| `[99.89]` (credit threshold) | derived: availability_tier minus 0.01 | 99.89 |
| `[support@company.com]` (2 occurrences) | `support_email` | [TBD — Support Email] |
| `[phone number]` | `support_phone` | [TBD — Support Phone] |
| `[Shared Company channel]` | `communication_tool` | Remove column if "none" |
| `[9:00 am Pacific Time]` | `support_hours` (start) | 9:00 am Pacific Time |
| `[5:00 pm Pacific Time]` | `support_hours` (end) | 5:00 pm Pacific Time |

---

## CONDITIONAL BLOCKS

### #NO-AUTO-RENEWAL — Section 5.1 Replacement

**When to use:** `auto_renewal: false`
**Replace:** Section 5.1 entirely.

> Subject to earlier termination as provided below, this Agreement is for the
> Initial Service Term as specified in the Order Form (the "Term"). This
> Agreement may be renewed for additional periods upon mutual written
> agreement of the parties executed at least thirty (30) days prior to the
> end of the then-current Term.

---

### #FEE-EXAMPLES — Order Form Service Fees Patterns

**When to use:** Always reference when composing the Order Form Service Fees
line. The LLM selects the pattern matching `fee_type` and adapts it using
`fee_details` from intake.

Unlike other supplementary language blocks, these are EXAMPLES — the LLM
adapts the pattern to match the specific deal terms. This is the one section
where composed (not verbatim) language is appropriate because fee structures
are factual and commercial, not legal terms.

**Flat Monthly/Annual:**
> Services Fees: $[amount] per [month/year], payable [in advance/monthly],
> subject to the terms of Section 4 herein.

**Per-Seat / Per-User:**
> Services Fees: $[amount] per user per month. Initial licensed users: [N].
> Monthly fee: $[total] (based on [N] users), payable in advance, subject to
> the terms of Section 4 herein.
>
> Service Capacity: [N] licensed users. Additional users may be added at
> $[amount] per user per month.

**Usage-Based / Consumption:**
> Services Fees: $[amount] per [unit]. Estimated monthly usage: [N] [units]
> (~$[total]/month). Actual charges billed [monthly] based on consumption,
> subject to the terms of Section 4 herein.
>
> Service Capacity: [N] [units] per [month]. Overages billed at $[amount]
> per [unit].

**Monthly Minimum + Overage:**
> Services Fees: $[minimum] per month (includes [N] [units]). Overages:
> $[amount] per additional [unit], billed monthly, subject to the terms of
> Section 4 herein.
>
> Service Capacity: [N] [units] per month included. Overages billed as
> described above.

**Prepaid Capacity (Annual True-Up):**
> Services Fees: $[amount] annual prepayment (covers [N] [units]). Annual
> true-up adjustment due within 30 days of contract anniversary, subject to
> the terms of Section 4 herein.
>
> Service Capacity: [N] [units] per year. Usage exceeding prepaid capacity
> billed at $[overage rate] per [unit] at annual true-up.

**Tiered Pricing:**
> Services Fees: [Tier name] tier at $[amount] per month, payable in advance,
> subject to the terms of Section 4 herein.
>
> Service Capacity: [Tier name] tier includes [N] users and [N] [units].
> Tier upgrades effective on next billing cycle.

**Hybrid (Base + Usage):**
> Services Fees: $[platform fee] per month (platform access) + $[amount] per
> [unit] of usage. Minimum monthly commitment: $[minimum], payable in
> advance, subject to the terms of Section 4 herein.
>
> Service Capacity: Platform access is unlimited. Usage measured in [units].
> Overages above [N] [units] at $[amount] per [unit].

**Performance/Outcome-Based:**
> Services Fees: [X]% of [metric] (e.g., qualified leads, attributed revenue),
> payable monthly. Minimum monthly fee: $[minimum], subject to the terms of
> Section 4 herein.

---

### #EXPANDED-DATA-RESTRICTIONS — Sensitive Data Protections

**When to use:** Optional — when the company handles highly regulated data
(HIPAA, financial, SSNs) and the intake reveals a need for explicit
restrictions beyond the standard §2.5 data privacy language.
**Insert:** After Section 2.5, as additional subsection.

> Company shall not: (i) sell, rent, or lease Customer Data to any third
> party; (ii) use Customer Data for targeted advertising or marketing
> purposes; (iii) use Customer Data to build, improve, or market products
> or services that compete with the services Customer provides to its own
> customers; or (iv) disclose Customer Data to any third party except as
> necessary to provide the Services, as authorized by Customer in writing,
> or as required by applicable law. Company shall maintain administrative,
> technical, and physical safeguards designed to protect Customer Data
> against unauthorized access, disclosure, or use, consistent with industry
> standards for the type of data processed.

---

### #ML-TRAINING — ML Model Training Rights

**When to use:** `ml_trains_on_content: true` AND attorney has reviewed.
**Insert:** Append to Section 3.3 after the existing analytics language.

> Notwithstanding the foregoing, Company may use Customer Data, in anonymized
> and de-identified form, to train, improve, and develop Company's machine
> learning models and algorithms. Company shall implement reasonable technical
> and organizational measures to ensure Customer Data is anonymized prior to
> use for model training, such that individual Customer or its end users
> cannot be identified from the training data or resulting models. For
> clarity, Company shall not use identifiable Customer Data for model
> training, and any models trained using anonymized Customer Data shall be
> owned by Company.

---

### #ML-FEDERATED — Privacy-Preserving ML (Federated Learning)

**When to use:** When the company uses federated learning or differential
privacy techniques — model updates computed locally, raw data never leaves
customer environment.
**Insert:** Append to Section 3.3 after the existing analytics language.

> Notwithstanding the foregoing, Company may use privacy-preserving machine
> learning techniques (such as federated learning or differential privacy)
> whereby model updates are computed locally within Customer's environment
> and only aggregated model parameters — not Customer Data — are transmitted
> to Company's systems. No raw Customer Data shall leave Customer's
> environment in connection with such model improvement activities. Company
> shall provide reasonable documentation of the privacy-preserving techniques
> employed upon Customer's written request.

---

## Usage Notes

- **Always-apply blocks** are inserted into every draft. They are not
  optional and should not be skipped.
- **Conditional blocks** are inserted only when the decision matrix specifies.
  Reference the anchor ID (e.g., `#ML-TRAINING`) in the decision matrix.
- **#FEE-EXAMPLES** is the ONLY block where the LLM composes language based
  on patterns rather than inserting verbatim text.
- When supplementary language is added, note it in the lawyer memo under the
  appropriate section so the reviewing attorney knows what was inserted vs.
  what came from the YC standard template.
- Do NOT paraphrase, condense, or rewrite the always-apply or conditional
  blocks. Use them verbatim or not at all.
