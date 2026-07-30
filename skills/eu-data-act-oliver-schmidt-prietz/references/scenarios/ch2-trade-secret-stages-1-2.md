# ch2-trade-secret-stages-1-2

**Anchor:** Data holder × Ch II × Art. 4(6)-(7) trade-secret safeguards and withholding. The data holder has identified trade secrets within the requested data and is at stage 1 (Art. 4(6) safeguards prior to disclosure) or has moved to stage 2 (Art. 4(7) withholding or suspension). Stage 3 (Art. 4(8) refusal) is the next card; this card holds the analysis that must be done before stage 3 is reachable.

**Routes from:**

- "Draft an Art. 4(6) safeguards proposal."
- "The user has declined our proposed safeguards. What do we do next?"
- "Can we withhold the data on the basis that the user has not implemented the agreed measures?"
- "Draft an Art. 4(7) withholding notice."
- "We want to refuse on trade-secret grounds; what comes first?"

**Adjacent cards (route there instead if the facts indicate):**

- Stages 1 and 2 have been completed and the data holder is contemplating Art. 4(8) refusal: `ch2-trade-secret-stage-3-refusal.md`.
- The data holder is producing the initial response and has identified trade secrets: `ch2-data-holder-response.md` (Path 1B leads here).
- The concern is safety or security rather than trade-secret: `ch2-safety-security-handbrake.md` (Art. 4(2)).
- The Art. 5(1) third-party route variant of stages 1 and 2 (Art. 5(9)-(10)) is not yet drafted as a dedicated card; this card's analysis transposes, with `references/gates/trade-secrets-directive.md` carrying the parallel ladder.

---

## Canonical fact pattern

A data holder has received an Art. 4(1) request from a user. The data holder has identified, in the relevant metadata and in correspondence with the user, that some or all of the requested data is protected as trade secret within the meaning of Art. 2(19) of the Data Act and Art. 2(1) of Directive (EU) 2016/943. The data holder is now at stage 1 of the trade-secret ladder (proposing safeguards under Art. 4(6)) or has moved to stage 2 (withholding or suspending under Art. 4(7) because no agreement was reached, the user failed to implement, or the user has undermined the confidentiality of the trade secrets).

The user is typically an enterprise. The data is typically mixed: trade-secret-protected and not, personal and not, raw or pre-processed and not. The competent authority under Art. 37(10) (Member State of establishment) has been or will be notified at stage 2 if the data holder withholds or suspends.

---

## Critical disciplines

- **Ladder, not switch.** Art. 4(6) and 4(7) are graduated. Stage 1 must be attempted before stage 2; stage 2 must be reached (and exhausted on its own grounds) before stage 3 is on the table. Skipping stage 1 invalidates the downstream regime. See `references/gotchas.md` entry 6.
- **Identification is constitutive (Art. 4(6)).** The data holder, or where they are not the same person the trade-secret holder, must identify the data protected as trade secrets, including in the relevant metadata. Identification is not a checkbox; it is the act that creates the procedural standing to invoke the rest of the regime. Data not identified at this stage cannot ground later withholding or refusal of that data.
- **Proportionate safeguards (Art. 4(6)).** The safeguards proposed must be proportionate to the trade-secret risk. Overbroad safeguards (full prohibition of any use, indemnification clauses that effectively bar acceptance, technical measures that prevent the user from realising the Art. 4(1) right at all) are not "necessary" within the article's meaning and are themselves a ground for the user to refuse and a competent-authority complaint route under Art. 37(5)(b).
- **Stage 2 grounds are conjunctive within each ground, but disjunctive across grounds.** Art. 4(7) authorises withholding or suspension where (a) there is no agreement on the safeguards under Art. 4(6), OR (b) the user fails to implement the agreed safeguards, OR (c) the user undermines the confidentiality of the trade secrets. Any one is sufficient. Each must be substantiated: a stage-2 notice that does not specify which ground is engaged is procedurally defective.
- **Stage 2 notification under Art. 37 is constitutive.** Art. 4(7) third sentence: where the data holder withholds or suspends, it notifies the competent authority designated pursuant to Art. 37, identifies which measures have not been agreed or implemented, and where relevant which trade secrets have had their confidentiality undermined. The notification is not subsequent to the withholding; it is part of it.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check, Art. 1(6) carve-outs, and the Art. 2(22) placement test. Confirm Art. 7(1) does not exclude the matter (data holder is not a microenterprise or small enterprise without disqualifying partner or linked enterprises). For Art. 4(6)-(7), the analysis presupposes Art. 4(1) is engaged.

