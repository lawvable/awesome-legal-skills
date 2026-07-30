---
name: legal-test-builder-patrick-munro
description: >
  Builds a high-fidelity interactive legal assessment as a single self-contained HTML artifact. Output includes a live countdown timer, contract review tasks with hover-annotated problem clauses, candidate answer textareas, model answers hidden behind reveal blocks, scenario-based legal memo tasks, strategy and function-building questions, and a pre-submission checklist that encodes the marking criteria. Use when the user needs to (1) assess a legal candidate with a realistic timed exercise, (2) train or onboard junior lawyers using problem sets rather than doctrine, (3) help a candidate prepare for a real take-home assessment they are facing, (4) build educational materials for law students, in-house teams, or compliance training, or (5) produce scenario-based training modules on specific legal topics. Triggers on "legal test", "take-home", "mock exam", "contract redline exercise", "candidate assessment", "legal training exercise", "practice test", or similar phrasing even when informal.
metadata:
  author: "Patrick Munro"
  license: "agpl-3.0"
  version: "2026-04-25"
---

# Legal Test Builder

Produces a production-grade interactive HTML legal assessment as a single self-contained file that works offline and renders cleanly in any modern browser.

## When to use

- Preparing a candidate for a real take-home assessment
- Assessing legal candidates with a realistic, timed exercise that tests judgment rather than doctrine recall
- Onboarding junior lawyers through scenario-based learning
- Building legal training modules for in-house teams or client education
- Law student moot and drafting exercises
- Compliance or regulatory training where scenario application is the point

## Step 1: Gather inputs

Before building, confirm or infer the following. If not specified, make sensible defaults and flag assumptions visibly in the output so the user can correct them.

| Input | Key questions | Default if unspecified |
|---|---|---|
| **Role** | What position is being tested or trained for? | "Legal Counsel" |
| **Organisation** | Context for the scenario | Fictional company from the library below |
| **Legal domain(s)** | Contract law, IP, employment, regulatory, M&A, compliance, privacy, etc. | Commercial contracts |
| **Governing law** | English law, German law, French law, New York law, etc. | English law |
| **Test duration** | Total time for the assessment | 3 hours |
| **Difficulty** | Junior / Mid / Senior / Partner-equivalent | Mid-level |
| **Purpose** | Candidate assessment vs. training vs. exam prep | Candidate assessment |
| **Number of tasks** | How many distinct exercises | 3-4 tasks |
| **Model answers** | Included (training / prep) or excluded (live exam) | Included as reveals |

For candidate prep and training: always include model answers as hidden reveals.
For live candidate assessment: generate a second "examiner version" that strips the reveals.

## Step 2: Design the task stack

A strong 3-hour test uses this structure. Scale task count and timing to the duration.

### Task 01: Contract Review and Redline (50-70 min)

The anchor task. Most revealing of practical legal judgment.

- Draft a realistic 6-10 clause agreement with **5-8 embedded problems**
- Problems should span critical, high, and medium severity
- Always include at least one **missing clause** (something not in the contract at all)
- Include at least one **trap clause** that looks standard but is not (e.g., a licence-back that launders an overbroad IP assignment)
- See `references/contract-design.md` for problem-embedding patterns

### Task 02: Legal Memo / Written Analysis (35-50 min)

Tests reasoning under novelty. Best structured as a scenario with no clean answer.

- Give a factual scenario with a genuine legal tension
- Specify the governing law and any constraints
- The scenario should be novel enough that the candidate cannot recite a textbook answer
- See `references/scenario-design.md` for scenario construction patterns

### Task 03: Short Analysis (20-35 min)

A focused issue with one problem and one answer. Good for: conflict of interest, regulatory compliance, specific employment or GDPR question, contractual interpretation.

### Task 04: Strategy / Function-Building (30-45 min)

Tests seniority and commercial judgment rather than legal knowledge.

