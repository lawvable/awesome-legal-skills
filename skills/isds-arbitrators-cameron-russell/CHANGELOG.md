# Changelog

## 1.0.0 — 2026-08-10

Initial public release.

- Two workflows: structured arbitrator profiles (single or multiple arbitrators) and case-based shortlisting with transparent, user-adjustable ranking weights.
- Profiles grounded in the user's own UNCTAD ISDS Navigator dataset (31/12/2023 snapshot) plus targeted live lookups of ICSID arbitrator profile pages; record checks retrieve and read the underlying decisions via the companion [isds-research](https://github.com/ccrnyc/isds-research) skill.
- Shortlist scoring normalised against the candidate pool (raw-count mode available via `--raw-scores`); ranking weights always printed with the shortlist.
- Delta workflow for cases newer than the snapshot, classified by the arbitrator's acceptance date.
- Hard sourcing rules throughout: no issue-outcome claims from secondary sources; table values read from the page's own text; availability never asserted without a named, dated source; conflicting values shown, never silently resolved.
- Compliance gates on by default: targeted, user-initiated lookups only; default-deny for hosts not in the compliance table; no bulk harvesting.
- Delivery checklist enforced on every run (work-product headers, archived extracts for everything quoted, formatting spec, run-folder verification).
