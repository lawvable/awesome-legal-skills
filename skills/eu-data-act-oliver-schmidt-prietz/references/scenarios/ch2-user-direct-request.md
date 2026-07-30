# ch2-user-direct-request

**Anchor:** User × Ch II × Art. 4(1) request preparation. The user (or counsel for the user) prepares the Art. 4(1) data access request to the data holder. Direct user-to-data-holder route, no third party involved. The card covers identity-verification expectations, scope drafting, format and latency expectations, and the pre-emptive trade-secret-safeguard posture.

**Routes from:**

- "Draft our Art. 4(1) request to the manufacturer."
- "What do we put in a Data Act access request?"
- "We want to retrieve our connected-product data. How do we ask?"
- "What is the data holder allowed to ask us to prove before responding?"
- "What format are we entitled to under Art. 4(1)?"

**Adjacent cards (route there instead if the facts indicate):**

- The user wants the data sent to a third party (e.g. an aftermarket service provider): `ch2-user-third-party-request.md` (Art. 5(1) route).
- The data holder has responded and refused: `ch2-trade-secret-stages-1-2.md` and downstream `ch2-trade-secret-stage-3-refusal.md`, or `ch2-safety-security-handbrake.md` if the refusal is grounded in safety or security.
- The user is reviewing the data holder's pre-contract disclosure before contracting: `ch2-pre-contract-transparency.md`.
- The data holder is preparing the response from its side: `ch2-data-holder-response.md`.

---

## Canonical fact pattern

A user (natural or legal person) has a connected product or related service in use. The data the user wants is not directly accessible from the product or service (so the Art. 3(1) direct-access default does not satisfy the need), and the user invokes the Art. 4(1) right to require the data holder to make readily available data available without undue delay.

The data sought is typically a mix of product data and related service data. The contract may or may not have been concluded after 12 September 2025; the Art. 4(1) right applies regardless of contract date for data generated after the date of application (per Commission interpretation in FAQ Q4, framed as such). The user has identity, contract reference, and a sense of which data categories it wants. It does not yet have a written request to send.

---

## Critical disciplines

- **Art. 4(5) caps the data holder's verification ask.** A data holder may not require the user to provide any information beyond what is necessary to verify that the person making the request qualifies as a user. Excessive identity-verification demands (proof of identity beyond what the contract supplies, written declarations of intended use, evidence of need) are prohibited. The user should pre-empt this by including only the information the data holder genuinely needs to identify the user and the product or service.
- **Format and quality entitlement.** Art. 4(1) entitles the user to data "of the same quality as is available to the data holder, easily, securely, free of charge, in a comprehensive, structured, commonly used and machine-readable format and, where relevant and technically feasible, continuously and in real-time." The data holder cannot downgrade format, redact for convenience, or charge the user. Continuous and real-time access is conditioned on technical feasibility.
- **Trade-secret pre-emption.** Where the user knows or expects that the requested data will include trade-secret-protected material, the request should signal a stage-1 safeguard posture (Art. 4(6)) from the outset. A user that pre-emptively offers proportionate safeguards (NDA, model contractual terms, technical measures) narrows the data holder's space to escalate to stage 2 withholding or stage 3 refusal. Failure to engage on safeguards is itself a stage-2 ground (Art. 4(7)).
- **Art. 4(10) prohibition on competing-product development.** The user cannot use the data to develop a competing connected product or share for that intent, and cannot use the data to derive insights about the manufacturer or data holder's economic situation, assets, or production methods. The request need not narrate the user's purposes, but the user's downstream use is constrained even if the request is silent.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check, Art. 1(6) carve-outs, and the Art. 2(22) placement test. Check Art. 2(5) "connected product" three limbs and Art. 2(6) "related service" test (bidirectional data exchange AND impact on connected-product behaviour, per FAQ Q10 framing). Check the temporal scope under Art. 50: data generated after 12 September 2025 is in scope of the Art. 4(1) right even where the connected product was placed on the market before that date (FAQ Q4 and Q34a, framed as Commission interpretation).

### Step 2: Chapter identification

Chapter II. Art. 4(1) is the operative user-access right. The request engages Art. 4(5) (verification limits), Art. 4(6)-(8) (trade-secret ladder if applicable), Art. 4(10)-(11) (user obligations), Art. 4(12) (personal data legal-basis condition where the user is not the data subject), Art. 4(13)-(14) (data holder use restrictions). If the user is also evaluating whether to direct disclosure to a third party, that route runs under Art. 5(1) and is a different card.

