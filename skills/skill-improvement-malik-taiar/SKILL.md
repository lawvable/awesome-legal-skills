---
name: skill-optimizer-lawvable
description: Guide to analyze a current work session and propose improvements to skills. Use (1) automatically after working with a skill to capture learnings, (2) when the user suggests improvements, corrections, or additions during a skill-related session, or (3) when the user manually invokes `self-improve`.
metadata:
  author: Malik Taiar (Lawvable)
  license: AGPL-3.0
  version: 2026.01.07
---

# Self-Improve Skill

Analyze the current conversation and propose improvements to skills based on corrections, successes, and edge cases discovered during the work session.

## Triggers

- `self-improve` - Analyze session and propose improvements
- `self-improve [skill-name]` - Target a specific skill
- `self-improve on` - Enable automatic mode (hook)
- `self-improve off` - Disable automatic mode
- `self-improve status` - Show automatic mode status
- `self-improve [skill-name] history` - Show modification history

---

## Main Workflow (`self-improve`)

### Step 1: Identify the Skill

If skill name not provided, list available skills from `skills/` directory and ask:

```
Which skill should I analyze for this session?
[List skills found in skills/ directory]
```

### Step 2: Detect Signals

Scan the conversation for **signals** - moments where the user expressed feedback:

| Signal Type | Examples |
|-------------|----------|
| **Correction** | "No", "That's not right", "It's missing X", "Always do Y", user rewrites output |
| **Success** | "Perfect", "Yes", "Exactly", user accepts without changes |
| **Edge case** | User needed a workaround, skill couldn't handle the request |

### Step 3: Evaluate Each Signal for Quality

For each correction signal, evaluate if it can become a good skill instruction.

#### Quality Criteria

**1. COMPLETE**

The instruction includes all information needed to apply it. No need to look elsewhere or make assumptions.

| Grade | Example |
|-------|---------|
| Pass | "Structure output as: Key Terms / Risk Areas / Suggested Revisions" |
| Fail | "Use the standard format" (which format?) |
| Fail | "Follow our firm's guidelines" (what guidelines?) |

**2. PRECISE**

No vague or subjective terms. Two different people reading the instruction would understand it the same way.

| Grade | Example |
|-------|---------|
| Pass | "Flag non-compete clauses over 12 months as high risk" |
| Fail | "Be more thorough in the analysis" |
| Fail | "Make it more appropriate for clients" |

**3. ATOMIC**

One instruction addresses one single requirement. Multiple checks should be split into separate instructions.

| Grade | Example |
|-------|---------|
| Pass | "Check for governing law clause" |
| Fail | "Check for governing law, jurisdiction, and arbitration clauses" (three checks - split them) |

**4. STABLE**

If referencing regulations or standards, specify the version or date. The instruction should be evaluable the same way regardless of when it's read.

| Grade | Example |
|-------|---------|
| Pass | "Review the termination provisions under our internal policy [policy name and reference], dated December 12, 2024." |
| Fail | "Follow latest market standards" (which standards? will change over time) |

### Step 4: Grade the Signal

| Criteria Met | Action |
|--------------|--------|
| **All 4 criteria pass** | Add to skill directly |
| **Less than 4 criteria** | Ask for clarification (see Step 5) |

### Step 5: Ask for Clarification

When feedback doesn't meet all criteria, ask for what's missing using the `AskUserQuestion` tool:

```
I detected a correction but need more information to improve the skill.

You said: "[user's feedback]"

To create a clearer instruction, I need the following information: 

[Structured tool call listing what's missing based on failed criteria]
```

**If the user provides clarification** → Update the instruction and proceed to Step 6.

**If the user prefers the original** → Proceed to Step 6 with the original instruction.

### Step 6: Propose Changes

```
--- Learning: [skill-name] ---

Proposed additions:

1. "[exact instruction to add]"
   Source: "[quote from conversation]"

2. "[exact instruction to add]"
   Source: "[quote from conversation]"

---

Apply these changes? [Y/n]
```

### Step 7: If Approved

1. **Update SKILL.md**
    - Read `skills/[skill-name]/SKILL.md`
    - Add each instruction in the appropriate section
    - Each instruction must be readable and applicable on its own

2. **Update `skills/[skill-name]/CHANGELOG.md`** 
    - Create if doesn't exist
    - Add new entry AT THE TOP:
      ```markdown
      ## [DATE (format: "January 7, 2026")]
      [Description of changes in natural language, 1-3 sentences]
      ```
    - Entry rules:
      - Most recent at top
      - 1-3 sentences max
      - Natural language
      - No git references

### Step 8: Save Observations

For signals that couldn't be processed, offer to save:

```
Save these observations for later review?
- "[signal 1]" - Status: [why insufficient]
- "[signal 2]" - Status: [why insufficient]
```

If yes, append to `skills/[skill-name]/OBSERVATIONS.md`

---

## Secondary Commands

### self-improve on

1. Run:
    ```bash
    rm -f ./.disabled
    ```
2. Reply: "Automatic mode enabled."

### self-improve off

1. Run:
    ```bash
    touch ./.disabled
    ```
2. Reply: "Automatic mode disabled."

### self-improve status

Check `.disabled` file existence and report.

## self-improve [skill-name] history

1. Display CHANGELOG.md content
2. Ask: "Would you like to revert to a previous version?"
3. If yes:
    - update the appropriate sections in `skills/[skill-name]/SKILL.md`
    - update `skills/[skill-name]/CHANGELOG.md` with a rollback note
    
---

## Examples

### Example 1: All criteria met

**User said:** "Always flag non-compete clauses over 12 months as high risk"

**Evaluation:**
- Complete: Yes - instruction is fully specified
- Precise: Yes - "12 months" and "high risk" are clear
- Atomic: Yes - single check
- Stable: Yes - no time dependency

**Result:** Add directly

### Example 2: Missing criteria

**User said:** "Flag any non-market-standard indemnification clause"

**Evaluation:**
- Complete: No - "non-market-standard" is not defined
- Precise: No - "market standard" is subjective and varies by deal type
- Atomic: Yes - single check
- Stable: No - market standards evolve over time

**Action:** Ask for clarification using the `AskUserQuestion` tool:
```
I detected a correction but need more details.

You said: "Flag any non-market-standard indemnification clause"

To make this actionable, can you specify:
- What makes an indemnification clause "non-market-standard"? (e.g., uncapped liability, coverage of indirect damages, no carve-outs for gross negligence)

Do you want to provide more details, or should I add the instruction as you stated it?
```

**If user clarifies:** Update the instruction and add it.
**If user prefers the original:** Add the instruction as stated.

---

## Important Notes

- Never guess what the user meant - always ask if unclear
- Never infer requirements from context - they must be explicit
- One instruction = one check - split bundled feedback
- Fewer good instructions is better than many vague ones
- CHANGELOG.md is the user-facing record
