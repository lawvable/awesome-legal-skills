# ch5-request-preparation

**Anchor:** Public sector body × Ch V × request preparation. The drafting stage where the lawfulness of any later Ch V access turns. A request that fails Art. 17(1) or (2) on its face will be declined under Art. 18(2)(c) within 5 or 30 working days, and the public sector body will have wasted the window. The card refuses to draft a Ch V request that does not satisfy the Art. 15(1) limb tests or the Art. 17 procedural conditions.

**Routes from:**

- "Draft a Ch V request for telematics data."
- "Our agency needs operator data for [X]. Help me prepare the Art. 14 request."
- "Can we ask under Ch V for [non-emergency dataset]?"
- "Public sector body here. We have an emergency. What can we demand under the Data Act?"
- "Is our Art. 15(1)(b) request properly grounded?"

**Adjacent cards (route there instead if the facts indicate):**

- The request is already received by the data holder and the question is whether to honour or decline: `ch5-decline-or-modify.md`.
- The data holder is established in a Member State other than the requesting body's: `ch5-cross-border-cooperation.md` (Art. 22 layer applies on top of this card).
- The matter is the data holder's compensation claim after the request was honoured: forthcoming `ch5-compensation.md`; in the interim, the Art. 20 framework is summarised in `ch5-decline-or-modify.md`.

---

## Canonical fact pattern

A public sector body (or the Commission, the European Central Bank, or a Union body) needs operational data held by a private legal person to discharge a statutory duty. The intended data source is identified. The body has considered whether the data could be obtained voluntarily, by purchase, or under another legal basis, and has concluded that a Ch V request under Art. 14 is the right instrument. The body is now preparing the request and wants either (a) a draft, or (b) confirmation that its draft satisfies Art. 15 and Art. 17.

The data holder is typically a legal person other than a public sector body (Art. 14). The data may be personal, non-personal, or mixed. The matter may be an emergency or a non-emergency. The requesting body and the data holder may or may not be in the same Member State; if they are not, the card hands off to `ch5-cross-border-cooperation.md` after this card's analysis is complete.

---

## Critical disciplines

Three failure modes drive most Art. 17 declensions in the practitioner literature. The card cannot be applied without holding all three.

- **The Art. 15(1) two-limb structure.** Limb (a) is emergency. Limb (b) is non-emergency. They are alternatives, not stages. Limb (b) is narrower than limb (a) on three independent axes: data type (non-personal only), eligible respondent (not microenterprises or small enterprises per Art. 15(2)), and prior-exhaustion requirement (including market purchase at market rates per Art. 15(1)(b)(ii)). A request that conflates them is defective at the level of legal basis.
- **The Art. 17 specificity bar.** Art. 17(1) lists ten cumulative content requirements ((a)-(j)). Art. 17(2) lists nine cumulative form and transmission requirements ((a)-(i)). A request that omits any one of these can be declined under Art. 18(2)(c). The data holder is not obliged to read between the lines. Draft each element explicitly.
- **The once-only principle.** Art. 18(2)(b) lets a data holder decline if a similar request for the same purpose has been previously submitted by another body and the data has not been notified as erased under Art. 19(1)(c). The requesting body must check (per Recital 67, "the once-only principle") that the same data is not already in the public sector's hands before issuing the request. Skipping this check produces an avoidable declension.

---

## The seven-step walk

### Step 1: Scope check

Verify Ch V applies. Art. 16(2) excludes from this Chapter activities for the prevention, investigation, detection, or prosecution of criminal or administrative offences, the execution of criminal penalties, and customs or taxation administration. Those matters route to the sectoral instruments, not Ch V. The carve-out in Art. 1(6) on national security is also live; Ch V cannot be used as a workaround for an instrument that would not otherwise reach the data.

Art. 14 limits the obligation to data holders that are legal persons other than public sector bodies. A request to another public sector body is outside Ch V (Recital 63: "the notion of 'data holder' does not, generally, include public sector bodies", though it may include public undertakings). Confirm the data holder's status before drafting.

