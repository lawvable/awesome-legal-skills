# ch6-custom-built-carve-out

**Anchor:** Provider × Ch VI × Art. 31 custom-built carve-out assessment. The provider claims, or is considering claiming, that one or more of its data processing services fall within the Art. 31(1) custom-built carve-out and so escape some of the most onerous Ch VI obligations (Art. 23(d) unbundling, Art. 29 charges, Art. 30(1) functional equivalence, Art. 30(3) common-specification compatibility). The deliverable is a carve-out assessment: yes / no per service, with the reasoning visible.

**Routes from:**

- "Does the Art. 31 carve-out apply to our custom-built service?"
- "Our cloud service is white-labelled / heavily configured per customer. Are we in Ch VI?"
- "Are we exempt from the switching obligations because the service is bespoke?"
- "Is our standard SaaS with customer-specific modules custom-built under Art. 31?"
- "The Commission proposal would broaden Art. 31; what is the position today?"

**Adjacent cards (route there instead if the facts indicate):**

- The service is not within the carve-out; full Ch VI applies: `ch6-provider-compliance.md`.
- Customer-side review of switching clauses where the carve-out is invoked: `ch6-customer-contract-review.md`.
- Switching execution where the carve-out is invoked late: `ch6-switching-execution.md`.
- Charges where the Art. 31 carve-out removes Art. 29 obligations specifically: `ch6-charges.md`.

---

## Canonical fact pattern

The provider has one or more data processing services that have been built, configured, or extended to fit a specific customer's needs. The configuration may range from heavy customisation of a standard catalogue offering through to a fully bespoke development for a single customer. The provider wants to escape some Ch VI obligations on the basis that the service is custom-built. The carve-out, if it applies, is meaningful: Art. 31(1) removes Art. 23(d), Art. 29, Art. 30(1), and Art. 30(3) from the service's obligation set. Art. 25(2), Art. 25(3), Art. 25(4), Art. 25(5), Art. 26, Art. 27, Art. 28, Art. 30(2), Art. 30(4), Art. 30(5), Art. 30(6) continue to apply.

The carve-out is narrow. Per gotcha 13, industry usage of "custom-built" is broader than the Art. 31(1) test. A SaaS solution with customer-specific configurations, white-labelled deployments, and contractually negotiated SLAs typically does not qualify. The Commission's Digital Omnibus proposal would broaden the carve-out for pre-12-September-2025 contracts and SME / small-mid-cap providers, but that is a proposal, not law.

---

## Critical disciplines

- **Two cumulative qualifying limbs plus a negative limb.** Art. 31(1): "data processing services of which (i) the majority of main features has been custom-built to accommodate the specific needs of an individual customer OR (ii) where all components have been developed for the purposes of an individual customer, AND (iii) where those data processing services are not offered at broad commercial scale via the service catalogue of the provider of data processing services." The disjunctive in the first limb (majority of main features OR all components) is internally cumulative with the negative limb. A service that meets one of the qualifying alternatives but fails the negative limb is not within the carve-out. Per gotcha 13 and analysis-method.md the structure is qualifying alternatives plus a negative limb, not three independent options.
- **The negative limb is the bite.** Standard SaaS configured per customer fails the negative limb because the configurable offering is in the service catalogue at broad commercial scale. White-labelled deployments fail where the underlying engine is in the catalogue. Heavy professional-services engagements that build atop a catalogue service fail where the catalogue service is the underlying offering. Genuinely bespoke developments for a single customer that are not offered to others can pass.
- **The carve-out is partial, not total.** Art. 31(1) names specific obligations that fall away: Art. 23(d) (unbundling), Art. 29 (charges), Art. 30(1) (functional equivalence for IaaS), Art. 30(3) (common-specification compatibility). Per FAQ Q52 the Commission view is that the other Ch VI obligations continue to apply. Per FAQ Q52: "this does not mean that custom-built services are fully excluded from the scope of Chapter VI. The provisions not listed in Article 31(1) still apply. For example, providers of such services must make open interfaces available and ensure that data are exported in a structured, commonly used and machine-readable format."
- **Art. 31(3) disclosure is constitutive.** "Prior to the conclusion of a contract on the provision of the data processing services referred to in this Article, the provider of data processing services shall inform the prospective customer of the obligations of this Chapter that do not apply." A provider that does not disclose pre-contract has not validly invoked the carve-out. The disclosure is part of the carve-out, not a downstream administrative step.
- **The Art. 31(2) non-production carve-out is separate and broader.** Art. 31(2) removes Chapter VI in its entirety from "data processing services provided as a non-production version for testing and evaluation purposes and for a limited period of time." This applies to typical free trial, beta, and proof-of-concept deployments. The Art. 31(2) carve-out does not require either the qualifying or negative limbs of Art. 31(1); the conditions are non-production purpose and limited time. The total exclusion is the difference: Art. 31(1) removes some obligations, Art. 31(2) removes all of Ch VI.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies and the service is a "data processing service" within Art. 2(8). Per FAQ Q58a the Commission considers IaaS, PaaS, and SaaS all in scope. Confirm the service is in the temporal scope of Ch VI (post-12-September-2025 application for new obligations; legacy contracts have separate Ch VI exposure forward-looking). The carve-out analysis only matters where Ch VI would otherwise apply.

