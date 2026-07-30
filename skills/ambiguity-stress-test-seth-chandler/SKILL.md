---
name: ambiguity-stress-test
description: >-
  Adversarially stress-tests a legal text — a contract, statute, regulation, or
  judicial opinion — for interpretive ambiguity: it finds the seams where the
  people governed by it will later disagree about what it means and turns each
  into a concrete dispute scenario with both sides' arguments, the likely
  outcome, and a fix. Use it whenever someone wants to pressure-test, red-team,
  audit, or find weak spots, loopholes, gaps, ambiguities, or drafting problems
  in a legal document; whenever a drafter wants to tighten a contract, statute,
  regulation, or opinion before it issues; whenever a litigator wants to mine an
  opinion or contract for arguments; or whenever someone hands over a legal text
  and asks where it will be fought over or for issue-spotting. Trigger it for
  contract review, statutory-ambiguity analysis, judicial-opinion scope
  analysis, and drafting QA — even if the user never says "stress-test" or
  "ambiguity."
metadata:
  author: "Seth J. Chandler"
  author_link: "https://legaled.ai"
  license: "Apache-2.0"
  version: "2026-07-29"
  jurisdiction: "United States"
  language: "English"
---

# Interpretive-Ambiguity Stress-Test

Adversarially stress-test a legal text for the places where the people governed by it will later disagree about what it means. For each weak seam, produce a concrete dispute scenario: a realistic fact pattern, both sides' arguments, the likely outcome, and a fix. The text can be a contract, a statute, a regulation, or a judicial opinion.

The skill rests on one principle — **generalize the detector, keep the resolver modular.** The machinery that *finds* ambiguity (parse, scan, construct an edge-case scenario, frame two plausible readings) is the same for every legal text. The machinery that *resolves* it is not: contract ambiguity is settled by recovering the parties' bargain, statutory ambiguity by the canons of construction, regulatory ambiguity by the canons plus the enabling act, and a judicial opinion's by the doctrines of precedent. So the skill has a general **core** (this file) and four domain **profiles** (in `resources/`). Run the core; load the one profile that matches the document.

The product is **disputes, not flags.** A linter says "this term is vague." This skill instead invents the two people who would each, plausibly, win if their reading prevailed — and the money or liberty riding on the answer. A latent ambiguity is invisible to a non-specialist until someone shows them the collision it will cause.

## Workflow

- **Step 0** — Select the profile and read its reference file.
- **Step 1** — Parse the text.
- **Step 2** — Scan for defects.
- **Step 3** — Construct a scenario for each confirmed defect.
- **Research** — between Steps 3 and 4, establish what sources are available and check the surviving scenarios against them. Statute, regulation and opinion profiles only; the contract profile skips it.
- **Step 4** — Emit the scenario records.

Steps 1–4 are the engine, identical across profiles. The profile supplies the domain-specific defect families, a lexicon, the competing interpreters, the doctrines that drive the likely outcome, the redraft register, and any quality-bar adjustment.

## Step 0 — Select the profile

Identify the document type and read the matching reference file before scanning:

| Document | Profile file |
|----------|--------------|
| Contract, agreement, lease, NDA, employment offer, policy, terms of service | `resources/contract.md` |
| Statute, code section, ordinance, enacted bill | `resources/statute.md` |
| Regulation, agency rule, administrative code provision | `resources/regulation.md` |
| Judicial opinion, court decision, or a draft opinion | `resources/opinion.md` |

If the text is some other normative document (a will, a treaty, an insurance policy, a set of bylaws), run the nearest profile and state plainly which interface elements do not fit. If the input mixes types — a statute and the regulation under it, say — run each through its own profile and also look across the link.

## Step 1 — Parse

Segment the text into addressable units and build four working lists: every **defined term**; every **operative provision** (a right, duty, or power — "shall," "may," "is entitled to"); every **trigger or condition** ("if," "provided that," "upon," "in the event of"); and every **grant of discretion or unilateral power**.

