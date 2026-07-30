# ch3-compensation-challenge

**Anchor:** Data recipient × Ch III × Art. 9 compensation challenge. The recipient's side of the Art. 8 / Art. 9 framework, focused on the SME and not-for-profit research cap at Art. 9(4) and on what the recipient can do when the data holder's price is, in the recipient's view, unreasonable. The dispute settlement route under Art. 10 is the operative escalation path.

**Routes from:**

- "The data holder is charging us [amount]. Is that lawful under Art. 9?"
- "We are an SME. We're being quoted with a margin. Can we challenge this?"
- "How do we challenge a Ch III price under Art. 9(4)?"
- "The data holder will not break down their compensation calculation. What is our remedy?"
- "Can we go to a dispute settlement body on price alone?"

**Adjacent cards (route there instead if the facts indicate):**

- The challenge is to the substantive non-price terms, not the price: `ch3-frand-terms.md`.
- The challenge is to a specific unilaterally imposed unfair term under Art. 13: `ch4-unfairness-challenge.md`.
- The data holder is invoking trade-secret protection to deny access altogether (not to price it): `ch2-trade-secret-stages-1-2.md` (Ch II ladder) or `ch2-trade-secret-stage-3-refusal.md` (stage 3 refusal).

---

## Canonical fact pattern

A data recipient has approached a data holder for data under a Ch III obligation. The Ch III obligation exists, the data holder is willing to share, but the parties cannot agree on the compensation. The data holder has quoted a price, the recipient considers the price excessive or the calculation opaque, and the recipient is considering a challenge.

The recipient is typically an SME or a not-for-profit research organisation (in which case Art. 9(4) caps the price at directly-related cost), or it is a larger enterprise testing whether the price is fair, reasonable, and non-discriminatory under Art. 8 and 9 generally. The data holder may have provided some calculation basis but not at sufficient detail for the recipient to verify compliance with Art. 9.

The Commission has not yet adopted Art. 9(5) guidelines on calculating reasonable compensation (FAQ Q72, expected Q2/Q3 2026, not adopted as of May 2026). The analysis runs on the regulation alone.

---

## Critical disciplines

These three are the load-bearing disciplines for any compensation challenge. Hold all three.

- **Direction of compensation.** Ch III compensation flows from the data recipient to the data holder, not the other way around. See `references/gotchas.md` entry 15. Drafts that reverse the direction (or assume the holder owes the recipient anything) misstate the basic economics.
- **Art. 9(5) guidelines are forthcoming, not published.** Citations to "the Commission's guidelines on reasonable compensation" as if they have been adopted are wrong. The analysis runs on Art. 9 itself plus the Art. 8 fairness framework. See `references/gotchas.md` entry 16.
- **Art. 9(4) carve-out is two conditional layers.** First, the recipient must qualify as an SME or not-for-profit research organisation. Second, the recipient must not have a partner or linked enterprise that does not qualify as an SME. Both layers need to be tested separately on the facts; an SME-by-headcount that is a subsidiary of a large multinational does not get the Art. 9(4) cap.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies and that the Ch III trigger is in place. Run the Art. 1(2)/(3) scope check and the Art. 1(6) carve-outs. Confirm the obligation to share data: either an Art. 5 user-directed request or another Union or national law instrument adopted in accordance with Union law (Art. 12(1)). Without an obligation, Ch III does not apply; the data sharing is voluntary, and Art. 9 does not constrain price (Recital 42, last sentence).

Confirm the temporal hook. Chapter III applies to obligations under EU or national law that enter into force after 12 September 2025 (Art. 50, fourth sub-paragraph). Sharing obligations under instruments in force before that date are outside Ch III.

### Step 2: Chapter identification

Chapter III. Art. 9 governs compensation; Art. 8 supplies the FRAND wrapper; Art. 10 supplies the dispute settlement route. The compensation challenge sits inside Art. 9 but a non-discrimination challenge (Art. 8(3)) often runs in parallel: the recipient suspects it is being charged more than comparable categories.

Where the contract concluded contains a specific term that is unfair within the meaning of Art. 13 (for example, an unilaterally imposed price-variation clause under Art. 13(5)(g)), the Ch IV unfairness route is also available and may be more effective than an Art. 9 challenge. Run both in parallel where the facts support.

