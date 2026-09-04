# The Standard Transforms
<!-- token-scan: exempt — this file documents the forbidden tokens -->

Each transform names the failure it prevents. Apply every one that fits; skip the ones
that don't. Substantive transforms (1–4) change what the skill does when things are
missing; mechanical transforms (5–9) change how it is packaged.

## 1. De-plugin: fold in stranded logic

**Failure prevented:** a skill that was half of a plugin ships without the plugin-level
instructions it silently depended on — mode-selection rules, verification stages, workflow
glue living in a plugin `CLAUDE.md` — and misbehaves standalone.

Read any plugin-level files that travelled with the input. Anything the skill *needs* moves
into SKILL.md or a resource file. Anything referencing a companion skill is either kept as
an honest optional pointer ("pairs with X, which renders this output") or cut cleanly —
never left dangling as a hard dependency on something the installer doesn't have.

## 2. Ladder the dependencies

**Failure prevented:** the skill assumes a connector, tool, or capability the installer
lacks, and either errors or silently degrades.

For research-type dependencies, write the four-rung ladder, decided once per run:
1. The user's named source wins. If it's unavailable, say so and ask — never substitute
   silently.
2. Otherwise use what is connected (name several candidate tools as examples, not an
   exhaustive list that rots).
3. Otherwise ordinary web search.
4. Otherwise proceed without, and *say so in the output* (a one-line sources note).

For capability-type dependencies (code execution, filesystem, companion skills, compilers):
check capabilities **before** promising outputs, offer only what will complete, and provide
a no-dependency fallback where one is feasible (a single self-contained file beats a
directory tree; source beats compiled output). Never let a user spend setup effort and hit
the wall at the end. And never promise the compiled artifact when only the source is
guaranteed — "produces LaTeX source" is honest; "produces a PDF" is a bet on the user's
machine.

## 3. Host-neutralize

**Failure prevented:** the skill instructs the model to call a tool by a host-specific name
(`mcp__<host>__present_files` and kin) that doesn't exist elsewhere.

Replace with intent-level instructions: "deliver the file by whatever mechanism the host
provides; if none exists, state the output path." Grep the whole package for `mcp__`,
`CLAUDE_PLUGIN_ROOT`, and host product names used as load-bearing instructions.

## 4. Honesty sections

**Failure prevented:** the submission attestation requires risks disclosed; and users
trust a catalogue skill they cannot inspect the history of.

Add or verify three things:
- **Limitations and risks** — skill-specific, not boilerplate. Name the real failure modes:
  what the skill can't see, what goes stale, what depends on the host, what its outputs
  must not be mistaken for. Include the not-legal-advice line for anything a lawyer might
  rely on. End with the code disclosure ("contains no executable code…" or an exact
  description of what the code does and doesn't do).
- **Jurisdiction honesty** — where mechanics transfer but doctrine doesn't, say which is
  which, in the body, so the field on the form and the text agree.
- **Preserve the source's own caveats.** Any transform that rewrites content wants to cut
  qualifications; check they survived.

## 5. Structure

**Failure prevented:** the package doesn't match the catalogue's conventions, or files the
skill needs sit outside the folder and don't travel.

Folder name = frontmatter `name`, lowercase-hyphen. `references/` → `resources/`, with
**every pointer rewritten** — grep afterward for the old path; a rename that misses a
pointer is worse than no rename. Exception: never rename a directory a bundled script
resolves by path (check the scripts first); note the constraint in the resources list
instead. LICENSE (full text) and NOTICE go *inside* the folder.

## 6. Frontmatter and description

**Failure prevented:** the form rejects the description at 1,024 characters; or it triggers
badly; or it promises what the skill no longer does.

Description ≤1,024 characters, counted, no emojis. Pushy triggers in the register users
actually type (match the audience's spelling — an American user types "analyze"). One
sentence of host requirements where they exist. Add the `metadata:` block: author,
author_link, license, version, jurisdiction, language; `derived_from` for adaptations;
`requires` for capabilities. **After every substantive transform, re-read the description
against the body** — formats added, dependencies laddered, names changed all invalidate it.

## 7. Orphans and links

**Failure prevented:** bundled files nothing points to (dead weight that will drift from
the inline content it duplicates), and pointers to files that don't exist.

Every bundled file gets referenced from SKILL.md with when-to-read guidance ("read before
producing X"); a Bundled resources section is the natural home. Every referenced path must
exist. Where content is duplicated between SKILL.md and a resource file, keep one copy and
point to it.

## 8. Attribution and licence files

**Failure prevented:** publishing someone else's work as one's own, or one's own work under
a scaffolding stamp.

Per the provenance decision (Step 2 of the pipeline): LICENSE carries the full text of the
chosen licence. NOTICE carries copyright, origin (original work, derivative-of-whom, or
formerly-part-of-what, including former names after a rename), the itemized
upstream-vs-added split for derivatives, a no-endorsement line, the code disclosure, and
the disclaimer. Cross-references elsewhere: a renamed skill's old name should appear in
NOTICE so people who knew it can connect the two, and any paired skill's description that
names this one must be updated to match.

## 9. Code hygiene

**Failure prevented:** a slow or failed security review, or a script that breaks when the
package is rearranged.

Standard library only where possible; no network, no subprocess, no eval/exec; writes
confined to caller-named output directories. State all of that in NOTICE. Smoke-test each
script after any reorganization (`--help` at minimum) and verify relative asset paths still
resolve. If code doesn't earn its place, remove it — a skill without scripts reviews
faster and breaks less.

## The change report

Deliver with every package: substantive adaptations first (what was folded in, laddered,
added, or removed, and why), mechanical fixes second, and any open items the user must
decide (licence choice, duplicate finding, unverifiable provenance). The user should never
discover a change by diffing.
