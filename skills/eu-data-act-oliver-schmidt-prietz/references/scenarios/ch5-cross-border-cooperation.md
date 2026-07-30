# ch5-cross-border-cooperation

**Anchor:** Cross-border × Ch V × Art. 22. The Ch V cross-border layer. A public sector body, the Commission, the European Central Bank, or a Union body wants data from a data holder established in a Member State other than the requesting body's Member State. Art. 22 imposes an ex ante notification and examination procedure that runs in addition to, not instead of, the Art. 15 substantive test and the Art. 17 procedural requirements. The card produces the Art. 22(3) notification and walks the parallel competent-authority examination under Art. 22(4).

**Routes from:**

- "We are based in MS A and need data from a holder in MS B. What does Art. 22 require?"
- "Cross-border Ch V notification."
- "The competent authority of [MS B] has objected to our request. What now?"
- "Mutual assistance under Art. 22: how does it work?"
- "Can we send a Ch V request directly to a data holder in another Member State?"

**Adjacent cards (route there instead if the facts indicate):**

- The request has not yet been substantively drafted and the analysis is upstream of Art. 22: `ch5-request-preparation.md` (run that card first; this card overlays the cross-border procedure).
- The data holder has received a cross-border request and is preparing to decline or modify it: `ch5-decline-or-modify.md` (the data holder's Art. 18(2) clock starts when the request is transmitted under Art. 22(4)(a), not when the public sector body initially issued it).
- The cross-border element is a third-country government access request to a data processing service provider, not an EU-internal cross-border Ch V request: that is Ch VII (Art. 32) territory, not Ch V; route via `references/method/analysis-method.md`.

---

## Canonical fact pattern

A requesting body (public sector body, the Commission, the European Central Bank, or a Union body) wants data from a data holder established in a Member State other than the requesting body's. The substantive analysis under Art. 15(1) and the procedural analysis under Art. 17(1) and (2) have been completed (per `ch5-request-preparation.md`). The body is ready to issue the request. Art. 22 imposes a notification step to the competent authority of the data holder's Member State before the request reaches the data holder.

The matter may be an emergency or a non-emergency. The requesting body's Member State and the data holder's Member State each have a designated competent authority under Art. 37; they may have a single data coordinator each or several competent authorities with a data coordinator. The competent authority of the data holder's Member State pre-examines the request under Art. 22(4) and either transmits it (with or without cooperation advice) or rejects it on duly substantiated grounds.

---

## Critical disciplines

Three failure modes drive most defective cross-border Ch V matters. The card cannot be applied without holding all three.

- **Art. 22(3) notification is constitutive, not advisory.** A cross-border request that bypasses the data holder's Member State competent authority and reaches the data holder directly is procedurally defective. The data holder may decline under Art. 18(2)(c) (Art. 17 conditions not met because Art. 22 was not respected). Notification must precede transmission to the data holder, not run in parallel.
- **The substantive test does not move.** Art. 22 layers on top of Arts. 14, 15, 17. The competent authority of the data holder's Member State examines the request in light of Art. 17 (Art. 22(4) opening). The cross-border procedure does not relax Art. 15(1) substance or Art. 17 specificity. If the request is substantively defective, the competent authority rejects it under Art. 22(4)(b) and the request never reaches the data holder. If it is substantively sound, the competent authority transmits and may advise on cooperation with public sector bodies of the data holder's Member State.
- **The competent authority's substantiated objection is not a recommendation.** Recital 72 (cross-border) and Art. 22(4) second subparagraph require the requesting body to "take into account the advice of and the grounds provided by the relevant competent authority pursuant to the first subparagraph before taking any further action such as resubmitting the request". A rejected request that is resubmitted without addressing the grounds is liable to a second rejection and to enforcement action under Art. 37. The requesting body cannot disregard a substantiated objection.

---

## The seven-step walk

### Step 1: Scope check

Verify Ch V applies (Art. 16(2) carve-outs: criminal law enforcement, customs, taxation; Art. 1(6): national security and other carve-outs). Verify that the cross-border element is genuinely EU-internal: a request from an EU public sector body to an EU-established data holder where the two are in different Member States. A request from an EU body to a non-EU data holder is outside the Art. 22 framework and outside Ch V's territorial reach in the absence of an Art. 37(11) legal representative.

Confirm the data holder is established in a Member State different from the requesting body's. Establishment, not data location, is the trigger for Art. 22. A data holder established in MS A with operations or data hosted in MS B is governed by MS A's competent authority for Art. 22 purposes.

### Step 2: Chapter identification

Chapter V, with the Art. 22 cross-border procedure overlaying the Art. 14-21 substantive and procedural rules. The card stays in Ch V. If the cross-border element is in fact a third-country government access matter (a non-EU authority seeking data from an EU data processing service provider), the relevant chapter is Ch VII (Art. 32), not Ch V Art. 22.

### Step 3: Role mapping

Required entity-by-entity mapping. Show as a table in the output.

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Requesting body (MS A or EU-level) | Public sector body (Art. 2(28)), the Commission, the European Central Bank, or a Union body | Controller for personal data received | Notification duty under Art. 22(3); take-into-account duty under Art. 22(4) second subparagraph |
| Data holder (MS B) | Data holder (Art. 2(13)) | Controller for personal data within the scope | Trade-secret holder if applicable; Art. 18(2) clock runs once the request is transmitted under Art. 22(4)(a) |
| Competent authority of MS A | Article 37 competent authority | Not a GDPR role | Receives the notification of intent from the requesting public sector body of MS A (Art. 17(2)(g)); publishes the request online under Art. 17(2)(g) unless public-security risk; may impose Art. 40 penalties on the data holder if non-compliance with a sound request |
| Competent authority of MS B | Article 37 competent authority | Not a GDPR role | Pre-examines the request under Art. 22(4) in light of Art. 17; transmits or rejects; advises on cooperation with MS B public sector bodies to reduce administrative burden |
| Public sector bodies of MS B |  |  | Potential cooperation partners under Art. 22(4)(a) (e.g. to coordinate data collection, leverage existing reporting channels, or de-conflict with parallel national requests) |
| GDPR supervisory authority of MS A (if personal data) |  |  | Notified by the requesting body under Art. 17(2)(i); the data holder's MS B supervisory authority is not notified by the Art. 17(2)(i) duty (which is MS A's), though the data holder's GDPR controller obligations engage MS B supervisory authority on the disclosure |