### Step 3: Role mapping

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| User (natural or legal person) | User (Art. 2(12)) | Data subject if a natural person and the data relates to them. Controller if an enterprise (Recital 34); the user must have a valid Art. 6 GDPR legal basis to receive personal data of third-party data subjects | If an enterprise user receives data, it may become a data holder for downstream onward sharing |
| Data holder | Data holder (Art. 2(13)) | Controller, typically | May be trade-secret holder under Directive (EU) 2016/943 |
| Affected data subjects (if user is an enterprise and data includes personal data of employees, customers, or other natural persons) |  | Data subjects |  |
| Manufacturer (if different from the data holder) | May not be the data holder; the data-holder role attaches to whoever controls access to readily available data (FAQ Q21) |  |  |

Recital 34: "Where the user is not the data subject but an enterprise, including a sole trader, and not in cases of shared household use of the connected product, the user is considered to be a controller." That controller status crystallises on the user's exercise of the Art. 4(1) right for personal data. The user must, before sending the request, identify its Art. 6 GDPR legal basis for receiving the personal data. The data holder cannot disclose personal data to the user otherwise (Art. 4(12)). See `references/gotchas.md` entry 3.

### Step 4: Fact-category sorting

Card-specific dimensions to sort the request against.

- **In-scope vs out-of-scope data.** Only readily available data (Art. 2(17)) is in scope. Inferred or derived data (Recital 15) is out of scope. The request should describe categories the user reasonably believes are in scope; descriptions of "all data" risk being treated as scope-stretching.
- **Personal vs non-personal.** Drives the Art. 4(12) legal-basis check where the user is not the data subject. Mixed datasets (Recital 7) trigger GDPR for the personal-data component.
- **Trade-secret data vs not.** Where the user knows trade-secret-protected data is likely in scope (e.g. sensor calibration data, proprietary algorithm outputs that may have been mistakenly classified as raw or pre-processed), the user should anticipate the Art. 4(6) safeguards conversation.
- **Connected-product data vs related service data.** Both are in scope; the request should not artificially restrict itself to one category if both are sought.
- **Real-time vs historical.** Art. 4(1) covers both. The user should distinguish: historical data has a one-time pull profile; real-time data needs an ongoing access channel and is conditioned on "where relevant and technically feasible".

### Step 5: Limb-by-limb application of Art. 4(1) and Art. 4(5)

Art. 4(1) imposes obligations on the data holder. The user's request is well-drafted when it tracks those obligations and leaves no room for the data holder to claim ambiguity. The cumulative entitlement is:

1. **Readily available data.** Art. 2(17). The data the data holder can lawfully obtain without disproportionate effort. The request need not prove readiness; the data holder bears the burden of justifying a refusal on readily-available grounds.
2. **Relevant metadata.** Art. 4(1). The request should expressly include metadata necessary to interpret and use the data; do not assume it is implicit.
3. **Without undue delay.** Art. 4(1). The user does not state a deadline because "without undue delay" has no numeric SLA (`references/gotchas.md` entry 4). If the user has operational urgency, it should narrate the urgency in the request rather than impose a number the regulation does not.
4. **Same quality as is available to the data holder.** The data holder cannot downgrade resolution, sampling rate, or precision.
5. **Easily, securely, free of charge.** Free of charge is a flat entitlement under Art. 4(1) for the user-to-data-holder route. (Charge may apply to third-party recipients under Art. 9 in the Art. 5 route, but not on Art. 4.)
6. **Comprehensive, structured, commonly used, and machine-readable format.** CSV, JSON, XML, Parquet, or a domain-specific structured format. PDFs of tables are not machine-readable in the regulation's sense. Lossy aggregation is not comprehensive.
7. **Continuously and in real-time, where relevant and technically feasible.** Conditional. If the user wants a real-time channel, the request should say so and ask the data holder to confirm technical feasibility.
8. **Simple request through electronic means where technically feasible.** Art. 4(1) final sentence. The user is entitled to a low-friction request channel; the data holder cannot insist on paper or in-person processes if electronic is feasible.

Art. 4(5) sets the verification ceiling. The data holder may ask only what is necessary to verify the user's status as user. Acceptable demands typically include: identification matching the contract counterparty, the contract reference or product identifier, and (where the user is an enterprise) the natural person authorised to act on the user's behalf. Unacceptable demands include: declarations of intended purpose, evidence of need or detriment, attestations beyond identity, and retention of log data on the user's access beyond what is necessary for sound execution and infrastructure security.

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. Two cases:
  - **User is the data subject.** Art. 4(1) and GDPR Art. 15 are parallel rights; the user-data-subject can rely on either or both. The Data Act right is typically broader in respect of non-personal product and related service data the data subject would not access under GDPR.
  - **User is not the data subject (enterprise user).** The user must have a valid Art. 6 GDPR legal basis (and where relevant Art. 9 conditions and Art. 5(3) ePrivacy conditions) for the personal data it receives. Art. 4(12) conditions the data holder's disclosure on the user having that basis; the request should state the basis and, where relevant, confirm the user's compliance with Art. 14 GDPR information obligations toward affected data subjects.
