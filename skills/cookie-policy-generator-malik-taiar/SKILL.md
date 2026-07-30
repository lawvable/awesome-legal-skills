---
name: cookie-policy-malik-taiar
description: Guide for drafting cookie policies compliant with GDPR and the ePrivacy Directive. Includes CNIL 2020 recommendations, a reference template, and best practices. Use when drafting or revising a cookie policy for a website or application.
metadata:
  author: Malik Taiar
  license: AGPL-3.0
  version: 2025.12.24
---

# Cookie Policy Guide

## Overview

A cookie policy informs users about cookies and trackers placed on their device. It is distinct from the privacy policy but can be integrated into it. It must comply with CNIL 2020 guidelines.

### Cookie Policy Objectives

| Objective | Requirement |
|-----------|-------------|
| **Transparency** | Inform about cookies used and their purposes |
| **Consent** | Obtain free, informed, and prior consent |
| **Control** | Allow users to manage their preferences |
| **Compliance** | Comply with GDPR + ePrivacy + CNIL recommendations |

---

## Reference Resources

### Template

| Template | Description |
|----------|-------------|
| `assets/sample_template_politique_cookies.docx` | Default template to use if no private template is provided |
| Internal template provided by lawyer | Use if the lawyer has a more suitable private template |

### CNIL Documentation

| PDF File to READ (Read tool) | URL to CONSULT (WebFetch tool) | Topic |
|------------------------------|--------------------------------|-------|
| `assets/CNIL_lignes_directrices_cookies_et_traceurs.pdf` | - | Cookie guidelines |
| `assets/CNIL_recommandation_cookies_et_traceurs.pdf` | https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies | Cookie recommendations |
| `assets/CNIL_faq_cookies_et_traceurs.pdf` | https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/FAQ | Cookie FAQ |
| `assets/CNIL_evolution_regles_utilisation_cookies.pdf` | https://www.cnil.fr/fr/evolution-des-regles-dutilisation-des-cookies-quels-changements-pour-les-internautes | Rules evolution |
| `assets/CNIL_transparence.pdf` | - | Guide on information and transparency |
| `assets/CNIL_principes_rgpd.pdf` | - | Fundamental GDPR principles |
| `assets/RGPD_texte_officiel.pdf` | - | Full text of EU Regulation 2016/679 |

> **REQUIREMENT**: For ANY information regarding cookies, consent, retention periods, exemptions, or best practices:
> 1. **READ the PDF files** with the Read tool BEFORE responding on a regulatory point
> 2. **CONSULT the online URLs** with WebFetch to verify the most current information
> 3. **CITE the CNIL URL** in your response when mentioning a rule or duration
> 4. **NEVER invent** a duration or rule without verifying it in the sources

### Knowledge Base

| Document | Content |
|----------|---------|
| **[COOKIES.md](references/COOKIES.md)** | Cookie categories, banners, CNIL sanctions, retention periods |
| **[BASES_LEGALES_COOKIES.md](references/BASES_LEGALES_COOKIES.md)** | Cookie-specific legal bases (consent, exemptions) |
| **[DROITS_PERSONNES.md](references/DROITS_PERSONNES.md)** | Data subject rights |
| **[DUREES_CONSERVATION.md](references/DUREES_CONSERVATION.md)** | Retention periods (6 months recommended by CNIL for consent, 13 months max) |

---

## Information to Collect from Client

> **IMPORTANT**: Before drafting the policy, collect the information below.

### 1. Website Publisher Information

- [ ] Full company name
- [ ] Legal form (SAS, SARL, Ltd, etc.)
- [ ] Registered office address
- [ ] Contact email
- [ ] Website URL

### 2. Cookies Used

STRICTLY NECESSARY COOKIES (exempt from consent)
- [ ] Session cookie
- [ ] Authentication cookie
- [ ] Shopping cart cookie
- [ ] Security cookie (CSRF)
- [ ] Language preference cookie
- [ ] Cookie choice remembrance cookie

ANALYTICS COOKIES
- [ ] Google Analytics
- [ ] Matomo
- [ ] AT Internet
- [ ] Other: ___________

