# ch6-provider-compliance

**Anchor:** Provider × Ch VI × full-stack compliance check. The provider of a data processing service is assessing whether its contracts, commercial practices, and technical capabilities comply with Articles 23 through 30 of the Data Act. The deliverable is a compliance check that names the gaps and the remediation steps. The mirror of `ch6-customer-contract-review.md` from the opposite side of the contract.

**Routes from:**

- "Are our cloud contracts Data Act compliant?"
- "What does Ch VI require us to put in our customer contracts?"
- "We are an IaaS / PaaS / SaaS provider; what are our switching obligations?"
- "Draft an Art. 25 compliance checklist for our service."
- "Walk us through the provider-side obligations under Ch VI."

**Adjacent cards (route there instead if the facts indicate):**

- Customer reviewing a provider's contract: `ch6-customer-contract-review.md`.
- Switching event already in progress: `ch6-switching-execution.md`.
- Switching-charge regime, Art. 29 phased reduction, 12 January 2027 abolition: `ch6-charges.md`.
- Whether the service falls outside Ch VI under Art. 31 custom-built carve-out: `ch6-custom-built-carve-out.md`.
- Art. 28 international-access transparency only, with Ch VII (Art. 32) focus: not yet drafted; the Art. 28 component is treated here.

---

## Canonical fact pattern

The provider operates one or more data processing services within the meaning of Art. 2(8). Per FAQ Q58a the Commission considers the definition covers IaaS, PaaS, and SaaS where the service displays the characteristics listed in the definition (on-demand access to a shared pool of configurable, scalable, elastic computing resources, rapidly provisioned with minimal service-provider interaction). The provider is in scope of Ch VI in full, unless an Art. 31 carve-out applies (which is the exception, gotcha 13).

The provider's contract base includes both pre-12-September-2025 legacy contracts and post-12-September-2025 new contracts. The provider has obligations in all directions: contract drafting (Art. 25), transparency disclosures (Art. 26, Art. 28), good-faith cooperation when switching happens (Art. 27), phased charge reduction (Art. 29), and technical aspects of switching (Art. 30). The provider may also be itself a customer of an upstream data processing service (Recital 91), in which case it benefits from the same regime in that direction.

---

## Critical disciplines

- **The IaaS-only point cuts both ways.** Functional equivalence under Art. 30(1) is an obligation only for providers offering IaaS within the Art. 30(1) definition: "scalable and elastic computing resources limited to infrastructural elements such as servers, networks and the virtual resources necessary for operating the infrastructure, but that do not provide access to the operating services, software and applications". PaaS and SaaS providers owe Art. 30(2) (open interfaces), Art. 30(3) (common-specification compatibility), and Art. 30(5) (exportable data in a structured, commonly used, machine-readable format) instead (gotcha 10, Recital 86, FAQ Q58a, FAQ Q58b). A SaaS provider that takes on functional-equivalence drafting voluntarily is going beyond statutory obligations and should know it; a SaaS provider that demands functional equivalence of its IaaS sub-provider is making a contractual claim, not a Data Act claim.
- **Art. 23 is the obstacle-removal mandate.** Beyond the specific Art. 25(2) clauses, Art. 23 prohibits pre-commercial, commercial, technical, contractual, and organisational obstacles to (a) termination after notice and switching, (b) concluding contracts with a different provider, (c) porting exportable data and digital assets (including after a free-tier offering, per FAQ Q55), (d) achieving functional equivalence under Art. 24 (for IaaS), and (e) unbundling Art. 30(1) services from other services where technically feasible. Compliance is more than mandatory-clause compliance; it is also the absence of obstacles erected elsewhere in the commercial relationship.
- **Art. 27 good faith is open-textured but enforceable.** "All parties involved, including destination providers of data processing services, shall cooperate in good faith to make the switching process effective." Bad-faith conduct during a live switch (delay, obstruction, last-minute charges, sandbagged interfaces) creates exposure even where the contract clauses themselves are compliant on their face.
- **Art. 26(b) online register is a perpetual obligation.** The provider must publish an up-to-date register of data structures, data formats, standards, and open interoperability specifications for the exportable data referred to in Art. 25(2)(e). For non-IaaS providers, Art. 30(4) requires that the register be kept current consistently with Art. 30(3) compatibility duties. A provider that points at static documentation last updated two years ago is non-compliant.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check and Art. 1(6) carve-outs. Confirm each of the provider's services is a "data processing service" within Art. 2(8). The Commission interpretation in FAQ Q58a covers IaaS, PaaS, and SaaS where the four characteristics are present (access to computing resources; on-demand network access; rapid provisioning with minimal service-provider interaction; elasticity). Free-tier offerings are within scope (FAQ Q55).