### Step 3: Role mapping

Required entity-by-entity mapping. Show as a table in the output.

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Data holder | Data holder (Art. 2(13)) | Controller, typically |  |
| Data recipient (the challenger) | Data recipient (Art. 2(14)) | Controller for personal data received, or processor depending on the arrangement | SME or not-for-profit research organisation flag if Art. 9(4) is in play |
| User (if Art. 5 is the trigger) | User (Art. 2(12)) | Controller under Recital 34 if not the data subject; data subject if a natural person |  |

Where the recipient is asserting SME status, the role mapping records both (i) the recipient's own SME qualification under Annex I to Recommendation 2003/361/EC (headcount under 250, turnover at most EUR 50 million or balance sheet at most EUR 43 million) and (ii) the absence of a non-SME partner or linked enterprise. Where the recipient is a not-for-profit research organisation, the record identifies the legal form and the not-for-profit basis.

### Step 4: Fact-category sorting

The challenge needs the cost lines and comparator categories disaggregated.

- **Costs incurred in making the data available (Art. 9(2)(a)).** Formatting, dissemination via electronic means, storage. Recital 47 elaborates: technical costs (data reproduction, dissemination, storage), processing costs (formatting), costs of facilitating the specific data sharing request. Costs that are shared across multiple requests cannot be charged in full to a single recipient (Recital 47 sixth sentence).
- **Investments in collection and production (Art. 9(2)(b)).** Recital 47 elaborates on the margin: it may vary by volume, format, or nature; it may decrease where the holder collected the data for its own business without significant investment; it may be limited or excluded where the recipient's use does not affect the holder's own activities; co-generation by the user reduces the margin further. The margin is not available against Art. 9(4) recipients at all.
- **Volume, format, nature (Art. 9(3)).** Where pricing varies by these factors, the variation needs to be objectively justified.
- **Comparator categories (Art. 8(3)).** Has the holder charged comparable recipients differently? Differentiation justified by objective reasons is not discrimination (Recital 45, third sentence); differentiation without objective reason is.
- **Transparency of calculation (Art. 9(7)).** Has the holder provided sufficient detail to permit the recipient to assess compliance with Art. 9(1)-(4)? A skeleton "cost-plus 30%" without cost lines does not satisfy Art. 9(7).

### Step 5: Limb-by-limb application of Art. 9 (recipient's perspective)

Art. 9 reads as a constraint on the holder's pricing; the recipient's challenge tests the constraint limb by limb.

