---
name: tabular-review-lawvable
description: "Guide to analyze multiple documents (PDF, DOCX) against user-defined columns and produce a structured Excel output with citations. Use when the user wants to: (1) Extract specific information from multiple documents into a table, (2) Compare clauses or provisions across contracts, (3) Create a document review matrix with source citations. Triggers on: 'tabular review', 'document matrix', 'extract from documents', 'compare across documents', 'review multiple contracts'."
metadata:
  author: "Dr. Antoine Louis"
  license: "agpl-3.0"
  version: "2026-04-10"
---

# Tabular Review

Extract structured data from multiple documents into an Excel matrix with citations.

## Required Skills

- **pdf** - For reading PDF documents
- **docx** - For reading Word documents
- **xlsx** - For creating the Excel output

## Workflow

### Step 1: Gather User Requirements

Use `AskUserQuestion` to collect:

1. **Document folder path** - Where are the documents?
2. **Output filename** - Name for the Excel file
3. **Columns to extract** - What information to pull from each document

Example column definitions:
```
- Parties: Names of all parties to the agreement
- Effective Date: When the agreement becomes effective
- Term: Duration of the agreement
- Governing Law: Jurisdiction for disputes
```

### Step 2: Discover Documents

Use `Glob` to find all documents:

```
Glob(pattern: "**/*.pdf", path: "<folder>")
Glob(pattern: "**/*.docx", path: "<folder>")
```

### Step 3: Process Documents in Parallel

Launch background agents to process documents concurrently. Each agent:
- Reads assigned documents using pdf or docx skill
- Extracts values for each column
- Captures page/paragraph citations
- Returns structured JSON

**Launch agents:**
```
Task(
  prompt: "<agent_prompt>",
  subagent_type: "general-purpose",
  run_in_background: true
)
```

**Agent prompt template:**
```
You are processing documents for a tabular review.

DOCUMENTS TO PROCESS:
<list of document paths>

COLUMNS TO EXTRACT:
<column definitions>

For each document:
1. Read the document using the pdf skill (for .pdf) or docx skill (for .docx)
2. Extract the requested information for each column
3. Note the page number (PDF) or section (DOCX) where you found the information
4. Include a brief quote (30-50 chars) showing the source text

Return your results as JSON:
{
  "results": [
    {
      "document": "<filename>",
      "path": "<absolute_path>",
      "extractions": [
        {
          "column": "<column_name>",
          "value": "<extracted_value>",
          "page": <page_number>,
          "quote": "<brief_context_quote>"
        }
      ]
    }
  ]
}

If you cannot find information for a column, set value to "Not found" and explain in the quote field.
```

**Distribution strategy:**
- For N documents and M agents, each agent processes ceil(N/M) documents
- Default: 10 agents maximum
- Adjust based on document count

### Step 4: Collect Results

Wait for all background agents to complete:

```
TaskOutput(task_id: "<agent_id>", block: true)
```

Aggregate all results into a single array of document extractions.

### Step 5: Generate Excel Output

Invoke the **xlsx skill** to create the output file:

```
Create an Excel workbook at <output_path>:

SHEET 1: "Document Review"
- Header row: Document | <Column1> | <Column2> | ...
- Data rows: One row per document

For each extraction cell:
- Cell value: The extracted text
- Cell hyperlink: file://<document_path>#page=<N> (for PDFs)
- Cell comment: "Page <N>: '<quote>'"

SHEET 2: "Summary"
- Total documents: <count>
- Documents processed: <count>
- Extraction date: <today>
```

## JSON Schema

**Extraction result format:**
```json
{
  "document": "Contract_ABC.pdf",
  "path": "/path/to/Contract_ABC.pdf",
  "extractions": [
    {
      "column": "Parties",
      "value": "Acme Corp and Beta Inc",
      "page": 1,
      "quote": "entered into between Acme Corp and Beta Inc"
    },
    {
      "column": "Effective Date",
      "value": "January 15, 2025",
      "page": 1,
      "quote": "effective as of January 15, 2025"
    }
  ]
}
```

## Excel Output Format

**Cell with citation:**
- Value: "Acme Corp and Beta Inc"
- Hyperlink: `file:///path/to/Contract_ABC.pdf#page=1`
- Comment: `Page 1: "entered into between Acme Corp and Beta Inc"`

**Color coding (optional):**
- Green: Value found with high confidence
- Yellow: Value found but uncertain
- Red: Value not found

## Error Handling

| Scenario | Action |
|----------|--------|
| Document unreadable | Log error, mark row as failed, continue |
| Column not found | Set value to "Not found", explain in comment |
| Agent timeout | Collect partial results, note incomplete |
| Missing skill | Prompt user to install required skill |

## Example Usage

```
User: I want to do a tabular review of my contracts

Claude: [Uses AskUserQuestion]
  - What folder contains your documents?
  - What should I name the output Excel file?
  - What columns do you want to extract?

User: ~/Contracts, review.xlsx, Parties/Date/Term/Governing Law

Claude: [Discovers 15 documents via Glob]
Claude: [Launches 5 background agents, 3 docs each]
Claude: [Collects results via TaskOutput]
Claude: [Creates review.xlsx via xlsx skill]

Output: review.xlsx with 15 rows, 4 columns, hyperlinks and citations
```
