# ch2-pre-contract-transparency

**Anchor:** User × Ch II × pre-contract transparency review. The user (or counsel for the user) reviews whether the seller, rentor, or lessor of a connected product, or the provider of a related service, has provided the minimum information required under Art. 3(2) or Art. 3(3) of Regulation (EU) 2023/2854 (Data Act) before contract conclusion. Mismatch between Art. 3(2) and Art. 3(3) is the most common drafting failure on the data-holder side and the most common review trigger on the user side.

**Routes from:**

- "Review this connected-product purchase contract for Data Act transparency compliance."
- "Did the related service provider give us what Art. 3(3) requires before sign-up?"
- "What information are we entitled to before we lease this device?"
- "We received a one-page disclosure. Is that enough under the Data Act?"
- "What are our redress options if the disclosure is incomplete?"

**Adjacent cards (route there instead if the facts indicate):**

- The user wants to draft an Art. 4(1) request based on what was disclosed: `ch2-user-direct-request.md`.
- The user wants to direct disclosure to a third party: `ch2-user-third-party-request.md`.
- The disclosure was given but the data holder has refused subsequent access: `ch2-trade-secret-stages-1-2.md` or `ch2-trade-secret-stage-3-refusal.md` (trade-secret grounds) or `ch2-safety-security-handbrake.md` (safety/security grounds).

---

## Canonical fact pattern

A natural or legal person (the prospective user) is about to enter into a contract for the purchase, rent, or lease of a connected product, or for the provision of a related service, or both. The counterparty has produced a pre-contract information sheet, terms and conditions, or product datasheet that purports to satisfy Art. 3(2) or Art. 3(3). The user (or counsel) reviews the disclosure against the regulation's minimum content list.

The user is typically an enterprise; the consumer-facing version of the review is shorter because most consumer disclosures are now templated. The connected product was, or will be, placed on the Union market within the meaning of Art. 2(22). The contract has not yet been concluded; if it has, the review is a post-contract gap analysis, not a transparency review.

---

## Critical disciplines

- **Art. 3(2) and Art. 3(3) are different lists.** Art. 3(2) (purchase, rent, lease of a connected product) has four items. Art. 3(3) (provision of a related service) has nine items. Conflating them produces an under-inclusive review on related services and an over-inclusive one on product sales. The full Art. 3(3) list includes trade-secret-holder identification (Art. 3(3)(h)) and complaint-route information (Art. 3(3)(g)), neither of which appears in Art. 3(2).
- **"At least" is a floor, not a ceiling.** Art. 3(2) and Art. 3(3) both open with "at least the following information". A disclosure that meets the minimum may still be insufficient if, on the facts, additional information is necessary for the disclosure to be "clear and comprehensible". Conversely, a disclosure that omits a listed item fails the minimum on its face.
- **Temporal scope.** Art. 3 applies to connected products and related services placed on the market after 12 September 2026 (Art. 50(2)). For products placed on the market before that date, the Art. 3 obligation does not apply, although the Art. 4 access right does for data generated after 12 September 2025. State the temporal scope when the answer turns on it; see `references/gotchas.md` entry 4 on the wider timeline.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check, Art. 1(6) carve-outs, and the Art. 2(22) placement test. Pre-contract reviews most often fail scope on Art. 2(5) "connected product" limb (iii): if the device's primary function is storing, processing, or transmitting data on behalf of a party other than the user (e.g. a server, router, smart speaker primarily acting as a hub), the device is not a connected product and Art. 3 does not apply. Check Art. 2(6) for related services: bidirectional data exchange AND impact on connected-product behaviour (FAQ Q10 framing). Power supply, connectivity, and repair/maintenance are not related services.

### Step 2: Chapter identification

Chapter II. Art. 3 sits in the pre-contract transparency layer of the user-access regime. The disclosure obligations are independent of the Art. 4(1) access right; a defective disclosure does not by itself prevent the user from making an Art. 4(1) request later, but it is a complaint ground under Art. 37(5)(b) and an unfair-terms hook under Art. 4(4) (non-neutral design) and Art. 13 in Ch IV (unfair contractual terms imposed on the user).