### Step 2: Chapter identification

Chapter V. The request is addressed to a "data holder" within the meaning of Art. 2(13), and the basis is Art. 14 read with Art. 15. The card stays in Ch V. If the data is also accessible via Ch II (user-access regime), the public sector body may have an alternative path as a "user" under Art. 2(12) (FAQ Q51: "Nothing prevents a public sector body (as a separate legal entity) from becoming a user in the sense of Chapter II"); that alternative is examined in Step 6.

### Step 3: Role mapping

Required entity-by-entity mapping. Show as a table in the output.

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Requesting body | Public sector body (Art. 2(28)), the Commission, the European Central Bank, or a Union body | Controller for any personal data received and processed | Subject to once-only principle (Recital 67); may not submit a Ch V request and simultaneously act as the competent authority that approves it (Recital 113, last sentence: competent authorities responsible for application "should not benefit from the right to submit such a request") |
| Data holder | Data holder (Art. 2(13)) | Controller, typically, for personal data generated through the connected product or related service | Trade-secret holder under Directive (EU) 2016/943 and Art. 2(19) Data Act if applicable; may be a microenterprise or small enterprise (limb (b) carve-out applies) |
| Data subjects (if personal data in scope) |  | Data subjects | Their GDPR rights run independently of the Ch V request (Art. 17(2)(i) supervisory authority notification) |
| Third parties receiving the data via Art. 17(4) or Art. 21(1) |  |  | Subject to the same Art. 19 obligations as the requesting body |

If the data holder is a microenterprise or small enterprise (Commission Recommendation 2003/361/EC), Art. 15(2) takes limb (b) off the table entirely. A request to an SME on a non-emergency basis is not curable by redrafting; the requesting body must find another data source or wait for an emergency to crystallise that legitimately engages limb (a).

### Step 4: Fact-category sorting

Card-specific dimensions to sort the requested data against.

- **Personal vs non-personal.** Limb (a) may reach personal data only where strictly necessary and after demonstration that non-personal data is insufficient (Art. 17(2)(e); Recital 68). Limb (b) is non-personal only by Art. 15(1)(b) opening words.
- **Data the data holder controls vs not.** Art. 17(2)(b) requires the request to "correspond to data which the data holder has control over at the time of the request". Art. 18(2)(a) lets the data holder decline for lack of control. Verify before drafting.
- **Data necessary to the stated purpose vs broader convenience.** Art. 14 limits the obligation to data "necessary to interpret and use" the requested data for the public-interest task. Art. 17(2)(c) requires proportionality "regarding the granularity and volume of the data requested and frequency of access". A request that exceeds necessity is declinable under Art. 18(2)(c).
- **Trade-secret data vs not.** Trade-secret status does not block a Ch V request (Art. 19(3)), but it triggers a specific safeguarding regime: the request must commit to ensuring the protection of trade secrets in accordance with Art. 19(3) (Art. 17(2)(d)), and the body must take all necessary technical and organisational measures before disclosure (Art. 19(3)).
- **Once-only check.** Has any other public sector body, the Commission, the European Central Bank, or a Union body previously requested similar data for the same purpose? If yes, has the data been erased under Art. 19(1)(c) and the requesting body notified? If the data is still held by another body, Art. 17(4) allows inter-body sharing without a fresh request to the data holder.

### Step 5: Limb-by-limb application

The Art. 15(1) test runs first; if it fails, no amount of Art. 17 drafting can rescue the request.

**Art. 15(1)(a): emergency limb.** Cumulative limbs:

