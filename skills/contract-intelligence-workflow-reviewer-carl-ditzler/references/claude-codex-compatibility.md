# Claude And Codex Compatibility

Use this file to keep the skill portable across Claude and Codex.

## Core Rule

The workflow should be identical across tools whenever possible. Tool differences should change execution mechanics, not legal standards.

## Shared Source Of Truth

- `.contract-review/` is the primary cross-platform workspace state.
- `CLAUDE.md` is a Claude-friendly mirror of durable setup.
- `SKILL.md` and the bundled references define the workflow for both systems.

## Compatibility Rules

- Read `.contract-review/` first in both tools.
- If `CLAUDE.md` exists, keep it aligned with `.contract-review/`.
- Use plain Markdown, YAML, JSON, and CSV for saved artifacts.
- Do not rely on product-specific hidden memory as the only stored configuration.
- Use the same least-privilege connector defaults, retention defaults, and security notice in both tools.

## Graceful Degradation

If a capability is unavailable, continue as follows:

- No MCP or connectors: ask for file upload or pasted text.
- No filesystem write access: keep the same workflow, but present the artifacts inline and tell the user persistence was not available.
- No sub-agents: perform the stages sequentially in one agent.
- No direct file conversion tools: ask for a cleaner playbook source or manually normalize from available text with lower confidence.

## Output Portability

- Keep outputs in ordinary Markdown for human reading.
- Keep structured artifacts in YAML, JSON, or CSV.
- Use text color labels like `Green`, `Yellow`, `Orange`, and `Red` instead of UI-specific formatting assumptions.

## User-Facing Disclosure

If the current environment lacks a capability that affected the workflow, say so briefly:

- what capability was unavailable
- what fallback path was used
- whether confidence or automation scope was reduced

If the environment supports connectors or remote MCP, also disclose that provider safeguards reduce but do not eliminate risks from sensitive-data exposure, prompt injection, or unexpected tool behavior.
