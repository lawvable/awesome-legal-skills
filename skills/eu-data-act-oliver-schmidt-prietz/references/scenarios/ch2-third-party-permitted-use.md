# ch2-third-party-permitted-use

**Anchor:** Third party × Ch II × Art. 6 permitted use. A third party has received, or is about to receive, data under Art. 5(1) from a data holder at the user's request. The third party (or counsel for the third party) reviews what it may lawfully do with the data under Art. 6(1) and what it must not do under the closed list of prohibitions in Art. 6(2). The card is built around the closed-list discipline: Art. 6(2) is exhaustive on its face, unlike most other illustrative lists in the regulation.

**Routes from:**

- "We have received Art. 5 data. What can we do with it?"
- "Draft a use-restriction memo for our internal teams on data received under the Data Act."
- "Can we onward-share this data to a sub-processor?"
- "Can we use this data to train our model?"
- "Can we develop a related service using this data?"
- "We are a gatekeeper recipient candidate. What are the limits?"

**Adjacent cards (route there instead if the facts indicate):**

- The user is preparing the Art. 5(1) request: `ch2-user-third-party-request.md`.
- The data holder is preparing the Art. 5(1) response or is at the trade-secret stages: `ch2-data-holder-response.md` and `ch2-trade-secret-stages-1-2.md` (Art. 4(6)-(7) analysis transposes to Art. 5(9)-(10) for the third-party route).
- The third party has been notified of suspected misuse by the data holder under Art. 11(2): the Art. 11 enforcement card is not yet drafted; this card's analysis identifies the Art. 6(2) limbs that would underpin an Art. 11 claim.

---

## Canonical fact pattern

A third party (typically an enterprise: aftermarket service provider, analytics vendor, fleet manager, data intermediation service, research organisation) has received or is about to receive data under Art. 5(1) made available by the data holder at the user's request. The third party has a contract with the user (Art. 6(1) requires this) specifying purposes and conditions for the processing. The data may include trade-secret-protected material and may include personal data.

The third party intends to use the data for the agreed purposes. The third party is reviewing what other uses are permitted, what onward-sharing is permitted, and what is closed off by Art. 6(2). The third party's downstream products and services may include possibilities the third party is unsure about: training internal AI models, profiling for service personalisation, onward sharing to sub-processors or business partners, developing related services or competing connected products. The card sorts each against Art. 6.

---

## Critical disciplines

- **Art. 6(2) is a closed list of prohibitions, not illustrative.** Most lists in the Data Act use "in particular" or "such as" (illustrative); Art. 6(2) does not. The list is exhaustive on its face. Unlisted behaviours are not prohibited by Art. 6(2) (although they may be prohibited by GDPR, competition law, consumer protection law, or other Union or national law). The closed character cuts both ways: it constrains the third party's risk-mapping but also limits the data holder's room to add contractual prohibitions on Art. 6(2) grounds. See `references/gotchas.md` entry 12.
- **Art. 6(2)(d) gatekeeper limit.** No onward sharing to any undertaking designated as a gatekeeper under Art. 3 of Regulation (EU) 2022/1925 (DMA). Direct and indirect routing are both within scope; this mirrors the Art. 5(3) tripartite bar on gatekeepers as recipients. See `references/gotchas.md` entry 11.
- **Art. 6(2)(e) competing-product prohibition.** The third party may not use the data to develop a connected product that competes with the connected product from which the accessed data originate, and may not share the data with another third party for that purpose. The third party may also not use any non-personal product data or related service data to derive insights about the economic situation, assets, or production methods of, or use by, the data holder. The recital framing (Recital 32) confirms that lawful purposes can include reverse engineering for repair or aftermarket service; the prohibition targets competition on the same product market.
- **Art. 6(1) contract requirement.** The third party processes only for the purposes and under the conditions agreed with the user. The user-third-party contract is the operative envelope; uses outside it are not authorised by Art. 6(1). The third party erases the data when no longer necessary for the agreed purpose, unless otherwise agreed with the user in relation to non-personal data.
- **The third party is a data recipient on receipt and may itself become a data holder.** Where the third party's processing of the received data creates downstream readily available data through the third party's connected products or related services, the third party may itself fall within the data-holder regime for that downstream data. Role permanence is not assumed (see `references/gotchas.md` entry 2 and Recital 34).

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check, Art. 1(6) carve-outs, and the Art. 2(22) placement test for the connected product whose data was made available. Art. 5(2) confirms that data in the context of testing of new connected products, substances, or processes not yet placed on the market is out of scope of the Art. 5(1) right unless contractually permitted; if the data sits in that bracket and the third party has received it through some other route, the Art. 6 analysis still runs but the upstream chain is irregular.

