# YC SaaS Drafter — Decision Matrix

Maps intake answers and always-apply defaults to specific modifications of
the YC Form SaaS Agreement. Organized into four sections:

A. Always-Apply Defaults — applied to every draft
B. Conditional Decisions — driven by intake answers
C. Variable Substitutions — placeholder replacement
D. Raise with Lawyer — flagged in memo for attorney review

---

## A. Always-Apply Defaults

These 17 modifications are applied to every draft regardless of intake.

### A1. Order Form Title

- **YC text:** "SAAS SERVICES ORDER FORM"
- **Action:** Change to "ORDER FORM NUMBER ONE"

### A2. Agreement Name

- **YC text:** "SAAS SERVICES AGREEMENT" (title) and "This SaaS Services Agreement ('Agreement')" (preamble)
- **Action:** Change to "CUSTOMER AGREEMENT" (title) and "This Customer Agreement ('Agreement')" (preamble). Replace ALL occurrences of "SaaS Services Agreement" with "Customer Agreement" throughout the document.

### A3. Preamble Date

- **YC text:** "this _______ day of ________, 2015"
- **Action:** Update year to current year. Fill date fields from `effective_date` intake value or leave as `[TBD — Effective Date]`.

### A4. Section 1.1 — SLA Reference Always On

- **YC text:** "in accordance with the Service Level Terms attached hereto as Exhibit B. *[OPTIONAL]*"
- **Action:** Remove the `[OPTIONAL]` marker. Keep the SLA reference — Exhibit B is always attached.

### A5. Section 1.2 — Support References Exhibit B

- **YC text:** "in accordance with the terms set forth in Exhibit C. *[OPTIONAL:...]*"
- **Action:** Change "Exhibit C" to "Exhibit B" (consolidated exhibit). Remove the `[OPTIONAL:...]` note. Both SLA and support terms live in the single Exhibit B.

### A6. Section 2.2 — Export Controls Cleanup

- **YC text:** Contains export restriction language followed by `*[Note: export and government rights clauses are typically less important for pure hosted solutions...]*`
- **Action:** Keep all export control and FAR/DFAR language. Delete the bracketed note only.

### A7. Section 2.3 — Delete Customer Indemnity

- **YC text:** "[Customer hereby agrees to indemnify and hold harmless Company against any damages, losses, liabilities, settlements and expenses (including without limitation costs and attorneys' fees) in connection with any claim or action that arises from an alleged violation of the foregoing or otherwise from Customer's use of Services.]" followed by `*[Note: many larger customers resist these types of indemnity clauses...]*`
- **Action:** Delete the entire bracketed indemnity clause AND the bracketed note. This language is always struck in negotiation — removing it proactively avoids an unnecessary redline and projects sophistication.

### A8. Section 2.5 — Add Data Privacy & Security

- **YC text:** Section does not exist in the YC template.
- **Action:** Insert new Section 2.5 using verbatim text from supplementary-language.md `#DATA-PRIVACY`. This is essential — no modern SaaS agreement should lack data privacy provisions.

### A9. Section 3.3 — Data Analytics Always On

- **YC text:** Bracketed paragraph beginning "Notwithstanding anything to the contrary, Company shall have the right collect and analyze data..." with `*[Note: it is important to determine what data rights are necessary...]*`
- **Action:** Remove the brackets around the paragraph — this language is always included, not optional. Remove the `*[Note:...]*`. The analytics/data improvement rights are standard SaaS language.

### A10. Section 6.1 — Add Exclusive Warranty Remedy

- **YC text:** Section 6 ends the company warranty with "professional and workmanlike manner" then goes to the disclaimer.
- **Action:** Restructure Section 6 into subsections. Section 6.1 is the existing company warranty. After "professional and workmanlike manner", insert verbatim text from supplementary-language.md `#WARRANTY-REMEDY`. Then the existing "EXCEPT AS EXPRESSLY SET FORTH..." disclaimer follows.

### A11. Section 6.2 — Add Customer Warranty

- **YC text:** Does not exist.
- **Action:** Insert new Section 6.2 using verbatim text from supplementary-language.md `#CUSTOMER-WARRANTY`.

