---
name: eu-data-act-compliance
description: Assess obligations under Regulation (EU) 2023/2854 for connected products, related services, statutory B2B data sharing, unfair data-contract terms, exceptional-need B2G requests, data-processing-service switching, international governmental access, interoperability, smart contracts, enforcement, and non-EU representatives. Use for Data Act scope analysis, gap assessments, product and service design, request handling, contract review, cloud exit planning, or cross-regulation mapping.
---

# EU Data Act Compliance Assessment

Perform a source-grounded assessment under Regulation (EU) 2023/2854. Separate enacted legal requirements from guidance, national law, contractual choices, and implementation recommendations.

This skill is not legal advice. Escalate unresolved interpretation, national enforcement, trade-secret refusal, personal-data processing, and authority-response decisions to qualified counsel.

## Source and Evidence Protocol

1. Start with the current consolidated text on EUR-Lex. Record the ELI/CELEX identifier, consolidation date, language, and access date.
2. Cite the controlling article and paragraph for each legal conclusion. Read the full provision before asserting that a duty, exception, right, or remedy does not exist.
3. Label every proposition as one of:
   - **Law:** binding text in Regulation (EU) 2023/2854 or another identified legal act.
   - **Official guidance:** Commission or competent-authority material, not the Regulation itself.
   - **National overlay:** applicable national legislation, authority designation, procedure, or penalty.
   - **Implementation recommendation:** operational advice, not a statutory requirement.
   - **Open question:** missing fact or unresolved interpretation.
4. Never infer a legal rule from a heading, recital, search miss, summary page, draft bill, or template alone.
5. Quote sparingly. Prefer an accurate paraphrase tied to the exact provision.

Authoritative starting points:

- Regulation (EU) 2023/2854, ELI: `http://data.europa.eu/eli/reg/2023/2854/oj`
- Commission Data Act page: `https://digital-strategy.ec.europa.eu/en/policies/data-act`
- Commission register of competent authorities and national penalty measures, where available

## Controlling Dates

| Event | Date | Authority |
|---|---:|---|
| Entry into force | 11 January 2024 | Article 50 |
| General application | 12 September 2025 | Article 50 |
| Article 3(1) design obligation for connected products and related services placed on the market after this date | 12 September 2026 | Article 50 |
| Chapter IV applies to qualifying legacy contracts | 12 September 2027 | Article 50 |
| Switching charges prohibited | 12 January 2027 | Article 29(1) |

Do not rewrite the 12 September 2026 rule as a product-design date. It is tied to when the connected product or related service is placed on the market.

## Assessment Workflow

Follow the steps in order. Stop and identify missing evidence instead of filling factual gaps with assumptions.

### 1. Fix the unit of analysis

Identify:

- legal entity and establishment;
- product, related service, data-processing service, contract, or request being assessed;
- relevant market and user location;
- assessment date and legal-text version;
- data flows, contractual chain, technical control, and actual data availability.

Do not assess an enterprise in the abstract when different products or services create different roles.

### 2. Assign roles using Article 2 and Article 1(3)

Assess each role independently:

| Role | Anchor | Core test |
|---|---|---|
| User | Article 2(12) | Owns the connected product, has temporary contractual use rights, or receives related services |
| Data holder | Article 2(13) | Has a legal right or obligation to use and make data available |
| Data recipient | Article 2(14) | Receives data in a professional capacity and is not the user |
| Provider of a related service | Articles 2(6), 3(3) | Provides qualifying software or digital service linked to product functions |
| Provider of a data processing service | Article 2(8) | Provides qualifying on-demand network access to scalable and elastic computing resources |
| Public sector body | Article 2(28) | Qualifying Member State authority, public-law body, or association |
| Smart-contract vendor or deployer for others | Articles 1(3)(g), 36 | Supplies or professionally deploys a smart contract used to execute a data-sharing agreement |

The Regulation does not define “manufacturer” in Article 2. For product-facing duties, identify who designs or manufactures the connected product and who is the seller, rentor, lessor, or related-service provider under Article 3.

Apply territorial scope from Article 1(3). Non-EU establishment does not by itself remove an entity from scope. Check the legal-representative duty in Article 37(11) to (13).

Read `references/scope-assessment.md`.

### 3. Classify the data and applicable chapter

Record:

- personal, non-personal, or mixed data;
- product data under Article 2(15), related service data under Article 2(16), and relevant metadata;
- readily available data under Article 2(17);
- content versus data concerning performance, use, or environment;
- raw or pre-processed data versus inferred or derived information;
- trade-secret status and identity of the trade-secret holder;
- security, intellectual-property, confidentiality, and sector restrictions.

Chapter II covers product and related-service data within Article 1(2)(a), not every record associated with a product. Do not assume all analytics or inferred information are readily available data.

