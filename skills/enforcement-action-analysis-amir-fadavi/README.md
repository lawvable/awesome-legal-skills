# enforcement-action-analysis

A Claude skill that analyzes OFAC and OFSI enforcement actions and produces a structured root cause analysis as a formatted Excel spreadsheet.

Drop in an enforcement action — URL, PDF, or paste — and get a working compliance self-assessment table in seconds.

**Built by [Sanctrust](https://sanctrust.com) · Free to use under MIT License**

---

## What it does

Reads any OFAC or OFSI enforcement action and outputs a six-column `.xlsx` table:

| Column | Description |
|--------|-------------|
| **Root Cause** | Short label identifying the compliance failure |
| **What Went Wrong** | What happened in this specific case |
| **How It Went Wrong** | The underlying failure mechanism |
| **What Could Have Stopped It** | Concrete controls that would have prevented it |
| **Is my organization immune to this?** | ☐ Yes / ☐ No / ☐ Partial — fill in during review |
| **Notes** | Free-text field for your team's observations |

The skill always cross-references OFAC's own **Compliance Considerations** section and the **OFAC Compliance Framework root cause taxonomy**, so the output reflects the regulator's stated expectations — not just generic advice.

---

## Example outputs

| Enforcement Action | Penalty | Root Causes Found |
|--------------------|---------|-------------------|
| FTI Consulting, Inc. (June 2026) | $1,050,000 | 3 |
| Adani Enterprises Limited (2025) | $275,000,000 | 5 |

---

## How to install

1. Download `enforcement-action-analysis.skill`
2. In Claude, go to **Settings → Skills** and upload the `.skill` file
3. The skill is now available in your Claude sessions

---

## How to trigger

Just describe what you want. Any of these will work:

- *"Analyze this enforcement action: [URL or paste text]"*
- *"What were the root causes in the FTI Consulting OFAC settlement?"*
- *"Turn this into a compliance checklist"*
- *"How do I make sure this doesn't happen to us?"*
- Upload a PDF of an enforcement action and ask Claude to analyze it

---

## Who it's for

Compliance officers, in-house counsel, external counsel, and consultants — at financial institutions and non-financial firms. The output is designed to be used directly in compliance reviews, board presentations, and program gap assessments.

---

## Files in this repo

```
enforcement-action-analysis/
├── SKILL.md          # The skill itself — instructions Claude follows
├── README.md         # This file
└── LICENSE           # MIT License
```

The `.skill` file (installable package) is available on the [Releases](../../releases) page.

---

## License

MIT — free to use, modify, and distribute. See [LICENSE](LICENSE).
