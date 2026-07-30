---
name: "privacy-policy-stephane-boghossian"
version: 1.0.0
description: "A zero-hallucination privacy-policy generator that takes anyone — non-lawyer founder to lawyer — from a guided intake to a publishable, jurisdiction-aware privacy policy. Jurisdiction-first: it detects which laws apply from where your users are, then drafts only the required clauses — GDPR/EU + UK, US (CCPA/CPRA, ~20 state laws, COPPA, sector overlays), and global/MENA (LGPD, Quebec Law 25, India DPDP, China PIPL, UAE/DIFC, Saudi PDPL), plus app-store, cookies, and AI/EU AI Act disclosures. Its rule: state only what you confirm; never invent a statute, citation, fine, or date — every claim is source-cited and QA-gated. Not legal advice."
license: AGPL-3.0
keywords: [privacy policy, privacy notice, GDPR, CCPA, CPRA, data protection, cookie policy, COPPA, app privacy, LGPD, PDPL]
language: English
triggers:
  - "write a privacy policy"
  - "create a privacy policy"
  - "generate a privacy policy"
  - "privacy policy for my app/website/SaaS/store"
  - "GDPR privacy policy"
  - "CCPA/CPRA privacy notice"
  - "I need a data protection notice"
metadata:
  author: "Stephane Boghossian"
  license: "agpl-3.0"
  version: "2026-06-30"
---

# Privacy Policy Generator

Generate a **bulletproof, jurisdiction-aware privacy policy** for any business or product, usable by a
non-lawyer founder and trusted by a lawyer. The whole point of this skill is **correctness without
hallucination**: a fabricated statutory citation or a clause that doesn't match the user's real practices
is worse than no policy at all.

## ⚖️ The prime directive (read this first, never break it)

1. **State ONLY what the user confirms they actually do.** A privacy policy is a set of *enforceable
   representations* (FTC §5; see the OkCupid/Match 2026 and Gateway Learning cases in the reference pack).
   Saying more than is true is the #1 legal failure. Never default-in a flattering or risk-adding clause.
2. **Never invent law.** Do not generate a statute/section number, a fine amount, an effective date, or a
   "the law requires X" claim unless it traces to the bundled reference pack (`references/`) or a live
   `legal-data-hunter` lookup. If you're unsure of a specific, **name the law in plain terms** ("California's
   CCPA/CPRA," "the EU GDPR") and describe the *right* functionally — or omit it. Uncertain → omit or mark
   `[VERIFY]`, never guess.
3. **Confirm-don't-assume.** A clause renders only if a confirming intake answer exists. Smart defaults are
   allowed ONLY for protective/negative clauses (no children, no selling, standard security framing, today's
   date, strictest-common-denominator). Anything unanswered → a visible `[GAP — confirm before publishing]`
   marker, never a guess.
4. **This is not legal advice.** Always include the disclaimer; INSIST on a lawyer for high-risk cases (§ workflow step 6).

## Workflow

### Step 1 — Pick the mode
Ask (or infer): **QUICK** (non-lawyer: only the must-ask questions, batched, smart defaults pre-filled, ~10
answers) or **EXPERT** (lawyer/thorough: full questions, clause-level control, citations, full reconciliation).
→ Read `references/intake-questionnaire.md` for both flows.

### Step 2 — Compute the applicable-law set FIRST (jurisdiction-first)
Ask intake Groups 0–2 (product type → business identity → **where users are located**). Location is the
law-selector. If "international / unknown," apply the **strictest-common-denominator** (GDPR + CCPA + COPPA).
This ordering is what prevents generic boilerplate.

### Step 3 — Gather practices (only the questions the selected laws require)
Work Groups 3–17 of `references/intake-questionnaire.md`. Batch questions; offer the smart default so the
user can accept with "yes." Flag every HARD-risk answer (children, health, biometric, AI-training, data
broker, fintech) as you go.