For statutes and regulations, also extract every **cross-reference** to another instrument — the most serious defects live in those links. For a judicial opinion, also map the structural parts — holding, supporting reasoning, dicta, disposition, and any separate opinions — because an opinion's operative rule is latent and must be reconstructed before it can be tested.

## Step 2 — Scan

Run the universal trigger lexicon and the active profile's lexicon over every unit, then run the seven-question diagnostic battery over every flagged unit and over the text as a whole. Classify each confirmed defect into one of the six universal families or a profile-specific family. Spend attention where disputes actually originate — definitions, triggers, conditions, grants of discretion, cross-references — and ignore boilerplate (headings, recitals, counterparts clauses).

### Universal defect taxonomy

Six families apply to any legal text. Each profile adds its own; these six are the floor.

- **A. Internal contradiction** — two provisions that cannot both be honored. *Ask:* if I enforce both literally, do I get an impossible or opposite result? Watch where a general provision and a specific one address the same subject.
- **B. Vague operative term** — a word that switches a right on or off but carries no definition and no measurement baseline. *Ask:* this term decides whether money changes hands or liberty is lost — could two honest readers draw the line in different places?
- **C. Definitional boundary ambiguity** — a *defined* term whose definition has fuzzy edges, so real facts fall neither clearly inside nor clearly outside it. *Ask:* can I describe a realistic thing that is arguably in and arguably out?
- **D. Standardless discretion** — one actor holds unilateral power over a consequential determination, with no stated standard, no neutral decider, no review. *Ask:* who decides, on what standard, and what stops a self-serving decision?
- **E. Gap / silence** — a situation the text does not address: a required precondition never guaranteed to occur, a missing remedy, a missing fallback. *Ask:* for every required step, what governs if it is skipped, only partly done, or impossible? For every duty, is the consequence of breach stated?
- **F. Cross-clause tension** — a power granted in one place quietly erodes a protection promised in another; both are individually valid, but together one swallows the other. *Ask:* does a power in provision A let an actor nullify what provision B promised? (This family has a *vertical* form — a power in a lower instrument eroding a higher one — used by the regulation profile.)

Families overlap by design. Aim for coverage, not clean partitions.

### Universal trigger lexicon

Flag a unit for inspection when it contains:

- *Discretion words* — "sole discretion," "in its discretion," "as it determines," "satisfactory to," "deem" → Family D.
- *Deferred-term words* — "to be established," "to be determined," "to be agreed," "as mutually agreed" → Family E.
- *Unquantified qualifiers* — "substantial," "significant," "material," "reasonable," "promptly," "customary," "appropriate" → Family B.
- *Open-list words* — "including without limitation," "such as," "and the like" → Family C.
- *Override words* — "notwithstanding," "supersedes," "except as," "at any time" → Family A.
- *Unilateral-change words* — "from time to time," "as designated by," "as assigned," "may amend or modify" → Family F.
- *Cross-reference and temporal words* — "subject to Section," "pursuant to," dates, named periods, durations, effective-date language → Families F and A, plus date-math checks.

The profile's reference file adds domain-specific trigger words to this list.

### Diagnostic battery

Run seven questions over every flagged unit and over the whole text: the six family questions above, plus a seventh — **term consistency:** is each defined term used consistently, and do undefined near-synonyms appear that an adversary could argue mean something different? A unit that survives all seven is sound. A unit that fails one is a scenario candidate. The profile adds its own family questions to the battery.

## Step 3 — Construct

Finding the defect is half the skill; turning it into a scenario a non-specialist instantly understands is the other half. Five rules govern construction.

