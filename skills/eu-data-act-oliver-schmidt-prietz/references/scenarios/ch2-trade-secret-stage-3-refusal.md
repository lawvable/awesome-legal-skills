# ch2-trade-secret-stage-3-refusal

**Anchor:** Data holder × Ch II × Art. 4(8) refusal. Highest-stakes drafting in the skill: the substantive bar is the highest, the failure mode (the circular trap) is the most consequential, and stage-3 refusals attract the closest competent-authority scrutiny.

**Routes from:**

- "Draft an Art. 4(8) refusal letter."
- "Can we refuse this Art. 4(1) request because [X] is a trade secret?"
- "We've claimed trade-secret status. What's our refusal posture under Ch II?"
- "Stage-1 safeguards have failed. What happens next?"
- "We want to refuse on grounds of competitive harm."

**Adjacent cards (route there instead if the facts indicate):**

- Stages 1 and 2 not yet attempted: `ch2-trade-secret-stages-1-2.md`.
- Art. 5(11) third-party refusal (parallel ladder): `ch2-trade-secret-stage-3-refusal-art5.md` (not yet drafted; this card holds the analysis until then).
- Refusal grounded in safety or security, not trade secret: `ch2-safety-security-handbrake.md` (Art. 4(2) regime).

---

## Canonical fact pattern

A data holder has received an Art. 4(1) request from a user. Some or all of the requested data is identified by the data holder as trade-secret-protected. Stage-1 safeguards under Art. 4(6) have been attempted and either no agreement was reached, or the safeguards were agreed but cannot be reasonably trusted to hold. The data holder is considering refusal under Art. 4(8).

The user is typically an enterprise (not a natural person) and may or may not be the data subject for any personal data in the dataset. The data is typically mixed (some trade-secret, some not; some personal, some not). The competent authority of the Member State of establishment has not yet been notified of any withholding or refusal.

---

## Critical disciplines

These three trip up almost every Art. 4(8) refusal drafted in the practitioner literature. The card cannot be applied without holding all three.

- **The circular trap.** Trade-secret status alone never satisfies Art. 4(8). Refusal requires the additional showing that disclosure would cause highly likely *serious AND irreparable* economic damage, demonstrated on objective elements (Recital 31; `references/gotchas.md` entries 6, 7, 8). A refusal drafted on trade-secret status alone is unlawful regardless of how confident the data holder is.
- **The conjunction.** Recital 31 reads "serious economic damage" as "serious and irreparable economic loss." "Serious but reparable" fails the test. So does "irreparable but trivial." Both elements need separate demonstration on the facts.
- **Stage-3 prerequisite.** Art. 4(8) is the third stage of a graduated ladder. The data holder cannot reach stage 3 without first attempting stage 1 (Art. 4(6) safeguards) and, where applicable, stage 2 (Art. 4(7) withholding). If stages 1 or 2 have not been attempted, route to `ch2-trade-secret-stages-1-2.md`.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check, Art. 1(6) carve-outs (criminal law enforcement, customs, taxation, national security, voluntary private-public arrangements, specified Union law instruments), and the Art. 2(22) "placed on the Union market" test for the connected product. Refusal cases are uncommon in genuinely out-of-scope matters, but the check is cheap and the carve-outs are real.

### Step 2: Chapter identification

Chapter II. Art. 4(8) sits in the user-access regime. The parallel third-party-access regime under Art. 5(11) is structurally identical; the analysis transposes, but the card is for the Art. 4 side. Where the user has directed disclosure to a third party that is also under threat of refusal, run both Art. 4(8) (data-holder vs user) and Art. 5(11) (data-holder vs third party) separately.

### Step 3: Role mapping

