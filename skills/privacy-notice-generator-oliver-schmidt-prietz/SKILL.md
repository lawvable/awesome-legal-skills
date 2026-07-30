---
name: gdpr-privacy-notice-eu-oliver-schmidt-prietz
description: |
  Draft GDPR/DSGVO-compliant privacy notices as .docx for any EU/EEA jurisdiction and audience. Use when user asks to create a privacy policy/notice, mentions "Datenschutzerklärung", "politique de confidentialité", "privacy notice", needs Art. 13/14 disclosures, AI Act transparency, cookie policy, or notices for applicants ("Bewerber-Datenschutz"), employees ("Beschäftigten-Datenschutz"), B2B partners, or B2C customers. Covers DE (DSGVO+BDSG+TDDDG), FR (RGPD+LIL+LCEN), AT, IT, ES, NL, BE, IE, UK GDPR. Five notice types: Website/App, Applicant, Employee, Business Partner, B2C Customer.
metadata:
  author: Oliver Schmidt-Prietz
  license: AGPL-3.0
  version: 2026.06.05
---

# Pan-EU GDPR Privacy Notice Generator

Generate jurisdiction-aware, GDPR-compliant privacy notices as professional .docx documents.

## Workflow Overview

```
1. SCOPE    → Notice type, jurisdiction(s), template choice
2. INTAKE   → Type-driven collection: controller info, data inventory, legal bases
3. DRAFT    → Generate notice from template + type profile + collected info
4. VERIFY   → Art. 13/14 compliance check + type-specific checks + AI Act check
5. DELIVER  → .docx output via docx skill
```

## Step 1: Scope, Notice Type & Template Selection

### Determine Notice Type (FIRST QUESTION)

Before anything else, determine what type of privacy notice is needed. Load `references/NOTICE_TYPES.md` and ask:

> "What type of privacy notice do you need?"

| Type | Description |
|---|---|
| **Website / App** | For visitors, users, subscribers of a website, web app, or mobile app |
| **Applicant / Recruiting** | For job applicants and candidates (Bewerber, candidats) |
| **Employee** | For employees, contractors, interns (Beschäftigte, salariés) |
| **Business Partner (B2B)** | For contact persons at vendors, suppliers, clients, partners |
| **B2C Customer** | For end consumers in a customer/purchase relationship |
| **Combined** | Multiple audiences in one or several linked notices |

The selected type determines:
- Which sections to include/skip in the final document
- Which data categories to probe during intake
- Which legal bases are most likely
- Which type-specific intake questions to ask
- Which retention defaults apply

Refer to `references/NOTICE_TYPES.md` for the full **section map**, **data profile**, **legal bases**, **intake questions**, and **retention defaults** for each type.

### Determine Jurisdiction

Ask which countries/markets the service targets. Load the appropriate reference:

| Target Market | Reference File |
|---|---|
| Germany / DACH | `references/DE.md` |
| France | `references/FR.md` |
| Other EU (AT, IT, ES, NL, BE, IE, UK) | `references/OTHER_EU.md` |
| Always load | `references/EU_COMMON.md` |