Temporal scope: Ch VI applies from 12 September 2025 (Art. 50). Pre-existing contracts that continue past that date are within scope for forward-looking compliance; the provider cannot leave old contracts as they were. Charge reduction under Art. 29(2) has applied since 11 January 2024, abolition from 12 January 2027.

### Step 2: Chapter identification

Chapter VI throughout. Art. 28 connects to Ch VII (Art. 32) on third-country governmental access; the Art. 28 disclosure is the customer-facing transparency artefact, the Art. 32 regime is the substantive set of measures behind it. Ch VIII (Art. 33) applies if the provider is also a participant in a data space.

### Step 3: Role mapping

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Provider | Provider of data processing services |  | Source provider in switching scenarios |
| Provider's customers | Customers (Art. 2(30)) | Controllers, typically | If a customer is itself a downstream provider, also a provider of data processing services |
| Provider's upstream providers (if any) | Providers of data processing services |  | The provider is itself the customer in that relationship (Recital 91) |
| Destination providers (in any switching event) | Providers of data processing services |  | Bound by Art. 27 good-faith obligation |
| End users of customer's services |  | Data subjects, typically | Generally not in scope of Ch VI as such |

Recital 91 confirms the bidirectional point: a provider that is itself a customer benefits from the regime upward and is bound by it downward.

### Step 4: Fact-category sorting

Card-specific dimensions to sort the provider's service portfolio against.

- **Service-type classification per service.** IaaS within Art. 30(1) ("limited to infrastructural elements... not access to the operating services, software and applications"), PaaS, or SaaS. The classification governs the Art. 30 obligations. Per Recital 86 and FAQ Q58b the IaaS-only functional-equivalence point is settled. Mixed offerings (IaaS with PaaS / SaaS layers in the same product) require per-layer analysis.
- **Contracts concluded before vs after 12 September 2025.** Existing contracts must be amended. New contracts must be Art. 25-compliant from day one. The Art. 31 carve-out for legacy custom-built contracts is currently narrow but may be broadened by the Digital Omnibus (gotcha 13, gotcha 20).
- **Free-tier vs paid.** Free-tier offerings (per FAQ Q55) are within Ch VI; the customer that has used a free tier can still benefit from switching rights, including porting of exportable data and digital assets.
- **Production vs non-production / test / beta.** Art. 31(2) removes non-production test or evaluation services for a limited period from Ch VI scope entirely. The provider's catalogue should identify which services qualify.
- **Standalone vs in-parallel use.** Art. 34 modifies the regime where customers are using services in parallel; egress charges are still permitted for the in-parallel use, but only at cost and only for the purpose of passing on egress costs incurred (Art. 34(2)).
- **Data processed.** Personal data triggers the GDPR overlay separately; that does not directly affect Ch VI obligations, but it does affect what the customer can demand at retrieval and erasure.

### Step 5: Limb-by-limb compliance check

The check walks the provider's full Ch VI obligation surface. Each item is independent; each gap is a separate remediation step.

**Art. 23. Obstacle removal.** Audit the contract base and commercial practice for pre-commercial, commercial, technical, contractual, and organisational obstacles to (a)-(e) above. Common defects: volume discounts that claw back on switching; perpetual minimum commitments that prevent termination after the maximum notice period; long-tail commercial penalties that make Art. 25(2)(d) notice nominal; technical bundling that prevents unbundling under Art. 23(e).

**Art. 25(1). Written contract available pre-signature.** The switching contract must be in writing and made available pre-signature in a form the customer can store and reproduce. Common defects: switching terms incorporated only by reference into general terms hosted on the provider's website with no pre-signature delivery.

**Art. 25(2)(a)-(i). The mandatory clauses.** Each clause must be present in the contract at no less than the statutory minimum:

- (a) Switching with a maximum 30-day mandatory transitional period after the notice period, with the four operational duties during transition (assistance, business continuity, risk information, security).
- (b) Exit-strategy support including all relevant information.
- (c) Termination on completion of switching or at end of notice period if the customer wishes only to erase.
- (d) Maximum notice period of two months.
- (e) Exhaustive specification of categories of data and digital assets that can be ported, including all exportable data at a minimum.
- (f) Exhaustive specification of any categories exempted for trade-secret breach risk, where the exemption does not impede or delay switching.
- (g) Minimum data retrieval period of 30 calendar days after the transitional period ends.
- (h) Full erasure of customer-generated exportable data and digital assets after retrieval expiry on successful switching.
- (i) Switching charges in accordance with Art. 29 (route to `ch6-charges.md`).