ADVERTISING / MARKETING COOKIES
- [ ] Google Ads
- [ ] Facebook Pixel
- [ ] LinkedIn Insight Tag
- [ ] Criteo
- [ ] Other: ___________

SOCIAL MEDIA COOKIES
- [ ] Facebook share buttons
- [ ] Twitter/X share buttons
- [ ] LinkedIn share buttons
- [ ] Embedded YouTube videos
- [ ] Other: ___________

FUNCTIONALITY COOKIES
- [ ] Live chat (e.g., Intercom, Crisp)
- [ ] Video player
- [ ] Interface personalization
- [ ] Other: ___________

### 3. Consent Management Platform (CMP)

- [ ] None
- [ ] Axeptio
- [ ] Didomi
- [ ] Cookiebot
- [ ] OneTrust
- [ ] Other: ___________

### 4. Retention Periods

> **READ CNIL SOURCE**: `assets/CNIL_recommandation_cookies_et_traceurs.pdf` + https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies
> **IMPORTANT**: CNIL recommends **6 months** for the consent cookie. Use 6 months as default.

| Cookie | CNIL Recommended Duration | Maximum Duration |
|--------|---------------------------|------------------|
| Consent cookie | 6 months | 13 months |
| Analytics cookies | Depending on purpose | 13 months |
| Advertising cookies | Depending on purpose | 13 months |

---

## Drafting Workflow

### Step 1: Template Selection (MANDATORY)

> **NEVER DRAFT A POLICY FROM SCRATCH.**
> Always start from a given template for drafting, either:
> - the default template in `assets/sample_template_politique_cookies.docx`;
> - another internal template provided by the user.
>
> This template is your base reference. You must:
> - **Faithfully reproduce the template's structure and wording**
> - **Keep the exact template phrasing** (they are validated)
> - **Only replace placeholders** with client information
> - **Do NOT rewrite sentences** even if you think you can phrase them better
> - **Do NOT add sections** that are not in the template
>
> The collected information (cookies used, CMP, etc.) is used to **fill in** the template, **not to rewrite it**.

**1. FIRST ACTION: Confirm the template to use BEFORE any drafting. Ask the user:**
```
"I will draft the cookie policy starting from the provided default template. Do you have an internal template that would be more suitable as a starting point?"
```

| Option | Action |
|--------|--------|
| Default template | Use `assets/sample_template_politique_cookies.docx` |
| Internal template | Use the document provided by the lawyer |

**2. Consider the user's choice and select the starting template.**

---

### Step 2: Understand the Site and Cookies Used

> **MAIN OBJECTIVE**: Precisely identify all cookies placed by the site.

**1. Ask the lawyer for available information:**
```
"To draft a perfectly tailored cookie policy, please provide:
- The website URL
- The list of cookies used (if known)
- The consent management platform (CMP) used
- Third-party tools integrated (analytics, advertising, social media...)
- Any existing documentation about the site's cookies

You may anonymize this information if necessary for confidentiality reasons.

The more information you provide, the better adapted the policy will be. Otherwise, we will conduct our own research but it will be limited to publicly accessible information."
```

**2. Research on the site (if accessible):**
- Visit the site and observe the cookie banner
- Identify the CMP used
- List visible cookies (via browser tools)
- Note third-party integrations (YouTube, social media, analytics...)
- Read the existing cookie policy (if present)

**3. Summary before drafting:**
```
SITE: [URL]
CMP USED: [Solution name]
STRICTLY NECESSARY COOKIES: [List]
ANALYTICS COOKIES: [List + providers]
ADVERTISING COOKIES: [List + providers]
SOCIAL MEDIA COOKIES: [List + providers]
FUNCTIONALITY COOKIES: [List]
RETENTION PERIODS: [Compliant with 13 months max?]
KEY LAWYER POINTS: [What must absolutely be included]
```

> Once the summary is ready → Proceed to Draft 1.

---

### Step 3: Draft 1

> **ABSOLUTE RULE**: The reference template is your validated base.
>
> - **START from the template**: structure, wording, tone → this is your reference
> - **ADAPT to the client case**: integrate the specific cookies identified
> - **DO NOT rewrite everything**: keep the template wording, only adapt what needs to be
>
> In summary: Template + client cookies = Draft 1. Not a complete rewrite.

