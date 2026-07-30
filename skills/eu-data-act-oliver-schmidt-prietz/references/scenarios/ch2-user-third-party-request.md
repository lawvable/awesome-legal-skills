# ch2-user-third-party-request

**Anchor:** User × Ch II × Art. 5(1) third-party request. The user directs the data holder to make readily available data available to a third party chosen by the user. The card runs the user-side analysis and drafts the user's request. The DMA gatekeeper gate (Art. 5(3)) is constitutive on this card: the gate runs every time, before the request is sent.

**Routes from:**

- "Draft an Art. 5(1) request to send our connected-product data to [third party]."
- "Can we redirect the data feed from the manufacturer to our chosen aftermarket service provider?"
- "What protections are in place for our chosen third party under the Data Act?"
- "We want a fleet-management vendor to receive our vehicle telematics directly. How?"
- "Is the third party allowed to be [named platform]?"

**Adjacent cards (route there instead if the facts indicate):**

- The user wants the data for itself, not for a third party: `ch2-user-direct-request.md` (Art. 4(1) route).
- The third party has received the data and is reviewing what it can lawfully do: `ch2-third-party-permitted-use.md` (Art. 6).
- The data holder is preparing the response to the Art. 5(1) request: `ch2-data-holder-response.md` (with Art. 5(1) adaptations).
- The data holder has refused under Art. 5(11): `ch2-trade-secret-stage-3-refusal.md` carries the Art. 4(8) analysis and the parallel Art. 5(11) ladder transposes; the dedicated Art. 5(11) card is not yet drafted.

---

## Canonical fact pattern

A user (natural or legal person) wants to direct disclosure of readily available data to a third party of its choice. The third party is typically an aftermarket service provider, an analytics vendor, a fleet manager, a data intermediation service, a research organisation, or another commercial partner. The user invokes Art. 5(1) to require the data holder to make the data available to the third party without undue delay, in the same format and quality entitlement as the Art. 4(1) right.

The user is typically an enterprise; consumer users also have the right but the operational profile differs. The third party has agreed in principle to receive the data and to enter into the contract required by Art. 6(1) for the agreed purposes. The connected product was placed on the Union market and the data was generated after 12 September 2025.

---

## Critical disciplines

- **The Art. 5(3) gatekeeper exclusion is constitutive.** Any DMA-designated gatekeeper is excluded as an eligible third party. The exclusion has three operative limbs (Art. 5(3)(a), (b), (c)) and is reinforced by Art. 6(2)(d) against indirect routing through another third party. The gate at `references/gates/dma-gatekeeper.md` runs every time; the request cannot be drafted until the gate has cleared. See `references/gotchas.md` entry 11 for the tripartite reach.
- **Art. 5(1) is free of charge to the user, not to the third party.** The user pays nothing. The third party may owe the data holder compensation under Arts. 8 and 9; the request runs through Ch III pricing rules. The user should not promise on the third party's behalf; the third party's compensation is the third party's matter.
- **Art. 5(7) personal data legal-basis condition.** Where the user is not the data subject and the data sought includes personal data of natural persons other than the user, the data holder may disclose personal data to the third party only where there is a valid Art. 6 GDPR legal basis (and where relevant Art. 9 GDPR and Art. 5(3) ePrivacy conditions). The user should pre-empt by either being the data subject (consent route under Art. 6(1)(a)), having a contract with affected data subjects (Art. 6(1)(b)), or identifying another lawful basis.
- **Art. 5(13) data subject rights are unaffected.** A third-party request must not adversely affect the rights of data subjects under applicable Union and national personal-data protection law. The Art. 20 GDPR portability right is parallel and is not displaced.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check, Art. 1(6) carve-outs, and the Art. 2(22) placement test. Two card-specific limbs:

- **Art. 5(2): not for testing-stage connected products.** Where the connected product, substance, or process is not yet placed on the market, Art. 5(1) does not apply unless third-party use is contractually permitted. Confirm the product is placed.
- **Art. 7(1): microenterprise and small enterprise exclusion.** The Ch II obligations do not apply to data generated through connected products manufactured or designed, or related services provided, by a microenterprise or a small enterprise (subject to the partner-or-linked-enterprise and subcontracting carve-outs). If the data holder is in that bracket, Art. 5(1) does not apply.

