# Section-by-Section Drafting Guide

Draft the notice in this order. All 12 sections are required unless explicitly marked *(if applicable)*. Write everything in plain, clear English — as if explaining to a smart adult who has never read a legal document. No legal citations in the notice body.

---

## Opening Lines (before Section 1)

At the very top of the notice, include in this order:

**Line 1 — Internal note:**
> *Internal note: All items marked [Note: …] need to be reviewed and confirmed by your team before this notice is finalised and deployed.*

**Line 2 — Research disclosure (only if factual details were assumed from research):**
> *[Note: Sections [X, Y, Z] contain details — including categories of personal data collected, purposes of processing, data sharing arrangements, storage locations, and security measures — that have been drafted based on the common practices of businesses of this type, researched from comparable companies. These are assumptions only. Your team must review and confirm all such details before this notice is finalised. Factual inaccuracies in a consent notice can affect the validity of consent obtained under it.]*

**Line 3 — Language option (always include, exactly as follows):**
> *You have the right to read this notice in the language of your choice. This notice is currently available in English.*
> *[Note for tech team: You are legally required to give users the option to access this notice in English OR any of the 22 languages listed in the Eighth Schedule of the Indian Constitution (Assamese, Bengali, Bodo, Dogri, Gujarati, Hindi, Kannada, Kashmiri, Konkani, Maithili, Malayalam, Manipuri, Marathi, Nepali, Odia, Punjabi, Sanskrit, Santali, Sindhi, Tamil, Telugu, Urdu). Build a language-selection interface at the point of consent collection — before the user accesses this notice — so they can select their preferred language. Each language version requires a professional translator. Asking users to email for a translation does not satisfy this legal requirement.]*

---

## Section 1 — Who We Are and What This Notice Is About

Write a short, welcoming intro paragraph (no sub-bullets, no heading numbering). Cover:
- The full legal name and address of the company
- That this is a notice asking for the user's consent to process their personal data
- A brief, factual description of the **Services** — define this clearly and give it a name (e.g., "[Company] Services") that you'll use throughout the notice. Research the industry to make this description accurate and specific. Mark anything inferred with `[Note: confirm this describes your services accurately]`
- A sentence that this notice should be read alongside the company's Privacy Policy, Terms of Use, and other applicable policies — but is itself complete and sufficient for consent purposes
- A sentence saying the user can reach the company at `[Note: insert contact email/DPO details]` with any questions

**Tone example:**
> "[Company Name] is a [type of company] that offers [brief service description] ("the Services"). This notice explains what personal information we collect, why we collect it, and how we use it — and asks for your consent before we start. If you have any questions, you can always reach us at [Note: insert contact email]."

---

## Section 2 — What Personal Information We Collect

Write this as a plain, readable list with a brief description for each category. Do not use legal language like "data subject" — say "you" and "your information."

**Structure**: Group into named categories with 1–2 sentences explaining each. Example:

> **Your identity and contact details** — Your name, email address, phone number, date of birth, and profile photo.
>
> **Your payment information** — Payment card details, UPI ID, and transaction history. [Note: confirm whether you store card details directly or only via payment gateway tokens]

Always separately identify any **sensitive information** (health data, financial data, biometric data, government IDs, precise location) and flag it clearly as sensitive to the reader.

**Research**: Based on the business type, research comparable companies' privacy notices to propose a full and realistic list. Mark each category inferred from research with `[Note: confirm we collect this]`.

**How data is collected**: End the section with a short paragraph explaining the sources:
- Directly from the user (forms, registration, transactions)
- Automatically (cookies, app usage, device data)
- From third parties (if applicable — payment processors, analytics providers, etc.)

---

## Section 3 — Why We Use Your Information

Write as a numbered list of specific purposes. Each purpose must:
- Have a clear, specific name
- Explain what it enables in plain language (what the user gets)
- State whether it is **required** (needed to use the service) or **optional** (the user can say no)

**Example format:**
> **1. Creating and managing your account** *(Required)* — We use your name, email and phone number to set up your account so you can log in and use [Services].
>
> **2. Processing your orders** *(Required)* — We use your delivery address and payment details to complete your purchases and send you what you ordered.
>
> **3. Sending you offers and updates** *(Optional — you can say no)* — We'd like to send you news about new products, offers and promotions via email, SMS or WhatsApp. You can choose whether to receive these.

