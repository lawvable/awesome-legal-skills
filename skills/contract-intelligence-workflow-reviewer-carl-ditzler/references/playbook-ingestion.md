# Playbook Ingestion

Use this file whenever the user provides a playbook, clause bank, standard template, or fallback positions by upload or cloud source.

## Accepted Inputs

Allow:

- direct file upload
- approved cloud-source link to a specific file
- approved connector path or identifier for a specific file

Preferred source types, in order:

1. existing Markdown or plain text
2. DOCX
3. structured XLSX or CSV
4. text PDF
5. scanned PDF

## Core Rule

Do not use a raw source file alone as the playbook source of truth when filesystem saving is available.

Create and maintain all three layers when possible:

- original source file reference in metadata
- readable extraction at `source.md`
- canonical structured version at `normalized.yaml`

The model should reason primarily from:

- `normalized.yaml` for clause comparison and scoring
- `source.md` for nuance, verification, and extraction fallback

## Required User Questions

Ask the user:

- Do you want to upload the playbook file or connect an approved cloud source?
- Which file is the controlling playbook?
- May the original source file be copied locally, or should only derived text and metadata be stored?
- If the playbook is in a cloud source, which specific file or path should control?
- If multiple playbooks exist, which one has priority?

## Save Structure

Save playbooks under:

```text
.contract-review/playbooks/<playbook-slug>/
  metadata.yaml
  source.md
  normalized.yaml
```

If local file copies are allowed, also record the original local or remote source path in metadata.

## Metadata Requirements

Record in `metadata.yaml`:

```yaml
playbook_metadata:
  playbook_name: ""
  source_type: "upload|connector|link|local"
  source_format: "md|txt|docx|xlsx|csv|pdf|unknown"
  connector_alias: ""
  source_identifier: ""
  original_file_local_copy_allowed: false
  extraction_method: ""
  extraction_confidence: "high|medium|low"
  normalized_at: ""
  notes: []
```

## Extraction Rules

- Convert the readable source into Markdown when possible.
- Preserve headings, clause names, tables, and fallback language structure.
- If a source table cannot be represented cleanly, rewrite it into Markdown sections without changing substance.
- If extraction quality is weak, lower confidence and warn the user.

## Confidence Rules

- `High`: the source is Markdown, text, DOCX, or a clean structured sheet with minimal ambiguity
- `Medium`: the source is readable but formatting or table structure is partially degraded
- `Low`: the source is scanned, OCR-heavy, or materially ambiguous

If extraction confidence is `Low`, tell the user that the playbook should be reviewed or replaced with a cleaner source.

## Cloud Source Rules

- Only use approved connectors or approved shared links.
- Record exact source provenance.
- Do not assume folder-level approval implies file-level approval if the user has limited the source more narrowly.

## Normalization Rule

After extracting Markdown, normalize the playbook into structured YAML before using it for deviation scoring.
