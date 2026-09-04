---
name: california-bar-complete
license: MIT. Study aid only — not legal advice.
metadata:
  version: 1.3.0
  author: Robb (@LegalHacks)
description: >-
  Complete prep for all three scored components of the California Bar Exam: the
  five written ESSAYS (13 subjects — Business Associations, Civil Procedure,
  Community Property, Constitutional Law, Contracts, Criminal Law & Procedure,
  Evidence, Professional Responsibility, Real Property, Remedies, Torts, Trusts,
  Wills & Succession), the PERFORMANCE TEST, and the multiple-choice MBE (7
  subjects). Trigger whenever someone is studying for the California bar (or the
  MBE) and says things like: "give me the rule for [issue]", "big issues in
  [subject]", "drill/quiz me on [topic]", "MBE questions on [subject]", "teach me
  [doctrine]", "build an attack outline", "grade my essay", "memorizable
  paragraph for [issue]", "performance test approach", or "make a study plan" —
  or names any tested essay/MBE subject in a study, memorization, drilling, or
  practice-question context. Also trigger when a student uploads a practice
  essay, PT, or question set to be graded or turned into rule blocks. When in
  doubt during bar prep, trigger.
---

# California Bar Complete

End-to-end prep for the **written and multiple-choice** halves of the California
Bar Exam, weighted roughly 50/50: **five one-hour essays** (any of 13 subjects),
**one 90-minute Performance Test**, and the **200-question MBE** (7 subjects).
This skill centralizes the black-letter **rules**, **pre-written memorizable IRAC
paragraphs**, **MBE practice**, and **exam-day strategy** a student needs.

Core philosophy: **memorize a bank of issue paragraphs in advance**, then on exam
day **spot the issue and transcribe the paragraph**, filling the application
sentence with the facts in front of you; for the MBE, **drill original questions**
until the rules and their traps are automatic. The banks make both fast.

## Three components

| Component | What it is | Where the material lives |
|-----------|-----------|--------------------------|
| **Essays** | 5 essays drawn from 13 subjects | `references/essays/` (attack outlines + IRAC rule blocks) + `references/standard-paragraphs/` (memorizable paragraphs) |
| **Performance Test** | 1 closed-universe lawyering task (90 min) | `references/pt/performance-test.md` |
| **MBE** | 200 MCQs across 7 subjects | `references/mbe/` (method + 7 subject files) |

Exam strategy for all components: `references/exam/exam-day.md` (timing, IRAC
discipline, issue-spotting, triage).

### The 13 essay subjects
Business Associations · Civil Procedure · Community Property · Constitutional Law
· Contracts · Criminal Law & Procedure · Evidence · Professional Responsibility ·
Real Property · Remedies · Torts · Trusts · Wills & Succession.

Each subject has two files: `references/essays/<subject>.md` (a condensed **attack
outline** plus full **IRAC rule blocks**) and
`references/standard-paragraphs/<subject>.md` (flowing **memorize-and-transcribe
paragraphs** with an *Apply:* frame for each issue). The standard-paragraphs file is
the **most complete memorization set** for a subject — it may include a few issues
not broken out in the attack-outline file — so prefer it when a student is memorizing,
and use the attack outline for issue-spotting structure.

For deeper calibration, the State Bar of California **publicly releases** past essay
questions, Performance Tests, and selected answers on calbar.ca.gov — point students
there for authentic practice material, and build issue maps from those released
questions on the fly when grading or generating practice.

### The 7 MBE subjects
Civil Procedure · Constitutional Law · Contracts · Criminal Law & Procedure ·
Evidence · Real Property · Torts. See `references/mbe/mbe-method.md` first, then
the per-subject files for high-yield rules, distractor traps, and the all-important
**MBE-vs-California** splits.

## How to use it — pick the component, then the mode

Figure out which **component** (essay, PT, or MBE) and which **mode** the student
wants from how they ask, then act. Students chain these constantly.