**Research**: Based on industry, propose a realistic full list of purposes. Mark inferred purposes with `[Note: confirm this purpose applies to your business]`.

---

## Section 4 — Who We Share Your Information With

Write as a structured list of recipient categories. For each category, say:
- Who they are (in plain terms, not legal labels)
- What information is shared with them
- Why it is shared
- Whether they are in India or outside India

Also state:
- That you require all processors to sign data processing agreements and maintain adequate security
- That you do not sell personal data

**Research**: Based on industry type, identify typical third-party recipients. Confirm with `[Note: confirm these are your actual third-party partners]`.

---

## Section 5 — How Long We Keep Your Information

Write in plain language. Do not reproduce statutory text verbatim.

**Core retention statement**: We keep your information for as long as needed to provide you with the Services and as required by law. Once it is no longer needed, we delete it securely.

**Sector-specific retention**: Based on the user's industry, check applicable laws and state specific retention periods where they apply. Examples:
- Banking/financial data: typically 8–10 years under PMLA and RBI rules
- Tax/GST transaction records: 8 years
- E-commerce (entities with 2 crore+ users): 3 years of inactivity before erasure under DPDPA Rules
- General consumer data with no inactivity: delete when purpose is served or consent withdrawn

**Rule 8 / Third Schedule — apply directly, do not cite**:
- If the business falls under the Third Schedule categories (e-commerce entity with 2 crore+ registered users; online gaming entity with 50 lakh+ users; social media entity with 2 crore+ users): state clearly in plain English that if the user hasn't logged in or used the service for 3 years, the data will be deleted — with a warning notice sent to the user at least 48 hours before deletion. Do not quote Rule 8(1) or (2) verbatim.
- If the business does NOT fall under the Third Schedule: simply state data is deleted when the purpose is served or consent is withdrawn — no mention of the 3-year rule or the 48-hour notification.

**Rule 8(3) / Schedule 7 — only include if relevant**:
Only mention the 1-year processing log retention requirement if the business is one where this is practically relevant (e.g., fintech, banking, telecom, large-scale e-commerce, or where the user has specifically asked about it). Do not include this for general consumer businesses unless there is a specific reason.

**Deletion process**: In plain English, explain:
- How users can request deletion (self-service + contact method)
- How long it takes to action a deletion request

Do **not** include a separate "Pre-Erasure Notification" sub-section heading. If the 48-hour notification applies (Third Schedule businesses), mention it naturally within the retention paragraph.

---

## Section 6 — Your Rights

Write each right as a short, friendly explanation followed by specific instructions. **Always lead with the self-service option** — what the user can do directly in their account or app, without needing to contact anyone. Email is only a fallback. This design principle applies to every single right: users must be able to act independently.

Format each right as:
1. Self-service path first: "Go to [Account Settings → Privacy → X]" — use `[Note for tech team: insert exact in-app path for this action]` if unknown
2. Fallback: "If you can't do this in your account, email us at `[Note: insert privacy email]`"

---

**6.1 The right to know** — You can ask us what personal information we hold about you and why we have it.
- *How*: View a summary of your data directly in your account under `[Note for tech team: insert path, e.g., Account Settings → Privacy → My Data]`. If you'd like more detail or can't find it there, email us at `[Note: insert privacy email]`. We'll respond within `[Note: insert timeline, e.g., 30 days]`.

**6.2 The right to access your information** — You can request a full copy of all personal information we hold about you.
- *How*: Download your data directly from `[Note for tech team: insert path, e.g., Account Settings → Privacy → Download My Data]`. If this isn't yet available in your account, email us at `[Note: insert privacy email]`. We'll respond within `[Note: insert timeline]`.

**6.3 The right to correct your information** — If any of your information is wrong or out of date, you can fix it.
- *How*: Update most details yourself in `[Note for tech team: insert path, e.g., Account Settings → Profile]`. For anything that can't be changed directly (such as identity documents or transaction records), email us at `[Note: insert privacy email]` with your account ID and the correction needed. We'll respond within `[Note: insert timeline]`.