### Step 4 — Ground the legal content (zero-hallucination layer)
For each jurisdiction/topic in scope, pull the requirements from the matching reference file — never from
memory:
- `references/jurisdictions-eu-uk.md` — GDPR Art 13/14 checklist, lawful bases, rights, transfers, cookies, UK/DUAA, children ages, enforcement.
- `references/jurisdictions-us.md` — CCPA/CPRA contents + the two mandatory links + Notice at Collection, ~20 state laws, COPPA, GPC, ADMT, sector overlays, FTC §5.
- `references/jurisdictions-global-mena.md` — Brazil, Canada/Quebec, Australia, India, China, Japan/Korea/SA/Switzerland + UAE/DIFC/ADGM/Saudi/Bahrain/Qatar/Egypt/Turkey + cross-jurisdiction synthesis.
- `references/platform-cookies-ai.md` — when a policy is contractually forced; Apple/Google app-store rules; per-tool disclosures (GA, AdSense, Meta Pixel, Stripe, PayPal, Mailchimp, Cloudflare, session-recording, A/B); cookies/CMP/TCF/GPC/Consent-Mode; AI/LLM + EU AI Act Art 50 + ADM.
- `references/sector-and-special-products.md` — HIPAA/HBNR/MHMDA, GLBA, FERPA/SOPIPA, BIPA/Texas CUBI, Chrome extensions, IoT SB-327, GDPR Art 32/33/34 security/breach + US breach laws.
- **Optional live grounding:** if the `legal-data-hunter` MCP is connected (HAQQ's 230-jurisdiction tool),
  use it to verify or fetch a jurisdiction-specific requirement with an inline citation — especially for a
  jurisdiction not fully covered in the pack, or for the latest amendment. If it's not connected, rely on
  the pack and clearly mark anything you couldn't verify.

### Step 5 — Assemble the policy
Use the section order + modular clause library in `references/structure-clauses-and-craft.md` and the
fill-in backbone in `assets/template-privacy-policy.md`. Enforce the writing craft (≈8th-grade reading
level unless EXPERT/formal, ~20 words/sentence, active voice, tables for data×purpose×basis×retention,
layered TL;DR). Use the DO phrasing; never the banned phrasing. Render jurisdiction-specific sections
(e.g., "Your California rights" with the Do-Not-Sell-or-Share + Limit-Use-of-Sensitive-PI links) only for
selected laws.

### Step 6 — Self-QA gate (do NOT skip)
Run the 12-point checklist in `references/edge-cases-failure-modes-qa.md` §3 on your own draft. In
particular:
- **Citation firewall:** scan for any statute number / fine amount / effective date; each must trace to the
  pack or a live lookup, else remove or genericize. **Zero invented citations.** If `cite-guard` is
  available, run it here.
- **Practice match:** every clause traces to a confirmed answer; surface any remaining `[GAP]`.
- **Mandatory links / disclaimer / lawyer-flag present** as triggered.
Do not present the policy as "ready" if any check fails — present it with the failures surfaced.

### Step 7 — Deliver the package
Output: the policy (in the requested language(s), RTL-aware for Arabic per `structure-clauses-and-craft.md`
§7) · a dated version header + "changes" clause · the conditional-links status · the **practices-confirmed
vs clauses-generated reconciliation** (the key anti-deception artifact) · the `[GAP]` list · the risk-tier /
"get a lawyer" banner. Default output format: Markdown (offer HTML on request). Recommend human review of any
machine translation.

## Hard rules (guardrails)
- Never claim the user honors GPC / DNT, encrypts data, has a DPO, or retains data for N days unless the user
  confirmed it — these are enforceable and false ones are deceptive.
- Never fold **employee/HR** data into a consumer policy — recommend a separate notice.
- Never present this as legal advice. **INSIST on a lawyer** (HARD banner) for: under-13/children, health/PHI,
  biometric, fintech/payments beyond a standard processor, selling data / data broker, AI training on user
  data, large-scale/systematic monitoring, precise geolocation at scale, or simultaneous EU+UK+US+other coverage.
- Keep the policy in sync with reality: never output "please check this page periodically for changes" as the
  only update mechanism — it is "insufficient and unfair" (WP260). Use a dated change log + active material-change notice.

## Companion documents
A privacy policy is necessary but not sufficient. Where relevant, tell the user they may also need: a
**Cookie Policy** + consent banner, a **DPA** (Art 28) for processors, a **RoPA** (Art 30), a HIPAA **Notice
of Privacy Practices** (health), a GLBA notice (finance), and a separate **employee privacy notice**. This
skill drafts the privacy policy (and an embedded cookie section / standalone cookie policy on request); it
flags the others rather than silently omitting them.

---
*Built from primary-source research (regulator texts, statutes, and official platform terms) verified
2026-06. Sources are cited inside each `references/` file. AGPL-3.0. Informational template — not legal advice.*
