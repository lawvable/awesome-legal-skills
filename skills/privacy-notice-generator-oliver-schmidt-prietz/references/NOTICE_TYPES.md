# Privacy Notice Types — Profiles & Guidance

## Table of Contents
1. [Type Selection](#type-selection)
2. [Website / App](#website--app)
3. [Applicant / Recruiting](#applicant--recruiting)
4. [Employee](#employee)
5. [Business Partner (B2B)](#business-partner-b2b)
6. [B2C Customer](#b2c-customer)
7. [Combined Notices](#combined-notices)

---

## Type Selection

Ask the user as the **very first question** after jurisdiction:

> "What type of privacy notice do you need?"

| Type | Typical Trigger Phrases |
|---|---|
| **Website / App** | "website", "app", "online service", "landing page", "SaaS", "platform" |
| **Applicant** | "Bewerber", "applicant", "recruiting", "career page", "candidat", "Bewerbungsverfahren" |
| **Employee** | "Mitarbeiter", "employee", "HR", "salarié", "Beschäftigte", "workforce" |
| **Business Partner** | "B2B", "vendor", "supplier", "business partner", "Geschäftspartner", "partenaire" |
| **B2C Customer** | "customer", "Kunde", "client", "loyalty", "CRM", "retail", "e-commerce" |

If the user needs multiple types → see [Combined Notices](#combined-notices).

Each type profile below defines:
- **Section map**: Which of the 13 standard sections to include, skip, or adapt
- **Likely data categories**: Pre-populated suggestions to accelerate intake
- **Likely legal bases**: Default assumptions to confirm with user
- **Type-specific intake questions**: Additional questions beyond standard Groups A–F
- **Type-specific legal considerations**: Jurisdiction-dependent rules
- **Retention defaults**: Common retention periods for this type

---

## Website / App

### Section Map

| Section | Include? | Notes |
|---|---|---|
| 1. Controller | ✅ Always | |
| 2. Data collected | ✅ Always | Focus on collection points: forms, account, cookies |
| 3. Purposes & bases | ✅ Always | |
| 4. Recipients | ✅ Always | Heavy on tech processors |
| 5. Transfers | ✅ Always | Most web tools involve US transfers |
| 6. Retention | ✅ Always | |
| 7. Rights | ✅ Always | |
| 8. Cookies & tracking | ✅ **Critical** | Core section for this type |
| 9. AI & automated | ✅ If applicable | Chatbots, recommendations, content personalization |
| 10. Security | ✅ Always | |
| 11. Children | ✅ If service accessible to minors | |
| 12. Changes | ✅ Always | |
| 13. Contact | ✅ Always | |

### Sub-Types & Data Profiles

**Brochure / Corporate Site** (minimal data):
- Identity: name, email (contact form only)
- Technical: IP, browser/OS, access logs
- Cookies: analytics, possibly social embeds
- Legal bases: Legitimate interest (analytics, security), consent (marketing cookies)

**E-Commerce**:
- All brochure data PLUS: account data, shipping address, payment (via provider), order history, returns, wishlist
- Legal bases: Contract (orders, account), legal obligation (invoices), consent (newsletter, marketing), legitimate interest (fraud prevention)

**SaaS / Web App**:
- All brochure data PLUS: account, usage/feature logs, API usage, collaboration data, uploaded content, settings
- Legal bases: Contract (service provision), legitimate interest (product improvement, security)

**Mobile App**:
- All web app data PLUS: device ID, push tokens, device permissions (camera, location, microphone, contacts), app usage metrics, crash logs
- Must disclose each permission and its purpose

**Marketplace / Platform**:
- Dual data subjects (buyers + sellers), ratings/reviews, messaging, payment escrow, seller verification documents
- Consider separate sub-sections for each user role

### Type-Specific Intake Questions
1. What forms exist on the site? (contact, registration, checkout, newsletter)
2. Is there user account creation? What data is required vs. optional?
3. What analytics tools are used? (GA4, Matomo, Plausible, Mixpanel)
4. Any third-party embeds? (YouTube, Google Maps, social buttons, chat widgets)
5. Any A/B testing or personalization tools?
6. Does the site use a CDN? (Cloudflare, Fastly — may involve data transfer)
7. Is there a blog with comments?
8. Any user-generated content?

### Retention Defaults
| Data | Duration | Basis |
|---|---|---|
| Contact form submissions | 6–12 months after resolution | Art. 6(1)(f) |
| Active account | Duration of relationship | Art. 6(1)(b) |
| Inactive account | 2–3 years after last activity | Prospecting limitation |
| Server logs | 7–30 days | Art. 6(1)(f) security |
| Cookies | Max 13 months (FR) / session-based or as declared | TDDDG § 25 / CNIL |
| Invoices | 6–10 years depending on jurisdiction | HGB/AO/Code de commerce |

### Sample Clause Patterns

**Analytics consent row** (purposes table):
```
| Web analytics | Understanding how visitors use our website to improve user experience | Art. 6(1)(a) GDPR — your consent via our cookie banner | Anonymized: unlimited; pseudonymized: [13 months / 26 months] |
```

**Third-party embed disclosure**:
```
Our website embeds content from third-party services ([YouTube / Google Maps / social media plugins]). When you access pages containing such content, a connection is established to the provider's servers, which may set cookies and collect your IP address. Legal basis: Art. 6(1)(a) GDPR — your consent. You can manage your preferences via our consent tool at any time.
```

**Soft opt-in clause** (existing customers):
```
If you have previously purchased [goods/services] from us, we may send you information about similar [goods/services] by email. This is based on [§ 7(3) UWG (DE) / Art. L.34-5 CPCE (FR) / Regulation 22 PECR (UK)]. You can unsubscribe at any time using the link in each email or by contacting us.
```

**Newsletter consent**:
```
| Newsletter & marketing emails | Sending you information about [products/services/offers] | Art. 6(1)(a) GDPR — your consent | Until you withdraw your consent |
```

**Contact form**:
```
| Responding to your inquiry | Processing and responding to your contact form submission | Art. 6(1)(f) GDPR — our legitimate interest in responding to inquiries / Art. 6(1)(b) GDPR if related to a contract | 6 months after resolution of your inquiry |
```

---

## Applicant / Recruiting

### Section Map

| Section | Include? | Notes |
|---|---|---|
| 1. Controller | ✅ Always | |
| 2. Data collected | ✅ Always | Sensitive data likely (health, disability, photo) |
| 3. Purposes & bases | ✅ Always | § 26 BDSG central in DE |
| 4. Recipients | ✅ Always | Recruiting platforms, background check providers, group companies |
| 5. Transfers | ✅ If applicable | Cloud HR tools (Workday, SAP SuccessFactors, Greenhouse) |
| 6. Retention | ✅ **Critical** | Short retention after rejection is key compliance point |
| 7. Rights | ✅ Always | |
| 8. Cookies & tracking | ⚠️ Only if career page has own cookies | Often minimal or handled by main site notice |
| 9. AI & automated | ✅ If applicable | CV screening, AI matching, automated pre-selection |
| 10. Security | ✅ Always | Emphasize confidentiality of application |
| 11. Children | ❌ Usually skip | Unless internship programs for minors |
| 12. Changes | ✅ Always | |
| 13. Contact | ✅ Always | |

### Likely Data Categories
- **Identity**: full name, date of birth, nationality, photo (if submitted), gender
- **Contact**: address, email, phone
- **Professional**: CV/resume, cover letter, work history, education, certifications, references
- **Assessment**: interview notes, assessment results, test scores
- **Sensitive (Art. 9)**: disability status (for accommodation / Schwerbehinderung), health (pre-employment medical), sometimes religion (church tax in DE)
- **Technical**: IP/logs if online application portal
- **AI-derived**: matching scores, automated screening results (if applicable)

### Likely Legal Bases
| Purpose | DE | FR | Generic EU |
|---|---|---|---|
| Application processing | § 26 Abs. 1 BDSG | Art. 6(1)(b) pre-contractual | Art. 6(1)(b) |
| Talent pool (future openings) | Consent (§ 26 Abs. 2 BDSG) | Consent Art. 6(1)(a) | Consent |
| Background checks | § 26 Abs. 1 BDSG (if necessary) | Art. 6(1)(b) + proportionality | Art. 6(1)(b) or (f) |
| Disability/Schwerbehinderung | § 26 Abs. 3 BDSG | Art. 9(2)(b) employment law | Art. 9(2)(b) |
| Equal opportunity monitoring | Art. 9(2)(b) employment law | Art. 9(2)(b) | Art. 9(2)(b) |
| AI-based screening | § 26 BDSG + Art. 22 DSGVO | Art. 6(1)(b) + Art. 22 RGPD | Art. 22 GDPR |

### Type-Specific Intake Questions
1. Is there an applicant tracking system (ATS)? Which one? (Personio, Workday, Greenhouse, SAP SF, BambooHR)
2. Do you use AI for CV screening or candidate matching?
3. Do you keep applications in a talent pool for future positions? For how long? With consent?
4. Are background checks or reference checks conducted?
5. Is there a works council (Betriebsrat) involved in the hiring process?
6. Do you collect disability status (Schwerbehinderung)?
7. Are external recruiters or headhunters involved (joint/separate controllership)?
8. Is the career page on the main website or a separate platform?
9. Do you process applicant data within a group of companies?

### Retention Defaults
| Data | Duration | Basis |
|---|---|---|
| Rejected applicant — standard | 6 months after rejection | AGG limitation period (DE), reasonable period (EU) |
| Rejected applicant — extended (with consent) | Up to 24 months | Consent for talent pool |
| Hired → employee | Transfers to employee file | § 26 BDSG / employment relationship |
| Assessment results | Delete with application | Same as application |
| Background check results | Immediately after decision | Data minimization |

### Type-Specific Legal Considerations
- **Germany**: § 26 BDSG is the primary legal basis, NOT Art. 6(1)(b). Art. 88 DSGVO + § 26 BDSG is the specific regime. Works council agreements (Betriebsvereinbarung) may serve as legal basis.
- **France**: CNIL "Guide recrutement" (2023) applies. Photo on CV: cannot be required. Criminal record check: limited to specific roles.
- **AI screening**: Art. 22 DSGVO applies if solely automated decisions with significant effect on the applicant. Must disclose logic, significance, consequences. Human review requirement.

### Sample Clause Patterns

**Talent pool consent**:
```
With your separate consent, we store your application documents in our talent pool to consider you for future suitable positions. Legal basis: Art. 6(1)(a) GDPR — your consent [DE: § 26 Abs. 2 BDSG]. Your data will be retained for [12/24] months. You may withdraw your consent at any time by contacting [contact].
```

**Rejection retention**:
```
If your application is unsuccessful, we retain your application data for [6 months (DE) / up to 2 years (FR)] after notification of the rejection. This serves to protect our legitimate interests in the event of potential legal proceedings (e.g., under the AGG / Code du travail). Legal basis: Art. 6(1)(f) GDPR [DE: § 26 Abs. 1 BDSG]. After this period, your data will be deleted unless you have consented to inclusion in our talent pool.
```

**AI screening disclosure**:
```
We use [system name] to support our candidate selection process. This system [analyses CVs for keyword matching / ranks candidates based on qualifications]. The results are used as one factor among others and are always reviewed by our recruitment team before any decision is made. Legal basis: Art. 6(1)(b) GDPR [DE: § 26 Abs. 1 BDSG]. You have the right to obtain human intervention, express your point of view, and contest the decision.
```

**External recruiter / Art. 14 source**:
```
If your data was provided to us by a recruitment agency or headhunter, the source of your data is [agency name / category: "external recruitment agencies"]. We received the following categories of data: [name, contact details, CV, professional qualifications]. We will inform you of this processing at the latest at the time of first contact.
```

---

## Employee

### Section Map

| Section | Include? | Notes |
|---|---|---|
| 1. Controller | ✅ Always | Employer as controller |
| 2. Data collected | ✅ Always | Very broad — payroll, health, performance, IT monitoring |
| 3. Purposes & bases | ✅ Always | Multiple bases: § 26 BDSG, legal obligation, BV |
| 4. Recipients | ✅ Always | Payroll provider, tax authorities, social insurance, pension, group companies |
| 5. Transfers | ✅ If applicable | Global HR platforms, group companies abroad |
| 6. Retention | ✅ **Critical** | Complex multi-period retention |
| 7. Rights | ✅ Always | Note: some rights limited in employment context |
| 8. Cookies & tracking | ⚠️ Only if intranet/employee tools | IT monitoring section instead |
| 9. AI & automated | ✅ If applicable | Performance scoring, workforce analytics, AI in HR tools |
| 10. Security | ✅ Always | |
| 11. Children | ❌ Skip | Unless apprenticeships (Ausbildung) with minors |
| 12. Changes | ✅ Always | |
| 13. Contact | ✅ Always | |

### Additional Sections (Employee-Specific)
- **IT Monitoring / BYOD**: Internet usage, email monitoring, device management policies
- **Video Surveillance**: § 4 BDSG, works council co-determination
- **GPS / Vehicle Tracking**: If company vehicles are tracked
- **Whistleblowing**: HinSchG (DE) / Loi Sapin II (FR) data processing
- **Works Council Access**: What data is shared with the Betriebsrat

### Likely Data Categories
- **Master data**: name, address, date of birth, tax ID, social insurance number, bank details
- **Contract**: employment contract, position, salary, working hours, start/end dates
- **Payroll**: salary, bonuses, tax class, deductions, benefits
- **Time & attendance**: working hours, overtime, vacation, sick leave
- **Performance**: reviews, goals, training, certifications
- **Health**: sick certificates (AU-Bescheinigungen), occupational health, BEM records
- **IT**: login data, email (if monitored), internet usage logs, access badges
- **Sensitive**: disability (SB status), religion (church tax), trade union membership (if payroll-relevant)

### Retention Defaults (DE)
| Data | Duration | Basis |
|---|---|---|
| Payroll records | 6 years after end of employment | § 257 HGB |
| Tax records | 10 years | § 147 AO |
| Social insurance records | Until age 67 + 6 years | SGB IV |
| Personnel file (general) | 3 years after termination | General limitation §§ 195, 199 BGB |
| Sick certificates | 1 year after end of year | Data minimization |
| BEM records | 3 years after end of BEM | Labor court precedent |
| Works council election records | 5 years | BetrVG |

### Type-Specific Intake Questions
1. What HR/payroll system is used? (Personio, SAP HCM, DATEV, Workday)
2. Is there IT monitoring? (Email, internet, screen monitoring)
3. Is there video surveillance on premises?
4. Are company vehicles tracked (GPS)?
5. BYOD policy? Mobile device management?
6. Works council in place? Relevant Betriebsvereinbarungen?
7. Is the company part of a group? Intra-group data sharing?
8. Whistleblowing channel in place?
9. Occupational health management (BEM)?
10. Any AI in HR processes? (People analytics, performance scoring)

### Sample Clause Patterns

**IT monitoring disclosure**:
```
We monitor the use of company IT systems (email, internet, applications) to ensure IT security, prevent data breaches, and comply with legal obligations. Monitoring is limited to metadata (sender/recipient, timestamps, data volumes) and does not include content surveillance. Legal basis: Art. 6(1)(f) GDPR [DE: § 26 Abs. 1 BDSG]. [If works council agreement exists: Processing is also based on the works council agreement dated [date] pursuant to § 26 Abs. 4 BDSG.]
```

**Church tax clause** (DE):
```
| Church tax processing | Calculating and remitting church tax as legally required | Art. 6(1)(c) GDPR + Art. 9(2)(b) GDPR, § 26 Abs. 3 BDSG, § 51a EStG | Duration of employment + 6 years (§ 257 HGB) |
```

**Sick leave handling**:
```
We process sick leave certificates (AU-Bescheinigungen / arrêts maladie) for the purpose of continued pay entitlement and absence management. We only receive information about the duration of incapacity, not the diagnosis. Legal basis: Art. 6(1)(c) GDPR + Art. 9(2)(b) GDPR [DE: § 26 Abs. 3 BDSG + § 5 EFZG]. Retention: [1 year after end of calendar year (DE) / duration + 5 years (FR)].
```

**BYOD clause**:
```
If you use personal devices for work purposes (BYOD), we process device identifiers and usage data through our mobile device management (MDM) solution [name] to protect company data and ensure IT security. We do not access personal content on your device. Legal basis: Art. 6(1)(f) GDPR — our legitimate interest in IT security [DE: § 26 Abs. 1 BDSG].
```

---

## Business Partner (B2B)

### Section Map

| Section | Include? | Notes |
|---|---|---|
| 1. Controller | ✅ Always | |
| 2. Data collected | ✅ Always | Minimal — contact persons, not companies |
| 3. Purposes & bases | ✅ Always | Legitimate interest dominant |
| 4. Recipients | ✅ Always | CRM, ERP, group companies |
| 5. Transfers | ✅ If applicable | CRM/ERP often US-based |
| 6. Retention | ✅ Always | Tied to commercial retention obligations |
| 7. Rights | ✅ Always | |
| 8. Cookies & tracking | ❌ Usually skip | Unless B2B portal with login |
| 9. AI & automated | ⚠️ Rarely | Only if credit scoring or AI in procurement |
| 10. Security | ✅ Always | |
| 11. Children | ❌ Skip | Not applicable |
| 12. Changes | ✅ Always | |
| 13. Contact | ✅ Always | |

### Key Distinction: Art. 13 vs. Art. 14
Business partner notices often involve **Art. 14** (data not collected directly from the data subject):
- Contact persons at a business partner may not have provided their data directly
- Their details may come from the company itself, public registers, LinkedIn, trade fairs
- Art. 14 requires disclosing the **source** of data and **categories** of data
- Must be provided within **1 month** of obtaining the data, or at first communication

### Likely Data Categories
- **Business contact**: name, position/title, business email, business phone, company name
- **Contract**: signatory details, authorized representatives
- **Financial**: company bank details, credit information (for B2B credit checks)
- **Communication**: business correspondence, meeting notes
- **Source**: How the contact was obtained (direct, website, trade fair, public register, referral)

### Likely Legal Bases
| Purpose | Legal Basis | Notes |
|---|---|---|
| Contract management | Art. 6(1)(b) if data subject is the contracting party; Art. 6(1)(f) if contact person at the partner company | Contact persons ≠ contracting entity |
| Pre-contractual measures | Art. 6(1)(b) or (f) | RFQs, proposals, negotiations |
| B2B prospecting | Art. 6(1)(f) | Legitimate interest — balancing test needed |
| Accounting & invoicing | Art. 6(1)(c) — tax/commercial law | HGB, AO, Code de commerce |
| CRM management | Art. 6(1)(f) | Relationship management |
| Compliance / KYC | Art. 6(1)(c) — AML, sanctions | If applicable |
| Credit check | Art. 6(1)(f) or (b) | § 31 BDSG (DE) if scoring |

### Type-Specific Intake Questions
1. How do you obtain business contact data? (Direct, trade fairs, LinkedIn, purchased lists, referrals)
2. Is there a B2B portal or customer login?
3. Do you conduct credit checks on business partners?
4. What CRM/ERP is used? (Salesforce, HubSpot, SAP, Microsoft Dynamics)
5. Do you share data within a corporate group?
6. Any compliance/KYC requirements? (Anti-money laundering, sanctions screening)
7. Are business contacts used for marketing? How (email, phone, events)?

### Retention Defaults
| Data | Duration | Basis |
|---|---|---|
| Active business relationship | Duration of relationship | Art. 6(1)(b)/(f) |
| Post-termination (contracts) | 3 years (general limitation) → up to 10 years (tax) | BGB/HGB/AO |
| Invoices & accounting | 6–10 years | HGB § 257 / AO § 147 |
| Prospecting contacts (no relationship) | 3 years without interaction | LI balancing |
| KYC/AML records | 5 years after end of relationship | GwG § 8 |

### Sample Clause Patterns

**Art. 14 source disclosure**:
```
We may obtain your business contact data from the following sources: your employer or the company you represent, publicly accessible business registers (e.g., Handelsregister, Registre du Commerce), professional networks (e.g., LinkedIn), trade fairs and industry events, or business referrals. Categories of data obtained: name, professional title, business email, business phone, company name.
```

**B2B prospecting legitimate interest**:
```
| Business development / B2B prospecting | Contacting potential business partners about our [products/services] relevant to their professional activity | Art. 6(1)(f) GDPR — our legitimate interest in developing business relationships | 3 years from last interaction |
```

**CRM management**:
```
We store your business contact data in our CRM system ([Salesforce / HubSpot / Microsoft Dynamics]) to manage our business relationship, coordinate communications, and ensure quality of service. Legal basis: Art. 6(1)(f) GDPR — our legitimate interest in efficient relationship management.
```

**Credit check clause** (B2B):
```
Before entering into a business relationship, we may obtain creditworthiness information about your company from [Creditreform / SCHUFA / Coface / Euler Hermes]. This includes scoring data and credit ratings. Legal basis: Art. 6(1)(f) GDPR — our legitimate interest in assessing credit risk [DE: § 31 BDSG]. You have the right to object to this processing.
```

---

## B2C Customer

### Section Map

| Section | Include? | Notes |
|---|---|---|
| 1. Controller | ✅ Always | |
| 2. Data collected | ✅ Always | Broad — account, purchase, payment, preferences |
| 3. Purposes & bases | ✅ Always | Contract + consent + legitimate interest mix |
| 4. Recipients | ✅ Always | Payment, shipping, marketing tools |
| 5. Transfers | ✅ Always | Payment processors, marketing tools often US-based |
| 6. Retention | ✅ Always | |
| 7. Rights | ✅ Always | Right to object for direct marketing is key |
| 8. Cookies & tracking | ✅ If online | Cross-reference with website notice or integrate |
| 9. AI & automated | ✅ If applicable | Recommendations, scoring, personalization, fraud detection |
| 10. Security | ✅ Always | Payment security particularly relevant |
| 11. Children | ✅ If products/services for minors | Toy stores, gaming, education |
| 12. Changes | ✅ Always | |
| 13. Contact | ✅ Always | |

### Context: Online vs. Offline B2C
This type covers customer relationships that may be purely offline (retail store), purely online (e-commerce — overlaps with Website type), or hybrid. For pure e-commerce, combine this profile with the Website/App profile.

### Likely Data Categories
- **Identity**: name, email, phone, address, date of birth (age verification, birthday offers)
- **Account**: credentials, preferences, wishlist, saved addresses
- **Purchase**: order history, product preferences, returns, warranty claims
- **Payment**: payment method (via processor), billing address, installment data
- **Marketing**: newsletter consent, campaign interactions, promotion usage
- **Loyalty**: points, tier status, program participation
- **Communication**: support tickets, reviews, complaints, chat history
- **Profiling**: purchase patterns, segment assignment, churn prediction, lifetime value

### Likely Legal Bases
| Purpose | Legal Basis | Notes |
|---|---|---|
| Order fulfillment | Art. 6(1)(b) | Contract performance |
| Account management | Art. 6(1)(b) | |
| Payment processing | Art. 6(1)(b) | Via processor (Stripe, PayPal, etc.) |
| Invoice retention | Art. 6(1)(c) | Tax law |
| Newsletter / email marketing | Art. 6(1)(a) consent | Soft opt-in for existing customers (DE: § 7 Abs. 3 UWG; FR: Art. L.34-5 CPCE) |
| Customer profiling | Art. 6(1)(f) or consent | Depends on intrusiveness |
| Fraud prevention | Art. 6(1)(f) | Legitimate interest |
| Product reviews | Art. 6(1)(f) or (b) | |
| Loyalty program | Art. 6(1)(b) if contractual; (a) if optional | |
| Warranty / legal claims | Art. 6(1)(c) or (f) | |

### Type-Specific Intake Questions
1. Is this for online, offline (retail), or omnichannel?
2. What payment methods / processors? (Stripe, PayPal, Klarna, Adyen)
3. Is there a loyalty program? What data is collected for it?
4. Do you do customer profiling or segmentation? How?
5. Email marketing: opt-in or soft opt-in for existing customers?
6. Do you use retargeting (Meta Pixel, Google Ads remarketing)?
7. Product reviews: own system or third-party (Trustpilot, Verified Reviews)?
8. Do you send postal marketing?
9. Customer support channels? (Email, phone, chat, WhatsApp)
10. Any credit check / BNPL (Buy Now Pay Later) integration?

### Retention Defaults
| Data | Duration | Basis |
|---|---|---|
| Active customer account | Duration of relationship | Art. 6(1)(b) |
| Inactive customer (marketing) | 3 years without interaction | LI / CNIL recommendation |
| Order/purchase data | Duration + 3–10 years | BGB/HGB/AO limitation + tax |
| Invoices | 6–10 years | HGB/AO/Code de commerce |
| Payment data | Delete after settlement + chargeback period | PCI DSS + Art. 6(1)(b) |
| Warranty claims | 2 years (legal warranty) | BGB § 438 / Code civil |
| Marketing consent proof | 3–6 years | Proof of consent |
| Reviews | Duration of publication + 3 years | Art. 6(1)(f) |
| Support tickets | 3 years after resolution | Limitation |

### Sample Clause Patterns

**Loyalty program**:
```
If you join our [loyalty program name], we process your purchase history, points balance, tier status, and preferences to administer the program and provide personalized offers. Legal basis: Art. 6(1)(b) GDPR — performance of the loyalty program terms. We may also analyse your purchase patterns to tailor offers to your interests; legal basis: Art. 6(1)(f) GDPR — our legitimate interest in personalized customer communication. You can leave the program at any time by contacting [contact].
```

**BNPL / credit check** (B2C):
```
If you choose to pay by installment ([Klarna / PayPal Pay Later / other BNPL provider]), your data (name, address, date of birth, order details) is transmitted to [provider], which conducts a creditworthiness assessment. [Provider] acts as an independent controller for the credit check. Legal basis for data transmission: Art. 6(1)(b) GDPR — contract performance. For details on [provider]'s processing, see their privacy notice at [URL].
```

**Profiling disclosure**:
```
We analyse your purchase history and browsing behaviour to create a customer profile used for personalised product recommendations and marketing. This profiling does not produce legal or similarly significant effects. Legal basis: Art. 6(1)(f) GDPR — our legitimate interest in relevant customer communication. You have the right to object to this profiling at any time (see Section [X] — Your Rights).
```

**Soft opt-in for existing customers**:
```
As an existing customer, we may send you marketing emails about products or services similar to those you have previously purchased. This is based on [§ 7(3) UWG (DE) / Art. L.34-5 CPCE (FR)]. You can opt out at any time by clicking the unsubscribe link in any email or by contacting us at [contact].
```

**Product review clause**:
```
If you submit a product review, we publish your [display name / first name] and review text on our website. Legal basis: Art. 6(1)(f) GDPR — our legitimate interest in providing product information to other customers [or Art. 6(1)(a) if consent-based]. Reviews are retained for the duration of the product listing + 3 years. You can request deletion of your review at any time.
```

---

## Combined Notices

If a user needs a notice covering multiple types (e.g., a company website that also has an applicant portal and B2B partner section):

### Option A: Single Comprehensive Notice (Recommended for Small/Medium)
- Merge all relevant section maps
- Use sub-headings within sections to separate audiences
- Example: Section 3 has sub-sections "3.1 Website visitors", "3.2 Applicants", "3.3 Business partners"
- Risk: document becomes long and hard to navigate

### Option B: Separate Notices (Recommended for Large/Complex)
- One notice per audience / data subject category
- Linked from a central privacy hub page
- Easier to maintain and update
- Better for complex organizations with different processing activities per audience
- German best practice: separate "Datenschutzhinweise für Bewerber" is very common

### Option C: Layered Approach
- One short general notice (1–2 pages) covering common elements (controller, rights, security, contact)
- Separate detailed annexes per type
- Good for organizations with many data subject categories

**Recommendation**: Ask the user which approach they prefer. For most SMEs, Option A with clear sub-headings works. For larger organizations or those with sensitive processing (e.g., employee + applicant), Option B is safer and more maintainable.
