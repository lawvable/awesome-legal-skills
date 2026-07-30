# Automation Metrics

Use this file to track workflow efficiency and bottlenecks.

## Purpose

The skill should help reduce manual work and contract cycle time. Track metrics so recurring friction becomes visible.

## Recommended Metrics

- contract opened at
- intake completed at
- review started at
- redline prepared at
- approval packet prepared at
- signature-ready reached at
- closed at
- missing-document count
- blocker count
- number of critical issues
- number of required approvals
- number of external dependencies

## Metrics File

Save `metrics.yaml` using:

```yaml
metrics:
  contract_opened_at: ""
  intake_completed_at: ""
  review_started_at: ""
  redline_prepared_at: ""
  approval_packet_prepared_at: ""
  signature_ready_at: ""
  closed_at: ""
  missing_document_count: 0
  blocker_count: 0
  critical_issue_count: 0
  required_approval_count: 0
  external_dependency_count: 0
  notes: []
```

## Use

- Update metrics at each major workflow stage.
- Mention major bottlenecks in the final summary if they materially affect timing or execution.