### Step 2: Chapter identification

Chapter VI. Art. 31 specifically (carve-out), with the cascading effect on Art. 23(d), Art. 29, Art. 30(1), Art. 30(3). The non-Art.-31 Ch VI obligations (Art. 25 contract terms, Art. 26 information, Art. 27 good faith, Art. 28 transparency, Art. 30(2), 30(4), 30(5), 30(6)) continue to apply even where the carve-out is established.

### Step 3: Role mapping

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Provider | Provider of data processing services |  | The party invoking the carve-out; bears the burden of substantiation |
| Individual customer | Customer (Art. 2(30)) | Controller, typically | The party for whom the service was custom-built; the carve-out is anchored to this customer |
| Other customers of the provider |  |  | Relevant to the negative limb: whether the same or substantially the same service is offered at broad commercial scale via the catalogue |
| The provider's service catalogue (as an artefact) |  |  | The reference point for the "broad commercial scale" assessment |

The negative-limb assessment turns on what the catalogue offers. A side-by-side comparison of the bespoke service and the closest catalogue offering is the basic analytical move.

### Step 4: Fact-category sorting

Card-specific dimensions to sort each candidate service against.

- **"Main features" identification.** Identify the main features of the service (compute, storage, networking, application logic, user interface, integrations, security, observability, etc.). The carve-out turns on whether the majority of these have been custom-built for the individual customer. A service with five main features of which three are custom-built passes the first qualifying alternative; one with two of five does not.
- **"All components" identification.** Components are narrower than main features; they are the building blocks. A service where all components have been developed for the individual customer passes the second qualifying alternative; a service where some components are off-the-shelf does not. This alternative is harder to satisfy than the first.
- **Catalogue presence.** Is the same or substantially the same service offered at broad commercial scale via the provider's catalogue. Cross-reference the marketing material, the public catalogue page, the pricing page, the sales playbook. A service marketed as "Enterprise Tier" with customer-specific configurations is in the catalogue; a service developed for a single customer that has never been marketed elsewhere is not.
- **Pre-contract disclosure.** Has the provider given the prospective customer clear pre-contract information about which Ch VI obligations do not apply (Art. 31(3)).
- **Contract date.** Pre-12-September-2025 contracts are within the existing Art. 31(1) regime today, with the Digital Omnibus proposing broader exemptions for them. Post-12-September-2025 contracts are subject only to the existing Art. 31 carve-outs.
- **Provider size.** SMEs and small mid-caps would benefit from a proposed exemption under the Digital Omnibus for non-IaaS obligations on pre-12-September-2025 contracts. Status today: not exempt as such; the general scope provisions (Art. 7) do not extend to Ch VI.

### Step 5: Limb-by-limb application of Art. 31

The assessment walks each limb explicitly. Each must be substantiated on the facts; the provider bears the burden.

**Art. 31(1) Limb 1, Alternative (a): "the majority of main features has been custom-built to accommodate the specific needs of an individual customer".** Test: (i) identify the main features of the service; (ii) for each, assess whether it was custom-built for the individual customer; (iii) confirm that the majority pass the custom-built test. "Custom-built" is more than configured: a configuration of an existing main feature does not custom-build it. The bar is development of the main feature for the individual customer's specific needs.

**Art. 31(1) Limb 1, Alternative (b): "where all components have been developed for the purposes of an individual customer".** Test: (i) identify the components; (ii) confirm each was developed for the individual customer's purposes. "All" is absolute. One off-the-shelf component defeats the alternative. This alternative is rarely satisfied in commercial cloud offerings because most include some off-the-shelf base layers.

