# Verified Reference Pack — Platforms, Third-Party Tools, Cookies & AI

> **Zero-hallucination rule:** cite only from this pack or a live lookup. The contractual clauses below
> are paraphrased from vendor terms that were fetched; for a *verbatim* quote in a high-stakes context,
> re-fetch the vendor page. Items the research flagged UNVERIFIED are marked. Last verified 2026-06.

This file answers two practical questions: (1) **what FORCES a privacy policy beyond statute**, and
(2) **what each tool/AI feature OBLIGES you to disclose**.

---

## 1. When a privacy policy is FORCED by contract (not just law)

A founder is contractually required to publish a privacy policy the moment they use any of these —
**even a zero-data app must still post one**:
- **Apple App Store** (Guideline 5.1.1(i)): every app must link a privacy policy in App Store Connect AND in-app.
- **Google Play**: privacy-policy link required in Play Console AND in-app; **apps that collect no data must still submit one** and complete the Data Safety form.
- **Google AdSense/AdMob/Ads, Google Analytics**: their terms require an appropriate privacy policy disclosing cookies/identifiers and data use.
- **Stripe, PayPal**: merchant must provide notices and make a privacy policy available.
- **Mailchimp**: sender must post a privacy policy linking to Mailchimp's.
- **Meta (Facebook) Login / Business Tools**: mandatory public privacy-policy URL.
- **Sign in with Apple / Google Sign-In (OAuth/SSO)**: login is a collection event the policy must disclose.

> **Skill rule:** if the product uses ANY third-party SDK that collects/transmits user/device data
> (ads, analytics, payments, crash reporting, social login), a privacy policy is forced and must NAME
> those third parties.

---

## 2. Apple App Store — what the policy must say to pass review
Guideline **5.1.1(i)** requires the policy to clearly and explicitly:
1. Identify **what data the app collects, how, and all uses**.
2. Confirm any **third party** receiving user data (analytics, ad networks, SDKs, affiliates) provides
   **equal protection** of the data.
3. Explain **data retention/deletion** policies and **how a user revokes consent / requests deletion**.

Plus: **5.1.1(ii)** consent for any data collection (even anonymous) + an easy way to withdraw;
**5.1.1(v)** apps with accounts must offer **in-app account deletion**; **App Privacy "nutrition label"**
in App Store Connect must **match** the policy; **App Tracking Transparency (ATT)** — if the app
links user/device data with other companies' data for ads, or shares with data brokers ("tracking"),
it must fire the ATT prompt and disclose the tracking; **5.1.4 Kids** category bans third-party
analytics/ads and requires COPPA/GDPR compliance + a privacy policy.
Source (fetched): https://developer.apple.com/app-store/review/guidelines/ · https://developer.apple.com/app-store/user-privacy-and-data-use/

