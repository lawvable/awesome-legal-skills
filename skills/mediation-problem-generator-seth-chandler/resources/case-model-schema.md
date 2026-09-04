# Canonical Case Model

Use `case-model.json` as the author-only source of truth. Distributed documents are views of this model, never independent sources.

## Contents

- Required top-level shape
- Metadata
- Parties
- Facts
- Public case
- Private cases
- Financials
- Settlement design
- Validation

## Required Top-Level Shape

```json
{
  "schema_version": "1.0",
  "metadata": {},
  "parties": [],
  "facts": [],
  "public_case": {},
  "private_cases": {},
  "financials": [],
  "settlement_design": {},
  "validation": {}
}
```

## Metadata

Require:

- `title`: original problem title.
- `industry`: commercial setting.
- `mode`: `sparse_full_package` or `general_to_confidentials`.
- `requested_outputs`: distributed outputs requested by the user.
- `source_files`: supplied source paths, if any.
- `author_assumptions`: assumptions made from a sparse prompt.

## Parties

Use exactly two principal parties unless the user expressly requests a multi-party problem. Each party requires:

```json
{
  "id": "party_a",
  "name": "Company or person",
  "role": "Requesting Party",
  "representatives": [],
  "decision_authority": "Scope of settlement authority",
  "resources_controlled": [],
  "rights_controlled": []
}
```

Do not give a representative power the organization has not granted.

## Facts

Store each material fact once:

```json
{
  "id": "fact_001",
  "text": "Concise atomic proposition",
  "status": "objective",
  "visibility": "public",
  "knower": null,
  "source": "created or supplied page reference",
  "date": null,
  "related_ids": []
}
```

Allowed status values:

- `objective`
- `belief`
- `allegation`
- `legal_uncertainty`
- `deliberate_ambiguity`

Allowed visibility values:

- `public`
- `party:<party-id>`
- `shared_private`
- `author_only`

For `belief` and `allegation`, identify the believing or alleging party in `knower`. Do not convert a belief into an objective fact in another document.

## Public Case

Require:

- `relationship`: commercial relationship and history.
- `chronology`: ordered event objects with dates or sequence labels.
- `agreements`: relevant public contracts and obligations.
- `dispute_issues`: live issues and public positions.
- `claims_and_defenses`: legal or contractual uncertainty without resolving it.
- `public_numbers`: references to financial item IDs.
- `mediation_context`: rules, attendees, authority, location, and timing if relevant.

Do not include targets, reservation conditions, undisclosed financial distress, private alternatives, hidden motivations, or intended packages.

## Private Cases

Key `private_cases` by both party IDs. Each requires:

```json
{
  "positions": [],
  "interests": [],
  "protected_interests": [],
  "constraints": [],
  "targets": [],
  "reservation_conditions": [],
  "batna": {},
  "watna": {},
  "private_resources": [],
  "private_risks": [],
  "beliefs_and_suspicions": [],
  "trade_authority": [],
  "desired_information": [],
  "facts_known": []
}
```

Model a reservation condition as a boundary that may combine cash and non-cash value. Do not assume every interest has a precise monetary value.

## Financials

Store every material number in `financials`:

```json
{
  "id": "fin_001",
  "label": "Annual contract price",
  "value": 3000000,
  "currency": "EUR",
  "unit": "total",
  "owner": "party_a",
  "visibility": "public",
  "calculation": null,
  "notes": ""
}
```

Use `calculation` for a machine-checkable relationship when useful:

```json
{
  "operation": "sum",
  "inputs": ["fin_002", "fin_003"],
  "tolerance": 0.01
}
```

Supported validator operations are `sum`, `difference`, `product`, and `percentage`.

Record ownership checks under `validation.ownership_groups` and installment checks under `validation.payment_schedules`.

## Settlement Design

Require:

- `core_tension`: why public positions conflict.
- `protected_interests`: keyed by both party IDs.
- `cross_trades`: at least two exchanges in which the parties value terms differently.
- `contingencies`: terms that manage uncertainty through triggers, pilots, earn-outs, options, audits, or staged performance.
- `candidate_packages`: two to four materially different sound agreements.
- `unsound_packages`: tempting agreements that fail and why.
- `corridor_explanation`: why agreement is possible but difficult.

Each candidate package requires:

```json
{
  "id": "pkg_1",
  "title": "Package name",
  "terms": [],
  "concessions_by_party": {
    "party_a": [],
    "party_b": []
  },
  "interests_served": {
    "party_a": [],
    "party_b": []
  },
  "implementation": [],
  "risk_controls": [],
  "soundness_reason": "Why it is lawful, authorized, financeable, and durable",
  "distinctive_dimension": "What makes this materially different from other packages"
}
```

Do not quote candidate packages verbatim in the confidential packets. The packets supply ingredients, not answer keys.

## Validation

Require:

```json
{
  "ownership_groups": [],
  "payment_schedules": [],
  "narrow_window": {
    "feasible_package_count": 0,
    "obvious_split_is_sound": false,
    "requires_linked_concessions": true,
    "requires_private_information": true,
    "difficulty_rating": "narrow_sound"
  },
  "audit_history": [],
  "open_questions": [],
  "originality_notes": []
}
```

Each audit history entry requires `iteration`, `hard_errors`, `high_severity`, `medium_severity`, `new_high_severity`, and `summary`. A final package needs two consecutive entries with `hard_errors`, `high_severity`, and `new_high_severity` all equal to zero.