1. The data requested is "necessary to respond to a public emergency". "Public emergency" is defined at Art. 2(29): "an exceptional situation, limited in time, such as a public health emergency, an emergency resulting from natural disasters, a human-induced major disaster, including a major cybersecurity incident ... and which is determined or officially declared in accordance with the relevant procedures under Union or national law". Recital 64 confirms the declaration requirement.
2. The body is unable to obtain the data by alternative means in a timely and effective manner under equivalent conditions. Per FAQ Q44, the Commission interprets "equivalent conditions" as requiring the body to verify the data could not be obtained elsewhere with a comparable amount of effort. Recital 64 last sentence gives illustrative alternatives: voluntary provision by another enterprise, consultation of a public database.

Limb (a) does not require market-purchase exhaustion. Limb (a) may reach microenterprises and small enterprises (Art. 20(1) requires them to claim compensation if they want it; the obligation to make the data available is not suspended for SMEs in an emergency).

**Art. 15(1)(b): non-emergency limb.** Cumulative limbs:

1. The matter is not covered by limb (a).
2. Only non-personal data is in scope.
3. The body is acting on the basis of Union or national law.
4. The body has identified specific data the lack of which prevents fulfilment of a specific task carried out in the public interest, explicitly provided for by law. Recital 65 gives illustrative examples: production of official statistics, mitigation of or recovery from a public emergency.
5. The body has exhausted all other means at its disposal, including purchase of non-personal data on the market at market rates, reliance on existing obligations to make data available, or adoption of new legislative measures that could guarantee timely availability.

Limb (b) does not apply to microenterprises and small enterprises (Art. 15(2)). The market-purchase exhaustion requirement does not apply where the specific task is the production of official statistics and national law does not allow purchase (Art. 15(3)). The Commission, in FAQ Q45, takes the view that limb (b) is available "only if it has been unable to obtain the non-personal data, either because the data cannot be purchased or because the public sector body made an unsuccessful attempt to buy it at the market rate (e.g. via procurement)". Document the procurement attempt or the unavailability before drafting.

**Art. 17(1) content requirements (ten cumulative limbs).** Each must appear in the request:

1. (a) Specify the data required, including relevant metadata.
2. (b) Demonstrate the Art. 15 conditions are met. This is the limb that carries the substantive justification.
3. (c) Explain purpose, intended use (including by any third party under Art. 17(4)), duration of use, and (if personal data) how processing addresses the exceptional need.
4. (d) Specify, if possible, when the data are expected to be erased by all parties.
5. (e) Justify the choice of data holder.
6. (f) Specify any other public sector bodies and third parties with which the data is expected to be shared.
7. (g) Where personal data are requested, specify technical and organisational measures to implement data protection principles, including pseudonymisation, and whether anonymisation can be applied by the data holder before transfer.
8. (h) State the legal provision allocating the specific public-interest task to the requesting body.
9. (i) Specify the deadline by which the data are to be made available and the Art. 18(2) decline-or-modify deadline applicable to the data holder.
10. (j) Make best efforts to avoid compliance resulting in the data holder's liability for infringement of Union or national law.

**Art. 17(2) form and transmission requirements (nine cumulative limbs).** Each must hold:

1. (a) In writing, in clear, concise, and plain language understandable to the data holder.
2. (b) Specific regarding the type of data and corresponding to data the data holder controls at the time of the request.
3. (c) Proportionate to the exceptional need, in granularity, volume, and frequency.
4. (d) Respects the data holder's legitimate aims, commits to trade-secret protection under Art. 19(3), and respects cost and effort.
5. (e) Non-personal data only, unless demonstrated insufficient to respond to an Art. 15(1)(a) exceptional need; personal data only in pseudonymised form with stated technical and organisational measures.
6. (f) Informs the data holder of the penalties under Art. 40 in case of non-compliance.
7. (g) For a public sector body requester, transmitted to the data coordinator of the requesting body's Member State (Art. 37), who publishes it online without undue delay unless publication creates a public-security risk.
8. (h) For Commission, ECB, or Union body requesters, made available online without undue delay.
9. (i) Where personal data are requested, notified without undue delay to the GDPR supervisory authority of the requesting body's Member State.