**Art. 25(3). Customer's election at end of notice period.** The customer's choice on termination of the notice period (switch to a different provider with the provider's details; switch to on-premises; or erase) must be drafted as a clause in the contract, not as a separately negotiated option.

**Art. 25(4). Technical-unfeasibility extension.** Process: provider notifies the customer within 14 working days of the switching request, justifies the technical unfeasibility, and proposes an alternative transitional period not exceeding seven months. Per Recital 87 the burden of proof falls fully on the provider. Service continuity must be maintained throughout. The provider should have internal escalation, justification, and notification workflows in place; ad-hoc justification at the switching point will fail.

**Art. 25(5). Customer's right to extend once.** The contract must include the customer's right to extend the transitional period once for a period the customer considers appropriate. This is the customer's right, not the provider's discretion. Per Recital 87 the customer may exercise the extension before or during the transitional period.

**Art. 26. Information obligations.** The provider must give the customer (a) information on available procedures for switching and porting, including methods, formats, restrictions, and known technical limitations; and (b) a reference to an up-to-date online register hosted by the provider, with details of all data structures, data formats, relevant standards, and open interoperability specifications in which the exportable data are available. Common defects: the register exists but is stale; the register references "documentation available on request" rather than being substantively populated; the customer-facing procedure description is buried in a developer portal the customer does not know exists.

**Art. 27. Good-faith cooperation.** During a live switch the provider, the customer, and the destination provider must cooperate in good faith to make the process effective. Compliance posture is conduct-based, not document-based. Operational training of customer-success and engineering teams matters as much as the contract drafting.

**Art. 28. International-access transparency.** The provider must publish on its website, and reference in its contracts, (a) the jurisdiction(s) to which its ICT infrastructure is subject and (b) a general description of the technical, organisational, and contractual measures adopted to prevent international governmental access in conflict with EU or Member State law. Common defects: jurisdictional disclosure incomplete (parent-company jurisdiction often omitted); measures disclosure vague ("we comply with applicable law"); website link not referenced in the contract. Art. 28 connects to the Ch VII (Art. 32) regime on substantive measures; the disclosure is the customer-facing artefact.

**Art. 29. Charges.** Charges have been "reduced" since 11 January 2024 (limited to costs incurred by the provider directly linked to the switching process per Art. 29(3)) and must be eliminated from 12 January 2027 onwards. The provider must, before signing, give the prospective customer clear information on standard service fees, any early-termination penalties, and any reduced switching charges. The full analysis is on `ch6-charges.md`.

**Art. 30(1). Functional equivalence (IaaS only).** For providers within Art. 30(1) IaaS scope, the obligation is to take all reasonable measures in their power to facilitate functional equivalence at the destination provider after switching. The duty per Recital 92 is limited to the source provider's own service environment; the provider does not have to rebuild the service inside the destination provider's infrastructure. Capabilities, information, documentation, and technical support are the deliverables.

**Art. 30(2) and (3). Open interfaces and common specifications (non-IaaS).** Providers other than within Art. 30(1) IaaS scope must (i) make open interfaces available to all customers and concerned destination providers free of charge, with sufficient information to enable the development of communicating software for portability and interoperability; and (ii) ensure compatibility with common specifications or harmonised standards for interoperability of data processing services published in the central Union standards repository, within 12 months of publication.

**Art. 30(4). Register currency.** Non-IaaS providers must keep the Art. 26(b) register current consistently with their Art. 30(3) compatibility duties.

**Art. 30(5). Exportable data in standard format.** Where common specifications or harmonised standards for interoperability have not been published in the central Union standards repository, the provider must, at the customer's request, export all exportable data in a structured, commonly used, machine-readable format. This applies to all providers within Art. 30(2)-(5) scope (non-IaaS).

**Art. 30(6). Intellectual property and trade secret limits.** The provider is not required to develop new technologies or services, or disclose or transfer assets protected by IP rights or trade secrets, or compromise security and integrity of service. The negative limit; relevant for what stays out of exportable data per Recital 82 and what the Art. 25(2)(f) exemption catalogue can cover.

**Art. 34. In-parallel use.** Where customers use the service in parallel with another data processing service, the requirements of Art. 23, Art. 24, Art. 25(2)(a)(ii), (a)(iv), (e), (f), and Art. 30(2)-(5) apply mutatis mutandis. Art. 34(2) permits ongoing data egress charges for in-parallel use at cost.

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data flows).** Load `references/gates/gdpr-overlay.md`. The provider's data processing agreement under GDPR Art. 28 (where the provider is processor) must reconcile with the Art. 25(2)(g) retrieval window and Art. 25(2)(h) erasure obligation. The Ch VI regime does not override GDPR but operates alongside it.
- **Trade Secrets Directive overlay (warn).** Load `references/gates/trade-secrets-directive.md` where the provider relies on Art. 25(2)(f) or Art. 30(6) trade-secret protection. The carve-out must not impede or delay switching.
- **Sectoral lex specialis (warn-only).** DORA (Regulation (EU) 2022/2554) imposes parallel exit and contractual obligations on ICT third parties of financial entities; the Data Act's Art. 25 contract terms must coexist with the DORA Annex obligations. NIS2 (Directive (EU) 2022/2555) imposes parallel supply-chain risk obligations. Load `references/gates/sectoral-lex-specialis.md`.
- **Member State implementing law (warn-only).** Competent authority designation under Art. 37, complaint procedures under Art. 38, and penalty determination under Art. 40 differ by Member State. Load `references/gates/member-state.md`.
- **Art. 41 MCTs / SCCs.** The Commission has published non-binding Standard Contractual Clauses for cloud computing contracts under Art. 41. Adoption is voluntary and is not a safe harbour, but the SCCs are useful as a benchmark for the provider's drafting. See `sources/mcts-sccs-recommendation-pointer.md`. Direct the user to the Commission landing page.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Articles 23 through 31 of Regulation (EU) 2023/2854 (Data Act) govern. Operative articles: Art. 23 obstacles; Art. 25(1)-(5) mandatory contract terms; Art. 26 information; Art. 27 good faith; Art. 28 international-access transparency; Art. 29 charges; Art. 30(1)-(6) technical aspects; Art. 31 carve-outs; Art. 34 in-parallel use. Operative recitals: Recital 82 (exportable data scope); Recital 83 (digital assets); Recital 86 (functional equivalence IaaS-only); Recital 87 (technical-unfeasibility extension burden of proof); Recital 88 (switching charges definition); Recital 89 (standard service fees and outsourcing costs); Recital 91 (the provider that is also a customer); Recital 92 (limits of source-provider obligations).
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final (19 November 2025) proposes (a) expansion of the Art. 31 custom-built carve-out for contracts concluded on or before 12 September 2025; (b) SME / small-mid-cap exemption from non-IaaS obligations for pre-12-September-2025 contracts; (c) operative clarification of early-termination penalties in fixed-term contracts. Status: co-legislator negotiation, not adopted. See `sources/digital-omnibus-amendments-tracker.md`.