- **Aim at the edge case.** Never pick facts that fall comfortably inside or outside a term. Pick facts that land *on the line* — the one fact pattern that makes the seam load-bearing.
- **Steel-man both sides.** Every scenario ends with two positions, each colorable, each citing real text, each able to plausibly win. **The central quality bar: a good scenario is one a competent tribunal could decide either way.** If one side obviously prevails, sharpen the facts until the contest is genuine, or drop the scenario.
- **Frame the dispute.** Two readings, opposed, mutually exclusive, with a concrete consequence turning on the answer.
- **Use the text's own world.** Real parties, real subject matter, realistic facts — a memo from the future, not an abstract hypothetical.
- **Keep the facts minimal.** Three to six sentences. Only what creates the dispute; no atmosphere, no backstory.

**Narrative template.** Sentence 1–2: the triggering event. Sentence 3: the first interpreter's position and the consequence claimed. Sentence 4: the second interpreter's counter-position. The narrative stops mid-dispute — it poses the question; the analysis layer answers it.

**Gauntlet.** The statute and regulation profiles add a *canon gauntlet*, and the opinion profile a *precedent gauntlet*: run each candidate ambiguity through the profile's interpretive doctrines and keep it only if it remains genuinely contestable *after* those doctrines are applied. An "ambiguity" the doctrines would dispatch in one paragraph is a false positive — drop it. The contract profile has no gauntlet; four-corners resolution is acceptable there.

## Research and sources

Applies to the **statute, regulation and opinion** profiles. The contract profile resolves from the instrument itself and skips this section entirely — do not spend effort surveying sources for a contract audit.

The doctrines dispatch some false positives; existing case law dispatches others. A seam a court has already construed is not a live disagreement, and reading the instrument alone will never reveal that. This step exists to catch that class of false positive, and nothing more.

### Which source to use

Take the first of these that applies. Decide once per audit, not once per scenario.

1. **The user's instruction wins.** If the user names a source — "use CourtListener," "use Descrybe," "just use the web," "skip the research" — do that. If the named source turns out to be unavailable, say so plainly and ask whether to fall back. Never substitute one source for another silently: a user who asked for a particular database and got something else has been given a result they cannot calibrate.
2. **Otherwise, use what is connected.** Before scanning, check what research tools this session actually has. Look for a legal-research connector — CourtListener, Descrybe, Midpage, Lexis and similar all serve — and use the first suitable one.
3. **Otherwise, use ordinary web search.** It is weaker than a legal database but adequate for the central question: has a court already construed this language?
4. **Otherwise, proceed from the text alone**, and say so in the output.

### What to look for

- Whether a court has already construed the contested language, in which case the scenario is dead and should be dropped.
- Whether provisions elsewhere in the same code, or the enabling act above a regulation, resolve what the excerpt leaves open.
- For an opinion: how later courts have read it, and whether it has been narrowed, distinguished or overruled. A prediction about an opinion's future reach is worthless if the opinion no longer stands.

### Naming doctrines, not cases

Prefer the doctrine to the citation. The `likely_outcome` field calls for the interpretive doctrine that drives the prediction — *ejusdem generis*, the rule of lenity, *contra proferentem*, the presumption against surplusage. Doctrines are stable; case citations go stale, and an unverified one is worse than none.

Name a specific case only where the research step actually verified it in this session. Where a scenario's outcome would turn on a case that could not be verified, state the doctrine and mark the case as unverified rather than dropping it silently.

### Say what happened

Every audit ends with one line naming the source used — or stating that none was available and that the scenarios were not checked against existing case law. Two people auditing the same statute, one with a legal-research connector and one without, will get different results. That is expected. It only looks like unreliability when the output does not say which run produced it.

## Step 4 — Output

Emit each scenario as a record with seven fields. The first three are the visible "card"; the last four are the analysis layer.

| Field | Content |
|-------|---------|
| `title` | ≤ 8 words, naming the defect category in plain language |
| `narrative` | 3–6 sentences, the Step 3 template, present tense, neutral voice |
| `anchors` | one or more provision IDs (native citations, not positional guesses); multiple anchors = a cross-clause or cross-instrument defect |
| `defect_family` | one universal family or a profile-specific family |
| `weak_point` | one sentence naming the precise textual flaw |
| `likely_outcome` | predicted resolution and the interpretive doctrine that drives it — **supplied by the profile** |
| `redraft` | proposed replacement or added language that closes the seam, in the profile's drafting register |