### Step 2: Chapter identification

Chapter II. Art. 5(1) is the operative third-party-disclosure right. The request engages Art. 5(3) (gatekeeper exclusion), Art. 5(4) (verification limits), Art. 5(7) (personal data legal basis), Art. 5(9)-(11) (trade-secret ladder for third parties), Art. 5(13) (data subject rights preservation), and pulls in Arts. 8 and 9 for the third-party compensation regime. Art. 6 obligations attach to the third party once it receives the data, in particular Art. 6(2)(d) (no onward sharing to gatekeepers) and Art. 6(2)(e) (no competing-product development).

### Step 3: Role mapping

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| User (natural or legal person) | User (Art. 2(12)) | Data subject if natural person and data relates to them; controller if enterprise (Recital 34) and personal data of other natural persons in scope | Source of the Art. 5(1) instruction |
| Chosen third party | Third party in the Art. 5 sense (Art. 5(1)); becomes data recipient on receipt | Controller for personal data it receives, typically; or joint controller with the user where they jointly determine purposes and means | Subject to Art. 6 prohibitions on receipt; subject to DMA gatekeeper exclusion check |
| Data holder | Data holder (Art. 2(13)) | Controller pre-disclosure | May be trade-secret holder |
| Affected data subjects (if user is an enterprise) |  | Data subjects | Rights preserved under Art. 5(13); Art. 20 GDPR portability unaffected |

Two role overlaps to flag:

- The user as enterprise becomes controller for personal data of other natural persons under Recital 34. The user's instruction to the data holder to disclose to a third party is the user-as-controller's processing decision; the user must have a valid Art. 6 GDPR basis for that disclosure. Art. 5(7) is the Data Act condition that mirrors this.
- The third party will be controller (or joint controller with the user) for the personal data it receives. The third party's own GDPR posture is a separate analysis from the Data Act analysis; do not blend.

### Step 4: Fact-category sorting

Card-specific dimensions to sort the requested data against.

- **In-scope vs out-of-scope data.** Readily available data (Art. 2(17)) only. Inferred or derived data out under Recital 15.
- **Personal vs non-personal.** Drives the Art. 5(7) legal-basis check.
- **Trade-secret data vs not.** Where trade-secret content is in scope, Art. 5(9) safeguards apply between data holder and third party. The user should anticipate that the safeguard contract will be tripartite or that the data holder will require direct safeguards from the third party before honouring the request.
- **Connected-product data vs related service data.** Both in scope.
- **Real-time vs historical.** Both in scope; real-time conditioned on "where relevant and technically feasible".

### Step 5: Limb-by-limb application of Art. 5(1) and the gatekeeper gate

Art. 5(1) cumulative entitlement (mirrors Art. 4(1) with one structural difference):

1. **Upon request by a user, or by a party acting on behalf of a user.** A data intermediation service or other authorised agent may submit the request on the user's behalf (Recital 30).
2. **Readily available data and relevant metadata.** Same standard as Art. 4(1).
3. **Without undue delay.** No numeric SLA (`references/gotchas.md` entry 4).
4. **Same quality, easily, securely, free of charge to the user, in a comprehensive, structured, commonly used and machine-readable format, and where relevant and technically feasible continuously and in real-time.** "Free of charge to the user" is the structural variation from Art. 4(1); the third party may owe compensation under Arts. 8 and 9.
5. **In accordance with Arts. 8 and 9.** The data holder's making available to the third party runs through the Ch III conditions (fair, reasonable, non-discriminatory; transparent; compensation per Art. 9).

Art. 5(3) gatekeeper exclusion (cumulative bar to drafting the request to or for a gatekeeper):