The output cites current law as operative. SME and small-mid-cap providers should track the proposal closely; the bulk of providers should not assume the carve-out will broaden.

---

## Decision point

After Steps 5 and 6 the compliance check yields one of three paths.

1. **Materially compliant, isolated gaps.** Remediation plan with specific clause amendments and operational fixes. Output Path 1 below.
2. **Materially non-compliant, multi-axis exposure.** A full compliance build-out is needed; the provider has gaps in contract drafting, transparency disclosures, technical capability, and operational readiness. Output Path 2 below.
3. **Provider believes Art. 31 carve-out applies.** Route to `ch6-custom-built-carve-out.md` before completing this check.

---

## Output skeleton: Path 1 (isolated gaps, remediation plan)

Memo, Markdown by default. Length: two to four pages.

```
Subject: Ch VI compliance check, [provider service / portfolio]

Conclusion. The portfolio is materially compliant with Articles 23
to 30 of Regulation (EU) 2023/2854 with [N] discrete gaps. The
remediation plan below addresses each.

Service classification.
| Service | Classification | Art. 30 obligations |
|---------|----------------|---------------------|
| [Service A] | IaaS | 30(1) functional equivalence |
| [Service B] | PaaS | 30(2), 30(3), 30(5) |
| [Service C] | SaaS | 30(2), 30(3), 30(5) |

Compliance summary.
| Article | Service A | Service B | Service C | Comment |
|---------|-----------|-----------|-----------|---------|
| 23 | OK | OK | OK |  |
| 25(1) | OK | OK | OK |  |
| 25(2)(a) | OK | Gap | OK | Transitional period defaulted to 60 days |
| ... | | | | |

Remediation plan.
1. [Gap and action, with owner and target date.]
2. [...]

Open items.
- [Service classification confirmation where mixed.]
- [Register-population programme.]
```

