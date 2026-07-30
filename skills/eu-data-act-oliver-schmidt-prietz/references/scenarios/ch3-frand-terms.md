# ch3-frand-terms

**Anchor:** Data holder × Ch III × Art. 8 FRAND. The horizontal contract-terms framework that governs whenever a data holder is obliged (by Art. 5 or by other Union or national law) to make data available to a data recipient. Most Ch III drafting starts here, because Art. 8 sets the substantive bar for the arrangements before Art. 9 sets the price.

**Routes from:**

- "Draft the data-sharing terms our Ch III obligation requires us to offer."
- "How do we structure FRAND access to this dataset for a downstream recipient?"
- "A recipient says our access conditions are discriminatory. How do we respond?"
- "We have a mandatory sharing obligation under [sectoral instrument]. What contract terms can we impose?"
- "Are these access conditions compliant with Art. 8?"

**Adjacent cards (route there instead if the facts indicate):**

- Recipient is challenging the price specifically, not the terms: `ch3-compensation-challenge.md`.
- The dispute is unfairness of a unilaterally imposed term in a B2B contract under Art. 13: `ch4-unfairness-challenge.md`.
- The data holder is considering withholding on trade-secret grounds rather than agreeing terms: `ch2-trade-secret-stages-1-2.md` (the Ch II ladder applies to the trade-secret data; Ch III still governs the commercial terms for the data that is shared).
- The data recipient is a DMA-designated gatekeeper acting under Art. 5: `ch2-art5-third-party.md` (not yet drafted; gatekeepers are excluded as Art. 5 third parties under Art. 5(3)).

---

## Canonical fact pattern

A data holder is obliged to make data available to a data recipient in a business-to-business relationship. The obligation arises either from a user request under Art. 5 of the Data Act, or from a separate Union or national law sharing obligation that engages Ch III by reference (Art. 12(1)). The parties are negotiating, or are about to negotiate, the contract that will govern the arrangements for making the data available.

The data holder typically wants to maximise compensation, retain control over scope and use, and avoid setting precedent that other recipients will invoke under the non-discrimination duty. The data recipient typically wants predictable access, transparent pricing, and protection against terms that would hollow out the access right. Both sides are operating against an Art. 13 unfairness backstop that survives any FRAND-compliant drafting (Art. 8(2)).

The data is typically mixed: some categories may be trade-secret-protected (engaging Art. 8(6) and the Ch II ladder), some may be personal (engaging the GDPR overlay), some readily available and some not.

---

## Critical disciplines

These three are the load-bearing disciplines for Art. 8 drafting. Hold all three.

- **Direction of compensation is recipient-to-holder.** Ch III is asymmetric. The data recipient pays the data holder for making the data available. Drafts that reverse the flow (treating the holder as paying a fee, or as obliged to provide free of charge unless an exception applies) misstate the basic economics. The exceptions to compensation are Art. 9(4) (SME or not-for-profit research recipient: cost only, no margin) and Art. 9(6) (lower or no compensation under other Union or national law). See `references/gotchas.md` entry 15.
- **FRAND is four duties, not a slogan.** Art. 8(1) imposes fair, reasonable, non-discriminatory, AND transparent. They are cumulative and each has independent operative content. A term may be reasonable in the abstract and still discriminatory between comparable recipients (Art. 8(3)), or transparent and still unfair (Art. 13 overlay). The four duties need to be tested separately.
- **Art. 13 unfairness is not displaced by Art. 8 compliance.** Art. 8(2) is express: a contractual term concerning data access and use, or liability and remedies for breach of data-related obligations, is not binding if it is unfair within the meaning of Art. 13 or if it derogates from a user's Ch II rights. Drafting FRAND-compliant terms does not pre-empt the Art. 13 black-list and grey-list; both regimes apply in parallel to the same contract.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check, Art. 1(6) carve-outs (criminal law enforcement, customs, taxation, national security, voluntary private-public arrangements, specified Union law instruments). For the Ch III trigger specifically, confirm there is an obligation to make data available, either under Art. 5 or under another Union or national law instrument. Without an obligation, Ch III does not engage; voluntary sharing remains free of Art. 8 constraints (Recital 42, last sentence: "Voluntary data sharing remains unaffected by those rules").

