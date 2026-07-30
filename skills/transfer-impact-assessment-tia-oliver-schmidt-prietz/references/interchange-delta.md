# TIA → RoPA Interchange Delta Format

This file documents how the TIA skill emits delta files that update RoPA's register. It conforms to RoPA's `interchange-inbound-schema.json` v1.0 (defined in `skills/ropa/references/interchange-inbound-schema.md`).

The TIA skill produces ONE delta file per assessed transfer that is linked to a RoPA activity.

---

## File Location and Naming

Delta files are written to:

```
skills/ropa-workspace/<org-slug>/inbound/tia-<target-activity-id>-<timestamp>.delta.json
```

Where:
- `<org-slug>` — slug for the organisation (e.g. `acme-gmbh`)
- `<target-activity-id>` — UUID of the RoPA ActivityEntry / ProcessorEntry being updated
- `<timestamp>` — ISO 8601 with hour-minute precision (e.g. `2026-05-28T1430+0200`)

Example: `tia-9a7fa4c8-3b0a-4f9d-a5d6-8e2b7a0f9c12-2026-05-28T1430+0200.delta.json`

---

## Delta File Structure

```json
{
  "schema_version": "1.0",
  "source_skill": "tia v<X.Y>",
  "produced_at": "2026-05-28T14:30:00+02:00",
  "target_activity_id": "9a7fa4c8-3b0a-4f9d-a5d6-8e2b7a0f9c12",
  "target_entry_type": "controller_activity",
  "patches": [
    {
      "op": "replace",
      "path": "/transfers/0/tia_ref",
      "value": "TIA-US-2026-001",
      "field_label": "TIA reference"
    },
    {
      "op": "replace",
      "path": "/transfers/0/tia_status",
      "value": "proceed_with_measures",
      "field_label": "TIA status"
    },
    {
      "op": "replace",
      "path": "/transfers/0/tia_completed_date",
      "value": "2026-05-28",
      "field_label": "TIA completion date"
    },
    {
      "op": "replace",
      "path": "/transfers/0/tia_review_date",
      "value": "2027-05-28",
      "field_label": "TIA next review date"
    },
    {
      "op": "replace",
      "path": "/transfers/0/supplementary_measures",
      "value": ["TM-1 encryption-exporter-keys", "CM-1 transparency-obligation", "CM-2 challenge-clause"],
      "field_label": "Supplementary measures"
    }
  ],
  "context": {
    "summary": "TIA completed for US transfer via SCCs Module 2. Step 3 conclusion: transfer tool not effective, supplementary measures required. Proceed with TM-1 + CM-1 + CM-2.",
    "rationale_doc": "skills/tia-workspace/acme-gmbh/TIA-US-2026-001.docx",
    "rationale_doc_sha256": "<sha256 hex of the docx>",
    "output_links": [
      "skills/tia-workspace/acme-gmbh/TIA-US-2026-001.md"
    ]
  }
}
```

---

## Field Reference

| Field | Required | Notes |
|---|---|---|
| `schema_version` | yes | Always `"1.0"` for current RoPA inbound schema |
| `source_skill` | yes | `"tia v<X.Y>"` |
| `produced_at` | yes | ISO 8601 with timezone |
| `target_activity_id` | yes | UUID — must exist in target RoPA sidecar |
| `target_entry_type` | no | `controller_activity` (default) or `processor_activity` |
| `patches` | yes | RFC 6902 subset (replace/add operations) |
| `context.summary` | yes | One sentence — surfaces in RoPA docx and session log |
| `context.rationale_doc` | yes | Path to the formal TIA .docx |
| `context.rationale_doc_sha256` | recommended | Tamper-evidence |
| `context.output_links` | optional | Additional artefacts (e.g. markdown report) |

---

## TIA Status Enum

The `tia_status` patch value uses these enum values:

- `proceed` — Step 3 conclusion (1): transfer tool effective
- `proceed_with_measures` — Step 3 conclusion (2): measures adopted, effectiveness sufficient
- `proceed_no_realistic_risk` — Step 3 conclusion (3): no realistic basis for problematic law to apply
- `suspend` — Step 3 conclusion (2) but measures insufficient OR no Chapter V mechanism in place
- `adequacy` — covered by Art. 45 adequacy decision (lightweight assessment only)
- `art49_consent` — Art. 49(1)(a) basis
- `art49_contract` — Art. 49(1)(b) basis
- `art49_other` — other Art. 49 derogation (with sub-provision noted in summary)

---

## Producer-Side Responsibilities

The TIA skill:
1. Reads the RoPA sidecar to confirm the `target_activity_id` exists.
2. Emits the delta only after the TIA is signed off (Section 6 of the .docx complete).
3. Writes the file atomically (temp file + rename).
4. Computes the SHA-256 of the rationale doc and includes it in the delta.
5. Does NOT delete or modify any prior deltas.

Once written, the delta is owned by RoPA. RoPA's merge mode will read, validate, apply, and move the file to `inbound/applied/` or `inbound/rejected/` accordingly.