1. **Art. 9(1) reasonableness and non-discrimination.** The compensation must be reasonable and non-discriminatory. Margin is permitted in principle. The recipient challenges either reasonableness (price too high relative to cost-plus reference) or non-discrimination (price higher than comparable categories receive).
2. **Art. 9(2)(a) costs.** Has the holder identified the cost lines actually incurred in making the data available to this recipient? Are they limited to formatting, dissemination, storage (and analogous costs per Recital 47)? Costs of data collection or production do not fall under Art. 9(2)(a) (Recital 47 first sub-paragraph, fourth sentence): "Those costs may be technical costs ... but not for data collection or production."
3. **Art. 9(2)(b) investments.** Where the holder claims a margin component reflecting collection and production investments, is the claim consistent with whether other parties contributed to obtaining, generating, or collecting the data (Recital 47)? Recital 47 last sentence: data co-generated by a connected product owned, rented, or leased by the user "could also reduce the amount of the compensation in comparison to other situations where the data are generated by the data holder for example during the provision of a related service."
4. **Art. 9(3) volume, format, nature.** Is the price tied to these factors with objective basis, or is it a flat figure that does not reflect the variation?
5. **Art. 9(4) SME / not-for-profit research cap.** Where the recipient qualifies, compensation shall not exceed the Art. 9(2)(a) cost base. No margin. Recital 49: "the reasonable compensation for making data available to be paid by them should not exceed the costs directly related to making the data available. Directly related costs are those costs which are attributable to individual requests, taking into account that the necessary technical interfaces or related software and connectivity is to be established on a permanent basis by the data holder." The fixed infrastructure costs are amortised, not charged in full to each SME recipient.
6. **Art. 9(5) Commission guidelines.** Not yet adopted (FAQ Q72, expected Q2/Q3 2026). Cannot be relied on in current challenges; flag the pending status in the output.
7. **Art. 9(6) other Union or national law.** Where another Union or national instrument excludes compensation or sets a lower compensation for the specific data type, Art. 9(6) preserves that result. Run the sectoral gate where relevant.
8. **Art. 9(7) transparency.** The holder must provide the basis for the calculation in sufficient detail for the recipient to assess compliance with Art. 9(1)-(4). Recital 51 anchors the transparency duty: the holder provides sufficiently detailed information for the calculation. Refusal or evasion is itself an Art. 9(7) breach independent of whether the underlying price would be unreasonable.

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. The recipient's GDPR role (controller or processor) and legal basis are independent of the compensation analysis, but they affect the cost lines the holder may charge (for example, costs of GDPR-compliant minimisation or pseudonymisation may legitimately appear in Art. 9(2)(a) where they are necessary to make the data available).
- **DMA gatekeeper exclusion (warn-only).** Run `references/gates/dma-gatekeeper.md` if the recipient is or acts for a DMA-designated gatekeeper and the Ch III trigger is Art. 5; in that case, the sharing is unlawful and the compensation question does not arise.
- **Sectoral lex specialis (warn-only).** Art. 9(6) preserves other Union or national instruments that exclude or limit compensation. Run `references/gates/sectoral-lex-specialis.md` to identify any sectoral price ceiling.
- **Member State implementing law (warn-only).** Dispute settlement bodies under Art. 10 are certified at Member State level. Run `references/gates/member-state.md` to identify the certified body and the procedural rules.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 9 of Regulation (EU) 2023/2854 (Data Act) governs. The seven-limb test above is the operative framework. Verbatim text at `sources/regulation-2023-2854.md` Art. 9 (lines 800-825); operative recitals at Recitals 46, 47, 49, 51.
- **Proposed amendment under Digital Omnibus.** COM(2025) 833 final does not materially alter Art. 9. The Art. 9(5) guidelines remain pending separately (FAQ Q72: expected Q2/Q3 2026, not adopted as of May 2026). See `references/gotchas.md` entry 16 and `sources/digital-omnibus-amendments-tracker.md`.

---

## Decision point

After Steps 5 and 6, the analysis yields one of four paths.

1. **Art. 9(4) cap applies and the holder's price exceeds cost.** The recipient is an SME or not-for-profit research organisation and the price includes a margin. The challenge is straightforward; produce the Art. 9(4) demand letter (Output Path 1 below).
2. **Art. 9(7) transparency fails.** The holder has not provided the basis for calculation in sufficient detail. The recipient demands it (Output Path 2 below). Until the calculation is disclosed, the substantive reasonableness challenge under Art. 9(1)-(3) is premature.
3. **Substantive challenge under Art. 9(1)-(3) or Art. 8(3) non-discrimination.** The recipient is a larger enterprise or the Art. 9(4) cap does not apply, but the price is excessive against cost-plus reference, or differs without objective reason from what comparable recipients pay. Escalate to Art. 10 dispute settlement (Output Path 3 below). The dispute settlement body is the practical forum because Art. 10(1) explicitly covers FRAND disputes in Ch III and Ch IV.
4. **Challenge has no Art. 9 hook.** The recipient may be unhappy with the price but the holder is within its Art. 9 envelope (margin permissible, transparency satisfied, no discrimination shown). The card does not produce a challenge; it explains why and identifies what facts the recipient would need for a sustainable challenge.

---

## Output skeleton: Path 1 (Art. 9(4) cap demand letter)

Formal letter. Markdown. Lead with the SME or not-for-profit qualification and the Art. 9(4) operative effect.

Structure:

```
[Recipient letterhead placeholder]

To: [Data holder, full legal entity name and address]
Date: [Date of demand]
Subject: Reasonable compensation under Article 9(4) of Regulation (EU)
         2023/2854 (Data Act) for data sharing under [Ch III trigger]

1. The sharing arrangement
   [Identification of the Ch III trigger: Art. 5 request dated [date]
   or [other Union or national law instrument] sharing obligation.
   Reference to the data holder's quote dated [date].]

2. Recipient qualification under Art. 9(4)
   [Statement that the recipient is an SME within the meaning of
   Annex I to Recommendation 2003/361/EC, supported by:
   (a) headcount and turnover or balance-sheet figures;
   (b) confirmation that the recipient does not have a partner or
       linked enterprise that does not qualify as an SME (or, for a
       not-for-profit research organisation, equivalent confirmation
       of legal form and basis).]

3. Operative effect of Art. 9(4)
   Art. 9(4): "Where the data recipient is an SME or a not-for-profit
   research organisation and where such a data recipient does not have
   partner enterprises or linked enterprises that do not qualify as
   SMEs, any compensation agreed shall not exceed the costs referred
   to in paragraph 2, point (a)."
   The cap is the Art. 9(2)(a) cost base only. No margin under Art.
   9(2)(b) is permissible against this recipient. Recital 49 confirms:
   "the reasonable compensation for making data available to be paid
   by them should not exceed the costs directly related to making the
   data available."

4. The holder's quote
   [Quote the holder's price and stated basis. Identify the components
   that go beyond Art. 9(2)(a) cost (margin; investment-recovery
   element; volume-pricing markup; etc.). State the excess amount
   relative to Art. 9(2)(a) cost.]

5. Request
   [Request that the holder reduce the price to the Art. 9(2)(a) cost
   level. Request that the holder provide, pursuant to Art. 9(7), the
   basis for the recalculated cost figure in sufficient detail for
   the recipient to verify Art. 9(4) compliance.]

6. Escalation
   [Statement that, in the absence of a revised quote within a
   reasonable period, the recipient will refer the dispute to a
   certified dispute settlement body under Art. 10, without prejudice
   to its right to seek redress before a court or tribunal of a
   Member State. Reference to the Art. 10 dispute settlement option,
   which under Art. 10(1) explicitly covers FRAND disputes in Ch III.]

[Signature block placeholder]
```

---

## Output skeleton: Path 2 (Art. 9(7) transparency demand)

Short formal letter. Markdown. Demands the basis for calculation.

```
[Recipient letterhead placeholder]

To: [Data holder]
Date: [Date]
Subject: Request for compensation calculation basis under Article 9(7)
         of Regulation (EU) 2023/2854 (Data Act)

Pursuant to Art. 9(7), the data holder is required to provide the data
recipient with information setting out the basis for the calculation
of the compensation in sufficient detail so that the recipient can
assess whether the requirements of Art. 9(1) to (4) are met.

The compensation quoted on [date] in the amount of [amount] does not
include the basis for calculation in the detail required by Art. 9(7).
Specifically, [identify what is missing: itemised costs under Art.
9(2)(a); allocation methodology where costs are shared across
recipients; investment recovery basis under Art. 9(2)(b); volume,
format, or nature factors under Art. 9(3); etc.].

The recipient requests that the data holder provide the calculation
basis within [reasonable period, e.g. 14 days] in sufficient detail
for assessment under Art. 9(1) to (4). The recipient reserves all
rights, including escalation to Art. 10 certified dispute settlement
should the calculation basis disclose terms that are unreasonable,
discriminatory, or in excess of the Art. 9(4) cap (if applicable).

[Signature block placeholder]
```

---

## Output skeleton: Path 3 (Art. 10 dispute settlement referral note)

Internal memorandum or instruction note. Markdown. Lays out the dispute settlement case the recipient brings to the certified body.