For personal data, the GDPR and ePrivacy rules continue to apply and prevail in a conflict under Article 1(5). A Data Act access right is not itself a universal GDPR lawful basis.

### 4. Test the Chapter II product and service duties

#### Access by design and pre-contract information

- Article 3(1): design and provide connected products and related services so relevant data and metadata are, by default, easily, securely, and free of charge available in the required format and, where relevant and technically feasible, directly accessible.
- Article 3(2): seller, rentor, or lessor gives the listed information before a purchase, rent, or lease contract.
- Article 3(3): related-service provider gives the listed information before the related-service contract.

#### User access

If direct access is unavailable, Article 4(1) requires the data holder, on a simple request where technically feasible, to make readily available data and relevant metadata accessible without undue delay, at the same quality available to the holder, easily, securely, free of charge, and in a comprehensive, structured, commonly used, machine-readable format. Continuous and real-time access applies only where relevant and technically feasible.

#### User-directed third-party sharing

Article 5(1) requires comparable access for an eligible third party requested by the user, subject to Articles 8 and 9. A DMA gatekeeper is not an eligible third party under Article 5(3). Article 6 governs how the recipient may use and further disclose the data.

#### Exceptions and safeguards

- Security restrictions: Article 4(2), with the required competent-authority notification.
- User trade secrets: Article 4(6) to (9).
- Third-party trade secrets: Article 5(9) to (12).
- Personal data: Articles 4(12) and 5(7).
- Chapter II enterprise exception: Article 7(1). This is tied to data generated by products manufactured or designed, or related services provided, by qualifying micro or small enterprises, subject to linked-enterprise and subcontracting conditions. It is not a general exemption for every small data holder.

Read `references/data-access-rights.md`.

### 5. Test B2B data-sharing conditions

Where a data holder must make data available to a business recipient under Article 5 or other qualifying law:

- use fair, reasonable, non-discriminatory, and transparent terms under Article 8;
- do not impose contractual terms that Article 8(2), Article 12(2), or Article 13 makes non-binding;
- assess compensation under Article 9, not under a fabricated frequent-or-complex-request rule;
- for an SME or qualifying not-for-profit research recipient without non-SME linked or partner enterprises, compensation cannot exceed the Article 9(2)(a) making-available costs;
- provide the calculation basis in sufficient detail under Article 9(7).

Article 9 governs B2B compensation between data holder and data recipient. It does not permit charging the user for Article 4 or Article 5 access.

### 6. Review unilaterally imposed B2B data terms

Article 13 applies to specified data-access, data-use, liability, and remedy terms unilaterally imposed by one enterprise on another.

Use the correct structure:

- Article 13(1): an unfair, unilaterally imposed term is not binding.
- Article 13(2): terms reflecting mandatory or default Union law are not unfair.
- Article 13(3): general unfairness standard.
- Article 13(4): terms that are unfair.
- Article 13(5): terms presumed unfair.
- Article 13(6): unilateral-imposition test and burden of proof.
- Article 13(7) to (9): severability, exclusions, and non-derogation.

There is no Article 13 safe harbor. Commission model terms under Article 41 are non-binding.

Read `references/unfair-terms-catalogue.md`.

### 7. Validate exceptional-need B2G requests

Use the sequence in Articles 14 to 22:

1. Article 14: confirm the requester and data holder are covered.
2. Article 15: identify the exceptional need.
3. Article 17: validate the request’s content, specificity, proportionality, legal-task basis, deadline, and publication/notification steps.
4. Article 18: calculate the response or challenge deadline and test only the listed grounds to decline or seek modification.
5. Articles 19 and 21: control use, security, erasure, trade secrets, and permitted onward sharing.
6. Article 20: determine compensation.

For a public emergency, qualifying non-micro and non-small data holders provide data free of charge under Article 20(1). Micro and small enterprises can claim compensation through Article 20(3). For Article 15(1)(b) requests, Article 20(2) generally allows technical and organisational costs plus a reasonable margin, subject to the official-statistics exception in Article 20(4).

Read `references/b2g-data-sharing.md`.

### 8. Assess data-processing-service switching

For services within Article 2(8) and Article 1(3)(f):

- Articles 23 and 24: identify covered services and obstacles;
- Article 25: check written contract terms, maximum two-month notice, maximum 30-calendar-day transition, exceptions, minimum 30-calendar-day retrieval period, erasure, exportable-data categories, and assistance;
- Article 26: check switching information and online register;
- Article 27: check good-faith cooperation;
- Article 28: check website disclosure on international access and transfer;
- Article 29: apply the switching-charge timeline;
- Article 30: assess technical duties by service type;
- Article 31: test custom-built and non-production exceptions;
- Article 32: assess third-country governmental access to non-personal data held in the Union.

