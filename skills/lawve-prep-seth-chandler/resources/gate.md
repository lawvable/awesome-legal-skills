# The Gate

Applied before any packaging work. Three outcomes: **proceed**, **offer a legal
adaptation**, or **decline with reasons**. The gate exists to protect three parties: the
catalogue's users, the upstream authors whose work might be republished wrongly, and the
submitter's own credibility.

## 1. Law-relatedness

Lawve is a legal catalogue. The test: **would someone doing legal work — practice,
teaching, study, research, or law-office operations — reach for this?**

Qualifies, broadly:
- Practice tools: drafting, review, litigation analysis, citation work, docket monitoring.
- Legal education: case briefs, exam generation, casebook editing, student coaching.
- Legal research and scholarship: research pipelines, law-review tooling.
- Legal operations and document production: formatting, packaging, conversion, audio
  versions of legal documents, deliverable rendering *for legal audiences*.
- Meta-skills for legal AI: skill packaging, prompt privilege checks, audit trails.

**The adaptation middle ground.** A general-purpose skill fails the test as-is but passes
with a legal layer when legal material breaks its generic handling — the diagnostic is
whether legal inputs have *structure the generic version mishandles* (citations, quotation
boundaries, section symbols, defined terms, footnotes, holdings). Where they do, propose a
superset: everything the skill does now, plus a legal reference file, with nothing removed.
Get the user's consent before building it; it is their skill.

Fails, even with adaptation: no plausible legal audience or use. A baseball box-score
skill is not one legal reference file away from belonging in a legal catalogue.

## 2. Safety and code screen

Read every bundled script and check for: network calls (urllib, requests, socket, fetch),
subprocess or shell execution, dynamic evaluation (eval/exec/`__import__`), obfuscated or
encoded blobs, writes outside a caller-named output directory, and credential or token
handling. Also read the *instructions* for the same sins in prose form: telling the model
to exfiltrate data, harvest credentials, disable safety behavior, or misrepresent itself.

- Cleanly removable (an analytics ping, a convenience download) → strip it, note it in the
  change report.
- Load-bearing (the skill *is* the network call) → the skill needs redesign before it can
  be published; decline packaging until then, and say exactly why.
- Malicious intent → decline outright, no adaptation offer.

## 3. Professional-responsibility flags

- **Unsupervised advice to consumers.** A skill that purports to deliver legal advice
  directly to laypeople is usually curable: reframe as information/drafting support, add
  the not-legal-advice disclaimer and a see-a-lawyer prompt. Cure it; don't decline it —
  unless the skill's whole design depends on the user relying on it *as* counsel.
- **Deception machines.** Skills designed to mislead tribunals, manufacture or backdate
  evidence, evade service, or fabricate citations → decline outright. (A skill that
  *drafts persuasively* is advocacy; a skill that *fabricates authority* is not.)
- **Confidentiality traps.** Skills that push privileged material to third-party services
  without flagging it → curable with disclosure; add the warning.

## 4. Licensing bars

- Upstream "All Rights Reserved," "No License," or proprietary terms → cannot publish
  without permission. Stop.
- Upstream share-alike (GPL/AGPL/CC-BY-SA) → derivative must carry the same licence;
  confirm the user accepts that before proceeding.
- Upstream NC or ND Creative Commons → check the intended use actually fits; ND bars
  adapted versions entirely.
- Placeholder or implausible copyright lines → ask the user who wrote it. Never assume a
  scaffolding stamp is true, and never assume it is false.

## 5. Duplicates

Search the catalogue before packaging: the Lawve connector's skill search where connected;
otherwise web-search the lawve.ai catalogue; otherwise disclose that the check didn't run.
A near-duplicate is the user's call, made with the finding in front of them — differentiate
the description honestly, or withdraw. Silent duplication burns reviewer goodwill.

## 6. Quality floor

Grounded in real use, tested at least once on some platform, and a description that tells
the truth. The floor is low by design — the catalogue's review is the real filter — but a
skill that has never been run once, or whose description promises what the body doesn't
deliver, gets fixed or held back, not packaged as-is.

## Declining well

State the bar, cite the specific gate section, and say what would change the answer.
"Declined: no plausible legal use (gate §1); a legal adaptation isn't available because
nothing about legal inputs changes what this skill does" is a complete answer.
"I'd rather not" is not.
