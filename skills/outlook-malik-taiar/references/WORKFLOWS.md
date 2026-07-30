# Common Legal Workflows with Outlook Integration

## Workflow 1: NDA Review from Email

### Scenario
A partner sends you an NDA for review via email. You want to quickly review it.

### Prompt
```
Read the latest email from jean@partner.com, download the NDA attachment,
and review it using the NDA skill.
```

### What Claude Does
1. **Fetch email** → runs `outlook_oauth.py --from "jean@partner.com" --limit 1 --download`
2. **Download attachment** → saves `.docx` to attachments folder
3. **Review NDA** → uses `nda-review-jamie-tso` skill
4. **Return analysis** → issue log with suggested redlines

### Output
- Issue log with clause-by-clause analysis
- Suggested redlines and fallback positions

---

## Workflow 2: Batch Contract Triage

### Scenario
You have multiple contract emails to process. You want to categorize them and prioritize.

### Prompt
```
Find all emails from this week with attachments containing "contract" or "agreement"
in the subject. Download them, identify the contract type, and create a triage
spreadsheet with sender, date, contract type, and urgency level.
```

### What Claude Does
1. **Search emails** → filters by date and subject keywords
2. **Download attachments** → extracts all `.docx` and `.pdf` files
3. **Classify** → determines type (NDA, MSA, DPA, Employment, etc.)
4. **Create spreadsheet** → uses `xlsx-processing-anthropic` skill

### Output
Excel file with columns:

| Sender | Date | Subject | Contract Type | Urgency | Notes |
| --- | --- | --- | --- | --- | --- |
| jean@... | 2024-01-15 | NDA Review | NDA | Medium | Standard terms |
| marie@... | 2024-01-16 | MSA Draft | MSA | High | Custom clauses |

---

## Workflow 3: Privacy Policy Request

### Scenario
A client emails asking about your privacy policy. You need to draft one based on their requirements.

### Prompt
```
Read Marie's email about the privacy policy requirements, then use the
privacy policy skill to draft a GDPR-compliant policy based on her specifications.
```

### What Claude Does
1. **Parse email** → extracts requirements (data types, purposes, transfers, etc.)
2. **Draft policy** → uses `privacy-policy-malik-taiar` skill
3. **Generate document** → creates `.docx` with proper formatting

---

## Workflow 4: Vendor Due Diligence

### Scenario
You receive vendor documentation via email and need to assess risk.

### Prompt
```
Find the email from the vendor NewTechCorp with their security documentation.
Run a due diligence assessment using the vendor assessment skill.
```

### What Claude Does
1. **Fetch email** → finds vendor email with attachments
2. **Download docs** → SOC2 reports, policies, certifications
3. **Assess** → uses `vendor-due-diligence-patrick-munro` skill
4. **Generate report** → risk scorecard with recommendations

---

## Workflow 5: Contract Amendment from Email Thread

### Scenario
You have an email thread discussing contract amendments. You need to consolidate and create an amendment document.

### Prompt
```
Read the email thread with subject "Contract Amendment Discussion" from the
last 2 weeks. Extract all agreed changes and create an amendment document.
```

### What Claude Does
1. **Fetch thread** → gets all emails in conversation
2. **Extract changes** → identifies agreed amendments
3. **Generate document** → creates formal amendment with track changes

---

## Quick Command Reference

### Reading Emails
```
"Read the latest email from [sender]"
"Find emails about [topic] from last [period]"
"Show unread emails in my inbox"
"Get emails with attachments from [sender]"
```

### Processing Attachments
```
"Download the attachment from [email description]"
"Extract text from the PDF in [sender]'s email"
"Review the Word document attached to [subject]"
```

---

## Best Practices

1. **Be specific with senders**: Use full email addresses when possible
2. **Specify time ranges**: "from last week" vs "from January 2024"
3. **Mention attachment types**: "the PDF attachment" vs "the attachment"
4. **Use keywords**: Help Claude find the right email with subject keywords