**6.4 The right to delete your information** — You can ask us to delete your personal information. We will, unless we're required by law to keep it.
- *How*: Delete your account and data through `[Note for tech team: insert path, e.g., Account Settings → Privacy → Delete My Account]`. For deletions that need manual review, email us at `[Note: insert privacy email]` with "Erasure Request" in the subject line. Note that deleting your information may mean we can no longer provide you with the Services.

**6.5 The right to withdraw or manage your consent** — You can change or withdraw your consent at any time. It should be as easy to withdraw as it was to give.
- *How*: Manage all your consent preferences directly in `[Note for tech team: insert path, e.g., Account Settings → Privacy → Manage Consent]` — you can switch any optional consent on or off whenever you like. If you can't find this in your account, email us at `[Note: insert privacy email]`. If you withdraw a consent we need to provide the Services, we may not be able to continue providing them.

**6.6 The right to nominate someone** — You can nominate a trusted adult to exercise these rights on your behalf if you pass away or become incapacitated.
- *How*: `[Note for tech team: if an in-app nomination flow is available, insert the path here. If not yet built, state:]` Submit a nomination request by emailing us at `[Note: insert privacy email]` with "Nomination Request" in the subject line. `[Note for tech team: consider building an in-app nomination flow so users can complete this without email dependency.]`