- **Trade Secrets Directive overlay (loaded if trade-secret data anticipated in scope).** Read `references/gates/trade-secrets-directive.md`. Where the user anticipates trade-secret content, it pre-emptively proposes Art. 4(6) safeguards in the request: an NDA, model contractual terms (if published), specified technical and organisational measures. Pre-empting strengthens the user's position if the data holder escalates to stage 2 or 3.
- **DMA gatekeeper (not applicable on this card).** Art. 5(3) excludes gatekeepers as eligible Art. 5 third parties; Art. 4(1) is the user's direct right and is not affected. If the user is a gatekeeper exercising its own Art. 4(1) right for its own use, Art. 5(3) does not bite, but downstream use limits remain.
- **Sectoral lex specialis (warn-only).** Run `references/gates/sectoral-lex-specialis.md` if the connected product is in a regulated sector. Several sectoral regimes carry their own access rights (e.g. vehicle in-vehicle data initiatives) that may layer with Art. 4(1).
- **Member State implementing law (warn-only).** Run `references/gates/member-state.md` for the competent authority designation, used in the redress paragraph of the request.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 4(1) of Regulation (EU) 2023/2854 (Data Act) is the operative right. Verbatim text at `sources/regulation-2023-2854.md` Art. 4(1); operative recitals at Recitals 26-30. Temporal applicability: 12 September 2025 for the access right; data generated before that date is out of scope per Commission interpretation in FAQ Q4 and Q34a.
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final does not propose substantive amendments to Art. 4(1) or Art. 4(5). Proposed amendments to Art. 4(8) (new third-country misuse refusal ground) are relevant downstream if the data holder refuses. See `sources/digital-omnibus-amendments-tracker.md`.

---

## Decision point

After Steps 5 and 6, the analysis yields one of three paths.

1. **Request can be drafted as posed.** Produce the request letter (Output Path 1 below). Adjust for trade-secret pre-emption where appropriate.
2. **Request needs scope reduction before drafting.** The user has asked for data that is out of scope (derived data, pre-application data, content outside Recital 16) or data that does not exist in readily available form. Produce a scoped request that drops the out-of-scope categories and explain the reduction (Output Path 2 below).
3. **Request blocked on Art. 4(12) personal data.** The user is an enterprise, the data sought includes personal data of natural persons other than the user, and the user has not yet identified its GDPR legal basis. Stop and resolve the legal-basis question before the request is sent. The data holder will refuse on Art. 4(12) grounds otherwise.

---

## Output skeleton: Path 1 (Art. 4(1) request letter)

Formal letter, Markdown by default. Length: typically one page.

Structure:

```
[User letterhead placeholder]

To: [Data holder, full legal entity name and registered address]
Date: [Date of request]
Subject: Request for access to data under Article 4(1) of
         Regulation (EU) 2023/2854 (Data Act)

1. User identification
   [Legal name, address. Contract reference or product
   identifier(s). Authorised contact person and their role,
   where the user is an enterprise.]

2. Connected product and/or related service
   [Identification of the in-scope connected product (model,
   serial number, identifier) and/or related service (name,
   subscription identifier). Date placed on the market or
   contract conclusion date where relevant.]

3. Data requested
   3(a) Categories. [Specific data categories. Avoid "all data";
        identify by category, source, sensor, log, or service
        function. Include relevant metadata (per Art. 4(1)).]
   3(b) Temporal range. [Specific period, e.g. "from
        [start date] to [end date]" or "ongoing from
        [start date]". For real-time access, state the
        operational profile.]
   3(c) Format. [Specific machine-readable format: CSV, JSON,
        Parquet, or other. State the preferred format and
        request that the data holder confirm any technical
        constraint that would require an alternative.]
   3(d) Delivery channel. [Electronic. Specific channel: secure
        download portal, API endpoint, secure file transfer.
        If the data holder operates a self-service portal, ask
        that it be used.]

4. Identity verification (Art. 4(5))
   [The user is willing to provide the following to verify its
   status as user: [list]. The user understands that the data
   holder may not require information beyond what is necessary
   for that verification and may not retain log data beyond
   what is necessary for sound execution and infrastructure
   security.]

5. Personal data and legal basis (Art. 4(12)) [include only if
   the user is an enterprise and personal data of other
   natural persons is in scope]
   [The user, in its capacity as controller under Recital 34
   for personal data generated by the connected product or
   related service relating to persons other than the user,
   relies on the following Art. 6(1) GDPR legal basis for
   processing the personal data sought: [legal basis,
   e.g. Art. 6(1)(b) performance of contract; Art. 6(1)(f)
   legitimate interests as documented in [reference];
   Art. 6(1)(a) consent of the data subjects as recorded in
   [reference]]. Where Art. 9 GDPR conditions apply: [state
   the Art. 9(2) condition]. The user has discharged its
   Art. 14 GDPR information obligations to affected data
   subjects.]

6. Trade-secret safeguards (Art. 4(6)) [include only if trade-
   secret content is anticipated]
   [The user understands that, where the requested data
   includes trade-secret-protected material, Art. 4(6)
   requires the parties to agree proportionate technical and
   organisational measures prior to disclosure. The user is
   willing to enter into [NDA / model contractual terms when
   published / specified safeguards] and invites the data
   holder to identify the trade-secret-protected data and
   propose safeguards.]

7. Format and quality entitlement
   [The user confirms that, under Art. 4(1), it is entitled
   to receive the data of the same quality as is available
   to the data holder, easily, securely, free of charge, in a
   comprehensive, structured, commonly used, and machine-
   readable format, and, where relevant and technically
   feasible, continuously and in real-time.]

8. Redress
   [If the data holder withholds or suspends the data sharing
   under Art. 4(7), or refuses under Art. 4(8), the user
   reserves the right to lodge a complaint under Art. 37(5)(b)
   with the competent authority of [Member State] designated
   pursuant to Art. 37, and/or to refer the matter to a
   dispute settlement body under Art. 10, and/or to seek
   redress before a court or tribunal of a Member State.]

[Signature block placeholder]
```

