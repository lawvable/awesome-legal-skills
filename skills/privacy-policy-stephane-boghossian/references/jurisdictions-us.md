# Verified Reference Pack — United States (federal + state)

> **Zero-hallucination rule:** cite only from this pack or a live `legal-data-hunter` lookup. Do NOT
> free-generate statute section numbers, per-violation fine amounts, or effective dates beyond what is
> stated and sourced here. When in doubt, name the law in plain terms ("California's CCPA/CPRA," "the
> FTC Act") and describe the *right* functionally. Last verified 2026-06.

The US has **no single federal privacy law**. Coverage = a sectoral federal layer (FTC Act, COPPA,
HIPAA, GLBA, etc.) **plus** ~20 comprehensive **state** laws. The unifying federal hook is the **FTC
Act §5**: a privacy policy is a set of **enforceable representations** — saying one thing and doing
another is an "unfair or deceptive practice." See enforcement (§7).

---

## 1. California — CCPA, as amended by CPRA (the benchmark)

**Who must comply (any one):** for-profit doing business in CA that (a) has annual gross revenue
>$25M; or (b) buys/sells/shares the personal information of 100,000+ CA consumers/households; or
(c) derives ≥50% of annual revenue from selling/sharing personal information. (Thresholds per CA AG;
verify current figures at oag.ca.gov/privacy/ccpa before quoting.)

**The privacy policy MUST disclose:**
- The **categories of personal information** collected (CCPA uses ~11 statutory categories), the
  **categories of sources**, the **business/commercial purposes**, and the **categories of third
  parties** to whom PI is disclosed/sold/shared.
- A **12-month look-back**: categories collected, sold/shared, and disclosed — or an explicit
  statement that the business has not sold/shared in the past 12 months.
- The **consumer rights** and how to exercise them: **know/access**, **delete**, **correct**,
  **opt-out of sale/sharing**, **limit use of sensitive personal information**, **non-discrimination**
  for exercising rights, and the right to use an **authorized agent**.
- Methods to submit requests + how the business verifies identity.

**Mandatory links/notices (the part founders miss):**
- **"Do Not Sell or Share My Personal Information"** link — required if the business sells PI or
  **shares** it for **cross-context behavioral advertising** (using Meta/Google ad pixels usually
  counts as "sharing"). Required since the CPRA "sharing" expansion took effect **Jan 1, 2023**.
- **"Limit the Use of My Sensitive Personal Information"** link — required if you use/disclose SPI
  beyond permitted purposes. (A single combined opt-out link / the Alt opt-out icon may be used.)
- **Notice at Collection** — at or before the point of collection, listing categories collected and
  purposes, with a link to the full policy. (A privacy policy alone does NOT satisfy the at-collection
  notice — it must be presented at collection.)
- **Global Privacy Control (GPC):** California requires businesses to treat a user-enabled GPC signal
  as a valid opt-out of sale/sharing. (See §6 + `platform-ai-cookies.md`.)

**Sensitive Personal Information (SPI) categories:** SSN/driver's licence/passport/financial account;
precise geolocation; racial/ethnic origin; religious/philosophical beliefs; union membership; contents
of mail/email/texts (not to the business); genetic data; biometric data for unique ID; health; sex
life/sexual orientation.

**Automated decision-making (ADMT):** CPPA finalized ADMT/risk-assessment/cybersecurity-audit
regulations — **effective Jan 1, 2026**, with **ADMT-for-significant-decisions compliance required
from Jan 1, 2027**. For significant decisions (financial, housing, employment, healthcare, etc.):
pre-use notice, an opt-out, and access to "meaningful information about the logic." Source:
https://cppa.ca.gov/regulations/ccpa_updates.html · https://cppa.ca.gov/announcements/2025/20250923.html

Sources: https://oag.ca.gov/privacy/ccpa · https://cppa.ca.gov/faq.html

### CalOPPA (older, still applies to ANY site collecting CA residents' data)
Requires a conspicuous privacy policy and — notably — a disclosure of **how the site responds to "Do
Not Track" (DNT)** signals (you must disclose your response even if it is "we do not respond").

---

## 2. The other state comprehensive laws (≈20 in effect in 2026)

As of 2026, ~20 states have comprehensive laws in effect; **Indiana, Kentucky, and Rhode Island took
effect Jan 1, 2026** (joining CA, VA, CO, CT, UT, TX, OR, MT, IA, DE, NJ, NH, NE, MN, MD, TN, IN, and
others). Source: https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026
· https://iapp.org/news/a/new-year-new-rules-us-state-privacy-requirements-coming-online-as-2026-begins

**Common-denominator consumer rights (most states):** access, delete, correct, data portability, and
**opt out of** (i) **sale**, (ii) **targeted advertising**, and (iii) **profiling** in furtherance of
decisions with legal/significant effects. Many add a **right to appeal** a denied request.

**Key deltas a generator must branch on:**
- **Sensitive data:** **opt-IN consent** for sensitive data in **Virginia, Colorado** (and several
  others) — vs CCPA's opt-OUT (limit) model. The skill must apply opt-in where the user's audience
  includes those states.
- **Universal Opt-Out Mechanism (UOOM / GPC):** honoring is mandatory in a growing set — California,
  Colorado, Connecticut, Texas, Oregon, Montana, Delaware, New Jersey, New Hampshire, Minnesota,
  Maryland (and more joining). The policy should state you honor GPC (only if you actually do).
- **Data protection assessments** for high-risk processing; **cure periods** vary (some sunsetting).
- Enforcement is by **state AGs** (no private right of action in these comprehensive laws, except
  narrow CCPA data-breach private action). Civil penalties commonly cited around **$7,500 per
  violation** (CCPA, intentional/minors) — verify current figure before quoting.

**Practical "comply with all states at once" recipe:** build to the **strictest common denominator**
— honor all opt-outs (sale/share, targeted ads, profiling) + GPC; offer access/delete/correct/portability
+ appeal; apply opt-IN for sensitive data; surface the two California links if you sell/share or use SPI.

---

## 3. COPPA — children under 13 (federal)

COPPA (16 CFR Part 312, FTC) applies to operators of sites/services **directed to children under 13**
or that **knowingly collect** data from under-13s. Requires: an **online notice** (a COPPA-specific
privacy policy section) + **direct notice to parents** + **verifiable parental consent BEFORE
collection**, plus data-minimization, security, and parental rights to review/delete.

**2025 Rule amendments (verified):** published in the Federal Register **Apr 22, 2025**; **effective
Jun 23, 2025**; **compliance required by Apr 22, 2026**. Key changes:
- **Biometric identifiers** and **government-issued identifiers** added to the definition of "personal
  information."
- **Separate verifiable parental consent required to disclose** children's PI to third parties (e.g.,
  for targeted advertising).