Where the requesting body is the Commission, the European Central Bank, or a Union body, the notification under Art. 17(2)(h) is online publication rather than transmission to a data coordinator. Art. 22(3) still requires notification to the competent authority of the data holder's Member State; the two duties run in parallel.

### Step 4: Fact-category sorting

Card-specific dimensions to sort the request and the cross-border procedure against.

- **Emergency vs non-emergency.** Affects the Art. 18(2) clock that runs against the data holder after Art. 22(4)(a) transmission: 5 working days for Art. 15(1)(a) emergency requests, 30 working days for Art. 15(1)(b) non-emergency requests. The Art. 22(4) competent authority pre-examination runs "without undue delay" and is not subject to the Art. 18(2) clock; the data holder's clock only starts on Art. 22(4)(a) transmission.
- **Member State of the data holder.** Drives which competent authority pre-examines under Art. 22(4) and which Art. 40 penalty regime applies. Identify the competent authority from the public register maintained by the Commission under Art. 37(7). The Member State gate file lists the source-of-truth register pointer.
- **Member State implementation maturity.** Some Member States may not yet have designated competent authorities, or designated authorities may not yet have published Art. 22(4) procedural rules. Run `references/gates/member-state.md` to identify the gap; in jurisdictions with mature designations, the procedure is mechanical; in others, the requesting body may need to engage the Commission for cross-border coordination.
- **Reduction-of-burden cooperation.** Art. 22(4)(a) gives the competent authority of the data holder's Member State a specific advisory role: "advise the requesting public sector body, the Commission, the European Central Bank or the Union body of the need, if any, to cooperate with public sector bodies of the Member State in which the data holder is established with the aim of reducing the administrative burden on the data holder". Identify, before issuing the Art. 22(3) notification, whether such cooperation is available (e.g. national statistical office in MS B already collects the relevant non-personal data; sectoral regulator in MS B already holds equivalent emergency-response data). Recital 67's once-only principle and Recital 72's burden-minimisation principle pull in the same direction.