### Step 3: Role mapping

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Seller, rentor, or lessor of the connected product (may be the manufacturer) | Subject of the Art. 3(2) disclosure obligation; will typically be data holder under Art. 2(13) once the contract concludes | Controller, typically, for personal data generated by the product | May be trade-secret holder under Directive (EU) 2016/943 |
| Provider of the related service | Subject of the Art. 3(3) disclosure obligation; will be data holder for data generated through the related service | Controller for related-service personal data | May be trade-secret holder |
| Prospective user (natural or legal person) | User under Art. 2(12) on contract conclusion | Data subject if a natural person and the data relates to them; controller if an enterprise and the data relates to others (Recital 34) |  |
| Manufacturer (if not the seller) | May be the data holder by separate arrangement; Art. 3 disclosure obligation does not attach to the manufacturer as such unless it is also the seller | Controller in some configurations |  |

The seller, rentor, or lessor is the Art. 3(2) addressee even where it is not the manufacturer (a dealer, a fleet-lease provider, a marketplace). The related service provider is the Art. 3(3) addressee; it may or may not be the same entity as the seller. Where the product and the related service come from different entities, both disclosures are required and the user receives two separate information sheets.

### Step 4: Fact-category sorting

Card-specific dimensions to sort the disclosure against.

- **Connected product vs related service vs both.** Drives which list applies. A combined offering needs both Art. 3(2) and Art. 3(3) disclosures, not a single blended one.
- **Data type description.** The Art. 3(2)(a) and Art. 3(3)(a)/(b) items require description of the type, format, estimated volume, and (for related service data) collection frequency of the data the product or service will generate. The description must let the user form a reasonable expectation of what data will be created.
- **Real-time and storage characteristics.** Art. 3(2)(b)/(c) require disclosure of real-time generation capability and on-device or remote storage with retention duration. A disclosure that says "data is stored as necessary" without retention duration fails Art. 3(2)(c).
- **Trade-secret status.** Art. 3(3)(h) requires identification of trade-secret-holder identity where the prospective data holder is not itself the trade-secret holder. Art. 3(2) has no parallel limb; this is one of the Art. 3(3) extras.
- **Personal data dimension.** Where the product or service will generate personal data, the Art. 3 disclosure complements (does not replace) the GDPR Art. 13/14 controller-information notice. The user-facing privacy notice and the Data Act disclosure are separate documents in most live deployments.

### Step 5: Limb-by-limb application of Art. 3(2) and Art. 3(3)

If the contract is for purchase, rent, or lease of a connected product, the Art. 3(2) checklist applies. Each item is independent; missing any one defeats the minimum.

1. **Art. 3(2)(a): type, format, and estimated volume of product data.** Specific enough to let the user form a reasonable expectation. "Telemetry data" alone is too generic. "Engine telemetry sampled at 1 Hz, GPS at 0.1 Hz, approximately 50 MB per operating day" meets the limb.
2. **Art. 3(2)(b): continuous or real-time generation capability.** Yes/no, with brief context where helpful.
3. **Art. 3(2)(c): on-device vs remote storage, and where applicable retention duration.** Both elements where applicable.
4. **Art. 3(2)(d): how the user accesses, retrieves, or where relevant erases the data, including technical means and terms of use and quality of service.** This is the operative access route. Vague "contact customer service" does not meet the limb if a self-service portal exists.

If the contract is for provision of a related service, the Art. 3(3) checklist applies. Each item is independent.

