# Arbitration Clause Design and Review — Changelog

---

## v0.8.1

Clarified the Arbitration Costs Calculator integration to distinguish the human-facing calculator page from the machine-readable specification page; updated cost-calculation instructions, sources, examples and QA scenarios accordingly.

- Updated the cost comparison runtime hierarchy in SKILL.md to use the machine-readable specification page (https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/) as the machine/runtime calculation path, and the human-facing calculator page (https://virjee-arbitration.com/arbitration-costs-calculator/) as the human fallback. Removed the implication that the interactive form of the human-facing page is the primary machine path.
- Added a note to the Arbitration Costs Calculator scope section in SKILL.md clarifying the two-page architecture and confirming that no server-side result endpoint exists.
- Updated sources.md Section 4 to name both pages with their respective roles, and expanded maintenance checklist item 14 to cover both URLs.
- Added a sentence to README.md noting the machine-readable specification page for tool/runtime use.
- Removed an unlabelled duplicate of the cost-comparison example that had been left in examples.md between Example 11 and Example 12.
- Updated Example 13 in examples.md to reflect the two-path approach: machine-readable specification for direct calculation; human-facing page as fallback.
- Updated QA Scenarios 30–33 and 36–39 in qa-scenarios.md so that expected behaviour, output criteria and pass criteria reflect the two-path logic, no server-side endpoint, and no reliance on query URLs as guaranteed machine-result endpoints.

---

## v0.8

Arbitration Costs Calculator integration.

- Added the Arbitration Costs Calculator (https://virjee-arbitration.com/arbitration-costs-calculator/) as the preferred consolidated source for institutional/administrative and tribunal fee estimates for ICC, HKIAC, SIAC, DELOS and the Swiss Arbitration Centre (SAC).
- Updated the cost-comparison runtime hierarchy so that the Arbitration Costs Calculator is attempted first for the five supported institutions; individual institutional calculators remain as fallback and verification sources.
- Added cost-calculation assumption rules covering amount in dispute (including use of contract value as proxy), currency handling for supported and unsupported currencies, and procedure/tribunal-size defaults.
- Added scope guidance: the calculator estimates institutional/administrative and tribunal fees; it does not estimate total arbitration costs or arbitrator remuneration; it has a supported amount range beyond which the skill does not extrapolate.
- Updated sources.md to add the Arbitration Costs Calculator as a prominently listed source and to reclassify individual institutional calculators as fallback and verification sources.
- Updated README.md to reflect the Arbitration Costs Calculator as the preferred source for the five supported institutions.
- Added QA Scenarios 30–39 covering calculator integration, currency handling, scope limitations, and edge cases.
- Added Example 13: cost comparison using the Arbitration Costs Calculator.

---

## v0.7.5

Seat selection and output structure improvements.

- Seat candidates must now respond to a specific fact in the transaction. Generic global shortlists are not permitted.
- Seats are named at city level in clause drafting and analysis (Port Louis, Kigali, London, Paris).
- Regional institution scenario outputs now lead with a practical recommendation and complete clause where sufficient information is available, followed by brief reasoning and a concise alternatives list. Where a genuine strategic choice remains open, an options-based structure is used instead.
- Cost comparison outputs follow a clear hierarchy: attempt live calculator first; if unavailable, identify the required comparison and provide calculator links; never estimate.
- GAP materials, once retrieved and used, do not require a further general review caveat. Specific legal flags are reserved for specific identified issues.
- Expedited procedure thresholds are not hardwired; the applicable threshold depends on the institution, rules version, and date of the arbitration agreement. SIAC's three-tier procedure structure (Streamlined, Expedited, standard) is noted as a material differentiator.
- Cost calculator guidance in sources aligned with the binary calculator rule introduced in v0.7.4.
- Three residual fee-schedule references removed from the Time, cost and dispute value section. Permitted cost-figure sources are now stated consistently throughout: live calculator run, official calculator output, or stored verified example.

---

## v0.7.4

Analytical discipline and output quality improvements.

- The skill now extracts claimant/respondent posture, relationship duration, payment structure, and governing law context from available information before asking follow-up questions.
- Seats and institutions are treated as separate analytical choices throughout. They are never bundled in shorthand.
- GAP materials now appear as clickable hyperlinks in the output. Where a live jurisdiction chapter is found, the specific chapter link is included. Where not found, the GAP jurisdiction-analysis page is linked with a brief note.
- Cost figures must come from a live calculator run or a verified stored example with stated assumptions. Scale-based estimation from fee schedules is not permitted.
- Market preference claims require a citable source and calibrated language. Unsupported generalisations are not permitted.
- Where the governing law analysis identifies the controlling party's law as the natural starting point, any departure to a neutral third-country law must be supported by a stated positive justification.

---

## v0.7.3

GAP output links.

- Where GAP materials are relied on, clickable links to the relevant public resources are now included directly in the output: the traffic-light table where seat assessment is relevant, and the GAP jurisdiction-analysis page or specific chapter link where applicable. Chapter-author firms are not named in default outputs.

---

## v0.7.2

Institution selection and non-EMEA coverage.

- Institution selection no longer infers party preferences from nationality. Where party familiarity matters and no user-provided information is available, institutions are presented by role: conventional global option, regionally coherent neutral option, party-home option, proportionate-process option, sector-specific option.
- New worked example: Korea/Turkey franchise agreement demonstrating role-based institution selection and Korean law as the governing law starting point.
- New QA scenario covering non-EMEA transactions and role-based institution selection.

---

## v0.7.1

Institution selection calibration and cost-rule alignment.

- Institution selection now requires justification by transaction profile and user priorities. No institution is selected by default.
- Cost comparison surfacing aligned with the conditional rule introduced in v0.7: internal sense-check always; public output only where relevant criteria are met.
- New worked example: Italy/Egypt franchise agreement demonstrating Italian law as the governing law starting point and criteria-based institution selection.

---

## v0.7

Cost comparison discipline and output structure.

- Cost sense-check is now always performed internally where a value is available. Public surfacing is conditional: cost predictability, proportionality, access to justice, Delos on the shortlist, or user request.
- Regional institution proposal scenarios remain a specific exception: the cost comparison appears in the main answer where a value is available.
- Design Path outputs lead with the clause. Review Path outputs lead with the overall assessment.
- Seat selection, language of arbitration, and alternative institution selection all require positive justification tied to the transaction.

---

## v0.6

Governing law framework and attribution.

- Governing law analysis now follows a structured five-step framework: legal family of the parties; commercial leverage and subject matter control; place of performance; coherence with the seat; recommendation.
- Author attribution simplified to name only; fuller attribution in the README.
- Duration statistics reframed as most recently published relevant figures, with an instruction to verify before use.

---

## v0.5

Multilingual support and North American coverage.

- Where the user is working in a language other than English, the skill notes that most major institutions make their rules and model clauses available in multiple languages.
- AAA-ICDR and JAMS added as live options for contracts with a North American nexus.

---

## v0.4

SOE counterparties and multi-party architecture.

- Contracts involving SOEs and public bodies are not automatically outside scope. The skill assists with the commercial arbitration clause while flagging immunity, authority, procurement, and enforcement issues for specialist advice.
- Multi-party and multi-contract scenarios receive the commercial arbitration architecture before any specialist referral.

---

## v0.3.1

Institutional neutrality.

- Bias safeguards refined to apply symmetrically: no automatic inclusion of any institution, and no omission of relevant options where they match stated priorities.

---

## v0.3

DELOS COMARB, GAP chapter routing, and clause validity rating.

- DELOS COMARB flagged as a sector-specific option for commodity trading in energy and mining.
- GAP chapter routing: the skill checks the GAP jurisdiction-analysis page for live chapters and links them where available.
- Red / potentially void introduced as a severity rating distinct from Red / serious issue, for clauses that may not constitute a valid arbitration agreement at all.

---

## v0.2

Regional institution proposal structure.

- Where a counterparty proposes a regional institution, outputs follow a mandatory scenario framework: counterparty-proposed option, conventional international option, and a time- and cost-disciplined administered option.

---

## v0.1

Initial public release.

Core design path and review path. Seat assessment with GAP integration. Institution and rules selection. Governing law companion clause. Confidentiality. Tiered dispute resolution. Bias and credibility safeguards.
