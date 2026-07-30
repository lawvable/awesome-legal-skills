"""Patch-gate library: validate and apply RFC 6902 JSON Patch ops against a manifest's extraction_result.

Patch paths are JSON Pointer paths evaluated against the manifest's ``extraction_result`` object,
not the manifest root.

Public API:
    validate(manifest, patch_ops) -> list[Finding]
    apply_patch(extraction_result, patch_ops) -> dict
    gate(manifest, patch_ops, apply=False) -> GateResult
"""
from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import Any

# ---------------------------------------------------------------------------
# imports from the extraction package
# ---------------------------------------------------------------------------
# Must be importable whether scripts/ is on sys.path or not.  patch_gate.py
# inserts scripts/ before calling us; tests insert ROOT (which is scripts/).
try:
    from extraction.domain import ENTITY_FIELDS
    from extraction.manifest import LLM_ONLY, NULL_FIELDS
except ImportError:
    from scripts.extraction.domain import ENTITY_FIELDS  # type: ignore[no-redef]
    from scripts.extraction.manifest import LLM_ONLY, NULL_FIELDS  # type: ignore[no-redef]

# ---------------------------------------------------------------------------
# types
# ---------------------------------------------------------------------------

ALLOWED_OPS = {"add", "replace", "remove"}

# ---------------------------------------------------------------------------
# V5 sub-field exemptions: (top_field, subfield) pairs that bypass immutability
# ---------------------------------------------------------------------------
_V5_SUBFIELD_EXEMPTIONS: frozenset[tuple[str, str]] = frozenset({
    ("obligations", "risk_level"),   # NULL_FIELDS: LLM may fill in risk_level
    ("controls", "obligation_id"),   # cross-linking: LLM may set obligation_id
})

# ---------------------------------------------------------------------------
# V7 hierarchy depth limit
# ---------------------------------------------------------------------------
_MAX_HIERARCHY_DEPTH = 2


@dataclass
class Finding:
    rule: str
    severity: str  # "error" | "warn"
    path: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return {"rule": self.rule, "severity": self.severity, "path": self.path, "message": self.message}


@dataclass
class GateResult:
    ok: bool
    findings: list[Finding] = field(default_factory=list)
    enriched_extraction_result: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "ok": self.ok,
            "findings": [f.to_dict() for f in self.findings],
        }
        if self.enriched_extraction_result is not None:
            d["enriched_extraction_result"] = self.enriched_extraction_result
        return d


# ---------------------------------------------------------------------------
# JSON Pointer (RFC 6901) with add/replace/remove
# ---------------------------------------------------------------------------

def _parse_pointer(pointer: str) -> list[str]:
    """Parse a JSON Pointer string into a list of reference tokens."""
    if pointer == "":
        return []
    if not pointer.startswith("/"):
        raise ValueError(f"Invalid JSON Pointer (must start with /): {pointer!r}")
    tokens = pointer[1:].split("/")
    # RFC 6901 escape sequences: ~1 -> /, ~0 -> ~  (order matters)
    return [t.replace("~1", "/").replace("~0", "~") for t in tokens]


def _resolve_parent(obj: Any, tokens: list[str]) -> tuple[Any, str]:
    """Walk to the parent of the final token.  Return (parent_object, final_token)."""
    if not tokens:
        raise KeyError("Empty pointer: no parent")
    parent = obj
    for t in tokens[:-1]:
        if isinstance(parent, dict):
            if t not in parent:
                raise KeyError(f"Key not found: {t!r}")
            parent = parent[t]
        elif isinstance(parent, list):
            idx = int(t)
            if idx < 0 or idx >= len(parent):
                raise IndexError(f"Array index out of range: {idx}")
            parent = parent[idx]
        else:
            raise TypeError(f"Cannot traverse into {type(parent).__name__}")
    return parent, tokens[-1]


