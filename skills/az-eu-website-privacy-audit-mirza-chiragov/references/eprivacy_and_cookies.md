# ePrivacy and Cookie Consent — Audit Reference

Loaded when the audit reaches Step 5 (ePrivacy / cookie findings) of the SKILL.md workflow.

## Source

- Directive 2002/58/EC ("ePrivacy Directive"), as amended by Directive 2009/136/EC. Implemented in each EU member state's national law — pinpoint citations are therefore to the national implementing law in the country whose users are affected. For audit purposes, cite the Directive and note that national implementation may vary.
- Draft ePrivacy Regulation ("ePR"). Not in force as of the knowledge cutoff. Note it as forthcoming but do not score against it.
- GDPR (2016/679) — supplies the definition of consent (Art. 4(11)) and the conditions for consent (Art. 7).
- CJEU, *Planet49* (C-673/17), 1 October 2019 — pre-ticked consent for cookies is not valid consent.
- CJEU, *Orange Romania* (C-61/19), 11 November 2020 — burden of proving consent lies on the controller; pre-ticked boxes do not satisfy "active behaviour".
- EDPB Guidelines 05/2020 on consent — the operational standard for what a valid consent flow looks like.
- Local DPA guidance (CNIL France, ICO UK as a non-EU but persuasive reference, Garante Italy, the Spanish AEPD, etc.) provides further enforcement context. Do not cite a specific DPA unless the audit is for a controller plainly targeting that member state.

## Applicability — does the cookie/ePrivacy regime apply?

The ePrivacy regime applies to storage of or access to information on the **terminal equipment** of a user located in the EU/EEA. In practice, for a website audit, ask:

1. Does the site set, read, or use cookies, local storage, IndexedDB, ETag/fingerprinting, SDK identifiers, or any other client-side storage?
2. Are users in the EU/EEA visiting the site?
3. Is the storage strictly necessary for a service explicitly requested by the user (i.e., session token to keep them logged in)?

If yes to 1 and 2, and no to 3 for any tracker, the consent requirement under Art. 5(3) of the ePrivacy Directive applies.

Crucially: the ePrivacy consent requirement is **not** limited to "personal data". It applies to **any** storage on the terminal that is not strictly necessary, regardless of whether the stored data identifies the user.

## Valid consent — the operational test

A cookie consent flow is valid only if **all** of the following are true. Score each as a row in the findings table.

### 1. Prior consent before non-essential storage

No non-essential cookie, pixel, SDK, or fingerprint may fire before the user gives consent. If the network panel shows analytics, ad, or social-media trackers firing on initial page load, this is **Red**. The standard mitigation is "consent mode" or a tag-manager gate that holds non-essential tags until the consent string is set.

### 2. Granular consent per purpose

Consent must be granular by purpose (or at minimum by category — strictly necessary, functional/preferences, analytics, advertising/personalisation, social media). A single "Accept all" toggle bundling all categories is **Amber to Red** depending on member state.

### 3. Active, unambiguous action

The user must take an active step — clicking "Accept" or selecting checkboxes. Pre-ticked boxes are invalid (*Planet49*). Implied consent from continued browsing is invalid. Closing the banner with an "X" is invalid as consent (but valid as a refusal in some DPAs' views).

### 4. Reject as easy as accept

The first layer of the banner must offer a "Reject all" option with the same prominence as "Accept all". A flow that requires the user to click into "Settings" and then untoggle items individually before they can refuse is **Red** per current French CNIL and Italian Garante enforcement.

### 5. Informed consent

Before consenting, the user must be told:

- Who is setting the cookies/trackers (the controller and any third parties).
- For what purposes.
- What categories of data are processed.
- How long the cookies persist (retention).
- That consent can be withdrawn at any time, and how.

This information is typically split between the banner (short) and a linked cookie policy (long). Both must be present.

### 6. Free consent

Consent must not be a condition of accessing the service unless the controller can demonstrate that the processing is necessary for the service. "Cookie walls" — refuse cookies, lose access — are generally invalid for non-essential cookies. Pay-or-okay flows are contested as of the knowledge cutoff; flag as **Amber — pay-or-okay is under active regulatory scrutiny**.

### 7. Withdrawal as easy as granting

A persistent way to revisit and change cookie choices must exist after consent — typically a "Cookie preferences" link in the footer or a re-opening icon. Missing withdrawal mechanism is **Red**.

### 8. Records / demonstrability

The controller must be able to demonstrate consent (Art. 7(1) GDPR). The site alone cannot prove this. Note as `Unverified — request consent log / CMP records`.

## IAB TCF specifics

If the audit subject implements the IAB Transparency and Consent Framework (TCF), assess additionally:

- **CMP registration.** The Consent Management Platform must be a registered IAB TCF CMP. Look for the CMP identifier in the TCF consent string (`tcfca` or `__tcfapi`) or the CMP's branding in the banner.
- **Vendor list integrity.** The full vendor list should be reachable from the banner in two or fewer clicks.
- **Special purposes vs. purposes.** The distinction between "purposes" (consent-required) and "special purposes" (legitimate-interest grounded under the TCF policy) should be respected; check that purposes 1 (store and access information on a device) is consented, not legitimate-interest signalled.
- **Consent string integrity.** The TC string must be set only after the user clicks Accept on the relevant purposes/vendors, not before.
- **Belgian DPA decision (APD 21/2022 of 2 February 2022).** The TCF as deployed by IAB Europe was found to have GDPR violations; while the framework has been iterated since, an audit should note that TCF-based flows do not by themselves guarantee compliance and require an independent consent assessment.

If the site implements TCF without these conditions, flag as **Red — TCF deployment likely non-compliant**.

## Cookie policy contents — checklist

The cookie policy linked from the banner should disclose:

- The fact that the site uses cookies and similar technologies.
- A current table of each cookie with: name, party (first vs third), purpose, category, retention.
- The third parties receiving data via cookies.
- The legal basis for each category (consent vs. strictly necessary as Art. 5(3) ePrivacy exception).
- How to withdraw consent and how to block cookies at the browser level.

A cookie policy that lists categories generically ("we use analytics cookies") without naming individual cookies is **Amber**.

## What you can and cannot verify from the materials you have

- **From a screenshot of the banner:** the first-layer choices and prominence (steps 2, 4 above).
- **From the cookie policy text:** the disclosure completeness.
- **From the policy text alone, without a network capture:** you cannot verify steps 1, 5, 7, 8. Flag these as `Unverified — site behaviour check required`.
- **From a HAR file or a cookie-scanner export (if the user provides one):** the actual cookies fired and their timing relative to consent. This converts several `Unverified` items to scoreable findings.

If the user has not provided a network capture, note in Step 10 (Assumptions and limitations) that the cookie audit is partial and recommend a live audit using browser developer tools or a CMP scanner.

## AZ Law angle on cookies

Cookies that process personal data (a unique identifier tied to a person, behaviour profiles tied to an account, IP addresses where they reach the identifiability threshold) fall under Law No. 998-IIIQ as well. The AZ Law does not have a dedicated ePrivacy-style storage rule, but the law's consent and legal-basis requirements apply where the cookie processes personal data. Score AZ-Law-on-cookies findings as a separate row prefixed `[AZ]` in the cookie findings table.