```
Memorandum: dispute settlement referral under Art. 10 of Regulation
(EU) 2023/2854 (Data Act)

1. Parties
   Data holder: [identity]
   Data recipient: [identity, qualification under Art. 9(4) if any]

2. Subject of dispute
   Compensation under Art. 9 for data sharing obligation arising under
   [Ch III trigger]. Specifically: [Art. 9(1) reasonableness; Art. 9(3)
   volume/format/nature; Art. 8(3) non-discrimination; Art. 9(4) cap
   breach; Art. 9(7) transparency breach; or combinations].

3. Jurisdiction of dispute settlement body
   Art. 10(1) covers "disputes relating to the fair, reasonable and
   non-discriminatory terms and conditions for, and transparent manner
   of, making data available in accordance with this Chapter and
   Chapter IV." The price dispute falls squarely within Art. 10(1).

4. Certified body
   [Identification of the Art. 10(5)-certified body the recipient
   refers the matter to. Per Art. 10(6), the Commission publishes the
   list. Reference to the Member State of certification.]

5. Decision timeline
   Art. 10(9): the body adopts its decision within 90 days of receipt
   of the request. Written or durable-medium decision, supported by a
   statement of reasons.

6. Binding nature
   Art. 10(12): the decision is binding on the parties only if both
   have explicitly consented to its binding nature prior to the start
   of proceedings. Without such consent, the decision is persuasive
   but not enforceable. Recipient strategy on consent depends on the
   strength of the substantive case and the cost asymmetry.

7. Costs
   Art. 10(3): where the body decides in favour of the recipient, the
   data holder bears all fees and reimburses other reasonable
   expenses. Where the body decides in favour of the holder, the
   recipient is not required to reimburse unless the body finds that
   the recipient manifestly acted in bad faith.

8. Without prejudice to court recourse
   Art. 10(13): the dispute settlement route does not affect the right
   of either party to seek effective remedy before a court or tribunal
   of a Member State.

9. Substantive case
   [Limb-by-limb analysis from Step 5 above: which Art. 9 limb is
   breached, with citations and supporting facts.]

10. Recommended next step
    [Submit referral to [identified body] within [timeframe]. Internal
    counsel adapts.]
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 8(3) (non-discrimination, where in issue); Art. 9 in full (always); Art. 10 (dispute settlement route); Art. 12 (Ch III scope); Art. 50 (temporal applicability).
- `sources/regulation-2023-2854.md` Recital 45 (non-discrimination; burden of proof on data holder); Recital 46 (reasonable compensation principle); Recital 47 (cost and margin structure; co-generation reduction); Recital 49 (SME cost-only cap); Recital 51 (transparency).
- `sources/faq-v1-4.md` Q38 (Commission interpretation on differentiation); Q39 (Commission interpretation on no upper or lower limit to compensation; SME no-margin rule); Q40 (Commission interpretation on Art. 10 dispute settlement coverage); Q72 (Commission interpretation on Art. 9(5) guidelines timing). Frame as Commission interpretation.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded if personal data in scope).
- `references/gates/dma-gatekeeper.md` (loaded if the recipient is or acts for a DMA-designated gatekeeper and the trigger is Art. 5).
- `references/gates/sectoral-lex-specialis.md` (warn-only; Art. 9(6) preserves sectoral compensation rules).
- `references/gates/member-state.md` (warn-only; for Art. 10 body selection).
- `references/gotchas.md` entry 15 (Ch III compensation is data-recipient-to-data-holder). Mandatory.
- `references/gotchas.md` entry 16 (Art. 9(5) Commission guidelines are forthcoming, not published). Mandatory on every compensation challenge.
- `references/gotchas.md` entries 4 ("without undue delay" has no numeric SLA), 19 (FAQ is non-authoritative). Check on each.
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (no material Art. 9 amendments; Art. 9(5) guidelines pending).
- Adjacent card: `ch3-frand-terms.md` (data-holder-side framing of the same articles).

---

## Drafter notes

Operational observations for using this card. Three only.

- **Art. 9(7) is the most practical lever.** When the holder will not break down the calculation, the recipient does not need to win the substantive Art. 9(1)-(4) argument first; the transparency obligation under Art. 9(7) is independent. Recital 51 anchors it. A demand under Art. 9(7) puts the holder in breach if it refuses to disclose, and the disclosure often resolves the substantive dispute by exposing where the price departs from cost.
- **SME qualification needs the linked-enterprise check.** Art. 9(4) excludes recipients with partner or linked enterprises that do not qualify as SMEs. A standalone SME by headcount that is owned by a non-SME parent does not benefit. Run the Annex I to Recommendation 2003/361/EC analysis fully; do not rely on the headcount and turnover thresholds alone.
- **Art. 10 dispute settlement is non-binding by default.** Art. 10(12): binding only if both parties consent before proceedings start. The recipient strategy is fact-sensitive: where the substantive case is strong and the holder has no incentive to comply with a non-binding finding, court proceedings under Art. 10(13) may be the more effective path. Where the holder is repeat-player and reputation-sensitive, an Art. 10 finding (even non-binding) often produces compliance.