- **No indefinite retention** — retain only as long as reasonably necessary for the purpose collected;
  written data-retention policy required.
- **New VPC methods** added (e.g., knowledge-based authentication; "text-plus"; government-ID +
  facial-match).
Sources: https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data
· https://www.whitecase.com/insight-alert/unpacking-ftcs-coppa-amendments-what-you-need-know
· https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312

> **Skill rule:** any under-13 audience → full COPPA block + a HARD "get a lawyer before publishing" flag.

---

## 4. Sector overlays — FLAG, don't draft (each is a separate regime)
If the intake reveals any of these, surface a flag that the consumer privacy policy is **not
sufficient** and a specialist/lawyer is needed. Do not draft these notices generically.
- **HIPAA** — protected health information; needs a separate **Notice of Privacy Practices**.
- **GLBA** — financial institutions; needs a GLBA privacy notice.
- **FERPA** — education records.
- **VPPA** — video viewing data (active plaintiffs' bar around pixels on video pages).
- **BIPA (Illinois)** — biometric data; **private right of action** with statutory damages (do NOT
  cite specific damage figures — verify). Texas/Washington have biometric laws without a private right.
- **CAN-SPAM / TCPA** — email and SMS/call marketing rules (consent + opt-out mechanics).

---

## 5. When is a privacy policy legally required in the US?
- If you collect personal data from **California** residents (CalOPPA + CCPA-if-thresholds-met) or any
  state with a comprehensive law that applies.
- If COPPA applies (under-13 audience).
- Practically always, via **contracts** — app stores, ad networks, analytics, and payment processors
  require one regardless of statute (see `platform-ai-cookies.md`).

---

## 6. Global Privacy Control (GPC) — the enforceable signal
GPC transmits one binding intent: opt out of sale/sharing. California requires honoring it; Colorado
approved GPC as the **first recognized Universal Opt-Out Mechanism** (controller compliance by **Jul 1,
2024**); Connecticut, New Jersey and others treat it as binding. **Sephora paid $1.2M (CA AG, Aug 2022)
specifically for failing to honor GPC.** Document compliance: state it in the policy AND publish
`/.well-known/gpc.json` with `gpc: true`. Source:
https://oag.ca.gov/news/press-releases/attorney-general-bonta-announces-settlement-sephora-part-ongoing-enforcement
· https://coag.gov/opt-out/

> Only assert "we honor GPC" if the user confirms they technically do — a false assertion is itself deceptive.

---

## 7. FTC §5 + enforcement (the "must match practice" rule)
The FTC treats a privacy policy as **enforceable representations**; a gap between what the policy says
and what you do is an unfair/deceptive practice. Two anchor cases:
- **Sephora — $1.2M** (CA AG, Aug 2022): failed to process GPC opt-outs / disclose "sale."
- **FTC v. OkCupid / Match (Mar 30, 2026):** the policy said data was shared only with a limited set of
  categories; the company transferred ~3M users' photos + location + demographics to a facial-recognition
  vendor (Clarifai) for AI training with no notice/opt-out. FTC framing: "a privacy policy is not merely
  an informational document. It is a set of representations to consumers, and under Section 5, those
  representations are enforceable commitments." Source:
  https://www.parkerpoe.com/news/2026/04/ftc-cracks-down-on-privacy-policy-transparency-signaling
- FTC: **quietly/retroactively** changing your policy (e.g., to start AI training on already-collected
  data) can itself be deceptive. Source:
  https://www.consumerfinancemonitor.com/2024/02/28/ftc-warns-quietly-changing-privacy-policies-may-be-an-unfair-or-deceptive-practice/

> **Skill prime directive (US + everywhere):** state ONLY what the user confirmed they actually do.
> Never default-in a flattering clause. This single rule prevents the most common and most expensive failure.

---

## 8. California AI-transparency statutes (effective Jan 1, 2026)
- **SB 942 (CA AI Transparency Act):** large GenAI providers (>1M monthly CA users) must provide
  visible + latent disclosures on AI-generated content and a free detection tool.
- **AB 2013 (Generative AI Training Data Transparency):** developers must publicly document training-data
  sources/types and whether personal info/copyrighted material is included.
- **SB 1001 (Bot disclosure, since Jul 1, 2019):** must clearly disclose a bot when used to incentivize a
  transaction or influence a vote.
Sources: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB942 ·
https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013 ·
https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201720180SB1001

### Primary sources (verified)
- CA AG CCPA: https://oag.ca.gov/privacy/ccpa · CPPA: https://cppa.ca.gov/
- COPPA: https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy · https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312
- IAPP US State Tracker (for live state list): https://iapp.org/resources/article/us-state-privacy-legislation-tracker/
- MultiState 2026 effective-dates: https://www.multistate.us/insider/2026/2/4/all-of-the-comprehensive-privacy-laws-that-take-effect-in-2026
