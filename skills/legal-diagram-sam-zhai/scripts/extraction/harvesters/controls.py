from __future__ import annotations

import re

from ..context import HarvestContext
from ..utils import control_documents, extract_subject, heading_prior_signals, score_confidence
from ._patterns import CORP_SUFFIX_ALT

# ---------------------------------------------------------------------------
# Privacy-controls gate (W6 T3): technical and organisational security measures.
#
# Design: the existing gate pattern (verified_by / evidenced_by / audit_etc.)
# covers formal audit-trail controls in contracts.  Privacy policies describe
# security measures in prose/list form that do not mention "verified by" or
# "audit"; they need a separate gate.
# ---------------------------------------------------------------------------

# Security-measure keywords that identify a sentence as describing a control.
_PRIVACY_CONTROL_KEYWORDS = re.compile(
    r"\b("
    r"encrypt(?:ed|ion|ing)|AES-256|TLS\s*\d|"
    r"role-based\s+access|multi-factor\s+auth(?:entication)?|MFA|"
    r"access\s+control|authentication|authorization|"
    r"penetration\s+test(?:ing)?|pen\s+test(?:ing)?|"
    r"incident\s+response\s+plan|breach\s+notification|"
    r"confidentiality\s+agreement|non-disclosure\s+agreement|NDA|"
    r"privacy\s+training|security\s+training|"
    r"data\s+(?:protection|security|masking|minimisation|minimization)|"
    r"pseudonymis(?:ed|ation)|anonymis(?:ed|ation)|"
    r"security\s+(?:control|measure|safeguard|assessment)|"
    r"vulnerability\s+scan(?:ning)?|"
    r"independent\s+third\s+party\s+(?:audit|test|review)|"
    r"annual\s+(?:penetration|security|privacy)\s+(?:test(?:ing)?|audit|review)"
    r")\b",
    re.I,
)

# Heading-prior check for security/controls sections in privacy policies.
_SECURITY_HEADING_RE = re.compile(
    r"\b(security|safeguards?|controls?|technical|organisational|organizational|"
    r"privacy|data\s+protection|encryption|access\s+management)\b",
    re.I,
)

# Exclusion patterns for data-flow descriptions that are NOT security controls:
# (1) Third-party service-provider list items (bold corp name + data receipt/transfer):
#     "**Org Corp.**: receives ... data" or "**Org Inc.**: hosts ..."
# (2) Data-transfer-path descriptions: "data is transferred via encrypted ..."
# These match the keyword gate but describe WHERE data goes, not HOW it's protected.
# Role/function names in bold ("**Privacy Officer review**:") are NOT excluded.
_DATAFLOW_DESCRIPTION_RE = re.compile(
    r"(?:"
    # Bold corp-entity opener: "**Name Inc.**: ..."  (corp suffix before closing **)
    r"^\*\*[^*]*(?:" + CORP_SUFFIX_ALT + r")\*\*\s*:"
    r"|"
    # Transfer-via description: "data is transferred via" / "information is sent to"
    r"\b(?:data|information)\s+is\s+(?:transferred|sent|transmitted)\s+(?:via|to|through)\b"
    r"|"
    # Receives-for description: "receives ... data for" (third-party receipts)
    r"\breceives?\s+(?:\w+\s+){0,3}(?:data|information)\s+for\b"
    r")",
    re.I,
)

# Phrase extractor: pulls the security measure phrase from a sentence.
# For "All X is encrypted using Y and in transit using Z" -> extracts the
# whole description (we store the sentence for controls, consistent with
# existing evidence_control behaviour).
# For list items with "- " prefix we strip the leading bullet.
_LIST_BULLET_RE = re.compile(r"^\s*[-*]\s+")


def _privacy_control_description(sent: str) -> str:
    """Return the measure phrase for a privacy-control sentence."""
    # Strip leading Markdown bullet if present.
    return _LIST_BULLET_RE.sub("", sent).strip()


def harvest_controls(ctx: HarvestContext, sent: str) -> None:
    anti = ctx.anti

    # ------------------------------------------------------------------
    # Original gate: formal audit/evidence controls (contracts, compliance).
    # ------------------------------------------------------------------
    if ctx.bundle.control_patterns[0].search(sent):
        signals = ["control_signal", *heading_prior_signals(ctx.source_ref, "controls")]
        if ctx.bundle.control_patterns[1].search(sent):
            signals.append("evidence_signal")
        if ctx.bundle.legal_action_verbs.search(sent):
            signals.append("legal_action_object")
        confidence = score_confidence(0.56, signals, anti)
        ctx.add_candidate(
            "controls",
            "evidence_control",
            {
                "description": sent,
                "owner": extract_subject(sent) or None,
                "obligation_id": "unlinked",
                "evidence_documents": control_documents(sent),
            },
            sent,
            ctx.source_ref,
            confidence,
            signals,
            anti,
        )
        return  # original gate matched; skip privacy-control gate

    # ------------------------------------------------------------------
    # Privacy-control gate (W6 T3): prose/list security measures.
    # ------------------------------------------------------------------
    if not _PRIVACY_CONTROL_KEYWORDS.search(sent):
        return

    # Exclude data-flow descriptions (third-party receipts, transfer paths) that
    # accidentally match the keyword gate but are not security controls.
    if _DATAFLOW_DESCRIPTION_RE.search(sent):
        return

    heading_text = " > ".join(ctx.source_ref.heading_path or [])
    under_security_heading = bool(_SECURITY_HEADING_RE.search(heading_text))

    signals = ["privacy_control"]
    if under_security_heading:
        signals.append("heading_prior")
    if ctx.bundle.legal_action_verbs.search(sent):
        signals.append("legal_action_object")

    description = _privacy_control_description(sent)
    confidence = score_confidence(0.68 if under_security_heading else 0.65, signals, anti)
    ctx.add_candidate(
        "controls",
        "privacy_control",
        {
            "description": description,
            "owner": extract_subject(sent) or None,
            "obligation_id": "unlinked",
            "evidence_documents": [],
        },
        sent,
        ctx.source_ref,
        confidence,
        signals,
        anti,
    )