### Step 5: Limb-by-limb application

**Art. 22(1) cooperation duty.** Cumulative limbs:

1. The duty falls on public sector bodies, the Commission, the European Central Bank, and Union bodies.
2. The duty is to "cooperate and assist one another, to implement this Chapter in a consistent manner".

The duty is general and frames the rest of Art. 22. It applies even where no formal Art. 22(3) notification is yet pending: bodies may consult one another in anticipation of a request, share lessons learned across Member States, and align procedural practice.

**Art. 22(2) use limit.** Cumulative limbs:

1. Data exchanged in the context of assistance requested and provided under Art. 22(1).
2. Shall not be used in a manner incompatible with the purpose for which they were requested.

Art. 22(2) extends Art. 19(1)(a) to the inter-body cooperation context. Where one Member State's authority shares data or work product with another in cooperation under Art. 22, the use limit travels with the data.

**Art. 22(3) ex ante notification.** Cumulative limbs:

1. The intention to request data from a data holder established in another Member State must be notified to the competent authority of that Member State (designated under Art. 37) before the request is made.
2. The same requirement applies to the Commission, the European Central Bank, and Union bodies.
3. The request is examined by the competent authority of the Member State where the data holder is established.

The notification carries the request as drafted plus the substantive justification under Art. 15 and the procedural envelope under Art. 17. The competent authority is not asked to draft the request; it is asked to examine it.

**Art. 22(4) competent authority action.** The competent authority of the data holder's Member State, having examined the request "in light of the requirements laid down in Article 17", shall "without undue delay" take one of two actions:

- (a) Transmit the request to the data holder and, if applicable, advise the requesting body of the need, if any, to cooperate with public sector bodies of the data holder's Member State to reduce administrative burden.
- (b) Reject the request on duly substantiated grounds in accordance with Ch V.

Art. 22(4) second subparagraph: the requesting body shall take into account the advice of and the grounds provided by the competent authority before taking any further action, including resubmitting.

**Interaction with Art. 18(2) clock.** The data holder's Art. 18(2) decline-or-modify window starts when the request is transmitted to the data holder under Art. 22(4)(a). The pre-examination period is between the requesting body and the competent authority; it does not consume the data holder's clock. The data holder treats the request as received on the date the competent authority transmits it.

