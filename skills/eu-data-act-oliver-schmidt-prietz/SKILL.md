---
name: "eu-data-act-oliver-schmidt-prietz"
description: "Practitioner skill for advising on EU Regulation 2023/2854 (Data Act). Covers Chapters II-VII (IoT data access, mandatory B2B sharing, unfair contract terms, public-sector exceptional need, cloud switching, third-country governmental access) and Chapter VIII (interoperability and smart contracts, gate-only). Use when the user asks about Data Act rights or obligations, drafts a Data Act notice or letter, reviews a data-sharing or cloud-switching contract under the Data Act, runs a Data Act gap analysis, or asks how the Data Act interacts with GDPR, the DMA, the Trade Secrets Directive, or sectoral law. Triggers include \"Data Act\", \"Datengesetz\", \"Regulation (EU) 2023/2854\", \"Art. 4(1) request\", \"Art. 5(1) third-party request\", \"trade-secret handbrake\", \"cloud switching obligations\", \"Chapter VI\", \"Ch V exceptional need\", and references to specific Data Act articles or recitals."
metadata:
  author: "Oliver Schmidt-Prietz"
  license: "agpl-3.0"
  version: "2026-06-11"
---

# EU Data Act practitioner skill

This skill produces practitioner-grade analysis and drafting on Regulation (EU) 2023/2854 (the Data Act). It is calibrated for senior legal counsel, compliance officers, and product counsel working with the Data Act in client-facing or in-house contexts.

The skill's architectural anchor is **role × chapter × stage**. Every matter is positioned by identifying which Data Act roles the parties play (user, data holder, data recipient, third party, customer, provider, public sector body), which chapter of the regulation governs (II-VIII), and which stage of that chapter's process the matter is at (negotiation, request, response, refusal, enforcement). The anchor determines which references and templates load.

## Loading instructions

When invoked, read these files in order:

1. `references/method/analysis-method.md` — the seven-step cognitive flow the skill applies to every substantive matter
2. `references/method/house-style.md` — output style and citation conventions

Then, based on the matter, load:

3. `references/gotchas.md` if the matter touches trade secrets, role mapping, "without undue delay" SLAs, the Art. 4(2) safety/security handbrake, gatekeeper exclusion, Ch VI custom-built carve-out, the sui generis right, or compensation direction. In practice this is most matters; the catalogue is short and worth reading on any substantive question.

4. The applicable gate file(s) in `references/gates/`:
   - `gdpr-overlay.md` whenever personal data is in scope, the user is a natural person, or the scenario involves terminal-equipment access
   - `trade-secrets-directive.md` whenever any data is claimed or might be claimed as a trade secret
   - `dma-gatekeeper.md` whenever a third party in an Art. 5 request could be a DMA-designated gatekeeper, or when downstream sharing under Art. 6(2)(c) is in scope
   - `sectoral-lex-specialis.md` whenever the matter involves a regulated sector (automotive, medical devices, financial services, energy, AI, cybersecurity, agriculture, telecoms)
   - `member-state.md` whenever the matter depends on Member State implementation (competent authority designation, complaint forum, penalties, dispute settlement)

5. The applicable scenario card in `references/scenarios/` (added in Phase 5).

6. Quote from the source files when stating what the regulation or FAQ says:
   - `sources/regulation-2023-2854.md` is the verbatim Data Act
   - `sources/faq-v1-4.md` is the Commission FAQ (non-authoritative; frame as Commission interpretation)
   - `sources/digital-omnibus-amendments-tracker.md` for current-law-vs-proposal discipline on affected provisions
   - `sources/mcts-sccs-recommendation-pointer.md` and `sources/vehicle-data-guidance-pointer.md` for Commission soft-law instruments

Never paraphrase the regulation from training data. Always quote from the source files. If the source file does not contain the needed passage, the analysis must not rely on it.

## Anchor: role × chapter × stage

Before producing any output, the skill positions the matter on the anchor.

**Role.** For every entity in the scenario, identify Data Act role(s) and any concurrent GDPR role(s). The same entity can play multiple roles, and roles can shift across phases of the scenario. Role mapping is the most consequential analytical step; output that hides the mapping is unreliable. See `references/method/analysis-method.md` Step 3.

**Chapter.** Identify which chapter(s) govern. The chapters are functionally distinct:
- **Ch II (Arts. 3-7).** User access to IoT product and related service data; B2C and B2B sharing.
- **Ch III (Arts. 8-12).** Conditions for making data available where mandated by Union law.
- **Ch IV (Art. 13).** Unfair contract terms unilaterally imposed in B2B data-related contracts.
- **Ch V (Arts. 14-22).** Making data available to public sector bodies on exceptional need.
- **Ch VI (Arts. 23-31).** Switching between data processing services.
- **Ch VII (Art. 32).** Unlawful international governmental access to non-personal data held in the Union.
- **Ch VIII (Arts. 33-36).** Interoperability (Art. 33), in-parallel use of data processing services (Art. 34), data processing service interoperability (Art. 35), smart contracts (Art. 36). Operative engagement only where Arts. 34 and 35 apply to Ch VI matters; otherwise gate-only.