### A12. Section 6.3 — Add Beta Products Disclaimer

- **YC text:** Does not exist.
- **Action:** Insert new Section 6.3 using verbatim text from supplementary-language.md `#BETA-DISCLAIMER`. Must be in ALL CAPS.

### A13. Section 7 — Indemnity Always Included

- **YC text:** "*[OPTIONAL: many start-up companies choose not to offer indemnity as a starting point...]*"
- **Action:** Delete the optional note. Indemnity is always included — omitting it signals the company isn't confident in its IP.

### A14. Section 7 — Remove "United States" from Patent Scope

- **YC text:** "infringement by the Service of any United States patent or any copyright"
- **Action:** Change to "infringement by the Service of any patent or any copyright". Removing the geographic limitation is a standard redline that counterparties almost always request.

### A15. Section 8 — Strip Negotiation Note

- **YC text:** `*[Note: Liability limitations are frequently heavily negotiated in larger deals...]*`
- **Action:** Delete the note. Default liability language stays as-is.

### A16. Section 9 — Replace Marketing Language

- **YC text:** "[The parties shall work together in good faith to issue at least one mutually agreed upon press release within 90 days of the Effective Date, and Customer otherwise agrees to reasonably cooperate with Company to serve as a reference account upon request.]" and `*[OPTIONAL:...]*`
- **Action:** Replace the entire bracketed sentence AND the optional note with verbatim text from supplementary-language.md `#MARKETING-DEFAULT`. This is always-on, not optional.

### A17. Exhibits — Consolidate B + C, Remove Exhibit C

- **YC text:** Exhibit B (Service Level Terms) and Exhibit C (Support Terms) as separate exhibits.
- **Action:** Replace both with the single consolidated exhibit from supplementary-language.md `#EXHIBIT-B-CONSOLIDATED`. Delete all references to "Exhibit C" throughout the document. Exhibit A (SOW) remains conditional per B3 below.

### A18. Strip All Annotations

- **Action:** Remove every instance of `*[Note:...]*`, `*[OPTIONAL:...]*`, `[OPTIONAL]`, and any other italicized drafting guidance throughout the entire document. None of these should appear in the output.

---

## B. Conditional Decisions

These modifications depend on intake answers.

### B1. Order Form — Services Description

- **Intake field:** `product_description`
- **YC text:** "[Name and briefly describe services here] (the 'Service(s)')."
- **Action:** Replace the bracketed placeholder with the product description from intake. The description should be broad, concise, and factual. Format: "[Company] develops and makes available [product_description] (the 'Service(s)')."

### B2. Order Form — Service Fees

- **Intake fields:** `fee_type`, `fee_details`, `service_capacity`, `overage_terms`
- **YC text:** "$______________ per month, payable in advance, subject to the terms of Section 4 herein."
- **Action:** Compose the Service Fees line using the pattern from supplementary-language.md `#FEE-EXAMPLES` that matches `fee_type`. Fill in amounts from `fee_details`. This is the ONE section where composed (not verbatim) language is used.
- **Service Capacity:** If `fee_type` is per_seat, usage, minimum_plus_overage, prepaid_capacity, tiered, or hybrid → keep "Service Capacity" line and fill from intake. If flat or performance → delete "Service Capacity" line and the overage note.

### B3. Order Form — Implementation Services

- **Intake field:** `implementation_services`
- **If true:** Keep "Implementation Services" and "Implementation Fee" sections in Order Form. Keep Exhibit A (SOW). Fill fee from `implementation_fee`. Flag in memo: "Implementation services included — discuss IP ownership of custom deliverables with counsel."
- **If false:** Delete "Implementation Services" paragraph, "Implementation Fee" line from Order Form. Delete Exhibit A entirely. Remove "Implementation Services" from Section 1.1 text. Remove "and Implementation Services" from Section 6 warranty language.

### B4. Order Form — Pilot Period