Article 24 does not set a notice period. The maximum two-month notice and the transition rules are in Article 25.

Read `references/cloud-switching.md`.

### 9. Assess smart contracts

Article 36 applies to smart contracts used to execute data-sharing agreements. Check:

- robustness and access control;
- safe termination and interruption;
- data archiving and continuity;
- governance-layer and smart-contract-layer access control;
- consistency with the data-sharing agreement;
- conformity assessment and EU declaration of conformity.

Do not cite Articles 30 or 31 for these duties.

### 10. Map enforcement and remedies

- Article 10: certified dispute settlement for specified disputes. Decisions bind only with prior explicit consent.
- Article 37: competent authorities, data coordinator, jurisdiction, legal representative, and authority powers.
- Article 38: complaint.
- Article 39: effective judicial remedy.
- Article 40: Member State penalties and specified GDPR-linked fine powers.
- Article 41: non-binding Commission model terms and cloud clauses.

Verify current authority designations and national penalties from official sources at the assessment date. Do not state a draft bill as enacted law.

### 11. Integrate adjacent regimes

Map, do not merge:

- GDPR and ePrivacy for personal data and terminal-equipment access;
- sector data-access law and Article 43 priority rules;
- Trade Secrets Directive and Data Act-specific safeguards;
- Digital Markets Act gatekeeper status;
- Cyber Resilience Act and sector security law;
- AI Act where data feeds an AI system;
- consumer, competition, intellectual-property, employment, and secrecy law;
- Data Governance Act where an intermediary or data-altruism structure is used.

Check current consolidated texts and application dates for every adjacent regime. Read `references/cross-regulation-mapping.md` and `references/dach-specific.md`.

## Mandatory Output

Deliver one assessment with these sections:

1. **Executive conclusion:** in scope, out of scope, or unresolved, with the three most material risks.
2. **Facts and assumptions:** entity, product/service, data, geography, contracts, and missing facts.
3. **Role and chapter matrix:** each role, factual basis, article, confidence, and evidence.
4. **Requirement matrix:** provision, binding rule, present state, evidence, gap, owner, due date, and confidence.
5. **Request or contract findings:** exact clause/request, legal test, result, and remediation.
6. **Cross-regulation conflicts:** GDPR and other overlays, with separate legal bases.
7. **Action plan:** prioritized remediation, validation step, and decision owner.
8. **Source register:** official URL, instrument/version, provision, access date, and proposition supported.

Use confidence labels:

- **High:** controlling text and material facts are clear.
- **Medium:** law is clear but a material fact or national overlay is incomplete.
- **Low:** interpretation, scope, or evidence is genuinely unresolved.

Use `references/templates.md` for reusable matrices and response structures.

## Quality Gate

Before finalizing, confirm:

- [ ] Every role uses the correct Article 2 definition or a clearly described functional duty.
- [ ] Article 3(1), (2), and (3) are not reversed.
- [ ] Article 7 is not stated as a general small-data-holder exemption.
- [ ] Article 9 compensation is not based on request frequency or complexity.
- [ ] Article 13 uses paragraphs 3, 4, and 5 correctly and no safe harbor is claimed.
- [ ] B2G grounds, response deadlines, and compensation match Articles 15, 18, and 20.
- [ ] Cloud notice, transition, retrieval, and charge dates match Articles 25 and 29.
- [ ] Smart-contract duties cite Article 36.
- [ ] Authorities, complaints, remedies, and representatives cite Articles 37, 38, and 39 correctly.
- [ ] Personal-data processing has a separately identified GDPR basis.
- [ ] Negative legal claims are based on the full provision, not a failed search.
- [ ] National-law and guidance statements have current official sources and dates.

## Reference Files

| File | Use |
|---|---|
| `references/scope-assessment.md` | Roles, territorial scope, enterprise conditions, chapter routing |
| `references/data-access-rights.md` | Articles 3 to 12, access, sharing, safeguards, compensation |
| `references/unfair-terms-catalogue.md` | Article 13 contract review |
| `references/b2g-data-sharing.md` | Articles 14 to 22 request review |
| `references/cloud-switching.md` | Articles 23 to 32 cloud switching and international access |
| `references/cross-regulation-mapping.md` | GDPR and adjacent EU-law mapping |
| `references/dach-specific.md` | Germany, Austria, and Switzerland verification framework |
| `references/templates.md` | Assessment, request, contract, and source-register templates |

## Disclaimer

This skill supports structured compliance analysis. It does not determine disputed facts, replace qualified legal advice, or guarantee an authority or court outcome. Obtain legal review before refusing access, disclosing trade secrets or personal data, responding to an authority, launching a regulated product, or relying on a national-law position.
