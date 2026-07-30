# scripts/

Developer and release tooling for the EU Data Act skill. Both utilities are plain Python 3 (no
third-party dependencies) and are referenced from `SKILL.md`.

- **`check_house_style.py`** — lints a generated memo, letter, or drafting deliverable against the
  skill's house-style rules (em dashes, banned connectors, preambles, marketing language).
  Usage: `python3 scripts/check_house_style.py <path-to-output>`.

- **`validate_sources.py`** — validates the source layer (`sources/`) before a release.
  Usage: `python3 scripts/validate_sources.py --verbose`.

The canonical, always-current versions live in the skill's GitHub repository.