Required entity-by-entity mapping. Show as a table in the output.

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Data holder | Data holder (Art. 2(13)) | Controller, typically | Trade-secret holder under Directive (EU) 2016/943 (Trade Secrets Directive) and Art. 2(19) Data Act |
| Requesting user | User (Art. 2(12)) | Controller if not the data subject (Recital 34; `references/gotchas.md` entry 3); or data subject if a natural person and the data relates to them |  |
| Affected data subjects (if user is an enterprise) |  | Data subjects |  |
| Trade-secret holder (if not the data holder) |  |  | Licensor of trade secret to data holder; complicates Art. 4(8) limb 2 below |

Recital 34 makes the user-not-data-subject route to controller status explicit. Art. 4(12) conditions disclosure of personal data to such a user on a valid GDPR legal basis, which is a separate analysis the data holder must run before Art. 4(8) is even reached.

### Step 4: Fact-category sorting

Card-specific dimensions to sort the requested data against.

- **Trade-secret data vs not.** Run the Directive (EU) 2016/943 Art. 2(1) three-limb test on each category the data holder claims as trade-secret: (i) secret; (ii) commercial value because secret; (iii) reasonable steps to keep it secret. Categories that fail the test are not trade secrets, and the handbrake does not apply to them. The full TSD baseline is in `references/gates/trade-secrets-directive.md`.
- **Personal vs non-personal.** Drives the GDPR overlay (Art. 1(5) bridge clause). Mixed datasets (Recital 7) trigger GDPR for the personal-data component independently of any trade-secret analysis.
- **Readily available (Art. 2(17)) vs not.** Data not readily available is not in scope of the Art. 4(1) right; a refusal on Art. 4(8) is the wrong instrument if the data is unavailable for technical reasons. The analysis there runs on Art. 2(17), not Art. 4(8).
- **Raw or pre-processed vs derived (Recital 15).** Derived data is out of Ch II scope. A refusal on Art. 4(8) is not the right move if the data is out of scope; the data holder declines on scope grounds instead.

### Step 5: Limb-by-limb application of Art. 4(8)

Art. 4(8) decomposes into eight cumulative limbs. The article text in `sources/regulation-2023-2854.md` Art. 4(8) collapses some of these into single sentences; the skill enumerates them separately for analytical clarity. Each is independent; missing any one defeats the refusal.

1. **Exceptional circumstances.** Stage 3 is residual. The data holder must explain why the matter is not ordinary. "All our trade-secret data justifies refusal" is not exceptional; it is the opposite.
2. **Data holder is a trade-secret holder.** The data holder must itself hold the trade secret within the meaning of Art. 2(19) Data Act and Art. 2(2) Directive (EU) 2016/943 (Trade Secrets Directive). Licensed-in trade secrets complicate this limb; the data holder may not be the trade-secret holder for Art. 4(8) purposes even if it holds the data.
3. **Highly likely to suffer serious AND irreparable economic damage.** The conjunction. "Highly likely" is more demanding than "likely" or "possible." "Serious" means significant magnitude affecting business viability or competitive position. "Irreparable" means not recoverable through ordinary commercial mitigation, insurance, or contractual remedies against the recipient. Both must be demonstrated separately.
4. **Despite the Art. 4(6) safeguards.** The damage must remain highly likely *after* the stage-1 safeguards have been agreed (or after stage-1 negotiation has failed). A refusal that has not engaged stage 1 cannot reach this limb.
5. **Substantiated on objective elements.** Not subjective concern. Recital 31 lists three illustrative elements introduced by "in particular" (`references/gotchas.md` entry 8): enforceability of trade-secret protection in third countries; nature and level of confidentiality of the data requested; uniqueness and novelty of the connected product. Other admissible elements per `references/gates/trade-secrets-directive.md`: specific competitive relationship between data holder and recipient; inadequacy of the recipient's safeguards in light of compliance record; scale of data requested vs stated purpose; reverse-engineering risk; cybersecurity exposure; AI-training risk.
6. **Case-by-case basis.** Each request is assessed on its own facts. A blanket policy refusing all category-X requests is not case-by-case and is invalid as a stage-3 refusal.
7. **In writing without undue delay.** The substantiation goes to the user in writing, promptly. "Without undue delay" has no fixed numeric value (`references/gotchas.md` entry 4). The procedural form is constitutive: an oral or delayed refusal is not lawful.
8. **Competent authority notification.** The data holder notifies the competent authority designated under Art. 37 of the Member State of establishment. This is a parallel step, not a downstream consequence: notification is part of the refusal, not subsequent to it.

