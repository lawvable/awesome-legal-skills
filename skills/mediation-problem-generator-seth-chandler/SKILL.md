---
name: mediation-problem-generator
description: >-
  Create original, competition-ready commercial mediation problems and confidential packets
  with iterative validation. Use when a user provides a topic, industry, dispute sketch, or
  existing general-information packet and wants a public packet plus confidential packets for
  both sides—or one named side. Build a narrow but workable settlement corridor; verify factual
  and numerical consistency, information asymmetry, balance, originality, and commercial
  feasibility; and revise until deterministic and semantic exit criteria pass. Do not use merely
  to summarize an existing packet or to advise parties in a real dispute. Requires local file
  access; Python 3 is recommended for bundled deterministic checks, with disclosed manual
  fallbacks when unavailable.
metadata:
  author: "Seth J. Chandler"
  author_link: "https://legaled.ai"
  license: "Apache-2.0"
  version: "2026-08-07"
  jurisdiction: "All"
  language: "English"
  category: "legal-education"
  requires: "Local file access; Python 3 recommended"
---

# Mediation Problem Generator

Create original, competition-ready commercial mediation materials. Treat internal consistency, balanced difficulty, and a narrow but workable settlement corridor as design requirements rather than cleanup tasks.

## Load the Required Guidance

Read all four references before drafting:

- `resources/case-model-schema.md` for the author-only source of truth.
- `resources/design-grammar.md` for problem construction and originality rules.
- `resources/packet-templates.md` for the public and confidential packet structures.
- `resources/semantic-audit.md` for balance, feasibility, and exit criteria.

Before promising outputs, confirm that the host can read and write local files. Python 3 is
recommended for the bundled deterministic checks. If Python is unavailable, perform the manual
fallbacks described below and state in the delivery summary which scripts were not run.

## Select the Entry Route

### Route A - Sparse Prompt to Full Package

Use when the user supplies a topic area, industry, relationship, dispute seed, or short sketch.

Produce by default:

1. `case-model.json` - author-only; never distribute to participants.
2. `general-information.md` - available to both parties.
3. `confidential-information-party-a.md`.
4. `confidential-information-party-b.md`.
5. `validation-report.md` - author-only.
6. `clarification-risk.md` - author-only.

Make reasonable creative assumptions. Ask a question only when a missing choice would materially change the exercise and guessing would create a substantial risk of divergence. Otherwise state the assumptions in the author-only model and continue.

### Route B - General Packet to Confidential Packets

Use when the user provides a general packet in PDF, DOCX, Markdown, or text.

1. Extract and inspect the complete packet using whatever document-reading capability the host
   provides. If the host cannot reliably read the format, ask the user for extracted text or a
   supported conversion; do not claim to have inspected content that was unavailable.
2. Reconstruct all public facts in `case-model.json` without changing them.
3. Design the hidden settlement architecture for both sides together.
4. Generate both confidential packets by default.
5. If the user requests one named side only, deliver only that packet, but still design both sides' private constraints and the full settlement corridor in the author-only model. Do not generate or expose the unrequested packet.

Never repair, contradict, or silently supplement a supplied public fact in a distributed packet. Record defects or necessary assumptions in `validation-report.md` and, if material, ask the user before finalizing.

## Build the Canonical Model First

Never draft the distributed packets independently. Create `case-model.json` first and record:

- objective public facts and chronology;
- party identities, roles, authority, and relationships;
- claims, defenses, and deliberately unresolved legal questions;
- financial data and calculation rules;
- each side's positions, interests, constraints, targets, reservation conditions, BATNA, and WATNA;
- fact visibility and epistemic status;
- protected interests that cannot simply be traded away;
- cross-trades, contingent terms, implementation mechanisms, and candidate packages;
- the intended settlement corridor and its failure boundaries.

Classify every material fact as `objective`, `belief`, `allegation`, `legal_uncertainty`, or `deliberate_ambiguity`. Classify visibility as `public`, `party:<party-id>`, `shared_private`, or `author_only`.

Use `<skill-dir>/scripts/scaffold_case_model.py` to create a starting model when useful. Resolve `<skill-dir>` to this skill's directory. Validate the model with `<skill-dir>/scripts/validate_case_model.py` after every material revision.

## Design a Narrow but Sound Settlement Corridor

Require all of the following:

- At least two and ordinarily no more than four materially different sound packages.
- No sound package that merely splits the public monetary positions without using confidential information.
- At least two linked concessions in each sound package.
- At least one value-creating, non-cash, contingent, relational, informational, or implementation term.
- A credible reason each party prefers settlement to its BATNA.
- A protected interest or hard constraint for each party.
- Enough overlap for agreement, but not enough for an obvious or costless agreement.
- No package that requires a party to promise money, authority, rights, performance, or information it does not possess.

Reject designs that are impossible, depend on one brittle hidden solution, make one side dominant on every dimension, or reveal the complete bargain merely by reading either confidential packet.

## Draft the Packets

Generate the public packet only from public fields in the model. Provide enough commercial, legal, financial, and relational context to make the dispute understandable without disclosing reservation values or intended trades.

Generate each confidential packet only from:

- the public model;
- that party's private facts;
- facts the party could reasonably know;
- its beliefs and allegations clearly labeled as such.

Write each packet in second person unless the user requests another convention. Give each side realistic internal tensions, priorities, and authority. Do not tell a party the other side's secret or prescribe a single settlement script.

Do not give both packets parallel menus of the same candidate packages. If one party has internally considered a direction, describe only that party's partial concept and the dependencies it cannot resolve alone. Present tradeable ingredients and constraints asymmetrically; leave package assembly to the mediation.

Follow `resources/packet-templates.md`. Preserve a supplied packet's style and naming conventions when using Route B.

