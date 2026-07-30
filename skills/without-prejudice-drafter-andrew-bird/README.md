# without-prejudice-drafter

Writes a settlement letter on the *right* footing — and warns you when marking it "without prejudice" won't actually keep it out of court.

A genuine settlement letter is normally protected, so the judge can't see it — but the label only works if the substance is a real attempt to settle, and even then there are exceptions. The skill picks the correct footing (without prejudice, without prejudice save as to costs / Calderbank, or open), drafts the finished letter, and surfaces the Unilever v Procter & Gamble exceptions that get WP material admitted despite the label — the traps a plain template won't warn you about. For juniors and in-house counsel who need the footing right the first time.

## Install

Part of the [claude-for-uk-legal](https://github.com/b1rdmania/claude-for-uk-legal) plugin suite:

```bash
/plugin marketplace add https://github.com/b1rdmania/claude-for-uk-legal
/plugin install uk-litigation-legal@claude-for-uk-legal
```

Or install the single skill directly:

```bash
cp -r without-prejudice-drafter ~/.claude/skills/without-prejudice-drafter
```

## Usage

```
/without-prejudice-drafter
/without-prejudice-drafter --type=wp
/without-prejudice-drafter --type=wpsatc
/without-prejudice-drafter --type=open
```

Run it against a matter with the dispute, the offer terms, and who is offering what. It returns the finished letter on the chosen footing.

```
/without-prejudice-drafter --type=wpsatc
Draft a Calderbank offer in the Khan unfair-dismissal claim: our client
will pay £18,000 inclusive, open for 21 days, ET so no Part 36.
```

The `--type` flag fixes the footing — `wp` for a plain settlement letter, `wpsatc` for a Calderbank / costs-protected offer, `open` for on-the-record correspondence. Omit it and the skill infers the footing from the request, asking only if it is ambiguous.

## What it does

- Identifies the correct footing — open, WP, or WPSATC — and proposes the right one for the situation.
- Applies the matching header convention and drafts the finished letter, not a template.
- Distinguishes the three footings on the point that matters: what is admissible at trial, and what is admissible only on costs.
- Surfaces the Unilever v Procter & Gamble exceptions, where WP material is admitted despite the label — concluded agreement, misrepresentation/fraud, estoppel, unambiguous impropriety, delay, costs, and tariff.
- Keeps open and WP content in separate documents and flags anything that risks an exception (admissions, threats, estoppel signals).

## What it doesn't do

- Settle the footing. It proposes a footing; it does not guarantee the footing holds. Mislabelling has real disclosure consequences either way.
- Give legal advice. The output is a draft for a solicitor, not advice the client can rely on. Counsel or the conducting solicitor must confirm the footing before the letter is sent.
- Make a labelled letter privileged when its substance is not a genuine settlement attempt. The label follows the substance.
- Provide Part 36 costs protection in the civil courts — draft a Part 36 offer separately for that.
- Cover Scottish tenders or Northern Ireland equivalents.

## Requirements

- Claude Code or Claude Cowork. No MCP connectors required.
- A matter to run against — the dispute, the offer terms, and the parties.

## License

Apache-2.0.