### Step 6: Cross-regime gate check

- **Trade Secrets Directive overlay (always loaded).** Read `references/gates/trade-secrets-directive.md` in full. The gate file walks the three-stage ladder, the conjunction, the objective elements, the technical and organisational measures, the substantiation obligations, the redress mechanics, and the McIntyre OSS enforcement signals. The gate also carries the eight-step refusal-letter structure that the Output Path 1 skeleton below tracks.
- **GDPR overlay (loaded if personal data in scope).** Read `references/gates/gdpr-overlay.md`. The Art. 4(8) refusal under the Data Act does not affect the data subject's GDPR Art. 15 right of access; Recital 31 last sentence is explicit. The data subject's GDPR rights run independently of the Data Act refusal. Where the user is not the data subject, Art. 4(12) conditions disclosure of personal data on a valid GDPR legal basis, which the data holder must analyse before reaching Art. 4(8).
- **DMA gatekeeper exclusion (warn-only on this card).** Art. 5(3) excludes gatekeepers as eligible third parties under Art. 5; it does not directly affect an Art. 4(1) request from a user. If the requesting user is or is acting for a DMA-designated gatekeeper, run `references/gates/dma-gatekeeper.md` before producing output.
- **Sectoral lex specialis (warn-only).** If the connected product is a vehicle, medical device, financial-services component, energy infrastructure, AI system, eIDAS-relevant, NIS2-covered, or Cyber Resilience Act covered, run `references/gates/sectoral-lex-specialis.md` and flag the overlay in the output. Stage-3 refusal in regulated sectors carries additional sectoral risk the horizontal analysis does not capture.
- **Member State implementing law (warn-only).** The competent authority designated under Art. 37 differs by Member State, as do the complaint procedure and dispute settlement options. Run `references/gates/member-state.md` to confirm the right authority before drafting the notification.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 4(8) of Regulation (EU) 2023/2854 (Data Act) governs. The eight-limb cumulative test above is the operative regime. Verbatim text at `sources/regulation-2023-2854.md` Art. 4(8); operative recital at Recital 31.
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final (19 November 2025) would add a new refusal ground for substantial risk of unlawful trade-secret acquisition, use, or disclosure to third-country entities operating under legal regimes with weaker protection than the EU. The amendment retains the case-by-case and objective-elements requirements. Status: co-legislator negotiation, not adopted. See `sources/digital-omnibus-amendments-tracker.md`.

The output cites current law as operative. The proposed amendment is forward-looking awareness only.

---

## Decision point

After Steps 5 and 6, the analysis yields one of four paths.

1. **All eight limbs satisfied, including the conjunction.** Proceed to the Art. 4(8) refusal letter (Output Path 1 below).
2. **Conjunction fails.** "Serious" demonstrated but not "irreparable", or vice versa, or both insufficient. Refuse to draft the refusal letter (Output Path 2 below). Explain the circular trap. Identify the missing facts the data holder would need to assemble for a stage-3 refusal to be lawful.
3. **Stages 1 or 2 not yet attempted.** Stage 3 is unreachable. Route to `ch2-trade-secret-stages-1-2.md`. Stage 1 attempts must be documented before any Art. 4(8) analysis is meaningful.
4. **Refusal grounds are not trade-secret.** Some refusals invoke trade-secret protection where the actual grievance is something else (safety, security, sectoral law, contractual non-disclosure obligations to third parties). If the gravamen is safety or security, route to `ch2-safety-security-handbrake.md` (Art. 4(2) regime). If sectoral, run the sectoral gate and reroute. Trade-secret status as a label for "I don't want to share this" is not a stage-3 ground.

The card does not produce a refusal letter on Paths 2, 3, or 4. The output explains why and what the data holder needs to do instead.