Complete the template section by section:

1. **What is a cookie?** (definition)
2. **Who places cookies?** (publisher + third parties)
3. **Strictly necessary cookies** (detailed table)
4. **Analytics cookies** (table + purposes)
5. **Advertising cookies** (table + purposes)
6. **Social media cookies** (table + purposes)
7. **How to manage your preferences?** (banner + browser)
8. **Retention period**
9. **Policy updates**
10. **Contact**

> **Immediate compliance check:** Before presenting Draft 1, verify the cookie compliance checklist (CNIL 2020):
> - [ ] Exhaustive list of cookies with name, provider, duration, purpose
> - [ ] Distinction between necessary cookies vs cookies requiring consent
> - [ ] Information that refusing is as easy as accepting
> - [ ] Retention periods ≤ 13 months
> - [ ] Clear explanation of how the banner works
> - [ ] Instructions for managing cookies via browser
> - [ ] Link to CMP to modify preferences
> - [ ] Document update date
> - [ ] Contact for questions
>
> If Draft 1 is compliant → Proceed to Step 3.

---

### Step 4: Deliver Draft 1 + Benchmark + Improvement Suggestions

**1. Deliver Draft 1 with explanation:**
```
"Here is Draft 1 of the cookie policy.

**What I took into account:**
- [List of identified cookies]
- [CMP used]
- [Retention periods]

**Compliance:** The document complies with CNIL 2020 guidelines."
```

**2. Present the benchmark (systematic):**

Research 3-5 cookie policies from companies in the same sector, then present:
```
"**Benchmark conducted:**

I analyzed the cookie policies of:
- [Company 1] - [what we noted]
- [Company 2] - [what we noted]
- [Company 3] - [what we noted]

**Identified possible improvements:**
- [Improvement 1]: [explanation]
- [Improvement 2]: [explanation]

Would you like to incorporate these elements into the provided Draft?"
```

**3. If the lawyer approves improvements → Produce Draft 2**

---

### Step 5: Final Verification

Final review before definitive delivery:

- [ ] All site cookies are listed
- [ ] Distinction between necessary / consent-required respected
- [ ] Retention periods ≤ 13 months
- [ ] Clear management instructions (banner + browser)
- [ ] No internal references in final document
- [ ] Update date present

---

## CNIL Reference Sanctions

| Company | Amount | Reason |
|---------|--------|--------|
| Google | €150M | Refusing cookies more difficult than accepting |
| Facebook | €60M | No visible "reject all" button |
| Amazon | €35M | Cookies placed without prior consent |
| Microsoft | €60M | Cookies placed without consent |

> These sanctions illustrate the importance of a compliant cookie policy and a banner respecting the principle that refusing must be as easy as accepting.

---

## Common Mistakes to Avoid

| Mistake | Potential Sanction | Solution |
|---------|-------------------|----------|
| Cookies placed before consent | Fine | Wait for "Accept" click |
| No visible "Reject" button | Fine | Button at same level as "Accept" |
| Strict cookie wall | Fine | Offer an alternative |
| Duration > 13 months | Formal notice | Respect maximum duration |
| No cookie list | Non-compliance | Detailed table required |
| Dark patterns | Fine | Neutral and clear design |
| Incomplete cookie list | Non-compliance | Complete site audit |

---

## Using This Guide

1. **Step 1 - Choose the template**: Default reference template, or lawyer's internal template
2. **Step 2 - Identify cookies**: Collect lawyer info + site analysis
3. **Step 3 - Draft Draft 1**: Complete template + compliance check
4. **Step 4 - Deliver + Benchmark**: Present Draft 1 + systematic benchmark + improvement suggestions
5. **Step 5 - Finalize**: Integrate approved improvements + final verification

> **TEMPLATE REMINDER**: Never draft from scratch. Always start from the reference template and adapt it.
> **DURATION REMINDER**: CNIL recommends **6 months** for the consent cookie (13 months max). Always verify in CNIL sources before mentioning a duration.