The European Central Bank and Union bodies must additionally inform the Commission of their requests (Art. 17(2) closing sentence).

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. The Ch V request itself triggers GDPR for any personal data the body subsequently processes. Recital 68 directs public sector bodies to use non-personal data wherever possible and to anonymise where personal data falls in scope (Art. 18(4)). The body's controller obligations under GDPR apply to the data received and to its onward use under Art. 21(1) (research) or Art. 17(4) (delegation).
- **Trade Secrets Directive overlay (loaded if trade-secret data in scope).** Read `references/gates/trade-secrets-directive.md`. Art. 19(3) of the Data Act adapts the TSD safeguarding regime to the Ch V context: the body must, prior to disclosure, take all necessary and appropriate technical and organisational measures to preserve confidentiality (model contractual terms, technical standards, codes of conduct). Build the safeguard commitment into Art. 17(2)(d) of the request.
- **Sectoral lex specialis (warn-only).** Read `references/gates/sectoral-lex-specialis.md` if the data is from a regulated sector. Sectoral instruments may already give the public sector body a route to the data (e.g. statistical reporting obligations, health emergency reporting). Use them first; Recital 65 prefers "existing obligations to make data available" as part of the Art. 15(1)(b)(ii) exhaustion analysis.
- **Member State gate (always loaded).** Read `references/gates/member-state.md`. The data coordinator for Art. 17(2)(g) is the requesting body's Member State data coordinator. If the data holder is established in another Member State, Art. 22 cooperation applies and the card hands off to `ch5-cross-border-cooperation.md`. The GDPR supervisory authority for Art. 17(2)(i) is also the requesting body's Member State supervisory authority.
- **Ch II alternative (warn-only).** If the requesting public sector body could obtain the same data as an Art. 2(12) "user" of a connected product or related service (FAQ Q51), Ch II may be a less burdensome route. Ch II avoids the Art. 17 procedural requirements, the once-only principle, and the cross-border Art. 22 layer, at the cost of being available only where the body is genuinely the user.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Articles 14, 15, 16, 17, 18, 19, 20, 21, and 22 of Regulation (EU) 2023/2854 (Data Act) govern. The two-limb Art. 15(1) test, the Art. 17 procedural conditions, and the Art. 19 use limits are operative as drafted. Verbatim text at `sources/regulation-2023-2854.md` Arts. 14-22; operative recitals at Recitals 63-72.
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final (19 November 2025) would narrow the conditions under which public authorities can demand data from businesses in non-emergency situations. Status: co-legislator negotiation, not adopted. See `sources/digital-omnibus-amendments-tracker.md` Chapter V entry.

The output cites current law as operative. The proposed amendment is forward-looking awareness only, relevant where a non-emergency limb (b) request is borderline today and would likely fail under the proposed narrowing.

---

## Decision point

After Steps 5 and 6, the analysis yields one of four paths.

1. **All Art. 15(1) limbs and all Art. 17 conditions can be satisfied on the facts.** Proceed to the Ch V request (Output Path 1 below).
2. **Art. 15(1) fails.** No emergency declared under Art. 2(29); or limb (b) but personal data needed; or limb (b) but data holder is a microenterprise or small enterprise; or limb (b) but market-purchase exhaustion not done and no Art. 15(3) statistical carve-out. Refuse to draft (Output Path 2 below). Identify what would have to change.
3. **Art. 17 missing elements that are not curable on present facts.** The body cannot demonstrate, e.g., the legal provision allocating the task (Art. 17(1)(h)) because no such provision exists. Refuse to draft and identify the gap.
4. **Ch II is a better fit.** The public sector body is or could be a user under Art. 2(12) for the same data. Route to a Ch II analysis (not yet a dedicated card; route via `references/method/analysis-method.md` Step 2).

The card does not produce a request on Paths 2, 3, or 4. The output explains why and what the body needs to do instead.

---

## Output skeleton: Path 1 (Ch V request, all conditions satisfied)