---

## Output skeleton: Path 1 (refusal letter, all limbs satisfied)

Formal letter, Markdown by default, ready for adoption with minimal edit. Length: typically 1.5 to 2.5 pages.

Structure:

```
[Data holder letterhead placeholder]

To: [Requesting user, full legal entity name and address]
Date: [Date of refusal, no later than "without undue delay" after the
       triggering event, which is typically the exhaustion of stage-1
       negotiation or the data holder's identification of stage-3
       conditions]
Subject: Refusal of data access request dated [request date] under
         Article 4(8) of Regulation (EU) 2023/2854 (Data Act)

1. The request
   [Identification of the user's Art. 4(1) request: date received,
   scope of data requested, reference number if any.]

2. Trade-secret status of the requested data
   [Identification of the specific data the data holder claims as
   trade secret. Statement that the data holder is the trade-secret
   holder within the meaning of Art. 2(19) Data Act and Art. 2(2)
   Directive (EU) 2016/943 (Trade Secrets Directive). Brief
   confirmation that the data satisfies the Art. 2(1) TSD test
   (secret; commercial value because secret; reasonable steps to
   keep it secret).]

3. Exceptional circumstances
   [Why this request is exceptional. Specific factual circumstances,
   not generic competitive concern. Tie to the objective elements
   identified in section 5(d) below.]

4. Stage-1 safeguards: status
   [Specific safeguards proposed under Art. 4(6). Either:
   (a) safeguards were agreed and implemented but remain insufficient
       to mitigate the damage demonstrated in section 5; or
   (b) no agreement was reached despite good-faith negotiation, with
       a brief factual account of the negotiation.]

5. Demonstration of highly likely serious and irreparable economic
   damage
   5(a) Highly likely. [Facts supporting the "highly likely"
        standard. Not "possible" or "likely"; the standard is
        elevated.]
   5(b) Serious. [Magnitude of the damage. Specific commercial
        consequences. Affected revenue lines, market positions, or
        R&D investments. Quantified where possible; qualitative
        where quantification is impossible but the substance is
        present.]
   5(c) Irreparable. [Why ordinary commercial mitigation,
        insurance, or contractual remedies against the recipient
        will not cure the damage. The conjunction's second element.
        This is the most common drafting failure; substantiate it
        independently of section 5(b).]
   5(d) Objective elements relied on. [Named elements with specific
        factual basis. Use the Recital 31 illustrative list where it
        fits (third-country enforceability; nature and level of
        confidentiality; uniqueness and novelty); add other
        admissible elements where they fit. Do not pad with elements
        the facts do not support.]

6. Case-by-case basis
   [Statement that the refusal is specific to this request and is
   not a blanket policy. Reference to past requests from the same or
   different recipients that were honoured, if relevant, to support
   the case-by-case characterisation.]

7. Notification to competent authority
   [Statement that the data holder has, in parallel with this
   refusal, notified the competent authority of [Member State of
   establishment] designated pursuant to Article 37. Reference
   number of the notification if available.]

8. The user's redress options
   [Information that the user may, without prejudice to its right to
   seek redress before a court or tribunal of a Member State, (a)
   lodge a complaint with the competent authority pursuant to
   Article 37(5)(b), which will decide without undue delay whether
   and under what conditions data sharing is to start; or (b) agree
   with the data holder to refer the matter to a dispute settlement
   body certified under Article 10.]

[Signature block placeholder]
```

---

## Output skeleton: Path 2 (refuse to draft, conjunction or other limb fails)

Short response. Markdown. Lead with the legal reason the refusal cannot be drafted as posed. No CYA padding; the user is the lawyer.

Structure:

```
The Art. 4(8) refusal as posed would not be lawful because [the
specific limb that fails]. Most commonly, this is the conjunction
under Recital 31: the regulation requires highly likely serious AND
irreparable economic damage, and the facts as presented demonstrate
[serious damage but not irreparability / irreparable damage but of
insufficient magnitude / trade-secret status without any damage
demonstration].

To draft an Art. 4(8) refusal, the data holder will need the
following additional facts:

- [Fact 1: specific factual scenario for the damage]
- [Fact 2: objective elements available]
- [Fact 3: why mitigation, insurance, or contractual remedies
  against the recipient are insufficient to repair the damage]
- [Fact 4 if relevant: stage-1 negotiation record]
- [Fact 5 if relevant: competent authority notification status and
  timing]

If those facts can be assembled, the card produces the refusal
letter (Path 1). If they cannot, the data holder has two practical
options:

1. Return to stage 1 or stage 2. Stage-1 safeguards may suffice for
   this request if the substantive concern is mitigable (see
   `ch2-trade-secret-stages-1-2.md`).
2. Disclose with safeguards. Where the conjunction cannot be
   demonstrated, the regulation requires disclosure. The graduated
   regime is intentional: stage 3 is residual.
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 4(6), Art. 4(7), Art. 4(8) (always); Art. 4(9) (for the redress section); Art. 4(12) (if personal data and the user is not the data subject); Recital 30 (graduated structure); Recital 31 (conjunction; objective elements; redress).
- `sources/regulation-2023-2854.md` Art. 37 (competent authority notification); Art. 10 (dispute settlement).
- `sources/faq-v1-4.md` Q23 (Commission interpretation on stage-1 safeguards); Q24 (Art. 3 direct access does not benefit from the handbrake by default). Frame both as Commission interpretation.
- Directive (EU) 2016/943 (Trade Secrets Directive) Art. 2(1) (definition); Art. 3(2)(d) (lawful disclosure required by Union law). The gate file at `references/gates/trade-secrets-directive.md` carries the TSD framing; do not re-derive it in the card output.
- `sources/digital-omnibus-amendments-tracker.md` for the Art. 4(8) entry on the proposed third-country misuse refusal ground.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/trade-secrets-directive.md` (always loaded; this is the TSD substantive gate and contains the eight-step refusal-letter structure that Output Path 1 above tracks).
- `references/gates/gdpr-overlay.md` (loaded conditionally on personal data in scope).
- `references/gates/dma-gatekeeper.md` (loaded if the requesting user is or acts for a DMA-designated gatekeeper).
- `references/gates/sectoral-lex-specialis.md` (warn-only; loaded if the connected product is in a regulated sector).
- `references/gates/member-state.md` (warn-only; loaded to identify the competent authority and complaint procedure).
- `references/gotchas.md` entries 6 (ladder, not switch), 7 (the serious-AND-irreparable conjunction), 8 (objective elements illustrative, not exhaustive). Mandatory check on every stage-3 deliverable.
- `references/gotchas.md` entries 3 (user-not-data-subject is controller), 4 ("without undue delay" has no numeric SLA), 19 (FAQ is non-authoritative), 20 (Digital Omnibus is a proposal). Check on each.
- `references/method/analysis-method.md` (the seven-step flow; this card is one instance).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (Art. 4(8) entry).

---

## Drafter notes

Operational observations for using this card. Three only.

- **Notification under Art. 37 is constitutive.** A stage-3 refusal that has not been notified to the competent authority of the Member State of establishment is not lawful. Notification is part of the refusal, not a downstream administrative step. Build it into the same workflow as the letter and run it in parallel.
- **Stage-1 documentation matters more than the letter itself.** The strongest stage-3 refusals are built on documented stage-1 negotiation that did not yield an adequate safeguard. The competent authority will look at the stage-1 record before assessing the stage-3 substantiation. Draft the stage-1 paper trail at the same time as the safeguards are proposed, not after.
- **The McIntyre OSS pattern.** Competent authorities have been ordering resumption of data sharing within weeks where stage-3 substantiation is weak. The practical risk of a weak stage-3 refusal is not "user sues if they care enough" but "competent authority overrules within a month." See `references/gates/trade-secrets-directive.md` enforcement-signal section.
