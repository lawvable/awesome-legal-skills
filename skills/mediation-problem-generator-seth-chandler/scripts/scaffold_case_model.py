#!/usr/bin/env python3
"""Create an author-only mediation case-model JSON scaffold."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_model(title: str, industry: str, mode: str) -> dict:
    parties = [
        {
            "id": "party_a",
            "name": "Party A",
            "role": "Requesting Party",
            "representatives": [],
            "decision_authority": "",
            "resources_controlled": [],
            "rights_controlled": [],
        },
        {
            "id": "party_b",
            "name": "Party B",
            "role": "Responding Party",
            "representatives": [],
            "decision_authority": "",
            "resources_controlled": [],
            "rights_controlled": [],
        },
    ]
    private_template = {
        "positions": [],
        "interests": [],
        "protected_interests": [],
        "constraints": [],
        "targets": [],
        "reservation_conditions": [],
        "batna": {"description": "", "risks": []},
        "watna": {"description": "", "risks": []},
        "private_resources": [],
        "private_risks": [],
        "beliefs_and_suspicions": [],
        "trade_authority": [],
        "desired_information": [],
        "facts_known": [],
    }
    return {
        "schema_version": "1.0",
        "metadata": {
            "title": title,
            "industry": industry,
            "mode": mode,
            "requested_outputs": [],
            "source_files": [],
            "author_assumptions": [],
        },
        "parties": parties,
        "facts": [],
        "public_case": {
            "relationship": "",
            "chronology": [],
            "agreements": [],
            "dispute_issues": [],
            "claims_and_defenses": [],
            "public_numbers": [],
            "mediation_context": "",
        },
        "private_cases": {
            "party_a": json.loads(json.dumps(private_template)),
            "party_b": json.loads(json.dumps(private_template)),
        },
        "financials": [],
        "settlement_design": {
            "core_tension": "",
            "protected_interests": {"party_a": [], "party_b": []},
            "cross_trades": [],
            "contingencies": [],
            "candidate_packages": [],
            "unsound_packages": [],
            "corridor_explanation": "",
        },
        "validation": {
            "ownership_groups": [],
            "payment_schedules": [],
            "narrow_window": {
                "feasible_package_count": 0,
                "obvious_split_is_sound": False,
                "requires_linked_concessions": True,
                "requires_private_information": True,
                "difficulty_rating": "unassessed",
            },
            "audit_history": [],
            "open_questions": [],
            "originality_notes": [],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--title", default="Untitled Mediation Problem")
    parser.add_argument("--industry", default="Unspecified commercial setting")
    parser.add_argument(
        "--mode",
        choices=("sparse_full_package", "general_to_confidentials"),
        default="sparse_full_package",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite an existing file")
    args = parser.parse_args()

    if args.output.exists() and not args.force:
        parser.error(f"Refusing to overwrite existing file: {args.output}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(build_model(args.title, args.industry, args.mode), indent=2) + "\n",
        encoding="utf-8",
    )
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