### Step 2: Chapter identification

Chapter II. Art. 6 is the operative third-party obligations article. Art. 5(9) and 5(10) (trade-secret safeguards and withholding) attach upstream and may bind the third party through its own undertaking to the data holder. Art. 11 enforcement is downstream; Art. 11(2) sets out the remedies the data holder may invoke if the third party has provided false information, used the data for unauthorised purposes including the development of a competing connected product (an Art. 6(2)(e) breach), unlawfully disclosed data, failed to maintain agreed Art. 5(9) measures, or altered or removed the data holder's technical protection measures.

### Step 3: Role mapping

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Third party (recipient) | Third party in the Art. 5 sense; data recipient (Art. 2(14)) on receipt | Controller for the personal data it receives, typically; or joint controller with the user in some configurations | Possibly becoming data holder for downstream data |
| User | User (Art. 2(12)) | Data subject if natural person; controller if enterprise (Recital 34) | Counterparty under the Art. 6(1) contract |
| Data holder | Data holder (Art. 2(13)) | Controller pre-disclosure | Trade-secret holder for trade-secret data; may invoke Art. 11(2) remedies on misuse |
| Affected data subjects |  | Data subjects | Rights preserved under Art. 5(13); Art. 20 GDPR portability parallel route |
| Sub-processor or onward-sharing recipient (if any) | Possibly another third party in the Art. 5 sense, but only under the Art. 6(2)(c) conditions | Processor or sub-controller depending on configuration |  |

Three role nuances:

- The third party's GDPR posture is independent of the Data Act posture. Most third parties are controllers for personal data they receive; processor configurations exist but are less common in Art. 5 routes.
- Where the user is an enterprise (controller under Recital 34), the user-third-party arrangement may be controller-to-controller, joint controllership, or controller-to-processor; the third party's classification under GDPR drives its Art. 6 GDPR obligations independent of Art. 6 Data Act.
- The third party may itself be (or become) a gatekeeper. Where the third party is or expects to become a gatekeeper, Art. 6(2)(d) does not bar it from receiving data via Art. 5 (the bar runs the other way: a gatekeeper cannot be an Art. 5 third party at all under Art. 5(3)). Run `references/gates/dma-gatekeeper.md` even from the third-party side as a check.

### Step 4: Fact-category sorting

Card-specific dimensions to sort the data and the intended uses against.

