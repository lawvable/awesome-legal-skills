from __future__ import annotations

from typing import Any, Optional

from .handoff import build_candidate_manifest as _build_candidate_manifest
from .handoff import build_llm_enrichment
from .harvesters import CandidateHarvester
from .materialize import materialize_result
from .resolver import dedupe_candidates, resolve_candidates


def extract(doc: Any, *, matter_type: Optional[str] = None, input_source: Optional[str] = None):
    harvester = CandidateHarvester(doc, input_source=input_source)
    candidates = dedupe_candidates(harvester.run())
    decisions = resolve_candidates(candidates, sparse=True)
    result, decisions = materialize_result(
        candidates,
        decisions,
        harvester.evidence_packets,
        matter_type=matter_type,
        input_source=input_source,
        truncated=getattr(doc, "truncated", False),
    )
    candidate_manifest = _build_candidate_manifest(
        doc,
        harvester.evidence_packets,
        candidates,
        decisions,
        harvester.synthetic_table_block_count,
    )
    result.extraction_warnings.extend(candidate_manifest.get("warning_codes", []))
    llm_enrichment = build_llm_enrichment(candidate_manifest)
    return result, candidate_manifest, llm_enrichment


