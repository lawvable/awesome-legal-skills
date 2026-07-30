# ai-act-high-risk

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/EU-AI-Act-Suite/ai-act-high-risk/)**

Depth assessment skill for the **EU AI Act high-risk classification under Art. 6** (Regulation (EU) 2024/1689), grounded in the European Commission's draft Art. 6(5) classification guidelines (general principles, Annex I, Annex III) published for stakeholder consultation in 2026.

For the full classification workflow, see [SKILL.md](SKILL.md).
For version history, see [CHANGELOG.md](CHANGELOG.md).

## What this skill does

Given an AI system description and intended-purpose evidence, determines whether the system is high-risk under:

- **Art. 6(1) + Annex I** — AI system as product or safety component of a product under Union harmonisation legislation requiring third-party conformity assessment.
- **Art. 6(2) + Annex III** — AI system falling into one of eight high-risk use-case areas (biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, justice/democracy), subject to the Art. 6(3) exception filter and profiling re-exception.

Outputs a structured decision block + practitioner memo + JSON interchange artefact.

## Deployment

Place this skill in your Claude Code skill directory (`~/.claude/skills/` or workspace-level). Claude will invoke it on user prompts mentioning Annex I / Annex III / Art. 6 classification, or whenever a broad risk-tier triage has already pointed to a likely high-risk branch that needs the depth assessment.

## Disclaimer

This skill is not legal advice. The Commission guidelines it draws on are draft and non-binding (only the CJEU can give authoritative interpretation). Use under qualified counsel.

## License

AGPL-3.0 (see repo-root LICENSE file).

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
