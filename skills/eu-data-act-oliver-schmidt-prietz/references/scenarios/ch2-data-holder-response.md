# ch2-data-holder-response

**Anchor:** Data holder × Ch II × Art. 4(1) response. The data holder (or counsel) drafts the response to an Art. 4(1) request from a user, or by adaptation to an Art. 5(1) request from or on behalf of a user. The card covers scope, format, latency, the pre-disclosure trade-secret identification under Art. 4(6), and the personal-data legal-basis check under Art. 4(12) where the user is not the data subject.

**Routes from:**

- "Draft the data holder's response to this Art. 4(1) request."
- "How do we comply with this access request without giving away trade secrets?"
- "What checks do we run before disclosing personal data to an enterprise user?"
- "How much time do we have to respond?"
- "Can we charge the user?"
- "The user is asking for data we treat as derived. How do we say no on that ground?"

**Adjacent cards (route there instead if the facts indicate):**

- The data holder wants to refuse on safety or security grounds: `ch2-safety-security-handbrake.md` (Art. 4(2)).
- The data holder has identified trade secrets and is moving to safeguards or withholding: `ch2-trade-secret-stages-1-2.md` (Art. 4(6)-(7)).
- The data holder is at stage 3 refusal: `ch2-trade-secret-stage-3-refusal.md` (Art. 4(8)).
- The request is from a user to disclose to a third party under Art. 5(1): adapt this card with Art. 5 substitutions, or route to `ch2-user-third-party-request.md` (user side) for the parallel analysis.
- The user is preparing the request: `ch2-user-direct-request.md`.

---

## Canonical fact pattern

