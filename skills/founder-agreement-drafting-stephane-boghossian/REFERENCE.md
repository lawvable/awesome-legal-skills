# Reference — Founder / Co-Founder Agreements: Best Practices for Drafting

> Research backbone for a `founder-agreement-drafting` Claude skill. Compiled 2026-07-06 from primary
> sources — Y Combinator, Cooley GO, Clerky, Carta, Orrick (incl. its Stripe Atlas Legal Guide), Gunderson
> Dettmer, Wilson Sonsini, SeedLegals, Slicing Pie (Mike Moyer), Noam Wasserman / HBS (*The Founder's
> Dilemmas*), NBER, IRS/Treasury regulations, and named case law — via live web search and fetch.
> Every claim below carries an inline source. Where sourcing is thin or unverifiable (mainly MENA
> founder-specific mechanics, and a handful of widely-repeated but untraceable statistics), that is
> flagged explicitly rather than papered over — see **§10 Sourcing Notes**.
>
> This is a drafting aid, not legal advice. See **§9 Ethics & Scope** before operationalizing.

---

## Contents

1. [What a Founders' Agreement Is](#1-what-a-founders-agreement-is)
2. [The Canonical Clause List](#2-the-canonical-clause-list)
3. [Equity Split Frameworks](#3-equity-split-frameworks)
4. [Vesting Deep-Dive](#4-vesting-deep-dive)
5. [IP Assignment](#5-ip-assignment)
6. [Leaver / Departure Mechanics](#6-leaver--departure-mechanics)
7. [Top Founder Disputes & Mistakes](#7-top-founder-disputes--mistakes)
8. [Entity & Jurisdiction Variation](#8-entity--jurisdiction-variation)
9. [Ethics & Scope](#9-ethics--scope)
10. [Sourcing Notes](#10-sourcing-notes)

---

## 1. What a Founders' Agreement Is

### 1.1 It is a category, not a standard instrument

Unlike a certificate of incorporation, a "founders' agreement" (or "co-founders' agreement") is not one
standardized document — US market practice is genuinely split on whether it should exist as a
free-standing instrument at all.

- **Cooley GO**: "most companies do not use a stockholder agreement at the time of formation" — founders
  instead rely on default Delaware corporate law, bylaws, and vesting agreements; "for most companies,
  these default rules, agreements and the trust between founders is sufficient." Where one is used, it
  typically covers three things: **governance** (board election, officers), **transferability** (rights
  over stock sales), and **buyout scenarios** (death, disability, termination).
  [Cooley GO, *Should You Have Founder Shareholder Agreements?*](https://www.cooleygo.com/founder-shareholder-agreements/)
- **Clerky**: it is "pretty rare for US startups to have one single 'founders agreement.'" What such an
  agreement would cover is instead scattered across the **Restricted Stock Purchase Agreement** (equity +
  vesting), the **CIIA/PIIA** (Confidential Information and Invention Assignment Agreement — "effectively
  synonymous with... Proprietary Information and Invention Assignment Agreement"), the **bylaws**
  (governance), and default Delaware law.
  [Clerky, *Legal Concepts for Founders*](https://handbooks.clerky.com/legal-concepts) ·
  [Clerky glossary](https://handbooks.clerky.com/glossary)
- **Startup Boston** goes further: a standalone founders' agreement can itself be a symptom of
  "deficiencies in the company's practices around issuing founder equity" or in founder communication, and
  such agreements "are disfavored by many seasoned investors" as a possible diligence red flag — "usually
  wiser to address the underlying issues... than to paper over them with a Founders' Agreement."
  [Startup Boston, *Do Founders' Agreements Solve More Problems Than They Create?*](https://www.startupbos.org/post/do-founders-agreements-solve-more-problems-than-they-create)

**Practical read for the skill**: treat "founders' agreement" as the *substantive terms* (equity, vesting,
IP, leaver, decision-making) rather than insisting on one physical document. Draft those terms into
whichever instrument the entity type and stage actually call for (RSPA + CIIA + bylaws for a Delaware
C-corp; the operating agreement for an LLC; Articles + a separate Shareholders' Agreement for a UK Ltd) —
and use a genuine standalone founders' agreement mainly as the **pre-incorporation bridge document**
before those instruments can exist.

### 1.2 Distinguishing it from the other documents

| Document | What it actually governs | Relationship to a founders' agreement |
|---|---|---|
| **Certificate / Articles of Incorporation** | Brings the entity into legal existence at the state level; the charter | Sits above everything else — nothing else has legal effect until filed. [Clerky](https://handbooks.clerky.com/legal-concepts/core) |
| **Bylaws** | Internal governance adopted post-filing (board size, initial directors, transfer-approval mechanics) | Where "governance" terms people expect in a founders' agreement often actually live — e.g. board approval requirements for stock transfers. [Cooley GO](https://www.cooleygo.com/founder-basics-founders-stock/) |
| **Shareholders' / Stockholders' Agreement** | Founder-level governance, transfer restrictions, buyout terms | Functionally the closest analog to a "founders' agreement" post-incorporation — but **expected to be superseded** the moment the company raises a priced round, replaced by the NVCA-style investor stack (Voting Agreement, ROFR/Co-Sale, Investors' Rights Agreement). [Cooley GO](https://www.cooleygo.com/founder-shareholder-agreements/) |
| **Stock Purchase Agreement / Restricted Stock Purchase Agreement (RSPA)** | Where founder **vesting is actually implemented** — price paid, vesting schedule, company repurchase right | This is the real mechanism; a founders' agreement that says "we'll vest over 4 years" is only intent until an RSPA + board resolution + timely 83(b) election exist. [Cooley GO](https://www.cooleygo.com/founder-basics-founders-stock/) · [Orrick Start-Up Forms](https://www.orrick.com/Total-Access/Tool-Kit/Start-Up-Forms/Founders-Stock-Purchase) · [Gunderson Dettmer Catalyze](https://catalyze.gunder.com/en/knowledge-articles/resource/formation) |
| **LLC Operating Agreement** | Combines what a corporation splits across certificate/bylaws/stockholders' agreement — ownership %, contributions, management, buy-sell, dissolution — in one document | For an LLC, this document generally **IS** the founders' agreement; there is no separate instrument. [Harbour Business Law](https://harbourbusinesslaw.com/when-do-i-need-a-founder-agreement-versus-an-operating-agreement/) |

### 1.3 Why sign before incorporation

**Risks a pre-incorporation agreement mitigates:**

- **Orphaned IP** — pre-entity work product (code, deck, prototype) has no automatic corporate owner.
  Gunderson Dettmer recommends a **Technology Assignment Agreement** to transfer pre-formation IP once the
  entity forms. [Gunderson Dettmer](https://catalyze.gunder.com/en/knowledge-articles/resource/formation)
- **A contributor walking away with the idea** — nothing legally binds an early participant absent a
  pre-formation commitment.
- **Equity-split ambiguity hardening into resentment** — YC: deciding early "avoids extended
  negotiations," but the timing tradeoff cuts both ways (see §3 on the "quick handshake" penalty).
  [YC, *5 ways to split equity among co-founders*](https://www.ycombinator.com/library/5x-how-to-split-equity-among-co-founders)
- **Ambiguity about who even counts as a "founder"** — directly determines what a departing contributor
  keeps. YC explicitly warns against treating part-time contributors as full co-founders.
  [YC, *Co-Founder Equity Mistakes to Avoid*](https://www.ycombinator.com/library/LP-co-founder-equity-mistakes-to-avoid)

**What it typically contains pre-incorporation**: IP assignment intent (interim mutual assignment, or a
commitment to assign to the future entity); equity-split intent; vesting intent (4yr/1yr cliff is already
the converged standard — see §4); roles/titles and decision-making intent; and pre-incorporation breakup
terms. YC's concrete numbers for a founder leaving pre-cliff: **token equity only (2–5%)**; post-cliff,
cap around **5%** or negotiate a return, with board resignation and signed releases.
[YC, *Co-Founder Equity Mistakes to Avoid*](https://www.ycombinator.com/library/LP-co-founder-equity-mistakes-to-avoid)

**What gets formalized later, and supersedes it**: equity intent → shares actually issued under the RSPA
at par value via board resolution; vesting intent → the real vesting schedule in the signed RSPA plus a
timely 83(b) election; IP intent → the actual CIIA/PIIA; governance intent → the certificate + bylaws.
Cooley GO's outer boundary: "any stockholder agreement will be replaced by a new set of agreements
requested by the investors" at the first priced round.
[Cooley GO](https://www.cooleygo.com/founder-shareholder-agreements/)

**Drafting implication**: build an explicit termination/supersession clause into any pre-incorporation or
early founders' agreement, tying its expiry to an objectively verifiable event (RSPA execution, priced
financing close) and naming which terms (typically confidentiality, IP) survive independently via the
CIIA anyway.

---

## 2. The Canonical Clause List

Full clause-by-clause matrix. "What it does" and the single most common drafting trap for each. Depth on
equity, vesting, IP, and leaver terms — the highest-dispute clauses — is in §§3–6; this table stays
concise for those and is comprehensive for the rest.

| # | Clause | What it does | Drafting trap | Source |
|---|---|---|---|---|
| 1 | **Parties & entity** | Defines who is a "founder" and what entity (existing or to-be-formed) the agreement flows into; ties each founder to a functional area (product, eng, sales, IP) | Treating "founder" as self-evident — a pre-incorporation contributor later claims founder status despite never being a named party, or a genuine early technical cofounder is left off because the agreement was drafted only post-incorporation | [Clerky](https://handbooks.clerky.com/legal-concepts/formation) · [San Jose Business Lawyers Blog](https://www.sanjosebusinesslawyersblog.com/what-you-need-to-know-about-pre-incorporation-founders-agreements/) |
| 2 | **Equity ownership & split** | Fixes each founder's % at formation | Reflexive 50/50 or equal-N-way split negotiated in under a day with no documented rationale — see §3 | [YC](https://www.ycombinator.com/blog/splitting-equity-among-founders/) · [Carta](https://carta.com/data/founder-equity-split-trends-2024/) |
| 3 | **Vesting & cliff** | Reverse-vesting: shares issued up front subject to company repurchase right that lapses over time | The cliff-edge discontinuity (month 11 = 0%, month 13 = 25%) misunderstood until a departure is final; or skipping vesting entirely — see §4 | [Clerky](https://help.clerky.com/article/1736-what-are-customary-stock-vesting-terms-for-startup-founders) · [Cooley GO](https://www.cooleygo.com/founder-basics-founders-stock/) |
| 4 | **Acceleration (single vs. double trigger)** | Governs whether/when unvested shares accelerate on a change of control | Single-trigger acceleration removes acquirer retention leverage and can depress deal price or kill it; double-trigger's protection is only as strong as the "Cause"/"Good Reason" definitions | [Orrick](https://www.orrick.com/en/Insights/2026/04/Single-and-Double-Trigger-Vesting-Acceleration-What-founders-and-employees-should-know) · [Pulley](https://pulley.com/guides/single-trigger-vs-double-trigger-acceleration) |
| 5 | **Roles & titles** | Assigns formal title *and* the decision authority behind it | Over-indexing on the title label while leaving actual authority undefined — "two founders both thinking they're CEO" | [Ramp](https://ramp.com/blog/what-is-in-a-startup-founder-agreement) · [Equity Matrix](https://equitymatrix.io/blog/founder-agreements-what-to-include) |
| 6 | **Responsibilities & time commitment** | Specifies expected hours/exclusivity; should directly drive the equity split | Locking an equal split while one founder is full-time and another moonlights ~10hrs/week off a day job, with no correction mechanism | [Pillsbury Propel](https://www.pillsburypropel.com/guidance/how-to-split-equity-between-co-founders-and-stay-friends) |
| 7 | **Decision-making / voting / board** | Governs major-decision authority pre-financing and board composition post-financing | Accepting governance terms pre-financing that hand investors authority with no safeguards; or over-correcting with unanimous-consent requirements that hand a minority founder a structural veto over routine matters | [Paul Graham, *Founder Control*](https://www.paulgraham.com/control.html) · [Valle Legal](https://www.vallelegal.com/insights/protecting-founder-control) |
| 8 | **Deadlock resolution** | Pre-agreed procedure for breaking a founder tie (acute in 50/50 splits) | **No mechanism at all** — the only recourse becomes judicial dissolution; or treating a shotgun/buy-sell clause as routine when it selects for who has cash, not who's right | [SPZ Legal](https://spzlegal.com/blog/incorporation/how-to-resolve-deadlock-in-50-50-founder-situations) · [Bianchi Fasani Green Law](https://bfg.law/deadlock-provisions-shareholder-operating-agreements/) |
| 9 | **IP assignment** | Present-tense ("hereby assigns") transfer of founder-created IP to the company | Future-tense "will assign" language — see §5 (*Stanford v. Roche*) | [Patent Docs](https://patentdocs.org/2011/06/06/board-of-trustees-of-the-leland-stanford-junior-university-v-roche-molecular-systems-inc-2011/) |
| 10 | **Confidentiality** | Mutual non-disclosure between cofounders re: trade secrets, business plans, pre-incorporation discussions | No survival clause (duty appears to lapse at departure, exactly when leak-incentive peaks); definition scoped only to post-incorporation "Company Confidential Information," missing pre-entity discussions | [Orrick Legal Guide for Stripe Atlas, pp.16-17](https://stripe.com/files/atlas/orrick-legal-guide.pdf) |
| 11 | **Non-compete / non-solicit** | Restricts a departing founder from competing / poaching | Highest enforceability risk in the whole document — see the jurisdiction table below | [Justia Cal. B&P §16600](https://law.justia.com/codes/california/code-bpc/division-7/part-2/chapter-1/section-16600/) |
| 12 | **Leaver provisions & buyback** | Good-leaver/bad-leaver distinctions; repurchase of vested shares on departure | "Cause"/"good reason" left undefined; single-founder companies often have **no vesting at all** initially — see §6 | [Orrick Legal Guide, pp.19-22](https://stripe.com/files/atlas/orrick-legal-guide.pdf) · [Ledgy](https://ledgy.com/blog/good-leaver-bad-leaver-clauses) |
| 13 | **Transfer restrictions / ROFR** | Blocks third-party transfer without company/founder consent; ~30-day matching window is standard | A pledge of shares as loan collateral not captured as a "transfer" needing consent bypasses the ROFR window on default; community-property-state spouses can hold an independent interest unless they also sign | [Orrick Legal Guide, p.24](https://stripe.com/files/atlas/orrick-legal-guide.pdf) · [NVCA Model ROFR](https://nvca.org/wp-content/uploads/2019/06/NVCA-Model-Document-Right-of-First-Refusal.docx) |
| 14 | **Capital contributions & future funding** | Addresses cash vs. sweat-equity contribution; founders can pay for shares by IP assignment, with cash owed only for any shortfall | Over-specifying financial terms (e.g. unanimous-consent capital calls) that a real VC term sheet will simply override — keep this deliberately light and springing/superseded | [Orrick Legal Guide, p.22](https://stripe.com/files/atlas/orrick-legal-guide.pdf) |
| 15 | **Salaries / expense reimbursement pre-revenue** | Governs pre-funding pay and expense documentation | Unequal informal pay with nothing in writing; commingling personal/business expenses (double risk: IRS recharacterization + corporate-veil piercing) | [Bend Law Group](https://www.bendlawgroup.com/post/catch-22-founders-must-pay-themselves-even-before-their-company-earns-revenue) |
| 16 | **Dispute resolution** | Negotiation → mediation → binding arbitration; governing law/venue | **No mechanism at all** — cited as a direct contributing factor in the Housing.com founder dispute (9 of 12 original founders exited by 2016); or a venue impractical for where founders actually live | [AAA clause drafting](https://www.adr.org/clause-drafting/) · [iPleaders](https://blog.ipleaders.in/co-founders-agreement-disputes-suggestions/) |
| 17 | **Amendment** | Specifies who must consent, and how, to change the agreement | Silent/ambiguous procedure invites a claim that an informal message constituted an amendment; requiring unanimity even from departed-but-still-holding founders hands them a unilateral veto | [Law Insider clause bank](https://www.lawinsider.com/clause/founders-agreement) |
| 18 | **Term & exit / termination of the agreement itself** | Defines when the agreement stops governing — usually tied to a priced-financing close | Never specifying a termination/superseding event, leaving ambiguity about whether the agreement conflicts with later NVCA-style docs | [Law Insider](https://www.lawinsider.com/clause/founders-agreement) · [Orrick UK Founder Series](https://www.orrick.com/en/Insights/2022/06/Founder-Series-Top-Tips-to-Follow-When-Setting-Up-Your-Private-Limited-Company) |

### 2.1 Non-compete / non-solicit — enforceability caveat detail (clause 11 above, expanded)

This is the single most jurisdiction-volatile clause in the list, and should be flagged in the skill as
needing a **live-law check at time of use**, not permanently fixed text:

- **California (Bus. & Prof. Code §16600)**: near-total ban — void "no matter how narrowly tailored,"
  outside the narrow M&A exception (§16601, requires sale of *goodwill* or *all* ownership interest; courts
  void outright rather than blue-pencil). 2024 amendments (SB 699/§16600.5, AB 1076/§16600.1) extended
  reach to out-of-state noncompetes if the worker later works/resides in CA, required individualized
  notice by Feb 14 2024, with **$2,500-per-violation** penalties.
  [Justia](https://law.justia.com/codes/california/code-bpc/division-7/part-2/chapter-1/section-16600/) ·
  [Shulman Rogers](https://www.shufirm.com/recent-amendments-to-california-business-and-professions-code-section-16600-sharper-teeth-for-a-potent-statute-and-a-serious-trap-for-unwary-employers)
- **US state patchwork (as of March 2026)**: total bans in California, Minnesota, Montana, North Dakota,
  Oklahoma, Wyoming; income-threshold restrictions in Colorado, D.C., Illinois, Maine, Maryland,
  Massachusetts, Nevada, New Hampshire, Oregon, Rhode Island, Virginia, Washington; Florida's 2025 CHOICE
  Act moved the opposite direction (up to 4-year terms enforceable for high earners).
  [Katz Banks Kumin, March 2026 update](https://katzbanks.com/employment-law-blog/noncompete-agreements-whats-the-status-of-laws-restricting-them-nationwide-march-2026-update/)
- **Federal status (as of 2026-07-06 — the date of this research)**: the FTC's 2024 nationwide noncompete
  ban was vacated in *Ryan LLC v. FTC* (N.D. Tex., Aug. 2024); the FTC voted 3-1 on Sept. 5 2025 to drop
  its appeal and accede to the vacatur, removing the rule from the CFR effective Feb. 12 2026. **There is
  no federal noncompete ban today** — the FTC now pursues case-by-case Section 5 enforcement instead.
  [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2025/09/federal-trade-commission-files-accede-vacatur-non-compete-clause-rule) ·
  [Federal Register](https://www.federalregister.gov/documents/2026/02/12/2026-02866/) ·
  [Duane Morris](https://www.duanemorris.com/alerts/ftc_abandons_appeals_decisions_striking_down_noncompete_rule_restrictive_covenants_remain_0925.html)
- **UK**: restraint-of-trade doctrine requires reasonableness; 6 months is the outer limit for most roles,
  12 months only for board/C-suite; courts have voided shareholder-agreement non-competes broader than the
  departing shareholder's own role. [DavidsonMorris](https://www.davidsonmorris.com/restraint-of-trade/)
- **Drafting fix for CA-facing companies**: skip the non-compete entirely; rely on confidentiality +
  trade-secret protection + IP assignment + a narrowly tailored **non-solicit** of employees/customers
  (restricts a relationship, not the ability to practice a trade — survives scrutiny far more often).

---

## 3. Equity Split Frameworks

### 3.1 The case against reflexive 50/50 (or equal N-way) splits

The empirical backbone here is **Hellmann & Wasserman, "The First Deal: The Division of Founder Equity in
New Ventures,"** NBER Working Paper w16922 — dataset of **1,476 founders across 511 private ventures**.
[NBER paper](https://www.nber.org/papers/w16922) · [NBER Digest summary](https://www.nber.org/digest/aug11/division-founder-equity-new-ventures)

- **~33% of founding teams split equity perfectly equally.**
- Three founder characteristics significantly *reduce* the likelihood of an equal split, and meaningfully
  raise a founder's equity premium when splits are unequal: **idea generation, prior entrepreneurial
  experience, and capital contribution.**
- Equal splitting correlates with **lower pre-money valuations** at first financing — the effect is
  strongest when the split was negotiated in **under a day**.
- **Cost estimate for the stronger founder in a too-generous equal split**: roughly **10% of total firm
  equity**, or **~25% of that founder's average stake** — an estimated **$450,000 NPV** left on the table.

From Wasserman's broader dataset (*The Founder's Dilemmas*, Princeton/Kauffman, 2012 —
[HBS listing](https://www.hbs.edu/faculty/Pages/item.aspx?num=42425)):

- **73% of founding teams split equity within one month of founding**, often without real negotiation.
  [noamwasserman.com](https://www.noamwasserman.com/category/equity-split/)
- **The "quick handshake" finding**: teams that negotiated an equal split in **one day or less**
  ("quick-equal") suffered a measurable negative valuation effect at first institutional financing; teams
  that spent longer negotiating an equal split ("slow-equal") did not. The problem is the *speed/
  superficiality* of the decision, not equality per se.
  [Inc. Magazine, summarizing Wasserman](https://www.inc.com/magazine/201406/leigh-buchanan/how-to-split-founder-equity.html)
- Wasserman's own framing of why founders default to quick equal splits: they are "too optimistic, lack
  information to make another choice, or want to avoid a contentious issue" — and a rapid even split
  "suggests that the founders don't have the business maturity to have a tough dialogue."
  [Inc. Magazine](https://www.inc.com/magazine/201406/leigh-buchanan/how-to-split-founder-equity.html)
- **Team unhappiness nearly triples** in teams that default to an equal split vs. teams that negotiate a
  differentiated one. [Inc. Magazine](https://www.inc.com/magazine/201406/leigh-buchanan/how-to-split-founder-equity.html)

> **Important framing note**: this is a critique of *fast, undocumented* equal splits, not of equal splits
> as such. Carta's more recent data (below) shows equal splits are becoming *more* common as full-time-
> from-day-one teams become the norm — not a contradiction, but a different population (deliberate parity
> among genuinely equal contributors vs. reflexive parity papering over real asymmetry).

**Canonical illustrative pairing** (used by Wasserman himself to teach this):

- **Zipcar** — Robin Chase proposed a 50/50 handshake split to Antje Danielson at their first meeting,
  explicitly to avoid a negotiation. Chase went full-time as CEO; Danielson kept outside employment. Chase
  later said: *"That first handshake caused a huge amount of angst over the next year and a half."*
  Danielson was pushed out of operational involvement in Jan 2001 while retaining her full 50% stake; by
  Zipcar's 2011 IPO, Chase (the operating founder) had been diluted to roughly 3%.
  [Gunderson Dettmer](https://www.gunder.com/en/news-insights/insights/splitting-the-pie-how-savvy-founders-divide-ownership-and-navigate-other-founder-equity-decisions) ·
  [Equity Matrix](https://equitymatrix.io/blog/famous-cofounder-disputes)
- **Ockham Technologies** — three cofounders split 50/30/20 based on capital contributed, *with
  conditional vesting* requiring full-time participation after one year or forfeiture — the dynamic/
  conditional structure Wasserman contrasts favorably against Zipcar's static handshake.

### 3.2 Factors that should drive an unequal split

Wasserman's three statistically significant drivers (from the NBER paper): **idea generation, prior
founding experience, capital contributed.**
[NBER Digest](https://www.nber.org/digest/aug11/division-founder-equity-new-ventures)

| Factor | Documented premium | Source |
|---|---|---|
| **Idea origination** | ~10–15 percentage points more equity for the idea originator vs. co-founders (e.g. ~50% vs. ~35% in IT ventures; somewhat lower, ~10pp, in life sciences) | [CBS News](https://www.cbsnews.com/news/what-the-idea-guy-is-worth-at-equity-split/) · [noamwasserman.com](https://www.noamwasserman.com/2008/05/01/idea-people-and-their-initial-roles-within-founding-teams/) |
| **Prior founding/entrepreneurial experience** | ~7–9 extra points vs. first-time cofounders | [Inc. Magazine](https://www.inc.com/magazine/201406/leigh-buchanan/how-to-split-founder-equity.html) |
| **CEO designation / role criticality** | ~14–20 extra points in some secondary syntheses *(medium confidence — not traced to a specific Wasserman primary figure)* | [Inc. Magazine](https://www.inc.com/magazine/201406/leigh-buchanan/how-to-split-founder-equity.html) |
| **Capital contributed** | Confirmed significant driver of unequal splits and share premiums | [NBER](https://www.nber.org/digest/aug11/division-founder-equity-new-ventures) |

Practitioner framework (Melissa Kwan, founder, on rejecting 50/50): weight **financial contribution and
personal liability, scope of responsibility, and risk tolerance/sacrifice** — list every responsibility
needed to build the business, assess each cofounder's capacity for those tasks, then split accordingly.
[melissakwan.com](https://www.melissakwan.com/p/cofounders-split)

**Gust's cofounder equity-split tool** — a long-standing free calculator — scores backward-looking factors
(background, skills, relevant experience) and forward-looking factors (full-time vs. part-time commitment,
sweat equity, expected role) to produce a recommended split, explicitly designed to force the "hard
conversation" investors expect founders to have already had.
[Gust tool](https://cofounders.gust.com/) ·
[Gust blog](https://gust.com/blog/cofounder-equity-split-framework-objectively-divide-equity/)

**Common practitioner rubric** (Capbase, ICanPitch, and similar calculators — vendor sources, illustrative
of consensus rather than validated data): idea, domain expertise, time commitment, capital, technical/
execution skill, network, risk tolerance, prior experience, leadership/role criticality — with
**replaceability** as a multiplier: a founder whose contribution is hard to replace commands materially
more equity than an easily-substituted role.
[Capbase calculator](https://capbase.com/startup-equity-calculator/)

### 3.3 Dynamic vs. fixed splits — Slicing Pie

**Origin**: Mike Moyer, *Slicing Pie: Funding Your Company Without Funds* (2012).
[Slicing Pie Handbook (free sample)](https://slicingpie.com/wp-content/uploads/2016/09/Slicing-Pie-Handbook-FREE-SAMPLE.pdf)

**Core principle**: *"A person's percentage share of the company's rewards should always be equal to that
person's percentage share of risk to attain those rewards."* Ownership floats dynamically based on
ongoing at-risk contributions and only fixes ("bakes") at a defined trigger event.
[Equity Matrix, Slicing Pie guide](https://equitymatrix.io/blog/slicing-pie-guide)

**The "Grunt Fund" mechanic** — ownership % = an individual's **slices** ÷ **total slices**, where
contributions convert to slices via risk multipliers:

| Contribution type | Typical multiplier |
|---|---|
| Unpaid/below-market time (valued at fair market hourly rate) | ~2x |
| Cash invested | 2x–4x (most at-risk/illiquid) |
| Equipment/supplies/IP | 1x–2x, at fair market or replacement cost |
| Deferred commissions/royalties | ~2x |
| Relationships/sales introductions | typically 5–10% of resulting deal value |

[Equity Matrix, Slicing Pie guide](https://equitymatrix.io/blog/slicing-pie-guide) ·
[Slicing Pie Grunt Fund Calculator](https://slicingpie.com/the-grunt-fund-calculator/)

**The "slicing pie moment" (baking the pie)** — the trigger converting dynamic slices into a fixed cap
table: (1) an outside institutional investment (required, since investors need a fixed table), (2) the
point all contributors are paid full market-rate salaries, (3) contributions stabilizing, or (4) a major
event (acquisition, key hire). [Equity Matrix](https://equitymatrix.io/blog/slicing-pie-guide)

**Pros**: removes the need to *predict* future contribution at founding (the hardest and most-often-wrong
input in a fixed split); formulaic/objective rather than negotiated; automatically handles pivots and
uneven contribution over time.

**Cons**: no inherent cliff protection (an early leaver keeps slices already earned — its own "dead
equity" risk); requires disciplined, continuous logging or the system fails; still needs to be wrapped in
proper legal/cap-table infrastructure once it "bakes."

**When appropriate**: very early, bootstrapped, pre-revenue teams with evolving roles and no fixed
salaries. **When not**: teams about to raise institutional capital, or with stable, defined roles.
**Investor reaction**: institutional investors expect a clean, fixed, fully-vested cap table before a
priced round — dynamic structures are treated as something to convert to fixed ownership as a **closing
condition**, typically onto the classic 4yr/1yr-cliff structure. [Equity Matrix](https://equitymatrix.io/blog/what-investors-look-for-in-cap-tables)

### 3.4 Rules of thumb

**YC's position (Michael Seibel)** — the standard counterweight to Wasserman's critique, and the position
this skill's users will most often need to reconcile against:

- *"Equity should be split equally or close to that because all the work is ahead of you."*
  [YC Library](https://www.ycombinator.com/library/5x-how-to-split-equity-among-co-founders)
- Four reasons: (1) it takes **7–10 years** to build real value, so year-one differences shouldn't drive
  permanent splits; (2) more equity = more motivation, and most startups fail, so motivation matters more
  than fairness-accounting; (3) investors read the split as a signal of how the CEO values the team; (4)
  startups are about execution, not ideas — "ideas are a dime a dozen."
- YC explicitly **rejects** as justifications for unequal splits: who had the idea, who started earlier,
  salary needs, age/experience gaps, fundraising status, tie-breaking authority.
- YC explicitly **rejects** performance/metric-tied dynamic equity (e.g. vesting tied to lines of code) as
  impractical, since startups pivot too often for such metrics to hold — and **rejects** equity for
  part-time cofounders entirely.
  [YC Library, Co-Founder Equity Mistakes to Avoid](https://www.ycombinator.com/library/LP-co-founder-equity-mistakes-to-avoid)

**Reconciling YC vs. Wasserman for the skill**: both agree the mechanism that actually matters is **vesting
over equal-split accounting** — YC recommends solving the "unequal contribution" risk through the 4yr/1yr
cliff rather than through a fractionally unequal split; Wasserman's critique targets speed/documentation of
the decision, not equality itself. Practical synthesis: an equal or near-equal split is defensible **if**
(a) it's genuinely negotiated (not resolved in under a day), (b) the rationale is documented in writing, and
(c) it sits behind a real vesting schedule. An unequal split is warranted where contribution asymmetry is
large and durable (capital, prior experience, sole-idea origination, part-time vs. full-time).

**Practical process rule of thumb**: document the split rationale in writing (Techstars, Gust); use the
1-year cliff as a built-in revisit-and-lock checkpoint before the split becomes economically painful to
unwind. [Techstars](https://www.techstars.com/blog/advice/how-to-split-co-founder-equity-the-right-way)

**Investor red flag**: a founder who won't negotiate or discuss equity openly signals future conflict —
investors expect to see that the hard conversation happened, not that it was avoided.
[Gust FAQ](https://gust.com/launch/faq/articles/when-and-why-should-i-determine-an-initial-equity-split-with-my-founding-team)

> **Flagged, not used**: a stat claiming "First Round Capital's 2024 State of Startups: 67% of seed
> investors view splits beyond 55/45 as a yellow flag" circulates on equity-calculator marketing blogs but
> could not be traced to First Round's actual published report. Do not cite as fact without independent
> verification.

### 3.5 Data on founder equity disputes

**The "65%" figure and its real lineage**: widely attributed to Wasserman as *"65% of high-potential
startups fail due to conflict among co-founders."* Tracing further back, this originates in part from
**Gorman & Sahlman (1989)**, who surveyed 49 VCs about 96 at-risk portfolio companies and found 61 of those
VCs ranked team/founder issues among their top three failure causes (61/96 ≈ 63.5%, rounded to ~65% and
folded into Wasserman's later, larger dataset). Use the 65% figure, but attribute the lineage rather than
presenting it as a clean modern empirical result.
[Entrepreneur.com](https://www.entrepreneur.com/leadership/harvard-business-school-professor-says-65-of-startups-fail/370367) ·
[CNN Money](https://money.cnn.com/2014/02/24/smallbusiness/startups-entrepreneur-cofounder/)

**Other Wasserman-derived churn statistics** (secondary synthesis of his HBS working papers — medium
confidence):

- In **73% of founder-CEO replacements**, the founder was fired rather than stepping down voluntarily.
- **52% of founders** are no longer CEO by the company's third financing round.
- Prior friendship/family ties within a founding team increase departure likelihood by roughly **30%** per
  additional relationship — teams often avoid the hard equity conversation *because* of the relationship,
  destabilizing after a roughly 6-month "honeymoon" period.
  [onstartups.com, synthesizing Wasserman](https://www.onstartups.com/tabid/3339/bid/80224/Avoiding-Founder-Failure-26-Quick-Tips-and-Real-Data.aspx)

**Carta's cap-table data** (45,000+ cap tables):

- Equal-split share by team size, 2015 → 2024/2025: **two-founder 31.5% → 45.9%**; **three-founder 12.1% →
  ~27%**; **four-founder 10.8% → 16.7%.**
- Among unequal splits, the median gap narrowed from ~**60/40 (2015) to ~51/49 (2024)**.
- Founder ownership erosion by stage (median, fully diluted): **Seed ~56% → Series A ~36% → Series B
  ~21.8%–27.3% → Series C**, where median employee option pool (~16.8%) can exceed median founder ownership
  (~16.1%) — context for why the initial split matters less in isolation than the whole cap-table
  trajectory (vesting + option-pool sizing + dilution).
- Solo founders: **36% of 2025 Carta-tracked startups** (up from 31% in 2024), roughly doubling over a
  decade.
- Carta's own framing: *"Most equity disputes happen because co-founders never explicitly discussed what
  each person was actually contributing."*
  [Carta, Founder Equity Split Trends 2024](https://carta.com/data/founder-equity-split-trends-2024/) ·
  [Carta Founder Ownership Report 2026](https://carta.com/data/founder-ownership-2026/)

**Documented dispute case studies** (useful as illustrative examples in a drafting skill):

| Company | What happened | Outcome | Source |
|---|---|---|---|
| **Zipcar** | Chase/Danielson 50/50 handshake, unequal actual contribution | Danielson pushed out operationally (2001), retained full stake; Chase diluted to ~3% by 2011 IPO | [Equity Matrix](https://equitymatrix.io/blog/famous-cofounder-disputes) |
| **Facebook (Eduardo Saverin)** | ~30% stake diluted to ~0.03% via a 2005 share reissuance he didn't consent to | Sued 2005, settled 2009; recovered an estimated 4–5% stake, worth ~$2B at IPO | [Equity Matrix](https://equitymatrix.io/blog/famous-cofounder-disputes) |
| **Snapchat (Reggie Brown)** | Conceived the disappearing-photo concept, force out by Aug 2011 with no equity | Sued 2013; settled for **$157.5M** (2014); settlement did not recognize him as "cofounder" | [TechCrunch](https://techcrunch.com/2017/02/02/snapchat-reggie-brown/) · [Forbes](https://www.forbes.com/sites/kathleenchaykowski/2017/02/03/snap-ipo-filing-reveals-ousted-cofounder-received-157-5-million-in-settlement/) |
| **Twitter (Noah Glass)** | Championed the core concept and coined the name; pushed out by Jack Dorsey | Minimal equity, no settlement — a dispute that never formally resolved | [Equity Matrix](https://equitymatrix.io/blog/famous-cofounder-disputes) |
| **Tinder (Whitney Wolfe Herd)** | Had "co-founder" title stripped; separate harassment claim tied to a co-founder relationship | Settled harassment claim for **$1M+**; title/credit dispute rather than a pure equity fight | [CNN Business](https://www.cnn.com/2019/12/13/tech/whitney-wolfe-herd-bumble-risk-takers) · [Inc.](https://www.inc.com/business-insider/ousted-tinder-co-founder-makes-1-million-in-lawsuit-settlement.html) |
| **ConnectU / Facebook (Winklevoss twins)** | No clear IP assignment; oral-contract breach alleged over source code | Settled Feb 2008 for a reported ~$65M | Background via [Wikipedia, Cameron Winklevoss](https://en.wikipedia.org/wiki/Cameron_Winklevoss) |

---

## 4. Vesting Deep-Dive

### 4.1 Why vesting protects cofounders from each other

Core problem: the **"free rider"** issue — without vesting, a founder who leaves after a short time keeps
their entire stake forever, while the founders who stay do all the remaining work.

- **YC (Michael Seibel)**: use 4-year vesting with a 1-year cliff on *all* founders, no exceptions.
  [YC Library](https://www.ycombinator.com/library/5x-how-to-split-equity-among-co-founders)
- **Cooley GO**: *"When a founder decides to leave, or is asked to leave, early in the company's existence,
  the vesting restriction protects the other founders from the 'free rider' problem that would otherwise
  exist."* [Cooley GO](https://www.cooleygo.com/founder-basics-founders-stock/)
- **WilmerHale Launch** frames vesting as a **commitment device**: without it, a cofounder can depart early
  "with his or her stock, and without the company being able to repurchase the stock, leaving you with a
  more complicated cap table."
  [WilmerHale Launch](https://launch.wilmerhale.com/research/blog/five-things-about-founder-stock-vesting)
- Second-order effect: an unvested, messy founder split → resentment → departures → **dead equity** on the
  cap table (see §6.4) → a hiring problem (no equity left for key hires) → a financing problem (VCs won't
  fund a cap table with non-contributing shareholders holding large blocks).
- **Key nuance**: founders already legally own their shares at issuance (this is what makes it "reverse"
  vesting) — YC recommends vesting anyway, precisely because bare ownership without a forfeiture mechanism
  doesn't protect the team from an early departure. YC explicitly warns against substituting complex
  performance-based earn-outs for the cliff/vesting structure — if a founder relationship isn't working,
  the fix is termination before the cliff, not bespoke performance conditions.
  [YC Library, Co-Founder Equity Mistakes to Avoid](https://www.ycombinator.com/library/LP-co-founder-equity-mistakes-to-avoid)

### 4.2 Standard structure: 4 years, 1-year cliff, monthly thereafter

| Period | What vests |
|---|---|
| Months 0–12 (the cliff) | **0%.** Nothing vests. Leave at month 11 → walk away with nothing. |
| Day of 1-year anniversary | **25%** vests in a single lump sum. |
| Months 13–48 | Remaining **75%** vests monthly — **≈1/48 (≈2.08%) of the original grant per month** — until 100% at month 48. |

- **Carta**: *"1/4 of your shares vest after one year... After the cliff, 1/36 of the remaining granted
  shares (or 1/48 of the original grant) vest each month until the four-year vesting period is over."*
  [Carta, Vesting Explained](https://carta.com/learn/equity/stock-options/vesting/)
- **WilmerHale Launch**: *"a four-year vesting schedule with a one-year vesting cliff... and month-to-month
  vesting for the remaining three years."*
  [WilmerHale Launch](https://launch.wilmerhale.com/research/blog/five-things-about-founder-stock-vesting)
- **Cooley GO**: *"the stock vests in monthly or quarterly increments over four years; if the Founder
  leaves the company before the stock is fully vested, the company has the right to buy back the unvested
  shares."* [Cooley GO](https://www.cooleygo.com/founder-basics-founders-stock/)

**Why this exact structure became standard**: Carta — *"It became standard practice because early venture
investors got burned by founders who split up six months after raising money and walked off with a large
ownership stake they'd done almost nothing to earn. The cliff protects the company and its remaining team
from a co-founder who leaves early... it's why Y Combinator has advised roughly this structure to nearly
every company it's funded since the mid-2000s."* [Carta, Vesting Explained](https://carta.com/learn/equity/stock-options/vesting/)

**Drafting trap**: the cliff-edge discontinuity itself catches founders off guard — a two-month difference
(month 11 vs. month 13) separates 0% from 25%. Second trap: skipping vesting entirely ("we're all
committed") leaves zero recourse if a founder exits at month 3 holding a full stake — investors will force
a retroactive (often worse-priced) fix. Third: monthly vs. quarterly post-cliff vesting — quarterly means a
founder leaving just short of quarter-end forfeits a whole quarter's shares.

### 4.3 Reverse vesting / vesting on already-issued shares

Founders are issued **100% of their shares up front, at incorporation** (for 83(b) tax reasons — §4.4), not
doled out over time. Vesting is therefore not a mechanism of withholding certificates; it is a **company
right to buy back (reacquire) the unvested portion at the original purchase price** if the founder's
service ends early. Hence "reverse" vesting — ordinary vesting grants shares over time; reverse vesting
takes back already-issued shares on early departure.

- **Cooley GO**: *"Stock subject to vesting tied to continuous service to the company is sometimes called
  'reverse vesting' because it gives the company the right to reacquire unvested stock if the service
  terminates."* Repurchase price is *"the lower of cost or the then fair market value"* — since original
  purchase price is nominal, this almost always just means "at cost."
  [Cooley GO](https://www.cooleygo.com/founder-basics-founders-stock/) ·
  [Cooley GO, Ownership Culture](https://www.cooleygo.com/establishing-ownership-culture-stock-vs-options/)
- **Implementation document**: the **Restricted Stock Purchase Agreement (RSPA)**. *"Founders should enter
  into a written restricted stock purchase agreement with the company that values the price of the shares
  at the time of purchase. Restricted stock purchase agreements should clearly describe vesting schedules
  and acceleration provisions."* [Cooley GO](https://www.cooleygo.com/founder-basics-founders-stock/) ·
  [Orrick Start-Up Forms](https://www.orrick.com/en/Total-Access/Tool-Kit/Start-Up-Forms/Founders-Stock-Purchase)

**Drafting point**: the vesting/repurchase right lives in the RSPA itself, not in a separate "vesting
agreement" controlling certificate issuance. Certificates exist and are owned from day one (triggering the
83(b) clock); only the company's contractual, tranche-by-tranche repurchase option creates the retention
effect.

### 4.4 The 83(b) election

**What it is**: IRC §83(b) lets a recipient of property subject to a substantial risk of forfeiture (here,
unvested restricted stock) elect to be taxed on its value **now**, at grant, instead of at each future
vesting date. Governing reg: [26 CFR §1.83-2](https://www.law.cornell.edu/cfr/text/26/1.83-2).

**Why founders with reverse-vesting stock must file it**: absent the election, the IRS treats each vesting
tranche as a new taxable event — ordinary income tax on the spread between fair market value and price
paid, calculated **at each vesting date**. FMV at incorporation is nominal but can rise substantially by
later vesting dates; filing 83(b) converts a potentially large, recurring ordinary-income liability into a
near-zero one-time tax at grant.

**The 30-day deadline — strict, no exceptions**:

- Treasury Reg. §1.83-2: *"The election shall be filed not later than 30 days after the date the property
  was transferred... and may be filed prior to the date of transfer."*
- The clock runs from the **date of stock issuance/purchase** — not board-approval date or any earlier
  "agreement in principle."
- Filings are timely if **postmarked** within the window (certified mail postmark date controls).
- [Clerky](https://help.clerky.com/article/2828-how-do-i-make-an-83b-election) ·
  [Stripe Atlas docs](https://docs.stripe.com/atlas/83b-election)

**Concrete consequence illustration** (Stripe Atlas): 200,000 shares purchased at $0.0001/share = $20
total cost. Half vests year 1 at $0.50 FMV; other half year 2 at $1.00 FMV; sold year 3 at $2.00/share
($400,000 total).

- **With 83(b)**: no tax at either vesting date — only capital gains on $399,980 at sale.
- **Without 83(b)**: ordinary income tax at year 1 on ~$49,990 and at year 2 on ~$99,990, before the
  founder has sold a single share or seen a dollar of liquidity — plus capital gains at sale.
  [Stripe Atlas](https://docs.stripe.com/atlas/83b-election) ·
  [Carta](https://carta.com/learn/equity/stock-options/taxes/83b-election/) ·
  [Cooley GO](https://www.cooleygo.com/what-is-a-section-83b-election/)

**Standardized IRS form**: **Form 15620** ("Section 83(b) Election") released Nov 2024 as an optional
standardized form; an online/electronic filing option opened mid-2025.
[IRS Form 15620 (PDF)](https://www.irs.gov/pub/irs-pdf/f15620.pdf) ·
[Goodwin, e-filing](https://www.goodwinlaw.com/en/insights/publications/2025/07/alerts-practices-erisa-online-filing-of-section-83b-elections)

> **Correction the skill should encode**: the removal of the requirement to attach a copy of the §83(b)
> election to the taxpayer's income-tax return is often mis-dated to the 2018 Tax Cuts and Jobs Act. It
> actually predates the TCJA — **Treasury Decision 9779, finalized 2016**, applicable to transfers on/after
> **January 1, 2016**. The **30-day filing-with-the-IRS deadline was unaffected** and remains absolute;
> practitioners still recommend retaining proof of the original filing.
> [Wilson Sonsini](https://www.wsgr.com/en/insights/final-regulations-issued-under-internal-revenue-code-section-83-eliminate-taxpayer-requirement-to-file-section-83-b-election-with-income-tax-return.html) ·
> [The Tax Adviser](https://www.thetaxadviser.com/news/2016/jul/regulations-eliminate-sec-83b-filing-statement-requirement-201614887/)

**QSBS interaction**: filing 83(b) starts the Qualified Small Business Stock holding-period clock at
purchase date rather than at each vesting date — an early filing can let shares that technically vest
within the QSBS window still qualify. [Carta](https://carta.com/learn/equity/stock-options/taxes/83b-election/)

**Irrevocability**: the election cannot be undone. If a founder pays tax on stock at grant and later
forfeits unvested shares by leaving early, **there is no refund** of tax already paid — a real reason to
route the decision through a CPA/tax attorney (see §9.3).

### 4.5 Founder-friendly vesting variations

- **Vesting credit for pre-incorporation work**: founders who worked full-time before formal incorporation
  commonly negotiate retroactive vesting credit so the cliff/schedule doesn't reset to zero. Example: 12
  months of demonstrable pre-incorporation full-time work → 25% of shares issued already fully vested, with
  the remaining 75% vesting over the next 36 months. Institutional investors are often reluctant to accept
  backdating beyond roughly a year, so keep any claimed credit realistic and well-documented — it will be
  scrutinized in diligence.
- **Shorter cliffs / faster schedules**: occasionally negotiated pre-institutional-money; the 4yr/1yr-cliff
  standard tends to reassert itself as a financing condition once VCs are involved.
- **YC's explicit warning**: against substituting milestone/performance-based vesting for time-based
  vesting — keep the structure uniform across founders and handle underperformance through an actual
  termination decision, not bespoke conditions layered onto vesting.
  [YC Library](https://www.ycombinator.com/library/LP-co-founder-equity-mistakes-to-avoid)

### 4.6 Acceleration triggers

**Single-trigger**: 100% (or a fixed %) of unvested shares vest automatically on **one** event alone — a
change of control. **Why acquirers/VCs resist it**: WilmerHale Launch — acquirers may **reduce the purchase
price** when single-trigger exists, since full acceleration removes the retention leverage the acquirer was
counting on; in the worst case it can make a deal untenable.
[WilmerHale Launch](https://launch.wilmerhale.com/research/blog/five-things-about-founder-stock-vesting)

**Double-trigger**: unvested shares accelerate only if **both** (1) a change of control occurs, **and** (2)
within a defined window after close (**commonly 12 months**), the founder is terminated without Cause or
resigns for Good Reason. Sample market language (WSGR): *"If within 12 months following a Change of
Control, the founder is terminated without Cause or resigns for Good Reason, 100% of unvested shares shall
immediately vest."*
[Wilson Sonsini](https://www.wsgr.com/en/insights/its-not-about-how-much-stock-you-have-its-about-how-much-copper-wire-you-can-get-out-of-the-building-with-founder-exits-part-2.html)

**Why double-trigger is the market standard**: Cooley GO frames it as *"a happy medium"* — acquirers want
people to stick around post-close, so single-trigger "doesn't usually make sense," but the founder still
needs protection against being terminated right after close specifically to avoid ever paying out the
unvested equity.
[Cooley GO](https://www.cooleygo.com/what-are-single-and-double-trigger-acceleration-and-how-do-they-work/) ·
[Orrick](https://www.orrick.com/en/Insights/2026/04/Single-and-Double-Trigger-Vesting-Acceleration-What-founders-and-employees-should-know)

**Drafting note**: double-trigger's protective value depends entirely on how "Cause" and "Good Reason" are
defined — a narrow "Good Reason" or broad "Cause" definition can gut the mechanism even though it nominally
exists. Clerky's standard founder package defaults to **100% double-trigger acceleration**.
[Clerky](https://help.clerky.com/article/1736-what-are-customary-stock-vesting-terms-for-startup-founders)

---

## 5. IP Assignment

### 5.1 Present-tense assignment language — the "hereby assigns" rule

IP assignment clauses (in founders' agreements and in the Confidential Information and Invention Assignment
Agreement / CIIAA / PIIA) must use **present-tense, self-executing language** — *"I hereby assign"* — not
future-tense *"I will assign"* or *"I agree to assign."*

**Doctrinal basis**: *Board of Trustees of the Leland Stanford Jr. Univ. v. Roche Molecular Systems*, 563
U.S. 776 (2011). The Stanford researcher's university agreement said he *"agree[d] to assign"* — held to be
a promise to assign in the future, an executory contract. His separate Cetus/Roche visitor's agreement said
*"will assign and do[es] hereby assign"* — held to be a **present assignment**, vesting rights instantly
with no further act required. Because the Cetus/Roche present assignment predated Stanford's own later
assignment, **Roche — not Stanford — won the patent rights**, despite Stanford being the inventor's home
institution.
[Patent Docs](https://patentdocs.org/2011/06/06/board-of-trustees-of-the-leland-stanford-junior-university-v-roche-molecular-systems-inc-2011/) ·
[Taft Law](https://www.taftlaw.com/news-events/law-bulletins/stanford-university-v-roche-molecular-131-s-ct-2188-2011/)

**Why this matters as a drafting trap**: future-tense language means no title transfers automatically; if a
founder later signs a *conflicting present-tense* assignment elsewhere (a prior employer, a co-founder's
other venture), the third party's present assignment can win outright — exactly what happened to Stanford.
A second, founder-specific trap: relying only on a standard post-incorporation employment agreement's IP
clause, which typically covers only IP created "during employment" — structurally missing the
pre-incorporation MVP/deck/codebase the company's value often actually rests on.
[Orrick](https://www.orrick.com/en/tech-studio/resources/glossary/Inventions-Assignment-Agreement) ·
[Crowley Law](https://www.crowleylawllc.com/founder-ip-assignment-pre-incorporation/)

### 5.2 Pre-incorporation IP

Founders often write code, build prototypes, or develop the core idea **before** the company exists. Absent
an assignment explicitly covering that period, this IP can remain the individual founder's personal
property rather than company property. Founders' agreements / IP assignment agreements should explicitly
cover "IP created prior to incorporation" and assign it to the entity upon formation — this is not a
cleanup task to defer, it is a mandatory step for any future funding or exit.
[Orrick](https://www.orrick.com/en/tech-studio/resources/glossary/Inventions-Assignment-Agreement) ·
[Gunderson Dettmer](https://catalyze.gunder.com/en/knowledge-articles/resource/formation) (recommending a
**Technology Assignment Agreement** specifically for this gap)

### 5.3 Moral rights

Moral rights (attribution, integrity of the work) are typically **waived** in IP assignment agreements.
This matters especially outside the US: in UK/EU/civil-law jurisdictions moral rights can be non-waivable
in some circumstances, whereas in the US they are narrow (e.g. VARA, limited to certain visual art) and
generally waivable. Drafting implication: include an explicit moral-rights waiver clause, flagged for local
counsel review in non-US jurisdictions where waivability is restricted.

### 5.4 Prior inventions carve-outs

Standard practice attaches a **"Prior Inventions" schedule/exhibit** to the IP assignment agreement, where
each founder discloses pre-existing IP/inventions they own that they are **not** assigning to the company —
protecting founders from inadvertently assigning unrelated personal projects. Where a listed prior invention
ends up incorporated into the product, the company typically receives a **non-exclusive license** to it
rather than full ownership.

### 5.5 The disaster case: un-assigned IP surfacing in diligence

IP assignment gaps that surface during fundraising or M&A due diligence are a well-documented deal-killer
or deal-delayer pattern: investor counsel discovers a departed cofounder or a founder's former employer has
a claim to core IP, forcing costly retroactive assignment negotiations — sometimes with a leverage-holding
ex-founder demanding payment simply to sign. The **ConnectU v. Facebook** dispute (§3.5 above, and §7
below) is the canonical illustration: no clear IP assignment agreement was in place, an oral-contract breach
was alleged over source code, and the matter settled for a reported ~$65M.
Background via [Wikipedia](https://en.wikipedia.org/wiki/Cameron_Winklevoss); general framing via
[Sandberg Phoenix](https://sandbergphoenix.com/why-ip-assignment-agreements-are-essential-for-startup-founders/) ·
[WilmerHale Launch](https://launch.wilmerhale.com/explore/formation/founders/who-owns-your-ip)

---

## 6. Leaver / Departure Mechanics

### 6.1 Good leaver vs. bad leaver

| | Good Leaver | Bad Leaver |
|---|---|---|
| **Typical triggers** | Death, disability/incapacity, redundancy, resignation for good reason, termination without cause | Voluntary resignation without good reason; termination for cause (fraud, gross misconduct, breach) |
| **Unvested shares** | Forfeited/repurchased at cost regardless (same as bad leaver — vesting status doesn't depend on leaver category) | Forfeited/repurchased at cost |
| **Vested shares** | Usually kept, or repurchased at fair market value / an agreed formula | Can be forced to transfer at **nil value** or a heavily discounted price (e.g. par value) in harsher (typically UK) drafting; in US practice, more often expressed via acceleration rather than clawback of already-vested shares |

**UK terminology (primary source: SeedLegals)**: "Good Leaver" = death, accident, or disability (not
voluntary departure) — usually keeps vested shares, transfers unvested at fair value. "Bad Leaver" =
terminated for fraud, gross negligence, or gross misconduct — may be forced to transfer unvested shares
**at nil value**. These terms live in the Articles of Association's "Compulsory Transfers" section.
[SeedLegals](https://help.seedlegals.com/en/5440634-my-co-founder-is-leaving-what-do-i-do-with-their-shares) ·
[SeedLegals, Founder Vesting](https://seedlegals.com/resources/startup-founder-vesting/) ·
[Bird & Bird](https://www.twobirds.com/en/insights/2025/leaver-provisions-the-terms-that-founders-fear-the-most)

**US practice (Orrick Legal Guide for Stripe Atlas)**: accelerated vesting of **6–12 months** typically
applies on without-cause/good-reason termination, death, or disability — *"under most agreements, there is
no acceleration if the founder voluntarily quits or is terminated for 'cause.'"*
[Orrick Legal Guide, p.22](https://stripe.com/files/atlas/orrick-legal-guide.pdf)

**Drafting trap**: "Cause" and "Good Reason" left undefined — Ledgy: *"there is no concrete guidance in
employment law on how to deal with leaver provisions,"* so an undefined categorization becomes a post-hoc
fight exactly when trust is lowest.
[Ledgy](https://ledgy.com/blog/good-leaver-bad-leaver-clauses)

**A second, sharper trap**: single-founder companies often have **no vesting at all** initially — Orrick:
*"For companies with only one founder, the founder's stock is often not subject to vesting initially,
though investors may later require that the shares become subject to vesting"* — a well-documented cap-
table poison pill that VCs force a retroactive (often worse-priced) fix for if not addressed from day one.
[Orrick Legal Guide, p.19](https://stripe.com/files/atlas/orrick-legal-guide.pdf)

### 6.2 Unvested share forfeiture

Reconfirming the reverse-vesting mechanic (§4.3): unvested shares are forfeited/repurchased by the company
at the original issue price (near-zero) upon departure, **regardless of good/bad leaver status** in most
US venture-backed structures — the good/bad leaver distinction chiefly affects **vested** shares, not
unvested ones.

### 6.3 Buyback / repurchase of vested shares

Common mechanisms: a company or cofounder **ROFR + buyback option** over a departed founder's vested
shares. Valuation methods used in practice: fair market value via independent appraisal/409A valuation, a
pre-agreed formula, book value, or last-round price. Payment terms are often structured as **installments
or a promissory note** rather than a lump sum, since cash-strapped startups frequently cannot pay FMV in
cash immediately.

### 6.4 The "dead equity" problem

**Dead equity** (or "dead weight equity"): a departed founder who keeps a meaningful chunk of vested equity
with no further contribution. Consequences: dilutes remaining founders/employees; complicates future
option-pool top-ups; creates cap-table friction with new investors who don't want to fund a non-
contributing shareholder; and creates governance/consent headaches where the departed founder's shares are
needed for a supermajority vote.

**Documented case study — UK SaaS startup**: a three-founder startup had one founder leave after six
months with **no vesting schedule or leaver clause in place**. That founder kept 33% of the company despite
contributing nothing further. When the startup approached seed investors, the cap table became "a serious
concern"; investors required a clean-up, and the remaining founders had to pay a cash settlement and
restructure the cap table, delaying the round by months.
[Cited via secondary legal-blog summary](https://vklegalassociates.com/founder-departures-and-equity-reassignment-in-uk-startups/) —
*(treat as illustrative, not independently corroborated by a named primary source)*.

**Flip-side case — Skype (2011)**: when Microsoft acquired Skype for $8.5B, some employees discovered their
equity was worth **$0** because of a buyback/clawback clause buried in the fine print — illustrating that
leaver/clawback terms which exist on paper but are poorly understood by the equity holder create their own
dispute risk.
[Stock Option Counsel, P.C.](https://www.stockoptioncounsel.com/blog/standards-ownership-canthecomanytakebackmyvestedshares)

A well-drafted leaver/buyback provision — clear good/bad leaver definitions, a defined valuation mechanism,
and a payment structure the company can actually afford — is what prevents both failure modes: equity
stranded with a non-contributor, and equity clawed back from a founder who never understood the risk they
signed up for.

---

## 7. Top Founder Disputes & Mistakes

The recurring, well-documented failure modes, each traced to a concrete cause and (where available) a
named case study:

| Mistake | Failure mode | Standard fix |
|---|---|---|
| **No vesting agreement** | A founder leaves after months, keeps 100% of a large stake forever ("free rider"); cap table becomes uninvestable | 4yr vesting / 1yr cliff on all founders (§4) |
| **Handshake/verbal-only equity** | "He said / she said" disputes over what was promised; unenforceable against a court or an investor's counsel | Written RSPA + documented split rationale |
| **No IP assignment** | Company doesn't actually own its core technology; surfaces catastrophically in diligence (§5.5) | Present-tense CIIAA/PIIA at incorporation, covering pre-incorporation work |
| **No leaver/departure terms** | Departed founder's equity becomes "dead equity" (§6.4); cap-table cleanup required before financing | Good/bad leaver definitions + buyback mechanism |
| **No decision-making/deadlock mechanism** | 50/50 teams deadlock on major decisions with no tiebreaker; sometimes fatal to the company | Mediation-first clause, neutral tiebreaker, or shotgun/Russian-roulette buy-sell (§2, clause 8) |
| **No written founders' agreement at all** | Investors gate financing on "clean, documented" founder terms; disputes have no governing framework | At minimum: RSPA, CIIA, and a documented equity/vesting rationale before any institutional money |

**Data behind these patterns**:

- **Wasserman (HBR, "The Founder's Dilemma," Feb 2008)**, analyzing 212 startups from the late 1990s/early
  2000s: by year three, **50% of founders were no longer CEO**; by year four, only 40% remained; **fewer
  than 25%** led their company's eventual IPO.
  [HBR](https://hbr.org/2008/02/the-founders-dilemma) (paywalled; summary via
  [Business of Software](https://businessofsoftware.org/talks/understanding-founders-dilemmas/))
- **The 65% co-founder-conflict-failure figure** — see §3.5 for full lineage (Gorman & Sahlman 1989 →
  Wasserman's broader dataset). [Entrepreneur.com](https://www.entrepreneur.com/leadership/harvard-business-school-professor-says-65-of-startups-fail/370367)
- **CB Insights "top reasons startups fail"** — flag that there are **two different vintages** in
  circulation, not one number: the classic ~20-reasons report lists **"not the right team" at 23%**
  (behind "no market need" 42% and "ran out of cash" 29%); a 2024-refreshed cut (431 VC-backed shutdowns
  since 2023) leads instead with "ran out of capital" (70%), "poor product-market fit" (43%), and doesn't
  prominently break out team/cofounder issues as a separate category. Cite both, dated — team dysfunction
  is frequently the root cause *behind* a "ran out of cash" or "poor PMF" death in the newer cut, not
  always broken out separately. [CB Insights](https://www.cbinsights.com/research/report/startup-failure-reasons-top/)

**Named public disputes** (see §3.5 table above for Zipcar, Facebook/Saverin, Snapchat/Brown, Twitter/
Glass, Tinder/Wolfe Herd, ConnectU/Facebook — repeated here by cross-reference rather than duplicated).

**Deadlock-specific case study — Housing.com**: cited as lacking any dispute-resolution mechanism, a
contributing factor in 9 of the original 12 founders exiting by 2016.
[iPleaders](https://blog.ipleaders.in/co-founders-agreement-disputes-suggestions/)

> **Flagged, not used**: secondary-blog statistics attributed to "First Round Capital" on cofounder
> breakup rates (e.g. "10% of co-founder teams split within a year," "20% of breakups shut the company down
> within 18 months") could not be traced to a single verifiable First Round Capital primary publication.
> Use First Round's actual, verifiable content instead —
> [First Round Review, "How to Fix the Co-Founder Fights You're Sick of Having"](https://review.firstround.com/how-to-fix-the-co-founder-fights-youre-sick-of-having-lessons-from-couples-therapist-esther-perel/)
> — and hedge or drop the specific percentages.

---

## 8. Entity & Jurisdiction Variation

### 8.1 Delaware C-corporation (US VC-backed default)

The standard default because of investor familiarity, a well-developed body of case law, and the Delaware
Court of Chancery's specialized corporate-law expertise. Vesting is implemented via an **RSPA under the
DGCL** — founders buy shares at a nominal price (e.g. $0.0001/share) subject to a company repurchase right
over unvested shares. Standard incorporation packages (Cooley GO, Clerky) bundle the certificate, bylaws,
board/incorporator consents, RSPA, 83(b) form, and CIIAA as one coherent, investor-recognized set.
[Cooley GO Docs, Incorporation Package (Delaware)](https://www.cooleygo.com/documents/incorporation-package-delaware/) ·
[Clerky, standard vesting terms](https://help.clerky.com/article/1746-what-kind-of-vesting-do-the-standard-post-incorporation-setup-forms-have)

### 8.2 LLC / Operating Agreement

- **Structural difference**: LLC owners hold **"membership interests"** or **"units,"** not shares. There
  is generally **no separate founders' agreement** — the operating agreement typically *is* the governing
  document. [Carta, LLC Membership Interests](https://carta.com/learn/startups/compensation/equity-incentive-plans/membership-interests/)
- **Vesting is possible but bespoke**: *"While it is possible to impose vesting on a member's units in an
  LLC, this creates significant added complexity... all vesting arrangements for an LLC need to be
  tailored... unlike... standard 'off-the-shelf' agreements"* for a corporation.
  [Orrick](https://www.orrick.com/en/tech-studio/resources/faq/do-an-llcs-membership-units-vest-like-the-shares-of-a-corporation)
- **Profits interests vs. capital interests**: the LLC equivalent of a stock grant is a "profits interest,"
  which usually requires "booking up" capital accounts before issuance, and converts a W-2 employee
  receiving one into a tax partner (K-1), no longer W-2-eligible.
  [Carta, Profits Interest](https://carta.com/learn/startups/compensation/equity-incentive-plans/profits-interest/)
- **Why VCs avoid LLCs**: pass-through taxation creates UBTI problems for tax-exempt LPs (pensions,
  endowments) who fund much of a VC's capital base; transferring partial LLC ownership is legally more
  complex than transferring stock; C-corps offer standardized, mature share-class infrastructure (common,
  Series Seed, Series A preferred). *"VCs strongly prefer to invest in C Corporations 99% of the time."*
  [Lighter Capital](https://www.lightercapital.com/blog/why-vcs-only-invest-in-c-corporations)
- **The LLC-to-C-corp "flip"**: standard practice is converting before a priced VC round. Note a 2026
  Orrick countervailing wrinkle: some founders deliberately start as an LLC and convert later to expand
  eventual QSBS gain-exclusion benefits, but *"any 'built-in' gain accrued before converting from an LLC to
  a corporation is not eligible for the QSBS exclusion."*
  [Orrick, 2026](https://www.orrick.com/en/Insights/2026/01/Risk-and-Reward-How-Starting-Your-Business-as-an-LLC-Could-Impact-QSBS-Tax-Savings)

### 8.3 UK Ltd (private limited company)

- **Document structure**: **Articles of Association** (binding "Compulsory Transfers" mechanics, share
  definitions, vesting-schedule variables) plus a separate **Shareholders' Agreement** for matters founders
  want kept private/flexible. [SeedLegals](https://help.seedlegals.com/en/5440634-my-co-founder-is-leaving-what-do-i-do-with-their-shares)
- **Good Leaver / Bad Leaver terminology is the standard UK usage** (§6.1) — distinct from, but analogous
  to, the US framing.
- **Vesting is investor-driven rather than baked into standard incorporation from day one**: *"All
  sophisticated investors will request some form of vesting schedule should you raise a round of
  financing"* — implying UK founders more often start without it, unlike the US where it's default from
  formation. [SeedLegals, Founder Vesting](https://seedlegals.com/resources/startup-founder-vesting/)
- **SEIS/EIS considerations**: SEIS gives investors 50% income-tax relief and 0% CGT (3-year hold); EIS
  gives 30% income-tax relief. Investor shares are usually a separate "A Ordinary" class with carefully
  worded (not literal) liquidation preference to stay SEIS/EIS-compliant; complicated holding/subsidiary
  structures can jeopardize the relief. [SeedLegals, SEIS & EIS](https://seedlegals.com/resources/seis-eis-tax-relief-facts/)
- **Growth shares**: a UK-specific share class with value only above a set hurdle price, used where EMI
  (the tax-favored option scheme, restricted to full-time UK-based employees) doesn't fit.
  [SeedLegals, share options](https://seedlegals.com/grow/share-options-scheme/)
- **Local counsel flag**: SEIS/EIS structuring is HMRC-specific, continuously monitored (relief can be lost
  retroactively), and interacts directly with Articles wording — mandatory qualified UK counsel/accountant
  territory, not DIY drafting.

### 8.4 MENA — DIFC / ADGM vs. onshore/mainland civil-law jurisdictions

**DIFC and ADGM (UAE free zones) — common-law, investor-familiar**:

- Both operate on **English common-law frameworks** with their own courts, independent of UAE civil
  courts; ADGM directly adopts ~50 English statutes; both offer 100% foreign ownership and 0% corporate
  tax on most activities. Multiple share classes are permitted (ordinary voting, multiple-voting,
  preferential-dividend); ADGM SPVs can offer fractional shareholding.
  [10 Leaves](https://10leaves.ae/publications/adgm/using-adgm-spvs-as-holding-structures-for-startups) ·
  [Al Tamimi & Company](https://www.tamimi.com/law-update-articles/remedies-for-shareholders-in-the-company-law-of-the-uae-and-the-difc/)
- **Vesting/ESOP structuring** (Kayrouz & Associates, UAE-focused firm): mainland UAE LLCs face a
  50-shareholder cap and mandatory pre-emption rights on all transfers, making genuine equity vesting
  impractical — practitioners instead use phantom shares, stock appreciation rights (SARs), or contractual
  profit participation (cash-settled, not true ownership). **DIFC** (Companies Law No. 5 of 2018) and
  **ADGM** allow pre-emption rights to be disapplied in the Articles, enabling true equity issuance without
  the mainland's statutory caps. Market-standard terms cited (10–15% fully-diluted ESOP pool, 4yr vesting/
  1yr cliff) mirror the US/Delaware norm once a DIFC/ADGM vehicle is used.
  [Kayrouz & Associates](https://www.kayrouzandassociates.com/insights/uae-employee-incentives-stock-options-esop-difc-adgm-mainland)

**Mainland/onshore UAE and other GCC civil-law jurisdictions**:

- Federal Decree-Law No. 32 of 2021 (effective Jan 2 2022, amended 2025) removed the historic 51%-Emirati-
  ownership/local-agent requirement for most mainland commercial activities, permitting up to 100% foreign
  ownership (strategic sectors still require approval).
  [U.ae](https://u.ae/en/information-and-services/business/doing-business-on-the-mainland/full-foreign-ownership-of-commercial-companies)
- 2025 amendments now allow more contractual freedom to structure voting rights, transfer restrictions,
  drag-along/tag-along rights, and exit mechanisms via shareholder agreements — *"provided these
  arrangements do not conflict with mandatory provisions of the law or public policy."*
  [Middle East Briefing](https://www.middleeastbriefing.com/news/uaes-2025-commercial-companies-law-what-businesses-need-to-know/)
- **Genuine grey area**: the Commercial Companies Law voids any Memorandum of Association provision that
  "deprives a partner of the profits or exempts him from sharing the losses" — a civil-law doctrine that
  could collide with Delaware/DIFC-style vesting-forfeiture mechanics. *This specific claim was
  reconstructed from secondary summaries rather than a single pinned primary legal-alert; verify against
  the Federal Decree-Law No. 32/2021 text or a named law-firm alert before treating as settled.*
- **Saudi Arabia — notable civil-law exception**: the new Companies Law (effective Jan 2023) introduced the
  **Simplified Joint-Stock Company (SJSC)** — no minimum capital, single-shareholder incorporation, a
  single president/director permitted, and multiple share classes (ordinary, preference, redeemable,
  convertible) — not available to Saudi LLCs. Recent MISA reforms permit up to 100% foreign ownership of
  JSCs in most sectors. **No source found confirming SJSC-specific vesting/forfeiture enforceability** —
  flag as a genuine gap. [HFA Firm](https://hfafirm.com/establishing-a-simplified-joint-stock-company-in-saudi-arabia/) ·
  [Al Tamimi](https://www.tamimi.com/law-update-articles/the-new-saudi-companies-law-what-you-need-to-know-1/)

**Local-counsel-mandatory flag**: any onshore/mainland GCC entity (UAE mainland, Saudi LLC/JSC/SJSC, Egypt,
or other MENA civil-law jurisdiction) should trigger a hard "local counsel required" flag in the skill —
both because the statutory freedom to contract around default profit-sharing/forfeiture rules is still
actively evolving, and because MENA-specific primary sourcing on founders'-agreement mechanics (as opposed
to general company/tax law) is genuinely thin in what's publicly available — see §10.

---

## 9. Ethics & Scope

### 9.1 Not legal advice; no attorney-client relationship

Mirror the pattern used by reputable legal-tech tools:

- **Cooley GO**: not intended as "specific legal, tax and/or accounting advice" or a substitute for
  qualified counsel; users "should not act or refrain from acting" based on its materials.
  [Cooley GO Terms of Use](https://www.cooleygo.com/terms-of-use/)
- **SeedLegals**: *"not a law firm and does not provide any legal or tax advice... offered for
  informational purposes only... they do not review materials for accuracy or legal sufficiency, draw
  legal conclusions, or apply the law to specific situations."*
  [SeedLegals ToS](https://seedlegals.com/us/terms-of-service/)

**For this skill**: a prominent, plain-language statement that its output is a drafting aid / document-
assembly tool, not legal advice, and that using it creates no attorney-client relationship with anyone.

### 9.2 The conflict of interest when one lawyer "represents the company"

Business lawyers are typically retained as counsel for the **to-be-formed entity**, not for any individual
founder — even though multiple founders rely on the same drafting.
[ABA Business Law Today, "Who Is the Client?"](https://businesslawtoday.org/2021/12/who-is-the-client-ethics-issues-structuring-start-ups-representing-early-stage-companies/)

Why this creates a real conflict: founders' individual interests (equity split, vesting acceleration,
leaver terms, credit for prior contribution) can and do diverge from each other and from the entity's
abstract interest. Under professional-responsibility norms, a lawyer recognizing this must counsel the
parties "to understand fully the implications of proceeding with one lawyer notwithstanding the risks of
possible conflicts down the road" —
grounded in [ABA Model Rule 1.7](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_7_conflict_of_interest_current_clients/comment_on_rule_1_7/).

**Recommendation**: each founder should obtain **independent counsel** before signing — especially for
equity split, vesting, and leaver terms, which are precisely where founder interests most often diverge.
This skill (like company counsel) drafts for the entity as a whole; it does not negotiate for any one
founder's individual interest, and should say so explicitly in its output.
[ABA Business Law Today](https://businesslawtoday.org/2021/12/who-is-the-client-ethics-issues-structuring-start-ups-representing-early-stage-companies/)

### 9.3 Tax advice caveats — 83(b) and QSBS

- **83(b) is irrevocable** — an election filed and later forfeited (founder leaves before vesting) cannot
  be refunded. The decision (whether to file, given a founder's specific AMT exposure, state tax posture,
  and QSBS eligibility) is not simple, and the 30-day deadline leaves no room to consult after the fact
  (§4.4). Route this to a CPA/tax attorney, always.
- **QSBS (IRC §1202) complexity**: requires a domestic C-corp; stock purchased directly from the
  corporation (not secondary); a 3-year (post-July 2025) or 5-year (pre-July 2025) holding period;
  non-corporate shareholders; a gross-assets threshold at issuance ($75M post-July 2025 / $50M before);
  exclusion of certain "qualified trade or business" categories (accounting, consulting, financial/legal
  services, banking, farming, hospitality, etc.); and **continuous compliance** — eligibility can be lost
  even after stock is originally issued as qualified if requirements aren't met for "substantially all" of
  the holding period.
  [Cooley, QSBS Cheat Sheet](https://www.cooley.com/-/media/cooley/pdf/practices/qsbs-cheat-sheet) ·
  [Wilson Sonsini](https://www.wsgr.com/en/insights/understanding-section-1202-the-qualified-small-business-stock-exemption.html)

**For this skill**: treat 83(b)/QSBS output as informational only, always paired with a CPA/tax-attorney
referral prompt, and never auto-recommend a specific election without that referral.

### 9.4 Bar association / UPL context

By 2025, over 30 US states had issued AI-specific bar guidance; core principle: lawyers may not delegate
tasks that constitute the practice of law to an AI tool, and allowing AI to give legal advice directly to
clients without attorney review is unauthorized practice of law. Supervising-lawyer responsibility (ABA
Model Rule 5.3, extended to non-human assistance) remains regardless of the tool used.
[Paxton, 2025 State Bar Guidance](https://www.paxton.ai/post/2025-state-bar-guidance-on-legal-ai) ·
[Oregon State Bar Formal Op. 2025-205](https://www.osbar.org/_docs/ethics/2025-205.pdf)

**Implication**: since this skill is intended for a lawyer's own drafting workflow (not a consumer-facing
tool), UPL risk is lower than a direct-to-founder product — but the same logic applies: frame the skill as
a drafting *aid* the lawyer reviews and remains professionally responsible for, never as an autonomous
advice-giver to founders directly.

---

## 10. Sourcing Notes

Confidence gradation for whoever operationalizes this into a `SKILL.md`:

- **High confidence, directly fetched/quote-verified**: Orrick's Stripe Atlas Legal Guide (the single
  richest primary source underlying most concrete percentages/timeframes), YC's equity-split and vesting
  library articles, Clerky's help-center articles, Carta's Vesting/83(b)/Founder Ownership data pages, the
  NBER "First Deal" paper and digest, *Stanford v. Roche* case commentary (Patent Docs, Taft Law), Paul
  Graham's "Founder Control," SeedLegals' UK-specific guides, the FTC's 2025 press release and the Federal
  Register's Feb 2026 rule removal, Treasury Reg. §1.83-2, IRS Form 15620.
- **Search-index-derived, not directly fetched** (Cooley GO, Wilson Sonsini, and Orrick blocked automated
  fetch with HTTP 403 in multiple research passes): quotes attributed to these firms were recovered via
  search-engine cached extraction of the exact cited URLs, not fabricated, but **should be independently
  re-verified against the live pages** before being encoded as boilerplate, since these firms periodically
  update template language.
- **Corrected, not as originally assumed**: the "no longer need to attach an 83(b) copy to the tax return"
  rule is **Treasury Decision 9779 (2016)**, not the 2018 TCJA (§4.4).
- **Flagged as unverifiable / do not cite as hard fact**: (1) "First Round Capital 67% of seed investors
  flag splits beyond 55/45" and other specific First-Round breakup percentages (§3.4, §7) — not traced to
  a primary First Round publication; (2) the "CEO designation = 14-20pp premium" figure (§3.2) — a
  secondary paraphrase of Wasserman's data, not traced to his primary text; (3) the UK SaaS "33% dead
  equity" case study (§6.4) — sourced from a single secondary legal blog, not independently corroborated.
- **Genuine sourcing gap, not filled with invented detail**: MENA founders'-agreement-specific mechanics
  (§8.4). Strong general company-law sourcing exists (DIFC/ADGM common-law status, UAE CCL 2021/2025
  reforms, Saudi SJSC), but no DIFC.ae/ADGM.com official guidance or Al Tamimi/Clyde & Co client alert was
  found addressing founder vesting/leaver mechanics with the depth SeedLegals provides for the UK or
  Cooley/Clerky provide for Delaware. Treat MENA vesting-enforceability claims as directional; hard-flag
  "local counsel mandatory" in the skill for any MENA onshore/civil-law jurisdiction.
- **Time-sensitive, needs a live-law check at time of use**: the non-compete enforceability landscape
  (§2.1) — state legislatures amend noncompete statutes yearly and the federal posture just changed in
  Feb 2026; do not treat as permanently fixed text.