## Run the Iterative Validation Loop

Repeat this cycle:

1. Validate `case-model.json` with:

   `python3 <skill-dir>/scripts/validate_case_model.py <case-model.json>`

2. Run the information-firewall check after drafting:

   `python3 <skill-dir>/scripts/check_information_firewall.py <case-model.json> <general.md> --party-a <party-a.md> --party-b <party-b.md>`

   When Route B produces one side only, supply only the corresponding `--party-a` or `--party-b` option.

3. Apply every semantic audit in `resources/semantic-audit.md`.
4. Record defects by severity in `validation-report.md`.
5. Revise the canonical model, not an isolated packet.
6. Regenerate every affected packet.
7. Repeat until the exit criteria pass.

Treat deterministic scripts as minimum checks. They do not replace semantic review.

### Manual fallback when Python is unavailable

Before delivery, manually verify the required top-level model fields, exactly two parties,
visibility and epistemic-status labels, required private-case fields, two to four candidate
packages, calculations and payment totals, the narrow-window settings, and the last two audit
iterations. Compare each distributed packet against the model's visibility labels for possible
leaks. Record that the manual fallback was used; never describe it as equivalent to running the
scripts.

## Use Information-Firewall Simulations

When independent agents are available, run role-limited audits:

- Party A auditor: general packet plus Party A packet only.
- Party B auditor: general packet plus Party B packet only.
- Mediator auditor: general packet only.
- Full-package auditor: case model and all packets.

Instruct role-limited auditors not to inspect the workspace or any unprovided artifact. If true file isolation is unavailable, pass only the permitted text and treat the exercise as an independence aid, not a security boundary.

Ask each side auditor to identify interests, constraints, likely proposals, apparent BATNA, confusing facts, and at least two sound settlement packages. Ask the mediator auditor whether the public problem supports productive negotiation without disclosing the answer. Ask the full-package auditor to test feasibility, balance, leaks, and contradictions.

If independent agents are unavailable, perform the same audits sequentially with fresh notes and strict information partitions.

## Enforce the Exit Criteria

Do not call the package final until:

- all deterministic errors are cleared;
- all high-severity semantic defects are cleared;
- the last two audit iterations introduce no new high-severity defect;
- each side-limited audit finds at least two plausible packages;
- the full audit confirms two to four materially different sound packages;
- no private fact leaks into the public packet or the opposing packet;
- all payments, valuations, ownership interests, dates, and authorities reconcile;
- likely clarification questions have answers or are intentionally designated as unresolved legal or factual ambiguities;
- the originality check finds no copied scenario, wording, distinctive combination, or numerical pattern from an example source.

Run the final deterministic check with:

`python3 <skill-dir>/scripts/validate_case_model.py <case-model.json> --final`

If five revision cycles do not satisfy the criteria, stop and report the remaining defects and the design choice needed. Do not conceal failure by weakening the rubric.

## Deliver Safely

Keep author-only artifacts separate from participant packets. Clearly label confidential packets and their intended recipient. Never combine both confidential packets in a participant-facing file.

Deliver Markdown by default. Create DOCX or PDF versions only when requested and when the host
provides a document-generation capability with visual verification. Otherwise deliver Markdown
and state that the requested conversion could not be completed in the current host.

Summarize:

- the selected entry route;
- the files created;
- the number of validation cycles;
- whether all exit criteria passed;
- any unresolved author judgment calls.

Use the model, validation report, and audit history to preserve continuity across revision cycles.

## Jurisdiction and professional use

This skill is jurisdiction-neutral because it designs fictional teaching simulations rather than
resolving substantive law. When a problem depends on actual doctrine, procedure, ethics rules, or
enforceability, the user must supply authoritative jurisdiction-specific sources or independently
verify the legal framework before distribution. The generated materials are educational exercises,
not legal advice or predictions about a real dispute.

## Bundled resources

- `resources/case-model-schema.md` — canonical author-only model; read before constructing a case.
- `resources/design-grammar.md` — originality, hidden-value, difficulty, and commercial-soundness
  rules; read before designing the settlement corridor.
- `resources/packet-templates.md` — distributed and author-only document structures; read before
  drafting packets or reports.
- `resources/semantic-audit.md` — severity rubric and exit criteria; use during every revision.
- `scripts/scaffold_case_model.py` — optional Python 3 utility that writes a starter JSON model to
  the caller-named path and refuses to overwrite unless expressly told to do so.
- `scripts/validate_case_model.py` — Python 3 deterministic validator; it reads a model and writes a
  report only when the caller supplies a report path.
- `scripts/check_information_firewall.py` — read-only Python 3 comparison for likely verbatim
  confidential-fact leakage.

## Limitations and risks

- The skill cannot establish that invented law, contractual language, industry practice, or
  financial assumptions are accurate without authoritative sources and human review.
- Deterministic validation catches structural and arithmetic defects, not every semantic leak,
  impractical bargain, unfair role, or pedagogical weakness. Role-limited audits remain judgment
  aids, and simulated agent separation is not a security boundary.
- Author-only models and opposing confidential packets can compromise an exercise if distributed
  to participants. Keep them separate and verify each delivery target.
- Do not place privileged, confidential, personal, or client information into an AI host unless
  authorized and consistent with the host's privacy, retention, and security terms.
- The output is a teaching simulation, not legal advice, a settlement recommendation, or a
  substitute for review by a qualified instructor or lawyer in the relevant jurisdiction.

The package contains three Python 3 scripts using only the standard library. They make no network
calls, spawn no subprocesses, access no credentials, and evaluate no dynamic code. The scaffold
writes only to the caller-named path; the validator writes only to an optional caller-named report
path; the firewall checker is read-only.
