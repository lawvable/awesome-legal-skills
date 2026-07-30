# Reference — The Intake Questionnaire (jurisdiction-first, confirm-don't-assume)

> This is how the skill NARROWS the request. Order: **triage → identity → jurisdiction → practices.**
> Compute the applicable-law set FIRST (Groups 0–2), then ask only the practice questions whose clauses
> those laws require (Groups 3–17). This is the proven model (Termageddon) and the antidote to generic
> boilerplate (the Shopify "fill 4 fields → generic policy" anti-pattern).
>
> **Legend:** [MUST] = legally load-bearing · [NICE] = improves accuracy/UX · *Default* = smart default
> for a non-expert · → = the clause/branch it drives.

---

## Two modes (ask which at the start, or infer)

- **QUICK mode (for anyone / non-lawyer):** ask the [MUST] questions only, batched in small groups, with
  the smart *Default* pre-filled so the user can accept with "yes." Aim to finish in ~10 answers. Use
  protective defaults for every negative/absence clause; require explicit opt-in for anything risk-adding.
- **EXPERT mode (for lawyers / thorough founders):** ask [MUST] + [NICE], offer clause-level control,
  surface legal-basis choices and citations, and expose the full reconciliation. Terser, less hand-holding.

**Confirm-don't-assume engine (applies to both modes):** maintain `clause → required answer`. A clause
renders ONLY if a confirming answer exists. *Defaults* are allowed only for **protective/negative** clauses
(no children, no selling, standard security framing, today's date, strictest-common-denominator). NEVER
default-in a **risk-adding or flattering factual** claim (selling data, AI training, biometric, specific
encryption, exact retention numbers, a DPO). Unanswered/unsure → emit a visible
`[GAP — confirm before publishing: …]` marker, never a guess.

---

## GROUP 0 — Triage (sets the whole flow)
- **0.1 [MUST]** What is this for? website / mobile app / SaaS web app / e-commerce / browser extension / IoT device / desktop software / API-B2B / multiple. *Default: website.* → template skeleton + platform clauses.
- **0.2 [NICE]** Tone: plain-language consumer / standard / formal legal. *Default: plain-language.* → readability threshold.
- **0.3 [NICE]** Publishing as-is, or lawyer-reviewing after? → calibrates how loud the attorney-review banner is.
- **0.4** Mode: QUICK or EXPERT? *Default: QUICK.*

## GROUP 1 — Business identity (the controller)
- **1.1 [MUST]** Legal entity name (+ trading/brand name). → controller clause.
- **1.2 [MUST]** Entity type (sole proprietor / LLC / Ltd / corp / nonprofit / not-yet-incorporated individual). A pre-incorporation solo founder is personally the controller — name a person. → controller clause.
- **1.3 [MUST]** Registered/business address. → contact clause + jurisdiction signal.
- **1.4 [MUST]** Privacy contact email (+ optional form/postal/phone). *Default: a dedicated privacy@ alias, not a personal inbox.* → contact + rights-exercise clause.
- **1.5 [MUST]** Domain(s)/app name(s) the policy covers. → scope clause.
- **1.6 [NICE→MUST if EU/UK targeted]** EU/UK representative appointed? (ask, don't assume) → representative clause.

## GROUP 2 — Jurisdiction (THE law-selector)
- **2.1 [MUST]** Where is the business established/operated from? → home-country law (PIPEDA/Quebec, UK DPA, Australia, POPIA, UAE/Saudi…).
- **2.2 [MUST]** **Where are your users/customers located?** US-only / specific US states / EU-EEA / UK / Canada / Quebec / Australia / India / China / MENA / "international / I don't know." → which jurisdiction sections render.
- **2.3 [MUST]** If international/unknown → apply **strictest-common-denominator** (GDPR + CCPA + COPPA)? *Default: yes.* → enables all major blocks.
- **2.4 [NICE]** Knowingly serve EU/UK residents even if not "targeting" them? → GDPR extraterritorial reach on/off.

## GROUP 3 — What data + how (the core practices block)
- **3.1 [MUST]** Which categories? (identifiers/name/email; credentials; contact; postal; **payment/financial**; device/IP; **precise geolocation**; usage/analytics; cookies/tracking IDs; UGC; photos/media; communications; purchase history; professional; education; inferences/profiles; **biometric**; **health**; **gov IDs/SSN**; **religion/politics/sexual-orientation/union**) → data-collected table; bold = sensitive branch.
- **3.2 [MUST]** For each, **how collected?** directly / automatically / from third parties or brokers / public sources. → "How we collect" + sources; any "from third parties" triggers **GDPR Art 14** source disclosure.
- **3.3 [MUST]** **Why** (purposes per category). → purposes clause.
- **3.4 [MUST if GDPR]** Legal basis per purpose (consent/contract/legal-obligation/legitimate-interests/vital/public-task). If legitimate interests → name the interest + confirm an LIA exists. *Offer a default with rationale but flag for confirmation — never silently pick.* → legal-basis clause.
- **3.5 [NICE]** Offline/other-channel collection (phone, in-store, events)? → broadens collection clause.

## GROUP 4 — Children
- **4.1 [MUST]** Directed to under-13s OR knowingly collect from them? → full **COPPA** block + **HARD lawyer flag**.
- **4.2 [MUST]** Serve teens 13–17 / mixed-age? → minors clause + age-gate recommendation.
- **4.3 [NICE]** If NOT for children → include the standard "we don't knowingly collect from under-13s; contact us to delete" clause? *Default: yes.*

## GROUP 5 — Sensitive / special-category data
- **5.1 [MUST]** Collect any health, biometric, precise geolocation, racial/ethnic, religious, political, sexual-orientation, union, genetic, financial-account, gov-ID, contents-of-communications? → GDPR Art 9 condition + CPRA "Limit Use of Sensitive PI" right/link + **HARD lawyer flag**.
- **5.2 [MUST if health]** HIPAA-covered / handling PHI? → flag a separate HIPAA Notice of Privacy Practices.
- **5.3 [NICE]** Biometric in IL/TX/WA? → biometric-consent clause + strong flag (don't cite damage figures).

## GROUP 6 — Third-party tools & sharing
- **6.1 [MUST]** Which third-party services? (analytics, ad pixels, payment processors, email/CRM, hosting/CDN, chat, embeds, AI APIs). → recipients table. *Default: list categories of recipients unless the user wants vendor names.*
- **6.2 [MUST]** For each, what data + why? → maps each recipient to data + purpose (the OkCupid lesson: an undisclosed recipient outside stated categories = deception).
- **6.3 [NICE]** DPAs in place with processors? → not in the policy verbatim; flags a compliance gap if "no."
- **6.4 [NICE]** Third-party links / embeds present? *Default: include* the "not responsible for third-party sites" clause.

## GROUP 7 — Selling / sharing for ads
- **7.1 [MUST]** Sell PI, or **share** for cross-context behavioral advertising (Meta/Google pixels usually count)? → if yes: **"Do Not Sell or Share My Personal Information"** link + 12-month look-back (or explicit "we have not sold/shared").
- **7.2 [MUST]** Use targeted/behavioral advertising at all? → triggers opt-out rights + GPC honoring.
- **7.3 [MUST if yes]** Data broker / trade in personal data? → broker disclosure + registration flag + **HARD lawyer flag**.

## GROUP 8 — Cookies & opt-out signals
- **8.1 [MUST]** Use cookies/trackers? Which types (strictly necessary / functional / analytics / advertising)? → cookies clause + (likely) separate cookie policy + consent banner.
- **8.2 [MUST for US state coverage]** Honor **Global Privacy Control (GPC)**? Only assert "yes" if technically true. → GPC clause + publish `/.well-known/gpc.json`.
- **8.3 [NICE]** Response to legacy Do Not Track (DNT)? (CalOPPA requires disclosing your response, even "we don't respond"). → DNT clause.

## GROUP 9 — AI
- **9.1 [MUST if any]** Use AI/LLMs to process user data (own feature / vendor APIs)? → AI-processing clause + list AI sub-processors.
- **9.2 [MUST]** **Train AI on user data?** *Default: assume NO unless confirmed.* If yes → AI-training clause + opt-out + **HARD lawyer flag**.
- **9.3 [MUST if GDPR / covered US state]** Automated decisions/profiling with legal/significant effects? → ADM clause (logic/significance/consequences) + opt-out.

## GROUP 10 — Payments
- **10.1 [MUST if paid]** Process payments? Self-handle card data or via processor (Stripe/PayPal)? → payments clause (say "processor handles card data, we don't store full numbers" only if true).
- **10.2 [NICE]** Loyalty/rewards program exchanging data for discounts? → CCPA financial-incentive clause.

## GROUP 11 — Marketing
- **11.1 [MUST if yes]** Send marketing email/SMS/push? → marketing clause (CAN-SPAM/CASL/GDPR consent).
- **11.2 [MUST if marketing]** Opt-out mechanism? *Default: unsubscribe link + privacy email.*

## GROUP 12 — Retention
- **12.1 [MUST]** How long do you keep data (per category if possible, else criteria)? *Default offered ("as long as needed for the stated purposes, then deleted/anonymised") but prompt for real periods.* → retention clause.
- **12.2 [MUST]** Deletion process when no longer needed / on request? → deletion clause.

## GROUP 13 — Security
- **13.1 [MUST]** What safeguards do you ACTUALLY use (encryption in transit/at rest, access controls)? *Default: "reasonable administrative, technical, organisational measures" + "no system is 100% secure" — name a specific control ONLY if confirmed.* → security clause. (Over-promising is a top failure mode.)
- **13.2 [NICE]** Breach-notification practice? → breach clause.

## GROUP 14 — International transfers
- **14.1 [MUST if EU/UK users]** Data transferred/stored outside the user's region (e.g. EU→US servers)? → transfers clause.
- **14.2 [MUST if transfers]** Which mechanism (adequacy / SCCs / DPF / IDTA)? *Default offered (SCCs) but flag for confirmation — ask, don't assume.*

## GROUP 15 — DPO & rights administration
- **15.1 [MUST if GDPR & required]** DPO appointed? *Default: none for small businesses — don't invent one.*
- **15.2 [MUST]** How do users exercise rights + how do you verify identity? *Default: via privacy email + verification.*
- **15.3 [MUST for VA/CO/CT etc.]** Right to appeal a denied request? → appeal clause (derive states from G2).

## GROUP 16 — Employee / HR data
- **16.1 [MUST]** Does this policy need to cover employees/applicants/contractors? *Default: NO — scope to consumers/users and emit a "HR data needs its own notice" recommendation.*

## GROUP 17 — Versioning, governing law, language
- **17.1 [MUST]** Effective/last-updated date. *Default: today.* → version block.
- **17.2 [MUST]** How will you notify users of material changes? *Default: post new version + update date; email for material changes.* (Never "check this page periodically" alone.)
- **17.3 [NICE]** Governing law / disputes (often in the ToS, optional here).
- **17.4 [NICE→MUST if non-English audience]** Languages needed (English / Arabic / multilingual)? → translated, RTL-aware output + controlling-language clause.

---

## Smart-default philosophy (so a non-expert finishes fast)
Pre-select the protective/conservative answer for every negative/absence clause (no children, no selling,
no AI training, standard security framing, today's date, strictest-common-denominator). Require explicit
opt-in for anything that adds risk (selling data, AI training, biometric/health, data-broker). NEVER
default-in a flattering factual claim — those are enforceable and must be user-confirmed.

(Sources for question→law mapping: see the `jurisdictions-*`, `platform-cookies-ai`, and
`sector-and-special-products` reference files; intake design informed by Termly/iubenda/Osano/Termageddon/Shopify generators.)
