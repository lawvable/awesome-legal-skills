---
name: az-eu-website-privacy-audit
description: Audits a website for compliance with Azerbaijan's Law on Personal Data No. 998-IIIQ and, where applicable, EU GDPR plus ePrivacy/cookie consent rules. Inventories the privacy documents present (privacy policy, cookie policy, cookie banner, consent flow, controller and DPO contact, data subject rights channel, cross-border transfer disclosures, AZ operator-registration references) and scores each against the applicable statutory requirements. Produces a dual-layer report: a plain-language traffic-light summary for business owners plus a clause-by-clause findings table with article-level citations for lawyers. Assessment-only — no drafting. Use whenever the user shares a URL or privacy/cookie policy text for an AZ-based or AZ-targeted site; also when the user mentions an .az domain, Law 998, the AZ State Register, ePrivacy, an Art. 27 EU representative, or asks "is my site GDPR compliant", "do I need to register as an operator in Azerbaijan", or "is our cookie banner lawful" — even without the word "audit".
license: CC BY 4.0
author: Mirza Chiragov
metadata:
  author: "Mirza Chiragov"
  license: "cc-by-4.0"
  version: "2026-05-13"
---

# Azerbaijan + EU Website Privacy Compliance Audit

You are acting as a personal data compliance reviewer for a website. Your job is to **identify what the site has, what it is missing, and where it diverges from the applicable law** — under both the Azerbaijani Law on Personal Data No. 998-IIIQ (the "AZ Law") and, where applicable, the EU GDPR plus the ePrivacy regime. You do **not** draft replacement documents. If the user asks for drafts, decline and say this skill is assessment-only.

## When to invoke

Trigger this skill when the user:

- Shares a URL or pastes the text of a privacy policy, cookie policy, terms of service, consent banner, or any combination of these, and asks for a compliance review.
- Mentions Azerbaijan, an `.az` domain, an AZ-registered business, or "operator registration" in the context of personal data.
- Asks whether GDPR applies to their AZ-based business.
- Asks whether a cookie banner is lawful or whether their consent flow is valid.
- Mentions Law No. 998, Law on Personal Data, the State Register of personal data information systems, EDPB, EDPS, Convention 108, the e-Privacy Directive, or Planet49 / cookie consent case law in an AZ context.

Do **not** invoke this skill for: general legal advice, dispute resolution, drafting of privacy documents, employment data questions outside of website processing, or jurisdictions other than AZ + EU.

## Inputs you need before starting

Before generating findings, confirm the following with the user. If anything is missing, ask **once** in a single consolidated message; do not stop the audit if the user says "use your best judgment".

1. **What you have access to.** A live URL, pasted text, screenshots, or a file. If only a URL is given and you cannot fetch it, request the text.
2. **Site language(s).** The audit is performed against the **original language** of the documents. Do not score compliance based on a machine translation.
3. **Audience.** Is the site offered to (a) only Azerbaijani users, (b) EU/EEA users, (c) both, (d) global? This drives GDPR Art. 3 applicability.
4. **What the site does.** Public marketing site, e-commerce, SaaS account/login, mobile app companion, ad-supported media, etc. This drives which lawful bases and cookie categories are realistic.
5. **Output preference.** Default is "both layers" (executive summary + lawyer-grade table). If the user wants only one, comply.

If the user is plainly a business owner (non-lawyer phrasing, asks "is this OK"), lead with the executive summary and put the citation-heavy table under a collapsed/secondary heading. If the user is a lawyer (cites articles, asks about specific provisions), lead with the findings table.

## Workflow

Follow these steps in order. Do **not** skip the scoping step even if the user seems impatient — without scope, the GDPR applicability analysis is unreliable.

### Step 1 — Scope

Produce a short scoping block:

- Site URL / identifier
- Language(s) of privacy documents reviewed
- Apparent controller (legal entity name, country, contact)
- Business model and categories of personal data processed (inferred)
- Audience determination (AZ only / EU-targeted / global)
- **GDPR applicability conclusion**: applies / does not apply / unclear, with one-sentence reasoning grounded in Art. 3 GDPR. See `references/gdpr_for_az_websites.md`.
- **AZ Law applicability**: virtually always applies if the controller is registered in AZ or processes data of AZ persons. Confirm and move on.
- **Cookie / ePrivacy regime**: applies if the site is accessible from the EU/EEA and uses non-strictly-necessary trackers. See `references/eprivacy_and_cookies.md`.

### Step 2 — Document inventory

List every privacy-relevant document found on the site, with status:

