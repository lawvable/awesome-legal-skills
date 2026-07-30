---
name: "pre-motion-andrew-bird"
description: |
  Adversarial premortem for England & Wales civil litigation - builds the strongest version of a case, then attacks it from four angles to find where it loses before opposing counsel does. Runs an adversarial premortem on a UK litigation matter. Builds the strongest version of the case, then attacks it from four angles — procedural, substantive, evidentiary, strategic — to find where it actually loses. Returns a ranked stress-test brief: failure scenarios, evidence inconsistencies, blind spots, mitigations, and one brutal one-sentence verdict. Use before issue, before settlement negotiations, before a litigation-funder pitch, or before deciding whether to take a case. 
argument-hint: "[--depth=fast|thorough]"
metadata:
  author: "Andrew Bird"
  license: "mit"
  version: "2026-06-05"
---

# Pre-Motion — adversarial premortem for UK litigation

You think you've built the strongest version of your case. Pre-Motion runs it through a structured adversarial pipeline to find where it actually loses — the procedural, substantive, evidentiary, and strategic failure modes opposing counsel will pull on first. The opposite of confirmation bias, by design.

For: solicitors stress-testing before issue, in-house counsel before sign-off, mediators valuing settlement, litigation funders pricing a matter, anyone deciding whether to take a case.

## How it runs

Four passes over the matter. Run the four adversarial passes in Stage 3 as parallel sub-agents if your environment supports them; otherwise run them in sequence — the method and the output are the same either way.

1. **Optimistic baseline.** Build the strongest version of the case the evidence supports. This is the foil for everything that follows.
2. **Evidence inspection.** Three checks: document review (gaps, weak documents), cross-reference (one document contradicting another), chronology (timeline gaps, dates that don't fit). Produce evidence flags with a severity each.
3. **Premortem adversary.** Four adversarial passes, one per failure category below. Give each the same frame: *"It is [trial date + 1 year]. This case has been LOST. Walk back — what in your category caused the loss?"* Produce ranked failure scenarios per category.
4. **Synthesis.** Diff the optimistic baseline against the adversarial findings. Produce the brief.

`--depth=fast` runs a single combined adversarial pass for a quick read; `--depth=thorough` runs all four passes in full.

## Inputs

- Matter facts: parties, brief chronology, claim heads, jurisdiction, forum.
- Evidence references: documents, witness statements, expert reports — pointers to matter content, not re-uploaded.
- The strongest version of the case as the user sees it (the optimistic baseline).
- Optional: the counterparty's pleaded or anticipated defence.
- Optional: `--depth=fast|thorough`.

## Step 1 — Permitted-use check (CPR 31.22 + privilege)

Before reading matter documents:

- The host workspace enforces the hard gate (matter-slug match against the proceedings reference, privilege posture). If this skill is running, that gate has already passed — this step does not replace it.
- Still confirm with the user: are any documents drawn from disclosure in *other* proceedings? If so, stop until permission, the parties' agreement, or open-court reference is established (CPR 31.22 implied undertaking).
- If the matter's privilege posture is mixed, add a `[PRIVILEGE FLAGGED]` banner to the output and recommend counsel review before any external distribution.

## Failure-mode categories

The four Stage 3 passes specialise in the four ways UK civil cases lose.

### Procedural

- Limitation expired or contested (Limitation Act 1980, s.5 / s.11 / s.14A).
- Pre-action protocol non-compliance (Pre-Action Conduct PD, sector protocols).
- Strike-out or summary-judgment vulnerability (CPR 3.4, CPR 24).
- Costs sanctions risk (CPR 44.2).
- ADR refusal exposure (Halsey; Churchill v Merthyr Tydfil [2023]).
- Service / jurisdiction defects (CPR 6).
- Disclosure-regime missteps (CPR 31 vs PD 57AD).

### Substantive

- Cause-of-action elements unproven.
- Causation gaps, factual or legal (Wagon Mound, Fairchild, SAAMCO).
- Mitigation failures (British Westinghouse).
- Affirmative defences (estoppel, waiver, release, contributory negligence, ex turpi causa).
- Statutory bars (Consumer Rights Act, UCTA, statutory limitation).

### Evidentiary

- Privilege exposure (Unilever exceptions, joint-defence breakdown, Rush & Tompkins boundary).
- Disclosure failures and adverse-inference risk (CPR 31, PD 57AD).
- Witness credibility, availability, inconsistency.
- Hearsay weaknesses (Civil Evidence Act 1995 s.2–4 notice failures).
- Expert-report deficiencies (CPR 35; joint-instruction failures; Toth v Jarman).
- Document authenticity and chain of custody.

### Strategic

- Settlement leverage misjudged (BATNA gap to the opposing side).
- Cost/benefit ratio misaligned with client objectives.
- Reputational or regulatory exposure from issue or trial.
- Information asymmetry working against the client.
- Counterparty's BATNA stronger than the optimistic baseline assumes.

Each pass should cite the relevant authority for its category, and mark any rule or case it cannot pin to a section or citation with `[CITE NEEDED]` rather than stating it as settled.

## Output

Produce the brief with the sections below. Render it as the finished brief — do not echo this list back as a template, and do not invent facts to fill a section; if a section has nothing in it, say so.

- A reviewer-note line: *work product, prepared in contemplation of litigation, subject to litigation privilege.*
- A header: matter name, date generated, depth, privilege posture, and the verdict (Steelman / Borderline / Strawman).
- **The one brutal sentence** — "If we lose this, this will be why: [single sentence]."
- **Optimistic baseline** — the strongest version of the case, as the baseline pass built it.
- **Ranked failure scenarios** — grouped Procedural / Substantive / Evidentiary / Strategic. Each scenario is one paragraph with a Severity (H/M/L), a Likelihood (H/M/L), and a Mitigation.
- **Evidence inconsistencies** — the flags from Stage 2.
- **Blind spots** — issues the baseline assumed resolved that the adversary found open.
- **Mitigations** — one concrete action per scenario where applicable: strengthen evidence, amend pleadings, settle, withdraw, brief counsel differently.
- **Settlement-posture implications** — qualitative only. Translate the failure profile into posture, e.g. "several procedural failure modes ranked H — settle harder than the baseline suggests; consider a Calderbank offer before issue." Produce no number; full BATNA / ZOPA analysis belongs to the v0.2 `settlement-helper` skill.

Mark uncertainty inline as you go:

- `[SME VERIFY — failure mode]` — borderline adversary output; counsel's call.
- `[CITE NEEDED — authority]` — a rule or doctrine referenced without a section or case; verify before relying on it.
- `[EVIDENCE FLAG — severity]` — surfaced by Stage 2; check against the source document.

## What this skill does not do

- Predict the outcome. It surfaces failure modes; outcomes depend on the tribunal, the judge, the witnesses, the day.
- Take the case for you. The verdict (steelman / strawman) is the model's read of the brief, not advice.
- Replace counsel's strategic call. Settle, withdraw, strengthen — all counsel decisions.
- Cover non-UK procedure (US federal, Scotland, NI).
- Run during trial. This is pre-action, pre-settlement, or pre-funding use.
- Replace a formal counsel opinion. A KC's view on case strength matters more than this output. Pre-Motion is a structured prompt for that conversation, not a substitute for it.

## v0.2 roadmap

A separate `settlement-helper` skill covering Calderbank / Part 36 mechanics and BATNA / ZOPA / Nash bargaining — the quantitative settlement analysis deliberately kept out of this skill.