def _pointer_get(obj: Any, pointer: str) -> Any:
    """Get the value at JSON Pointer path; raise KeyError/IndexError on miss."""
    tokens = _parse_pointer(pointer)
    if not tokens:
        return obj
    parent, last = _resolve_parent(obj, tokens)
    if isinstance(parent, dict):
        if last not in parent:
            raise KeyError(f"Key not found: {last!r}")
        return parent[last]
    elif isinstance(parent, list):
        idx = int(last)
        if idx < 0 or idx >= len(parent):
            raise IndexError(f"Array index out of range: {idx}")
        return parent[idx]
    raise TypeError(f"Cannot index into {type(parent).__name__}")


def _pointer_add(obj: Any, pointer: str, value: Any) -> None:
    """RFC 6902 add: append to list (- token), insert at index, or set dict key."""
    tokens = _parse_pointer(pointer)
    if not tokens:
        raise ValueError("Cannot add at root pointer")
    parent, last = _resolve_parent(obj, tokens)
    if isinstance(parent, list):
        if last == "-":
            parent.append(value)
        else:
            idx = int(last)
            if idx < 0 or idx > len(parent):
                raise IndexError(f"Array index out of range: {idx}")
            parent.insert(idx, value)
    elif isinstance(parent, dict):
        parent[last] = value
    else:
        raise TypeError(f"Cannot add into {type(parent).__name__}")


def _pointer_replace(obj: Any, pointer: str, value: Any) -> None:
    """RFC 6902 replace: target must exist."""
    tokens = _parse_pointer(pointer)
    if not tokens:
        raise ValueError("Cannot replace root pointer")
    parent, last = _resolve_parent(obj, tokens)
    if isinstance(parent, dict):
        if last not in parent:
            raise KeyError(f"Key not found: {last!r}")
        parent[last] = value
    elif isinstance(parent, list):
        idx = int(last)
        if idx < 0 or idx >= len(parent):
            raise IndexError(f"Array index out of range: {idx}")
        parent[idx] = value
    else:
        raise TypeError(f"Cannot replace into {type(parent).__name__}")


def _pointer_remove(obj: Any, pointer: str) -> None:
    """RFC 6902 remove."""
    tokens = _parse_pointer(pointer)
    if not tokens:
        raise ValueError("Cannot remove root pointer")
    parent, last = _resolve_parent(obj, tokens)
    if isinstance(parent, dict):
        if last not in parent:
            raise KeyError(f"Key not found: {last!r}")
        del parent[last]
    elif isinstance(parent, list):
        idx = int(last)
        if idx < 0 or idx >= len(parent):
            raise IndexError(f"Array index out of range: {idx}")
        del parent[idx]
    else:
        raise TypeError(f"Cannot remove from {type(parent).__name__}")


def apply_patch(extraction_result: dict[str, Any], patch_ops: list[dict[str, Any]]) -> dict[str, Any]:
    """Apply patch ops to a deep copy of extraction_result.  Raises on path errors."""
    result = copy.deepcopy(extraction_result)
    for op_obj in patch_ops:
        op = op_obj["op"]
        path = op_obj["path"]
        if op == "add":
            _pointer_add(result, path, copy.deepcopy(op_obj["value"]))
        elif op == "replace":
            _pointer_replace(result, path, copy.deepcopy(op_obj["value"]))
        elif op == "remove":
            _pointer_remove(result, path)
        else:
            raise ValueError(f"Unsupported op: {op!r}")
    return result


# ---------------------------------------------------------------------------
# tier-guard helpers
# ---------------------------------------------------------------------------

def _top_field(path: str) -> str:
    """Return the first path segment (top-level field of extraction_result)."""
    tokens = _parse_pointer(path)
    return tokens[0] if tokens else ""  # audit-ok: credential-exposure: JSON Pointer path segment, not a credential


def _build_allowed_fields(manifest: dict[str, Any]) -> set[str]:
    """Compute the set of tier-allowed top-level fields from the manifest at runtime."""
    allowed: set[str] = set()

    # Always allowed
    allowed.update({"hierarchy", "extraction_warnings", "matter_type"})

    # (a) field values from llm_enrichment.directives
    for directive in manifest.get("llm_enrichment", {}).get("directives", []):
        f = directive.get("field", "")
        if not f:
            continue
        # Dotted form like "obligations[].risk_level" -> top field is "obligations"
        base = f.split("[")[0].split(".")[0]
        allowed.add(base)

    # (b) suggested_field values from extraction_hints
    for hint in manifest.get("extraction_hints", []):
        sf = hint.get("suggested_field", "")
        if sf:
            allowed.add(sf)

    # (c) keys of LLM_ONLY
    allowed.update(LLM_ONLY.keys())

    # (d) field names in NULL_FIELDS (first element of each tuple = array field name)
    for field_name, *_ in NULL_FIELDS:
        allowed.add(field_name)

    return allowed


