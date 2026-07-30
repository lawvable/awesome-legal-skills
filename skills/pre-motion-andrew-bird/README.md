# pre-motion

Adversarial premortem for England & Wales civil litigation. Builds the strongest version of a case, then attacks it from four angles — procedural, substantive, evidentiary, strategic — to find where it loses before opposing counsel does.

For solicitors stress-testing before issue, in-house counsel before sign-off, mediators valuing settlement, and litigation funders pricing a matter.

## Install

Part of the [claude-for-uk-legal](https://github.com/b1rdmania/claude-for-uk-legal) plugin suite:

```bash
/plugin marketplace add https://github.com/b1rdmania/claude-for-uk-legal
/plugin install uk-litigation-legal@claude-for-uk-legal
```

Or install the single skill directly:

```bash
cp -r pre-motion ~/.claude/skills/pre-motion
```

## Usage

```
/pre-motion
/pre-motion --depth=fast
/pre-motion --depth=thorough
```

Run it against a matter with the facts, evidence references, claim heads, and the strongest version of the case as you see it. It returns a ranked stress-test brief.

## What it does

- Builds the optimistic baseline — the strongest version the evidence supports.
- Inspects the evidence: document gaps, cross-document contradictions, timeline holes, each flagged with a severity.
- Runs four adversarial passes (parallel sub-agents where supported, otherwise sequential), each told the case has been lost and asked to walk back why — one per failure category.
- Synthesises a brief: ranked failure scenarios with severity, likelihood and mitigation; evidence inconsistencies; blind spots; settlement-posture implications; and one one-sentence verdict.
- Marks every uncertain point inline — `[CITE NEEDED]`, `[SME VERIFY]`, `[EVIDENCE FLAG]` — so nothing reads as settled.

## What it doesn't do

- Predict the outcome — it surfaces failure modes, not results.
- Decide whether to take, settle, or withdraw — those are counsel's calls.
- Replace a formal counsel opinion. It is a structured prompt for that conversation, not a substitute.
- Cover non-UK procedure (US federal, Scotland, Northern Ireland).
- Verify case law against a live source — check any authority it cites before relying on it.

## Requirements

- Claude Code or Claude Cowork. No MCP connectors required.
- A matter to run against (facts and evidence references). In a host workspace, the CPR 31.22 / privilege gate is enforced upstream; run standalone only on material you are permitted to use.

## License

Apache-2.0.