Confirm the temporal hook. Chapter III applies to obligations under EU or national law that enter into force after 12 September 2025 (Art. 50, fourth sub-paragraph). Sharing obligations under instruments in force before that date are not in Ch III scope; the contract terms then sit outside the Art. 8 framework.

### Step 2: Chapter identification

Chapter III. Art. 8 governs the conditions and Art. 9 governs the compensation. Art. 10 supplies the dispute settlement route. Art. 12(1) is the scope-of-application provision that brings third-party sharing obligations (under Union or national law) within Ch III.

Where Art. 5 (user-directed third-party sharing) is the trigger, both Ch II and Ch III engage. Ch II governs the rights of the user and the third party; Ch III governs the commercial terms between the data holder and the data recipient. The chapters interact, they do not displace each other.

Where Ch IV unfairness is alleged on a specific term, the analysis runs in parallel under Art. 13 (see `ch4-unfairness-challenge.md`). Art. 8(2) cross-refers explicitly.

### Step 3: Role mapping

Required entity-by-entity mapping. Show as a table in the output.

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Data holder | Data holder (Art. 2(13)) | Controller, typically | Possibly trade-secret holder under Directive (EU) 2016/943 and Art. 2(19) Data Act for some data categories |
| Data recipient | Data recipient (Art. 2(14)) | Controller if receiving personal data; or processor if receiving as service provider on behalf of the user |  |
| User (if Art. 5 is the trigger) | User (Art. 2(12)) | Controller under Recital 34 if not the data subject (`references/gotchas.md` entry 3); data subject if a natural person |  |
| Affected data subjects (if user or recipient is an enterprise) |  | Data subjects |  |

Where the data recipient is an SME or not-for-profit research organisation, flag this on the role mapping line; it changes the Art. 9(4) calculation (cost only, no margin). The Art. 9(4) carve-out has its own qualifying tests (no non-SME partner or linked enterprise; see Art. 9(4)) which are reviewed on the facts.

### Step 4: Fact-category sorting

Card-specific dimensions to sort the data against. Several feed directly into Art. 8 and Art. 9.

- **Trade-secret data vs not.** Triggers the Art. 8(6) carve-out: an obligation to make data available under Art. 8 "shall not oblige the disclosure of trade secrets" unless Union law provides otherwise (including Art. 4(6) and Art. 5(9), which authorise disclosure with safeguards). Where Art. 5 is the trigger, the Ch II ladder applies to the trade-secret data; Art. 8 still governs the commercial terms for any data that is shared (with safeguards).
- **Personal vs non-personal.** Drives the GDPR overlay (Art. 1(5) bridge). Mixed datasets (Recital 7) require the personal-data component to be processed on a valid GDPR legal basis; the data recipient's role as controller or processor is itself a contractual term that needs explicit treatment.
- **Volume, format, nature.** Art. 9(3) permits compensation to depend on these. Sorting the data into volume-bands and format-categories is a precondition for an Art. 9-compliant pricing structure.
- **Cost basis.** Art. 9(2)(a) directs costs incurred in making the data available (formatting, dissemination via electronic means, storage). Art. 9(2)(b) directs investments in collection and production. These are the two cost lines that feed compensation; the holder needs to identify both with sufficient detail to satisfy Art. 9(7).
- **Comparator categories of recipients.** Art. 8(3) non-discrimination is tested against comparable categories of recipients. The data holder needs to identify which categories of recipients it serves on what terms, because the data holder bears the burden of showing non-discrimination on a reasoned request (Art. 8(3) second sentence).

### Step 5: Limb-by-limb application of Art. 8

Art. 8(1) decomposes into four substantive duties plus the Chapter IV cross-reference. Each is independent.