**6.7 The right to raise a complaint** — If you're unhappy with how we've handled your personal information, you can raise a complaint with us. If we don't resolve it to your satisfaction, you can take it to the **Data Protection Board of India**.
- *How*: `[Note for tech team: if an in-app grievance submission feature exists, insert the path here. If not:]` Contact our Grievance Officer (see Section 12 for details). If your complaint isn't resolved within `[Note: insert number of days]` days, you can escalate to the Data Protection Board of India. `[Note for tech team: consider adding an in-app "Report a Privacy Issue" flow so users aren't solely dependent on email.]`

---

## Section 7 — How We Keep Your Information Safe

Write in plain language. Cover:
- That we use industry-standard security measures (encryption, access controls, regular monitoring)
- That we require our processors and service providers to maintain the same standards
- That while we take all reasonable steps, no internet transmission is 100% secure
- Where data is stored (India / outside India / cloud) — `[Note: confirm data storage locations]`

Keep this section concise — 3–4 short paragraphs. Do not quote Rule 6 provisions.

---

## Section 8 — Automated Decisions About You *(include only if applicable)*

Only include this section if the business uses automated decision-making that affects users (e.g., credit scoring, fraud flagging, personalised pricing, content recommendations with real consequences).

Write in plain language:
- What automated decisions are made
- What information is used
- Whether a human will review if the user disagrees
- How to request human review

If the business does not use consequential automated decision-making, omit this section entirely.

---

## Section 9 — Children's Privacy *(always include)*

**Option A — Service not for children (most cases)**:
> "Our Services are for adults aged 18 and above. We do not knowingly collect personal information from anyone under 18. If you are under 18, please do not use our Services or give us your information. If we discover we have collected information from a child, we will delete it immediately. If you are a parent or guardian and think your child has given us information, please contact us at `[Note: insert email]`."

Also include whether the company has a technical mechanism to screen out minors `[Note: confirm your age-verification process]`.

**Option B — Service collects children's data (requires parental consent)**:
- Explain that children's information is only collected with **verified consent from a parent or guardian**
- Explain the verification method in plain terms `[Note: confirm your parental consent verification mechanism, e.g., DigiLocker, OTP to parent's number, etc.]`
- State clearly: we do not track children's behaviour, build profiles on children, or show them targeted advertising
- Structure all consent boxes at the end for the parent/guardian, not the child

**Option C — Schedule 4 exemptions (healthcare providers, email-only services)**:
If the business qualifies for an exemption from parental consent requirements, state what the service does and why parental consent is not required — in plain terms. Confirm the applicable exemption with `[Note: confirm this exemption applies to your service with legal counsel]`.

---

## Section 10 — Cookies and Tracking *(if applicable)*

Only include if the business uses a website, app, or any tracking technology. Write in plain, friendly language.

**Structure**: Explain each category of cookie simply:

> **Cookies we need to run the site** — These are essential for the website to work. We can't turn them off.
>
> **Cookies that remember your preferences** — These remember things like your language or login details so you don't have to re-enter them every time.
>
> **Analytics cookies** — These tell us how people use our site (e.g., which pages are most popular). The information is anonymous.
>
> **Advertising cookies** — These are used to show you ads that are relevant to you, including on other websites. `[Note: confirm which advertising/retargeting platforms you use, e.g., Google Ads, Meta Pixel]`
>
> **Third-party cookies** — Some of our partners (like payment providers or social media buttons) may place their own cookies. We don't control these — please check the relevant partner's privacy policy.

Then explain how to manage preferences:
> "You can manage your cookie preferences using our cookie settings `[Note: insert cookie preference centre link]` or through your browser settings."

**Research**: Based on the user's tech stack and industry, propose typical cookie categories and providers. Mark with `[Note: confirm]`.

---

## Section 11 — Sending Your Information Overseas *(if applicable)*

Only include if data is transferred outside India.

Write plainly:
- What information is transferred overseas and to where (country/region)
- Why (e.g., "our cloud servers are based in Singapore")
- What safeguards protect the transfer (e.g., contracts with the service provider, their compliance with equivalent data protection standards)

Do NOT include a clause saying "by giving your consent under this notice, you consent to transfers." Delete any such clause if present.

Do NOT include legal commentary about Section 16 DPDPA or the absence of Government notifications. Simply state what happens and what protections are in place.

If no international transfers occur, omit this section entirely.

---

## Section 12 — Grievances and Contact

Write as a clear contact block. Include:
- Grievance Officer name, email, postal address
- How to raise a grievance (email, form, or portal — `[Note: confirm grievance mechanism]`)
- Response timeline (`[Note: insert, e.g., 30 days]`)
- That unresolved grievances can be escalated to the **Data Protection Board of India**
- Data Protection Officer details if the company has one (or if they are required to have one as a Significant Data Fiduciary)
- General privacy queries contact

Format the contact details as a clear box:

```
Grievance Officer
Name: [Note: insert name]
Email: [Note: insert email]
Address: [Note: insert address]
Response time: [Note: insert timeline]
```

---

## Sector-Specific Disclaimer Box

After Section 12 and before the consent boxes, always include (tailor the sectors to the user's business — only list the ones that are actually relevant):

> **A note for the [Company Name] team**: If your business activities involve [Banking and Financial Services / Telecommunications / Healthcare and Pharmaceuticals / Insurance / other regulated sector — include only what's relevant], you may have additional data protection obligations under sector-specific regulations, beyond what the DPDPA requires. This consent notice covers your DPDPA obligations. Please review any applicable sectoral laws separately with your legal counsel.

---

## Consent Boxes (Granular — at the End of the Notice)

Always provide separate, individually ticked consent boxes. **Never bundle consents together.** Unticked by default (except where stated).

**Box 1 — Core service consent (mandatory to use the service)**:
> ☐ I have read and understood this Notice and agree to [Company Name] collecting and using my personal information to provide me with [Services], as described above. I confirm I am 18 or older (or a legal guardian acting on behalf of someone who needs my consent). I know I can withdraw this consent at any time.

**Box 2 — Marketing communications** (optional):
> ☐ I'd like to receive updates, offers and news from [Company Name] by email, SMS and/or WhatsApp. I can unsubscribe at any time.

**Box 3 — Personalised recommendations** (optional):
> ☐ I'm happy for [Company Name] to use my browsing and purchase history to show me personalised product recommendations and offers.

**Box 4 — Analytics cookies** (optional):
> ☐ I agree to [Company Name] using analytics cookies to understand how I use the website/app, which helps improve the service.

**Box 5 — Advertising and retargeting** (optional):
> ☐ I agree to [Company Name] and its advertising partners using my data to show me relevant ads on other websites and platforms.

**Box 6 — Sharing with group companies for their marketing** (optional — only include if applicable):
> ☐ I agree to [Company Name] sharing my contact details with its group companies so they can tell me about their own products and services.

**Additional boxes**: Add any other optional processing that applies to the specific business (e.g., sharing health data with partner clinics, sharing data with loyalty programme partners, etc.). Research what's industry-standard and mark additions with `[Note: confirm this applies]`.

**Legal guardian version** (for services that include children):
> ☐ I am the parent or legal guardian of the person named above, who is under 18. I have read and understood this Notice and give my verified consent on their behalf for [Company Name] to collect and use their personal information as described. I confirm I am over 18 and am the lawful guardian of this child.
