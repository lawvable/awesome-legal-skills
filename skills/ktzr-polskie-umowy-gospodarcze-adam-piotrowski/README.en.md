[🇵🇱 PL ←](./README.md) | 🇬🇧 EN

# Polish Commercial Legal

**An example of how Claude can work with Polish contracts.**
It can serve as a starting point for what practical AI tools for lawyers should look like.

Built on the practice of our law firm (**Kancelaria Radcow Prawnych Zurawska Piotrowski i Wspolnicy**, Zurawska Piotrowski Law Firm, [ktzr.pl](https://ktzr.pl)), primarily on B2B, IP and IT contracts.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Jurisdiction](https://img.shields.io/badge/Law-Poland-red)](https://github.com/apiotrowski-afk/commercial-legal-pl)
[![Status](https://img.shields.io/badge/Status-v0.x_(early)-yellow)](https://github.com/apiotrowski-afk/commercial-legal-pl)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-orange)](https://claude.ai)

> ⚠️ **Disclaimer:** This skill does not replace legal advice; it is an operational tool for a lawyer's work, and every specific matter requires individual review by a qualified person.

## What this is

A Claude skill for **drafting and reviewing contracts under Polish civil law**, focused on B2B contracts, IP and IT. The skill loads on demand; Claude reaches for it when the conversation involves Polish contracts, drafting clauses, or reviewing a contract a client has just signed (or is about to).

It is written in Polish, because Polish contracts are written in Polish, and the doctrine is in Polish, and the case law is in Polish. The skill works in Polish; this README in English exists so you can decide if it's worth a closer look.

## Why we are publishing this

There is plenty of talk about AI in Polish Legaltech, especially at conferences and in social media posts. There are far fewer working implementations that actually help in the daily practice of a law firm.

We believe the best tools come not from conference presentations or consulting PoCs, but from daily use. We build something for ourselves, use it, refine it as we go, and then share it with others.

So we decided to start with something concrete: drafting B2B, IP and IT contracts, which we wrapped in a Claude skill and put out in the open — not as a *"production tool of our firm"*, but as an example of one possible approach, open to criticism, fork, and discussion.

It may give someone:
- an idea on how to build a skill of their own for another area of law or another firm
- a starting point for the conversation *"what should claude-for-legal look like in Polish"*, because for now the Anthropic ecosystem is mostly US/UK common law

If you want to engage (issues, PRs, comments, fork, your own version for another field), all welcome.

## What to know before you start

A few honest caveats to avoid disappointment:

- **This is a slimmed-down slice, not the full toolkit of the firm.** What you see here is a deliberate cut, synthesized and paraphrased so that it is useful but does not breach professional confidentiality of a Polish radca prawny (art. 3 of the Act on Legal Counsels). The full internal base is bigger, containing clauses tied to specific cases, client profiles, case studies, technical supplements; all kept in a local, private copy. **What you see here are examples, not "the one right way."**

- **The skill is only as good as your own work with it.** *Garbage in, garbage out* applies here especially. The best results come from iterating against your own practice: you add your own clauses to `references/baza-klauzul/`, your own rules to `references/zlote-reguly.md`, your own workflows. Our set is a starting point.

- **This is not a universal template.** One firm, one set of design choices. If your practice is different, fork it and adapt.

- **The scope is limited** to B2B, IP and IT contracts. No criminal law, no administrative law, no tax, no family, no court procedure.

- **The skill is not yet in `claude-plugins-community`.** For now you install straight from our repo.

## What is inside

The skill has five main layers:

| Layer | What's in it | File |
|---|---|---|
| **Golden Rules** | 12 rules for drafting Polish contracts: control of definitions, structure, language | `references/zlote-reguly.md` |
| **Editorial style** | Concrete style patterns from practice (when to use *"W przypadku"* instead of *"Jeżeli"*, party pairs for each type of relationship, typography) | `references/style-redakcyjny.md` |
| **Clause taxonomy** | 7 categories of contract language — Polish adaptation of Adams' MSCD framework | `references/kategorie-klauzul.md` |
| **Clause base** | Sample clauses by category (parties, subject matter, IP, liability, termination, GDPR, settlement, etc.); generic IT patterns + our reference clauses | `references/baza-klauzul/` |
| **Knowledge base** | Doctrinal analyses with case law (Supreme Court, Supreme Administrative Court): maintenance, copyright, GDPR, liability cap, image rights | `references/baza-wiedzy/` |

Add to this `references/essentialia-mapowanie.md` (essentialia negotii for each contract type), `references/checklist-15.md` (a 15-point completeness check) and `references/legal-design.md` (visual layer for outgoing documents).

The skill ships with **8 operational workflows** in `workflows/`: quick triage (GREEN/YELLOW/RED), full contract analysis, risk audit, contract generation, clause editing, consistency check, devil's advocate review, and client onboarding. Each workflow specifies exactly which reference files to load and when.

## How to use this

```bash
# Fastest — works with Claude Code, Cursor, Codex and 40+ agents:
npx skills add apiotrowski-afk/commercial-legal-pl

# Or clone manually into your skills directory:
cd ~/.claude/skills
git clone https://github.com/apiotrowski-afk/commercial-legal-pl.git
```

In any Claude conversation the skill loads automatically when the topic touches Polish contracts.

Detailed installation instructions in the [Polish README](./README.md).

## License

Apache 2.0. Use it, fork it, adapt it. We only ask that you preserve the attribution to KTZR Law Firm in the NOTICE file, for those who care about provenance and want to know where the patterns came from.

## Contact

- Website: [ktzr.pl](https://ktzr.pl)
- Email: a.piotrowski@ktzr.pl
- GitHub: [@apiotrowski-afk](https://github.com/apiotrowski-afk)

---

*The skill is in active development. Things will change. Issues and PRs welcome.*
