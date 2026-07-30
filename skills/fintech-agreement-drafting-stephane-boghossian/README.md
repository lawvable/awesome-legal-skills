# fintech-agreement-drafting

A [Claude](https://claude.com/claude-code) **skill** that turns a senior
fintech lawyer's drafting method into a repeatable, end-to-end workflow for
**drafting and finalising a complex, multi-pillar regulated payments
agreement** — from intake to signature.

The running example is a payments framework bundling **agent cash-in/cash-out,
QR payments, wallet e-payments, and a marketplace integration**, where a
licensed payment-services provider (PSP) engages a counterparty across service
lines that each carry their own regulatory profile. The method generalises to
any regulated, multi-service fintech contract.

## What it does

Runs the matter across **five phases and fourteen steps**:

| Phase | What you produce |
| --- | --- |
| **1 — Intake & regulatory mapping** | Activity-to-licence matrix, resolved grey-zone classifications, true party-role map |
| **2 — Architecture** | Framework-plus-sub-agreement structure; ring-fenced marketplace |
| **Cross-cutting — regulatory/commercial balance** | The negotiable vs non-negotiable line; proportionate, sequenced controls |
| **3 — Core clause drafting** | Authority, float mechanics, hard-coded regulator caps, compliance/data/audit, liability — all tracking *control* |
| **4 — Execution-blocker triage** | Decision packages (obstacle → path → fallback → consequence) |
| **5 — Iteration & finalisation** | Versioned tracked-changes rounds, a pre-signature compliance/consistency check, and closing open blockers as conditions precedent |

The spine running through every step: **map the regulatory perimeter before
you draft a word; authority, money, and liability each track control; structure
for pillar independence; find the lowest-friction structure the regulator
accepts; and sequence honestly with conditions precedent.**

## Install

Drop the folder into your Claude skills directory:

```bash
git clone https://github.com/sboghossian/fintech-agreement-drafting.git \
  ~/.claude/skills/fintech-agreement-drafting
```

Then invoke it in Claude Code with `/fintech-agreement-drafting`, or just
describe a regulated payments deal and it triggers on phrases like *"draft a
PSP/agent agreement", "structure this multi-pillar deal", "is this QR flow P2P
or acquiring?", "review this fintech contract for compliance."*

## Files

- **`SKILL.md`** — the executable workflow (the skill itself).
- **`REFERENCE.md`** — the verbatim source manual the skill operationalises.

## Scope

This is a **drafting method, not legal or regulatory advice.** It tells you
*where* the licence-specific terms (commission caps, agent caps, KYC
allocation, permitted activities, notification duties) must live in the
contract and *how they must behave* — it does **not** supply their values. Every
one must be tied to the actual article or decision of the governing licensing
instrument, and the output requires qualified legal and local regulatory
review. Prompts to a public AI tool are not privileged; work with abstracted
placeholders.

## Credit

Methodology authored by **Abbas, Chief Legal Officer, [HAQQ Legal AI](https://haqq.ai)**,
from the manual *"Drafting & Finalising a Complex Multi-Pillar Fintech
Agreement."* Packaged as a Claude skill by **Stephane Boghossian** (Head of
Growth, HAQQ Legal AI).

## License

[AGPL-3.0](./LICENSE). Anyone who builds this method into a hosted or
distributed product must open-source the derivative.