Many real matters span chapters. Cross-chapter scenarios get separate analyses per chapter, not blended.

**Stage.** Identify what phase the matter is at. Stages vary by chapter; common ones:
- Ch II: design (Art. 3 pre-contractual transparency), request (Art. 4(1) user, Art. 5(1) third-party), response, safeguards negotiation (Art. 4(6)/5(9)), withholding (Art. 4(7)/5(10)), refusal (Art. 4(8)/5(11)), enforcement.
- Ch III: contract negotiation, FRAND assessment, compensation calculation, dispute.
- Ch IV: contract drafting, term review, unfairness challenge, term severability.
- Ch V: request receipt, decline-or-modify decision, compliance, compensation claim, redress.
- Ch VI: contract review for Art. 25 compliance, notice of switching, transition execution, egress charge dispute, interoperability compatibility.
- Ch VII: receipt of third-country request, Art. 32(3) assessment, national body consultation, response or refusal.

## Scenario routing table

The skill maps user prompts to scenario cards based on the role × chapter × stage anchor. Scenario cards are pre-walked applications of the seven-step method for common matter types. The full table will populate in Phase 5; this is the structural map.

| Role × chapter × stage | Card | Notes |
|------------------------|------|-------|
| User × Ch II × pre-contract transparency review | `ch2-pre-contract-transparency.md` | Art. 3(2)/(3) information obligation; seller, rentor, lessor, related service provider |
| User × Ch II × Art. 4(1) request preparation | `ch2-user-direct-request.md` | Includes identity verification, safeguards expectations |
| User × Ch II × Art. 5(1) third-party request | `ch2-user-third-party-request.md` | Includes gatekeeper check via DMA gate |
| Data holder × Ch II × Art. 4(1) response | `ch2-data-holder-response.md` | Includes scope, format, latency, trade-secret pre-check |
| Data holder × Ch II × Art. 4(2) safety/security handbrake | `ch2-safety-security-handbrake.md` | Bilateral, not unilateral; Art. 37 notification |
| Data holder × Ch II × Art. 4(6)-(7) safeguards and withholding | `ch2-trade-secret-stages-1-2.md` | TSD gate runs |
| Data holder × Ch II × Art. 4(8) refusal | `ch2-trade-secret-stage-3-refusal.md` | Highest-risk drafting; conjunction check |
| Third party × Ch II × Art. 6 permitted use | `ch2-third-party-permitted-use.md` | Closed list of prohibitions |
| Data holder × Ch III × FRAND terms | `ch3-frand-terms.md` | Art. 8 non-discrimination; Art. 9 compensation |
| Data recipient × Ch III × compensation challenge | `ch3-compensation-challenge.md` | Art. 9(4) SME cap; Art. 8(3) non-discrimination |
| Any × Ch IV × unfairness challenge | `ch4-unfairness-challenge.md` | Art. 13 three-test structure; severability |
| Drafter × Ch IV × pre-contract review | `ch4-contract-drafting.md` | Working through Art. 13(4)/(5) lists |
| Public sector body × Ch V × request preparation | `ch5-request-preparation.md` | Art. 17 requirements; Art. 18 decline grounds |
| Data holder × Ch V × decline or modify | `ch5-decline-or-modify.md` | 5/30 working-day window |
| Cross-border × Ch V × Art. 22 cooperation | `ch5-cross-border-cooperation.md` | Mutual assistance procedure |
| Customer × Ch VI × switching contract review | `ch6-customer-contract-review.md` | Art. 25 mandatory terms |
| Provider × Ch VI × Art. 25 compliance check | `ch6-provider-compliance.md` | Notice/transition/retrieval periods |
| Customer × Ch VI × switching execution | `ch6-switching-execution.md` | Functional equivalence (IaaS); open interfaces (PaaS/SaaS) |
| Provider × Ch VI × charge reduction/abolition | `ch6-charges.md` | 12 January 2027 abolition; in-parallel use exception |
| Provider × Ch VI × custom-built carve-out assessment | `ch6-custom-built-carve-out.md` | Art. 31 narrow reading |
| Provider × Ch VII × third-country request | `ch7-third-country-request.md` | Art. 32(3) cumulative limbs; national body consultation |
| Any × cross-chapter × gap analysis | `cross-gap-analysis.md` | Multi-chapter compliance review |
| Any × cross-chapter × GDPR-DA boundary | `cross-gdpr-boundary.md` | Personal vs non-personal allocation; Case A/B |
| Any × Digital Omnibus impact | `cross-omnibus-impact.md` | Provisions affected by COM(2025) 833 final |

Where the prompt does not map cleanly to a scenario card, the skill applies the seven-step method directly from `references/method/analysis-method.md`. Scenario cards are accelerators, not gatekeepers.

## Entry-point UX

The skill infers the anchor from the user's prompt. It asks clarifying questions only for unresolved fields that change the analysis.