For multi-jurisdiction services, load all relevant files and note where requirements differ (e.g., children's age thresholds, DPO thresholds, retention rules).

### Template Selection

Ask the user:

> "I will draft the privacy notice as a professional .docx document. Do you have an existing template or privacy notice I should use as a base? If not, I will use one of our pre-built templates."

| Option | Action |
|---|---|
| User provides template | Use their .docx as base — preserve structure, wording, and formatting; only fill/adapt |
| No user template | Generate from `references/templates.md` using the docx skill |

`references/templates.md` includes: 13-section structure, Art. 21 objection box (visually highlighted), purposes/retention table, cookie table, AI/automated decision-making section, children's data section, proper header/footer with page numbers, A4 formatting, TOC, and full translations for DE, FR, and EN. Select the language matching the target jurisdiction.

**If user provides a template**: faithfully preserve its structure and validated wording. Only replace placeholders and adapt to the specific case. Do NOT rewrite validated legal language.

### Multi-Language Decision Tree

If the service targets multiple jurisdictions or language groups, determine the language approach:

| Scenario | Approach |
|---|---|
| **Single market, single language** | One notice in the market's language (e.g., DE only → German) |
| **Single market, international workforce/users** | Primary language + English version. State which version governs in case of conflict. |
| **Two markets, two languages** | Option A: Two separate notices (one per language), each self-contained. Option B: Bilingual notice with clear visual separation (e.g., side-by-side columns or sequential sections). |
| **Pan-EU / many markets** | English as primary + translations for key markets. Each translation should be a standalone notice, not a partial translation. |
| **Swiss company (nDSG + GDPR)** | Address both the Swiss nFADP (new Federal Act on Data Protection) and GDPR. Typical approach: single notice referencing both regimes, in at least German + French (+ Italian if applicable). Note: nFADP has no consent requirement for general processing but requires information duties similar to Art. 13/14 GDPR. |

**Template handling for bilingual documents**:
- Use the primary-language template as the structural base
- Ensure both language versions contain all mandatory disclosures (a translation gap = a compliance gap)
- Mark the governing language version explicitly (e.g., "In case of discrepancies, the [German/French] version shall prevail.")

**Multi-language verification checklist** (add to Step 4 if applicable):
- [ ] All mandatory Art. 13/14 disclosures present in each language version
- [ ] Governing version clearly identified
- [ ] Legal terminology correctly translated (not machine-translated without review)
- [ ] Supervisory authority information correct for each jurisdiction
- [ ] Jurisdiction-specific requirements addressed in the relevant language version

### Platform Sub-Type (Website/App type only)

If the notice type is **Website / App**, further classify the platform to anticipate data categories. See `references/NOTICE_TYPES.md` → "Website / App" → "Sub-Types & Data Profiles" for details.

| Sub-Type | Typical Additional Data |
|---|---|
| Brochure/corporate site | Contact forms, analytics, cookies only |
| E-commerce | Account, payment, order history, shipping, returns |
| SaaS / Web app | Account, usage data, feature logs, API keys, collaboration data |
| Mobile app | Device ID, push tokens, permissions (camera, location, contacts), app usage |
| Marketplace | Dual roles (buyers/sellers), ratings, messaging, payment escrow |
| Platform with AI features | Training data, AI inputs/outputs, model decisions, profiling |

## Step 2: Information Intake

Collect ALL information before drafting. Use the **type profile** from `references/NOTICE_TYPES.md` to guide the intake — each type pre-defines likely data categories, legal bases, and type-specific questions.

Ask in logical groups, not all at once. Start with Group A (always), then use the type profile to determine which categories to probe and which type-specific questions to ask.

### Group A — Controller Identity
- Company name, legal form, registration number
- Registered address
- Legal representative (name + title)
- Contact email + phone
- DPO appointed? → Contact details (use functional email)

### Group B — Data Inventory
For each collection point (forms, account creation, purchase, cookies, app usage):
- What data is collected?
- Is it mandatory or optional?
- What is the source (direct from user, third party, automated)?

Categories to probe:
- **Identity**: name, email, phone, address, date of birth, photo
- **Account**: credentials, preferences, settings, activity history
- **Technical**: IP, device ID, browser fingerprint, logs
- **Browsing**: pages visited, clicks, session duration, referrer
- **Transaction**: orders, payment method (via provider), invoices
- **Communication**: messages, support tickets, comments
- **Special categories** (Art. 9): health, biometric, political, religious, sexual orientation, ethnic origin, trade union, genetic — **If any Art. 9 data is identified**: consult `EU_COMMON.md` → "Special Category Data (Art. 9)" for the full intake protocol. Determine the Art. 9(2) exception for each category, confirm the dual legal basis (Art. 6 + Art. 9(2)), and document additional safeguards. Common triggers by notice type: Employee (church tax, disability, sick leave, union dues), Applicant (disability, health, religion), B2C (health data for pharmacy/insurance/fitness).
- **AI-related**: inputs to AI systems, AI-generated outputs, automated scores/decisions

### Group C — Purposes & Legal Bases
For each processing activity, determine the legal basis. Reference `EU_COMMON.md` for guidance.

Present as a table for the user to confirm:

| Purpose | Legal Basis | Data Categories |
|---|---|---|
| Service provision / contract execution | Art. 6(1)(b) | [to fill] |
| Account management | Art. 6(1)(b) | [to fill] |
| Legal/tax compliance | Art. 6(1)(c) — [specific law] | [to fill] |
| Analytics | Art. 6(1)(f) or consent | [to fill] |
| Marketing / newsletter | Art. 6(1)(a) consent | [to fill] |
| AI-based processing | [determine per use case] | [to fill] |

### Group D — Recipients & Transfers
- Hosting provider + location
- Payment processor
- Analytics tools
- Email/marketing tools
- CRM / support tools
- AI/ML service providers (e.g., OpenAI, Google AI, Anthropic)
- Any other processors
- Transfers outside EU/EEA → which countries, which mechanism (adequacy, SCCs, DPF, BCRs)

**DPA / Art. 28 Cross-Reference** — For each processor identified:
- Verify a Data Processing Agreement (Art. 28 GDPR) is in place. If not, flag as a **compliance gap** requiring remediation before the notice is finalized.
- **What to disclose in the notice**: processor name (or category), purpose, location, transfer mechanism. Do NOT include DPA terms, sub-processor lists, or TOMs in the privacy notice — these belong in the Art. 28 agreement.
- **What NOT to disclose**: specific technical/organizational measures (Art. 32), sub-processor chains, pricing, SLA details.
- If the user confirms no DPA exists for a processor: note this in the summary and recommend immediate remediation. The privacy notice should still name the processor/category but add a note that the controller is in the process of formalizing the agreement.
- Joint controllership (Art. 26): if applicable, the arrangement's essence must be disclosed in the notice, including respective responsibilities and the contact point for data subjects.

### Group E — Cookies & Tracking
- Cookie categories used (essential, analytics, marketing, social)
- Specific tools (Google Analytics, Meta Pixel, Matomo, HubSpot, etc.)
- CMP solution (Usercentrics, Cookiebot, Axeptio, Didomi, Borlabs, etc.)
- Server-side tracking? Fingerprinting?
- Cookie lifespans

### Group F — AI & Automated Processing
If the service uses AI/ML:
- What AI systems are used and for what purpose?
- Are decisions solely automated or human-in-the-loop?
- Do decisions produce legal or similarly significant effects (Art. 22)?
- Is user data used for model training?
- AI Act classification: prohibited / high-risk / limited-risk / minimal-risk?

### Group G — DPIA Indicators (Art. 35 GDPR)

Check whether a Data Protection Impact Assessment may be required. If **2 or more** of the following indicators apply, inform the user and recommend a DPIA as a separate deliverable:

1. **Systematic evaluation/scoring** of individuals (profiling, credit scoring, performance reviews)
2. **Automated decision-making** with legal or similarly significant effects (Art. 22)
3. **Systematic monitoring** of a publicly accessible area (CCTV, Wi-Fi tracking)
4. **Special category data** or criminal offence data processed at scale (Art. 9/10)
5. **Large-scale processing** of personal data (high volume, broad geographic scope, many data subjects)
6. **Matching or combining datasets** from different sources in ways data subjects would not reasonably expect
7. **Vulnerable data subjects** (employees, children, patients, elderly)
8. **Innovative use of technology** (biometrics, AI/ML, IoT, blockchain for personal data)

**If 2+ indicators are flagged**:
- Inform the user: "Based on the processing activities described, a Data Protection Impact Assessment (DPIA) under Art. 35 GDPR appears to be required."
- Explain the notice implications: the privacy notice should reference that a DPIA has been conducted (without disclosing the DPIA content itself)
- Recommend: "A DPIA is a separate compliance exercise and should be conducted before the processing begins. This privacy notice skill can draft the notice, but the DPIA should be prepared as a standalone document."
- Check national mandatory DPIA lists (DE: DSK-Liste; FR: CNIL list of processing operations requiring DPIA)

### Summary Before Drafting

After collection, produce a structured summary for user confirmation:

```
NOTICE TYPE: [Website / Applicant / Employee / B2B / B2C / Combined]
CONTROLLER: [Name, form, address]
JURISDICTION(S): [Countries]
PLATFORM: [Type / Sub-type if website]
DPO: [Yes/No + contact]
DATA CATEGORIES: [List by collection point]
PURPOSES + BASES: [Table]
PROCESSORS: [List with locations]
TRANSFERS: [Countries + mechanisms]
COOKIES: [Categories + tools + CMP — if applicable per type]
AI PROCESSING: [Yes/No + details]
RETENTION: [Key periods — cross-check with type defaults]
SPECIFICS: [Anything unusual]
SECTIONS TO INCLUDE: [Based on type section map]
SECTIONS TO SKIP: [Based on type section map]
```

Confirm with user before proceeding to draft.

## Step 3: Draft the Notice

### Section Selection by Type

Use the **section map** from `references/NOTICE_TYPES.md` for the selected notice type. Only include sections marked ✅ or ⚠️ (if applicable). Skip sections marked ❌. This avoids irrelevant content (e.g., cookie tables in an applicant notice).

For **combined notices** covering multiple audiences, see `references/NOTICE_TYPES.md` → "Combined Notices" for structural options (single comprehensive, separate, or layered).

### Standard Structure (full — adapt per type)

```
PRIVACY NOTICE / DATENSCHUTZERKLÄRUNG / POLITIQUE DE CONFIDENTIALITÉ
[Company Name]
Last updated: [DATE]

1. WHO WE ARE (Controller identity + DPO)
2. WHAT DATA WE COLLECT (by category, with source + mandatory/optional)
3. WHY WE PROCESS YOUR DATA (purposes + legal bases table, incl. retention per purpose)
4. WHO RECEIVES YOUR DATA (recipients + processors)
5. INTERNATIONAL TRANSFERS (countries + safeguards)
6. HOW LONG WE KEEP YOUR DATA (retention table — can be merged with section 3)
7. YOUR RIGHTS (all applicable rights + exercise procedure)
8. COOKIES & TRACKING (categories + management + CMP reference)
9. AI & AUTOMATED DECISIONS (if applicable — Art. 22 + AI Act)
10. DATA SECURITY (general measures, no sensitive technical details)
11. CHILDREN'S DATA (if applicable — age threshold + mechanism)
12. CHANGES TO THIS NOTICE (notification method)
13. CONTACT (email + postal + form link)
```

### Drafting Rules

- **Language**: Write in the jurisdiction's language. For multi-jurisdiction, primary language first with clear indication of governing version.
- **Tone**: Address the reader as "you"/"Sie"/"vous". Clear, accessible language — understandable by non-lawyers.
- **Art. 21 Right to Object**: Must be presented **prominently and separately** from other rights (GDPR Art. 21(4)). In German notices, a separate "WIDERSPRUCHSRECHT" section is standard practice.
- **Legal bases**: Cite article numbers precisely (e.g., "Art. 6(1)(f) DSGVO" not just "legitimate interest").
- **Retention periods**: Use specific durations with legal justification, not vague language.
- **AI disclosure**: If AI is used, include a dedicated section even if Art. 22 doesn't strictly apply — the AI Act requires transparency.
- **Tables**: Use tables for purposes/bases/retention and for cookie categories. They improve readability.
- **No internal references**: The final document must not contain references to this skill, CNIL guides, or other drafting aids.

## Step 4: Compliance Verification

Before delivery, perform a structured final check in this order:

**1. Re-read the jurisdiction reference(s)** loaded in Step 1 (DE.md, FR.md, OTHER_EU.md). Cross-check:
- Supervisory authority name, address, and URL are correct for the controller's registered seat
- Retention periods match jurisdiction-specific legal citations (not just generic defaults)
- Standard wording blocks (Art. 21 objection, complaint right, controller intro) use the jurisdiction's validated language from the reference file
- Any jurisdiction-specific requirements not yet addressed (e.g., § 26 BDSG for DE employee/applicant, Art. L.34-5 CPCE for FR marketing)

**2. Verify Art. 13/14 mandatory disclosures** against `EU_COMMON.md` → "Mandatory Disclosures Checklist". Every item must be present or explicitly not applicable with reason.

**3. Additional checks:**

- [ ] Art. 21 right to object presented separately and prominently
- [ ] Correct supervisory authority named (check jurisdiction reference)
- [ ] DPO contact included if DPO appointed
- [ ] Cookie section matches actual cookie usage (if included per type)
- [ ] Retention periods are specific (not "as long as necessary" without criteria)
- [ ] Transfer mechanisms match actual processor locations
- [ ] AI/automated decision-making addressed if applicable
- [ ] Children's data addressed if service accessible to minors
- [ ] Special category data (Art. 9): dual legal basis disclosed (Art. 6 + Art. 9(2)), specific exception identified, additional safeguards mentioned
- [ ] Language matches target jurisdiction
- [ ] No placeholder text remaining ([...], ___, TODO)
- [ ] Update date present
- [ ] Sections match the type's section map (no irrelevant sections, no missing required sections)

**4. Type-specific checks** (from `references/NOTICE_TYPES.md`):

**Applicant**: § 26 BDSG referenced (DE)? Talent pool consent separate? Retention ≤ 6 months post-rejection unless consent? Art. 14 used if data from recruiters?

**Employee**: § 26 BDSG as primary basis (DE)? Works council mentioned if relevant? IT monitoring disclosed? Complex retention chain complete?

**B2B**: Art. 14 disclosure if data not from data subject directly? Source of data disclosed? Contact person vs. contracting entity distinction clear?

**B2C Customer**: Soft opt-in conditions met (DE: § 7(3) UWG)? Payment processor disclosed? Loyalty program terms clear? Profiling disclosed if applicable?

**5. AI Act compliance** (if AI features present):
- [ ] Users informed they interact with AI (Art. 50 AI Act)
- [ ] AI-generated content disclosed where applicable
- [ ] High-risk AI: transparency obligations met
- [ ] Link between Art. 22 GDPR rights and AI system disclosed

## Step 5: Deliver as .docx

Generate the final document using the docx generation skill (`/mnt/skills/public/docx/SKILL.md` in Claude.ai Projects, or the `docx-processing-anthropic` skill in Claude Code). If no docx skill is available, generate well-formatted Markdown as fallback.

### Document Formatting Standards

- **Page size**: A4 (standard for EU documents)
- **Font**: Arial or Calibri, 11pt body, headings proportionally larger
- **Margins**: 2.5 cm all sides (EU standard) = 1417 DXA
- **Structure**: Numbered headings (1., 2., 3...), table of contents for documents > 3 pages
- **Tables**: Light borders, header row shaded, readable cell padding
- **Header**: Company name or "Privacy Notice"
- **Footer**: Page numbers, "Last updated: [DATE]"

Read the docx skill instructions before generating the file. Use `docx-js` for new documents. Follow all critical rules from the docx skill (DXA widths, LevelFormat.BULLET for lists, ShadingType.CLEAR for tables, etc.).

### Delivery

Present the .docx file with:
1. Brief confirmation of what was included
2. Any open questions or assumptions made
3. Recommendation for legal review before publication

> **IMPORTANT**: Always recommend that the user has the notice reviewed by qualified legal counsel before publication. This tool assists in drafting — it does not replace legal advice.

### Post-Generation Checklist & Approval Workflow

Present the following checklist to the user to guide their internal review and publication process:

**Legal Review**:
- [ ] Privacy notice reviewed by qualified data protection counsel / DPO
- [ ] All legal bases confirmed as appropriate for the specific processing activities
- [ ] Retention periods verified against current legal requirements
- [ ] Transfer mechanisms confirmed as valid and up-to-date (especially DPF certifications, SCC versions)
- [ ] Art. 9 special category processing: dual legal basis and safeguards reviewed

**Technical Review**:
- [ ] All processors and tools listed are actually in use (no outdated entries)
- [ ] Cookie table matches actual cookies set by the website (audit with browser dev tools)
- [ ] Data flows match the technical architecture (verify with IT/engineering)
- [ ] Contact details (email, postal, DPO) are correct and monitored

**Translation QA** (if multi-language):
- [ ] Each language version reviewed by a native speaker with legal expertise
- [ ] Legal terminology verified (not raw machine translation)
- [ ] All versions contain identical substantive content
- [ ] Governing version clearly marked

**Publication Requirements**:
- [ ] Notice accessible within 2 clicks from any page (DE: BGH requirement)
- [ ] Linked in website footer / app settings / onboarding flow as appropriate
- [ ] Previous version archived with effective date (for audit trail)
- [ ] Cookie banner / CMP updated to reference the current privacy notice
- [ ] Employees / applicants notified of updated notice (if applicable)

**Ongoing Review Triggers** — Recommend the user reviews the notice when:
- New processors or tools are introduced
- New processing purposes are added
- Legal framework changes (new adequacy decisions, court rulings, regulatory guidance)
- Company undergoes a merger, acquisition, or restructuring
- A data breach occurs that reveals undisclosed processing
- At minimum: annual review

## Cross-References

- **Breach response**: If the user also needs breach notification procedures, reference the `breach-sentinel` skill
- **DPIA**: If processing is likely high-risk, recommend a Data Protection Impact Assessment (Art. 35 GDPR) as a separate exercise
- **Cookie policy**: Can be integrated in the privacy notice or a separate document — ask the user's preference

## Writing Style Guide

| Do | Avoid |
|---|---|
| "you" / "your data" / "Sie" / "Ihre Daten" | "the user" / "the data subject" / "der Betroffene" |
| Short, clear sentences | Dense legal paragraphs |
| Specific examples for complex processing | Vague language ("various data", "diverse Daten") |
| Tables for structured information | Walls of text for purposes/retention |
| Precise article references | Generic "in accordance with applicable law" |
| Active voice | Passive constructions where avoidable |
| Plain language with legal precision | Either pure legalese or oversimplified language |

## Related GDPR skills

This skill works standalone, but pairs well with my other EU data-protection skills — install any on its own or combine them:

- **DPIA Sentinel** — Art. 35 Data Protection Impact Assessments
- **GDPR Breach Sentinel** — Art. 33/34 breach response & notification
- **Transfer Impact Assessment (TIA)** — Chapter V transfer assessments
- **DPA Art. 28** — controller–processor agreements (AVV)
- **Legitimate Interest** — Art. 6(1)(f) LIA / balancing test