Formal request, Markdown by default, ready for adoption with minimal edit. Length: typically 2 to 3 pages depending on the substantive justification under Art. 17(1)(b).

Structure:

```
[Requesting body letterhead placeholder]

To: [Data holder, full legal entity name and address]
Date: [Date of request]
Reference: [Request reference number; data coordinator publication
            reference once assigned per Art. 17(2)(g) or (h)]
Subject: Request for data pursuant to Articles 14 and 15 of
         Regulation (EU) 2023/2854 (Data Act)

1. Identity and legal basis of the requesting body
   [Full legal name of the requesting body. Statement of whether the
   body is a public sector body of a Member State (Art. 2(28)), the
   Commission, the European Central Bank, or a Union body. Reference
   to the body's establishing instrument.]

2. Data requested
   [Specification of the data required, including relevant metadata
   necessary to interpret and use the data. Granularity, volume,
   frequency, and time-window all stated. Reference to Art. 17(1)(a)
   and (2)(b) for specificity, and Art. 17(2)(c) for proportionality.]

3. Demonstration of exceptional need under Article 15
   3(a) Applicable limb. [Either Art. 15(1)(a) emergency or
        Art. 15(1)(b) non-emergency. Not both.]
   3(b) For Art. 15(1)(a) requests:
        - Reference to the determination or official declaration of
          the public emergency under Union or national law, with
          citation of the declaring instrument (Art. 2(29)).
        - Demonstration that the data cannot be obtained by
          alternative means in a timely and effective manner under
          equivalent conditions. Itemise the alternatives considered
          and why each failed (voluntary provision by another
          enterprise; consultation of a public database; other).
   3(c) For Art. 15(1)(b) requests:
        - Statement that the data sought is non-personal.
        - Statement that the data holder is not a microenterprise or
          small enterprise (Art. 15(2)).
        - Reference to the Union or national law on the basis of
          which the body is acting.
        - Identification of the specific data the lack of which
          prevents fulfilment of a specific task carried out in the
          public interest explicitly provided for by law (e.g.
          production of official statistics under [statistical
          instrument]; mitigation of or recovery from a public
          emergency under [recovery instrument]).
        - Demonstration of exhaustion: voluntary alternatives,
          existing legal obligations, and market purchase at market
          rates each attempted or shown unavailable. If Art. 15(3)
          statistical carve-out applies, state that purchase is not
          allowed by national law and cite the relevant national
          provision.

4. Purpose, intended use, duration, and onward sharing
   [Art. 17(1)(c). Purpose of the request, intended use (including
   any use by a third party under Art. 17(4)), and duration. Where
   personal data is requested, statement of how the processing
   addresses the exceptional need.]

5. Justification of the choice of data holder
   [Art. 17(1)(e). Why this data holder, and not another, has been
   selected.]

6. Other recipients and third parties
   [Art. 17(1)(f). Any other public sector bodies, the Commission,
   the European Central Bank, Union bodies, or third parties with
   which the data is expected to be shared. If applicable, state the
   delegation under Art. 17(4) and confirm that the third party will
   be subject to Article 19 obligations.]

7. Personal data: necessary safeguards
   [Art. 17(1)(g). If personal data is requested:
   - Technical and organisational measures to implement data
     protection principles (purpose limitation, data minimisation,
     storage limitation, integrity and confidentiality).
   - Pseudonymisation measures applied.
   - Whether anonymisation can be applied by the data holder before
     making the data available (Art. 18(4) presumption).
   Statement that the request has been notified to the GDPR
   supervisory authority of [requesting body's Member State]
   pursuant to Art. 17(2)(i).]

8. Trade-secret safeguards
   [Art. 17(2)(d), Art. 19(3). Commitment that the requesting body
   will, prior to any disclosure, take all necessary and appropriate
   technical and organisational measures to preserve the
   confidentiality of trade secrets identified by the data holder,
   including, as appropriate, model contractual terms, technical
   standards, and codes of conduct.]

9. Legal provision allocating the public-interest task
   [Art. 17(1)(h). Citation of the Union or national law allocating
   to the requesting body the specific task in the public interest
   relevant to this request.]

10. Erasure
    [Art. 17(1)(d). When the data are expected to be erased by all
    parties that have access to them. Reference to the Art. 19(1)(c)
    erasure obligation and the Art. 21(4) six-month research extension
    if applicable.]

11. Deadlines
    [Art. 17(1)(i).
    - Deadline by which the data are to be made available.
    - Decline-or-modify deadline under Art. 18(2): no later than 5
      working days for emergency requests (Art. 15(1)(a)); no later
      than 30 working days for non-emergency requests (Art. 15(1)(b)).]

12. Compliance with other legal obligations
    [Art. 17(1)(j). Statement of the body's best efforts to avoid
    compliance with this request resulting in the data holder's
    liability for infringement of Union or national law.]

13. Penalties on non-compliance
    [Art. 17(2)(f). Information that non-compliance with this request
    may attract penalties imposed by the competent authority
    designated under Art. 37 of the data holder's Member State,
    pursuant to Art. 40.]

14. Publication and notifications
    [Art. 17(2)(g) or (h):
    - Public sector body: confirmation that the request has been
      transmitted to the data coordinator of [requesting body's
      Member State] for online publication.
    - Commission, ECB, or Union body: confirmation that the request
      will be made available online without undue delay; ECB and
      Union bodies have informed the Commission.]

15. Compensation
    [Art. 20.
    - Emergency requests under Art. 15(1)(a): data made available
      free of charge unless the data holder is a microenterprise or
      small enterprise claiming compensation under Art. 20(3).
    - Non-emergency requests under Art. 15(1)(b): fair compensation
      covering technical and organisational costs plus a reasonable
      margin; the body will, upon request, provide the basis for the
      calculation.
    - If the body disagrees with the compensation claimed, the
      matter may be referred to the competent authority under
      Art. 20(5).]

[Signature block placeholder]
```