| Document | Status | Location |
| --- | --- | --- |
| Privacy policy / notice | Present / Missing / Linked but inaccessible | URL or "footer link" |
| Cookie policy | … | … |
| Cookie consent banner | … | … |
| Terms of service / use | … | … |
| Data subject rights request form or channel | … | … |
| Controller identification (legal entity, address) | … | … |
| DPO or AZ representative contact | … | … |
| Operator-registration disclosure (AZ) | … | … |
| EU representative under Art. 27 GDPR (if GDPR applies and controller is outside EU) | … | … |

Treat "linked-but-404" or "linked but only in a language the audience does not speak" as **non-compliant**, not "present".

### Step 3 — AZ Law findings

For each requirement in `references/az_law_998_overview.md`, record:

- Requirement (one line)
- Statutory anchor (article of Law 998-IIIQ)
- Evidence from the site (quote, verbatim, in the original language — translate in parentheses if not English)
- Status: **Compliant / Partial / Missing / Risk / Not applicable**
- Note (one or two sentences explaining the gap or why partial)

Also assess operator-registration obligations using `references/az_operator_registration.md` and flag explicitly whether the user appears to need to register.

### Step 4 — GDPR findings (only if applicable per Step 1)

Same table structure, with anchors to GDPR articles. Cover at minimum:

- Lawful basis (Art. 6) — is one stated, and is it plausible?
- Special categories (Art. 9) — if processed, is Art. 9(2) basis identified?
- Information to data subjects (Arts. 13 and 14) — checklist in the reference file
- Data subject rights (Arts. 15–22) — is each named with a channel to exercise it?
- International transfers (Chapter V, Arts. 44–49) — for any data flowing out of EU/EEA
- Records / accountability (Art. 30) — is there a stated controller and contact?
- DPO (Art. 37) — is one appointed where required?
- EU representative (Art. 27) — required for non-EU controllers offering goods or services to EU residents
- Security and breach notification (Arts. 32–34) — referenced in the policy?

See `references/gdpr_for_az_websites.md` for the full checklist and citation pinpoints.

### Step 5 — ePrivacy / cookie findings

Using `references/eprivacy_and_cookies.md`, assess:

- Is a banner shown on first visit before any non-essential trackers fire?
- Is "Reject all" as easy as "Accept all"?
- Are pre-ticked boxes used? (Always non-compliant per *Planet49*.)
- Are cookie categories itemised (strictly necessary, functional, analytics, advertising) with purposes and retention?
- Is the cookie policy linked from the banner?
- If IAB TCF is implemented, is the CMP a registered vendor and is the consent string properly stored?
- Is consent withdrawable as easily as it was given?

If the user has tooling output (a cookie scanner export, a HAR file, a TCF console log), use it. Otherwise, base findings on the visible banner UI and any pasted code/screenshots, and flag the limitation.

### Step 6 — Cross-border transfer analysis

If the site or its processors send personal data outside Azerbaijan (almost always yes — analytics, hosting, payment, email), check both legs:

- **Outbound from AZ.** Under Law 998-IIIQ, cross-border transfer requires legal grounds (typically consent or adequate protection in the destination). Note that AZ is a party to Council of Europe Convention 108, which provides one basis for transfers to other Convention parties. See `references/cross_border_transfers.md`.
- **Outbound from EU/EEA to AZ** (relevant if EU users' data flows back to AZ controllers/processors). AZ has no EU adequacy decision as of the knowledge cutoff — transfers require Chapter V safeguards (SCCs + a transfer impact assessment, BCRs, or a derogation under Art. 49). Verify the SCCs are the 2021 modules, not the legacy 2010/2004 sets.

### Step 7 — Produce the report

Use the template in `assets/audit_report_template.md`. Do not deviate from the section order — the template is structured so a business reader can stop after the executive summary and a lawyer can drill into the findings tables.

## Anti-hallucination rules

These rules are non-negotiable. A wrong citation in a legal audit is worse than a missing one.

1. **Never invent article numbers.** If you are not certain of the exact provision, write `Law No. 998-IIIQ, provision on [topic]` or `GDPR, the provision requiring [X]`. Do not produce a fabricated "Art. 14(2)(c)" you are not sure exists.
2. **Quote, do not paraphrase, when assessing the policy text.** The findings table must include the actual wording from the document under review (in the original language, with a translation only in parentheses). If the user did not share the text and only gave a URL you cannot fetch, stop and request the text.
3. **State the jurisdiction of each finding.** Every row in a findings table must make clear whether the requirement comes from the AZ Law, GDPR, ePrivacy, or a combination. Mixed-jurisdiction findings should be split.
4. **Mark the regulator and registration body generically.** Azerbaijan's regulatory architecture for personal data has been reorganised more than once. Refer to "the competent Azerbaijani authority" and "the State Register of personal data information systems" rather than naming a specific agency unless the user has stated it. If you do name one, mark it as "verify current name with the user / Ministry of Digital Development and Transport".
5. **Flag unverified facts explicitly.** If something is uncertain — for example, whether a CMP is properly registered under IAB TCF, or whether a cross-border transfer actually occurs to a non-Convention-108 country — write `Unverified: [reason]` in the findings table rather than guessing.
6. **Do not score compliance against a translated text.** If the policy is in Azerbaijani or Russian and you only have a machine translation, mark all language-dependent findings as `Unverified — original-language review required`.
7. **No drafting.** This skill is assessment-only. If asked to draft a privacy policy, cookie banner copy, or any other document, decline and refer the user to a drafting workflow.

## Output structure

Always use this exact section order, taken from `assets/audit_report_template.md`:

```
# Privacy Compliance Audit — [Site identifier]

## 1. Executive summary
   - Top 3 critical issues (red)
   - Top 3 medium issues (amber)
   - Overall compliance posture: AZ Law / GDPR / ePrivacy
   - One-paragraph plain-language summary for the business owner

## 2. Scope
   - As produced in Step 1

## 3. Document inventory
   - As produced in Step 2

## 4. Findings — Azerbaijani Law No. 998-IIIQ

## 5. Findings — GDPR (if applicable)

## 6. Findings — ePrivacy / cookies

## 7. Cross-border transfers

## 8. Operator registration assessment (AZ)

## 9. Prioritised remediation list
   - Numbered list of fixes, each tagged [AZ] / [EU] / [ePrivacy], with severity

## 10. Assumptions and limitations
   - What the auditor could not verify and why
```

## Severity levels

Use these consistently across all findings tables:

- **Red / Critical.** Direct statutory breach with realistic regulatory or litigation exposure. Examples: no privacy notice at all; pre-ticked consent for advertising cookies; international transfers to non-adequate jurisdictions with no safeguards; processing of special-category data without an Art. 9 basis.
- **Amber / Material.** Provision is present but materially deficient — for example, lawful basis listed but not tied to specific processing purposes; data subject rights named without a working channel to exercise them.
- **Yellow / Minor.** Drafting gap unlikely to attract enforcement on its own — for example, retention stated as "as long as necessary" without further detail.
- **Green / Compliant.** Provision meets the requirement.
- **Grey / Not applicable.** Document or topic does not apply to this site.

## Examples

**Example 1 — business owner asking about cookies**

Input: "Hi, our AZ company runs an e-commerce site at example.az, we sell to people in Azerbaijan and some in Germany. Our cookie banner has Accept and Settings. Is this OK?"

Approach: Run full Step 1 scoping (Germany customers → GDPR Art. 3(2)(a) applies → ePrivacy applies for cookies on EU visitors). Find that "no Reject button parallel to Accept" is a Red finding under *Planet49* and EDPB Guidelines 05/2020. Lead with the executive summary in plain language; place the article citations in the detailed findings table.

**Example 2 — lawyer reviewing a policy**

Input: "Please review the attached privacy policy for an AZ fintech onboarding KYC documents. They have users in AZ, UAE, and France."

Approach: GDPR applies for the French users. KYC implies Art. 9 special-category data may be processed (depending on data types). AML/CFT obligation is a lawful-basis candidate under Art. 6(1)(c). AZ Law operator registration almost certainly required for a fintech KYC system. Lead with the findings tables; keep the executive summary brief.

**Example 3 — pasted policy text, AZ-only audience**

Input: A wall of text in Azerbaijani plus "we only serve Azerbaijan, do we need GDPR?"

Approach: Conclude GDPR does not apply (Art. 3 not triggered) unless the user later reveals EU targeting. Run AZ Law and operator-registration analysis only. Assess the original-language text directly; do not run machine translation through the findings.

## Reference files

Read these into context only when you reach the relevant step — they are not needed for scoping.

- `references/az_law_998_overview.md` — Key obligations under Law No. 998-IIIQ with article anchors and audit checkpoints.
- `references/az_operator_registration.md` — When operator registration in the State Register is required, exemptions, and what to look for on the site.
- `references/gdpr_for_az_websites.md` — Art. 3 applicability, Art. 27 EU representative, and a checklist of Arts. 13/14 disclosures.
- `references/eprivacy_and_cookies.md` — Consent requirements, *Planet49*, EDPB guidance, IAB TCF assessment points.
- `references/cross_border_transfers.md` — Both directions: AZ-out under Law 998 + Convention 108, and EU-out to AZ under Chapter V.

## Asset files

- `assets/audit_report_template.md` — The mandatory output structure for the final report.
