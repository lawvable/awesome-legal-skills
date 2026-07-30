# unfair-dismissal-screener

Screens a dismissal — proposed or already done — against the England & Wales unfair dismissal framework, and shows where it is exposed.

Most dismissals fail in the tribunal on process, not substance. This skill frames the qualifying-service question, checks the automatically-unfair categories that need no qualifying period, and structures the Burchell / Polkey / band-of-reasonable-responses analysis, then surfaces the specific procedural defects — as a draft for a solicitor to verify, not a determination of fairness. For employers deciding whether to proceed before a dismissal, and either side assessing the strength of a prospective claim after one.

## Install

```bash
git clone https://github.com/b1rdmania/unfair-dismissal-screener ~/.claude/skills/unfair-dismissal-screener
```

Or in a [Legalise](https://github.com/b1rdmania/legalise) workspace: add it from the skill library — review the manifest, grant capabilities, enable on a matter, run from chat. Every run leaves a signed, auditable record.

## Usage

```
/unfair-dismissal-screener
/unfair-dismissal-screener --mode=pre-dismissal
/unfair-dismissal-screener --mode=post-dismissal
```

Run it against a matter with the start date, effective date of termination, the reason the employer advances, and the procedure followed. It returns a structured screen: eligibility, reason, substantive and procedural fairness, an indicative risk score, and an illustrative compensation range.

## What it does

- Frames the qualifying-service gate (s.108 ERA) and checks for automatically-unfair heads with no qualifying period.
- Identifies the potentially fair reason advanced (s.98(2)) and whether it is genuine.
- Structures the Burchell analysis for conduct cases — genuine belief, reasonable grounds, reasonable investigation — against the band of reasonable responses.
- Structures the Polkey question and the ACAS Code uplift, and carries them through to an illustrative compensation range.
- Produces an indicative risk score with the reasoning visible, and marks every uncertain point inline — `[CITE NEEDED]`, `[SME VERIFY]` — so nothing reads as settled.

## What it doesn't do

- Determine fairness — that is the Tribunal's call on facts and witnesses the prompt never sees.
- Predict the outcome — the risk score is indicative, not a calibrated probability.
- Give legal advice — it is a draft screen for solicitor review, and a solicitor owns the conclusion.
- Quantify pension loss precisely, or cover redundancy selection-criteria challenges in detail.
- Cover Scotland or Northern Ireland.
- Verify statute or case law against a live source — check every citation and recompute every figure before relying on it.

## Requirements

- Claude Code or Claude Cowork. No MCP connectors required.
- A matter to run against (the dismissal facts, the reason advanced, the procedure followed).

## License

Apache-2.0.
