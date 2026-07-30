from __future__ import annotations

from ..lexicon import MONEY_RE
from ..utils import classify_headers, has_payment_verb, infer_role_from_text, money_text, render_row_text, row_values

# W6 T4 Item C: single-token generic role words that appear as table "party"
# column values are internal cross-references rather than real party names.
# This static set is the harvest-time floor: words that are NEVER standalone
# party identifiers regardless of document context.  "party" and "parties"
# belong here because they always describe a role category, not a specific
# contracting entity.
#
# Context-sensitive suppression (resolver stage): words like "company",
# "vendor", "purchaser", etc. are suppressed at the resolver when a
# defined_party_alias candidate in the same run maps that same role word to a
# specific named party.  If no such mapping exists, the bare role word IS the
# party identifier (e.g. "Vendor" in a compliance schedule where Vendor was
# never given a legal name) and must be promoted.  See resolver.py
# _suppress_defined_role_table_parties.
_GENERIC_ROLE_WORDS: frozenset[str] = frozenset({
    "party", "parties",
})


def _materialise_obligation_description(party: str, obligation: str, deadline: str) -> str:
    """Build a human-readable obligation description from table cell values.

    Shape: "Party shall <obligation> by <deadline>" (when all three present).
    Omits parts that are empty.  Verbatim cell text is preserved for the
    obligation action core; party and deadline are joined with modal "shall"
    and preposition "by" so the description matches label phrasing.
    """
    if not obligation:
        return obligation
    if party and deadline:
        return f"{party} shall {obligation[0].lower() + obligation[1:]} by {deadline}"
    if party:
        return f"{party} shall {obligation[0].lower() + obligation[1:]}"
    if deadline:
        return f"{obligation} by {deadline}"
    return obligation


def harvest_tables(h) -> None:
    for t_idx, table in enumerate(getattr(h.doc, "tables", []) or []):
        headers = [str(item or "").strip() for item in getattr(table, "headers", []) or []]
        header_map = classify_headers(headers)
        for r_idx, row in enumerate(getattr(table, "rows", []) or [], start=1):
            cells = [str(item or "").strip() for item in row]
            if not any(cells):
                continue
            values = row_values(headers, cells, header_map)
            text = render_row_text(headers, cells)
            source_ref = h._table_source_ref(table, t_idx, r_idx)
            h.synthetic_table_block_count += 1
            harvest_table_row(h, values, text, source_ref)


def harvest_table_row(h, row_values: dict[str, str], text: str, source_ref) -> None:
    party = row_values.get("party", "")
    obligation = row_values.get("obligation", "")
    deadline = row_values.get("deadline", "")
    status = row_values.get("status", "")
    control = row_values.get("control", "")
    document = row_values.get("document", "")
    amount = row_values.get("amount", "")
    risk = row_values.get("risk", "")
    if party:
        h.known_aliases.add(party.lower())
        # W6 T4 Item C: suppress bare generic role words (single-token values
        # like "Company", "Vendor") from table_party frame -- they are internal
        # cross-references, not real party names.
        party_tokens = party.strip().split()
        is_generic = len(party_tokens) == 1 and party_tokens[0].lower() in _GENERIC_ROLE_WORDS
        if not is_generic:
            h._add_candidate("parties", "table_party", {"name": party, "role": infer_role_from_text(party), "type": "party"}, text, source_ref, 0.86, ["table_row_binding", "party_header"])
    if obligation:
        signals = ["table_row_binding", "obligation_header", "legal_action_object"]
        if party:
            signals.append("known_party_subject")
        if deadline:
            signals.append("deadline_signal")
        # Materialise description with party + deadline context (Defect D fix).
        description = _materialise_obligation_description(party, obligation, deadline)
        h._add_candidate("obligations", "table_obligation", {"party": party or "unspecified", "description": description, "deadline": deadline or None, "status": status or None}, text, source_ref, 0.86 if party or deadline else 0.72, signals)
    if deadline:
        h._add_candidate("deadlines", "table_deadline", {"date_or_timing": deadline, "party": party or None, "description": obligation or text}, text, source_ref, 0.84, ["table_row_binding", "deadline_signal"])
    if control:
        h._add_candidate("controls", "table_control", {"description": control, "owner": party or None, "obligation_id": "unlinked", "evidence_documents": [document] if document else []}, text, source_ref, 0.82, ["table_row_binding", "control_header"])
    if document:
        h._add_candidate("documents", "table_document", {"name": document, "type": "document", "parties": [party] if party else [], "description": obligation or control or text}, text, source_ref, 0.80, ["table_row_binding", "document_header"])
    if amount or (MONEY_RE.search(text) and has_payment_verb(text)):
        h._add_candidate("transfers", "table_payment", {"from_party": party or None, "to_party": "unspecified", "amount_text": amount or money_text(text), "description": text, "timing": deadline or None}, text, source_ref, 0.78, ["table_row_binding", "payment_signal"])
    if risk:
        h._add_candidate("risk_items", "table_risk", {"label": risk, "description": text, "category": status or None, "x_score": 0.5, "y_score": 0.5}, text, source_ref, 0.74, ["table_row_binding", "risk_header"])