- **Intake field:** `pilot`
- **If true:** Keep "Pilot Use" section. Fill Pilot Period from `pilot_duration` and Pilot Use Fee from `pilot_fee`. If fee is $0, write "$0 (no charge)".
- **If false:** Delete entire "Pilot Use" section from Order Form, including Pilot Period and Pilot Use Fee lines.

### B5. Section 2.1 — Distributed Software License

- **Intake field:** `distributed_software`
- **YC text:** "Company hereby grants Customer a non-exclusive, non-transferable, non-sublicensable license to use such Software during the Term only in connection with the Services." followed by `*[OPTIONAL:...]*`
- **If true:** Keep the license sentence. Delete the optional note.
- **If false:** Delete the license sentence AND the optional note. Pure cloud SaaS does not distribute software.

### B6. Section 3.2 — Derivative Data Ownership

- **Intake field:** `customer_owns_derivatives`
- **YC text:** "Customer shall own all right, title and interest in and to the Customer Data[, as well as any data that is based on or derived from the Customer Data and provided to Customer as part of the Services]" followed by `*[OPTIONAL:...]*`
- **If true:** Keep the bracketed language (remove brackets, keep text). Delete the optional note. Customer owns raw data + derived outputs.
- **If false:** Remove the bracketed language entirely. Delete the optional note. Customer owns raw Customer Data only. Flag in memo: "Customer does not own derivative data — expect counterparty negotiation on this point."

### B7. Section 5.1 — Auto-Renewal

- **Intake fields:** `auto_renewal`, `renewal_notice_days`
- **YC text:** "automatically renewed for additional periods of the same duration... unless either party requests termination at least thirty (30) days prior to the end of the then-current term."
- **If auto_renewal: true, notice: 30:** Keep as-is.
- **If auto_renewal: true, notice: 60:** Change "thirty (30) days" to "sixty (60) days".
- **If auto_renewal: true, notice: 90:** Change "thirty (30) days" to "ninety (90) days".
- **If auto_renewal: false:** Replace Section 5.1 with verbatim text from supplementary-language.md `#NO-AUTO-RENEWAL`.

### B8. Section 5.2 — Data Retrieval on Termination

- **Intake field:** `data_retention_days`
- **YC text:** "[Upon any termination, Company will make all Customer Data available to Customer for electronic retrieval for a period of thirty (30) days, but thereafter Company may, but is not obligated to, delete stored Customer Data.]" and `*[Confirm appropriate language...]*`
- **Action:** Remove the brackets around the paragraph — this language is always included. Remove the `*[Confirm...]*` note. Replace "thirty (30) days" with the value from `data_retention_days` (e.g., "sixty (60) days"). This section is always present.

### B9. Section 9 — Governing Law

- **Intake field:** `governing_law`
- **YC text:** "State of [California]"
- **Action:** Replace "[California]" with the state from intake (derived from `principal_place_of_business`). Default: California.

### B10. Section 9 — Marketing Formulation Adjustment

