# Reference — Document Structure, Clause Library, Writing Craft & Multilingual/RTL

> This file is the OUTPUT backbone: the recommended section order, the modular clauses to assemble, the
> plain-language rules to enforce, the versioning trap to avoid, and the Arabic/RTL build rules. The
> *legal requirements* behind each clause live in the `jurisdictions-*` and `platform-cookies-ai` files.

---

## 1. Recommended table of contents (best-in-class order)
Front-load identity + purposes + rights (EDPB WP260 §36 says those three belong in the first layer),
then follow the natural who → what → why → who-we-share → how-long → your-controls → housekeeping flow.

0. **TL;DR / "In short" summary** (plain-language overview — design best practice, not a legal field)
1. **Who we are** — controller identity, address, contact; representative (if outside EU/UK); **DPO** (if any)
2. **What data we collect** — categories; for indirectly-obtained data, the **source** (GDPR Art 14)
3. **Why we use it (purposes) + legal basis** — each purpose stated concretely; Art 6 basis per purpose; named legitimate interest if used
4. **Cookies & tracking** — inline or cross-linked to a Cookie Policy; consent mechanism; GPC/DNT
5. **Who we share it with** — recipients/categories (be specific); "full list on request"
6. **International transfers** — third countries + the mechanism (adequacy / SCCs / DPF / IDTA) + how to get a copy
7. **How long we keep it (retention)** — periods or criteria, per category where possible
8. **Your rights + how to exercise them** — list the applicable rights; the right to object shown **clearly and separately**; channel + response time + free + verification
9. **Right to complain to a supervisory authority** — name/link the relevant authority
10. **Automated decision-making / AI** — existence + logic/significance/consequences; AI sub-processors; training posture; chatbot disclosure
11. **Children** — age threshold + parental consent (or the negative "we don't knowingly collect from under-13s" clause)
12. **Security** — general safeguards + "no system is 100% secure" + breach commitment
13. **Changes to this policy** — effective/last-updated date + how material changes are notified (NOT "check this page periodically")
14. **Contact / how to reach us** — repeated channel for privacy questions + rights requests
15. **Jurisdiction-specific sections** — e.g., "Your California privacy rights" (with the Do-Not-Sell-or-Share + Limit-SPI links), "Your EEA/UK rights," etc.
16. **Disclaimer** — "informational/template, not legal advice; no attorney-client relationship"

---

## 2. Modular clause library — recommended phrasing (DO) vs banned (DON'T)

**Core principle (the prime directive):** generate a clause ONLY when a confirming intake answer exists.
State only what the user confirmed they actually do. Never default-in a flattering factual claim.

**DO — concrete, definitive phrasing:**
- "We process [X data] for [specific purpose] on the basis of [named Art 6 basis]."
- "Our legitimate interest is [specific interest, e.g. preventing fraud]. You can object — see [Your rights]."
- "We share data with: [named categories — e.g. our payment processor Stripe, our hosting provider AWS]. A full list of recipients is available on request."
- "We keep [data] for [period] / until [event], then delete or anonymise it."
- "We transfer data to [country] using [mechanism]; request a copy of the safeguards at [contact]."
- "You can withdraw consent at any time by [method]; this doesn't affect prior lawful processing."
- "You can complain to [named authority] at [link]."
- "We implement reasonable administrative, technical, and physical safeguards… No method is 100% secure."

**DON'T — banned phrasing (these are documented transparency failures):**
- Open qualifiers that hide a determinable fact: *may, might, possibly, such as, including but not limited to, from time to time, where appropriate.*
- "We **may share** your data with **partners / affiliates / third parties**" (without naming categories).
- "We use your data **to improve our services / for business purposes / for research**" (without specifics).
- "**By using this website you consent** to our privacy policy" (consent ≠ notice; invalid bundling).
- Security superlatives: *military-grade, bank-grade, 100% secure, fully secure, guaranteed, fully compliant.*
- "**Please check this page periodically for changes**" as the *only* change mechanism — WP260 deems this
  "not only insufficient but also unfair." Pair it with a dated change log + active material-change notice.

**WP260 worked example:** bad = "We may use your personal data to offer personalised services"; good = "We
will keep a record of the articles you have clicked on and use that to target advertising relevant to your
interests."

---

## 3. Writing craft (enforce these on the output)
- **Reading level:** aim **~8th grade** for a broad consumer audience (NN/g); up to 12th-grade only for a
  professional audience. Write several steps below the audience's formal-education level.
- **Sentences:** short; **~20 words average**, **one idea per sentence** (Federal Plain Language Guidelines).
- **Active voice**, plain words, no excess nouns, no legalese (GDPR Art 12 + WP260).
- **Concrete & definitive**, never abstract/ambivalent. Avoid hedging qualifiers (see banned list).
- **Scannability:** use **tables** for data category × purpose × legal basis × retention (the format the ICO
  itself uses); bulleted lists; bold key phrases; sentence case (not ALL CAPS); a short glossary for
  unavoidable terms. NN/g: concise + scannable + objective writing raised usability +124%.
- **Define terms** inline or in a short glossary; add a plain-language summary alongside any unavoidable legalese.