**Art. 31(1) Limb 2, the negative limb: "those data processing services are not offered at broad commercial scale via the service catalogue of the provider of data processing services".** Test: (i) identify what is in the provider's service catalogue; (ii) assess whether the bespoke service in question is "offered at broad commercial scale" via that catalogue. A service that exists only for the individual customer and has never been catalogued passes. A service that is a heavy configuration of a catalogue offering typically fails. A service catalogued as a "Custom" tier with standard onboarding fails where customers are routinely sold the tier; the catalogue presence at broad commercial scale defeats the negative limb.

**Art. 31(3). Pre-contract disclosure.** Test: (i) confirm the provider has given the prospective customer clear pre-contract information about which Ch VI obligations do not apply because of Art. 31; (ii) confirm the information was clear and pre-contract, not post-contract or buried. Absent disclosure, the carve-out is not validly invoked even if the substantive limbs are met.

**Art. 31(2). The separate non-production carve-out.** Test: (i) is the service provided as a non-production version; (ii) is it for testing and evaluation purposes; (iii) is it for a limited period of time. If all three are satisfied, Ch VI does not apply in its entirety to the service. Typical fit: free trial, sandbox, beta, proof of concept, evaluation tier. Note that a free-tier production offering does not fit Art. 31(2); per FAQ Q55 a free-tier offering is in Ch VI and the customer retains switching rights.

**Cumulative satisfaction.** Art. 31(1) requires (Limb 1 alternative a OR Limb 1 alternative b) AND Limb 2 negative AND Art. 31(3) disclosure. Failure on any element defeats the carve-out, even if the others are clean. Art. 31(2) is independent and broader.

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded conditionally).** Load `references/gates/gdpr-overlay.md` only where the service processes personal data. The carve-out does not affect GDPR analysis; it is an internal Ch VI scope question.
- **Trade Secrets Directive overlay (rarely loaded).** The carve-out analysis is structural; the Trade Secrets Directive does not bear on it.
- **DMA gatekeeper exclusion (rarely loaded).** The DMA gate is Ch II / Art. 5 focused; the carve-out analysis is Ch VI. Cross-load only where the customer or destination provider is a gatekeeper, which would matter for the broader compliance posture but not for Art. 31.
- **Sectoral lex specialis (warn-only).** Custom-built cloud services for regulated sectors (DORA for finance, NIS2 for essential or important entities, sectoral cloud rules) face parallel obligations that the Art. 31 carve-out does not affect. Load `references/gates/sectoral-lex-specialis.md`.
- **Member State implementing law (warn-only).** Disputes over the carve-out are likely to surface at Art. 38 complaints or Art. 10 dispute settlement; the competent authority and certified dispute body are Member State specific. Load `references/gates/member-state.md`.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 31(1)-(3) of Regulation (EU) 2023/2854 (Data Act) governs. Operative reading per gotcha 13 and analysis-method.md: two qualifying alternatives in Limb 1 (majority of main features OR all components) AND the negative Limb 2 (not offered at broad commercial scale via the service catalogue) AND the pre-contract disclosure under Art. 31(3). The carve-out removes Art. 23(d), Art. 29, Art. 30(1), Art. 30(3) from the service's obligation set; the other Ch VI obligations continue (FAQ Q52). Art. 31(2) is the separate non-production carve-out that removes Ch VI in its entirety for non-production test or evaluation services provided for a limited period.
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final (19 November 2025) proposes: (a) expansion of the Art. 31(1) carve-out for contracts concluded on or before 12 September 2025, broadening the eligible services beyond the current narrow test; (b) SME / small-mid-cap exemption from non-IaaS Ch VI obligations for pre-12-September-2025 contracts; (c) operative clarification that early-termination penalties are permissible (relevant to Art. 29 charges analysis where Art. 31 does not apply). Per the tracker file: the proposal would broaden Art. 31(1) exemptions for custom-made DPS but limit the expansion to contracts concluded before or on 12 September 2025. Status: co-legislator negotiation, not adopted. See `sources/digital-omnibus-amendments-tracker.md`.

The output cites current law as operative. Provider clients who hope to rely on the Omnibus expansion need to be told it is not law and should plan to comply with current Art. 31 today. Legacy-contract clients should track the proposal closely; the expansion is targeted precisely at them.

---

## Decision point

After Steps 5 and 6 the carve-out assessment yields one of four paths.

