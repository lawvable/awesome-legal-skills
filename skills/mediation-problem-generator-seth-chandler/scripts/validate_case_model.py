#!/usr/bin/env python3
"""Validate deterministic integrity of a mediation case-model JSON file."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


TOP_LEVEL = {
    "schema_version",
    "metadata",
    "parties",
    "facts",
    "public_case",
    "private_cases",
    "financials",
    "settlement_design",
    "validation",
}
FACT_STATUSES = {
    "objective",
    "belief",
    "allegation",
    "legal_uncertainty",
    "deliberate_ambiguity",
}
DIFFICULTIES = {"impossible", "brittle", "narrow_sound", "too_easy", "unassessed"}


class Findings:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def nonempty(value: Any) -> bool:
    return value not in (None, "", [], {})


def require_keys(obj: Any, keys: set[str], path: str, out: Findings) -> None:
    if not isinstance(obj, dict):
        out.error(f"{path} must be an object")
        return
    for key in sorted(keys):
        if key not in obj:
            out.error(f"{path}.{key} is required")


def load_model(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Top-level JSON value must be an object")
    return data


def validate_metadata(model: dict, out: Findings) -> None:
    meta = model.get("metadata")
    require_keys(
        meta,
        {"title", "industry", "mode", "requested_outputs", "source_files", "author_assumptions"},
        "metadata",
        out,
    )
    if not isinstance(meta, dict):
        return
    if meta.get("mode") not in {"sparse_full_package", "general_to_confidentials"}:
        out.error("metadata.mode must be sparse_full_package or general_to_confidentials")
    for key in ("title", "industry"):
        if not nonempty(meta.get(key)):
            out.error(f"metadata.{key} must not be empty")
    if not isinstance(meta.get("requested_outputs"), list) or not meta.get("requested_outputs"):
        out.error("metadata.requested_outputs must be a nonempty list")
    for key in ("source_files", "author_assumptions"):
        if not isinstance(meta.get(key), list):
            out.error(f"metadata.{key} must be a list")


def validate_parties(model: dict, out: Findings) -> list[str]:
    parties = model.get("parties")
    if not isinstance(parties, list) or len(parties) != 2:
        out.error("parties must contain exactly two principal parties")
        return []
    ids: list[str] = []
    required = {
        "id",
        "name",
        "role",
        "representatives",
        "decision_authority",
        "resources_controlled",
        "rights_controlled",
    }
    for i, party in enumerate(parties):
        require_keys(party, required, f"parties[{i}]", out)
        if isinstance(party, dict):
            party_id = party.get("id")
            if not isinstance(party_id, str) or not party_id:
                out.error(f"parties[{i}].id must be a nonempty string")
            else:
                ids.append(party_id)
            for key in ("name", "role", "decision_authority"):
                if not nonempty(party.get(key)):
                    out.error(f"parties[{i}].{key} must not be empty")
    if len(ids) != len(set(ids)):
        out.error("party IDs must be unique")
    return ids


def validate_facts(model: dict, party_ids: list[str], out: Findings) -> None:
    facts = model.get("facts")
    if not isinstance(facts, list):
        out.error("facts must be a list")
        return
    if not facts:
        out.error("facts must not be empty")
    seen: set[str] = set()
    allowed_visibility = {"public", "shared_private", "author_only"} | {
        f"party:{party_id}" for party_id in party_ids
    }
    for i, fact in enumerate(facts):
        require_keys(fact, {"id", "text", "status", "visibility"}, f"facts[{i}]", out)
        if not isinstance(fact, dict):
            continue
        fact_id = fact.get("id")
        if not isinstance(fact_id, str) or not fact_id:
            out.error(f"facts[{i}].id must be a nonempty string")
        elif fact_id in seen:
            out.error(f"duplicate fact ID: {fact_id}")
        else:
            seen.add(fact_id)
        if fact.get("status") not in FACT_STATUSES:
            out.error(f"facts[{i}].status is invalid")
        if fact.get("visibility") not in allowed_visibility:
            out.error(f"facts[{i}].visibility is invalid: {fact.get('visibility')}")
        if not nonempty(fact.get("text")):
            out.error(f"facts[{i}].text must not be empty")
        if fact.get("status") in {"belief", "allegation"} and fact.get("knower") not in party_ids:
            out.error(f"facts[{i}] belief/allegation must identify a party ID in knower")
    for party_id in party_ids:
        if not any(
            isinstance(fact, dict) and fact.get("visibility") == f"party:{party_id}"
            for fact in facts
        ):
            out.error(f"facts must contain at least one private fact for {party_id}")


def validate_public_case(model: dict, out: Findings) -> None:
    public = model.get("public_case")
    required = {
        "relationship",
        "chronology",
        "agreements",
        "dispute_issues",
        "claims_and_defenses",
        "public_numbers",
        "mediation_context",
    }
    require_keys(public, required, "public_case", out)
    if not isinstance(public, dict):
        return
    for key in ("relationship", "chronology", "dispute_issues", "claims_and_defenses", "mediation_context"):
        if not nonempty(public.get(key)):
            out.error(f"public_case.{key} must not be empty")


def validate_private_cases(model: dict, party_ids: list[str], out: Findings) -> None:
    private = model.get("private_cases")
    if not isinstance(private, dict):
        out.error("private_cases must be an object keyed by party IDs")
        return
    if set(private) != set(party_ids):
        out.error("private_cases keys must exactly match party IDs")
    required = {
        "positions",
        "interests",
        "protected_interests",
        "constraints",
        "targets",
        "reservation_conditions",
        "batna",
        "watna",
        "private_resources",
        "private_risks",
        "beliefs_and_suspicions",
        "trade_authority",
        "desired_information",
        "facts_known",
    }
    for party_id in party_ids:
        case = private.get(party_id)
        require_keys(case, required, f"private_cases.{party_id}", out)
        if not isinstance(case, dict):
            continue
        for key in (
            "positions",
            "interests",
            "protected_interests",
            "constraints",
            "targets",
            "reservation_conditions",
            "private_resources",
            "trade_authority",
        ):
            if not nonempty(case.get(key)):
                out.error(f"private_cases.{party_id}.{key} must not be empty")
        for key in ("batna", "watna"):
            value = case.get(key)
            if not isinstance(value, dict) or not nonempty(value.get("description")):
                out.error(f"private_cases.{party_id}.{key}.description must not be empty")


def validate_financials(model: dict, party_ids: list[str], out: Findings) -> None:
    financials = model.get("financials")
    if not isinstance(financials, list):
        out.error("financials must be a list")
        return
    if not financials:
        out.error("financials must contain at least one material number")
    by_id: dict[str, dict] = {}
    for i, item in enumerate(financials):
        require_keys(item, {"id", "label", "value", "currency", "unit", "visibility"}, f"financials[{i}]", out)
        if not isinstance(item, dict):
            continue
        fin_id = item.get("id")
        if not isinstance(fin_id, str) or not fin_id:
            out.error(f"financials[{i}].id must be a nonempty string")
            continue
        if fin_id in by_id:
            out.error(f"duplicate financial ID: {fin_id}")
        by_id[fin_id] = item
        value = item.get("value")
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
            out.error(f"financials[{i}].value must be a finite number")

    for fin_id, item in by_id.items():
        calc = item.get("calculation")
        if not calc:
            continue
        if not isinstance(calc, dict):
            out.error(f"financials.{fin_id}.calculation must be an object")
            continue
        operation = calc.get("operation")
        inputs = calc.get("inputs", [])
        if operation not in {"sum", "difference", "product", "percentage"}:
            out.error(f"financials.{fin_id}.calculation.operation is unsupported")
            continue
        if not isinstance(inputs, list) or any(x not in by_id for x in inputs):
            out.error(f"financials.{fin_id}.calculation.inputs contains an unknown financial ID")
            continue
        values = [by_id[x]["value"] for x in inputs]
        expected: float | None = None
        if operation == "sum":
            expected = sum(values)
        elif operation == "difference" and len(values) == 2:
            expected = values[0] - values[1]
        elif operation == "product" and values:
            expected = math.prod(values)
        elif operation == "percentage" and len(values) == 2:
            expected = values[0] * values[1] / 100
        else:
            out.error(f"financials.{fin_id}.calculation has the wrong number of inputs")
        if expected is not None:
            tolerance = float(calc.get("tolerance", 0.01))
            if not math.isclose(float(item["value"]), expected, rel_tol=0, abs_tol=tolerance):
                out.error(f"financials.{fin_id} value {item['value']} does not equal calculated {expected}")


def validate_settlement(model: dict, party_ids: list[str], out: Findings) -> None:
    settlement = model.get("settlement_design")
    required = {
        "core_tension",
        "protected_interests",
        "cross_trades",
        "contingencies",
        "candidate_packages",
        "unsound_packages",
        "corridor_explanation",
    }
    require_keys(settlement, required, "settlement_design", out)
    if not isinstance(settlement, dict):
        return
    for key in ("core_tension", "corridor_explanation"):
        if not nonempty(settlement.get(key)):
            out.error(f"settlement_design.{key} must not be empty")
    protected = settlement.get("protected_interests")
    if not isinstance(protected, dict) or set(protected) != set(party_ids):
        out.error("settlement_design.protected_interests must be keyed by both party IDs")
    else:
        for party_id in party_ids:
            if not nonempty(protected.get(party_id)):
                out.error(f"settlement_design.protected_interests.{party_id} must not be empty")
    cross_trades = settlement.get("cross_trades")
    if not isinstance(cross_trades, list) or len(cross_trades) < 2:
        out.error("settlement_design.cross_trades must contain at least two trades")
    if not nonempty(settlement.get("contingencies")):
        out.error("settlement_design.contingencies must contain at least one uncertainty-management term")
    packages = settlement.get("candidate_packages")
    if not isinstance(packages, list) or not 2 <= len(packages) <= 4:
        out.error("settlement_design.candidate_packages must contain two to four packages")
        return
    package_ids: set[str] = set()
    package_required = {
        "id",
        "title",
        "terms",
        "concessions_by_party",
        "interests_served",
        "implementation",
        "risk_controls",
        "soundness_reason",
        "distinctive_dimension",
    }
    for i, package in enumerate(packages):
        require_keys(package, package_required, f"candidate_packages[{i}]", out)
        if not isinstance(package, dict):
            continue
        package_id = package.get("id")
        if not isinstance(package_id, str) or not package_id:
            out.error(f"candidate_packages[{i}].id must be a nonempty string")
        if package_id in package_ids:
            out.error(f"duplicate candidate package ID: {package_id}")
        package_ids.add(package_id)
        if not isinstance(package.get("terms"), list) or len(package["terms"]) < 2:
            out.error(f"candidate_packages[{i}] must contain at least two linked terms")
        for field in ("concessions_by_party", "interests_served"):
            mapping = package.get(field)
            if not isinstance(mapping, dict) or set(mapping) != set(party_ids):
                out.error(f"candidate_packages[{i}].{field} must be keyed by both party IDs")
            elif any(not nonempty(mapping[p]) for p in party_ids):
                out.error(f"candidate_packages[{i}].{field} must be nonempty for each party")
        for field in ("implementation", "risk_controls", "soundness_reason", "distinctive_dimension"):
            if not nonempty(package.get(field)):
                out.error(f"candidate_packages[{i}].{field} must not be empty")


def validate_control_totals(model: dict, out: Findings) -> None:
    validation = model.get("validation")
    require_keys(
        validation,
        {"ownership_groups", "payment_schedules", "narrow_window", "audit_history", "open_questions", "originality_notes"},
        "validation",
        out,
    )
    if not isinstance(validation, dict):
        return
    for i, group in enumerate(validation.get("ownership_groups", [])):
        shares = group.get("shares") if isinstance(group, dict) else None
        if not isinstance(shares, list) or any(not isinstance(x, (int, float)) for x in shares):
            out.error(f"validation.ownership_groups[{i}].shares must be numeric")
        elif not math.isclose(sum(shares), float(group.get("expected_total", 100)), abs_tol=0.01):
            out.error(f"validation.ownership_groups[{i}] shares do not equal expected total")
    for i, schedule in enumerate(validation.get("payment_schedules", [])):
        installments = schedule.get("installments") if isinstance(schedule, dict) else None
        total = schedule.get("total") if isinstance(schedule, dict) else None
        if not isinstance(installments, list) or any(not isinstance(x, (int, float)) for x in installments):
            out.error(f"validation.payment_schedules[{i}].installments must be numeric")
        elif not isinstance(total, (int, float)) or not math.isclose(sum(installments), total, abs_tol=0.01):
            out.error(f"validation.payment_schedules[{i}] installments do not equal total")
    narrow = validation.get("narrow_window")
    require_keys(
        narrow,
        {"feasible_package_count", "obvious_split_is_sound", "requires_linked_concessions", "requires_private_information", "difficulty_rating"},
        "validation.narrow_window",
        out,
    )
    if isinstance(narrow, dict):
        package_count = len(model.get("settlement_design", {}).get("candidate_packages", []))
        if narrow.get("feasible_package_count") != package_count:
            out.error("validation.narrow_window.feasible_package_count must equal candidate package count")
        if narrow.get("difficulty_rating") not in DIFFICULTIES:
            out.error("validation.narrow_window.difficulty_rating is invalid")
        if narrow.get("obvious_split_is_sound") is not False:
            out.error("validation.narrow_window.obvious_split_is_sound must be false")
        if narrow.get("requires_linked_concessions") is not True:
            out.error("validation.narrow_window.requires_linked_concessions must be true")
        if narrow.get("requires_private_information") is not True:
            out.error("validation.narrow_window.requires_private_information must be true")
    originality = validation.get("originality_notes")
    if not isinstance(originality, list) or len(originality) < 3:
        out.error("validation.originality_notes must contain at least three notes")
    history = validation.get("audit_history")
    if not isinstance(history, list):
        out.error("validation.audit_history must be a list")
    else:
        required_audit = {
            "iteration",
            "hard_errors",
            "high_severity",
            "medium_severity",
            "new_high_severity",
            "summary",
        }
        for i, entry in enumerate(history):
            require_keys(entry, required_audit, f"validation.audit_history[{i}]", out)


def validate_final(model: dict, out: Findings) -> None:
    validation = model.get("validation", {})
    narrow = validation.get("narrow_window", {})
    if narrow.get("difficulty_rating") != "narrow_sound":
        out.error("final validation requires difficulty_rating narrow_sound")
    history = validation.get("audit_history")
    if not isinstance(history, list) or len(history) < 2:
        out.error("final validation requires at least two audit-history entries")
        return
    for entry in history[-2:]:
        if not isinstance(entry, dict):
            out.error("audit-history entries must be objects")
            continue
        for key in ("hard_errors", "high_severity", "new_high_severity"):
            if entry.get(key) != 0:
                out.error(f"last two audit iterations must have {key}=0")


def run_validation(model: dict, final: bool) -> Findings:
    out = Findings()
    missing = TOP_LEVEL - set(model)
    for key in sorted(missing):
        out.error(f"top-level field {key} is required")
    validate_metadata(model, out)
    party_ids = validate_parties(model, out)
    validate_facts(model, party_ids, out)
    validate_public_case(model, out)
    validate_private_cases(model, party_ids, out)
    validate_financials(model, party_ids, out)
    validate_settlement(model, party_ids, out)
    validate_control_totals(model, out)
    if final:
        validate_final(model, out)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    parser.add_argument("--final", action="store_true")
    parser.add_argument("--report", type=Path, help="Write machine-readable findings")
    args = parser.parse_args()
    try:
        model = load_model(args.model)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    findings = run_validation(model, args.final)
    result = {"errors": findings.errors, "warnings": findings.warnings}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for message in findings.errors:
        print(f"ERROR: {message}")
    for message in findings.warnings:
        print(f"WARNING: {message}")
    print(f"Validation complete: {len(findings.errors)} error(s), {len(findings.warnings)} warning(s)")
    return 1 if findings.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
