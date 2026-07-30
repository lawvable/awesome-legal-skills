# SOC 2 Vendor Risk Reference

## Table of Contents
1. [Vendor Risk Program Overview](#vendor-risk-program-overview)
2. [Vendor Inventory Template](#vendor-inventory-template)
3. [Vendor Risk Questionnaire](#vendor-risk-questionnaire)
4. [Reviewing a Vendor's SOC 2 Report](#reviewing-a-vendors-soc-2-report)
5. [CUEC Management](#cuec-management)
6. [Vendor Onboarding Checklist](#vendor-onboarding-checklist)

---

## Vendor Risk Program Overview

SOC 2 CC9.2 requires organizations to assess and manage risks arising from vendors and business
partners who have access to systems or data, or on whom the organization depends for critical
services.

### What auditors look for:
1. A **vendor inventory** exists and is maintained
2. Vendors are **tiered by risk** and assessed accordingly
3. **Due diligence** was performed before critical vendors were onboarded
4. Vendor assessments are **reviewed at least annually**
5. **Contracts** include appropriate security and data protection requirements
6. **CUECs** from vendor SOC 2 reports are identified and addressed

---

## Vendor Inventory Template

Maintain a spreadsheet or GRC tool record for each vendor:

| Field | Description |
|---|---|
| Vendor Name | Legal entity name |
| Service Provided | What they do for you |
| Risk Tier | Critical / High / Medium / Low |
| Data Access | Types of data they can access (PII, Confidential, none) |
| System Access | Production / Staging / None |
| SOC 2 Available? | Yes / No / In progress |
| Last Assessment Date | Date of most recent due diligence |
| Next Review Due | Based on tier cadence |
| Contract Expiry | Date |
| DPA Signed? | Yes / No / N/A |
| Security Addendum? | Yes / No / N/A |
| Primary Contact | Vendor security/legal contact |
| Owner | Internal stakeholder who owns the relationship |

### Risk Tier Definitions

**Critical:** Vendor has access to production systems or processes/stores customer PII.
Examples: AWS, Azure, GCP, Salesforce, Snowflake, Stripe, database vendors.
- Requires: SOC 2 report review OR full questionnaire + annual re-assessment
- Contract must include: DPA, security addendum, breach notification <72hr, right to audit

**High:** Vendor processes sensitive business data or is operationally critical.
Examples: HR systems (Workday, Rippling), GitHub, Slack, identity providers.
- Requires: SOC 2 report or questionnaire annually
- Contract must include: DPA (if any personal data), security requirements

**Medium:** Limited data exposure, some operational dependency.
Examples: Project management tools, design tools, analytics platforms.
- Requires: Security questionnaire or SOC 2 review at onboarding + biennial review
- Contract should include: acceptable use and data handling clauses

**Low:** No meaningful data access, low operational risk.
Examples: Office supplies vendors, most SaaS point solutions without data access.
- Requires: Lightweight onboarding check (do they have a security program?)
- Standard contract terms sufficient

---

## Vendor Risk Questionnaire

Use this questionnaire for High/Critical vendors that don't have a SOC 2 report, or to
supplement a SOC 2 report. Customize based on the vendor's service type.

---

### Section 1: Company and Security Program

1. Does your organization have a documented Information Security Policy? If yes, when was it last reviewed?

2. Do you have a dedicated security function (e.g., CISO, security team)? Please describe its structure.

3. Has your organization undergone any third-party security assessments in the past 12 months? (SOC 2, ISO 27001, pen test, etc.) If yes, please provide the most recent report or executive summary.

4. Does your organization carry cybersecurity insurance? Please provide coverage amount.

5. Have you experienced a security incident or data breach in the past 24 months that affected customers? If yes, please describe.

---

### Section 2: Access Controls

6. Do you enforce multi-factor authentication (MFA) for access to systems that process our data? Which systems require MFA?

7. How do you manage privileged/admin access? Do you use a Privileged Access Management (PAM) solution?

8. How quickly are accounts for terminated employees deprovisioned? What is your offboarding process?

9. Do you perform periodic access reviews? How frequently?

10. Is access to customer data restricted to personnel who require it for their role (least privilege)?

---

### Section 3: Data Protection

11. What data do you collect, process, or store on our behalf? Please provide a data inventory or data flow diagram.

12. Is data encrypted at rest? If yes, what encryption standard is used?

13. Is data encrypted in transit? What TLS version is enforced?

14. How is our data logically separated from data belonging to other customers (multi-tenancy)?

15. What is your data retention policy? How and when is our data deleted at contract end?

16. Do you have a sub-processor/sub-vendor list? Will you notify us before engaging new sub-processors?

---

### Section 4: Incident Response

17. Do you have a documented Incident Response Plan? When was it last tested?

18. What is your process and timeline for notifying customers of a security incident that affects their data?

19. Do you maintain security logs? For how long are logs retained?

20. Do you have a SIEM or security monitoring solution in place?

---

### Section 5: Vulnerability Management

21. How frequently do you perform vulnerability scanning on systems that process our data?

22. What is your SLA for remediating critical and high vulnerabilities?

23. How frequently do you perform penetration testing? Who performs it (internal or third-party)?

24. Do you have a patch management program? What is your patching cadence?

---

### Section 6: Business Continuity

25. Do you have a Business Continuity Plan (BCP) and Disaster Recovery Plan (DRP)?

26. What are your RTO (Recovery Time Objective) and RPO (Recovery Point Objective) for the systems we depend on?

27. How frequently do you test your DR plan? When was the last test performed?

28. Do you have redundant infrastructure (e.g., multi-region, HA setup)?

---

### Section 7: Compliance and Legal

29. Are you subject to any industry-specific compliance requirements (HIPAA, PCI-DSS, GDPR, etc.)? Are you currently compliant?

30. Are you willing to sign a Data Processing Agreement (DPA) with our organization?

31. Will you notify us within 72 hours of becoming aware of a breach involving our data?

32. Do you have a process for responding to Data Subject Requests (DSRs) that require action on data you process on our behalf?

---

### Scoring Guidance

For each question, score:
- **2** — Fully in place with evidence available
- **1** — Partially in place or controls exist but not fully documented/tested
- **0** — Not in place

| Score Range | Risk Level | Recommendation |
|---|---|---|
| 45–64 | Low risk | Proceed; standard contract terms |
| 30–44 | Medium risk | Proceed with DPA; annual re-review |
| 15–29 | High risk | Requires security addendum; risk acceptance from CISO |
| 0–14 | Critical risk | Escalate to leadership; consider alternative vendor |

---

## Reviewing a Vendor's SOC 2 Report

When a vendor provides their SOC 2 report, review the following:

### 1. Report Basics
- **Report type:** Is it Type 1 (design only) or Type 2 (operating effectiveness)? Prefer Type 2.
- **Audit period:** Does it cover a recent period? Reports older than 12 months are stale.
- **Criteria in scope:** Does the report include the criteria relevant to your use case? (e.g., if you care about availability, is Availability in scope?)
- **Auditor:** Is the CPA firm reputable? (Larger firms: Deloitte, KPMG, EY, PwC, Grant Thornton, etc.)

### 2. Auditor's Opinion
- **Unqualified (clean) opinion:** No material exceptions. 
- **Qualified opinion:** One or more criteria not met — flag for review.
- **Adverse opinion:** Multiple failures — escalate, this is a significant red flag.

### 3. Exceptions and Deviations
- Read the "results of tests of controls" section carefully.
- Any **exceptions** (control failures during the audit period) must be evaluated:
  - Is the control we depend on the one that had exceptions?
  - What was the vendor's remediation plan?
  - Has it been addressed (look for management response)?

### 4. Complementary User Entity Controls (CUECs)
- Look for a section titled "Complementary User Entity Controls" or similar.
- These are controls the vendor *requires you to operate* for their controls to be effective.
- You must address every applicable CUEC (see [CUEC Management](#cuec-management) below).

### 5. System Description
- Does the description match the services you actually use?
- Are the systems and infrastructure you depend on included in scope?

### Review Log Entry

Document each vendor SOC 2 review:
```
Vendor:             [Name]
Report Type:        Type 1 / Type 2
Audit Period:       [From] – [To]
Date Reviewed:      [Date]
Reviewed By:        [Name / Role]
Opinion:            Unqualified / Qualified / Adverse
Notable Exceptions: [None / Description]
CUECs Identified:   [None / List]
CUECs Addressed:    [Yes / Partial / No — with details]
Risk Rating:        Low / Medium / High
Action Items:       [Any follow-up required]
```

---

## CUEC Management

CUECs (Complementary User Entity Controls) are controls a vendor assumes *you* have in place.
If you don't have them, the vendor's controls may not fully protect your environment.

### Common CUECs and Typical Responses

| Common CUEC | Typical Vendor (Example) | Your Corresponding Control |
|---|---|---|
| "User entities restrict access to the service using the vendor's access control features" | AWS, Salesforce | Access control policy; MFA enforcement; role-based access |
| "User entities are responsible for monitoring for unauthorized access using access logs" | AWS CloudTrail, Okta | SIEM ingesting vendor logs; alerting on suspicious logins |
| "User entities configure data encryption using the features provided" | AWS S3, RDS | Encryption enabled at rest; documented in system configuration |
| "User entities are responsible for their users' credentials" | Any SaaS | Password policy; MFA policy; offboarding process |
| "User entities notify the vendor of any personnel changes" | Managed service providers | Offboarding SOP includes notifying critical vendors |
| "User entities perform their own risk assessments" | Most vendors | Annual risk assessment process (CC3) |

### CUEC Tracking Spreadsheet Fields

| CUEC # | Vendor | CUEC Description | Applicable? | Corresponding Control | Evidence | Owner | Status |
|---|---|---|---|---|---|---|---|
| 1 | AWS | Users restrict access via IAM | Yes | Access Control Policy + IAM review | Quarterly IAM review records | DevOps | Met |
| 2 | Salesforce | Users monitor login activity | Yes | SIEM ingests Salesforce logs | SIEM screenshots | Security | Met |

---

## Vendor Onboarding Checklist

Before onboarding a new Critical or High-tier vendor:

- [ ] Risk tier assigned based on data access and operational dependency
- [ ] Security questionnaire sent (or SOC 2 report requested)
- [ ] Questionnaire/report reviewed and scored
- [ ] Risk acceptance documented if score is medium/high
- [ ] Data Processing Agreement (DPA) executed (if PII involved)
- [ ] Security addendum signed (for Critical vendors)
- [ ] Contract includes: breach notification <72hr, data deletion on termination, right to audit
- [ ] CUECs identified and mapped to internal controls
- [ ] Vendor added to inventory with next review date
- [ ] Onboarding approved by CISO or security owner