### Step 2: Chapter identification

Chapter II. Art. 4(6) and Art. 4(7) are the operative articles. The parallel third-party-route articles are Art. 5(9) (safeguards) and Art. 5(10) (withholding); their analysis transposes structurally, with the addition that the bilateral negotiation is data-holder-to-third-party rather than data-holder-to-user. Art. 8(6) (Ch III) carries the rule that the obligation to make data available does not oblige the disclosure of trade secrets unless Union law (including Art. 4(6) and Art. 5(9)) or national law adopted in accordance with Union law requires it; this is a structural reinforcement of the safeguards regime, not a separate route to refusal.

### Step 3: Role mapping

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Data holder | Data holder (Art. 2(13)) | Controller, typically | Trade-secret holder under Art. 2(19) Data Act and Art. 2(2) Directive (EU) 2016/943 for trade secrets it holds |
| Trade-secret holder (if not the data holder) |  |  | Licensor of the trade secret to the data holder; required to participate in the Art. 4(6) identification step |
| User | User (Art. 2(12)) | Data subject if natural person; controller if enterprise (Recital 34) |  |
| Competent authority under Art. 37 (Member State of establishment) | Outside the Data Act roles | Outside | Recipient of the stage-2 Art. 4(7) notification |

Where the trade-secret holder and the data holder are different persons, the Art. 4(6) identification step is joint. The data holder cannot make the identification unilaterally on data the trade-secret holder controls; the trade-secret holder cannot make it unilaterally on data the data holder controls. Stage 1 safeguards proposals should reflect both parties' positions and be signed by both where appropriate.

### Step 4: Fact-category sorting

Card-specific dimensions to sort the requested data against.

- **Trade-secret data vs not.** Run the Art. 2(1) Trade Secrets Directive test on each category: (i) secret (not generally known or readily accessible); (ii) commercial value because secret; (iii) subject to reasonable steps under the circumstances by the lawful holder to keep it secret. A category that fails the test is not a trade secret and the Art. 4(6) regime does not apply to it. The full TSD framing is at `references/gates/trade-secrets-directive.md`.
- **Personal vs non-personal.** Drives the parallel GDPR analysis under Art. 4(12) for personal data. The trade-secret regime and the GDPR regime run in parallel; safeguards under Art. 4(6) do not displace GDPR conditions.
- **Readily available vs not (Art. 2(17)).** Not-readily-available data is out of scope of the Art. 4(1) right; the data holder does not need the trade-secret ladder for that data. The analysis falls on Art. 2(17), not Art. 4(6).
- **Categories the data holder claims as trade-secret that may not satisfy the Art. 2(1) TSD test.** The most common operational error is over-claiming: the data holder marks too much of the dataset as trade-secret. Over-claiming creates competent-authority exposure (the authority may rule that the safeguards were imposed on non-trade-secret data, which is itself an Art. 4(4) non-neutral-design issue and an Art. 37(5)(b) complaint ground).

### Step 5: Limb-by-limb application of Art. 4(6) and Art. 4(7)

Art. 4(6) stage 1 obligations on the data holder (and where different the trade-secret holder):