1. **Fair.** Not defined positively in the regulation. Recital 61 anchors fairness against "grossly deviating from good commercial practice" for the Art. 13 unfairness test; the Art. 8 fairness duty is in the same spirit but operates at the contract-formation stage, not as an ex-post invalidation. A fair term is one that does not abuse the data holder's structural position vis-a-vis the recipient. Specific Art. 13 unfairness checks run separately at Step 5 of any Ch IV analysis.
2. **Reasonable.** Reasonableness applies both to non-price terms and to the price. For price, Art. 9(1) and 9(2) supply the operative content. For non-price terms, reasonableness reads against the legitimate interests of both parties: the holder's investment recovery and continued data generation (Recital 46), and the recipient's effective access to the value of the data (Recital 47).
3. **Non-discriminatory.** Art. 8(3). The holder shall not discriminate between comparable categories of data recipients, including partner or linked enterprises. On a reasoned request, the holder must without undue delay provide the recipient with information showing there has been no discrimination. The burden of proof rests on the data holder once the recipient has raised a reasoned challenge (Recital 45). Differentiation justified by objective reasons is not discrimination (Recital 45 third sentence).
4. **Transparent.** Art. 8(1) imposes transparency as a free-standing duty. Art. 9(7) gives it operative content for compensation: the holder shall provide the recipient with information setting out the basis for calculating the compensation in sufficient detail so that the recipient can assess compliance with Art. 9(1)-(4). For non-price terms, transparency means clear disclosure of access conditions, permitted-use scope, and any technical or organisational measures the recipient must implement.
5. **Art. 13 unfairness backstop (Art. 8(2)).** A contractual term concerning data access and use, or liability and remedies for breach or termination of data-related obligations, is not binding if it is unfair within the meaning of Art. 13. Drafting FRAND-compliant terms does not exhaust the Art. 13 check; the black-list at Art. 13(4) and grey-list at Art. 13(5) apply in parallel. Run them.
6. **Art. 8(4) user request precondition.** A data holder shall not make data available to a data recipient (including on an exclusive basis) unless requested to do so by the user under Ch II. Where the Ch III trigger is Art. 5, this is satisfied by the user's request itself. Where the Ch III trigger is another Union or national law, the obligation arises by force of that law rather than user request; the Art. 8(4) restriction applies to Art. 5 sharing specifically and does not bar sharing mandated by other instruments.
7. **Art. 8(5) information minimisation.** Neither side is required to provide information beyond what is necessary to verify compliance with the contractual terms or with the Regulation or other applicable Union or national law. This caps the holder's disclosure obligation under Art. 8(3) and Art. 9(7), and caps the recipient's reporting obligations under any audit or compliance term.
8. **Art. 12(2) anti-derogation.** A contractual term derogating from Ch III, varying its effect, or excluding its application, to the detriment of one party (or the user where applicable), is not binding. Includes contractual choice-of-law clauses purporting to lift the contract out of Ch III scope.

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. The data recipient typically becomes the controller (or processor on behalf of the user) for the personal data it receives; the contract must record this and the corresponding legal basis. Where the user under Art. 5 is not the data subject, Art. 4(12) and 5(7) condition disclosure on a valid GDPR legal basis (see `references/gotchas.md` entry 3).
- **Trade Secrets Directive overlay (loaded if any data is claimed as trade-secret).** Read `references/gates/trade-secrets-directive.md`. Art. 8(6) does not require disclosure of trade secrets; where the data holder agrees to share trade-secret data, Art. 4(6) / 5(9) safeguards apply, and the FRAND terms must accommodate those safeguards (confidentiality, access restrictions, technical and organisational measures). The compensation under Art. 9 may include the costs of implementing those safeguards.
- **DMA gatekeeper exclusion (warn-only on this card).** Art. 5(3) excludes gatekeepers as eligible third parties under Art. 5. Where the Ch III trigger is Art. 5 and the recipient is or acts for a DMA-designated gatekeeper, the sharing is not lawful at all; the Art. 8 drafting is moot. Run `references/gates/dma-gatekeeper.md` before producing output. Where the Ch III trigger is another Union or national law (not Art. 5), the gatekeeper exclusion does not directly engage; sectoral law may provide its own restrictions.
- **Sectoral lex specialis (warn-only).** Where the obligation to share arises from a sectoral instrument (financial-services data, vehicle telematics, health data, energy data, agricultural data), the sectoral instrument is the primary source of the sharing obligation and Ch III is the horizontal layer over it. Art. 9(6) explicitly allows other Union or national law to exclude compensation or provide for lower compensation. Run `references/gates/sectoral-lex-specialis.md` to identify any sectoral overlay.
- **Member State implementing law (warn-only).** Dispute settlement bodies under Art. 10 are certified at Member State level. Run `references/gates/member-state.md` to confirm which body is competent and whether the Member State has notified Art. 37 competent authorities.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 8 and Art. 9 of Regulation (EU) 2023/2854 (Data Act) govern, with Art. 10 dispute settlement available. Verbatim text at `sources/regulation-2023-2854.md` Art. 8 (lines 778-798) and Art. 9 (lines 800-825); operative recitals at Recitals 42-51.
- **Proposed amendment under Digital Omnibus.** COM(2025) 833 final (19 November 2025) does not materially alter Art. 8 or Art. 9 in respect of the FRAND framework itself. The Commission has signalled the forthcoming Art. 9(5) guidelines on calculating reasonable compensation (FAQ Q72: expected Q2/Q3 2026, not adopted as of May 2026). See `references/gotchas.md` entry 16 and `sources/digital-omnibus-amendments-tracker.md`.