1. **Art. 5(3)(a): no soliciting or commercial-incentivising of the user to provide Art. 4(1)-obtained data to a gatekeeper service.** Where the user is being incentivised by a gatekeeper to invoke Art. 4(1) and feed the data onwards, the user should disengage from the incentive before drafting the request; the request itself would be valid but the chain becomes a Art. 5(3)(a) issue for the gatekeeper.
2. **Art. 5(3)(b): no soliciting or commercial-incentivising of the user to request the data holder to make data available to a gatekeeper service under Art. 5(1).** The Art. 5(1) request to a gatekeeper is directly within this limb.
3. **Art. 5(3)(c): no receiving by a gatekeeper of data the user obtained under Art. 4(1).** The indirect route.

Art. 6(2)(d) extends the bar bidirectionally: any third party that receives data is prohibited from making it available to a gatekeeper. The user's chosen third party must not be itself a gatekeeper and must not be planning to onward-share to one.

Art. 5(4) verification ceiling. Same standard as Art. 4(5): only what is necessary to verify the user's status as user and the third party's status as third party.

Art. 5(7) personal data legal-basis condition. Where the user is not the data subject, the data holder discloses personal data to the third party only where there is a valid Art. 6 GDPR legal basis (and where relevant Art. 9 conditions and Art. 5(3) ePrivacy conditions). The user identifies the legal basis in the request.

### Step 6: Cross-regime gate check

- **DMA gatekeeper gate (always loaded on this card).** Read `references/gates/dma-gatekeeper.md`. Verify the proposed third party against the Commission's current list of designated gatekeepers under Art. 3 of Regulation (EU) 2022/1925 (DMA). Verify whether the third party is part of a corporate group that contains a gatekeeper and whether the proposed receiving entity routes data to a gatekeeper service. If the third party is a gatekeeper, the request cannot proceed; the user must choose a different third party. If the third party is connected to a gatekeeper, run the gate's recipient-attestation procedure. See `references/gotchas.md` entry 11 on tripartite reach.
- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. Two cases:
  - **User is the data subject.** The Art. 5(1) instruction is the user's exercise of its own data right; the parallel Art. 20 GDPR portability right may co-apply.
  - **User is not the data subject (enterprise user).** Art. 5(7) gates the data holder's disclosure on a valid Art. 6 GDPR legal basis. Identify the basis in the request.
- **Trade Secrets Directive overlay (loaded if trade-secret data anticipated).** Read `references/gates/trade-secrets-directive.md`. The Art. 5(9) safeguards arrangement is between the data holder and the third party, but the user is operationally in the loop: the request should signal awareness of the safeguards obligation and confirm the user's expectation that the third party will engage in good faith.
- **Sectoral lex specialis (warn-only).** Run `references/gates/sectoral-lex-specialis.md`.
- **Member State implementing law (warn-only).** Run `references/gates/member-state.md`.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 5(1), Art. 5(3), Art. 5(7), Art. 5(9)-(11) of Regulation (EU) 2023/2854 (Data Act) govern. Verbatim text at `sources/regulation-2023-2854.md` Art. 5; operative recitals at Recitals 30, 33, 34. The Commission maintains the public register of designated gatekeepers under DMA Art. 3.
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final proposes a new refusal ground at Art. 5(11) for substantial risk of unlawful trade-secret acquisition by third-country entities under weaker legal regimes (parallel to the proposed Art. 4(8) amendment). Status: co-legislator negotiation, not adopted. See `sources/digital-omnibus-amendments-tracker.md`.

---

## Decision point

After Steps 5 and 6, the analysis yields one of four paths.

1. **Third party is eligible and request can be drafted.** Produce the Art. 5(1) request (Output Path 1 below).
2. **Third party is a gatekeeper or routes to a gatekeeper.** The request cannot proceed. Path 2: explain the Art. 5(3) bar to the user and ask whether the user wants to choose a different third party.
3. **Personal data in scope and the user (as enterprise) has no valid Art. 6 GDPR legal basis.** Stop and resolve the legal-basis question before the request is sent. Art. 5(7) blocks the data holder's disclosure otherwise.
4. **Trade-secret content in scope and the third party has not agreed in principle to Art. 5(9) safeguards.** The data holder will likely invoke stage 2 (Art. 5(10)) and escalate; the user should secure the third party's safeguard willingness before the request goes out.