1. **Preserve and disclose only after necessary measures are taken.** "Trade secrets shall be preserved and shall be disclosed only where the data holder and the user take all necessary measures prior to the disclosure to preserve their confidentiality in particular regarding third parties." The wording is that the measures are taken jointly by both parties before disclosure.
2. **Identify the trade-secret data.** Specifically. With sufficient particularity that the user can know which categories require which safeguards. The identification must be reflected in the relevant metadata.
3. **Agree proportionate technical and organisational measures.** Examples in the regulation: model contractual terms (when published by the Commission), confidentiality agreements, strict access protocols, technical standards, codes of conduct. Proportionate to the risk; not more restrictive than necessary.
4. **Engage in good faith.** Implicit in the "agree" language. A data holder that proposes safeguards on a take-it-or-leave-it basis without engaging with user counter-proposals risks the engagement being treated as not in good faith for stage-2 purposes.

Art. 4(7) stage 2 grounds (disjunctive across grounds, conjunctive within each):

1. **No agreement on the measures referred to in Art. 4(6).** Bilateral negotiation has not yielded an arrangement.
2. **User fails to implement the measures agreed pursuant to Art. 4(6).** Stage 1 produced an agreement but the user has not deployed the measures (or has deployed them defectively).
3. **User undermines the confidentiality of the trade secrets.** A specific factual event: confidentiality has been breached.

Stage 2 procedural obligations:

- **Decision duly substantiated and in writing.** Art. 4(7) second sentence.
- **Provided to the user without undue delay.** Promptly in light of the facts; no numeric SLA (`references/gotchas.md` entry 4).
- **Notification to the competent authority under Art. 37.** Specifically: which measures have not been agreed or implemented; where relevant, which trade secrets have had their confidentiality undermined.
- **Withholding or suspension as the case may be.** "Withhold" applies where disclosure has not yet started; "suspend" applies where disclosure has started and is being paused.

The article's language is "withhold or, as the case may be, suspend the sharing of data identified as trade secrets." The measure is targeted to the trade-secret data; non-trade-secret data continues to be made available on the Art. 4(1) standard.

### Step 6: Cross-regime gate check

- **Trade Secrets Directive overlay (always loaded on this card).** Read `references/gates/trade-secrets-directive.md`. The gate file walks the three-stage ladder, the TSD baseline definition test, the conjunction (relevant at stage 3, but the build-up runs through stages 1 and 2), and the technical and organisational measures menu. The gate is the substantive authority for what counts as "proportionate" safeguards.
- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. The trade-secret regime does not displace the GDPR Art. 15 right of access of the data subject. Where the user is also the data subject and is being held off on Art. 4(7) grounds, the user can invoke Art. 15 GDPR directly against the data holder. Recital 31 last sentence: the exceptions to data access rights in this Regulation shall not in any case limit the right of access and right to data portability of data subjects under Regulation (EU) 2016/679.
- **DMA gatekeeper (not applicable on this card).** Art. 5(3) is the gatekeeper exclusion regime and applies to Art. 5 third-party requests; Art. 4(6) and 4(7) on the user route are not affected.
- **Sectoral lex specialis (warn-only).** Run `references/gates/sectoral-lex-specialis.md`. Some sectoral regimes have their own trade-secret-equivalent regimes (e.g. clinical trial regulations); flag the overlay.
- **Member State implementing law (warn-only).** Run `references/gates/member-state.md` for the Art. 37 competent authority.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 4(6) and Art. 4(7) of Regulation (EU) 2023/2854 (Data Act) govern. Verbatim text at `sources/regulation-2023-2854.md` Art. 4(6) and Art. 4(7); operative recital at Recital 31.
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final does not propose substantive amendments to Art. 4(6) or Art. 4(7). The proposed new ground at Art. 4(8) (third-country trade-secret misuse risk) is downstream and does not change the stage-1 or stage-2 mechanics. See `sources/digital-omnibus-amendments-tracker.md`.

---

## Decision point

After Steps 5 and 6, the analysis yields one of four paths.