# ---------------------------------------------------------------------------
# validation rules
# ---------------------------------------------------------------------------

def _v1_op_shape(patch_ops: Any) -> list[Finding]:
    findings: list[Finding] = []
    if not isinstance(patch_ops, list):
        findings.append(Finding("V1", "error", "", "Patch document must be a JSON array"))
        return findings
    for i, op_obj in enumerate(patch_ops):
        path_ctx = f"[{i}]"
        if not isinstance(op_obj, dict):
            findings.append(Finding("V1", "error", path_ctx, "Each op must be a JSON object"))
            continue
        op = op_obj.get("op")
        if op not in ALLOWED_OPS:
            findings.append(Finding("V1", "error", path_ctx, f"op {op!r} not in allowed set {ALLOWED_OPS}"))
        if "path" not in op_obj:
            findings.append(Finding("V1", "error", path_ctx, "op missing 'path' key"))
        if op in ("add", "replace") and "value" not in op_obj:
            findings.append(Finding("V1", "error", path_ctx, f"op {op!r} requires 'value' key"))
    return findings


def _collect_evidence_ids(manifest: dict[str, Any]) -> set[str]:
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


def _is_hierarchy_path(path: str) -> bool:
    tokens = _parse_pointer(path)
    return bool(tokens) and tokens[0] == "hierarchy"


def _is_matter_type_path(path: str) -> bool:
    tokens = _parse_pointer(path)
    return bool(tokens) and tokens[0] == "matter_type"


def _is_entity_array_path(path: str) -> bool:
    """Return True if the path targets an entity array (first token in ENTITY_FIELDS)."""
    tokens = _parse_pointer(path)
    return bool(tokens) and tokens[0] in ENTITY_FIELDS


def _is_scalar_subfield_path(path: str) -> bool:
    """Return True if path targets a sub-field of an entity array element (depth >= 3).

    Example: /obligations/0/risk_level has tokens ['obligations', '0', 'risk_level'] -> depth 3.
    """
    tokens = _parse_pointer(path)
    return len(tokens) >= 3 and tokens[0] in ENTITY_FIELDS


def _v2_evidence_presence(patch_ops: list[dict[str, Any]]) -> list[Finding]:
    findings: list[Finding] = []
    for op_obj in patch_ops:
        if not isinstance(op_obj, dict):
            continue
        op = op_obj.get("op")
        if op not in ("add", "replace"):
            continue
        path = op_obj.get("path", "")
        value = op_obj.get("value")

        # Hierarchy and matter_type are exempt
        if _is_hierarchy_path(path) or _is_matter_type_path(path):
            continue

        # Sub-field scalar replaces (e.g. /obligations/0/risk_level) are exempt
        if _is_scalar_subfield_path(path):
            continue

        # Only apply V2 to entity-array targets
        if not _is_entity_array_path(path):
            continue

        # Whole-entity add/replace: value must be a dict with evidence_id and source_ref
        if not isinstance(value, dict):
            continue
        missing = [k for k in ("evidence_id", "source_ref") if k not in value]
        if missing:
            findings.append(Finding(
                "V2", "error", path,
                f"Value missing required evidence keys: {missing}",
            ))
    return findings


def _v3_evidence_resolves(
    patch_ops: list[dict[str, Any]],
    known_ids: set[str],
) -> list[Finding]:
    findings: list[Finding] = []
    for op_obj in patch_ops:
        if not isinstance(op_obj, dict):
            continue
        if op_obj.get("op") not in ("add", "replace"):
            continue
        value = op_obj.get("value")
        if not isinstance(value, dict):
            continue
        ev_id = value.get("evidence_id")
        if ev_id is not None and ev_id not in known_ids:
            findings.append(Finding(
                "V3", "error", op_obj.get("path", ""),
                f"evidence_id {ev_id!r} does not resolve to any known evidence packet or hint",
            ))
    return findings