- Classic framing: "You are the first legal hire. It is Day 90. What have you built, what have you deliberately not built, and what keeps you up at night?"
- Alternative: "Identify the three highest-priority legal risks and how you would address each."
- See `references/strategy-questions.md` for templates by role type

## Step 3: Build the HTML

Read `references/html-framework.md` before writing code. It contains:

- The full CSS design system (tokens, typography, components)
- The contract annotation pattern with hover tooltips on problem clauses
- The reveal block component
- The timer implementation
- The checklist component
- Colour and severity conventions

### Core architectural rules

1. **Single file**: everything inline. No external dependencies except Google Fonts.
2. **Offline-capable**: the test must work without internet access once fonts are cached.
3. **Timer**: sticky header, shows hours:minutes:seconds. Colour shifts: normal → amber (under 30 min) → red and pulsing (under 10 min).
4. **Contract problems**: annotated with `data-title` and `data-body` attributes on `<span class="problem">` elements. A JS tooltip renders on hover. The annotation is invisible until hovered.
5. **Reveal blocks**: model answers hidden by default. Click to reveal. Never auto-open.
6. **Write areas**: `<textarea class="write-area">` beneath every question. Candidate writes before revealing.
7. **Checklist**: final section with clickable items. Use it to encode the marking criteria.

### Content quality rules

- **Contract text must be realistic.** Not obviously fake. Use proper defined terms, clause numbering, and recitals where appropriate.
- **Problems must be embedded naturally.** The bad clause should read plausibly. A poorly-drafted clause spotted only because it is obviously wrong is a bad test.
- **Model answers must be opinionated.** Not "it depends." State a conclusion, justify it, then acknowledge genuine uncertainty where it exists.
- **Traps must be explicitly called out** in a clearly styled trap box. Candidates need to understand not just what the problem is but why the instinctive response is wrong.
- **Hook quotes**: include one memorable framing sentence per major section. One line that captures the strategic point, styled in a hook box.
- **Gaps must be flagged honestly.** If a model answer involves a developing area of law, say so. A gap box signals "this is uncertain; here is how to handle it."

## Step 4: Severity and priority framework

Use this consistently across all problem rows and scenario analyses:

| Severity | Colour | Definition |
|---|---|---|
| **CRITICAL** | Red | Existential to the organisation's mission, business model, or legal position. A lawyer who misses this fails the test. |
| **HIGH** | Amber | Significant commercial or legal exposure. Should be caught and negotiated. |
| **MEDIUM** | Blue | Suboptimal but not immediately dangerous. Bonus credit for catching it. |

In contract tasks, always include at least 2 CRITICAL problems. The candidates who catch both and articulate why they are existential are the ones worth hiring.

## Step 5: Checklist design

The pre-submission checklist is the invisible marking rubric. Design it to:

- Encode what separates a good answer from an excellent one
- Include at least 2 items about *how* the candidate engaged (honest about uncertainty, conclusions first, no padding) rather than only *what* they wrote
- End with one sentence capturing the philosophy of the role being tested

## Step 6: Two-version output

- For candidate prep or training: build with model answers (reveals included)
- For live assessment: strip reveals and model answer content, leaving task instructions, contract text, and write areas. Present as a clean "examiner version."

To generate the clean version, remove all `.reveal-block` divs and `.reveal-body` content. The `.reveal-header` can be removed or left as a "Marking notes" placeholder visible only to the examiner version.

## Reference files

Read these before building:

- `references/html-framework.md`: complete CSS and JS implementation with all component patterns
- `references/contract-design.md`: how to design realistic contracts with well-embedded problems
- `references/scenario-design.md`: scenario construction for memo and analysis tasks
- `references/strategy-questions.md`: strategy question templates by role type

## Output format

Present the final HTML file. Note in the summary:

1. How many tasks, total time budget
2. How many embedded contract problems and their severity distribution
3. Whether model answers are included or excluded
4. Any legal uncertainty flags the candidate or trainer should be aware of