Only `likely_outcome` and the register of `redraft` are domain-specific; the core produces everything else unchanged. The judicial-opinion profile modifies this schema (a `redraft` becomes a tightening of the opinion, or in retrospective mode is replaced by an argument pair) — see `resources/opinion.md`.

Hedge predicted outcomes; they are predictions, not pronouncements. When the user asks for an audit rather than highlights, **report coverage** — every defect the scan surfaces — not just the marquee few.

Close every audit with a one-line **sources note** recording what the research step used, per "Say what happened" above. On a contract audit the note reads that the instrument was read on its own terms and no research step applies.

## Scope — what this skill does not do

The skill detects **interpretive ambiguity**, not **validity**. A contract can be perfectly clear and wholly unenforceable; a statute can be unambiguous and unconstitutional. Run from the four corners, the detector will not catch either — clarity is not legality. The statute and regulation profiles reach slightly outside the text where their domain demands it (constitutional-avoidance and ultra vires families), but that is ambiguity-detection shading into validity, not a systematic legality audit. If the user wants a validity or enforceability opinion, say so plainly and treat it as a separate pass.

## Jurisdiction

The detector is jurisdiction-neutral. The six defect families, the trigger lexicon and the seven-question battery work on any normative text in English, because they turn on how language behaves rather than on whose law governs.

The resolvers are not. All four profiles run on United States doctrine — the canons of construction, the enabling-act and ultra vires frame, and the American law of precedent — and the worked examples are United States materials. Outside that system the scanning half transfers and the `likely_outcome` half does not. When the text is plainly from another jurisdiction, run the scan, and either state that outcomes are predicted on a United States interpretive frame or substitute the local doctrines and say so.

## Bundled resources

Read the one profile matching the document; do not read all four.

- `resources/contract.md` — contracts, agreements, leases, policies, terms of service.
- `resources/statute.md` — statutes, code sections, ordinances, enacted bills.
- `resources/regulation.md` — agency rules and administrative code; builds on the statute profile, which must be read as well.
- `resources/opinion.md` — judicial opinions, including drafts; carries the two output modes and a worked example.

## Limitations and risks

This skill produces interpretive analysis of a legal text. It is not legal advice, it does not determine anyone's rights, and its predicted outcomes are predictions rather than answers. Nothing it produces should be filed, relied upon, or sent to a counterparty without a lawyer's own reading of the instrument.

Five risks are worth naming.

**Predictions are hedged for a reason.** The `likely_outcome` field states how the governing doctrines would probably resolve a seam. Courts resolve seams differently, and a scenario built precisely so that either side could win is by construction one whose outcome is uncertain.

**Currency depends on the research step.** Without a legal-research source, the skill has no way to know that a court already construed the language, or that an audited opinion has been narrowed or overruled. The sources note discloses which run produced the audit; read it before relying on the result.

**False negatives are invisible.** The scan finds defects reachable from the text and from whatever research ran. A defect that depends on trade usage, on a course of dealing between the parties, on an unprovided schedule or exhibit, or on an unresolvable cross-reference will not appear — and its absence looks identical to its non-existence.

**False positives survive in proportion to what was checked.** The doctrinal gauntlets drop ambiguities the canons would dispatch; only the research step drops ones the case law has already dispatched. A four-corners-only run will over-report.

**Scenarios are adversarial constructions.** Each is built to make a genuine contest out of an edge case, which means the facts are chosen for difficulty rather than for likelihood. A seam that would rarely arise in practice can read as urgent. Weight them accordingly.

The skill contains no executable code, makes no network calls of its own beyond whatever research tool the host provides, and moves no data outside the session.
