# Proposed PR / submission text

## Title

Add Swiss Legal Source & Authority Triage skill

## Description

This submission adds a Swiss legal methodology skill focused on source and authority routing before legal-answer generation.

The skill helps an AI assistant identify whether a Swiss legal issue is federal, cantonal, communal, regulatory, contractual, professional, register-based, soft-law, or mixed before producing an answer. It includes a Swiss source hierarchy, official-source-first approach, multilingual/version checks, uncertainty flags, and human-review boundaries.

## Why this is useful

Swiss legal AI workflows are especially vulnerable to source-routing errors because Swiss law can involve federal, cantonal, communal, regulator, register, contractual, multilingual, doctrinal and soft-law layers. This skill is intended as infrastructure for later Swiss-law-specific skills rather than as a substantive legal-advice bot.

## What is included

- `SKILL.md`: core instructions and output structure.
- `resources/swiss-legal-source-map.md`: curated map of major free/open Swiss legal sources.
- `resources/source-hierarchy.md`: source-status hierarchy and classification labels, including a dedicated tier for doctrine and expert authority.
- `resources/doctrine-and-expert-authority-map.md`: a field-based guide to Swiss doctrinal sources and how to use them as persuasive authority.
- `resources/output-template.md`: reusable Swiss Legal Source Map template.
- `resources/examples.md`: sample outputs for employment/data protection, contract enforceability, fintech authorisation, and corporate authority.

## Safety posture

The skill does not provide Swiss legal advice. It requires source mapping, source-status classification, official-source verification where possible, uncertainty flags, and clear escalation to qualified Swiss legal review for client-specific conclusions, litigation, regulatory authorisation, deadlines, and high-risk issues.

## Suggested category

Legal Methodology / Legal Research / Jurisdictional Infrastructure