The output cites current law as operative. The forthcoming Art. 9(5) guidelines are flagged but not relied on.

---

## Decision point

After Steps 5 and 6, the analysis yields one of three paths.

1. **All four Art. 8(1) duties drafted and the cross-regime gates clear.** Produce the FRAND-compliant data-sharing terms (Output Path 1 below).
2. **A specific term fails the Art. 13 backstop.** Identify the failing term and re-draft it. The card produces a redline (Output Path 2 below) rather than the full agreement.
3. **The Ch III trigger is absent.** Where there is no Art. 5 request and no other Union or national law obligation to share, Ch III does not apply. The arrangement is voluntary (Recital 42); the parties contract freely without the Art. 8 framework. The card produces a short note explaining the absence of trigger and routes the user to standard contract drafting.

---

## Output skeleton: Path 1 (FRAND-compliant data-sharing terms)

Drafting input, Markdown by default, structured as the operative clauses for a data-sharing agreement. Length: typically 2 to 4 pages depending on data complexity. The user adapts to its own template.

Structure:

```
DATA-SHARING AGREEMENT (Ch III COMPLIANT)

Parties:
  Data Holder: [legal entity]
  Data Recipient: [legal entity]

Recital A: Trigger for sharing
  [Identification of the obligation. Either: (i) Art. 5 request by user
  [user identity, date]; or (ii) [Union or national law instrument]
  imposing the sharing obligation, citation, effective date.]

Recital B: Categorisation of data
  [Brief description of data categories in scope, separated as
  trade-secret / non-trade-secret, personal / non-personal, raw or
  pre-processed / out-of-scope-derived. Detailed schedule attached.]

1. Scope of data made available
   [Specific data categories. Cross-reference to schedule. Statement
   of exclusions (derived data; data not readily available; data
   covered by Art. 4(6) / 5(9) safeguards under separate annex).]

2. Conditions of access (Art. 8(1))
   2.1 Fair: [description of access modalities. Avoid take-it-or-leave-it
       drafting on non-essential terms.]
   2.2 Reasonable: [permitted use scope. Restrictions read against
       Art. 6(2) where the recipient is an Art. 5 third party.]
   2.3 Non-discriminatory: [statement that the terms are offered to all
       comparable categories of recipients on the same basis;
       identification of any objective reasons for differentiation that
       the holder relies on.]
   2.4 Transparent: [disclosure of the basis for the conditions in
       sufficient detail for the recipient to verify compliance.]

3. Compensation (Art. 9)
   3.1 Compensation: [amount and structure. Recipient pays holder.]
   3.2 Basis of calculation (Art. 9(2)): [costs incurred in making the
       data available, including formatting, dissemination, storage
       (point (a)); investments in collection and production (point (b))
       where applicable.]
   3.3 Dependence on volume, format, nature (Art. 9(3)): [where the
       pricing varies by these factors, the variation is specified.]
   3.4 SME / not-for-profit research recipient (Art. 9(4)): [if the
       recipient qualifies, the compensation does not exceed the
       Art. 9(2)(a) cost base; no margin. Statement of qualifying
       criteria. If the recipient does not qualify, this clause is
       inapplicable; record that explicitly.]
   3.5 Transparency of calculation (Art. 9(7)): [the holder provides
       the recipient with the cost-and-margin breakdown in sufficient
       detail for the recipient to assess compliance with Art. 9(1)-(4).
       Schedule attached.]

4. Non-discrimination challenge procedure (Art. 8(3))
   [On a reasoned request by the recipient that the terms are
   discriminatory, the holder provides without undue delay information
   showing no discrimination, including identification of comparator
   recipients and any objective reasons for differentiation.]

5. Trade-secret safeguards (Art. 8(6), Art. 4(6) or 5(9) where the
   trigger is Art. 5)
   [Identification of trade-secret data. Technical and organisational
   safeguards (confidentiality; access protocols; technical standards).
   Cross-reference to a separate confidentiality annex if needed.]

6. Use restrictions
   [Permitted purposes. Where the trigger is Art. 5, recall that the
   recipient is bound by Art. 6 restrictions (no profiling beyond
   strict necessity; no onward sharing without user contract; no use
   to develop a competing connected product; etc.). Avoid drafting
   that purports to displace Art. 6.]

7. Term, renewal, termination
   [Reasonable notice, no unreasonably short termination. Avoid the
   Art. 13(5)(f) grey-list trap (termination at unreasonably short
   notice).]

8. Liability and remedies
   [Symmetrical, non-discriminatory. Avoid Art. 13(4)(a) (exclude
   liability for intentional or gross negligence) and 13(4)(b)
   (exclude remedies for non-performance). Draft these by reference to
   ordinary contract principles, not as one-sided exclusions.]

9. Dispute settlement (Art. 10)
   [Reference to Art. 10 certified dispute settlement body as an
   option for the parties, without prejudice to court or tribunal
   recourse. Specify a Member State whose dispute body is certified
   if the parties want a defined forum.]

10. Anti-derogation (Art. 12(2))
    [Statement that no term of this agreement derogates from Ch III
    or Ch II rights to the detriment of either party or the user.
    Severability clause carries the standard Art. 13(7) result for
    any term later found unfair.]

Schedules:
  - Data schedule (categorisation by trade-secret / personal /
    readily available)
  - Compensation calculation (cost lines, margin if any, volume
    bands)
  - Trade-secret safeguards annex (if applicable)
```

