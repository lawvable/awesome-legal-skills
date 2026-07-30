# EU-Wide GDPR Reference

## Table of Contents
1. [Legal Bases (Art. 6)](#legal-bases)
2. [Special Category Data (Art. 9)](#special-category-data-art-9)
3. [Data Subject Rights (Art. 15–22)](#data-subject-rights)
4. [International Transfers (Chapter V)](#international-transfers)
5. [AI & Automated Decision-Making](#ai--automated-decision-making)
6. [Children's Data (Art. 8)](#childrens-data)
7. [Soft Opt-In for Direct Marketing](#soft-opt-in-for-direct-marketing)
8. [Art. 13/14 Mandatory Disclosures Checklist](#mandatory-disclosures-checklist)

---

## Legal Bases

### Art. 6(1)(a) — Consent
- Free, specific, informed, unambiguous
- Withdrawable at any time; withdrawal must be as easy as giving consent
- Burden of proof on controller (Art. 7(1))
- No pre-ticked boxes (Planet49, C-673/17)
- **Use for**: Newsletter, marketing cookies, ad tracking, sharing with partners, non-essential profiling

### Art. 6(1)(b) — Contract Performance
- Processing necessary for contract execution or pre-contractual steps at data subject's request
- Cannot be stretched to cover all processing a controller wants to do (EDPB Guidelines 2/2019)
- **Use for**: Order fulfilment, account creation/management, payment processing, customer support related to the contract

### Art. 6(1)(c) — Legal Obligation
- Processing necessary for compliance with a legal obligation to which the controller is subject
- Must identify the specific legal provision
- **Use for**: Tax retention, AML/KYC, employment law obligations, regulatory reporting

### Art. 6(1)(d) — Vital Interests
- Rarely applicable; only when data subject physically unable to consent
- **Use for**: Medical emergencies

### Art. 6(1)(e) — Public Interest / Official Authority
- Requires basis in Union or Member State law
- **Use for**: Public sector tasks, official authority exercise

### Art. 6(1)(f) — Legitimate Interest
- Requires documented balancing test (LIA): legitimate interest → necessity → balancing against rights
- Data subject has absolute right to object for direct marketing (Art. 21(2))
- **Use for**: Fraud prevention, network security, anonymized analytics, B2B prospecting, intra-group admin

## Special Category Data (Art. 9)

### What Qualifies as Special Category Data
Art. 9(1) GDPR prohibits processing of these 8 categories unless an Art. 9(2) exception applies:

| Category | Examples |
|---|---|
| **Racial or ethnic origin** | Nationality, ethnicity, photo (if revealing) |
| **Political opinions** | Party membership, political donations |
| **Religious or philosophical beliefs** | Church membership (church tax in DE), dietary requirements revealing beliefs |
| **Trade union membership** | Union dues deducted from payroll |
| **Genetic data** | DNA tests, genetic predisposition data |
| **Biometric data** (for identification) | Fingerprint access, facial recognition, iris scan |
| **Health data** | Sick certificates, disability status, occupational health, insurance data |
| **Sex life or sexual orientation** | Marital status (in some contexts), partner benefits |

### Art. 9(2) Exceptions (Legal Bases for Special Categories)

Processing special categories requires **both** an Art. 6 legal basis **and** an Art. 9(2) exception (dual legal basis requirement).

| Exception | Art. 9(2) | Typical Use Cases |
|---|---|---|
| **Explicit consent** | (a) | Voluntary health surveys, diversity monitoring (where not legally required) |
| **Employment & social security law** | (b) | Payroll (church tax, union dues, disability), sick leave, occupational health |
| **Vital interests** | (c) | Medical emergency when data subject incapacitated |
| **Not-for-profit bodies** | (d) | Processing by churches, unions, political parties for their members |
| **Manifestly public** | (e) | Data subject has clearly made the data public (e.g., public social media profile) |
| **Legal claims** | (f) | Establishing, exercising, or defending legal claims |
| **Substantial public interest** | (g) | Anti-discrimination monitoring, statutory equality duties |
| **Preventive/occupational medicine** | (h) | Pre-employment medicals, occupational health assessments, fitness-for-duty |
| **Public health** | (i) | Pandemic response, pharmacovigilance |
| **Archiving / research / statistics** | (j) | Scientific research with appropriate safeguards |

### Dual Legal Basis Requirement
Every processing of special category data must cite **two** legal bases:
1. **Art. 6(1)** basis — e.g., Art. 6(1)(b) contract, Art. 6(1)(c) legal obligation, Art. 6(1)(f) legitimate interest
2. **Art. 9(2)** exception — e.g., Art. 9(2)(b) employment law, Art. 9(2)(a) explicit consent

Example: Processing church tax data for an employee:
- Art. 6(1)(c) GDPR (legal obligation — tax law) **+** Art. 9(2)(b) GDPR (employment/social security law)

### What to Disclose in the Privacy Notice
For each special category processed, the notice must state:
- The specific category of sensitive data processed
- The purpose of processing
- The Art. 6 legal basis **and** the Art. 9(2) exception
- Any additional safeguards applied (e.g., restricted access, pseudonymization, DPO oversight)
- Specific legal provisions authorizing the processing (e.g., § 26(3) BDSG, Art. 9(2)(b) + national employment law)

### Intake Questions When Special Categories Are Detected
If any Art. 9 data is identified during intake, ask:
1. Which specific categories of sensitive data are processed?
2. What is the purpose for each sensitive data category?
3. Which Art. 9(2) exception applies to each? Is there a Member State law authorizing it?
4. Is explicit consent obtained? If so, how is it documented and how can it be withdrawn?
5. What additional safeguards are in place (access restrictions, encryption, DPO involvement)?
6. Is a DPIA required or already conducted for this processing? (Art. 35(3)(b) — large-scale special category processing requires DPIA)

## Data Subject Rights

| Right | Article | Conditions / Limits | Response Time |
|-------|---------|---------------------|---------------|
| **Access** | Art. 15 | Free first copy; may charge for additional | 1 month (extendable +2) |
| **Rectification** | Art. 16 | Inaccurate or incomplete data | 1 month |
| **Erasure ("Right to be Forgotten")** | Art. 17 | When consent withdrawn, no longer necessary, unlawful, etc. Exceptions: legal obligation, public interest, legal claims | 1 month |
| **Restriction** | Art. 18 | Accuracy contested, unlawful processing, controller no longer needs data but subject needs for claims | 1 month |
| **Data Portability** | Art. 20 | Only for consent/contract-based automated processing | 1 month |
| **Object** | Art. 21 | Legitimate interest: must demonstrate compelling grounds. Direct marketing: absolute right | 1 month |
| **Not be subject to automated decisions** | Art. 22 | Decisions producing legal/significant effects. Exceptions: contract, law, explicit consent | 1 month |
| **Withdraw Consent** | Art. 7(3) | At any time; as easy as giving consent | Without undue delay |

### Exercise Procedure (to include in notice)
- Dedicated email address (e.g., privacy@..., datenschutz@..., dpo@...)
- Postal address
- Identity verification method (proportionate — no excessive ID requests)
- Response timeline: 1 month, extendable by 2 months for complex/numerous requests
- Free of charge (except manifestly unfounded/excessive)

## International Transfers

### Transfer Mechanisms (Chapter V)
| Mechanism | Article | When to Use |
|-----------|---------|-------------|
| **Adequacy Decision** | Art. 45 | Country on EU Commission's adequate list |
| **Standard Contractual Clauses (SCCs)** | Art. 46(2)(c) | Most common mechanism for US/non-adequate transfers |
| **Binding Corporate Rules (BCRs)** | Art. 47 | Intra-group transfers |
| **Derogations** | Art. 49 | Explicit consent, contract necessity, public interest (narrow) |

### Adequacy Decisions (current as of 2025)
Andorra, Argentina, Canada (PIPEDA), Faroe Islands, Guernsey, Israel, Isle of Man, Japan, Jersey, New Zealand, Republic of Korea, Switzerland, UK, Uruguay, **USA (EU-U.S. Data Privacy Framework — DPF)**.

### US Transfers — Specifics
- EU-U.S. DPF (Adequacy Decision July 2023) — verify the recipient is on the DPF list
- If not DPF-certified: SCCs + Transfer Impact Assessment (TIA) required
- Mention Schrems II implications if relevant
- Common processors requiring US transfer disclosure: Google, Meta, AWS (if US region), Microsoft, Salesforce, Mailchimp/Intuit, HubSpot, Stripe

### What to Disclose in the Notice
For each transfer:
1. Country/countries of destination
2. Transfer mechanism used
3. Where to obtain a copy/info about safeguards (link or on-request)

## AI & Automated Decision-Making

### GDPR Art. 22 Requirements
If the service uses AI/ML for decisions that produce legal or similarly significant effects:
- **Right not to be subject** to solely automated decisions
- Must disclose: (1) existence of automated decision-making, (2) meaningful information about the logic involved, (3) significance and envisaged consequences
- Exceptions: contract, law, explicit consent — but even then, safeguards required (human intervention, express point of view, contest)

### EU AI Act Interplay (Regulation 2024/1689)
Applicable from August 2025 onwards (phased):

**Transparency obligations for AI systems (Art. 50 AI Act)**:
- AI-generated content must be disclosed (chatbots, deepfakes, synthetic text)
- Users must be informed they are interacting with an AI system
- High-risk AI systems: extensive documentation and transparency requirements

**Privacy notice should address**:
- Whether AI/ML is used in processing personal data
- Purpose of AI processing (recommendations, scoring, content generation, moderation)
- Whether decisions are purely automated or human-in-the-loop
- Meaningful explanation of logic (not source code, but understandable impact description)
- How to contest AI-driven decisions
- Data used for training (if applicable to the user's data)

### Standard AI Disclosure Wording (adapt per jurisdiction language)
```
[AI / AUTOMATED PROCESSING]

We use automated processing technologies, including [machine learning / artificial intelligence], for the following purposes:
- [Purpose 1, e.g., personalized content recommendations]
- [Purpose 2, e.g., fraud detection]

[If Art. 22 applies:]
These processes may produce decisions that significantly affect you. You have the right to:
- Obtain human intervention
- Express your point of view
- Contest the decision

To exercise these rights, contact [DPO/privacy contact].

[If AI Act applies:]
In accordance with the EU AI Act (Regulation 2024/1689), we inform you that [specific AI transparency disclosure].
```

## Children's Data

### Age Thresholds by Member State (Art. 8 GDPR)

| Country | Age | Source |
|---------|-----|--------|
| Austria | 14 | § 4(4) DSG |
| Belgium | 13 | Art. 7 loi du 30 juillet 2018 |
| Croatia | 16 | default |
| Czech Republic | 15 | § 7 Zákon č. 110/2019 |
| Denmark | 13 | § 6 Databeskyttelsesloven |
| Estonia | 13 | § 8 IKS |
| Finland | 13 | § 5 Tietosuojalaki |
| France | 15 | Art. 45 LIL |
| Germany | 16 | § 2 Nr. 17 TDDDG |
| Greece | 15 | Art. 21 Law 4624/2019 |
| Hungary | 16 | default |
| Ireland | 16 | Sec. 31 Data Protection Act 2018 |
| Italy | 14 | Art. 2-quinquies D.lgs. 196/2003 |
| Latvia | 13 | Art. 9 FPDP |
| Lithuania | 14 | Art. 8 ADTAĮ |
| Luxembourg | 16 | default |
| Malta | 13 | Reg. 5 SL 586.08 |
| Netherlands | 16 | default |
| Poland | 16 | default |
| Portugal | 13 | Art. 16 Lei n.º 58/2019 |
| Romania | 16 | default |
| Slovakia | 16 | default |
| Slovenia | 16 | default |
| Spain | 14 | Art. 7 LOPDGDD |
| Sweden | 13 | 2 § Kompletterande dataskyddslag |

If the service may be used by children, include:
- Age-appropriate language in the notice
- Description of parental consent mechanism
- How parental consent is verified
- What data is collected from minors
- Whether profiles are created for minors

## Soft Opt-In for Direct Marketing

### Common 3-Condition Test
Most EU/EEA jurisdictions allow email marketing to existing customers without prior consent ("soft opt-in") if **all three** conditions are met:
1. **Existing customer relationship**: The contact details were obtained in the context of a sale or service
2. **Similar products/services**: The marketing concerns the controller's own similar products or services
3. **Easy opt-out**: The customer was given a clear opportunity to object at the time of collection and in every subsequent message

### Jurisdiction Comparison

| Jurisdiction | Legal Provision | Key Differences |
|---|---|---|
| **Germany** | § 7(3) UWG | Strict: own similar products only; opt-out at collection + every email; no third-party marketing |
| **France** | Art. L.34-5 CPCE | Similar to DE; CNIL enforces strictly; B2B prospecting has separate, more permissive regime |
| **Italy** | Art. 130(4) D.lgs. 196/2003 | Soft opt-in recognized; Garante recommends clear disclosure at collection point |
| **UK** | Regulation 22 PECR | Similar to EU; ICO guidance: "similar products" interpreted reasonably |
| **Spain** | Art. 21 LSSI | Soft opt-in available; must clearly identify as commercial communication |

### 5-Step Decision Tree
1. **Was data collected during a sale/service?** → No: consent required (Art. 6(1)(a))
2. **Is the marketing about your own similar products/services?** → No: consent required
3. **Was an opt-out offered at the point of collection?** → No: consent required (and remediate)
4. **Is an opt-out included in every message?** → No: add it (legally required regardless)
5. **All conditions met** → Soft opt-in applies; legal basis: Art. 6(1)(f) GDPR + national implementing provision

### What to Disclose in the Notice
- State that existing customers may receive marketing about similar products/services
- Cite the specific national provision (e.g., § 7(3) UWG, Art. L.34-5 CPCE)
- Explain the right to opt out at any time
- Distinguish from consent-based marketing (newsletters, third-party offers)

## Children's Data — Applicability Decision Logic

### Decision Tree for Determining Applicability

**Step 1: Is the service directed at children?**
- Marketing, content, or design targets minors → children's data rules apply
- Examples: educational platforms, gaming, toy stores, children's apps

**Step 2: Is the service likely to be accessed by children?**
- General audience services accessible without age gate → consider children's rules
- Social media, entertainment, free online games → likely accessed by minors

**Step 3: Is the service exclusively B2B or adult-only?**
- Corporate SaaS, professional services, age-restricted products (alcohol, gambling) → children's rules generally not applicable
- Document the rationale for excluding children's data provisions

**Multi-jurisdiction rule**: When the service operates across multiple Member States, apply the **lowest applicable age threshold** across all target markets. See the age threshold table above.

**Intake trigger conditions** — Ask about children's data when:
- The service is publicly accessible (no B2B gating)
- The target audience includes families or education
- The platform allows user-generated content without age verification
- Products or services are marketed to or commonly used by minors

## Mandatory Disclosures Checklist

### Art. 13 (Data Collected from Data Subject)
- [ ] Controller identity and contact details
- [ ] DPO contact details (if appointed)
- [ ] Processing purposes + legal basis for each
- [ ] Legitimate interests pursued (if Art. 6(1)(f))
- [ ] Recipients or categories of recipients
- [ ] Transfer to third countries + safeguards
- [ ] Retention period or criteria to determine it
- [ ] Right to: access, rectification, erasure, restriction, portability, object
- [ ] Right to withdraw consent (if Art. 6(1)(a))
- [ ] Right to lodge complaint with supervisory authority
- [ ] Whether provision of data is statutory/contractual requirement + consequences of non-provision
- [ ] Existence of automated decision-making including profiling (Art. 22) + meaningful info about logic + significance + envisaged consequences
- [ ] If special categories (Art. 9): specific Art. 9(2) exception identified, dual legal basis disclosed (Art. 6 + Art. 9(2)), additional safeguards mentioned
- [ ] If data to be further processed for another purpose: info about that purpose before further processing

### Art. 14 (Data NOT Collected from Data Subject)
All of the above, PLUS:
- [ ] Categories of personal data concerned
- [ ] Source of the data (and whether publicly accessible)
- [ ] Must be provided within 1 month / at first communication / at first disclosure to recipient

---

## Regulatory horizon (2026)

### EDPB Coordinated Enforcement — Transparency (LIVE, 2026)
On **19 March 2026** the EDPB launched its 2026 Coordinated Enforcement Framework (CEF) action on **transparency and the right to information (Arts. 12–14)**. This is a live, EU-wide enforcement priority for 2026 — supervisory authorities are actively reviewing transparency compliance across the bloc. Treat completeness of the Art. 13/14 disclosures (and the clarity/accessibility duties in Art. 12) as elevated-risk this year: notices generated by this skill should pass the full Art. 13/14 checklist above with no gaps.

### Digital Omnibus — reduced transparency (PROPOSED, not in force)
The Commission's Digital Omnibus (COM(2025) 833 final, 19 November 2025) proposes to **reduce** the Art. 13/14 transparency burden in limited cases (e.g. data obtained from the data subject who is likely already informed, low-intensity processing, no automated decision-making or high-risk processing or transfer). This is a proposal in the ordinary legislative procedure as of 2026-05-31 — **not law**. Apply the full Art. 13/14 obligations; flag the proposal only as forward planning.
