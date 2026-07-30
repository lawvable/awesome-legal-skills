# cpr-letter-drafter

Writes the formal letter you send before suing someone in a civil case in England & Wales — the Letter Before Claim that starts the pre-action clock — under the *right* pre-action protocol for the claim.

Which protocol applies (debt, professional negligence, housing disrepair, personal injury, or the default Practice Direction on Pre-Action Conduct) changes the rules, and a generic letter misses them. For litigation juniors, in-house counsel, and small firms without a precedent bank to copy from: it catches what a general draft skips — the 30-day debt-claim response window, the professional-negligence preliminary-notice-then-letter-of-claim sequence — and flags the limitation date for a solicitor to confirm rather than stating it as fact.

## Install

Part of the [claude-for-uk-legal](https://github.com/b1rdmania/claude-for-uk-legal) plugin suite:

```bash
/plugin marketplace add https://github.com/b1rdmania/claude-for-uk-legal
/plugin install uk-litigation-legal@claude-for-uk-legal
```

Or install the single skill directly:

```bash
cp -r cpr-letter-drafter ~/.claude/skills/cpr-letter-drafter
```

## Usage

```
/cpr-letter-drafter
/cpr-letter-drafter --protocol=debt
/cpr-letter-drafter --protocol=prof-neg
```

Run it against a matter with the parties, cause of action, chronology, loss breakdown, and documents to disclose. It identifies the applicable protocol (or defaults to PACC), checks the limitation gate, and returns a drafted LBC structured the way that protocol expects.

Example:

```
/cpr-letter-drafter --protocol=debt

Claimant: Acme Supplies Ltd. Defendant: J. Khan (sole trader).
Unpaid invoices totalling £18,400 plus contractual interest.
Contract formed 12 Jan 2025; last payment received 3 Mar 2025.
```

It returns a Debt Claims Protocol letter with the 30-day response window, the required information sheet and reply form references, a statement of account, and a limitation marker for the solicitor to confirm.

## What it does

- Identifies whether a specific pre-action protocol applies or whether the default Practice Direction on Pre-Action Conduct and Protocols (PACC) governs.
- Applies that framework's timing, content, and disclosure requirements — for example the 30-day debt window, or the professional negligence preliminary-notice-then-letter-of-claim sequence.
- Drafts the letter with the parties, facts, claim heads applied to their elements, particularised loss with interest, documents, ADR signal, response requirements, and costs.
- Surfaces the apparent limitation date as a `[SOLICITOR: confirm limitation date]` marker, never as settled fact, and flags accrual assumptions and exceptions.
- Surfaces CPR Part 36 and Part 44 costs consequences if the matter proceeds.
- Marks uncertain points inline — `[SOLICITOR: confirm X]`, `[PROTOCOL]`, `[SME VERIFY]`, `[CITE NEEDED]` — so nothing reads as settled.

## What it doesn't do

- Issue the claim. The LBC is pre-action.
- Apply Scottish or Northern Irish procedure.
- Replace counsel's call on whether to issue protectively where limitation is tight.
- Guarantee or certify compliance. The output is styled to follow the relevant protocol; verify its current content, timing, and enclosure requirements before sending.
- Settle the limitation position. The periods it uses are general defaults; the accrual date and exceptions must be checked by a solicitor.

This is a draft for solicitor review, not legal advice. A solicitor with conduct of the matter is responsible for compliance and for what goes out under the firm's name.

## Requirements

- Claude Code or Claude Cowork. No MCP connectors required.
- A matter to run against — parties, cause of action, chronology, loss breakdown, and the documents to disclose.

## License

Apache-2.0.