**Interaction with Art. 17(2)(g) data coordinator publication.** The Art. 22(3) notification to the data holder's Member State competent authority is separate from the Art. 17(2)(g) transmission to the requesting body's Member State data coordinator. A public sector body of MS A makes both notifications: to its own data coordinator for online publication, and to the competent authority of MS B for Art. 22 examination. The Commission, the European Central Bank, and Union bodies publish online under Art. 17(2)(h) instead of Art. 17(2)(g), and additionally notify under Art. 22(3).

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. The Art. 17(2)(i) supervisory authority notification is the requesting body's Member State supervisory authority. The data holder's GDPR controller obligations to its own supervisory authority on disclosure are not displaced by Art. 22. Where personal data crosses Member State boundaries, GDPR's one-stop-shop and lead supervisory authority rules apply to the data holder's processing (including its disclosure to the requesting body) independently of Art. 22.
- **Trade Secrets Directive overlay (loaded if trade-secret data in scope).** Read `references/gates/trade-secrets-directive.md`. The Art. 19(3) safeguarding regime applies as in domestic Ch V matters. Cross-border element does not alter the safeguarding obligations of the requesting body, which retain extraterritorial reach by virtue of Art. 19(3) attaching to the disclosure rather than to the jurisdiction.
- **Sectoral lex specialis (warn-only).** Read `references/gates/sectoral-lex-specialis.md`. Cross-border sectoral cooperation mechanisms (e.g. ECDC for health emergencies, ENISA for cybersecurity, ESMA for financial markets) may pre-empt or supplement the Art. 22 procedure. Where a sectoral instrument provides a faster or more targeted route, use it; Art. 22 remains available where the sectoral instrument does not reach the data.
- **Member State gate (always loaded).** Read `references/gates/member-state.md`. The competent authority of the data holder's Member State is identified from the Commission's Art. 37(7) public register. If MS B has multiple competent authorities, the data coordinator is the single point of contact (Recital 113). Where MS B has not yet completed designation, the requesting body coordinates through the Commission, which can act as an interim point of contact.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Articles 14-22 of Regulation (EU) 2023/2854 (Data Act) govern. Art. 22(1) cooperation duty; Art. 22(2) use limit on inter-body exchanges; Art. 22(3) ex ante notification; Art. 22(4) competent authority examination and action. Verbatim text at `sources/regulation-2023-2854.md` Art. 22; operative recital at Recital 72 (cross-border).
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final (19 November 2025) does not directly amend Art. 22 as of the tracker's source date. The proposed narrowing of Art. 15(1)(b) non-emergency conditions reaches Art. 22 indirectly: a narrower substantive basis means fewer cross-border non-emergency requests survive Art. 22(4) competent authority examination. Status: co-legislator negotiation, not adopted. See `sources/digital-omnibus-amendments-tracker.md` Chapter V entry.

The output cites current law as operative. The proposed amendment is forward-looking awareness only.

---

## Decision point

After Steps 5 and 6, the analysis yields one of four paths.

1. **All Art. 15(1) and Art. 17 conditions satisfied; cross-border procedure required.** Produce the Art. 22(3) notification (Output Path 1 below) and the Ch V request (per `ch5-request-preparation.md` Output Path 1). The two go together: the notification carries the request as drafted.
2. **Competent authority of the data holder's Member State has rejected the request under Art. 22(4)(b).** The requesting body cannot issue the request unchanged. Either (a) resubmit with the substantiated grounds addressed, or (b) abandon the request. Produce the resubmission strategy or the file-closure note (Output Path 2 below).
3. **Cooperation with MS B public sector bodies would reduce burden and is feasible.** Produce a cooperation engagement letter to the MS B public sector body identified by the competent authority of MS B under Art. 22(4)(a) (Output Path 3 below). The Art. 22(3) notification and the Ch V request still go forward; cooperation runs in parallel.
4. **The cross-border element is fictive: the data holder is in fact established in the requesting body's Member State.** Drop Art. 22; route to `ch5-request-preparation.md` for the domestic procedure.

The card does not refuse to draft. Cross-border procedure is a layered obligation, not a substantive bar; the substantive bar lives in Art. 15 and Art. 17 and is treated in `ch5-request-preparation.md` and `ch5-decline-or-modify.md`.

---

## Output skeleton: Path 1 (Art. 22(3) notification accompanying the Ch V request)

Formal notification, Markdown by default, accompanying the Ch V request itself (drafted under `ch5-request-preparation.md` Output Path 1). Length: typically 1 to 2 pages, plus the request as an annex.

Structure:

```
[Requesting body letterhead placeholder]

To: [Competent authority of the data holder's Member State,
     designated under Article 37 of Regulation (EU) 2023/2854, full
     name and address]
Date: [Date of notification, prior to transmission of the request
       to the data holder]
Reference: [Notification reference]
Subject: Notification of intent to request data from a data holder
         established in [data holder's Member State] pursuant to
         Article 22(3) of Regulation (EU) 2023/2854 (Data Act)

1. Identity and legal basis of the requesting body
   [Full legal name of the requesting body. Statement of whether
   the body is a public sector body of [requesting body's Member
   State], the Commission, the European Central Bank, or a Union
   body. Reference to the body's establishing instrument and the
   legal provision allocating the specific public-interest task
   (Art. 17(1)(h)).]

2. Identity of the data holder
   [Full legal name and address of the data holder. Statement of
   the data holder's Member State of establishment, with evidence
   (commercial register reference; principal place of business).
   Statement that the data holder is a legal person other than a
   public sector body (Art. 14).]

3. Notification of intent under Article 22(3)
   [Statement that, pursuant to Art. 22(3), the requesting body
   intends to request data from the data holder named in section 2
   and is notifying the competent authority of the data holder's
   Member State of that intent before the request is transmitted
   to the data holder.]

4. The request (annexed)
   [Reference to the annexed Ch V request, drafted in compliance
   with Art. 17(1) and (2). The annex is the request as it would
   be transmitted to the data holder under Art. 22(4)(a). The
   competent authority examines the request "in light of the
   requirements laid down in Article 17" pursuant to Art. 22(4).]

5. Summary of the substantive basis
   [Concise summary, for the competent authority's examination, of:
   - Art. 15(1)(a) or (b) limb invoked.
   - For Art. 15(1)(a): reference to the public emergency
     declaration under Art. 2(29) and the alternative-means
     analysis under Art. 15(1)(a) closing words.
   - For Art. 15(1)(b): the Union or national law on the basis of
     which the body is acting; the specific public-interest task;
     the data identified and the lack-of-data analysis;
     the exhaustion analysis including market-purchase attempts
     (or the Art. 15(3) statistical carve-out).
   - Confirmation that the data holder is not a microenterprise
     or small enterprise (for Art. 15(1)(b) requests; Art. 15(2)).]

6. Art. 22(4)(a) cooperation
   [Identification of any cooperation with public sector bodies of
   the data holder's Member State that the requesting body has
   already explored or proposes. Where the competent authority
   identifies additional cooperation opportunities under
   Art. 22(4)(a), the requesting body undertakes to take that
   advice into account.]

7. Notifications running in parallel
   [Reference to:
   - For public sector body requesters: Art. 17(2)(g)
     transmission to the data coordinator of the requesting
     body's Member State for online publication.
   - For Commission, ECB, Union body requesters: Art. 17(2)(h)
     online publication; ECB and Union bodies have informed the
     Commission.
   - For personal data requests: Art. 17(2)(i) notification to
     the GDPR supervisory authority of the requesting body's
     Member State.]

8. Effect of this notification
   [Statement that the requesting body will not transmit the
   request to the data holder until the competent authority has
   acted under Art. 22(4)(a) (transmission with or without
   cooperation advice) or Art. 22(4)(b) (rejection on duly
   substantiated grounds). Statement that, upon Art. 22(4)(b)
   rejection, the requesting body will take into account the
   advice of and the grounds provided by the competent authority
   before any resubmission, per Art. 22(4) second subparagraph.]

[Signature block placeholder]

Annex: The Ch V request to the data holder, drafted under Article 17.
```

---

## Output skeleton: Path 2 (response to Art. 22(4)(b) rejection)

Used after the competent authority of the data holder's Member State has rejected the request on duly substantiated grounds under Art. 22(4)(b). Markdown. Two variants depending on whether the requesting body resubmits or closes the file.

### Path 2A: resubmission

