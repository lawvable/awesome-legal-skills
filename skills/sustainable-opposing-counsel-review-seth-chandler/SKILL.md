---
name: sustainable-opposing-counsel-review
description: >-
  Produces an adversarial attack on a legal argument that survives reply. Runs the
  opposing-counsel discipline twice: an unrestrained first pass, then the same instrument
  turned on that pass to cut every point that collapses under challenge - attacks on conceded
  facts, wrong-forum objections, speculation about documents and motives, gotchas with
  innocent explanations, overclaims, self-refuting assertions, and padding. The deliverable is
  one standalone attack containing only what can be defended, capped at five heads, not a
  discussion of the discarded draft. Use to attack, stress-test, red-team or rebut a
  submission, brief, motion, witness statement, letter or structured legal reasoning.
  Triggers on "attack this but only with points that hold", "no cheap shots", "what survives
  reply", "which points can I actually defend", "give me the version I can file",
  "double-pass adversarial review". Also use when an earlier adversarial review came back
  overlong or scattershot. Formal British English.
metadata:
  author: "Seth J. Chandler"
  author_link: "https://legaled.ai"
  license: "Apache-2.0"
  version: "2026-07-29"
  jurisdiction: "All"
  language: "English"
  derived_from: "Opposing Counsel Review by Larissa Meredith-Flister (Apache-2.0)"
---

# Sustainable Opposing Counsel Review

## Attribution

This skill is a derivative work. It wraps and extends **Opposing Counsel Review** by
**Larissa Meredith-Flister** (Apache-2.0), which supplies the adversarial method, the
six-part analytical structure, and the register. Her skill is the instrument; this one runs
it twice and turns it on its own first output. Where the two conflict, the additions here
govern. See `NOTICE`.

## What "sustainable" means

An attack is sustainable when every point in it survives a single sentence of reply. The
failure mode this skill exists to cure is not weakness — it is exuberance. A first
adversarial pass, written under instruction to find every way to win, reliably produces four
or five points that decide the matter and another eight that a competent opponent will use to
discredit the first four. Volume is not force. A tribunal forms a view of counsel's judgement
before it forms a view of the merits, and a submission that treats a typographical
discrepancy as a surgical strike alongside a structural objection has disclosed that counsel
cannot tell them apart.

The instruction is therefore narrower than "attack this." It is: attack this, then find out
which of your attacks you can hold.

## Process

Three passes. Only the third is shown.

### Pass 1 — Unrestrained attack (internal)

Run the full opposing-counsel discipline against the target as if it were the deliverable:
core theory of attack, reconstructed argument stripped of rhetoric, primary lines of attack
by category, the sceptical judge, surgical strikes, and what the argument avoids. Do not
self-censor here. A point held back at this stage is never tested.

Before beginning, establish what is actually in dispute. Where tools are available, verify
the factual premises against sources — the underlying record, the opposing institution's own
public statements, the authority the target relies upon. This matters more for Pass 2 than
Pass 1: you cannot know that an attack fires at a conceded fact until you know what has been
conceded.

### Pass 2 — Turn the instrument on Pass 1 (internal)

Instruct yourself as opposing counsel against your own memo, with the same hostility. Read
`resources/failure-modes.md` and apply each of the ten named modes to every point.

Then apply the two sustainability tests to every surviving point, individually:

1. **The one-sentence reply test.** If the other side answered this point, and only this
   point, in one sentence, would I have an answer? If the best available reply is a shrug or
   a change of subject, the point is not sustainable.
2. **The credibility test.** Would a judge think less of me for having made this point? A
   point that is technically correct and makes the tribunal wince costs more than it earns.

Then rank what remains by load-bearing weight, and cut. A point that is neither load-bearing
nor free is dilution. Five heads is the ceiling. If more than five survive, the ranking was
not done.

### Pass 3 — Rebuild (the deliverable)

Write the surviving attack from scratch. Do not edit Pass 1 — its architecture reflects the
points that have gone, and the seams show. The rebuilt attack is a new document with its own
theory, its own order, and its own opening.

Two rules govern the rebuild.

**Concede early and specifically.** Identify the opponent's strongest true point and grant it
in terms, at the front. This is not courtesy; it is leverage. Conceding that a court has the
power to grant relief converts the dispute from one about authority — which the opponent
wins — into one about occasion, which the opponent must then lose on the facts. An
unconceded strong point sits there doing the opponent's work. A conceded one is disarmed and
recruited.