def _v4_tier_guard(
    patch_ops: list[dict[str, Any]],
    allowed_fields: set[str],
) -> list[Finding]:
    findings: list[Finding] = []
    for op_obj in patch_ops:
        if not isinstance(op_obj, dict):
            continue
        path = op_obj.get("path", "")
        top = _top_field(path)
        if top and top not in allowed_fields:
            findings.append(Finding(
                "V4", "error", path,
                f"Target field {top!r} is not in the tier-allowed set",
            ))
    return findings


def _v5_immutability(
    patch_ops: list[dict[str, Any]],
    extraction_result: dict[str, Any],
) -> list[Finding]:
    findings: list[Finding] = []
    for op_obj in patch_ops:
        if not isinstance(op_obj, dict):
            continue
        op = op_obj.get("op")
        path = op_obj.get("path", "")
        tokens = _parse_pointer(path)
        if not tokens:
            continue
        top = tokens[0]

        # V6 owns remove; skip here to avoid double-reporting
        if op == "remove":
            continue

        # Appends (/-) to any array are fine
        if op == "add" and tokens[-1] == "-":
            continue

        if op == "replace":
            # matter_type: allowed only when currently null/empty
            if _is_matter_type_path(path):
                current = extraction_result.get("matter_type")
                if current not in (None, ""):
                    findings.append(Finding(
                        "V5", "error", path,
                        "matter_type may only be replaced when currently null/empty",
                    ))
                continue

            # Sub-field replacements (depth >= 3)
            if len(tokens) >= 3 and top in ENTITY_FIELDS:
                subfield = tokens[2]
                # Exempt sub-fields that LLM is allowed to fill in or cross-link
                if (top, subfield) in _V5_SUBFIELD_EXEMPTIONS:
                    continue
                # Other sub-field replaces: check if entity exists
                # (we don't block sub-field replaces generically here; only whole-entity below)
                continue

            # Whole-entity replace: check if entity exists in extraction_result
            if top in ENTITY_FIELDS and len(tokens) >= 2:
                # An existing entity array entry is immutable
                arr = extraction_result.get(top)
                if isinstance(arr, list) and arr:
                    # An indexed replace on an existing entity is forbidden
                    try:
                        idx = int(tokens[1])
                        if 0 <= idx < len(arr):
                            findings.append(Finding(
                                "V5", "error", path,
                                f"Existing {top} entity at index {idx} may not be replaced",
                            ))
                    except (ValueError, IndexError):
                        pass
    return findings


def _v6_remove_scope(patch_ops: list[dict[str, Any]]) -> list[Finding]:
    findings: list[Finding] = []
    for op_obj in patch_ops:
        if not isinstance(op_obj, dict):
            continue
        if op_obj.get("op") != "remove":
            continue
        path = op_obj.get("path", "")
        if not _is_hierarchy_path(path):
            findings.append(Finding(
                "V6", "error", path,
                "remove ops are only allowed under /hierarchy",
            ))
    return findings


def _v7_hierarchy_integrity(
    patch_ops: list[dict[str, Any]],
    extraction_result: dict[str, Any],
) -> list[Finding]:
    """Apply all ops (in-memory trial) then check hierarchy constraints."""
    findings: list[Finding] = []
    # Trial-apply to get the post-patch state
    try:
        trial = apply_patch(extraction_result, patch_ops)
    except Exception:
        # V8 will report this; skip V7 check
        return findings

    hierarchy = trial.get("hierarchy", [])
    if not hierarchy:
        return findings

    node_ids = {n.get("id") for n in hierarchy if n.get("id")}

    for node in hierarchy:
        source = node.get("source", "")
        node_id = node.get("id", "<unknown>")
        depth = node.get("depth")
        parent = node.get("parent")

        if source not in ("deterministic", "llm"):
            findings.append(Finding(
                "V7", "error", "/hierarchy",
                f"Node {node_id!r} has invalid source {source!r}; must be 'deterministic' or 'llm'",
            ))

        if depth is not None and depth > _MAX_HIERARCHY_DEPTH:
            findings.append(Finding(
                "V7", "error", "/hierarchy",
                f"Node {node_id!r} has depth {depth} exceeding maximum of {_MAX_HIERARCHY_DEPTH}",
            ))

        if source == "llm":
            if parent not in (None, "") and parent not in node_ids:
                findings.append(Finding(
                    "V7", "error", "/hierarchy",
                    f"LLM node {node_id!r} has parent {parent!r} that does not exist in hierarchy",
                ))

    return findings