- **Trade-secret data vs not.** Where the third party has received data identified as trade-secret under Art. 5(9), the safeguards arrangement with the data holder applies. Art. 6(2)(g) prohibits disregarding the specific measures agreed and undermining confidentiality. Art. 6(2)(c) prohibits onward sharing without ensuring the recipient takes all the agreed safeguards.
- **Personal vs non-personal.** Drives the Art. 6(2)(b) profiling restriction (which overrides Art. 22(2)(a) and (c) GDPR exceptions and limits profiling to what is necessary to provide the requested service). Drives the GDPR controller analysis.
- **Product data vs related service data.** Both in scope of Art. 6. The Art. 6(2)(e) competing-connected-product bar targets the connected product the data originated from; the Recital 32 carve-out for related-service development applies in parallel.
- **Intended uses by the third party.** The card-specific sort. Each intended use is mapped against Art. 6(1) (agreed purpose with the user) and Art. 6(2) (the closed list). Common intended uses to assess:
  - Provide the agreed service to the user.
  - Develop a related service that uses the data.
  - Develop a competing connected product. (Prohibited under Art. 6(2)(e).)
  - Develop a non-competing connected product. (Not prohibited by Art. 6(2)(e); may engage Art. 6(1) if outside the agreed purpose.)
  - Train an AI model. (Not prohibited by Art. 6(2) as such; engages Art. 6(1) purpose constraint and, where personal data is in scope, GDPR.)
  - Profile the user's customers. (Constrained by Art. 6(2)(b): only necessary to provide the requested service.)
  - Onward share to a sub-processor. (Permitted only under Art. 6(2)(c): contract with the user AND the onward recipient takes all necessary safeguards.)
  - Onward share to a business partner. (Same Art. 6(2)(c) condition; Art. 6(2)(d) absolute bar if the partner is a gatekeeper.)
  - Use to derive insights about the data holder. (Prohibited under Art. 6(2)(e) second clause: third parties shall also not use any non-personal product data or related service data made available to them to derive insights about the economic situation, assets, and production methods of, or use by, the data holder.)
  - Use in a manner that has an adverse impact on the security of the connected product or related service. (Prohibited under Art. 6(2)(f).)
  - Prevent a consumer user from making the data available to other parties. (Prohibited under Art. 6(2)(h).)

### Step 5: Limb-by-limb application of Art. 6(1) and Art. 6(2)

Art. 6(1) cumulative:

1. **Purpose constraint.** Process only for the purposes agreed with the user. The contract is the operative document; the third party reviews the contract before each new use.
2. **Conditions constraint.** Process under the conditions agreed with the user. Conditions may include technical and organisational measures, retention periods, audit rights.
3. **GDPR overlay (insofar as personal data are concerned).** The third party's processing of personal data is subject to Union and national law on the protection of personal data including the rights of the data subject.
4. **Erasure when no longer necessary.** Default rule for the data; the user and the third party may otherwise agree in relation to non-personal data only.

Art. 6(2) closed list. Each item independent; the third party must clear all eight.

1. **Art. 6(2)(a): No undue difficulty in user choices or rights.** No dark patterns, no non-neutral choice presentations, no subverting or impairing user autonomy, decision-making, or choices, including via user digital interfaces. Mirrors the data-holder-side Art. 4(4) discipline on the third-party side.
2. **Art. 6(2)(b): No profiling beyond what is necessary to provide the requested service.** Notwithstanding Art. 22(2)(a) and (c) GDPR. This is a Data-Act-specific narrowing of profiling: even where GDPR would permit profiling (e.g. on contract performance or explicit consent grounds under Art. 22(2)), the Data Act limits the third party to profiling that is necessary for the service. Profiling for marketing, advertising, or independent commercial purposes is closed off.
3. **Art. 6(2)(c): No onward sharing except under contract with the user and with confidentiality safeguards.** Two cumulative conditions: a contract with the user authorising the onward share; the onward recipient takes all the necessary safeguards agreed between data holder and third party to preserve trade-secret confidentiality. Sub-processors, intra-group sharing, and joint-venture sharing all run through this limb.
4. **Art. 6(2)(d): No sharing with a gatekeeper.** Absolute bar. No carve-outs. The third party's compliance posture should include affirmative checks against the Commission's current register of designated gatekeepers under Art. 3 of Regulation (EU) 2022/1925 (DMA).
5. **Art. 6(2)(e): No competing-product development; no insight-derivation about the data holder.** Two clauses. First clause: no use of the data to develop a connected product that competes with the connected product from which the accessed data originate, and no sharing for that purpose. Second clause: no use of non-personal product data or related service data to derive insights about the data holder's economic situation, assets, or production methods, or use by the data holder.
6. **Art. 6(2)(f): No use that has an adverse impact on the security of the connected product or related service.** Targets uses that, by their effects, could weaken the product or service's security (e.g. publishing exploits, deploying the data into systems that interact insecurely with the product).
7. **Art. 6(2)(g): No disregarding the agreed Art. 5(9) measures; no undermining confidentiality.** Mirror of Art. 4(7)(c) on the third-party side.
8. **Art. 6(2)(h): No preventing a consumer user from onward sharing.** The consumer user has the right to make the data available to other parties; the third party cannot contractually or technically prevent that. Enterprise users do not benefit from this specific protection (their freedom to onward-share is governed by other parts of the regime).