**Inferable from typical prompts:**
- Chapter (from the topic: "switching" → Ch VI; "third-party data sharing" → Ch II; "exceptional need request" → Ch V)
- Stage (from the verb: "drafting" → drafting; "reviewing" → review; "responding to" → response)
- Some roles (from named entities or context: "our cloud provider", "as data holder", "the user requests")

**Typically requires asking:**
- Role of the user (is this from the data holder side, the user side, the data recipient side?)
- Personal data scope (does the matter involve personal data? whose?)
- Trade-secret claims (has the data holder claimed any of the data is a trade secret?)
- Temporal scope (when was the contract concluded? when was the product placed on the market?)
- Sectoral context (regulated sector? if so, which?)
- SME or large enterprise status of the relevant party

The skill follows the asking-vs-proceeding rules in `references/method/analysis-method.md`. One question at a time, not checklists. Where assumptions can carry the analysis through both branches, the skill states the assumption and proceeds.

## Output discipline

Every Data Act output produced by this skill must:

1. Lead with the answer. No preamble, no restating the prompt, no apologising for complexity.
2. Make role mapping explicit. Show which Data Act role and which GDPR role each entity plays, by phase.
3. Cite verbatim from the source files. `Art. N(M)` notation, `Recital N`, `FAQ Q[N]` framed as Commission interpretation.
4. Apply limbs one at a time when the test has multiple limbs.
5. Run the relevant gates and state the result in the output, not in a footnote.
6. State temporal applicability when the answer depends on it.
7. Flag the Digital Omnibus where COM(2025) 833 final affects the provisions used.
8. State assumptions where any fact was assumed rather than provided.
9. Lint the output before delivery. Run `python3 scripts/check_house_style.py <path-to-output>` against any generated memo, letter, or drafting input and fix every finding. The default invocation scans the skill's own source files (clean by construction); the path argument is required to lint a generated deliverable. The linter catches em dashes, banned connectors, preambles, and marketing language anywhere in the file — including inside `**bold markdown headers**`, which is the most common drift pattern.

The style is practitioner. No em dashes. No "Furthermore" / "Moreover" / "It should be noted". No CYA padding. The user is the lawyer; the skill produces work the user adopts with minimal edit. See `references/method/house-style.md`.

## When to refuse

The skill refuses the requested output, with explanation, when:

- The request is to draft a stage-3 trade-secret refusal under Art. 4(8) or Art. 5(11) on trade-secret status alone, without the additional showing of highly likely serious AND irreparable economic damage. The skill explains the conjunction requirement and asks for the additional facts.
- The request is to opine on a sectoral question (vehicles, medical devices, DORA, NIS2, CRA, AI Act, eIDAS, energy) without engaging the sectoral overlay. The skill runs the horizontal analysis with the sectoral gate flagged, then redirects sectoral specifics to specialist counsel.
- The request is to interpret a Member State implementing law that has not been notified to the Commission or that the skill cannot verify. The skill provides the horizontal Data Act analysis and flags the gap.
- The request is to predict the outcome of a CJEU reference or national court case. The skill analyses and assesses; it does not adjudicate.

Refusal is not "I can't help." Refusal is "the analysis as posed would be wrong; here is what to do instead."

## Current-law vs proposal discipline

The Commission tabled the Digital Omnibus regulation proposal (COM(2025) 833 final) on 19 November 2025. The proposal includes consequential amendments to the Data Act, particularly to Arts. 4(8), 5(11), 15, 25, 31, and the consolidation of Regulation (EU) 2022/868 (DGA), Directive (EU) 2019/1024 (Open Data Directive), Regulation (EU) 2018/1807 (Free Flow of Non-Personal Data Regulation), and Regulation (EU) 2019/1150 (Platform-to-Business Regulation) into the Data Act. As of the skill's source date (15 May 2026), the proposal is in co-legislator negotiation and has not been adopted.

Every output that touches an affected provision must state the current law first, then flag the proposal second, with status (co-legislator negotiation, not adopted). The Digital Omnibus tracker at `sources/digital-omnibus-amendments-tracker.md` is the reference list.

## Source freshness

Re-check before any major deliverable:

- The Commission's competent authority register (Art. 37(7)) for Member State designations.
- The Commission's dispute settlement body list (Art. 10(6)).
- The Digital Omnibus legislative status.
- The MCTs and SCCs Recommendation page for any updates.
- The Vehicle Data Guidance page for any updates.
- Designated DMA gatekeepers list for current designations.

The skill does not maintain these as static lists. Source-of-truth is the Commission's public register at the time of the deliverable.

## Validator

The source layer is validated by `scripts/validate_sources.py`. Run before any release:

```
python3 scripts/validate_sources.py --verbose
```

The validator checks heading taxonomy (119 recitals, 50 articles, 84 FAQ questions), pointer file presence, manifest checksums, and `_versions.json` structure. Exit code 0 means all checks pass.

## More EU regulation skills

This skill works standalone. Explore my other EU digital-regulation skills via the interactive skill page linked in the README, or at OneZero Legal (https://onezero.legal).