1. **Art. 3(3)(a): product data the prospective data holder is expected to obtain, with arrangements to access or retrieve and storage and retention details.**
2. **Art. 3(3)(b): related service data to be generated, with the same arrangements.**
3. **Art. 3(3)(c): whether the prospective data holder will use readily available data itself, the purposes, and whether it intends to allow third parties to use the data for purposes agreed with the user.**
4. **Art. 3(3)(d): identity of the prospective data holder (trading name, geographical address of establishment), and where applicable other data processing parties.**
5. **Art. 3(3)(e): means of communication that make it possible to contact the data holder quickly and efficiently.**
6. **Art. 3(3)(f): how the user can request third-party sharing and end the sharing.**
7. **Art. 3(3)(g): the user's right to lodge a complaint with the competent authority designated pursuant to Art. 37.** The disclosure must name the relevant authority for the Member State where the user has its habitual residence, place of work, or establishment, or at minimum point the user to the public register the Commission maintains under Art. 37(7).
8. **Art. 3(3)(h): whether the prospective data holder is the trade-secret holder for trade secrets in the data, and where it is not, the identity of the trade-secret holder.**
9. **Art. 3(3)(i): contract duration and the arrangements for termination.**

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. The Art. 3 disclosure does not replace the GDPR Art. 13 controller-information notice. Where the user is an enterprise and the data subject is a natural person (e.g. employee using a connected work device), Recital 34 places the user-as-controller obligations onto the user; the Art. 3 disclosure must give the user enough information to discharge those obligations.
- **Sectoral lex specialis (warn-only).** If the product is a vehicle, medical device, financial-services component, energy infrastructure, AI system, eIDAS-relevant, NIS2-covered, or Cyber Resilience Act covered, run `references/gates/sectoral-lex-specialis.md`. Several sectoral regimes carry their own pre-contract information duties that the Data Act disclosure complements rather than replaces.
- **Member State implementing law (warn-only).** Run `references/gates/member-state.md` to identify the competent authority for Art. 3(3)(g). Member States have designated different authorities; the disclosure should name the right one for the user's circumstances.
- **DMA gatekeeper (not applicable on this card).** Pre-contract transparency does not engage the Art. 5(3) gatekeeper exclusion. The DMA overlay surfaces only at the Art. 5(1) third-party request stage.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 3(1) (design and default-accessibility obligation) applies only to connected products and related services placed on the market after 12 September 2026 (Art. 50(2)). Art. 3(2) and Art. 3(3) (pre-contract information obligations) apply from 12 September 2025 to all in-scope contracts concluded thereafter. Verbatim text at `sources/regulation-2023-2854.md` Art. 3; operative recitals at Recitals 23-25.
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final does not propose substantive amendments to Art. 3. See `sources/digital-omnibus-amendments-tracker.md` for confirmation.

---

## Decision point

After Steps 5 and 6, the analysis yields one of three paths.

1. **All applicable limbs satisfied.** Confirm compliance to the user. Note any "at least" enhancements the disclosure could helpfully add (e.g. a contact channel for Art. 3(3)(e) that is more specific than a general info@ inbox). Path 1 below.
2. **One or more limbs fail.** Identify each failure with the specific Art. 3(2)/(3) reference and what is missing. Recommend either pre-contract remediation (the user demands a corrected disclosure before signing) or post-contract complaint to the competent authority under Art. 37(5)(b). Path 2 below.
3. **Out-of-scope facts surface.** The product is not a connected product, the service is not a related service, the seller is a microenterprise or small enterprise under Art. 7(1), or the temporal scope under Art. 50 has not yet been reached. State the carve-out and stop. Art. 3 does not apply.

---

## Output skeleton: Path 1 (compliance memo, all limbs satisfied)

Memorandum, Markdown by default. Length: typically half a page to one page.

Structure:

```
1. Conclusion
   [One sentence: the pre-contract disclosure satisfies the
   applicable Art. 3 minimum. Identify which Article (3(2),
   3(3), or both).]

2. Disclosure reviewed
   [Document name, date, version. Specific Art. 3 list applied.]

3. Limb-by-limb compliance
   [Bullets or table mapping each applicable limb to the
   disclosure section that satisfies it. Quote the relevant
   disclosure language where useful.]

4. Optional enhancements
   [Where the disclosure meets the minimum but could be
   sharper (e.g. retention duration stated as a range rather
   than a fixed period), name the enhancement and leave the
   adoption decision to the user. Not a defect; a calibration.]

5. Next steps
   [If the user intends to make an Art. 4(1) request after
   contract conclusion, point to ch2-user-direct-request.md.]
```