```
[Requesting body letterhead placeholder]

To: [Competent authority of the data holder's Member State]
Date: [Date]
Reference: [Resubmission reference; quote the prior notification
            reference and the competent authority's rejection
            reference]
Subject: Resubmission of intent to request data pursuant to
         Article 22 of Regulation (EU) 2023/2854 (Data Act)

1. Grounds of the prior rejection
   [Concise restatement of the grounds the competent authority
   provided in the Art. 22(4)(b) rejection.]

2. How the resubmitted request addresses each ground
   [Point-by-point response. Where the ground was a Art. 17
   procedural defect, the resubmission cures it (revised wording
   annexed). Where the ground was an Art. 15(1) substantive defect
   (e.g. limb (b) without exhaustion), the resubmission either
   demonstrates the missing limb or invokes a different limb
   that the facts now support, or it is abandoned.]

3. Take-into-account statement
   [Statement that the requesting body has taken into account the
   advice of and the grounds provided by the competent authority
   pursuant to Art. 22(4) second subparagraph. Identify any advice
   that has been adopted and any that has not, with reasons.]

4. The revised request (annexed)
   [Reference to the annexed revised Ch V request.]

[Signature block placeholder]
```

### Path 2B: file-closure note (internal)

Where the rejection cannot be cured on current facts, the requesting body closes the file. Internal note, not addressed to the competent authority.

```
File closure note. Ch V request to [data holder] withdrawn following
Art. 22(4)(b) rejection by [competent authority of MS B].

Grounds of rejection: [list].

Cure analysis: [why each ground cannot be addressed on current
facts; e.g. limb (b) attempted against an SME, blocked by
Art. 15(2); limb (b) without market-purchase exhaustion and no
statistical carve-out].

Alternatives considered:
- Ch II as a user (FAQ Q51).
- Sectoral reporting instrument.
- Procurement at market rates.
- Inter-body sharing under Art. 17(4) from a different public
  sector body that already holds the data.

Decision: [closure / pursuit of alternative]. Owner: [name and
function].
```

---

## Output skeleton: Path 3 (cooperation engagement letter)

Used in parallel with the Art. 22(3) notification where the competent authority of MS B has advised, or the requesting body has independently identified, that cooperation with MS B public sector bodies would reduce administrative burden on the data holder. Markdown. Short.