---

## Output skeleton: Path 1 (Art. 5(1) request letter)

Formal letter, Markdown by default. Length: typically one to one-and-a-half pages.

Structure:

```
[User letterhead placeholder]

To: [Data holder, full legal entity name and registered address]
Date: [Date of request]
Subject: Request to make data available to a third party under
         Article 5(1) of Regulation (EU) 2023/2854 (Data Act)

1. User identification
   [Legal name, address. Contract reference or product
   identifier(s). Authorised contact person.]

2. Third party identification
   [Third party legal name, address, contact person. Statement
   that the third party is not a gatekeeper designated under
   Art. 3 of Regulation (EU) 2022/1925 (DMA) and is not part of
   a corporate group containing a gatekeeper service to which
   the data would be routed; cross-reference to the Commission's
   public register of designated gatekeepers.]

3. Connected product and/or related service
   [Identification of the in-scope connected product and/or
   related service.]

4. Data requested
   4(a) Categories. [Specific data categories. Include relevant
        metadata.]
   4(b) Temporal range.
   4(c) Format.
   4(d) Delivery channel. [Direct from the data holder to the
        third party. Specify the technical channel: API
        endpoint, secure file transfer, or other.]

5. Identity verification (Art. 5(4))
   [What the user and third party will provide to verify user
   and third-party status. Statement that the data holder may
   not require more than what is necessary.]

6. Personal data and legal basis (Art. 5(7)) [include only if
   personal data of natural persons other than the user is in
   scope]
   [The user relies on the following Art. 6(1) GDPR legal basis
   for the disclosure of personal data sought: [legal basis].
   Where Art. 9 GDPR conditions apply: [state the Art. 9(2)
   condition]. The user has discharged its Art. 14 GDPR
   information obligations to affected data subjects. The user
   confirms that, under Art. 5(13), the rights of data subjects
   are not adversely affected by this request.]

7. Trade-secret safeguards (Art. 5(9)) [include only if trade-
   secret content is anticipated]
   [The user understands that, where the requested data
   includes trade-secret-protected material, Art. 5(9)
   requires the data holder (or, where different, the trade-
   secret holder) and the third party to agree proportionate
   technical and organisational measures prior to disclosure.
   The user confirms that the third party has agreed in
   principle to engage in that arrangement and to comply with
   the obligations under Art. 6(2)(c) and (g).]

8. Compensation (Arts. 8 and 9)
   [The user understands that the data holder may agree
   compensation with the third party under Art. 9 for making
   the data available; the user, by contrast, is entitled to
   the data being made available free of charge to the user.
   The user has no role in setting the data-holder-to-third-
   party compensation arrangement.]

9. Format and quality entitlement
   [The user confirms that, under Art. 5(1), the third party
   is to receive the data of the same quality as is available
   to the data holder, easily, securely, in a comprehensive,
   structured, commonly used, and machine-readable format,
   and, where relevant and technically feasible, continuously
   and in real-time.]

10. Redress
    [If the data holder withholds, suspends, or refuses
    sharing under Art. 5(10) or 5(11), the user reserves the
    right to lodge a complaint under Art. 37(5)(b) with the
    competent authority of [Member State], to refer the
    matter to a dispute settlement body under Art. 10, and to
    seek redress before a court or tribunal of a Member
    State. The third party has parallel redress under
    Art. 5(12).]

[Signature block placeholder]
```

## Output skeleton: Path 2 (gatekeeper bar, request declined)

Short response to the user, Markdown. Length: typically half a page.

Structure:

```
The Art. 5(1) request cannot be issued to [proposed third
party] because Art. 5(3) of Regulation (EU) 2023/2854 (Data
Act) excludes any DMA-designated gatekeeper as an eligible
third party. [Specific factual basis: the proposed third
party is itself a gatekeeper / is part of a corporate group
containing a gatekeeper service to which the data would be
routed / is commercially incentivising the user to redirect
data to a gatekeeper service.]

The bar is cumulative across Art. 5(3)(a), (b), and (c) and
is reinforced by Art. 6(2)(d) (no onward sharing by any
third party to a gatekeeper). See `references/gates/dma-
gatekeeper.md` for the tripartite reach.

To proceed, the user has the following options:

1. Choose a different third party that is not a gatekeeper
   and not connected to one for these purposes. Re-run the
   gate at `references/gates/dma-gatekeeper.md` against the
   replacement.

2. Exercise the Art. 4(1) right to obtain the data directly,
   for the user's own use. The user may then process the
   data itself, but cannot make it available to a gatekeeper
   thereafter (the Art. 5(3)(c) bar persists).

3. If the user is itself a gatekeeper exercising its own
   data right, the Art. 4(1) route is available; the Art. 5
   route is not.
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 5(1), Art. 5(3), Art. 5(4), Art. 5(7), Art. 5(13) (always); Art. 5(9)-(12) (where trade-secret content anticipated or redress flagged); Art. 6(1), Art. 6(2)(d), Art. 6(2)(e) (downstream constraints on the third party).
- `sources/regulation-2023-2854.md` Art. 8, Art. 9 (compensation regime, third-party side).
- `sources/regulation-2023-2854.md` Art. 37(5)(b), Art. 10 (redress).
- `sources/regulation-2023-2854.md` Recital 30 (lawful purpose, intermediary submission), Recital 33 (third-party scope, data holder must not abuse position), Recital 34 (user-not-data-subject).
- Regulation (EU) 2022/1925 (DMA) Art. 3 (gatekeeper designation; Commission's public register).
- `sources/faq-v1-4.md` Q36 (gatekeeper exclusion under Art. 5(3)), framed as Commission interpretation.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/dma-gatekeeper.md` (always loaded on this card; constitutive).
- `references/gates/gdpr-overlay.md` (loaded if personal data in scope).
- `references/gates/trade-secrets-directive.md` (loaded if trade-secret content anticipated).
- `references/gates/sectoral-lex-specialis.md` (warn-only).
- `references/gates/member-state.md` (warn-only, redress paragraph).
- `references/gotchas.md` entries 3 (user-not-data-subject is controller), 4 ("without undue delay" has no numeric SLA), 6 (trade-secret ladder), 11 (Art. 5(3) tripartite reach), 12 (Art. 6(2) closed list).
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `ch2-third-party-permitted-use.md` (the third-party-side card on Art. 6 permitted use after receipt).
- `ch2-data-holder-response.md` (the data-holder-side card; the response card adapts for Art. 5(1)).
- `ch2-trade-secret-stage-3-refusal.md` (where the data holder refuses under Art. 5(11), the analysis transposes from the Art. 4(8) ladder; the dedicated `ch2-trade-secret-stage-3-refusal-art5.md` card is not yet drafted).

---

## Drafter notes

- **The gatekeeper gate runs every time.** Even where the proposed third party seems obviously not a gatekeeper (e.g. a small aftermarket service provider), check against the Commission's current register. The register changes; new gatekeeper designations land at the rate of two or three per year. A request issued to a now-designated gatekeeper is unlawful regardless of the user's intent.
- **Do not blend compensation into the user's request.** The user's letter does not propose or commit on compensation. That is a bilateral matter between data holder and third party under Art. 9. A user that pre-empts compensation discussion risks being read as the controller of that arrangement, which has knock-on roles in Art. 9(4) (SME caps) and Art. 8(3) (non-discrimination).
- **Recipient attestation is the operational answer to gatekeeper-group risk.** Where the third party is connected to a corporate group containing a gatekeeper service, the gate file's recipient-attestation procedure is the practical risk-allocation tool: the third party warrants that it is not a gatekeeper, that the data will not be routed to a gatekeeper service, and that it will indemnify the user on Art. 5(3) and Art. 6(2)(d) breaches. Insert the attestation language into the user-third-party contract, not into the Art. 5(1) request to the data holder.
