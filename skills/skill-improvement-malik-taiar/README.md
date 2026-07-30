# Self-Improve Skill

A self-improving skill system that analyzes your work sessions and proposes improvements to other skills.

## Commands

| Command | Description |
|---------|-------------|
| `self-improve` | Analyze current session and propose skill improvements |
| `self-improve [skill-name]` | Target a specific skill |
| `self-improve on` | Enable automatic mode |
| `self-improve off` | Disable automatic mode |
| `self-improve status` | Check automatic mode status |
| `self-improve [skill-name] history` | View modification history |

## Manual Usage

After working with a skill, run `self-improve` to capture improvements:

```
> self-improve my-skill

--- Self-Improve: my-skill ---

Proposed additions:

1. "Always check for X before proceeding"
   Source: User correction at 14:32

2. "Use table format for Y"
   Source: User accepted format at 14:45

---

Apply these changes? [Y/n]
```

## Manual vs Automatic Mode

### Manual Mode (default)

Run `self-improve` whenever you want to capture improvements from a session. Nothing happens automatically.

### Automatic Mode

When enabled, the skill automatically analyzes your session at the end and proposes improvements for your approval.

**To enable:**

1. Run `self-improve on`

2. Add the hook to your local Claude Code settings (`.claude/settings.local.json`):

```json
{
  "hooks": {
    "stop": [
      {
        "type": "command",
        "command": "./skills/skill-optimizer-en-malik-taiar/scripts/self-improve-hook.sh"
      }
    ]
  }
}
```

3. At the end of each session, you'll see proposed improvements and be asked to approve them

**To disable:** Run `self-improve off`

## How It Works

### Signal Detection

The skill scans conversations for:
- **Corrections**: "No", "That's wrong", "Always do X"
- **Successes**: "Perfect", "Exactly", accepted outputs
- **Edge cases**: Workarounds needed, unhandled scenarios

### Quality Criteria

Each correction is evaluated against 4 criteria to ensure high-quality skill improvements:

1. **Complete**: Includes all information needed to apply the instruction
2. **Precise**: No vague or subjective terms
3. **Atomic**: One check per instruction (not bundled)
4. **Stable**: No time-dependent references without specific dates

### Grading

| Criteria Met | Action |
|--------------|--------|
| All 4 criteria | Add to skill directly |
| Less than 4 | Ask for clarification, but add anyway if user insists |

### Why Quality Criteria Matter

Without rigorous criteria, skills accumulate vague instructions like "be more thorough" or "use the standard format" that are impossible to follow consistently.

The quality criteria ensure every instruction added to a skill is:
- Actionable without guessing
- Understandable by anyone reading the skill
- Consistently applicable across sessions

## History

All modifications are tracked in `CHANGELOG.md` within each skill folder. View with `self-improve [skill-name] history`.

The history is written in natural language (no git knowledge required). You can revert to any previous version through the history command.
