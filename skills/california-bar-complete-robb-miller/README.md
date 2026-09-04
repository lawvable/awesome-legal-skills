# California Bar Complete

**A Claude skill for end-to-end California Bar Exam prep** — the five essays (13 subjects), the 90-minute Performance Test, and the 200-question MBE (7 subjects).

Built by a practicing attorney who used it to compress four months of prep into a week and a half. The story: *[Hacking the CalBar with AI](BLOG-POST-URL)*.

## Philosophy

You don't learn to write bar essays under time pressure — you **memorize a bank of issue paragraphs in advance**, then on exam day you spot the issue and transcribe the paragraph, dropping the facts in front of you into the application sentence. For the MBE, you drill original NCBE-style questions until the rules and their traps are automatic.

The highest-yield layer throughout: **California divergences**. 🔴 flags mark everywhere California departs from the majority/MBE rule (CEC vs FRE, community property, CA RPC, pure comparative negligence, and more). On the essays the CA rule usually controls; on the MBE the majority/federal rule controls — the skill keeps the two answers separate so you don't cross them up.

## What's inside

```
SKILL.md                        — the skill's instructions and modes
references/
  essays/                       — 13 subjects: attack outlines + full IRAC rule blocks
  standard-paragraphs/          — 13 subjects: memorize-and-transcribe paragraphs
  mbe/                          — MBE method + 7 subject files (rules, traps, CA splits)
  pt/performance-test.md        — Performance Test approach
  exam/exam-day.md              — timing, IRAC discipline, issue-spotting, triage
```

## Five modes

1. **Retrieve** — "Give me the rule for the parol evidence rule."
2. **Drill / Teach** — "Drill me on Community Property." Active recall: it prompts, you recite, it diffs your rule against the bank and re-tests your misses.
3. **MBE Quiz / Timed Drill** — "Give me a timed set of 10 Evidence questions." Original questions, full explanations, every distractor accounted for.
4. **Grade** — "Grade my essay" / "mark my outline." Issue map, IRAC integrity, missed CA divergences, an estimated 40–100 band, and the 2–3 highest-leverage fixes. Works on outlines when you don't have an hour to write.
5. **Generate / Plan** — "Write me a practice essay question" / "build me a 10-day study plan."

And the underrated sixth use: **argue with it**. Push back on a grade, defend your version of a rule, and find out why your argument fails — including in voice mode, hands-free.

## Install

**Claude Code / Claude Agent SDK:**

```bash
git clone GITHUB-REPO-URL
cp -r california-bar-complete ~/.claude/skills/
```

**Claude.ai / Claude desktop (Cowork):** upload `california-bar-complete.skill` (or this folder zipped) where your plan accepts skills, or grab the ready-to-run version on [Lawve](LAWVE-URL).

Then just start studying: *"quiz me on hearsay"*, *"grade this essay"*, *"drill me on wills in the car"*.

## Practice against real released questions

This repo contains **only original material**. The State Bar of California publicly releases past essay questions, Performance Tests, and selected answers — download them free at [calbar.ca.gov](https://www.calbar.ca.gov/Admissions/Examinations/California-Bar-Examination/Past-Exams) and bring them into a session; the skill will build issue maps and grade you against them on the fly.

## Heads up: the exam is changing

Beginning with the **July 2028** administration, California moves to the **NextGen Uniform Bar Exam** (with a California component expected to follow). This skill targets the current California Bar Exam format — good through the February 2028 administration. Verify the current exam scope at [calbar.ca.gov](https://www.calbar.ca.gov) before relying on it.

## Disclaimers

- **Study aid only. Not legal advice.** Verify every rule against current California authority — items flagged `⚠️ VERIFY` involve recently amended or unsettled law.
- All rules and practice questions are stated in original wording. No CalBar, NCBE, or commercial-vendor text is reproduced. No affiliation with the State Bar of California or the NCBE.
- No guarantee of any exam outcome. The bar is, famously, not a fair fight — prepare accordingly.

## Author

Built by **Robb** — Canadian lawyer since 1996, New York attorney since 2017, California bar taker (July 2026). Find me on X at [@LegalHacks](https://x.com/LegalHacks).

## License

[MIT](LICENSE) — free for bar takers, tutors, and builders. If it helps you pass, tell someone.