```
[Requesting body letterhead placeholder]

To: [MS B public sector body identified as a cooperation partner]
Cc: [Competent authority of MS B]
Date: [Date]
Reference: [Cooperation engagement reference]
Subject: Cooperation under Article 22(4)(a) of Regulation (EU)
         2023/2854 (Data Act)

1. Context
   [Reference to the Art. 22(3) notification dated [date]
   concerning a Ch V request to [data holder]. Reference to the
   competent authority of MS B's advice (or the requesting body's
   independent identification) that cooperation with the
   addressee MS B public sector body would reduce the data
   holder's administrative burden.]

2. Cooperation proposed
   [Concrete cooperation proposal. Examples:
   - The MS B public sector body already collects equivalent
     data from the data holder under a sectoral reporting
     instrument; the requesting body would receive the data via
     the MS B body's onward transfer under Art. 17(4) rather
     than via a fresh Art. 14 request.
   - The MS B public sector body and the requesting body agree
     on a single technical channel for the data holder's
     transmission, avoiding duplicative format conversions.
   - The MS B public sector body coordinates the data holder
     interaction in-language, with the requesting body receiving
     the data after technical processing.]

3. Limits of the cooperation
   [Statement that the substance of the Ch V request remains
   under Art. 14-21 governance; the cooperation is operational,
   not substantive. The Art. 19 use limits travel with any data
   the MS B body or any third party receives in the cooperation.]

4. Next steps
   [Proposed timeline for the cooperation, aligned with the
   data holder's Art. 18(2) clock (5 or 30 working days from
   Art. 22(4)(a) transmission).]

[Signature block placeholder]
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 14, Art. 15(1)-(3), Art. 17(1)-(2), Art. 18(1)-(5), Art. 19(1)-(4), Art. 20(1)-(5), Art. 21(1)-(5), Art. 22(1)-(4); Art. 2(13) (data holder), Art. 2(28) (public sector body), Art. 2(29) (public emergency), Art. 37 (competent authority designation and register), Art. 40 (penalties).
- `sources/regulation-2023-2854.md` Recital 63 (exceptional need; SME limit); Recital 64 (emergency declaration); Recital 65 (limb (b) examples and exhaustion); Recital 67 (once-only and transparency); Recital 72 (cross-border procedure; notification of supervisory authority where personal data; competent authority's substantiated objection and the requesting body's take-into-account duty); Recital 113 (competent authorities and data coordinators; cross-border cooperation; conflict-of-interest rule that competent authorities responsible for application may not request data themselves).
- `sources/faq-v1-4.md` Q46 (data holder's verification checklist; cross-border element); Q47 (cross-border permissibility, and that Art. 22 provides the ex ante examination procedure to ensure the data holder's protection). Frame each as Commission interpretation.
- `sources/digital-omnibus-amendments-tracker.md` Chapter V entry on proposed narrowing of non-emergency conditions; Art. 22 itself is not directly amended in the proposal.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded conditionally on personal data in scope; Art. 17(2)(i) supervisory authority notification is the requesting body's Member State authority).
- `references/gates/trade-secrets-directive.md` (loaded conditionally on trade-secret data; Art. 19(3) safeguards travel with the disclosure across Member State boundaries).
- `references/gates/sectoral-lex-specialis.md` (warn-only; sectoral cross-border instruments may pre-empt or supplement Art. 22).
- `references/gates/member-state.md` (always loaded; identifies the Art. 22 competent authority of the data holder's Member State from the Art. 37(7) public register; identifies the requesting body's Member State competent authority and data coordinator).
- `references/gotchas.md` entry 4 ("without undue delay" has no numeric SLA; relevant to Art. 22(4) timing); entry 19 (FAQ is non-authoritative; Q46 and Q47 framed as Commission interpretation); entry 20 (Digital Omnibus is a proposal; Art. 22 itself unaltered but the substantive Art. 15(1)(b) narrowing reaches cross-border practice).
- `references/method/analysis-method.md` (the seven-step flow; this card is one instance and overlays `ch5-request-preparation.md`).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (Chapter V entry).
- `references/scenarios/ch5-request-preparation.md` (the upstream substantive and procedural drafting card; the Art. 22 notification carries the request drafted there as an annex).
- `references/scenarios/ch5-decline-or-modify.md` (the data holder's response posture once the request is transmitted under Art. 22(4)(a); the data holder's Art. 18(2) clock starts at that point).

---

## Drafter notes

Operational observations for using this card. Three only.

- **Art. 22(3) runs in parallel with Art. 17(2)(g) or (h), not instead of.** The requesting public sector body notifies the data coordinator of its own Member State under Art. 17(2)(g) for online publication, and separately notifies the competent authority of the data holder's Member State under Art. 22(3) for examination. These are two distinct duties served by two distinct documents. The Commission, the European Central Bank, and Union bodies publish online under Art. 17(2)(h) and notify under Art. 22(3); they do not transmit to a data coordinator (they have none of their own).
- **The data holder's Art. 18(2) clock starts at Art. 22(4)(a) transmission.** Do not pre-emptively engage the data holder before the competent authority of MS B has acted. Engaging the data holder before transmission both bypasses Art. 22(3)-(4) (a procedural defect) and may prejudice the competent authority's pre-examination. Confine pre-transmission contact with the data holder to operational courtesy (e.g. notifying the data holder that a request is in train); do not start substantive discussions.
- **Substantiated objections compound across resubmissions.** A first Art. 22(4)(b) rejection on grounds X gives the requesting body the option to resubmit with X addressed. A second rejection of a resubmission that did not adequately address X (or that introduced new grounds Y) damages the requesting body's standing in any subsequent enforcement action under Art. 37. Treat the first rejection's grounds as substantive feedback to be addressed, not as an obstacle to be worked around.