---

## Output skeleton: Path 2 (refuse to draft, Art. 15(1) or Art. 17 fails)

Short response. Markdown. Lead with the legal reason the request cannot be drafted as posed. No CYA padding; the user is the lawyer.

Structure:

```
The Ch V request as posed cannot be drafted because [the specific
limb that fails]. The most common failures and their cures:

- Art. 15(1)(b) attempted against a microenterprise or small
  enterprise. Art. 15(2) takes limb (b) off the table for these data
  holders entirely. The cure is to find an alternative data source,
  not to redraft the request.

- Art. 15(1)(b) attempted for personal data. Limb (b) is
  non-personal only by Art. 15(1)(b) opening words. The cure is
  either to anonymise the data need (Art. 18(4) regime) or to wait
  for a limb (a) emergency that justifies personal data.

- Art. 15(1)(b) without market-purchase exhaustion. The body must
  attempt to purchase the non-personal data at market rates before
  the limb is available, unless the Art. 15(3) statistical carve-out
  applies. The cure is to document the procurement attempt or its
  unavailability.

- Art. 17(1)(h) cannot be cited because no Union or national law
  allocates the specific public-interest task to the requesting
  body. Without a legal-task anchor, neither limb (a) nor limb (b)
  is reachable; the body must identify the legal basis or
  abandon the request.

- Art. 17(2)(b) specificity fails because the data is requested at a
  level the data holder does not control. The cure is to redraft to
  match the data holder's actual control envelope (Art. 18(2)(a) is
  otherwise the consequence).

To proceed, the requesting body needs to assemble the following
additional facts:

- [Fact 1: relevant declaration or legal provision]
- [Fact 2: alternatives considered and their outcome]
- [Fact 3: if limb (b), market-purchase exhaustion record]
- [Fact 4: data holder's status (SME or not, where applicable)]
- [Fact 5: data scope verified against the data holder's control]

If those facts can be assembled, the card produces the request
(Path 1). If they cannot, the body should consider:

1. Ch II as a user under Art. 2(12) (FAQ Q51), where the body is the
   user of the connected product or related service.
2. A sectoral reporting instrument that already requires the data
   holder to make the data available.
3. Procurement at market rates, which is in any case the limb (b)
   precondition.
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 14, Art. 15(1)-(3), Art. 16(1)-(2), Art. 17(1)-(6), Art. 18(2)(c), Art. 19(1)-(4), Art. 20(1)-(5), Art. 21(1)-(5); Art. 2(28) (public sector body), Art. 2(29) (public emergency).
- `sources/regulation-2023-2854.md` Recital 63 (exceptional need; SME burden limit); Recital 64 (emergency illustrative list; declaration requirement; alternatives examples); Recital 65 (limb (b) examples; exhaustion); Recital 67 (once-only principle; transparency); Recital 68 (anonymisation preference; personal data only on strict necessity); Recital 69 (purpose limitation; erasure); Recital 71 (compensation); Recital 72 (research sharing under Art. 21); Recital 113 last sentence (competent authority may not request its own data).
- `sources/faq-v1-4.md` Q43 (mitigation and recovery), Q44 ("equivalent conditions"), Q45 (limb (b) and procurement attempt), Q46 (data holder's verification checklist), Q47 (cross-border permissibility), Q48 (data is not open data; sharing onwards), Q49 (once-only refusal), Q50 (fundamental rights safeguards), Q51 (public sector body as user under Ch II). Frame each as Commission interpretation.
- `sources/digital-omnibus-amendments-tracker.md` Chapter V entry on proposed narrowing of non-emergency circumstances.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded conditionally on personal data in scope).
- `references/gates/trade-secrets-directive.md` (loaded conditionally on trade-secret data in scope; Art. 19(3) adapts the TSD regime to Ch V).
- `references/gates/sectoral-lex-specialis.md` (warn-only; loaded if the data is from a regulated sector that may offer an alternative route).
- `references/gates/member-state.md` (always loaded; identifies the data coordinator under Art. 17(2)(g) and the supervisory authority under Art. 17(2)(i); identifies the data holder's competent authority for downstream complaints).
- `references/gotchas.md` entry 3 (user-not-data-subject is controller; relevant where the requesting body becomes a Ch II user); entry 4 ("without undue delay" has no numeric SLA; note the Art. 18(2) 5/30 working-day exception); entry 19 (FAQ is non-authoritative); entry 20 (Digital Omnibus is a proposal).
- `references/method/analysis-method.md` (the seven-step flow; this card is one instance).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (Chapter V entry).
- `references/scenarios/ch5-decline-or-modify.md` (the data holder's mirror response; cited so the drafter sees what the data holder will check against).
- `references/scenarios/ch5-cross-border-cooperation.md` (Art. 22 layer if the data holder is in a different Member State).

---

## Drafter notes

Operational observations for using this card. Three only.

- **The Art. 17(2)(g) publication is a discipline.** Member State data coordinators publish public sector body requests online unless publication creates a public-security risk. The request will be public. Draft as if it will be read by the data holder's competitors, the regulator, and the press; do not put anything in the substantive justification that the body would not defend in court.
- **Limb (a) and limb (b) have different decline-or-modify clocks.** Art. 18(2) gives the data holder 5 working days for emergency requests and 30 working days for non-emergency requests. State the applicable clock in Art. 17(1)(i). A request that does not name the clock invites a decline on Art. 18(2)(c) procedural grounds before the substantive merits are reached.
- **The once-only check is cheap.** Recital 67 builds the once-only principle into the regime. Before issuing the request, query other public sector bodies and the data coordinator for prior requests for the same data and the same purpose. A request that ignores this risks an Art. 18(2)(b) decline that the body could have avoided by a single email.