## Output skeleton: Path 2 (gap analysis with remediation)

Memorandum, Markdown. Length: typically one to two pages.

Structure:

```
1. Conclusion
   [One sentence: the pre-contract disclosure does not satisfy
   Art. 3(N), specifically because [missing limbs].]

2. Disclosure reviewed
   [Document name, date, version. Specific Art. 3 list applied.]

3. Gap analysis

| Limb | Required content | Disclosure status | Remediation |
|------|------------------|-------------------|-------------|
| Art. 3(3)(a) | Nature, estimated volume, collection frequency of product data | Volume disclosed as "data necessary for service operation". Collection frequency not stated. | Demand specific frequency (Hz, sampling rate, or per-event description). |
| Art. 3(3)(g) | User's complaint right and the competent authority designated under Art. 37 | Not addressed. | Add reference to the competent authority in [Member State] and to the Commission's public register under Art. 37(7). |
| ... | ... | ... | ... |

4. Recommendation
   [Either: pre-contract remediation. Ask the counterparty to
   re-issue the disclosure with the gaps closed before signing.
   Or: post-contract complaint. After contract conclusion,
   lodge a complaint under Art. 37(5)(b) with the competent
   authority of the Member State of the user's habitual
   residence, place of work, or establishment, pursuant to
   Art. 38(1). The competent authority will investigate.]

5. Collateral exposure
   [Where the defective disclosure also engages Art. 4(4) (non-
   neutral interface design) or Art. 13 (unfair contractual
   terms imposed on the user, where the user is an enterprise
   under Ch IV), flag the additional ground.]

6. Next steps
   [If the user intends to make an Art. 4(1) request, point to
   ch2-user-direct-request.md. Defective pre-contract
   disclosure does not block the Art. 4(1) right.]
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 3(1), Art. 3(2), Art. 3(3) (always); Art. 4(4) (where the disclosure interacts with interface design); Art. 7(1) (microenterprise and small enterprise exclusion); Art. 37(5)(b) and Art. 38(1) (redress route).
- `sources/regulation-2023-2854.md` Art. 50(2) (temporal scope for Art. 3(1)); Recitals 23-25 (operative on transparency).
- `sources/faq-v1-4.md` Q10 on the related service test, framed as Commission interpretation.
- Where personal data is in scope, `sources/regulation-2023-2854.md` Recital 34 on the user-not-data-subject overlay.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded conditionally on personal data in scope).
- `references/gates/sectoral-lex-specialis.md` (warn-only).
- `references/gates/member-state.md` (warn-only, for the competent-authority reference).
- `references/gotchas.md` entries 3 (user-not-data-subject is controller), 4 ("without undue delay" has no numeric SLA, relevant if the disclosure overpromises a numeric response time), 9 (related service vs data processing service distinction).
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `ch2-user-direct-request.md` (the natural follow-on once contract is concluded).

---

## Drafter notes

- **Volume language is the usual failure point.** Disclosures routinely give qualitative volume statements ("the data necessary for service operation") that fail Art. 3(2)(a) or Art. 3(3)(a)/(b). Specific numerical estimates are required; ranges are acceptable; "as necessary" is not.
- **The Art. 3(3)(g) complaint route is almost always missing.** Most pre-contract disclosures drafted before September 2025 omit this limb entirely. Where the disclosure has been refreshed for the Data Act it is often the only thing changed; check that the named authority matches the user's actual Member State.
- **Microenterprise and small enterprise carve-out (Art. 7(1)).** The Art. 3 obligation does not apply to data generated through connected products manufactured or designed, or related services provided, by a microenterprise or small enterprise without disqualifying partner or linked enterprises. Confirm the manufacturer's or provider's size before producing a non-compliance finding.
