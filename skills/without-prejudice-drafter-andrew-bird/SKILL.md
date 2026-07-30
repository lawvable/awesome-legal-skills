---
name: "without-prejudice-drafter-andrew-bird"
description: "Writes a settlement letter on the right footing — and warns you when marking it 'without prejudice' won't actually keep it out of court. A genuine settlement letter is normally protected (the judge can't see it), but only if the substance is a real attempt to settle, and even then there are exceptions. The skill picks the correct footing — without prejudice (WP), without prejudice save as to costs (WPSATC / Calderbank), or open — drafts the finished letter, and surfaces the Unilever v Procter & Gamble exceptions that get WP material admitted despite the label, which a plain template won't flag. Built for juniors and in-house counsel drafting a settlement or Calderbank offer who need the footing right the first time. Use when the user asks to draft a WP letter, a Calderbank, a settlement letter, or wants to know whether material is likely protected from disclosure."
argument-hint: "[--type=wp|wpsatc|open]"
metadata:
  author: "Andrew Bird"
  license: "mit"
  version: "2026-06-09"
---

# /without-prejudice-drafter

1. Identify the correct footing: open, WP, or WPSATC.
2. Apply the right header convention. WP is not protected just because labelled — the substance must be a genuine settlement attempt in an existing or contemplated dispute.
3. Surface the Unilever exceptions: WP protection is not absolute.
4. Draft accordingly. Keep open and WP material in separate documents.

---

# Without prejudice / WPSATC correspondence

## The three footings

| Footing | Disclosure at trial | Use |
|---|---|---|
| **Open** | Yes — fully admissible | Statements of case, demands, pre-action letters not yet in negotiation |
| **Without prejudice (WP)** | No — inadmissible to prove liability or quantum | Genuine settlement negotiations |
| **Without prejudice save as to costs (WPSATC) / Calderbank** | Inadmissible on liability/quantum; intended to be **admissible on costs** after judgment | Settlement offers where the offeror wants costs protection but cannot use CPR Part 36 (e.g. Employment Tribunal) or wants Calderbank flexibility |

Labelling a letter WPSATC signals the intended footing; it does not by itself secure costs protection. Whether the court reads the letter on costs, and what weight it gives it, is a matter for the court's discretion (CPR 44.2) on the facts. The footing is a proposal, not a guarantee.

## When WP protection applies

Three conditions:

1. There is an **existing or contemplated dispute**.
2. The communication is **a genuine attempt to settle** that dispute.
3. The parties intended the communication to be confidential.

A letter labelled "without prejudice" that does not satisfy these conditions is not protected. A letter that satisfies them but is not labelled is still protected — the label is evidence of intention, but substance prevails (Rush & Tompkins Ltd v Greater London Council [1989] AC 1280).

## The Unilever exceptions (Unilever v Procter & Gamble [2000])

WP protection is not absolute (Unilever plc v Procter & Gamble Co [2000] 1 WLR 2436, [2000] EWCA Civ 11). The categories below are illustrative, not a closed or settled set — the courts treat them as fact-sensitive, so confirm the current scope before relying on any one of them. The court has admitted WP material in evidence in situations including the following. Do not over-extend these; treat anything outside a squarely-decided category as in need of verification rather than asserting protection is lost:

1. The WP communications show the agreement was concluded — to prove or rebut existence/terms of the agreement.
2. The communications are evidence of misrepresentation, fraud, or undue influence.
3. The communications give rise to estoppel.
4. Without admission, exclusion would act as a cloak for "unambiguous impropriety" (e.g. perjury, blackmail, threats).
5. To explain delay or apparent acquiescence (relevant to limitation).
6. The communications are relevant to costs (only if WPSATC was the footing).
7. The communications include a tariff or formula relevant to determining a related issue.

A letter discussing a settlement that also makes a threat or admits a crime is exposed under (4). Practical implication: WP is not a magic shield. Labelling a letter does not make it privileged, and even a properly-footed letter can be admitted under an exception. Don't write anything you'd be embarrassed by if a judge reads it, and don't promise the client the letter is "safe" — the footing can fail.

## Calderbank / WPSATC specifics

The Calderbank offer (Calderbank v Calderbank [1976] Fam 93) lets a party put a settlement on the table that the court will see on costs at the end. Mostly displaced by CPR Part 36 in the civil courts, but still alive where:

- The forum doesn't have Part 36 (Employment Tribunal — use a Calderbank / WPSATC offer instead).
- The offer is on terms Part 36 cannot accommodate (mixed money and non-money relief; offers including a contribution; offers conditional on third-party action).
- The offeror wants to avoid the strictures of Part 36 formality.