def _v8_applies_cleanly(
    patch_ops: list[dict[str, Any]],
    extraction_result: dict[str, Any],
) -> list[Finding]:
    findings: list[Finding] = []
    trial = copy.deepcopy(extraction_result)
    for i, op_obj in enumerate(patch_ops):
        if not isinstance(op_obj, dict):
            continue
        op = op_obj.get("op")
        path = op_obj.get("path", "")
        try:
            if op == "add":
                _pointer_add(trial, path, copy.deepcopy(op_obj.get("value")))
            elif op == "replace":
                _pointer_replace(trial, path, copy.deepcopy(op_obj.get("value")))
            elif op == "remove":
                _pointer_remove(trial, path)
            # Unknown ops already caught by V1; skip here
        except (KeyError, IndexError, TypeError, ValueError) as exc:
            findings.append(Finding(
                "V8", "error", path,
                f"Op [{i}] ({op!r}) failed to apply: {exc}",
            ))
    return findings


def _v9_no_op_restate(
    patch_ops: list[dict[str, Any]],
    extraction_result: dict[str, Any],
) -> list[Finding]:
    findings: list[Finding] = []
    for op_obj in patch_ops:
        if not isinstance(op_obj, dict):
            continue
        if op_obj.get("op") != "replace":
            continue
        path = op_obj.get("path", "")
        new_value = op_obj.get("value")
        try:
            current = _pointer_get(extraction_result, path)
        except (KeyError, IndexError, TypeError, ValueError):
            continue
        if current == new_value:
            findings.append(Finding(
                "V9", "warn", path,
                "replace op restates the current value; no change will occur",
            ))
    return findings


# ---------------------------------------------------------------------------
# public gate function
# ---------------------------------------------------------------------------

def validate(manifest: dict[str, Any], patch_ops: Any) -> list[Finding]:
    """Run all V1-V9 validation rules.  Return list of Finding objects."""
    findings: list[Finding] = []

    # V1 first; any V1 error suppresses downstream rules to avoid spurious secondary findings
    if not isinstance(patch_ops, list):
        findings.extend(_v1_op_shape(patch_ops))
        return findings
    v1 = _v1_op_shape(patch_ops)
    findings.extend(v1)
    if any(f.severity == "error" for f in findings):
        return findings

    extraction_result = manifest.get("extraction_result", {})
    known_ids = _collect_evidence_ids(manifest)
    allowed_fields = _build_allowed_fields(manifest)

    findings.extend(_v2_evidence_presence(patch_ops))
    findings.extend(_v3_evidence_resolves(patch_ops, known_ids))
    findings.extend(_v4_tier_guard(patch_ops, allowed_fields))
    findings.extend(_v5_immutability(patch_ops, extraction_result))
    findings.extend(_v6_remove_scope(patch_ops))
    findings.extend(_v7_hierarchy_integrity(patch_ops, extraction_result))
    findings.extend(_v8_applies_cleanly(patch_ops, extraction_result))
    findings.extend(_v9_no_op_restate(patch_ops, extraction_result))

    return findings


def gate(
    manifest: dict[str, Any],
    patch_ops: Any,
    *,
    apply: bool = False,
) -> GateResult:
    """Validate patch_ops against manifest.  If apply=True and ok, return enriched result."""
    findings = validate(manifest, patch_ops)
    has_errors = any(f.severity == "error" for f in findings)
    ok = not has_errors

    enriched: dict[str, Any] | None = None
    if ok and apply and isinstance(patch_ops, list):
        enriched = apply_patch(manifest.get("extraction_result", {}), patch_ops)

    return GateResult(ok=ok, findings=findings, enriched_extraction_result=enriched)