### Mode 1 — Retrieve (default)
"Give me the rule for [X]" / "what are the big issues in [subject]." Open the
relevant essay or MBE file and surface the matching attack-outline slice and IRAC
rule block(s) or paragraph(s). If only a subject is named, lead with the **major
issues** that anchor most questions, then offer the minor ones.

### Mode 2 — Drill / Teach
"Drill me", "quiz me on the rules", "teach me [doctrine]." Run active recall: prompt
with an issue label → student states the rule → reveal the stored rule and diff what
was missed. Track misses and re-test those first. One issue at a time; keep it brisk.

### Mode 3 — MBE Quiz / Timed Drill
"Quiz me with MBE questions", "give me a timed set." Follow `references/mbe/mbe-method.md`:
generate **original** NCBE-style questions (never reproduce real exam questions),
reveal the best answer with a full explanation of why it's right and why each
distractor is wrong, and flag any MBE-vs-California divergence.

### Mode 4 — Grade (full answers and outlines)
"Grade my essay/PT answer" or "mark my outline." For **full answers**: build the
question's **issue map** (every issue a strong answer must raise, majors first) from the
fact pattern and the subject's attack outline, then mark against it — issue spotting,
IRAC integrity, rule accuracy, whether the answer got the **hard structural move** the
question turns on, and missed CA divergences. Give an estimated **40–100 band** (CalBar's
essay scale) with the 2–3 highest-leverage fixes. For **outlines** (no time to write it
out), mark spotting + sequencing + rule-cue accuracy only. Missed majors = the biggest
leak (flag 🔴). Always state this is self-study calibration, not an official score.

### Mode 5 — Generate / Plan (incl. essay & outline creation)
"Build an attack outline / memorizable paragraphs for [topic]", **"write me a practice
essay question"**, or a student uploads their own outline or question set. To **author new
essay questions or model outlines**: pick 4–7 issues from the subject's attack outline
(majors anchoring, one crossover), weave a fact pattern that raises each one, plant
ambiguities that cut both ways and at least one CA-divergence trigger, and label output
*original practice question in CalBar style*. For rule content,
produce new material in the existing file format (major issue first, then minor), in
**original** wording. Also handles study-plan requests — build a week-by-week plan across
the three components using `references/exam/exam-day.md`.

### Working from released CalBar material
When the user brings released CalBar questions, selected answers, or their own scored
essays into a session, use them freely **within the session** — build issue maps, anchor
grading, diff the student's answer against what scored well. Do not reproduce vendor
prose or graded student essays in outputs; distill them into original issue maps and
analysis instead.

## California divergences are the highest-yield points

Throughout, 🔴 flags mark where California law departs from the majority/MBE rule —
CEC vs FRE, CA community property, the CA Rules of Professional Conduct, pure
comparative negligence, CA civil procedure, CA criminal statutes. On the **essays**
the CA rule usually controls; on the **MBE** the majority/federal rule controls. The
MBE subject files keep these two answers explicitly separate so students don't cross
them up.

## Sourcing, accuracy, and disclaimer

- All rules and all practice questions are stated in **original wording**. Black-letter
  law is not copyrightable, but specific vendor prose and real NCBE questions are —
  never reproduce them.
- Items marked `> ⚠️ VERIFY` involve recently amended or unsettled law (e.g., CA
  Rules of Professional Conduct, Evidence/Probate Code section numbers, felony-murder
  reform, recent Supreme Court decisions). Confirm against current authority before
  relying on them.
- Exam scope can change. Confirm the tested subjects against the State Bar of
  California's current scope outline near the exam date.
- **This skill is a study aid, not legal advice.** End substantive outputs with:
  *"Study aid only — verify against current California authority. Not legal advice."*

## Conventions
- Confidence flags: 🟢 settled · 🟡 verify nuance · 🔴 high-divergence-from-MBE or
  recently changed.
- Keep retrieval tight — show the block(s) asked for, not a whole file.
- Cross-reference overlapping subjects (Contracts↔Remedies, Crim Law↔Crim Pro,
  Wills↔Trusts↔Community Property, and every MBE subject ↔ its essay-subject files).