### Step 6: Cross-regime gate check

- **DMA gatekeeper gate (always loaded on this card).** Read `references/gates/dma-gatekeeper.md`. The Art. 6(2)(d) bar runs even if the user has not flagged gatekeeper risk; the third party owes its own diligence. Verify the third party's onward-sharing destinations against the Commission's current register of designated gatekeepers. Recipient attestation language in onward-sharing contracts is the operational tool.
- **Trade Secrets Directive overlay (loaded if trade-secret data in scope).** Read `references/gates/trade-secrets-directive.md`. The third party's Art. 5(9) safeguards bind it; the Art. 6(2)(g) prohibition reinforces.
- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. The Art. 6(2)(b) profiling restriction is independent of GDPR Art. 22 and narrows the third party's profiling space. The data subject's rights, including Art. 15 access and Art. 20 portability, are unaffected by the third party's Data Act status.
- **Sectoral lex specialis (warn-only).** Run `references/gates/sectoral-lex-specialis.md`. Sectoral rules on data use (e.g. financial services data use, medical-device data use) may layer.
- **Member State implementing law (warn-only).** Run `references/gates/member-state.md`.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 6 of Regulation (EU) 2023/2854 (Data Act) governs. Verbatim text at `sources/regulation-2023-2854.md` Art. 6(1)-(2); operative recitals at Recitals 32 (competing-product framing; reverse engineering carve-out) and 33 (third-party scope).
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final does not propose substantive amendments to Art. 6. See `sources/digital-omnibus-amendments-tracker.md`.

---

## Decision point

After Steps 5 and 6, the analysis yields one of three paths.

1. **All intended uses clear Art. 6(1) and Art. 6(2).** Produce the use-restriction memo (Output Path 1 below) documenting that the intended uses are permitted, with internal control points to keep the third party within scope going forward.
2. **One or more intended uses fail Art. 6(2).** Identify the failures with specific limb references. Recommend either dropping the use, restructuring the use to comply (e.g. obtaining user contract for the onward sharing under Art. 6(2)(c) and putting safeguards in place; substituting a non-gatekeeper recipient under Art. 6(2)(d); pivoting the development away from a competing product under Art. 6(2)(e)), or escalating to the user-third-party contract for a renegotiation of purposes. Output Path 2.
3. **Intended use is in a grey area not addressed by Art. 6(2).** Because Art. 6(2) is a closed list, an unlisted use is not prohibited by Art. 6(2). Run the Art. 6(1) purpose-constraint analysis (is the use within the agreed purposes?) and the GDPR/competition-law/IP-law overlays. The use may be permitted under the Data Act and prohibited elsewhere, or permitted everywhere. Path 3: produce a memo that names the closed-list non-application and identifies the remaining legal overlays for the user's separate analysis.

---

## Output skeleton: Path 1 (clean use-restriction memo)

Internal memorandum or letter, Markdown by default. Length: typically one to two pages.

Structure:

```
[Third party letterhead placeholder]

To: [Internal teams or user, depending on audience]
Date: [Date of memo]
Subject: Permitted use of data received under Article 5(1)
         of Regulation (EU) 2023/2854 (Data Act)

1. Source of the data
   [Identification of the data holder, the connected product
   or related service, the user's Art. 5(1) request, and the
   date of receipt.]

2. Operative envelope (Art. 6(1))
   [Reference to the user-third-party contract dated [date].
   Agreed purposes: [list]. Agreed conditions: [list,
   including any technical or organisational measures,
   retention period, audit rights].]

3. Intended uses cleared
   [Each intended use, with the Art. 6(1) and Art. 6(2)
   analysis confirming permitted status. Examples:

   - Use 1: provide the agreed analytics service to the
     user. Cleared under Art. 6(1) (agreed purpose) and
     Art. 6(2) (no listed prohibition engaged).

   - Use 2: process to provide service personalisation
     features. Cleared under Art. 6(2)(b) on the basis that
     the personalisation is necessary to provide the
     requested service to the user.

   - Use 3: develop a related service that uses the data,
     to be offered to other customers. Cleared under
     Art. 6(2)(e) on the basis that the new service is not
     a connected product that competes with the connected
     product from which the data originate, and Recital 32
     framing is consistent. Note: out-of-scope if the new
     service is the kind that Art. 6(1) does not permit
     absent further agreement with the user; check the
     contract.

   - Use 4: onward sharing to [named sub-processor] under
     [data processing agreement]. Cleared under Art. 6(2)(c)
     on the basis that the user-third-party contract
     authorises the sub-processor's involvement and the
     sub-processor's safeguards mirror those agreed between
     data holder and third party under Art. 5(9).]

4. Internal control points
   [Specific operational measures the third party puts in
   place to maintain compliance:
   - Quarterly review of intended uses against Art. 6(1)
     purpose constraint.
   - Pre-engagement check on any new onward-sharing
     destination against the Commission's register of
     designated gatekeepers.
   - Quarterly review of profiling activity for Art. 6(2)(b)
     necessity.
   - Erasure or anonymisation review at the conclusion of
     each use cycle (Art. 6(1) final sentence).]

5. Escalation triggers
   [Specific events that would require legal review before
   proceeding:
   - Designation of any onward-sharing destination as a
     gatekeeper.
   - Proposed development of any connected product in or
     near the same product market as the data-holder's
     connected product.
   - Proposed change to processing purposes beyond those
     agreed with the user.
   - Notification from the data holder under Art. 11(2)
     alleging misuse.]
```

## Output skeleton: Path 2 (use-restriction memo with failures and remediation)

Memorandum. Length: typically one to three pages depending on the number of failed uses.

Structure (the structural variant of Path 1):

```
[Sections 1 and 2 as Path 1.]

3. Use-by-use analysis

| Intended use | Article applied | Analysis | Status |
|--------------|-----------------|----------|--------|
| [Use 1] | Art. 6(1); Art. 6(2)(...) | [Analysis] | Permitted |
| [Use 2] | Art. 6(2)(d) | [The proposed onward-sharing destination is a designated gatekeeper] | Prohibited |
| [Use 3] | Art. 6(2)(e) first clause | [The proposed product would compete with the connected product from which the data originate] | Prohibited |
| [Use 4] | Art. 6(2)(c) | [The user-third-party contract does not authorise this sub-processor; safeguards are not in place] | Conditionally permitted on contract amendment and safeguards put in place |

4. Remediation
   [Use-by-use remediation:

   - Use 2: substitute a non-gatekeeper onward recipient.
     Run `references/gates/dma-gatekeeper.md` recipient-
     attestation procedure on the replacement.

   - Use 3: drop the use, or restructure the development so
     that the resulting product is not in the same product
     market as the data holder's connected product. Note
     that "same product market" is defined by Union
     competition law principles (Recital 32). A non-
     competing complementary product is permissible.

   - Use 4: amend the user-third-party contract to
     authorise the sub-processor and confirm the safeguards.]

5. Internal control points and escalation triggers
   [As Path 1 sections 4 and 5.]
```

## Output skeleton: Path 3 (closed-list non-application; overlays flagged)

Short memo. Length: typically one page.

Structure:

```
[Sections 1 and 2 as Path 1.]

3. Intended use under review
   [Description of the intended use.]

4. Art. 6(2) closed-list analysis
   [Statement that Art. 6(2) is a closed list (in contrast to
   most Data Act lists, which are illustrative). The intended
   use is not within any of the eight enumerated prohibitions.
   Therefore Art. 6(2) does not prohibit the use.]

5. Remaining legal overlays
   [Identification of overlays that may still constrain or
   prohibit the use:

   - Art. 6(1) purpose constraint. Is the use within the
     agreed purposes under the user-third-party contract?
     If not, contract amendment is needed before the use
     proceeds.

   - GDPR. Where personal data is in scope, the use is
     subject to all GDPR conditions, including Art. 6 legal
     basis, Art. 9 special-category conditions, data
     minimisation, retention, and data subject rights.

   - Competition law. The use is subject to general Union
     and national competition law independent of the Data
     Act.

   - IP law (Recital 30, Art. 43). Existing IP rights in
     the data are not displaced by the Data Act, except for
     the specific sui generis database right exclusion at
     Art. 43.

   - Sectoral law where relevant.]

6. Recommendation
   [Either: proceed, having confirmed the overlays do not
   prohibit. Or: route to the relevant specialist for the
   overlay analysis before proceeding.]
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 6(1), Art. 6(2)(a)-(h) (always); Art. 5(9) (where trade-secret data in scope); Art. 11(2)-(5) (downstream enforcement).
- `sources/regulation-2023-2854.md` Recital 32 (competing-product framing; reverse-engineering carve-out for repair and aftermarket), Recital 33 (third-party scope, intermediation).
- Regulation (EU) 2022/1925 (DMA) Art. 3 (gatekeeper designation; Commission's public register), for the Art. 6(2)(d) check.
- `sources/faq-v1-4.md` Q36 (gatekeeper exclusion under Art. 5(3) and its DMA-side mirror), framed as Commission interpretation.
- Directive (EU) 2016/943 (Trade Secrets Directive) Art. 2(1) (trade-secret definition; the third party's safeguard duty under Art. 6(2)(c) and (g) presupposes the upstream identification).
- Regulation (EU) 2016/679 (GDPR) Art. 22 (profiling baseline that Art. 6(2)(b) overrides).

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/dma-gatekeeper.md` (always loaded on this card; Art. 6(2)(d) check).
- `references/gates/trade-secrets-directive.md` (loaded if trade-secret data in scope).
- `references/gates/gdpr-overlay.md` (loaded if personal data in scope).
- `references/gates/sectoral-lex-specialis.md` (warn-only).
- `references/gates/member-state.md` (warn-only).
- `references/gotchas.md` entries 2 (manufacturer not always data holder, relevant to the upstream chain), 3 (user-not-data-subject is controller), 6 (trade-secret ladder, relevant to Art. 5(9) safeguards binding the third party), 11 (Art. 5(3) tripartite reach), 12 (Art. 6(2) is closed), 14 (sui generis database right inapplicable, relevant if the data holder asserts it against the third party), 17 (Art. 11 remedies require predicate).
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `ch2-user-third-party-request.md` (the upstream user-side card).
- `ch2-data-holder-response.md` and `ch2-trade-secret-stages-1-2.md` (data-holder-side cards; the third party may receive copies of the Art. 5(9) safeguards arrangement from the data holder).
- `ch2-trade-secret-stage-3-refusal.md` (the data holder's stage-3 refusal under Art. 5(11) tracks the Art. 4(8) analysis; the third party is the addressee on that refusal route).

---

## Drafter notes

- **The closed list is a discipline both ways.** Counsel for the third party should not concede behaviours not within Art. 6(2) as prohibited, and the data holder should not claim prohibitions not within Art. 6(2). The contract negotiation often features both errors. Hold the closed-list line firmly: unlisted behaviours are governed by other Union and national law, not by Art. 6(2).
- **Recipient-attestation language in onward-sharing contracts.** The Art. 6(2)(d) gatekeeper bar runs against the third party even if the onward recipient is not currently a gatekeeper but is later designated. Recipient-attestation language (the onward recipient warrants its non-gatekeeper status, agrees to notify on any designation, and accepts indemnity terms) is the operational tool. See `references/gates/dma-gatekeeper.md`.
- **Reverse engineering for repair is lawful.** Recital 32 second-half clause confirms reverse engineering for purposes of repairing or prolonging the lifetime of a connected product, or for the provision of aftermarket services, is a lawful purpose under Art. 6. The third party that is an aftermarket service provider should not concede on this point in negotiation. The line is at "competing connected product" under Art. 6(2)(e), not at "reverse engineering" as such.
