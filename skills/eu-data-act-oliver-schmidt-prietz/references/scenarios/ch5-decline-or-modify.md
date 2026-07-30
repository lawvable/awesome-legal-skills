# ch5-decline-or-modify

**Anchor:** Data holder × Ch V × decline or modify. The data holder's mirror to `ch5-request-preparation.md`. A Ch V request has been received. The clock under Art. 18(2) is running: 5 working days for emergency requests, 30 working days for non-emergency requests. The data holder must decide whether to comply, decline, or seek modification, on closed Art. 18(2) grounds. The card produces the decline-or-modify letter where the grounds hold.

**Routes from:**

- "We received a Ch V request. Help us decline."
- "Is this Art. 14 request lawful? Can we push back?"
- "Draft a modification request under Art. 18(2)."
- "The deadline on this Ch V request is [date]. What do we do?"
- "Our compensation claim under Art. 20."

**Adjacent cards (route there instead if the facts indicate):**

- The request has not yet been issued and the question is whether the public sector body can or should issue it: `ch5-request-preparation.md`.
- The data holder is in a different Member State from the requesting body: `ch5-cross-border-cooperation.md` (the competent authority of the data holder's Member State pre-examines the request under Art. 22(3)-(4); the decline-or-modify clock still runs against the data holder once the request is transmitted).
- The matter is a compensation dispute alone, no contest of the request itself: forthcoming `ch5-compensation.md`; the Art. 20 framework is summarised below in Step 5(c).

---

## Canonical fact pattern

A data holder, a legal person other than a public sector body (Art. 14), has received a request under Ch V. The request purports to be made under Art. 14 with reference to Art. 15. The requesting body is a public sector body of a Member State, the Commission, the European Central Bank, or a Union body. The data holder is now within the Art. 18(2) decline-or-modify window and is assessing the request for lawfulness, scope, and burden.

The data may be personal, non-personal, or mixed. The data holder may be a microenterprise or small enterprise (relevant to Art. 15(2) and Art. 20(1) carve-outs). The data may include trade-secret content (relevant to Art. 19(3) safeguards) and is in any event covered by the data holder's legitimate interests (Art. 17(2)(d)). The Art. 22 cross-border layer may apply if the data holder and the requesting body are in different Member States; the card flags but does not duplicate that analysis.

---

## Critical disciplines

Three failure modes drive most defective decline-or-modify responses. The card cannot be applied without holding all three.

- **The Art. 18(2) grounds are closed.** Art. 18(2) lists three grounds for declining or seeking modification: (a) lack of control over the data; (b) prior similar request, with the data not yet notified as erased under Art. 19(1)(c); (c) the request does not meet Art. 17(1) and (2). The list is exhaustive. The data holder cannot decline on commercial inconvenience, on a generalised competition concern, or on contract terms with the data subject. Where the gravamen is trade-secret protection, the answer is Art. 19(3) safeguards plus full compliance, not refusal: trade-secret status alone does not block a Ch V request.
- **The 5 / 30 working-day clock is constitutive.** Art. 18(2) requires the decline-or-modify response "without undue delay and, in any event, no later than five working days after the receipt of a request for the data necessary to respond to a public emergency and without undue delay and, in any event, no later than 30 working days after the receipt of such a request in other cases". A response outside the window is treated as a failure to decline; the data holder owes the data. The clock starts on receipt, not on internal triage.
- **Decline and modify are different remedies.** Art. 18(2) gives the data holder both options. Modification is the proportionate response where the Art. 17(2)(c) proportionality deficit is curable by narrowing scope, lengthening deadlines, or changing format. Decline is the response where the request has no curable defect (e.g. wrong legal basis under Art. 15(1)). Drafting a decline where a modification would resolve the matter is over-reach; the competent authority can be expected to side with the requesting body on Art. 18(5) referral.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies and the request is genuinely a Ch V request. Run the Art. 1(6) carve-out check: criminal law enforcement, customs, taxation, and national security are out of scope of Ch V by Art. 16(2), and Art. 1(6) excludes several other matters. A request labelled "Ch V" that is in substance a criminal-investigation tool is not a Ch V request; the data holder declines on scope, not on Art. 18(2).

Confirm the requesting body's identity matches Art. 17(1) (public sector body of a Member State, the Commission, the European Central Bank, or a Union body). A request from any other entity is not a Ch V request; the data holder declines on standing.

### Step 2: Chapter identification

Chapter V. The card stays in Ch V. If the requesting body is also a "user" under Art. 2(12) (FAQ Q51 confirms a public sector body can be a Ch II user), the data holder may receive a parallel or alternative Ch II request; that is a separate matter that does not collapse the Art. 18(2) clock on the Ch V request received.

### Step 3: Role mapping

Required entity-by-entity mapping. Show as a table in the output.

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Data holder (responding) | Data holder (Art. 2(13)) | Controller, typically, for personal data in the dataset | Trade-secret holder under Directive (EU) 2016/943 and Art. 2(19) Data Act if applicable; may be a microenterprise or small enterprise (Art. 15(2) carve-out and Art. 20(3) compensation entitlement) |
| Requesting body | Public sector body (Art. 2(28)), the Commission, the European Central Bank, or a Union body | Controller for personal data received | Subject to Art. 19 use limits; subject to Art. 21 onward-sharing limits |
| Data subjects (if personal data in scope) |  | Data subjects | GDPR rights run independently of the Ch V transaction (Art. 18(4) anonymisation/pseudonymisation regime) |
| Competent authority of the data holder's Member State |  |  | Forum for Art. 17(5), Art. 18(5), and Art. 20(5) complaints; pre-examines cross-border requests under Art. 22(3)-(4) |

### Step 4: Fact-category sorting

Card-specific dimensions to sort the request against.

- **Control vs not.** Art. 18(2)(a) lets the data holder decline for lack of control. "Control" tracks Art. 2(13) and Recital 66 (a data holder declines where it "does not have control over the data requested, namely where it does not have immediate access to the data and cannot determine its availability"). Where the data is held by a third party (a sub-contractor, a component supplier, a downstream processor), the data holder identifies the actual controller and declines, ideally pointing the requesting body at the right respondent.
- **Personal vs non-personal.** Drives the Art. 18(4) anonymisation/pseudonymisation obligation. Where personal data is in scope, the data holder anonymises unless compliance requires personal data disclosure, in which case it pseudonymises. The data holder does not defer to the requesting body's assessment of necessity; the anonymisation/pseudonymisation analysis is the data holder's responsibility on disclosure.
- **Trade-secret vs not.** Art. 19(3) requires the data holder (or the trade-secret holder if different) to identify the trade-secret data, including in metadata. The requesting body, prior to disclosure, must take all necessary and appropriate technical and organisational measures to preserve confidentiality. The data holder withholds disclosure of the trade-secret subset until safeguards are in place, but cannot decline the request on trade-secret status alone (the Ch II circular trap does not have an Art. 18 analogue; the answer is safeguards, not refusal).
- **SME status.** If the data holder is a microenterprise or small enterprise per Commission Recommendation 2003/361/EC, Art. 15(2) takes Art. 15(1)(b) requests off the table entirely. Where the request is non-emergency and the data holder is an SME, the data holder declines on Art. 18(2)(c) (Art. 17(1)(b) cannot be satisfied because Art. 15(2) excludes the request).
- **Once-only check.** Art. 18(2)(b) lets the data holder decline where a similar request for the same purpose has been previously submitted by another public sector body or the Commission, the European Central Bank, or a Union body and the data has not been notified as erased under Art. 19(1)(c). Check internal records for prior Ch V requests on the same data and purpose; the public sector body should have done this check before issuing under Recital 67, but the data holder can rely on it independently.

### Step 5: Limb-by-limb application

**Art. 18(2) ground (a): lack of control.** Cumulative limbs:

1. The data holder does not have control over the data requested.
2. Control means immediate access plus power to determine availability (Recital 66).

Where the data is held by another entity within the data holder's group, the data holder may not have control if the holding entity is a separate legal person with its own technical and contractual envelope. The data holder identifies the actual holder in the decline letter.

**Art. 18(2) ground (b): prior request.** Cumulative limbs:

1. A similar request for the same purpose was previously submitted by another public sector body, the Commission, the European Central Bank, or a Union body.
2. The data holder has not been notified of the erasure of the data under Art. 19(1)(c).

"Similar" is functional, not literal: a request for substantially the same dataset for substantially the same statutory task. The data holder must, under Art. 18(3), indicate in the decline the identity of the prior requesting body to enable the new body to obtain the data from the prior recipient if Art. 17(4) inter-body sharing is available.

**Art. 18(2) ground (c): Art. 17(1) and (2) failure.** The single most common ground in practice. Disjunctive within the ground: failure on any one of Art. 17(1)(a)-(j) or Art. 17(2)(a)-(i) is sufficient. Common failure modes:

- Art. 15(1) substantive failure (Art. 17(1)(b) cannot be demonstrated). E.g. no public emergency declared under Art. 2(29); limb (b) attempted against the data holder as an SME (Art. 15(2)); limb (b) attempted for personal data; limb (b) without market-purchase exhaustion and no Art. 15(3) statistical carve-out.
- Art. 17(1)(h) failure: no Union or national law cited that allocates the specific public-interest task to the requesting body.
- Art. 17(1)(e) failure: no justification for the choice of this data holder rather than another.
- Art. 17(2)(c) proportionality failure: granularity, volume, or frequency exceeds what the exceptional need requires. This is often curable by modification rather than decline.
- Art. 17(2)(d) failure: the request does not commit to Art. 19(3) trade-secret safeguards.
- Art. 17(2)(g) or (i) procedural failure: not transmitted to the data coordinator; not notified to the GDPR supervisory authority where personal data is requested.

**Art. 18(2) timing limb.** "Without undue delay and, in any event, no later than five working days" for emergency requests under Art. 15(1)(a); "no later than 30 working days" for non-emergency requests under Art. 15(1)(b). The clock starts on receipt. The "without undue delay" qualifier means the data holder cannot sit on the response until day 4 of 5 or day 29 of 30; promptness is required within the cap.

**Art. 18(4) personal data limb.** Where the request engages personal data and the data holder is preparing to comply (full or modified), the data holder anonymises unless compliance "requires the disclosure of personal data", in which case the data holder pseudonymises. The decline-or-modify letter does not promise more than the data holder will deliver: if personal data cannot be fully anonymised on the facts, the letter states this and proposes pseudonymisation under Art. 18(4).

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. The Art. 18(4) anonymisation/pseudonymisation obligation is the operative Data Act mechanism. The data holder remains the controller for personal data under its existing legal basis until disclosure, and any disclosure to the requesting body is itself a processing operation requiring an Art. 6 GDPR basis (typically Art. 6(1)(c), legal obligation). The Art. 17(2)(i) notification to the GDPR supervisory authority is the requesting body's obligation, not the data holder's; absence of notification is an Art. 17(2) failure the data holder can rely on under Art. 18(2)(c).
- **Trade Secrets Directive overlay (loaded if trade-secret data in scope).** Read `references/gates/trade-secrets-directive.md`. The Ch V regime adapts the TSD: the data holder identifies trade-secret data (Art. 19(3)) and the requesting body implements safeguards prior to disclosure. Disclosure proceeds; refusal is not available on trade-secret status alone. Where the requesting body's request fails to commit to Art. 19(3) safeguards (Art. 17(2)(d) failure), the data holder may decline under Art. 18(2)(c) until the commitment is added.
- **Sectoral lex specialis (warn-only).** Read `references/gates/sectoral-lex-specialis.md` if the data holder operates in a regulated sector (vehicles, medical devices, financial services, energy, AI systems, eIDAS, NIS2, CRA). Sectoral confidentiality, security, or restriction obligations may overlay the Ch V response (e.g. NIS2 incident-reporting confidentiality; MDR adverse-event confidentiality). The Data Act does not override these.
- **Member State gate (always loaded).** Read `references/gates/member-state.md`. The data holder's Member State competent authority under Art. 37 is the forum for an Art. 18(5) referral if the requesting body challenges the decline. The same competent authority handles complaints under Art. 17(5) (data holder challenging an unlawful Art. 17(4) onward transmission) and Art. 20(5) (disagreement on compensation level).
- **Cross-border overlay (loaded if the requesting body is in another Member State).** Hand off to `ch5-cross-border-cooperation.md`. The competent authority of the data holder's Member State pre-examines the request under Art. 22(3)-(4) and may reject it on duly substantiated grounds before transmission to the data holder. Once the request is transmitted, the data holder's Art. 18(2) clock runs as normal.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Articles 14-22 of Regulation (EU) 2023/2854 (Data Act) govern. Art. 18(2) decline-or-modify on closed grounds; Art. 18(4) anonymisation/pseudonymisation; Art. 19(3) trade-secret regime; Art. 20 compensation; Art. 21 onward sharing. Verbatim text at `sources/regulation-2023-2854.md` Arts. 14-22; operative recitals at Recitals 63-72.
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final (19 November 2025) would narrow the conditions under which public authorities can demand data from businesses in non-emergency situations under Art. 15(1)(b). Status: co-legislator negotiation, not adopted. See `sources/digital-omnibus-amendments-tracker.md` Chapter V entry.

The output cites current law as operative. Where a decline turns on a borderline Art. 15(1)(b) condition that the proposal would narrow, the decline letter may note the proposal as additional context without relying on it as law.

---

## Decision point

After Steps 5 and 6, the analysis yields one of five paths.

1. **No Art. 18(2) ground holds; request lawful and proportionate.** Comply within the deadline stated in Art. 17(1)(i). The card does not produce a compliance response; it produces an internal note confirming the analysis and a compensation-claim letter under Art. 20 if applicable (Output Path 3 below).
2. **Art. 18(2)(a) lack of control.** Produce the decline letter (Output Path 1 below), identifying the actual data controller and pointing the requesting body at it.
3. **Art. 18(2)(b) prior request.** Produce the decline letter (Output Path 1 below), identifying the prior requesting body under Art. 18(3).
4. **Art. 18(2)(c) Art. 17 failure, not curable by modification.** Produce the decline letter (Output Path 1 below), identifying the specific Art. 17 limbs that fail.
5. **Art. 18(2)(c) Art. 17 failure, curable by modification.** Produce the modification request (Output Path 2 below), proposing concrete amendments to the request that would resolve the deficit.

The card does not refuse to draft on Path 1 facts: a Ch V decline is not the Ch II circular trap. The Art. 18(2) grounds are open to the data holder where they apply on the facts. Decline is the prescribed remedy.

---

## Output skeleton: Path 1 (decline letter, Art. 18(2)(a), (b), or (c))

Formal letter, Markdown by default, ready for adoption with minimal edit. Length: typically 1 to 2 pages.

Structure:

```
[Data holder letterhead placeholder]

To: [Requesting body, full legal entity name and address]
Date: [Date of decline, within the Art. 18(2) clock: no later than 5
       working days after receipt for an Art. 15(1)(a) emergency
       request; no later than 30 working days after receipt for an
       Art. 15(1)(b) non-emergency request; without undue delay in
       either case]
Reference: [Decline reference; quote the requesting body's reference
            from the original request]
Subject: Decline of data request dated [request date] under
         Article 18(2) of Regulation (EU) 2023/2854 (Data Act)

1. The request
   [Identification of the request: date received, requesting body,
   purpose stated, Art. 15(1)(a) or (b) limb invoked, deadline
   stated under Art. 17(1)(i), data coordinator publication
   reference if any.]

2. Ground for decline
   [State the specific Art. 18(2) ground:
   (a) the data holder does not have control over the data
       requested; OR
   (b) a similar request for the same purpose has been previously
       submitted by [identify prior requesting body per
       Art. 18(3)], and the data has not been notified as erased
       under Art. 19(1)(c); OR
   (c) the request does not meet the conditions of Art. 17(1)
       and/or (2), specifically [name each failed limb].]

3. Substantiation
   3(a) For Art. 18(2)(a) declines:
        - Why the data holder does not have immediate access to
          the data and cannot determine its availability (Recital
          66).
        - Identification of the actual data controller, with
          contact information where appropriate.
   3(b) For Art. 18(2)(b) declines:
        - Identity of the prior requesting body and date of the
          prior request (Art. 18(3)).
        - Confirmation that no Art. 19(1)(c) erasure notification
          has been received.
   3(c) For Art. 18(2)(c) declines, one of:
        - Art. 17(1)(b) failure: e.g. no public emergency declared
          under Art. 2(29) (Art. 15(1)(a) limb cannot be met); or
          the request is Art. 15(1)(b) but the data holder is a
          microenterprise/small enterprise (Art. 15(2)); or limb
          (b) but personal data sought; or limb (b) without market-
          purchase exhaustion outside the Art. 15(3) statistical
          carve-out.
        - Art. 17(1)(h) failure: no Union or national law cited
          that allocates the specific task to the requesting body.
        - Art. 17(2)(c) proportionality failure not curable by
          modification on these facts.
        - Art. 17(2)(d) failure: no Art. 19(3) trade-secret
          safeguard commitment.
        - Art. 17(2)(g) or (i) procedural failure: not transmitted
          to the data coordinator; not notified to the GDPR
          supervisory authority.

4. Implications for the requesting body
   [Statement that the data holder has not made the requested data
   available pursuant to this Art. 18(2) decline. Reminder that
   under Art. 18(5), if the requesting body wishes to challenge the
   decline, the matter shall be referred to the competent authority
   designated under Art. 37 of the Member State where the data
   holder is established. Identify that competent authority.]

5. Communication channel
   [Statement that the data holder remains available to discuss
   modifications that could resolve the deficiency, where the
   ground for decline is Art. 18(2)(c) on facts that may be
   curable. This is not an offer to compromise on Art. 15(1)
   substance; it is an invitation to redraft the procedural
   envelope.]

[Signature block placeholder]
```

---

## Output skeleton: Path 2 (modification request)

Formal letter, Markdown by default. Used where Art. 18(2)(c) is engaged on a curable defect and proportionality, format, or scope changes would resolve the matter. Length: typically 1 to 1.5 pages.

Structure:

```
[Data holder letterhead placeholder]

To: [Requesting body, full legal entity name and address]
Date: [Date of modification request, within the Art. 18(2) clock]
Reference: [Modification reference; quote the requesting body's
            reference]
Subject: Request for modification of data request dated [request
         date] under Article 18(2) of Regulation (EU) 2023/2854
         (Data Act)

1. The request
   [Identification of the request as in Path 1, section 1.]

2. Deficit identified
   [Specific Art. 17(1) or (2) limb that the data holder cannot
   accept as drafted. Most commonly Art. 17(2)(c) proportionality:
   the granularity, volume, or frequency exceeds what the
   exceptional need requires.]

3. Modifications proposed
   3(a) Scope. [Concrete narrowing of the data set requested.
        Identify the subset of fields, the time window, or the
        granularity the data holder can make available consistent
        with Art. 17(2)(c).]
   3(b) Format. [Where the requested format is technically
        unfeasible or disproportionate, propose an alternative
        format consistent with the data the data holder has
        control over.]
   3(c) Schedule. [Where the deadline under Art. 17(1)(i) is
        operationally infeasible, propose a revised deadline that
        respects "without undue delay" under Art. 18(1) and the
        proportionality requirement of Art. 17(2)(c).]
   3(d) Personal data. [Where the request engages personal data,
        confirmation that the data holder will anonymise pursuant
        to Art. 18(4) unless full anonymisation is not feasible,
        in which case pseudonymisation; identification of the
        proposed pseudonymisation method.]
   3(e) Trade-secret safeguards. [Where the request omits an
        Art. 19(3) safeguard commitment, propose the safeguards
        (model contractual terms, technical standards, codes of
        conduct) the data holder requires prior to disclosure.]

4. Compensation
   [Reference Path 3 compensation framework as applicable.]

5. Effect of acceptance
   [Statement that on acceptance of the modifications, the data
   holder will comply with the modified request within the revised
   deadline. Statement that, if no agreement is reached, the data
   holder is entitled to decline under Art. 18(2)(c) and the matter
   may be referred to the competent authority under Art. 18(5).]

[Signature block placeholder]
```

---

## Output skeleton: Path 3 (compensation claim under Art. 20)

Used in parallel with compliance, modification, or in a separate communication after compliance. Markdown. Short. The Art. 20 framework:

- Art. 20(1): Emergency requests under Art. 15(1)(a) are free of charge for data holders other than microenterprises and small enterprises. The data holder may request public acknowledgement.
- Art. 20(2): Non-emergency requests under Art. 15(1)(b) entitle the data holder to fair compensation covering technical and organisational costs (including anonymisation, pseudonymisation, aggregation, and technical adaptation) plus a reasonable margin. The data holder, on request, provides the basis for the calculation.
- Art. 20(3): Microenterprises and small enterprises may claim Art. 20(2) compensation even for Art. 15(1)(a) emergency requests.
- Art. 20(4): No compensation where the task is the production of official statistics and national law does not allow purchase of data; Member States notify the Commission of such national-law provisions.
- Art. 20(5): Disagreements on the level of compensation may be referred to the competent authority of the data holder's Member State.

Structure:

```
[Data holder letterhead placeholder]

To: [Requesting body]
Date: [Date]
Reference: [Compensation claim reference; quote the request
            reference]
Subject: Claim for compensation under Article 20 of Regulation (EU)
         2023/2854 (Data Act)

1. Basis
   [Statement of the data holder's status (microenterprise/small
   enterprise or not) and the applicable Art. 20 paragraph: (1) for
   public acknowledgement on emergency requests; (3) for SME
   compensation on emergency requests; (2) for non-emergency
   compensation.]

2. Costs incurred
   [Itemised technical and organisational costs: data extraction;
   anonymisation; pseudonymisation; aggregation; technical
   adaptation; format conversion; transmission. Each line with the
   quantum and the basis.]

3. Reasonable margin
   [Applicable to Art. 20(2) and (3) claims. The Commission has not
   yet adopted guidelines on calculating reasonable compensation
   (Art. 9(5) applies by analogy; FAQ Q72 states guidelines are
   expected Q2/Q3 2026). The data holder proposes a margin
   consistent with general principles of fairness, reasonableness,
   and non-discrimination from Art. 8.]

4. Acknowledgement (Art. 15(1)(a) emergency requests only)
   [Where the data holder is not an SME and Art. 20(1) applies, the
   data holder may request public acknowledgement in lieu of
   monetary compensation. State the requested form (press release,
   dataset citation, report acknowledgement).]

5. Dispute resolution
   [Statement that, in case of disagreement on the level of
   compensation, the data holder will refer the matter to the
   competent authority of [Member State of establishment]
   designated under Art. 37, pursuant to Art. 20(5).]

[Signature block placeholder]
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 14, Art. 15(1)-(3), Art. 16(1)-(2), Art. 17(1)-(2), Art. 18(1)-(5), Art. 19(1)-(4), Art. 20(1)-(5), Art. 21(1)-(5); Art. 2(13) (data holder), Art. 2(28) (public sector body), Art. 2(29) (public emergency).
- `sources/regulation-2023-2854.md` Recital 63 (exceptional need; SME burden limit); Recital 64 (emergency illustrative list; declaration requirement); Recital 65 (limb (b) examples and exhaustion); Recital 66 (decline grounds; sui generis database right shall not block Ch V access); Recital 67 (once-only principle; competent authority lawfulness assessment); Recital 68 (anonymisation/pseudonymisation regime); Recital 69 (purpose limitation; erasure); Recital 71 (compensation framework, including SME entitlement and statistical carve-out); Recital 72 (research onward-sharing under Art. 21).
- `sources/faq-v1-4.md` Q46 (data holder's verification checklist); Q47 (cross-border permissibility); Q48 (data is not open data); Q49 (once-only refusal); Q50 (fundamental-rights safeguards). Frame each as Commission interpretation.
- `sources/digital-omnibus-amendments-tracker.md` Chapter V entry on proposed narrowing of non-emergency circumstances.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded conditionally on personal data in scope; Art. 18(4) regime).
- `references/gates/trade-secrets-directive.md` (loaded conditionally on trade-secret data; Art. 19(3) adapts the TSD to Ch V; decline on trade-secret status alone is not available).
- `references/gates/sectoral-lex-specialis.md` (warn-only; sectoral confidentiality and security overlays).
- `references/gates/member-state.md` (always loaded; identifies the Art. 18(5), Art. 17(5), and Art. 20(5) competent authority).
- `references/gotchas.md` entry 4 ("without undue delay" has no numeric SLA; note the Art. 18(2) 5/30 working-day cap is an exception); entry 14 (sui generis database right does not apply to Data Act in-scope data, by Art. 43; Recital 66 confirms this for Ch V); entry 15 (Ch V compensation direction: public sector body pays data holder, opposite of Ch III where this is the same direction; the SME-emergency entitlement is the key carve-out); entry 16 (reasonable compensation guidelines forthcoming, not published; FAQ Q72); entry 19 (FAQ is non-authoritative); entry 20 (Digital Omnibus is a proposal).
- `references/method/analysis-method.md` (the seven-step flow; this card is one instance).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (Chapter V entry).
- `references/scenarios/ch5-request-preparation.md` (the requesting body's mirror; cited so the data holder sees what should have been done upstream).
- `references/scenarios/ch5-cross-border-cooperation.md` (Art. 22 layer if the requesting body is in another Member State; the competent authority of the data holder's Member State pre-examines).

---

## Drafter notes

Operational observations for using this card. Three only.

- **The clock is the most operationally important detail.** Art. 18(2) sets 5 working days for emergency requests and 30 working days for non-emergency requests. The clock starts on receipt, not on internal routing. Build the response workflow so the legal review, the technical assessment of control, and the trade-secret identification all complete within the cap. A response on day 6 of 5 is a missed decline; the data holder owes the data.
- **Modification beats decline where the defect is curable.** Art. 18(5) routes disputes to the competent authority of the data holder's Member State. The competent authority will assess whether the data holder declined in good faith or stretched a curable defect into a decline. A modification request that the requesting body refuses to accept is a stronger posture before the competent authority than a decline that overstates the defect.
- **Compensation is a separate matter from the decline.** A data holder may comply with the request and claim compensation under Art. 20 (Path 3) without invoking Art. 18(2). The two letters are different instruments; do not mix them. Where the compensation claim is the data holder's only objection, the request is honoured and the Art. 20(5) referral is the right forum if the level is disputed.