- **Intake field:** `marketing_formulation`
- **If "default":** No change — the always-apply default marketing language (#MARKETING-DEFAULT) is used.
- **If "more":** Flag in memo: "User requested expanded marketing rights beyond the default. Attorney should draft appropriate press release or reference account language."
- **If "less":** Flag in memo: "User requested more restrictive marketing language. Attorney should review and potentially remove or narrow the default marketing clause."

### B11. Exhibit B — Availability Commitment

- **Intake field:** `availability_tier`
- **Action:** In the consolidated Exhibit B, substitute the `[99.9]` placeholder with the selected tier. Adjust the credit table first row accordingly: if 99.95%, the 0% credit row becomes "99.95 - 100.0%" and the 5% row starts at "99.0 - 99.94%". If 99.99%, adjust similarly.

### B12. Exhibit B — Support Details

- **Intake fields:** `support_email`, `support_phone`, `support_hours`, `communication_tool`
- **Action:** Substitute all support placeholders in the consolidated Exhibit B per the variable table in supplementary-language.md `#EXHIBIT-B-CONSOLIDATED`. If `communication_tool` is "none", remove the COMMUNICATION TOOL column from the contact channels table.

---

## C. Variable Substitutions

All placeholders mapped to intake fields.

| YC Placeholder | Intake Field | Default if Missing |
|---|---|---|
| `[Company, Inc.]` (preamble + signature, 2 places) | `company_name` | `[TBD — Company Name]` |
| `[COMPANY NAME]` (Order Form header) | `company_name` (uppercase) | `[TBD — COMPANY NAME]` |
| `[Customer]` (signature block) | `customer_name` | `[TBD — Customer Name]` |
| `Customer:` (Order Form top) | `customer_name` | `[TBD — Customer Name]` |
| `[Name and briefly describe services here]` | `product_description` | `[TBD — Service Description]` |
| `$______________ per month` | composed from `fee_type` + `fee_details` | `[TBD — Service Fees]` |
| `[One] Year` | `initial_term` | `One` |
| `$____________` (implementation fee) | `implementation_fee` | `[TBD — Implementation Fee]` |
| `[Sixty (60) days]` (pilot period) | `pilot_duration` | `[TBD — Pilot Period]` |
| `[$XXX]` (pilot fee) | `pilot_fee` | `[TBD — Pilot Fee]` |
| `[California]` (governing law) | `governing_law` | California |
| `thirty (30) days` (renewal notice, §5.1) | `renewal_notice_days` | thirty (30) |
| `thirty (30) days` (data retrieval, §5.2) | `data_retention_days` | thirty (30) |
| `place of business at _______` | (not collected) | `[TBD — Company Address]` |
| `Service Capacity: ________` | `service_capacity` | `[TBD — Service Capacity]` or deleted per B2 |
| `[99.9]` (Exhibit B availability) | `availability_tier` | 99.9 |
| `[support@company.com]` (Exhibit B, 2 places) | `support_email` | `[TBD — Support Email]` |
| `[phone number]` (Exhibit B) | `support_phone` | `[TBD — Support Phone]` |
| `[Shared Company channel]` (Exhibit B) | `communication_tool` | Remove column if none |
| `[9:00 am Pacific Time]` | `support_hours` (start) | 9:00 am Pacific Time |
| `[5:00 pm Pacific Time]` | `support_hours` (end) | 5:00 pm Pacific Time |

**Fields not collected during intake** (billing address, contact info on Order Form, etc.) are left as `[TBD — description]` with clear labels. The memo lists all TBD items.

---

## D. Raise with Lawyer

These items are flagged in the lawyer memo for attorney review. The skill
does not resolve them — it identifies the issue and explains why counsel
should weigh in.

### D1. DPA (Data Processing Addendum)

- **Trigger:** Always flagged. The §2.5 data privacy language references a DPA.
- **Memo text:** "A Data Processing Addendum (DPA) will almost certainly be needed, especially if either party operates internationally or processes personal data of California residents. DPA drafting should be handled separately — use dpa-drafter skill."

### D2. Implementation Services IP Ownership

- **Trigger:** `implementation_services: true`
- **Memo text:** "Implementation services are included. Custom development, onboarding, and training work create IP ownership questions — who owns the custom deliverables? This must be resolved with counsel before sending. Consider whether a separate Statement of Work with IP assignment provisions is needed."

### D3. Derivative Data Ownership

- **Trigger:** `customer_owns_derivatives: false`
- **Memo text:** "Customer does not own derivative data under the current draft. This is a common negotiation point — counterparty's counsel will likely push for ownership of all outputs generated from their data. Discuss acceptable compromise positions with counsel."

### D4. ML Training on Customer Content

- **Trigger:** `ml_trains_on_content: true`
- **Memo text:** "Company trains ML models on customer content. The data rights language in Section 3.3 must be reviewed by counsel to confirm it (a) accurately describes the company's actual data practices, (b) provides sufficient legal basis for the training use, and (c) will withstand customer scrutiny during negotiation."

### D5. Data Retention Timeline

- **Trigger:** Always flagged.
- **Memo text:** "Data retention period is set to [X] days post-termination per Section 5.2. Counsel should verify this aligns with the company's actual data infrastructure, any regulatory retention requirements, and customer expectations."