1. **Carve-out applies.** All limbs satisfied including pre-contract disclosure. The Ch VI obligations listed in Art. 31(1) (Art. 23(d), Art. 29, Art. 30(1), Art. 30(3)) do not apply. The other Ch VI obligations continue. Output Path 1 below.
2. **Carve-out does not apply.** One or more limbs fail. The full Ch VI regime applies. Route to `ch6-provider-compliance.md`. Output Path 2 below summarises the failure and routes the user.
3. **Non-production carve-out under Art. 31(2) applies.** The service is a non-production test or evaluation offering for a limited period. Ch VI does not apply in its entirety. Output Path 3 below.
4. **Mixed portfolio.** Some services within the carve-out, some not. The assessment is per service. Output Path 4 below combines the others.

---

## Output skeleton: Path 1 (Art. 31(1) carve-out applies)

Memo, Markdown. Length: two to three pages.

```
Subject: Art. 31(1) carve-out assessment for [service], [provider]

Conclusion. The carve-out under Article 31(1) of Regulation (EU)
2023/2854 applies to [service]. The obligations under Article
23(d), Article 29, Article 30(1) and Article 30(3) do not apply.
The other Chapter VI obligations continue to apply.

Limb-by-limb assessment.

Limb 1 alternative (a) (majority of main features custom-built).
[Identification of main features; per-feature assessment;
conclusion that the majority is custom-built. Or: this alternative
does not apply; alternative (b) is the qualifying route.]

Limb 1 alternative (b) (all components developed for the individual
customer). [If applicable: identification of components; per-
component assessment; conclusion. Or: this alternative does not
apply; alternative (a) is the qualifying route.]

Limb 2 negative (not offered at broad commercial scale via the
service catalogue). [Identification of what is in the catalogue;
comparison with the bespoke service; conclusion that the bespoke
service is not catalogued at broad commercial scale.]

Pre-contract disclosure under Art. 31(3). [Reference to the
disclosure provided; confirmation that it was clear and pre-
contract.]

Obligations that fall away.
- Art. 23(d) unbundling.
- Art. 29 (all paragraphs): switching-charge reduction and
  abolition.
- Art. 30(1) functional equivalence (relevant to IaaS).
- Art. 30(3) common-specification compatibility.

Obligations that continue.
- Art. 23 (all other obstacles).
- Art. 25 in full (the mandatory contract terms).
- Art. 26 (information obligation).
- Art. 27 (good faith).
- Art. 28 (international-access transparency).
- Art. 30(2) (open interfaces) and Art. 30(4)-(6).
- Art. 34 in-parallel use mutatis mutandis.

Per FAQ Q52 the Commission interpretation confirms that custom-
built services are not fully excluded from Chapter VI; only the
provisions listed in Art. 31(1) fall away.
```

---

## Output skeleton: Path 2 (carve-out does not apply, routing)

Short memo, Markdown. Length: one to two pages.

```
Subject: Art. 31(1) carve-out assessment for [service], [provider]

Conclusion. The carve-out under Article 31(1) of Regulation (EU)
2023/2854 does not apply to [service]. The full Chapter VI regime
applies. Route to ch6-provider-compliance.md for the full
obligation set.

Limb that fails.
[Identification of the limb or limbs that fail, with the factual
basis. The most common failure point is Limb 2 negative: the service
is configured per customer but is offered at broad commercial scale
via the catalogue.]

The Commission Digital Omnibus proposal would broaden the carve-out
for pre-12-September-2025 contracts and for SME / small-mid-cap
providers. The proposal is not law. Status: co-legislator
negotiation. See sources/digital-omnibus-amendments-tracker.md.

If the contract was concluded on or before 12 September 2025, the
provider should track the proposal but plan to comply with current
Art. 31 today. If the contract is post-12-September-2025, the
proposal does not assist; full Chapter VI compliance is required.
```

---

## Output skeleton: Path 3 (Art. 31(2) non-production carve-out applies)

Short memo, Markdown. Length: one page.

```
Subject: Art. 31(2) non-production carve-out assessment for
         [service], [provider]

Conclusion. The carve-out under Article 31(2) of Regulation (EU)
2023/2854 applies. The service is provided as a non-production
version for testing and evaluation purposes for a limited period.
Chapter VI does not apply.

Conditions satisfied.
- Non-production version: [factual basis].
- Testing and evaluation purposes: [factual basis].
- Limited period of time: [factual basis: duration of the offering
  and the limitation mechanism].

Pre-contract disclosure under Art. 31(3). [Reference to the
disclosure provided.]

Boundary check. If the service moves into production for the
customer, or extends beyond a limited period, the Art. 31(2) carve-
out ceases and the full Chapter VI regime applies. The provider
should monitor the transition.

Per FAQ Q55 a free-tier production offering does not fit Art. 31(2);
free-tier customers retain switching rights under Chapter VI.
```

