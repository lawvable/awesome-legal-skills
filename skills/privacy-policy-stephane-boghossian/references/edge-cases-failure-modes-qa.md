# Reference — Edge Cases, Failure Modes, Guardrails & the Self-QA Checklist

> The safety layer. The skill runs the QA checklist (§3) on its OWN output before presenting it as
> "ready," and surfaces the disclaimers/lawyer-flags in §4. The prime directive runs through everything:
> **state only what the user confirmed; never default-in a flattering or risk-adding clause.**

---

## 1. Edge cases & correct treatment

1. **"We collect no personal data" sites — still need a policy.** Passive sites still log IPs (personal
   data under GDPR) + analytics, and Google Analytics' terms *require* a policy. → produce a minimal but
   real policy describing passive collection (server logs, analytics, essential cookies); never output
   "we collect nothing" if any analytics/hosting exists.
2. **Solo founder / pre-launch MVP / not incorporated.** The individual is the controller. → name the
   person + contact; don't imply a company exists; flag that incorporating later means updating the controller clause.
3. **Multi-entity / holding companies.** → ask which entity decides purposes/means; name THAT one as
   controller; list affiliates as recipients only if data actually flows to them (don't broaden "family of companies" loosely — that was an OkCupid trap).
4. **B2B vs B2C.** B2B still processes personal data (contacts at client companies). → don't skip the
   policy; scope to business-contact data; B2C adds consumer-rights emphasis + more state-law coverage.
5. **Selling internationally / unknown user location.** → apply **strictest-common-denominator** (GDPR +
   CCPA + COPPA); render all major jurisdiction blocks.
6. **Children & mixed-age.** under-13 → full COPPA + HARD lawyer flag; teen/mixed → age statement + minor
   protections + age-gating; not-for-kids → standard negative "we don't knowingly collect from under-13s."
7. **Health / biometric / financial / precise-geolocation.** → sensitive-data clause; GDPR Art 9 explicit
   consent; CPRA "Limit Use of Sensitive PI" link; HIPAA → separate NPP; BIPA states → biometric consent;
   always HARD lawyer flag; do NOT cite statutory damage figures.
8. **Employee / HR / applicant data.** → SEPARATE notice; exclude from the consumer policy + recommend a distinct employee notice.
9. **User-generated content & public profiles.** → disclose UGC/public fields are visible to others and may
   be indexed; user controls what they post; explain deletion limits for already-shared content.
10. **Data brokers / selling / ad-tech.** → sale/sharing clause + "Do Not Sell or Share" link + 12-month
    look-back; broker → registration flag + HARD lawyer flag. Surface that Meta/Google pixels usually count as "sharing."
11. **AI training on user data.** → explicit AI-training clause + purpose + opt-out; default NO unless
    confirmed; HARD lawyer flag if yes (OkCupid/Clarifai precedent; a policy permitting training can defeat any confidentiality expectation).
12. **Acquisitions / business transfer.** → include the standard "if we merge/are acquired, data may
    transfer as a business asset; we'll notify / the policy continues to govern" clause (near-universal, low-risk).
13. **Third-party links & embedded content.** → "not responsible for third-party privacy practices" clause;
    note embeds (YouTube, Maps, social) may set their own cookies.
14. **Do Not Track / GPC signals.** → disclose DNT response (CalOPPA requires disclosure even if "we don't
    respond"); state GPC handling — but only assert "we honor GPC" if technically true (binding in CA/CO/CT/NJ; false assertion = deception).
15. **Free vs paid / loyalty programs.** → loyalty programs exchanging data for discounts trigger the CCPA
    financial-incentive disclosure.
16. **Non-English / Arabic / multilingual.** → translated versions; RTL-aware Arabic; controlling-language
    clause; flag that machine-translated legal text needs human review (see `structure-clauses-and-craft.md` §7).

---

## 2. Failure modes & the guard the skill MUST enforce

| # | Failure mode | Guard |
|---|--------------|-------|
| F1 | **Policy doesn't match actual practice** (THE #1 legal risk — FTC §5 deception; OkCupid/Match 2026; policies are enforceable promises). | Only state what the user explicitly confirmed. No favorable defaults. Where skipped/unsure → visible `[GAP — confirm before publishing]` marker, not a guess. Output a **practices-confirmed vs clauses-generated reconciliation**. |
| F2 | **Over-promising security** (statements read as warranties). | Default to "reasonable… measures" + "no system is 100% secure"; name a specific control only if confirmed; ban "military-grade / bank-grade / 100% secure / guaranteed." |
| F3 | **Wrong boilerplate** (generic template naming the wrong law/entity/practice). | Jurisdiction-first generation: render only clauses for laws selected in intake Group 2; never carry a clause with no confirming answer. |
| F4 | **Missing mandatory jurisdiction-specific links.** | Conditional checklist: sells/shares → "Do Not Sell or Share" link; sensitive PI → "Limit Use of Sensitive PI" link; EU → supervisory-authority reference; marketing → unsubscribe. QA fails if a triggered link is absent. |
| F5 | **Gives the impression of legal advice.** | Mandatory "informational/template, not legal advice, no attorney-client relationship" disclaimer. |
| F6 | **Hallucinated statutory citations** (the zero-hallucination crux). | Do NOT invent statute/section numbers, fine amounts, or effective dates. Allowed: name the law in plain terms ("California's CCPA/CPRA," "the EU GDPR") and describe the right functionally. A precise citation may appear ONLY if it traces to the reference pack or a live `legal-data-hunter` lookup. Any uncertain specific → omit or mark UNVERIFIED. Prefer functional descriptions over quoting statutes. |

---

## 3. Self-QA checklist (run on the generated draft BEFORE presenting it as ready)
1. **Completeness** — every triggered clause present; no unresolved `[GAP]` markers (surface any that remain, don't silently ship).
2. **Internal consistency** — data-collected table, purposes, recipients, retention, rights don't contradict (e.g., "we don't sell" up top + a "Do Not Sell" section below = fail).
3. **Mandatory links present** — Do-Not-Sell-or-Share (if selling/sharing), Limit-Use-of-Sensitive-PI (if SPI), supervisory-authority reference (if GDPR), unsubscribe (if marketing).
4. **Matches stated practices** — every clause traces to a confirmed answer; no clause without a backing answer; emit the reconciliation.
5. **Jurisdiction coverage** — exactly the laws selected in Group 2 are addressed; none missing, none spurious.
6. **Controller/contact identified** — named entity/person + working contact method.
7. **Readability** — plain-language threshold met (≈8th grade unless EXPERT/formal requested); no undefined jargon.
8. **Version/date present** — effective/last-updated date + a "changes to this policy" clause (NOT "check periodically" alone).
9. **No banned vague qualifiers / over-promises** — scan for and reject "military-grade / 100% secure / fully compliant / guaranteed" and the hedging qualifiers (may/might/such as/from time to time where they hide a fact).
10. **No uncited statutory claim** — scan for statute numbers, fine amounts, effective dates; each must trace to the reference pack / live lookup or be removed/genericized. **Zero invented citations.** (This is where `cite-guard` runs, if available.)
11. **Disclaimer present** — "not legal advice" + attorney-review banner (intensity-matched).
12. **Sensitive-trigger audit** — if any HARD-flag category was selected (children/health/biometric/AI-training/data-broker/fintech), the "insist on a lawyer" banner is present.

---

## 4. Disclaimers & when to INSIST on a lawyer
- **Always include** in the output: "This is an informational template, not legal advice; using it creates
  no attorney-client relationship; have a qualified attorney review before publishing."
- **In the skill's chat** (not just the document): state up front that the output is a starting draft.
- **INSIST on a lawyer (HARD banner, recommend stopping before publishing)** when ANY are true:
  - Children under 13 (COPPA) / services to minors.
  - Health/PHI (HIPAA), biometric (BIPA states), genetic data.
  - Financial services / fintech / payments beyond a standard processor.
  - Selling data / data broker / ad-tech reselling.
  - AI training on user/customer data.
  - Large-scale processing or systematic monitoring (GDPR DPO/DPIA territory).
  - Precise geolocation at scale.
  - Multi-jurisdiction with EU/UK + US + others at once.
- **Calibrate disclaimer intensity** to the highest-risk answer in the intake (Group 0.3 + the HARD flags).

---

## 5. Output package (deliver more than a blob)
Emit: the policy (in the requested language(s), RTL-aware for Arabic) · a dated version header + change
clause · the conditional-links checklist status · the **practices-vs-clauses reconciliation** (the single
most valuable anti-deception artifact) · the `[GAP]` list · the risk-tier/lawyer banner. For non-English
output, recommend human translation review.

(Sources: FTC §5 / OkCupid-Match 2026 + Gateway Learning — see `jurisdictions-us.md` and
`structure-clauses-and-craft.md`; intake/edge-case design informed by Termly/iubenda/Osano/Termageddon/Shopify.)
