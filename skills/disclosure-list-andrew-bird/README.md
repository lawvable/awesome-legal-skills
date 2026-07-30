# disclosure-list

Works out which documents you have to hand over to the other side in a civil case in England & Wales, and builds the formal list — getting right the bit that trips people up: which disclosure regime applies.

In the Business and Property Courts that's the Disclosure Pilot under Practice Direction 57AD (now permanent, with its Models A–E); everywhere else it's standard disclosure under CPR Part 31. Ask a general tool for "a disclosure list" and it'll usually default to old CPR 31 and miss PD 57AD entirely. For litigation juniors, in-house counsel, and small teams without a precedent bank: this picks the regime, selects a Model per issue, structures the Disclosure Review Document, and drafts the certificate as scaffolding for the party to sign personally.

## Install

Part of the [claude-for-uk-legal](https://github.com/b1rdmania/claude-for-uk-legal) plugin suite:

```bash
/plugin marketplace add https://github.com/b1rdmania/claude-for-uk-legal
/plugin install uk-litigation-legal@claude-for-uk-legal
```

Or install the single skill directly:

```bash
cp -r disclosure-list ~/.claude/skills/disclosure-list
```

## Usage

```
/disclosure-list
/disclosure-list --regime=pd57ad --model=C
/disclosure-list --regime=cpr31
```

Run it against a matter with the court/division, the issues for disclosure, custodians, data sources, date range, and privilege scope. It identifies the regime, selects the Extended Disclosure Model(s) per issue, and returns the drafted list.

Example: a Commercial Court claim where you give the issues for disclosure, the four custodians, the data sources (Outlook, Teams, a shared drive, WhatsApp), and the date range. It returns a Disclosure Review Document with a model per issue, a custodian/source/keyword table, and a draft Disclosure Certificate marked as scaffolding.

## What it does

- Identifies the regime — PD 57AD for the Business and Property Courts (Commercial, Chancery, TCC, Circuit Commercial, IP, Financial List), CPR Part 31 everywhere else.
- Selects PD 57AD Extended Disclosure Models A–E per issue, with Model C as the default and Model E reserved for exceptional cases.
- Maps custodians, data sources, date ranges, and keywords into a search methodology, including TAR/predictive-coding disclosure.
- Flags privilege candidates by category — legal advice, litigation, without prejudice, common interest.
- Builds the output: an N265-structured List of Documents (three parts) under CPR 31, or a simplified Disclosure Review Document under PD 57AD.
- Marks every uncertain point inline — `[REGIME]`, `[PRIVILEGE]`, `[GDPR]`, `[SME VERIFY]` — so nothing reads as settled.

## What it doesn't do

- Run the search. It scopes and lists; the search happens outside the model and must actually be performed before any list or statement is certified.
- Decide privilege. It flags candidates by description; counsel reviews every flagged document and makes the call.
- Produce an executed certificate. The Disclosure Statement (CPR 31.10) and the PD 57AD Disclosure Certificate are signed personally by the party — the model drafts scaffolding behind a DRAFT banner, it does not make the certification.
- Invent documents. Every entry traces to a real input you supplied.
- Cover Scottish or Northern Irish procedure (Commission and Diligence; Schedule 1 RCS), or family proceedings.
- Give legal advice. It is a drafting aid; verify the scope, the search, and the privilege calls with counsel before serving any output.

## Requirements

- Claude Code or Claude Cowork. No MCP connectors required.
- A matter to run against — court/division, issues, custodians, sources, date range, and privilege scope.

## License

Apache-2.0.