---

## Output skeleton: Path 4 (mixed portfolio)

Combined assessment. Markdown. Length: three to five pages.

```
Subject: Art. 31 carve-out assessment, [provider] portfolio

Conclusion. Of [N] services assessed, [n1] fall within Art. 31(1)
custom-built carve-out; [n2] fall within Art. 31(2) non-production
carve-out; [n3] are within full Chapter VI. The per-service
breakdown is below.

Per-service assessment.
| Service | Carve-out claim | Result | Obligations falling away | Obligations continuing |
|---------|-----------------|--------|--------------------------|------------------------|
| [Service A] | Art. 31(1) | Applies | Art. 23(d), 29, 30(1), 30(3) | Other Ch VI |
| [Service B] | Art. 31(1) | Does not apply: Limb 2 fails | None | Full Ch VI |
| [Service C] | Art. 31(2) | Applies | All Ch VI | None |
| ... | | | | |

Per-service reasoning.
[Service-by-service walk through the limb-by-limb assessment.]

Routing.
- For [Service A]: see Path 1 conclusion above.
- For [Service B]: see ch6-provider-compliance.md for the full Ch
  VI compliance build-out.
- For [Service C]: monitor transition out of non-production.
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 23 (all paragraphs); Art. 25(1)-(5); Art. 26; Art. 27; Art. 28; Art. 29(1)-(7); Art. 30(1)-(6); Art. 31(1)-(3); Art. 34; Art. 50 (temporal); Recital 86 (functional equivalence IaaS-only); Recital 88 (switching charges); Recital 89 (standard service fees not switching charges; early-termination penalties); Recital 92 (limits of source-provider obligations).
- `sources/faq-v1-4.md` Q52 (Art. 31 specific regime; custom-built services not fully excluded from Ch VI; non-listed provisions continue, including open interfaces and machine-readable export); Q55 (free-tier offering is in Ch VI scope); Q58a (Ch VI applies to IaaS, PaaS, SaaS); Q58b (limits of source-provider duty). Frame as Commission interpretation.
- `sources/digital-omnibus-amendments-tracker.md` for the Art. 31 expansion proposal, SME / small-mid-cap exemption proposal, and early-termination penalty operative clarification.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded conditionally on personal data).
- `references/gates/sectoral-lex-specialis.md` (warn-only; DORA, NIS2 do not depend on the Art. 31 carve-out and continue to apply).
- `references/gates/member-state.md` (warn-only; competent authority for any dispute over carve-out applicability).
- `references/gotchas.md` entries 1 (Art. 2 numbering trap; do not confuse Art. 2(8) data processing service with Art. 8 operative), 9 (Ch II related service vs Ch VI data processing service), 10 (functional equivalence IaaS-only; relevant to which Art. 30 obligation falls away under Art. 31(1)), 13 (Art. 31 carve-out narrow), 20 (Digital Omnibus is a proposal). Mandatory check on every Art. 31 assessment.
- `references/method/analysis-method.md` (the seven-step flow; the illustrative-vs-exhaustive discipline on Art. 31's qualifying limbs).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (Art. 31 expansion proposal).
- `ch6-provider-compliance.md` (full Ch VI compliance where carve-out does not apply).
- `ch6-customer-contract-review.md` (customer-side review where the provider has invoked the carve-out).
- `ch6-switching-execution.md` (live switch where the carve-out is invoked late).
- `ch6-charges.md` (Art. 29 is one of the obligations falling away under Art. 31(1)).

---

## Drafter notes

- **The carve-out is structural; the disclosure is constitutive.** Art. 31(3) is not a formality. A provider that meets the substantive limbs but has not given a clear pre-contract disclosure has not validly invoked Art. 31. Build the disclosure into the contracting workflow as a gating step, not a post-signature compliance fix.
- **Catalogue review is the gatekeeper.** Most failed carve-out claims fail on Limb 2 negative. The catalogue review (what is offered at broad commercial scale via the service catalogue) is the decisive analytical move. A side-by-side of the bespoke service and the closest catalogue offering, with the differences enumerated, is what the assessment turns on.
- **The Digital Omnibus expansion is targeted at the wrong audience for new clients.** The proposal would broaden Art. 31(1) for pre-12-September-2025 contracts only. For new contracts the provider is drafting today, the proposal does not assist. Pre-12-September-2025 contracts are a different conversation, and the proposal should be tracked there, but a provider that is structuring new offerings around the hoped-for expansion is taking on real risk.
