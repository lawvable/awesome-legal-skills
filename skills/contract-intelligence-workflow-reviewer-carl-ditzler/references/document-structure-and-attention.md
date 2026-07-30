# Document Structure And Attention

Contracts are networks of clauses, definitions, exhibits, and cross-references. The review system must structure that network correctly before asking the model to reason about it.

## Core Rule

Do not rely on brute-force full-document loading as the default review method. The model should work from a structured contract map and only load the portions of the contract and playbook needed for each review task.

## Required Parsing Outputs

Before substantive review, create:

- clause tree
- definition index
- cross-reference map
- exhibit and ancillary-document registry
- clause family labels

## Required Ancillary-Document Checks

Always check whether the contract includes, incorporates, or references:

- service level agreement or service levels
- security measures, security exhibit, or security schedule
- AI terms, AI addendum, model-use terms, or service-improvement language
- DPA or privacy addendum
- BAA where PHI and HIPAA are implicated
- financial-sector cloud addendum, audit schedule, or equivalent enhanced cloud control schedule where required

## Attention Management Rules

- Load only the relevant clause plus the linked definitions, cross-referenced clauses, and relevant playbook rules.
- If a clause depends on another clause, load them together.
- If a clause depends on an exhibit or schedule, load that exhibit section with it.
- Keep the context window focused on the current issue instead of stuffing the entire agreement into one prompt.

## Retrieval Rules

Do not use vector search as the primary method for clause-to-playbook matching in active contract review.

Prefer this order:

1. structural parsing and clause-family classification
2. defined-term and cross-reference retrieval
3. deterministic term overlap and clause labels
4. targeted semantic help only as a secondary filter if needed

## Why

The system should manage attention by putting the right clauses, definitions, and constraints on the desk at the same time. Bigger context windows do not remove the need for orchestration.