## 4. Layered notices, dashboards, icons
- **Layered notice:** first layer = controller identity + purposes + rights (+ any high-impact/surprising
  processing); deeper detail behind expandable sections / "learn more." Layers must NOT be "several clicks
  to find the real info" (the Google/CNIL failing) and must not conflict.
- **Just-in-time** contextual notices at the point of collection; **privacy dashboards** for preference
  management; **standardised icons** (GDPR Art 12(7) permits them) for a meaningful overview.
- **Privacy "nutrition labels"** (Apple App Store style) are a good overview format — but a label is only as
  honest as the practice behind it (CMU found many inaccurate).

## 5. Versioning & maintenance (the #1 legal trap)
- **Match practice, always.** A policy is a set of enforceable representations (FTC §5; OkCupid/Match 2026).
  Saying more than you do = deception. The skill must reconcile every clause against a confirmed answer.
- **No retroactive material changes without consent.** *Gateway Learning* (FTC 2004): "you can change the
  rules but not after the game has been played." Starting AI training on already-collected data via a quiet
  policy edit is unfair/deceptive (FTC 2024).
- **Dated + change-notified.** Show a prominent "Last updated" date + a change summary; consider a public
  change log (37signals/Basecamp version their policies on GitHub). Communicate **material** changes via a
  dedicated channel (email/pop-up) — not bundled with marketing. "Please check periodically" alone is non-compliant.

## 6. Sibling documents — what belongs where
- **Privacy Policy** = ALL data handling (what/why/basis/sharing/transfers/retention/rights/complaints).
- **Cookie Policy** = ONLY cookies/trackers (categories, purpose, how to give/refuse/withdraw consent). Can
  be a section inside the privacy policy or a separate linked doc + a consent banner.
- **Terms of Service / EULA** = the contract governing *use* (acceptable use, IP/licence, liability,
  disputes) — NOT a data-handling document.
- **DPA (Data Processing Agreement)** = a B2B *contract* (GDPR Art 28) between controller and processor —
  not consumer-facing. Don't fold DPA terms into the public policy.
- **Employee/applicant notice** = a SEPARATE notice (different bases; consent generally invalid in
  employment). Don't fold HR data into the consumer policy.

---

## 7. Multilingual & Arabic / RTL build rules (for MENA / multilingual audiences)
GDPR transparency requires the audience's language; Saudi/UAE-onshore expect Arabic. Key rules for an
Arabic RTL policy (a hard case because legal text mixes RTL Arabic with LTR brand names, URLs, emails,
citations, dates, numbers):
- Set base direction with **`<html lang="ar" dir="rtl">`** (the attribute, not CSS `direction`) so it
  survives reader mode, email, and PDF. Declare `lang` separately from `dir`.
- Use **CSS logical properties** (`margin-inline-start`, `text-align: start`) — never physical
  `left/right` — so one stylesheet serves both LTR and RTL versions.
- **Isolate every embedded LTR run** (brand names, URLs, emails, phone/account numbers, dates, statute
  citations) with `<span dir="ltr">` (known direction) or `<bdi>` / `dir="auto"` (dynamic) — otherwise
  punctuation, parentheses, and digits reorder. In plain-text/attribute contexts use Unicode isolates
  (RLI/LRI/PDI, U+2066-2069), never the old embedding controls (U+202A/B).
- **No emphasis via case** (Arabic has none) — use weight/size/color and a real Arabic webfont (e.g., Noto
  Kufi Arabic) with genuine bold; never faux-bold. Generous `line-height` (~1.6–1.8) for diacritics/descenders.
- Avoid naive `justify` (no kashida support on the web) — use `text-align: start`.
- **Numerals:** Eastern Arabic-Indic (٠١٢٣) for Gulf/Levant, Western (0123) for Maghreb / pan-MENA digital
  default; be consistent; keep numeric runs isolated.
- Tables mirror: first column on the right, cells right-aligned — verify column order after mirroring.
- **PDF export is where bidi breaks** — use a UBA-aware engine and proof the PDF separately.
- Add a **controlling-language clause** (which language version governs in case of conflict) and have a
  legally-literate native Arabic speaker review the rendered page + PDF.
- Flag that a machine translation of a legal document must be human-reviewed.

### Sources (verified)
- WP260 transparency guidelines: https://www.cnil.fr/sites/cnil/files/atoms/files/wp260_enpdf_transparency.pdf
- GDPR Art 12: https://gdpr-info.eu/art-12-gdpr/ · ICO methods: https://ico.org.uk/.../what-methods-can-we-use-to-provide-privacy-information/
- NN/g readability: https://www.nngroup.com/articles/legibility-readability-comprehension/ · privacy policy mistakes: https://www.nngroup.com/articles/privacy-policies-terms-use-pages/
- Federal Plain Language Guidelines: https://www.plainlanguage.gov/howto/guidelines/FederalPLGuidelines/FederalPLGuidelines.pdf
- FTC Gateway Learning: https://www.ftc.gov/news-events/news/press-releases/2004/07/gateway-learning-settles-ftc-privacy-charges
- 37signals open-source policies: https://github.com/basecamp/policies
- W3C RTL/bidi: https://www.w3.org/International/questions/qa-html-dir · https://www.w3.org/International/articles/inline-bidi-markup/ · https://www.w3.org/International/alreq/
