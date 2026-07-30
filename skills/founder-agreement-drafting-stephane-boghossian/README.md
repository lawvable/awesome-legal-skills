# founder-agreement-drafting

A [Claude](https://claude.com/claude-code) **skill** that turns the drafting and
review of a **founders' / co-founders' agreement** into a repeatable method —
the document (or set of terms) that fixes **equity, vesting, IP ownership, roles,
decision-making, deadlock, and departure** between the people starting a company.

Jurisdiction-agnostic, anchored on the **Delaware C-corp** default, with the
highest-dispute terms handled first-class — the equity split, reverse vesting and
the 83(b) clock, present-tense IP assignment, leaver mechanics, and the deadlock
clause most tools skip.

## What it does

Runs in **two modes**.

**DRAFT** — five phases, fourteen steps, from intake to signature:

| Phase | What you produce |
| --- | --- |
| **1 — Intake & founder mapping** | Founder-and-role map, entity/jurisdiction determination, contribution inventory |
| **2 — Equity & vesting architecture** | The split *with a written rationale* (not a fake calculator), the vesting schedule, the 83(b) flag, acceleration |
| **3 — Core clause drafting** | IP assignment, roles & deadlock, leaver & buyback, transfer/ROFR, and the supporting terms — into the right instrument |
| **4 — Conflict & blocker triage** | Desirable-vs-blocking, plus divergent-interest points routed to independent counsel |
| **5 — Pre-signature finalisation** | The "clean, investable cap table" diligence dry-run; open blockers closed as conditions |

**REVIEW** — audit an existing agreement against an 18-clause checklist and a
red-flag scan, and output a triaged gap report (Critical / Important / Optional).

The spine running through every step: **vesting is the mechanism, not the split;
document the rationale, not just the number; present-tense IP assignment or
nothing; every share must have a home on departure; design the deadlock before it
happens; draft the terms into the right instrument and make them expire cleanly.**

## Install

Drop the folder into your Claude skills directory:

```bash
git clone https://github.com/sboghossian/founder-agreement-drafting.git \
  ~/.claude/skills/founder-agreement-drafting
```

Then invoke it in Claude Code with `/founder-agreement-drafting`, or just
describe a founder deal and it triggers on phrases like *"draft a founders'
agreement", "split equity between founders", "set up founder vesting", "founder
IP assignment", "founder deadlock clause", "review this founders' agreement."*

## Files

- **`SKILL.md`** — the executable workflow (the skill itself).
- **`REFERENCE.md`** — the research backbone, with every clause, the case law
  (*Stanford v. Roche*), the equity-split data (Wasserman / NBER), the
  jurisdiction table (Delaware / LLC / UK / MENA), and primary-source citations.

## Scope

This is a **drafting method, not legal, tax, or financial advice.** It tells you
*where* each founder term must live and *how it must behave* — it does **not**
certify that a term is enforceable in your jurisdiction, decide who "deserves"
more equity, or recommend a tax election. It drafts for the **venture as a
whole**, the way company counsel does: **each founder should have independent
counsel before signing.** Jurisdiction-specific terms (non-compete enforceability,
MENA onshore forfeiture, LLC profits-interest tax, the 83(b) decision) are flagged
for local / tax counsel, not supplied. Prompts to a public AI tool are not
privileged; work with abstracted placeholders.

## Credit

Part of a series of open legal skills from **[HAQQ Legal AI](https://haqq.ai)**,
initiated with **Abbas** (Chief Legal Officer). The method here is synthesised
from public best-practice sources — Y Combinator, Cooley GO, Clerky, Carta,
Orrick, Wilson Sonsini, SeedLegals, Noam Wasserman / HBS, and named case law
(all cited in `REFERENCE.md`). Packaged as a Claude skill by **Stephane
Boghossian** (Head of Growth, HAQQ Legal AI).

## License

[AGPL-3.0](./LICENSE). Anyone who builds this method into a hosted or distributed
product must open-source the derivative.