---

## Output skeleton: Path 2 (redline of failing term)

Short response. Markdown. Quote the failing term, identify the failure under Art. 8 or Art. 13, propose amended language.

Structure:

```
The following term in the proposed data-sharing agreement is not
binding as drafted under Art. 8(2) of Regulation (EU) 2023/2854 (Data
Act):

> [Quote the failing term verbatim from the draft.]

The failure is [Art. 13(4)(N) / Art. 13(5)(N) / Art. 8(3)
non-discrimination / Art. 9(4) SME compensation cap / etc.]. [One- or
two-sentence explanation of why the term fails on the regulation's
operative text, with citation.]

Proposed amended language:

> [Replacement clause that addresses the failure while preserving the
> data holder's legitimate commercial interest where possible.]

The amendment cures the specific defect. Other terms of the draft
agreement remain to be reviewed against the full Art. 8 / Art. 13
matrix. See `Output Path 1` for the complete checklist.
```

---

## Output skeleton: Path 3 (no Ch III trigger)

Very short response. The Ch III framework does not apply.

```
Ch III of the Data Act applies only where the data holder is obliged
to make data available, either under Art. 5 (user-directed third-party
sharing) or under other Union or national law (Art. 12(1)). On the
facts presented, no such obligation has been identified.

Voluntary data sharing remains unaffected by Ch III rules (Recital 42,
last sentence). The parties contract freely. The Art. 8 FRAND
framework, the Art. 9 compensation framework, and the Art. 10 dispute
settlement framework do not apply by force of law.

The Art. 13 Ch IV unfairness control may still apply (Ch IV is not
conditional on a Ch III trigger; it covers any B2B data-related
contractual term between enterprises). Route to
`ch4-unfairness-challenge.md` if the unfairness of a specific term is
in issue.
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 8 (always); Art. 9 (where compensation is in issue); Art. 10 (where the dispute settlement option is being referenced); Art. 12 (scope of Ch III obligations); Art. 13 (Art. 8(2) cross-reference); Art. 50 (temporal applicability of Ch III, fourth sub-paragraph).
- `sources/regulation-2023-2854.md` Recital 42 (horizontal access rules; voluntary sharing carve-out); Recital 45 (non-discrimination; burden of proof); Recital 46 (reasonable compensation principle); Recital 47 (cost and margin structure); Recital 49 (SME cost-only cap); Recital 51 (transparency of calculation).
- `sources/faq-v1-4.md` Q38 (Commission interpretation on differentiation between recipients); Q39 (Commission interpretation on absence of upper or lower limit to compensation; SME no-margin rule); Q40 (Commission interpretation on dispute settlement coverage); Q72 (Commission interpretation on Art. 9(5) guidelines timing). Frame all as Commission interpretation.
- Directive (EU) 2016/943 (Trade Secrets Directive) where Art. 8(6) trade-secret data is in scope. The gate file at `references/gates/trade-secrets-directive.md` carries the substantive framing.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded if personal data in scope).
- `references/gates/trade-secrets-directive.md` (loaded if any data is claimed as trade-secret; Art. 8(6) cross-references the Art. 4(6) and 5(9) safeguards regime).
- `references/gates/dma-gatekeeper.md` (loaded if the data recipient is or acts for a DMA-designated gatekeeper and the Ch III trigger is Art. 5).
- `references/gates/sectoral-lex-specialis.md` (warn-only; loaded where the sharing obligation arises from a sectoral instrument).
- `references/gates/member-state.md` (warn-only; loaded for Art. 10 dispute settlement body selection and Art. 37 competent authority).
- `references/gotchas.md` entry 15 (Ch III compensation is data-recipient-to-data-holder; the basic-economics check). Mandatory on every Art. 8 / Art. 9 output.
- `references/gotchas.md` entry 16 (Art. 9(5) Commission guidelines are forthcoming, not published). Flag on every compensation drafting.
- `references/gotchas.md` entries 3 (user-not-data-subject is controller), 4 ("without undue delay" has no numeric SLA), 11 (gatekeeper exclusion is bidirectional), 19 (FAQ is non-authoritative). Check on each.
- `references/method/analysis-method.md` (the seven-step flow; this card is one instance).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (no material Art. 8 / Art. 9 amendments; Art. 9(5) guidelines still pending).

---

## Drafter notes

Operational observations for using this card. Three only.

- **Pricing transparency is the most-tested obligation in practice.** Art. 9(7) requires the data holder to provide the recipient with the basis of calculation in sufficient detail to permit assessment of compliance with Art. 9(1)-(4). Skeleton pricing ("market rate"; "cost-plus") will not satisfy Art. 9(7). The holder needs to identify the cost lines (formatting, dissemination, storage; collection and production investments where claimed) and the margin (if any, and zero for Art. 9(4) recipients) on a per-recipient basis. Draft the pricing schedule before drafting the contract clauses.
- **The non-discrimination burden flips early.** Once a recipient makes a reasoned request under Art. 8(3), the data holder has the burden of showing that the terms are not discriminatory. Build the comparator-recipient register on the same workflow as the pricing schedule; it is the holder's defensive evidence for any Art. 8(3) challenge or any Art. 10 dispute. Recital 45 puts the burden of proof explicitly on the data holder.
- **Art. 9(5) guidelines are the missing piece.** As of May 2026, the Commission has not adopted the Art. 9(5) guidelines on calculating reasonable compensation; the expected adoption window is Q2/Q3 2026 per FAQ Q72. Compensation analyses run on the regulation text and Art. 8 fairness principles alone. Flag in every output that the guidelines are pending; the user is taking decisions today that may shift when the guidelines drop.
