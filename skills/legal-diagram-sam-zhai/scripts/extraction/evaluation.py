"""Pass-2 evaluation library: grade an LLM patch against user-owned label expectations.

This module implements the grading pipeline for eval_pass2.py. It reuses the
patching.validate and patching.apply_patch APIs for all gate logic; no V1-V9
knowledge lives here.

Public API:
    grade(manifest_bytes, manifest, patch_ops, labels) -> GradeResult
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

# Reuse the patching API for gate and apply.
try:
    from extraction.patching import validate as _gate_validate
    from extraction.patching import apply_patch as _gate_apply
    from extraction.patching import Finding
except ImportError:
    from scripts.extraction.patching import validate as _gate_validate  # type: ignore[no-redef]
    from scripts.extraction.patching import apply_patch as _gate_apply  # type: ignore[no-redef]
    from scripts.extraction.patching import Finding  # type: ignore[no-redef]


# ---------------------------------------------------------------------------
# V3 evidence resolution -- replicated minimally from patching._collect_evidence_ids
# See patching.py _collect_evidence_ids and _v3_evidence_resolves for the canonical logic.
# ---------------------------------------------------------------------------

def _collect_known_ids(manifest: dict[str, Any]) -> set[str]:
    """Collect all known evidence / hint IDs from a manifest.

    Mirrors patching._collect_evidence_ids; kept minimal and local to avoid
    reaching into private patching internals.
    """
    ids: set[str] = set()
    for ep in manifest.get("candidate_manifest", {}).get("evidence_packets", []):
        if ep.get("id"):
            ids.add(ep["id"])
    for ep in manifest.get("llm_enrichment", {}).get("evidence_packets", []):
        if ep.get("id"):
            ids.add(ep["id"])
    for hint in manifest.get("extraction_hints", []):
        if hint.get("id"):
            ids.add(hint["id"])
    return ids


# ---------------------------------------------------------------------------
# JSON Pointer -- thin wrapper for evaluation; reuse patching internals indirectly
# via apply_patch; define pointer-get here for expectation evaluation.
# ---------------------------------------------------------------------------

def _parse_pointer(pointer: str) -> list[str]:
    if pointer == "":
        return []
    if not pointer.startswith("/"):
        raise ValueError(f"Invalid JSON Pointer (must start with /): {pointer!r}")
    tokens = pointer[1:].split("/")
    return [t.replace("~1", "/").replace("~0", "~") for t in tokens]


def _pointer_get(obj: Any, pointer: str) -> Any:
    """Get value at JSON Pointer path; raise KeyError/IndexError on miss."""
    tokens = _parse_pointer(pointer)
    if not tokens:
        return obj
    current = obj
    for token in tokens:
        if isinstance(current, dict):
            if token not in current:
                raise KeyError(f"Key not found: {token!r}")
            current = current[token]
        elif isinstance(current, list):
            idx = int(token)
            if idx < 0 or idx >= len(current):
                raise IndexError(f"Array index out of range: {idx}")
            current = current[idx]
        else:
            raise TypeError(f"Cannot index into {type(current).__name__}")
    return current


# ---------------------------------------------------------------------------
# result types
# ---------------------------------------------------------------------------

@dataclass
class ExpectationResult:
    id: str
    credit: str  # "required" | "bonus"
    pass_: bool
    detail: str

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "credit": self.credit, "pass": self.pass_, "detail": self.detail}


@dataclass
class ForbiddenViolation:
    id: str
    kind: str
    detail: str

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "kind": self.kind, "detail": self.detail}


@dataclass
class Score:
    required_pass: int = 0
    required_total: int = 0
    bonus_pass: int = 0
    bonus_total: int = 0
    forbidden_violations: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "required_pass": self.required_pass,
            "required_total": self.required_total,
            "bonus_pass": self.bonus_pass,
            "bonus_total": self.bonus_total,
            "forbidden_violations": self.forbidden_violations,
        }


@dataclass
class GradeResult:
    ok: bool
    fixture: str
    labelled: bool
    gate_findings: list[Finding] = field(default_factory=list)
    results: list[ExpectationResult] = field(default_factory=list)
    forbidden_violations: list[ForbiddenViolation] = field(default_factory=list)
    score: Score = field(default_factory=Score)
    vacuous: bool = False

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "ok": self.ok,
            "fixture": self.fixture,
            "labelled": self.labelled,
            "gate_findings": [f.to_dict() for f in self.gate_findings],
            "results": [r.to_dict() for r in self.results],
            "forbidden_violations": [v.to_dict() for v in self.forbidden_violations],
            "score": self.score.to_dict(),
        }
        if self.vacuous:
            d["vacuous"] = True
        return d


# ---------------------------------------------------------------------------
# staleness check
# ---------------------------------------------------------------------------

def _staleness_finding(manifest_bytes: bytes, labels: dict[str, Any]) -> Finding | None:
    """Return a warn Finding if the manifest bytes do not match the frozen sha256 in labels."""
    expected_sha = labels.get("frozen_manifest_sha256", "")
    if not expected_sha:
        return None
    actual_sha = hashlib.sha256(manifest_bytes).hexdigest()
    if actual_sha != expected_sha:
        return Finding(
            rule="labels_stale",
            severity="warn",
            path="",
            message=(
                f"Manifest sha256 {actual_sha!r} does not match "
                f"frozen_manifest_sha256 {expected_sha!r}; labels may be stale"
            ),
        )
    return None


# ---------------------------------------------------------------------------
# expectation evaluators
# ---------------------------------------------------------------------------

def _is_filled(value: Any) -> bool:
    """Return True if value is considered filled: not None, not empty string/list/dict."""
    if value is None:
        return False
    if value == "":
        return False
    if isinstance(value, (list, dict)) and len(value) == 0:
        return False
    return True


def _eval_field_filled(
    exp: dict[str, Any],
    enriched: dict[str, Any],
) -> ExpectationResult:
    path = exp.get("path", "")
    try:
        value = _pointer_get(enriched, path)
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        return ExpectationResult(
            id=exp["id"], credit=exp["credit"],
            pass_=False, detail=f"Path {path!r} not found: {exc}",
        )
    filled = _is_filled(value)
    return ExpectationResult(
        id=exp["id"], credit=exp["credit"],
        pass_=filled,
        detail=f"value={value!r}" if not filled else f"value present ({type(value).__name__})",
    )


def _eval_value_matches(
    exp: dict[str, Any],
    enriched: dict[str, Any],
) -> ExpectationResult | None:
    """Evaluate value_matches expectation.

    Returns None when the predicate shape is invalid (caller emits exit 2).
    """
    path = exp.get("path", "")
    predicate = exp.get("predicate", {})

    pred_keys = [k for k in ("equals", "one_of", "regex") if k in predicate]
    if len(pred_keys) != 1:
        return None  # signal: invalid predicate shape

    try:
        value = _pointer_get(enriched, path)
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        return ExpectationResult(
            id=exp["id"], credit=exp["credit"],
            pass_=False, detail=f"Path {path!r} not found: {exc}",
        )

    key = pred_keys[0]
    if key == "equals":
        passed = value == predicate["equals"]
        detail = f"value={value!r}, expected {predicate['equals']!r}"
    elif key == "one_of":
        passed = value in predicate["one_of"]
        detail = f"value={value!r}, allowed={predicate['one_of']!r}"
    else:  # regex
        pattern = predicate["regex"]
        if not isinstance(value, str):
            passed = False
            detail = f"value={value!r} is not a string; regex requires string"
        else:
            passed = bool(re.fullmatch(pattern, value))
            detail = f"value={value!r}, pattern={pattern!r}"

    return ExpectationResult(
        id=exp["id"], credit=exp["credit"],
        pass_=passed, detail=detail,
    )


def _entities_matching(arr: list[Any], match: dict[str, Any]) -> list[Any]:
    """Return all elements of arr where all match fields are equal."""
    results = []
    for item in arr:
        if isinstance(item, dict) and all(item.get(k) == v for k, v in match.items()):
            results.append(item)
    return results


def _eval_entity_added(
    exp: dict[str, Any],
    frozen_er: dict[str, Any],
    enriched: dict[str, Any],
    known_ids: set[str],
) -> ExpectationResult:
    """Evaluate entity_added expectation.

    Passes when the entity identified by match fields exists in the named array
    of the enriched result AND was not already present in the frozen extraction_result
    (net-new count must increase vs frozen).

    Evidence resolution is done via known_ids (mirrors V3 logic from patching).
    """
    predicate = exp.get("predicate", {})
    array_name = predicate.get("array", "")
    match = predicate.get("match", {})

    frozen_arr = frozen_er.get(array_name, [])
    enriched_arr = enriched.get(array_name, [])

    frozen_matching = _entities_matching(frozen_arr if isinstance(frozen_arr, list) else [], match)
    enriched_matching = _entities_matching(enriched_arr if isinstance(enriched_arr, list) else [], match)

    # The entity must exist in enriched AND the count must exceed the frozen count.
    net_new = len(enriched_matching) - len(frozen_matching)

    if net_new > 0:
        # Verify evidence_id resolves for at least one of the new entities (V3 mirror).
        new_entities = enriched_matching[len(frozen_matching):]
        ev_ok = all(
            e.get("evidence_id") is None or e.get("evidence_id") in known_ids
            for e in new_entities
        )
        if ev_ok:
            return ExpectationResult(
                id=exp["id"], credit=exp["credit"],
                pass_=True,
                detail=f"Entity matching {match!r} found in {array_name!r} (net-new: {net_new})",
            )
        return ExpectationResult(
            id=exp["id"], credit=exp["credit"],
            pass_=False,
            detail=f"Entity matching {match!r} added to {array_name!r} but evidence_id does not resolve",
        )
    if enriched_matching:
        return ExpectationResult(
            id=exp["id"], credit=exp["credit"],
            pass_=False,
            detail=f"Entity matching {match!r} in {array_name!r} already existed in frozen manifest",
        )
    return ExpectationResult(
        id=exp["id"], credit=exp["credit"],
        pass_=False,
        detail=f"No entity matching {match!r} found in {array_name!r} after patch",
    )


def _eval_unchanged(
    exp: dict[str, Any],
    frozen_er: dict[str, Any],
    enriched: dict[str, Any],
) -> ExpectationResult:
    path = exp.get("path", "")
    try:
        frozen_val = _pointer_get(frozen_er, path)
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        return ExpectationResult(
            id=exp["id"], credit=exp["credit"],
            pass_=False, detail=f"Path {path!r} not found in frozen: {exc}",
        )
    try:
        enriched_val = _pointer_get(enriched, path)
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        return ExpectationResult(
            id=exp["id"], credit=exp["credit"],
            pass_=False, detail=f"Path {path!r} not found in enriched: {exc}",
        )
    passed = frozen_val == enriched_val
    return ExpectationResult(
        id=exp["id"], credit=exp["credit"],
        pass_=passed,
        detail=(
            "value unchanged" if passed
            else f"frozen={frozen_val!r}, enriched={enriched_val!r}"
        ),
    )


# ---------------------------------------------------------------------------
# forbidden evaluators
# ---------------------------------------------------------------------------

def _eval_no_entity_added(
    forb: dict[str, Any],
    frozen_er: dict[str, Any],
    enriched: dict[str, Any],
) -> ForbiddenViolation | None:
    """Return a violation if the patch added an entity matching the match dict."""
    array_name = forb.get("array", "")
    match = forb.get("match", {})

    frozen_arr = frozen_er.get(array_name, [])
    enriched_arr = enriched.get(array_name, [])

    frozen_count = len(_entities_matching(frozen_arr if isinstance(frozen_arr, list) else [], match))
    enriched_count = len(_entities_matching(enriched_arr if isinstance(enriched_arr, list) else [], match))

    if enriched_count > frozen_count:
        return ForbiddenViolation(
            id=forb["id"], kind=forb["kind"],
            detail=(
                f"Forbidden entity matching {match!r} was added to {array_name!r} "
                f"(frozen count {frozen_count}, enriched count {enriched_count})"
            ),
        )
    return None


def _eval_path_untouched(
    forb: dict[str, Any],
    frozen_er: dict[str, Any],
    enriched: dict[str, Any],
) -> ForbiddenViolation | None:
    """Return a violation if the value at path is unchanged between frozen and enriched.

    Also report a violation if the path was present in frozen but removed in enriched.
    """
    path = forb.get("path", "")
    try:
        frozen_val = _pointer_get(frozen_er, path)
    except (KeyError, IndexError, TypeError, ValueError):
        # Path absent in frozen; cannot be "untouched" in a meaningful sense.
        return None

    try:
        enriched_val = _pointer_get(enriched, path)
    except (KeyError, IndexError, TypeError, ValueError):
        # Path present in frozen but absent in enriched: it was removed.
        return ForbiddenViolation(
            id=forb["id"], kind=forb["kind"],
            detail=f"Path {path!r} was removed by the patch",
        )

    if frozen_val == enriched_val:
        return ForbiddenViolation(
            id=forb["id"], kind=forb["kind"],
            detail=f"Path {path!r} was not changed by the patch; value={frozen_val!r}",
        )
    return None


# ---------------------------------------------------------------------------
# main grading entry point
# ---------------------------------------------------------------------------

class PredicateError(Exception):
    """Raised when a value_matches expectation has an invalid predicate shape."""


def grade(
    manifest_bytes: bytes,
    manifest: dict[str, Any],
    patch_ops: Any,
    labels: dict[str, Any],
) -> GradeResult:
    """Grade a patch against label expectations.

    Pipeline:
    1. Staleness check (warn, non-blocking).
    2. Gate (validate); any error finding aborts grading.
    3. Apply patch on deep copy.
    4. Evaluate each expectation.
    5. Evaluate each forbidden entry.
    6. Compute score.

    Raises PredicateError when a value_matches predicate shape is invalid
    (caller must map to exit 2).
    """
    fixture = labels.get("fixture", "")
    labelled = bool(labels.get("labelled", False))
    gate_findings: list[Finding] = []

    # Step 1: staleness check
    stale = _staleness_finding(manifest_bytes, labels)
    if stale is not None:
        gate_findings.append(stale)

    # Step 2: gate
    gate_results = _gate_validate(manifest, patch_ops)
    gate_findings.extend(gate_results)

    has_errors = any(f.severity == "error" for f in gate_findings)
    if has_errors:
        return GradeResult(
            ok=False,
            fixture=fixture,
            labelled=labelled,
            gate_findings=gate_findings,
            results=[],
            forbidden_violations=[],
            score=Score(),
        )

    # Step 3: apply patch
    frozen_er = manifest.get("extraction_result", {})
    enriched_er = _gate_apply(frozen_er, patch_ops if isinstance(patch_ops, list) else [])

    # Vacuous case: not yet labelled
    if not labelled:
        return GradeResult(
            ok=True,
            fixture=fixture,
            labelled=labelled,
            gate_findings=gate_findings,
            results=[],
            forbidden_violations=[],
            score=Score(),
            vacuous=True,
        )

    # Step 4: expectations
    known_ids = _collect_known_ids(manifest)
    expectations = labels.get("expectations", [])
    results: list[ExpectationResult] = []

    for exp in expectations:
        kind = exp.get("kind", "")
        if kind == "field_filled":
            results.append(_eval_field_filled(exp, enriched_er))
        elif kind == "value_matches":
            result = _eval_value_matches(exp, enriched_er)
            if result is None:
                raise PredicateError(
                    f"Expectation {exp.get('id')!r}: value_matches predicate must have exactly one "
                    f"of equals/one_of/regex; got keys {list(exp.get('predicate', {}).keys())!r}"
                )
            results.append(result)
        elif kind == "entity_added":
            results.append(_eval_entity_added(exp, frozen_er, enriched_er, known_ids))
        elif kind == "unchanged":
            results.append(_eval_unchanged(exp, frozen_er, enriched_er))
        else:
            results.append(ExpectationResult(
                id=exp.get("id", "?"), credit=exp.get("credit", "required"),
                pass_=False, detail=f"Unknown expectation kind {kind!r}",
            ))

    # Step 5: forbidden
    forbidden_violations: list[ForbiddenViolation] = []
    for forb in labels.get("forbidden", []):
        kind = forb.get("kind", "")
        if kind == "no_entity_added":
            v = _eval_no_entity_added(forb, frozen_er, enriched_er)
        elif kind == "path_untouched":
            v = _eval_path_untouched(forb, frozen_er, enriched_er)
        else:
            v = None
        if v is not None:
            forbidden_violations.append(v)

    # Step 6: score
    required = [r for r in results if r.credit == "required"]
    bonus = [r for r in results if r.credit == "bonus"]
    score = Score(
        required_pass=sum(1 for r in required if r.pass_),
        required_total=len(required),
        bonus_pass=sum(1 for r in bonus if r.pass_),
        bonus_total=len(bonus),
        forbidden_violations=len(forbidden_violations),
    )

    return GradeResult(
        ok=True,
        fixture=fixture,
        labelled=labelled,
        gate_findings=gate_findings,
        results=results,
        forbidden_violations=forbidden_violations,
        score=score,
    )