1. **Stage 1: identification done, safeguards proposed, no engagement yet.** Issue the Art. 4(6) safeguards proposal to the user. Output Path 1.
2. **Stage 1 to stage 2: no agreement after good-faith engagement, or user has failed to implement, or user has undermined confidentiality.** Issue the Art. 4(7) withholding or suspension notice; notify the competent authority. Output Path 2.
3. **Stage 1 progresses to disclosure with safeguards agreed.** The matter resolves; the data holder discloses on the Art. 4(1) standard, subject to the agreed safeguards. No further card output beyond the agreed safeguards memorialised in writing.
4. **Stage 2 is reached but the data holder is contemplating stage 3.** Route to `ch2-trade-secret-stage-3-refusal.md`. Stage 3 is not produced under this card; this card holds the work that must precede stage 3.

---

## Output skeleton: Path 1 (Art. 4(6) safeguards proposal)

Letter to the user, Markdown by default. Length: typically one to two pages. This skeleton is the more elaborated version of the Path 1B skeleton in `ch2-data-holder-response.md`.

Structure:

```
[Data holder letterhead placeholder]

To: [Requesting user]
Date: [Date of proposal]
Subject: Article 4(6) trade-secret identification and proposed
         safeguards in response to your Article 4(1) request
         dated [request date]

1. The request and scope under analysis
   [Identification of the user's request. Identification of
   the data within scope.]

2. Trade-secret identification (Art. 4(6) sentence 2)

   2(a) Categories identified as trade-secret. [Specific
        categories, with sufficient particularity. Reference
        to where the categories appear in the dataset
        structure or schema. The identification will be
        reflected in the relevant metadata on disclosure.]

   2(b) Confirmation of trade-secret status. [Brief
        confirmation that, on the data holder's analysis,
        each identified category satisfies the Art. 2(1) TSD
        test:
        - Secret: not generally known or readily accessible
          to persons within the circles that normally deal
          with the kind of information in question.
        - Commercial value because secret: explained by
          reference to the data's role in the data holder's
          (or trade-secret holder's) business.
        - Reasonable steps to keep it secret: technical and
          organisational measures already in place
          internally.]

   2(c) Trade-secret holder. [Where the trade-secret holder is
        not the data holder, identify the trade-secret holder
        and confirm its participation in this identification.]

3. Proposed safeguards (Art. 4(6) sentence 3)

   3(a) Confidentiality agreement.
        [Specific form: NDA on terms substantially as
        attached; model contractual terms when published by
        the Commission; or sector-specific equivalent.]

   3(b) Strict access protocols.
        [Named individuals authorised to access; two-factor
        authentication; access logging; periodic recertification.]

   3(c) Technical measures.
        [Encryption at rest and in transit; secure
        transmission channel; prohibition on copying outside
        the controlled environment; technical watermarking or
        fingerprinting where appropriate.]

   3(d) Onward-sharing constraints.
        [Prohibition on onward sharing absent the data
        holder's specific written consent, with the carve-out
        that the user may share aggregated, anonymised
        outputs that do not disclose the trade secret.]

   3(e) Code of conduct.
        [Adherence to [specific code if available], or
        compliance with the principles set out in [internal
        document].]

   3(f) Audit rights.
        [Proportionate audit on reasonable notice,
        cost-allocated to the data holder absent a finding of
        breach.]

   3(g) Duration.
        [Safeguards endure for as long as the data retains
        trade-secret status; the user may apply at any time
        for re-assessment if the data ceases to qualify.]

4. Proportionality
   [Brief statement that the safeguards proposed are
   proportionate to the identified trade-secret risk and do
   not extend beyond what is necessary to preserve the
   confidentiality of the data. The data holder is open to
   counter-proposals from the user that would achieve
   equivalent protection through alternative arrangements.]

5. Non-trade-secret data
   [Where the request scope includes non-trade-secret data,
   the data holder is making that portion available
   immediately on the Art. 4(1) standard by [channel] in
   [format].]

6. Invitation to agree
   [Invitation to the user to confirm acceptance within
   [reasonable period], propose modifications, or raise
   questions. Disclosure of the trade-secret-identified data
   follows on agreement. If no agreement is reached, the
   data holder reserves the right to withhold or suspend
   sharing of the trade-secret-identified data under Art.
   4(7) and to notify the competent authority accordingly.]

7. Redress
   [If the user disagrees with the trade-secret
   identification or considers the proposed safeguards
   disproportionate, the user may, without prejudice to its
   right to seek redress before a court or tribunal of a
   Member State, lodge a complaint under Art. 37(5)(b) with
   the competent authority of [Member State] or refer the
   matter to a dispute settlement body under Art. 10.]

[Signature block placeholder]
```