Calderbank cost consequences in the civil courts are weaker than Part 36 — the court has discretion under CPR 44.2 and 36.17 does not apply. State the WPSATC footing explicitly; if uncertain, run the offer as a Part 36 instead.

## Drafting rules

1. **Header**: place the words "Without Prejudice" or "Without Prejudice Save As To Costs" prominently at the top of the document, before the salutation.
2. **Don't mix**: do not put open content and WP content in the same document. If both are needed, write two letters, one open, one WP, cross-referenced.
3. **No threats**: don't put anything in a WP letter that you would not want read out in court if WP fails.
4. **Settlement substance**: state clearly that the letter is part of a genuine attempt to settle the [described dispute].
5. **Authority**: a WP offer should be authorised by the client and confirm the lawyer has authority to bind on those terms (or expressly state subject-to-client-approval).
6. **Acceptance mechanics**: how is acceptance communicated; how long is the offer open; what happens if not accepted.
7. **Costs reservation (WPSATC only)**: expressly reserve the right to refer to the letter on costs. The reservation states the intended footing; it does not bind the court, which retains discretion under CPR 44.2.

## Workflow

### Step 1 — Confirm footing
Infer the intended footing from the request:
- "Settlement offer" or "without prejudice letter" → WP.
- "Calderbank", "costs protection", "offer with costs consequences", or any ET-context offer → WPSATC.
- "Demand", "letter before claim", "on the record" → open (use `cpr-letter-drafter` instead).
Surface for confirmation only if ambiguous from the request.

### Step 2 — Confirm dispute
Is there an existing or contemplated dispute? If no, WP doesn't apply — use open correspondence.

### Step 3 — Draft

Use the appropriate template. Keep separate from any open correspondence going out the same day.

### Step 4 — Surface exceptions

Flag any content that risks an Unilever exception (admissions, threats, signals of estoppel).

## Output

Produce the finished letter, not the template. Each section below is content to PRODUCE — render it as the completed correspondence, fully drafted on the chosen footing. Do not echo the template skeleton back to the user, and do not fabricate facts to fill a placeholder: for any value you don't have (sums, dates, party names, dispute description), insert `[SOLICITOR: confirm X]` rather than guessing. The placeholders below (£[X], [21] days, [brief description]) mark exactly the spots that must be confirmed, not copied verbatim.

The two structures below are the WP and WPSATC variants. Pick the one matching the confirmed footing and render only that.

### Without Prejudice — sections to produce

**WITHOUT PREJUDICE**

[Date]

[Recipient]

Dear Sirs,

**Re: [Matter — dispute description]**

This letter is written without prejudice as a genuine attempt to settle the dispute between our respective clients concerning [brief description of the dispute].

1. [Statement of position — neutral, not adversarial.]
2. [Proposal — sum, terms, mechanism.]
3. [Time limit for acceptance.]
4. Subject to acceptance on these terms, the matter will be compromised on the basis of [release / settlement deed / consent order].

This letter is intended to be confidential and may not be disclosed to the court without our written consent.

Yours faithfully,

[Signature]

### Without Prejudice Save As To Costs — sections to produce

**WITHOUT PREJUDICE SAVE AS TO COSTS**

[Date]

[Recipient]

Dear Sirs,

**Re: [Matter]**

This letter is written without prejudice save as to costs.

1. Our client offers [to pay / to accept] £[X] in full and final settlement of the [dispute / claim / counterclaim].
2. The offer is open for acceptance for [21] days from the date of this letter.
3. The sum is [inclusive / exclusive] of [costs / interest / VAT].
4. Acceptance will be by [signed agreement / consent order / written acceptance].

If the offer is not accepted, our client reserves the right to refer to this letter on the question of costs after judgment.

Yours faithfully,

[Signature]

## Markers

- `[FOOTING — review: this content reads more open than WP]`
- `[UNILEVER RISK — admission / threat / unambiguous impropriety language]`
- `[SEPARATION — keep open correspondence in a different letter]`

## What this skill does not do

- Give legal advice or settle the privilege footing. This produces a draft for a solicitor to review, not advice the client can rely on. The footing it proposes is exactly that — a proposal. Counsel or the conducting solicitor must confirm it before the letter is sent, because mischaracterising a letter's footing has real disclosure consequences: an offer the client believed was protected can end up admissible, and open material wrongly treated as WP can frustrate the client's own case.
- Make a labelled letter privileged that isn't substantively a settlement attempt. The label follows the substance, not the other way round.
- Guarantee the footing holds. WP protection can fail (see the Unilever exceptions), and WPSATC costs treatment is at the court's discretion under CPR 44.2.
- Provide costs-protection equivalent to Part 36 in the civil courts — draft a CPR Part 36 offer separately for that.
- Cover Scottish "tenders" or NI equivalents.