A data holder has received an Art. 4(1) request from a user (or from a party acting on the user's behalf). The data holder must respond: produce the data, narrow the scope on grounds the regulation permits, identify trade secrets and propose safeguards, raise the Art. 4(12) legal-basis condition where it applies, or in narrow cases invoke a refusal regime. The card produces the response.

The data is typically a mix: some in scope, some not (derived data out of scope under Recital 15); some personal, some not; some trade-secret-protected, some not; some readily available, some requiring disproportionate effort. The data holder is established in one or more Member States; the relevant competent authority under Art. 37 is the one of the Member State of establishment (Art. 37(10)).

---

## Critical disciplines

- **The default is disclosure, on the regulation's quality and format standards.** The data holder cannot downgrade format, charge the user, or impose response delays beyond what "without undue delay" permits on the facts. Refusals are exceptional and run on specific articles; scope-narrowing on Recital 15 (derived data) or Art. 2(17) (not readily available) is a different argument from a refusal.
- **Trade-secret pre-disclosure identification (Art. 4(6)).** The data holder, or where they are not the same person the trade-secret holder, must identify the data protected as trade secrets, including in the relevant metadata, and agree proportionate safeguards with the user prior to disclosure. The identification step is constitutive: data not identified as trade secret at the pre-disclosure stage cannot later support stage 2 withholding or stage 3 refusal in respect of that data. See `references/gotchas.md` entry 6.
- **Art. 4(12) legal-basis check.** Where the user is not the data subject and personal data is in scope, the data holder may disclose personal data to the user only where there is a valid Art. 6 GDPR legal basis (and where relevant Art. 9 GDPR and Art. 5(3) ePrivacy conditions). The legal basis is the user-as-controller's; the data holder does not invent it but does require the user to identify it. A response that discloses personal data to an enterprise user without confirming the basis exposes the data holder to GDPR liability independently of the Data Act.
- **Free of charge to the user, on the Art. 4 route.** Compensation runs under Art. 9 only on the Art. 5 third-party route. The data holder cannot charge the user on Art. 4. It can recover infrastructure costs in setting up an Art. 4 channel; it cannot extract value per request.
- **"Without undue delay" is fact-specific.** No numeric SLA (`references/gotchas.md` entry 4). Promptness in light of the request's scope, the data holder's reasonable preparation time, and the operational character of the data. A two-week response for a one-off historical pull may be reasonable. A two-week setup for a real-time channel may be reasonable. A two-week delay on a self-service portal download is unlikely to be reasonable.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check, Art. 1(6) carve-outs, and the Art. 2(22) placement test. Where the connected product was placed on the market before 12 September 2025, the access right still applies to data generated after that date (FAQ Q4 and Q34a, framed as Commission interpretation). Where the data holder is a microenterprise or small enterprise without disqualifying partner or linked enterprises, Art. 7(1) excludes the Ch II obligations.

### Step 2: Chapter identification

Chapter II. Art. 4(1) is the primary operative article. The response engages Art. 4(2) (only if safety/security is genuinely in play; see adjacent card), Art. 4(5) (verification ceiling, restricting what the data holder may ask the user), Art. 4(6) (trade-secret identification and safeguards), Art. 4(12) (personal data legal basis where user is not data subject), Art. 4(13)-(14) (data holder use restrictions on data after the request). If the request is under Art. 5(1) from a user for a third party, transpose to Art. 5(1)/(4)/(7)/(9) and run Arts. 8 and 9 for compensation.

### Step 3: Role mapping

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Data holder | Data holder (Art. 2(13)) | Controller, typically; may be processor in some configurations | Trade-secret holder (Art. 2(19) Data Act; Directive (EU) 2016/943) for trade-secret data it controls |
| Requesting user | User (Art. 2(12)) | Data subject if a natural person and data relates to them; controller (Recital 34) if an enterprise and personal data of other natural persons in scope; must have Art. 6 GDPR basis under Art. 4(12) |  |
| Affected data subjects (if user is an enterprise and personal data in scope) |  | Data subjects | Rights preserved; the response does not affect their GDPR Art. 15 rights |
| Trade-secret holder (if different from the data holder) |  |  | Must participate in the Art. 4(6) identification step |
| Manufacturer (if different from the data holder) | Not the data holder per se for this purpose | Possibly controller for some processing |  |

Manufacturer-is-not-always-data-holder is the most common role-mapping error from the data holder's side (see `references/gotchas.md` entry 2 and FAQ Q21 framed as Commission interpretation). A response purporting to come from the manufacturer when the data-holder role sits with a related service provider creates standing issues and risks the response being treated as a non-response.

### Step 4: Fact-category sorting

Card-specific dimensions to sort the requested data against.

- **In-scope vs out-of-scope data.** Readily available (Art. 2(17)) and raw or pre-processed (Recital 15) only. Derived data goes out on a scope ground (Recital 15), not a refusal ground. Content data (Recital 16) is similarly out of scope of the Data Act access right.
- **Personal vs non-personal.** Drives the Art. 4(12) gate. Mixed datasets (Recital 7) trigger GDPR for the personal-data component.
- **Trade-secret data vs not.** Drives the Art. 4(6) identification and safeguards step. The data holder runs the Art. 2(1) TSD test on each category it claims as trade-secret: (i) secret; (ii) commercial value because secret; (iii) reasonable steps to keep it secret.
- **Readily available vs not.** Data the data holder can lawfully obtain without disproportionate effort. The data holder may decline to produce data that fails this test, on a scope ground, with explanation.
- **Connected product data vs related service data.** Both in scope.

### Step 5: Limb-by-limb application of the Art. 4 response duties

Cumulative obligations on the data holder, each independent.

1. **Verify the user (Art. 4(5)).** Only what is necessary. Do not demand declarations of intended use, evidence of need, or attestations beyond identity.
2. **Identify the in-scope data (Art. 4(1), Art. 2(17), Recital 15).** Sort the request against the four fact-category dimensions in Step 4. Where data is out of scope, state the specific scope ground (derived; content; not readily available; pre-application).
3. **Identify trade-secret data and propose safeguards (Art. 4(6)).** Pre-disclosure step. Identify the trade-secret-protected categories with sufficient particularity, including in the relevant metadata. Propose proportionate technical and organisational measures: model contractual terms (when published), confidentiality agreements, strict access protocols, technical standards, codes of conduct. The data holder cannot skip this step on the rationale that "the user knows it is sensitive."
4. **Apply the Art. 4(12) legal-basis check (where user is not data subject and personal data is in scope).** Ask the user to identify its Art. 6 GDPR basis (and Art. 9 condition where applicable, Art. 5(3) ePrivacy condition where applicable). Disclose only where the user has identified the basis. Where the user's response is unsatisfactory, withhold the personal-data component on Art. 4(12) grounds; this is a GDPR-conditioned withholding, not a Data Act refusal.
5. **Make the data available (Art. 4(1) format and quality).** Same quality as available to the data holder; easily, securely, free of charge; comprehensive, structured, commonly used, machine-readable format; continuously and in real-time where relevant and technically feasible; simple request through electronic means where technically feasible. The data holder should default to its highest-fidelity exportable format.
6. **Respect verification log-data limits (Art. 4(5)).** The data holder may not keep log data on the user's access beyond what is necessary for sound execution and infrastructure security.
7. **Observe Art. 4(13)-(14) use restrictions.** The data holder may only use the data on the basis of a contract with the user, and may not use it to derive insights about the user's economic situation, assets, or production methods, or in any other manner that could undermine the user's commercial position. The data holder may not make non-personal product data available to third parties other than for the fulfilment of its contract with the user.

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. The Art. 4(12) check is the front line. The data holder's GDPR position is also engaged: the data holder is typically controller for personal data generated by the connected product. The disclosure to the user-as-controller (Recital 34) is a controller-to-controller transfer that needs its own Art. 6 basis on the data holder's side. Where the data subject is the user (natural person), the disclosure is a controller-to-data-subject release that falls under Art. 6(1)(c) (legal obligation under the Data Act) on the data holder's side.
- **Trade Secrets Directive overlay (loaded if trade-secret content in scope).** Read `references/gates/trade-secrets-directive.md`. Run the Art. 2(1) TSD test on each claimed trade-secret category before the Art. 4(6) identification. The gate file carries the eight-step safeguards-then-withholding-then-refusal structure.
- **DMA gatekeeper (not applicable on Art. 4(1) directly).** Art. 5(3) excludes gatekeepers as Art. 5 third parties; it does not constrain Art. 4(1) responses to user requests. If the requesting user is a gatekeeper exercising its own Art. 4(1) right, the response proceeds; the gatekeeper's downstream use is constrained by Art. 4(10) and (11) and Art. 5(3) bars onward redirection.
- **Sectoral lex specialis (warn-only).** Run `references/gates/sectoral-lex-specialis.md`. Sectoral access regimes (e.g. vehicle-data initiatives, medical-device data) may layer with Art. 4(1). The data holder's response should not blend sectoral and Data Act grounds.
- **Member State implementing law (warn-only).** Run `references/gates/member-state.md` to identify the competent authority of the Member State of establishment under Art. 37(10).

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 4 of Regulation (EU) 2023/2854 (Data Act) governs. Verbatim text at `sources/regulation-2023-2854.md` Art. 4(1)-(14); operative recitals at Recitals 26-31, 34.
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final does not propose substantive amendments to the Art. 4(1) response duties. Proposed amendments to Art. 4(8) (new third-country misuse refusal ground) are relevant downstream if the data holder is considering refusal. See `sources/digital-omnibus-amendments-tracker.md`.

---

## Decision point

After Steps 5 and 6, the analysis yields one of five paths.

1. **All requested data is in scope, no trade-secret content, no personal-data Art. 4(12) issue.** Produce the data in compliance with Art. 4(1) format and quality standards. Send a short cover note. Output Path 1A.
2. **All requested data is in scope, but trade-secret content is in scope.** Issue a pre-disclosure Art. 4(6) safeguards proposal. Disclosure follows after agreement. If no agreement: route to `ch2-trade-secret-stages-1-2.md`. Output Path 1B.
3. **Some requested data is out of scope (derived, content, not readily available, pre-application).** Disclose the in-scope portion; explain the scope-based exclusion for the rest. Output Path 1C.
4. **Personal data in scope, user is not data subject, Art. 4(12) check not satisfied.** Withhold the personal-data component pending the user's identification of a valid Art. 6 GDPR legal basis. Output Path 2.
5. **Refusal contemplated on safety, security, or trade-secret grounds.** Route to the dedicated card (`ch2-safety-security-handbrake.md`, `ch2-trade-secret-stages-1-2.md`, or `ch2-trade-secret-stage-3-refusal.md`). Do not produce a refusal under this card.

---

## Output skeleton: Path 1A (clean disclosure)

Short cover letter accompanying the data delivery. Markdown by default. Length: typically half a page.

Structure:

```
[Data holder letterhead placeholder]

To: [Requesting user]
Date: [Date of response, calibrated to "without undue delay"
       on the facts]
Subject: Response to your Article 4(1) request dated [request
         date] under Regulation (EU) 2023/2854 (Data Act)

1. The request
   [Identification of the user's request, scope, reference.]

2. Data made available
   [Description of the data being made available, format,
   delivery channel (portal, API, secure transfer), and
   retrieval instructions. Confirmation that the data is of
   the same quality as is available to the data holder, in a
   comprehensive, structured, commonly used, and machine-
   readable format.]

3. Verification (Art. 4(5))
   [Confirmation that the data holder has applied no more
   verification than necessary and retains no log data on the
   user's access beyond what is necessary for sound execution
   and infrastructure security.]

4. Contact
   [Contact person for any operational follow-up.]

[Signature block placeholder]
```

## Output skeleton: Path 1B (Art. 4(6) safeguards proposal)

Letter, Markdown. Length: typically one to two pages.

Structure:

```
[Data holder letterhead placeholder]

To: [Requesting user]
Date: [Date of response]
Subject: Article 4(6) trade-secret identification and proposed
         safeguards in response to your Article 4(1) request
         dated [request date]

1. The request and trade-secret identification
   [Identification of the user's request. Identification, with
   specificity, of the data within the requested scope that is
   protected as a trade secret within the meaning of Art. 2(1)
   of Directive (EU) 2016/943 and Art. 2(19) of the Data Act.
   The data will be flagged in the relevant metadata on
   disclosure.]

2. Confirmation of trade-secret status
   [Brief confirmation that, on the data holder's analysis,
   the identified data satisfies the Art. 2(1) TSD test:
   secret; commercial value because secret; reasonable steps
   to keep it secret. Where the trade-secret holder is a
   third party (e.g. licensor to the data holder), identify
   the trade-secret holder and confirm its participation in
   this step.]

3. Proposed safeguards
   [Proportionate technical and organisational measures the
   data holder considers necessary to preserve confidentiality:
   - [NDA / model contractual terms when published]
   - [Strict access protocols: named individuals only;
     two-factor authentication; audit logging]
   - [Technical measures: encryption at rest and in transit;
     contractual prohibition on copying or onward
     transmission outside the safeguard envelope]
   - [Code of conduct adherence where applicable]
   The data holder considers these proportionate in light of
   the data's sensitivity and the user's stated or apparent
   use.]

4. Invitation to agree
   [Invitation to the user to confirm acceptance, propose
   modifications, or raise questions. Disclosure will follow
   on agreement. If no agreement is reached, the data holder
   reserves the right to withhold or suspend sharing of the
   trade-secret-identified data under Art. 4(7).]

5. Non-trade-secret data
   [Where the request scope includes non-trade-secret data,
   the data holder is making that portion available
   immediately on the Art. 4(1) standard, by [channel].
   Trade-secret data follows the agreed safeguards.]

6. Redress
   [Information that the user, without prejudice to its right
   to seek redress before a court or tribunal of a Member
   State, may lodge a complaint under Art. 37(5)(b) or refer
   the matter to a dispute settlement body under Art. 10
   should agreement not be reached.]

[Signature block placeholder]
```

## Output skeleton: Path 1C (partial disclosure with scope exclusion)

The Path 1A letter, with an additional section.

```
[Add as section 2(a):]

2(a) Out-of-scope categories
     [The user's request included [specific category]. The
     data holder considers this category to fall outside the
     scope of Art. 4(1) on the following ground: [specific
     ground].
     - "Derived" data resulting from proprietary algorithms
       or substantial additional investment is out of scope
       per Recital 15.
     - Data that is not readily available within the meaning
       of Art. 2(17) (where production would require
       disproportionate effort or where the connected
       product's design does not support external storage or
       transmission).
     - Content data (textual, audio, audiovisual) typically
       covered by IP and outside Ch II per Recital 16.
     - Data generated before 12 September 2025 per
       Commission interpretation in FAQ Q4 and Q34a (framed
       as such).
     The data holder is available to discuss the scope
     analysis if the user disagrees.]
```

## Output skeleton: Path 2 (Art. 4(12) withholding pending legal basis)

Short response, Markdown. Length: typically half a page.

Structure:

```
[Data holder letterhead placeholder]

To: [Requesting user]
Date: [Date of response]
Subject: Article 4(12) personal-data condition in response to
         your Article 4(1) request dated [request date]

1. The request
   [Identification of the user's request and the personal-
   data component within it.]

2. Article 4(12) condition
   [Where the user is not the data subject whose personal
   data is requested, Art. 4(12) of the Data Act conditions
   disclosure on the existence of a valid legal basis for
   processing under Art. 6 of Regulation (EU) 2016/679
   (GDPR) and, where relevant, the conditions of Art. 9 of
   that Regulation and of Art. 5(3) of Directive 2002/58/EC
   (ePrivacy).]

3. Request for information
   [Request that the user identify its Art. 6(1) GDPR legal
   basis for receiving the personal data sought, the Art. 9
   GDPR condition where applicable, the Art. 5(3) ePrivacy
   condition where applicable, and a brief confirmation that
   the user has discharged its Art. 14 GDPR information
   obligations to affected data subjects. The data holder
   will not retain this information beyond what is necessary
   for the assessment.]

4. Non-personal data
   [Where the request scope includes non-personal data, the
   data holder is making that portion available immediately
   on the Art. 4(1) standard.]

5. Next steps
   [Once the user has provided the Art. 4(12) information,
   the data holder will make the personal-data component
   available on the Art. 4(1) standard, subject to
   trade-secret pre-disclosure identification under Art. 4(6)
   if any trade-secret content is in scope.]

[Signature block placeholder]
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 4(1), Art. 4(5), Art. 4(6), Art. 4(12) (always); Art. 4(7) (where moving toward stage 2); Art. 4(13), Art. 4(14) (data holder use restrictions); Art. 2(17) (readily available); Art. 7(1) (SME carve-out).
- `sources/regulation-2023-2854.md` Recitals 15 (derived data), 16 (content), 20 (readily available), 26-30 (operative on disclosure mechanics), 34 (user-as-controller).
- `sources/faq-v1-4.md` Q21 (manufacturer not always data holder), Q4 and Q34a (pre-application data out of scope), Q5a (edge-processing edge cases), Q13 (anonymisation does not transform raw into derived), framed as Commission interpretation.
- Directive (EU) 2016/943 (Trade Secrets Directive) Art. 2(1) (definition; pre-disclosure test).
- Regulation (EU) 2016/679 (GDPR) Art. 6, Art. 9 (legal basis and special-category conditions, for the Art. 4(12) referral).

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded if personal data in scope).
- `references/gates/trade-secrets-directive.md` (loaded if trade-secret content in scope).
- `references/gates/sectoral-lex-specialis.md` (warn-only).
- `references/gates/member-state.md` (warn-only, for the competent authority of establishment).
- `references/gates/dma-gatekeeper.md` (not applicable to Art. 4(1) responses; load only if the request is under Art. 5(1) and the response is being transposed).
- `references/gotchas.md` entries 2 (manufacturer not always data holder), 3 (user-not-data-subject is controller), 4 ("without undue delay" has no numeric SLA), 6 (trade-secret ladder), 19 (FAQ framing).
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `ch2-user-direct-request.md` (mirror card from the user's side).
- `ch2-trade-secret-stages-1-2.md` (downstream if Art. 4(6) safeguards fail or are escalated).
- `ch2-trade-secret-stage-3-refusal.md` (downstream if stage 2 also fails).
- `ch2-safety-security-handbrake.md` (alternative refusal regime if the gravamen is safety or security).

---

## Drafter notes

- **Identify trade secrets pre-disclosure, not on refusal.** The Art. 4(6) identification step is constitutive: data not identified as trade-secret pre-disclosure cannot ground a later stage 2 or stage 3 invocation in respect of that data. The first response to an Art. 4(1) request is the moment to do the identification; treating it as an afterthought is the most common operational failure on the data-holder side.
- **Do not skip Art. 4(12) silently.** Where the user is an enterprise and personal data is in scope, the legal-basis confirmation is required. Disclosing the personal-data component without the confirmation is a GDPR exposure on the data holder's side independent of the Data Act. Path 2 above is the structured pause; use it rather than disclosing on assumption.
- **Latency calibration.** "Without undue delay" is fact-specific. For a self-service portal release, a few business days is the operational expectation. For a real-time channel setup, two to four weeks is often reasonable. Document the rationale internally; the competent authority looks at the response timing when complaints arrive.