## 3. Google Play — what the policy must say
The User Data policy requires the policy to comprehensively disclose: **developer identity + privacy
contact**; **all personal/sensitive data accessed/collected/used/shared**; **recipient parties (incl.
third-party SDKs)**; **security practices**; **retention + deletion**; be **labeled "privacy policy"**;
and live at an **active, public, non-geofenced, non-PDF, non-editable URL** (in Play Console AND in-app).
The **Data Safety section must match the privacy policy**. **Prominent Disclosure & Consent:** when
collection is background/unexpected, an in-app runtime disclosure + **affirmative consent before
collection** is required — a policy alone is NOT enough.
Source (fetched): https://support.google.com/googleplay/android-developer/answer/10787469 · https://support.google.com/googleplay/android-developer/answer/10144311 · https://support.google.com/googleplay/android-developer/answer/9888076
(Google "Designed for Families" policy: verify at https://support.google.com/googleplay/android-developer/answer/9893335 — UNVERIFIED specifics.)

---

## 4. Third-party tools → what each obliges you to DISCLOSE

| Tool | Must disclose in the policy | Consent gate (EU) | Source |
|------|------------------------------|-------------------|--------|
| **Google Analytics (GA4)** | use of GA; cookies/identifiers/mobile-ad-IDs collect traffic data; data processed by Google; any Advertising Features + opt-outs; link to "How Google uses information…"; **no PII may be sent to Google** | Consent before tags fire; **Consent Mode v2** (`ad_user_data`,`ad_personalization`) required for EEA/UK since **6 Mar 2024** | https://www.google.com/analytics/terms/default.html · https://support.google.com/google-ads/answer/13695607 |
| **AdSense/AdMob/Ads** | third parties incl. Google use cookies to serve ads based on prior visits; how to opt out (Google Ads Settings, aboutads.info); name other ad networks | Explicit consent for personalized ads to EEA users; **NPA fallback**; Google-certified CMP + Consent Mode | https://support.google.com/adsense/answer/1348695 · https://support.google.com/adsense/answer/7670013 |
| **Meta Pixel / CAPI** | Pixel/CAPI is used; data shared with Meta (Meta Platforms Ireland for EEA) for measurement/targeting; transfer to US under SCCs; link to Meta data policy | **Must NOT fire before consent** in the EU (most common GDPR violation); verifiable consent required | https://www.facebook.com/legal/technology_terms |
| **Stripe** | Stripe processes payment data (card, billing, name, email, IP, device, transaction); acts as **both processor AND independent controller** (fraud/AML); full card data handled by Stripe (PCI scope); link to Stripe privacy | Lawful basis; merchant provides notices | https://stripe.com/legal/dpa |
| **PayPal** | PayPal used as processor; acts as an **independent data controller** of data it receives; link to PayPal privacy statement; payment completed on PayPal's systems | — | https://www.paypal.com/us/legalhub/paypal/data-protection |
| **Mailchimp** | email processor used; subscriber data (email, name, open/click tracking, IP); lawful basis (consent for marketing); transfer mechanism (DPF/SCCs); unsubscribe/withdraw | DPA required for EEA/UK/CH contacts | https://mailchimp.com/gdpr/ |
| **Cloudflare / CDN** | CDN/security provider processes connection/log data incl. **IP addresses** + request metadata for delivery/caching/DDoS; basis = legitimate interest (security); DPA/SCCs in place | Security cookies (`__cf_bm`) often "strictly necessary" — confirm per deployment | https://www.cloudflare.com/privacypolicy/ |
| **Hotjar / FullStory (session recording)** | session recording/heatmaps capture interactions; input masking applied; purpose (UX); **basis = consent** (not strictly necessary); retention; opt-out | **Consent-gate before recording** (Hotjar records on script load by default) | https://help.hotjar.com/hc/en-us/articles/36819990621073-Processing-Personal-Data-in-Hotjar |
| **A/B testing (Optimizely/VWO/AB Tasty)** | variant-assignment cookies; purpose (optimization); **basis = consent** (not strictly necessary) | **Consent before cookies set** — common trap is setting on script load | https://www.convert.com/blog/privacy/analytics-and-a-b-testing-cookies-only-after-consent-in-europe/ |

---

## 5. Cookies & tracking infrastructure
- **Cookie banners/CMPs** are required where you have EU/EEA (and UK) visitors: **non-essential cookies
  (analytics + advertising) must not be set until the user gives explicit prior consent**; refusal as
  easy as acceptance; no cookie walls/dark patterns; scripts blocked before consent. CNIL fined Google
  €100M and Amazon €50M for failing to block cookies before consent.
- **Cookie categories (ICO-aligned):** (1) strictly necessary — exempt, interpreted narrowly; (2)
  functional/preferences — consent; (3) analytics/performance — consent (not strictly necessary); (4)
  advertising/targeting — consent.
- **IAB TCF** (Transparency & Consent Framework): adtech consent-string standard for programmatic/RTB.
  Current **v2.3** (the `disclosedVendors` segment required for strings created after **28 Feb 2026**);
  under v2.2, advertising/content-personalization vendors may rely **only on consent** (not legitimate
  interest), and the first banner layer must show the total vendor count. **Caveat:** the **TC String is
  personal data** (CJEU C-604/22, Mar 2024) and the Brussels Court of Appeal (14 May 2025) found the TCF
  failed GDPR — "we use an IAB framework" is not a compliance shield.
- **Consent logging / proof-of-consent (GDPR Art 7(1) + Art 5(2)):** record **who / what they decided /
  when / where / which notice version**; retain for the processing period + limitation period (~3–5 yrs).
Sources: https://usercentrics.com/knowledge-hub/cnil-cookies/ · https://iabeurope.eu/transparency-consent-framework/ · ICO PECR cookies guidance (https://ico.org.uk/.../cookies-and-similar-technologies/)

---

## 6. Machine-readable signals — what actually works (do this)
- **Global Privacy Control (GPC)** is the ONE machine-readable signal with legal teeth: `Sec-GPC: 1`
  header + `navigator.globalPrivacyControl` + an optional **`/.well-known/gpc.json`** declaring `gpc:true`.
  Binding in CA/CO/CT/NJ (and growing); **Sephora paid $1.2M (CA AG, Aug 2022)** for ignoring it.
  → **Action:** honor GPC, state it in the policy, and publish `/.well-known/gpc.json`.
- **P3P is dead** (W3C-obsoleted 2018; gamed by fake compact policies). **schema.org has NO adopted
  privacy-policy type** — `schema.org/PrivacyPolicy` 404s; SEO blogs claiming otherwise repeat an
  un-merged proposal. Don't waste effort there.
- **DPV (W3C Data Privacy Vocabulary)** is an emerging Community-Group taxonomy — not a standard, near-zero
  production adoption. Watch, don't deploy.
Sources: https://www.w3.org/TR/gpc/ · https://globalprivacycontrol.org/ · https://oag.ca.gov/news/press-releases/attorney-general-bonta-announces-settlement-sephora-part-ongoing-enforcement

---

## 7. AI / LLM-specific disclosures (the 2025–2026 frontier)

### 7.1 Training on user data + the retroactivity trap
- **The FTC rule:** it can be unfair/deceptive to start using already-collected data for AI training via
  a quiet, **retroactive** policy change. Material new uses (like training) generally need affirmative
  notice/consent **before** the new processing. (FTC, Feb 2024; the foundational case is *Gateway
  Learning* 2004 — "you can change the rules but not after the game has been played.")
- **Disclose:** whether user inputs/content are used to train/improve models, the basis, and an opt-out
  (or opt-in where required). **Default to NO training unless the user confirms it.**
Source: https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/02/ai-other-companies-quietly-changing-your-terms-service-could-be-unfair-or-deceptive

### 7.2 Third-party model providers as sub-processors (verified vendor postures)
If the product calls OpenAI/Anthropic/Google APIs, list them as sub-processors and state the transmission of prompts/outputs + the vendor posture:
- **OpenAI API:** data sent to the API is **not** used to train models unless you explicitly opt in; abuse-monitoring logs retained up to 30 days unless ZDR. https://developers.openai.com/api/docs/guides/your-data
- **Anthropic commercial/API:** by default does **not** train on inputs/outputs of commercial products unless you explicitly report feedback/opt in. https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training (the "7-day/30-day" API retention figures were UNVERIFIED on the primary page — don't quote them without confirming)
- **Google Gemini API / Vertex AI:** "Gemini doesn't use your prompts or its responses as data to train its models." https://docs.cloud.google.com/gemini/docs/discover/data-governance

### 7.3 Automated decision-making & profiling (rights to disclose)
- **GDPR Art 22** — right not to be subject to solely-automated decisions with legal/significant effect;
  Art 13(2)(f)/14(2)(g) require disclosing the **logic, significance, and envisaged consequences**.
  https://gdpr-info.eu/art-22-gdpr/
- **US state profiling opt-outs:** VA/CO/CT and others let consumers opt out of "profiling in furtherance
  of decisions that produce legal or similarly significant effects." **California ADMT regs** effective
  Jan 1 2026, significant-decision compliance from **Jan 1 2027** (pre-use notice + opt-out + logic access).

### 7.4 Chatbot & AI-content disclosure
- **EU AI Act Art 50** (applies from **2 Aug 2026**): tell users they're interacting with an AI at the
  latest at first interaction (unless obvious); mark AI-generated synthetic content as machine-readable;
  deployers must disclose deepfakes and AI-generated public-interest text. https://artificialintelligenceact.eu/article/50/
- **US:** California **SB 1001** (bot disclosure, since 2019); **SB 942** AI-content transparency + **AB 2013**
  training-data transparency (both effective Jan 1 2026).

> **Skill rule:** AI features → list AI sub-processors, state the training posture (default NO training),
> disclose any automated decisions (logic/significance/consequences) + opt-out, and add a chatbot
> "you're talking to an AI" disclosure. AI training on user data → HARD "get a lawyer" flag.