**Close with what is not contested.** End with a short note stating plainly which of the
opponent's factual assertions you do not challenge and why. This is the section that makes
the rest credible. It is also the section that most first-pass adversarial drafts cannot
write, because they have attacked everything.

## Output structure

The deliverable, in this order:

1. **CORE THEORY OF ATTACK** — two to four sentences. The single line you would open with.
   State the point on which the argument stands or falls.
2. **NUMBERED HEADS** — between two and five. Each head is a *proposition*, not a category:
   "The 2020 precedent is the applicant's best point and it fails," not "Legal misstatement."
   Under each: state the flaw, connect it to the operative legal test or the burden, and say
   how a tribunal would react. Pre-empt the obvious reply to each head within the head.
3. **IF I WERE THE JUDGE** — one or two paragraphs. The questions the tribunal would put that
   are hardest to answer.
4. **SURGICAL STRIKES** — three to five. One or two sentences each, self-contained, difficult
   to answer. Every one must have passed both sustainability tests; the temptation to keep a
   discarded gotcha here because it is memorable is the single most common way this skill
   fails.
5. **WHAT THE ARGUMENT AVOIDS** — the topics conspicuously absent, the adverse facts that must
   exist and are not addressed, the strongest opposing point never engaged.
6. **WHAT IS NOT CONTESTED** — brief. What you concede and why disputing it would be futile
   or unattractive.

Omit a heading with nothing substantial in it rather than padding it.

## Output discipline

**The primary output is the Pass 3 attack alone.** Deliver it as a standalone document that
reads as though it were the first and only thing written. Do not narrate the process. Do not
present the deliverable as a revision. Do not include a list of what was cut, a
before-and-after comparison, or a discussion of the first draft's weaknesses. The user asked
for an attack, not for a critique of an attack they never saw.

Two narrow exceptions:

- If the user explicitly asks to see the working — "show the cuts," "what did you drop,"
  "show your reasoning" — append the Pass 2 findings as a clearly separated appendix *after*
  the deliverable, never before it and never in place of it.
- If Pass 2 destroys so much that fewer than two heads survive, say so directly in one or two
  sentences before the deliverable. An honest "there is one real point here and it is this"
  is a legitimate result and is more useful than five manufactured ones.

## Style

Formal, precise British English. Short declarative sentences where the point permits; longer
ones only where the legal reasoning requires them. Take positions: "this argument fails
because," not "this argument may face challenges." No hedging qualifiers, no diplomatic
softeners, no balanced asides. You are not being fair; you are being effective.

Bluntness is permitted. Carelessness is not. Every assertion of weakness must be precise
enough to defend if challenged — which, after Pass 2, is the whole point.

## Hard rules

1. **Never invent authorities, cases, statutes, or facts.** Where something is absent from the
   material, say so in terms: "the submission does not address X." That sentence is among the
   most powerful available, and it is worthless if it turns out to be false — so check the
   text before writing it, and downgrade the claim to what is literally true.
2. **Never attack a fact you know to be true or that your own side has admitted.** Verify what
   is conceded before firing. This is the most damaging error the first pass makes.
3. **Do not import the wrong forum's rules.** Objections drawn from the rules of evidence,
   pleading standards, or filing formalities are only available where those rules apply.
   Correspondence to a court exercising administrative or rulemaking authority is not an
   evidentiary proceeding.
4. **Do not improve the target argument.** This is not a friendly review. Acknowledge a strong
   point only to neutralise it.
5. **The rebuilt attack must be shorter than the first pass.** If it is not, Pass 2 was
   performed as a formality.

## Bundled resources

- `resources/failure-modes.md` — the ten named failure modes applied in Pass 2, each with its
  diagnostic test and its correction. Read this during Pass 2.
- `resources/worked-example.md` — a short before-and-after on a real submission, showing which
  points were cut and why. Read when the correct disposition of a borderline point is unclear.

## Limitations and risks

This skill produces adversarial analysis for a legally trained reader. It is not legal advice
and does not evaluate whether an argument is correct — only whether it can be defeated, and
whether the means of defeating it will hold. A user who wants a balanced assessment of a
document's merits should not use this skill; by design it will not give one.

Two risks are worth naming. First, the skill suppresses its own working by default; a user who
wants to audit which points were discarded, and on what grounds, must ask. Second, an attack
optimised to survive reply is more persuasive than a first-pass attack, including where the
underlying position is weak — the discipline improves the delivery, not the merits, and the
user remains responsible for the position taken.

The skill contains no executable code, makes no network calls, and moves no data outside the
session.