## Output skeleton: Path 2 (scope-adjusted request)

The same letter structure as Path 1, with a section added explaining the scope adjustment.

```
[Add as section 3(e):]

3(e) Scope clarification
     [The user initially considered requesting [original
     scope]. On review, the user has narrowed the request
     because [stated reason: derived data out of scope per
     Recital 15; data generated before 12 September 2025 out
     of scope per Commission interpretation in FAQ Q4 framed
     as such; content data out of scope per Recital 16; or
     other]. The user reserves the right to revisit the
     scope if the data holder takes the position that the
     additional categories are in scope.]
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 4(1), Art. 4(5), Art. 4(10), Art. 4(11), Art. 4(12) (always); Art. 4(6) and Art. 4(7) (where trade-secret content anticipated); Art. 4(9) (redress).
- `sources/regulation-2023-2854.md` Art. 37(5)(b), Art. 38(1), Art. 10 (redress paragraph).
- `sources/regulation-2023-2854.md` Recital 30 (broad lawful-purpose framing), Recital 34 (user-not-data-subject controller), Recital 15 (derived data exclusion), Recital 16 (content exclusion), Recital 20 (readily available).
- `sources/faq-v1-4.md` Q4 (data generated before 12 September 2025), Q21 (manufacturer is not always data holder), Q34a (pre-application data), framed as Commission interpretation.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded if personal data in scope).
- `references/gates/trade-secrets-directive.md` (loaded if trade-secret content anticipated).
- `references/gates/sectoral-lex-specialis.md` (warn-only).
- `references/gates/member-state.md` (warn-only, for the redress paragraph).
- `references/gotchas.md` entries 2 (manufacturer not always data holder, drives whom to address), 3 (user-not-data-subject is controller, drives Art. 4(12) section), 4 ("without undue delay" has no numeric SLA, do not impose one), 6 (trade-secret ladder).
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `ch2-data-holder-response.md` (the mirror card from the data holder's side).
- `ch2-user-third-party-request.md` (Art. 5(1) variant where the user wants disclosure to a third party).

---

## Drafter notes

- **Address the right entity.** The data holder is whoever controls access to readily available data, not necessarily the manufacturer (FAQ Q21, framed as Commission interpretation). For a connected vehicle, the data holder may be the manufacturer, a fleet-management contractor, or a related service provider, depending on the architecture. Identify the right entity before the request goes out; a request to the wrong entity will be redirected at best and ignored at worst.
- **Real-time access is conditional.** If the user genuinely needs a continuous real-time feed, the request should narrate why and ask the data holder to confirm technical feasibility under Art. 4(1). Where the data holder responds that real-time is not feasible, the user is entitled to periodic snapshots at the data holder's lowest natural latency.
- **Pre-empt the trade-secret conversation.** Where the user expects trade-secret content (e.g. proprietary sensor outputs, calibration matrices), proposing safeguards in the initial request prevents the data holder from using the absence of safeguards as a stage-2 ground under Art. 4(7). Even where no trade secrets are anticipated, a willingness-to-engage paragraph forecloses one common refusal route.
