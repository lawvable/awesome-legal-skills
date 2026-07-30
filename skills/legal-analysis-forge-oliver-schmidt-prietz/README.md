# legal-analysis-forge

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/EU-Legal-Analysis-Forge/)**

A **prompt forge** for structured legal analysis of EU digital regulation documents. Given a Regulation, Directive, Commission Guidelines, EDPB Opinion, CJEU judgment, AG Opinion, national DPA decision, code of conduct, harmonised standard, or draft consultation document, the skill characterises the document, elicits the desired deliverable, and produces a tailored expert prompt. The prompt can be executed in-session to generate the deliverable, and is always accompanied by a plain-English explainer for the practitioner using the skill.

For the full six-step workflow, see [SKILL.md](SKILL.md).
For version history, see [CHANGELOG.md](CHANGELOG.md).

## What this skill does

Given an EU digital regulation document and a deliverable type, the skill:

- **Characterises** the document — instrument type, binding force, issuer and legal basis, status, subject matter, sectoral interfaces, contestable interpretive moves, temporal application, plain-language summary.
- **Generates a tailored expert prompt** assembled from a role marker, document context, task description, analytical framework (general legal interpretation rules plus document-specific scrutiny points), citation conventions, register constraints, output structure, and a self-check protocol.
- **Optionally executes the prompt** in-session to produce the deliverable directly, applying the self-check before delivery.
- **Always produces a plain-English explainer** alongside the formal output; the user chooses whether to integrate it into the deliverable.

Deliverable types supported: stakeholder consultation response, internal compliance memo, external client memo, public commentary (LinkedIn / blog / newsletter), conference talk preparation, internal risk assessment, litigation brief input, comparative analysis, horizon-scan entry, skill input.

## Scope

EU digital regulation only: GDPR, AI Act, Data Act, DGA, DSA, DMA, NIS2 (incl. BSIG-neu), ePrivacy, CRA, DORA, eIDAS 2.0, PLD (Dir. 2024/2853), AI Liability Directive, and adjacent secondary instruments (delegated acts, implementing acts, harmonised standards, codes of conduct).

Out of scope: competition, IP, tax, employment, sectoral law not touching the digital stack. For operational compliance (DPIA, DPA drafting, AI Act obligations mapping, RoPA, breach response, NIS2 scoping), the skill routes to the relevant compliance skill in the portfolio rather than absorbing the task.

## Deployment

Place this skill in your Claude Code skill directory (`~/.claude/skills/` or workspace-level). Claude routes to it automatically when a user provides an EU digital regulation document and asks for structured analysis, a consultation response, a memo, a briefing, or comparable deliverable — in English or German. The skill does not require any external tool configuration beyond `WebFetch` (for live research) and `pdf-processing-anthropic` (for PDF ingestion); both are standard Claude Code capabilities.

Outputs are written to the user's current working directory by default.

## Disclaimer

This skill is not legal advice. It enforces interpretive discipline, citation hygiene, and an anti-hallucination protocol, but it does not guarantee accuracy. EU instruments evolve and only the CJEU can give authoritative interpretation. Use under qualified counsel.

## License

AGPL-3.0 (see repo-root LICENSE file).

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
