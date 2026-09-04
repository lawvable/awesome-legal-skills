# Lawve Submission Requirements
<!-- token-scan: exempt — this file documents the forbidden tokens -->

Codified from lawve.ai's submission form, the lawve-ai/awesome-legal-skills CONTRIBUTING.md,
and its submit-skill issue template, as of July 2026. **This is a snapshot.** Where the live
form disagrees with this file, the live form wins; update this file when it does.

## The submission form

**General section:**

| Field | Rule |
|-------|------|
| Owner | The submitter's account; only they can set it. |
| Skill name | Lowercase, hyphen-separated, matching the folder and frontmatter `name`. Shorter beats longer where equally descriptive; the description does the triggering work, not the name. |
| Description | Required, **1,024 characters maximum**, enforced by the form. No emojis. Must say what the skill does, when to use it, and any host requirements. |
| Jurisdictions | Dropdown, defaults to All. Narrow it when the skill's *resolving* logic is jurisdiction-bound even if its *detecting* or formatting logic is not. |
| Category | Primary practice area or category. Live catalogue slugs observed July 2026 include skill-authoring, legal-operations, legal-education, data-protection; the companion GitHub taxonomy is Domain / Utility / Meta. Pick the live slug that fits; skills about skills go under skill-authoring. |
| Language | Primary language of the resource. |

**Configuration section:**

| Field | Rule |
|-------|------|
| Visibility | Public for catalogue distribution. |
| License | Dropdown, **defaults to AGPL 3.0** — almost every submission needs this changed. Accepted: MIT, Apache-2.0, GPL-3.0, LGPL-3.0, AGPL-3.0, BSD-2/3-Clause, ISC, MPL-2.0, Unlicense, CC0-1.0, CC-BY-4.0, CC-BY-SA-4.0, CC-BY-NC-4.0, CC-BY-NC-ND-4.0, All Rights Reserved, No License, Other. |

**Upload:** a `.skill` or `.zip` archive. Deliver `.zip` — Finder and browsers handle it
predictably, and Safari's "open safe files" setting silently expands `.skill` downloads
into folders, which confuses users.

## Directory and file conventions

```
skill-name/                 ← lowercase-hyphen, equals frontmatter name
├── SKILL.md                ← required
├── LICENSE                 ← full licence text, inside the folder
├── NOTICE                  ← attribution, origin, disclaimers, code disclosure
├── resources/              ← reference files (their convention; not references/)
├── scripts/                ← optional; expect longer security review
└── templates/ or assets/   ← optional; don't rename a folder a script resolves by path
```

The zip must contain the named folder at its root, not loose files.

## Frontmatter

Required: `name` (matches folder), `description` (≤1,024 chars). Strongly expected
`metadata:` block: `author`, `author_link`, `license`, `version` (date form works),
`jurisdiction`, `language`; `derived_from` when the skill adapts someone else's work;
`requires` when the skill needs host capabilities or companion skills.

## Attestations the submitter must make

- The skill has not already been submitted (search first).
- It provides genuine value **with risks disclosed** — this is what the Limitations and
  risks section satisfies.
- All links are functional and public.
- One skill per submission.
- Grounded in actual use, not theoretical; tested on at least one platform.
- Original creators credited where the work was inspired by or derived from theirs.

## Review notes

- All submissions are security-reviewed for data risks and malicious code.
- Skills bundling scripts or "advanced tools" take longer to review. Ship code only when it
  earns its place; keep it standard-library, no network, no subprocess, no dynamic
  evaluation; and disclose exactly that in the NOTICE so the reviewer doesn't have to
  discover it.

## Manual validation checklist

Mirror of `scripts/validate.py`, for hosts that cannot run it:

1. `SKILL.md` exists at the folder root; folder name = frontmatter `name`.
2. Description ≤ 1,024 characters, no emojis.
3. `metadata:` block present with author, license, version.
4. Every `resources/…` (and `scripts/…`, `assets/…`, `templates/…`) path named in SKILL.md
   exists in the package.
5. Every bundled file is referenced from SKILL.md (or from another referenced file) with
   when-to-read guidance — no orphans.
6. No leftover tokens: `references/`, `mcp__` tool names, `CLAUDE_PLUGIN_ROOT`, plugin
   `CLAUDE.md` or `.mcp.json` mentions, old skill names after a rename.
7. `LICENSE` present with full licence text; `NOTICE` present.
8. A "Limitations" (risks) section present in SKILL.md.
9. Any bundled scripts: standard library only, no network, no subprocess, no eval/exec —
   verified by reading them, not assumed.
10. Zip contains the named folder at its root.
