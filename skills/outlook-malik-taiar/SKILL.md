---
name: outlook-emails-lawvable
description: Read, search, and download emails and attachments from Microsoft Outlook via OAuth2. Use when the user asks to (1) check, read, or fetch emails or messages from Outlook, (2) search emails by keyword, sender, or subject, (3) download email attachments such as contracts, NDAs, or documents, (4) chain email content into other skills (e.g. "read the latest email from X and review the attached NDA"), or (5) any task involving Microsoft Outlook, Office 365, or Exchange email access.
metadata:
  author: Malik Taiar (Lawvable)
  license: AGPL-3.0
  version: 2026.02.02
---

# Outlook Email Integration (Read-Only)

## Overview

| What this skill does | What it does NOT do |
| --- | --- |
| Read and search Outlook emails | Send emails |
| Download email attachments | Store any data between sessions |
| Integrate with other Skills (NDA, contracts) | Require any technical setup |

## Getting Started

No configuration needed. Just run the skill and sign in with your Microsoft account.

### Read emails

```bash
# Last 10 emails
uv run .agents/skills/outlook-emails-lawvable/scripts/outlook_oauth.py

# Last 5 emails
uv run .agents/skills/outlook-emails-lawvable/scripts/outlook_oauth.py --limit 5
```

### Search emails

```bash
# Search by keyword
uv run .agents/skills/outlook-emails-lawvable/scripts/outlook_oauth.py --search "NDA"

# Search by sender
uv run .agents/skills/outlook-emails-lawvable/scripts/outlook_oauth.py --from "jean@example.com"
```

### Download attachments

```bash
uv run .agents/skills/outlook-emails-lawvable/scripts/outlook_oauth.py --download
```

---

## Authentication

Each run opens a browser window for Microsoft login. Sign in with your Microsoft account and accept the permissions.

**Read-only access.** The skill only requests permission to read your emails and your profile. It cannot send emails or modify anything.

**Zero data retention.** No token is stored between sessions. Each time you run the skill, you authenticate fresh. Nothing is cached on disk.

**Your password is never shared with Lawvable.**

---

## Integration with Other Skills

### Example: Email → NDA Review

```
User: "Read the latest email from jean@partner.com and review
       the NDA attachment using the NDA skill"

Claude will:
1. Use outlook_oauth.py to fetch the email
2. Download the .docx attachment
3. Use nda-review-jamie-tso skill to analyze
4. Return the issue log with redlines
```

---

## Advanced: Use Your Own Azure App

If you prefer to use your own Azure App Registration, set this environment variable:

```
AZURE_CLIENT_ID=your-client-id
```

See `references/AZURE_SETUP.md` for the full setup guide.