---

## Output skeleton: Path 2 (multi-axis compliance build-out)

Build-out roadmap. Markdown. Length: four to eight pages.

```
Subject: Ch VI compliance build-out, [provider portfolio]

Conclusion. The current portfolio is not materially compliant with
Chapter VI of Regulation (EU) 2023/2854. A multi-axis build-out is
required across (a) contract drafting, (b) transparency disclosures,
(c) technical capability, and (d) operational readiness. The
sequence below sets out the build-out by axis, with prerequisites
flagged.

Axis 1. Contract drafting (Art. 25).
[Per-clause gap analysis and proposed drafting. Cross-reference to
the customer-facing review on ch6-customer-contract-review.md.]

Axis 2. Transparency disclosures (Art. 26, Art. 28, Art. 29(4)).
[Online register population. International-access transparency
page. Pre-signature charge disclosure procedure.]

Axis 3. Technical capability (Art. 30).
[Open interfaces. Common-specification monitoring. Exportable-data
standard format. For IaaS, functional-equivalence capability set.]

Axis 4. Operational readiness (Art. 25(2)(a) operational duties,
Art. 25(4) extension workflow, Art. 27 good faith).
[Customer success training. Engineering-side switching playbook.
Internal escalation and justification template for the 14-working-day
technical-unfeasibility notification.]

Sequencing.
1. [Phase 1 with prerequisites.]
2. [Phase 2.]
3. [Phase 3.]

Standalone deliverables.
- Art. 25 contract amendment package.
- Art. 26 register population brief.
- Art. 28 international-access transparency page.
- Art. 25(4) technical-unfeasibility notification template.
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 23 (always); Art. 24; Art. 25(1)-(5); Art. 26; Art. 27; Art. 28; Art. 29 (cross-reference to `ch6-charges.md`); Art. 30(1)-(6); Art. 31 (cross-reference to `ch6-custom-built-carve-out.md`); Art. 34 (where in-parallel use); Art. 50 (temporal scope).
- `sources/regulation-2023-2854.md` Recital 82; Recital 83; Recital 84; Recital 85; Recital 86; Recital 87; Recital 88; Recital 89; Recital 91; Recital 92.
- `sources/faq-v1-4.md` Q52 (Art. 31 specific regime); Q53 (exportable data and digital assets); Q55 (free-tier offering); Q56 (notice and transition periods); Q58a (Ch VI applies across IaaS, PaaS, SaaS, with the Art. 30(1) asymmetry); Q58b (limits of source-provider duty). Frame as Commission interpretation.
- `sources/mcts-sccs-recommendation-pointer.md` for the Art. 41 SCCs as benchmark.
- `sources/digital-omnibus-amendments-tracker.md` for Art. 25, Art. 29, Art. 31 entries.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded conditionally on personal data flows).
- `references/gates/trade-secrets-directive.md` (loaded where Art. 25(2)(f) or Art. 30(6) trade-secret protection is in issue).
- `references/gates/sectoral-lex-specialis.md` (warn-only; DORA, NIS2, sectoral cloud rules).
- `references/gates/member-state.md` (warn-only; competent authority, complaints, penalties).
- `references/gotchas.md` entries 9 (Ch II related service vs Ch VI data processing service), 10 (functional equivalence IaaS-only), 13 (Art. 31 carve-out narrow), 20 (Digital Omnibus is a proposal). Mandatory check.
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (Ch VI entries).
- `ch6-customer-contract-review.md` (customer-side mirror).
- `ch6-switching-execution.md` (mechanics during transition).
- `ch6-charges.md` (Art. 29 deep dive).
- `ch6-custom-built-carve-out.md` (Art. 31 test).

---

## Drafter notes

- **Compliance is portfolio-wide.** A provider with five services on its catalogue cannot run Art. 25 compliance one service at a time; the obligations apply across the portfolio. The compliance plan should treat the portfolio as a whole and identify per-service variations only where the service type or carve-out status differs.
- **The 14-working-day notification template is operationally load-bearing.** Art. 25(4) only works if the provider can produce a justified technical-unfeasibility notification inside 14 working days of a switching request. The template, the escalation, and the engineering-side input flow should be in place before any switching request lands. Reactive drafting in week one of a switch will not meet the deadline.
- **The Art. 28 page and the Ch VII (Art. 32) substance are different artefacts.** Art. 28 requires a customer-facing transparency disclosure on the website. Art. 32 is the substantive set of measures behind it. A provider that has the page but no measures is exposed; a provider that has the measures but no page is also exposed. Both are needed.