## Output skeleton: Path 2 (Art. 4(7) withholding or suspension notice + Art. 37 notification)

Two documents in parallel. Markdown. Length: typically one to two pages combined.

Notice to the user:

```
[Data holder letterhead placeholder]

To: [User]
Date: [Date of notice]
Subject: Withholding [or: Suspension] of data sharing under
         Article 4(7) of Regulation (EU) 2023/2854 (Data Act)
         in respect of your Article 4(1) request dated
         [request date]

1. The request and stage-1 record
   [Identification of the user's request. Reference to the
   Art. 4(6) safeguards proposal dated [date] and the
   subsequent engagement.]

2. Stage-2 ground engaged
   [Specifically: one or more of the following.
   (a) No agreement was reached on the measures referred to
       in Art. 4(6). [Brief factual account of the
       negotiation and where it broke down.]
   (b) The user has failed to implement the measures agreed
       pursuant to Art. 4(6). [Specific implementation
       failure.]
   (c) The user has undermined the confidentiality of the
       trade secrets. [Specific factual event, including
       date and nature of the undermining.]
   Where more than one ground is engaged, identify each.]

3. Substantiation
   [Brief substantiation of the engaged ground(s) on the
   facts.]

4. Scope of withholding or suspension
   [Specific identification of the trade-secret-identified
   data that is being withheld or whose sharing is being
   suspended. Confirmation that non-trade-secret data
   continues to be made available on the Art. 4(1)
   standard, unimpeded.]

5. Notification to the competent authority
   [Statement that the data holder has, in parallel with
   this notice, notified the competent authority of [Member
   State] designated pursuant to Art. 37. Notification
   reference number where available.]

6. Resumption pathway
   [Statement of the conditions under which the data holder
   would resume sharing: e.g. user implementation of the
   agreed measures; user remediation of the specific
   confidentiality breach; user acceptance of further or
   alternative safeguards.]

7. Redress
   [Information that the user may, without prejudice to its
   right to seek redress before a court or tribunal of a
   Member State, lodge a complaint under Art. 37(5)(b) with
   the competent authority, which shall, without undue
   delay, decide whether and under which conditions data
   sharing is to start or resume, or refer the matter to a
   dispute settlement body under Art. 10.]

[Signature block placeholder]
```

Notification to the competent authority:

```
[Data holder letterhead placeholder]

To: Competent authority of [Member State] designated
    pursuant to Article 37 of Regulation (EU) 2023/2854
    (Data Act)
Date: [Date of notification]
Subject: Notification under Article 4(7) of Regulation (EU)
         2023/2854 (Data Act): withholding [or: suspension]
         of trade-secret data sharing

1. Data holder identification
   [Legal name, address, Art. 37(10) Member State of
   establishment, contact person.]

2. The user and the request
   [Identification of the user, date and scope of the Art.
   4(1) request.]

3. Trade-secret identification record
   [Reference to the Art. 4(6) identification, the trade-
   secret-holder participation (if relevant), and the
   proposed safeguards.]

4. Stage-2 ground engaged
   [Specifically: which of Art. 4(7)(a), (b), or (c).]

5. Measures not agreed or implemented; trade secrets with
   confidentiality undermined
   [Identification, in line with Art. 4(7) third sentence,
   of which measures have not been agreed or implemented,
   and where relevant which trade secrets have had their
   confidentiality undermined.]

6. Withholding or suspension scope
   [Specific identification of the data affected.]

[Signature block placeholder]
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 4(6), Art. 4(7) (always); Art. 4(8) (forward-looking, if stage 3 is on the horizon); Art. 4(9) (redress); Art. 8(6) (Ch III reinforcement that trade-secret disclosure obligations require Union law or national law adopted in accordance with Union law).
- `sources/regulation-2023-2854.md` Art. 37(5)(b), Art. 37(6)(c), Art. 37(10), Art. 38(1), Art. 10 (redress and Commission annual reporting).
- `sources/regulation-2023-2854.md` Recital 31 (graduated structure, conjunction at stage 3, identification step, safeguards menu, redress).
- `sources/faq-v1-4.md` Q23 (Commission interpretation on stage-1 safeguards), framed as Commission interpretation.
- Directive (EU) 2016/943 (Trade Secrets Directive) Art. 2(1) (definition; identification baseline); Art. 3(2)(d) (lawful disclosure required by Union law).

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/trade-secrets-directive.md` (always loaded; substantive authority on identification, safeguards, and proportionality).
- `references/gates/gdpr-overlay.md` (loaded if personal data in scope; Recital 31 last sentence on preservation of data subject GDPR rights).
- `references/gates/sectoral-lex-specialis.md` (warn-only).
- `references/gates/member-state.md` (warn-only, for the competent authority of establishment).
- `references/gates/dma-gatekeeper.md` (not loaded on this card; load if the analysis is transposed to the Art. 5(9)-(10) third-party route and the third party is a gatekeeper).
- `references/gotchas.md` entries 4 ("without undue delay" has no numeric SLA), 6 (ladder, not switch), 7 (the serious-AND-irreparable conjunction; not engaged at stages 1 and 2 but the data holder should be aware before contemplating stage 3), 8 (objective elements illustrative; same forward-looking awareness), 19 (FAQ framing), 20 (Digital Omnibus is a proposal).
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `ch2-data-holder-response.md` (the initial-response card; safeguards proposal originates there at Path 1B and elaborates here).
- `ch2-trade-secret-stage-3-refusal.md` (the next card if stage 2 is reached and the data holder contemplates refusal; that card's Path 1 incorporates the stage-1 and stage-2 record produced here).
- `ch2-safety-security-handbrake.md` (alternative regime; do not confuse).

---

## Drafter notes

- **Build the stage-1 paper trail.** The competent authority's review of any stage-2 withholding or stage-3 refusal will start with the stage-1 record. A stage-1 safeguards proposal that is bare, that does not explain proportionality, or that reads as a take-it-or-leave-it does not support a stage-2 invocation. Build the paper trail at the time, not retrospectively. The stage-1 file is the data holder's strongest asset in the McIntyre OSS enforcement pattern described in `references/gates/trade-secrets-directive.md`.
- **Do not over-identify trade secrets.** Marking too much of the dataset as trade-secret invites the competent authority to find that the safeguards were imposed on non-trade-secret data, which is a separate Art. 4(4) (non-neutral choice imposition) and Art. 37(5)(b) complaint ground. Run the Art. 2(1) TSD test category by category and exclude the categories that genuinely fail.
- **Stage 2 is not a precursor to stage 3 by default.** Stage 2 is its own regime. Many matters resolve at stage 2: the user accepts the engaged ground, remediates, and disclosure resumes. The data holder should not draft stage-2 notices in the expectation of stage 3; that posture weakens the stage-2 substantiation and pre-empts the user's resumption pathway under Art. 4(7) second sentence and Recital 31.
