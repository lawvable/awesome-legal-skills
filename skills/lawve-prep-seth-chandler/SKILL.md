---
name: lawve-prep
description: >-
  Takes a skill — a .skill or .zip archive, a bare SKILL.md, a folder, or just a raw idea —
  and produces a package ready for public distribution on lawve.ai, plus the exact entries
  for the submission form. Runs a gate first: skills with no plausible legal use, unsafe
  code, or licensing bars are declined with reasons, and general-purpose skills that could
  serve legal work are offered a legal adaptation instead. Then applies the standard
  compliance transforms — structure, metadata, attribution, dependency ladders,
  orphaned-file repair, limitations disclosure — validates the result, and delivers a zip.
  Raw ideas are gated first, built (via skill-creator where available), then adapted. Use
  for "make this Lawve-compliant," "prep this skill for Lawve," "package for lawve.ai,"
  "is this suitable for Lawve," "get my skill ready to publish," or any request to ready
  a skill for the Lawve catalogue.
metadata:
  author: "Seth J. Chandler"
  author_link: "https://legaled.ai"
  license: "Apache-2.0"
  version: "2026-07-30"
  jurisdiction: "All"
  language: "English"
  category: "skill-authoring"
---

<!-- token-scan: exempt — the intake step names plugin config files -->

# Lawve-Prep: Package a Skill for Public Distribution on Lawve

Turn a skill in any state — packaged, half-packaged, a bare SKILL.md, or an idea in a
sentence — into something that can stand in a public legal catalogue: correctly structured,
honestly described, properly attributed, safe to review, and accompanied by the exact form
entries the submission page asks for.

The pipeline has six steps. The order is deliberate: the gate comes first because no
packaging effort should be spent on a skill that will be declined, and provenance comes
second because the licence decision shapes everything downstream.

**Intake → Gate → Provenance → Transform → Validate → Package.**

## Step 0 — Intake

Identify what the user handed over:

- **A `.skill` or `.zip` archive** — unzip it. Both are zip files.
- **A folder or bare `SKILL.md`** — work from it directly. A bare SKILL.md becomes a folder
  named after its frontmatter `name`.
- **A plugin** — a bundle with `.claude-plugin/`, a plugin-level `CLAUDE.md`, or `.mcp.json`
  contains more than one thing. Lawve takes one skill per submission. Split it: each skill
  becomes its own package, plugin-level instructions get folded into the skill that needs
  them (see transforms), and cross-references between the halves are updated or cut cleanly.
- **A raw idea** — gate the *idea* first (Step 1); do not build a skill you would then
  decline. If it passes, build it with the `skill-creator` skill where available, otherwise
  draft a SKILL.md directly following Anthropic's skill-authoring practices (frontmatter
  name + pushy description; body instructions; bundled resources only where they earn their
  place). Then continue through the pipeline like any other input.

Read the whole skill before judging it — SKILL.md and every bundled file. Half the problems
live in the bundled files.

## Step 1 — Gate

Read `resources/gate.md` and apply it. Three outcomes:

- **Proceed** — the skill serves legal work in some form. The bar is broad: practice,
  litigation, drafting, legal education, legal research, law-office operations, document
  production for legal audiences, and meta-skills for legal AI all qualify.
- **Offer a legal adaptation** — the skill is general-purpose but a legal layer would earn
  its place in the catalogue (a text-to-audio skill gains citation and quotation handling; a
  formatting skill gains brief-and-memo structures). Propose the superset — everything it
  does now, plus the legal layer — and get the user's yes before building it.
- **Decline** — no plausible legal use even with adaptation, or a safety, licensing, or
  professional-responsibility bar that adaptation cannot cure. Decline in plain terms: what
  the bar is, and what (if anything) would change the answer. Never quietly package
  something the gate should have stopped.

## Step 2 — Provenance and licence

Establish whose work this is before touching the files.

- **The user's original work** → the user picks the licence; default Apache-2.0 (MIT also
  fine). Both are on Lawve's accepted list.
- **A derivative of someone else's skill** → match the upstream licence where it permits
  derivatives (Apache-2.0, MIT, BSD, and CC-BY all do). Get attribution right in three places:
  frontmatter (`derived_from`), an attribution section in the SKILL.md body, and the NOTICE
  file, which itemizes what is upstream and what is added and disclaims endorsement.
- **Upstream licence forbids or is absent** — "All Rights Reserved," "No License," or a
  proprietary notice → stop. The skill cannot be published without permission. Say so.
- **A placeholder copyright line** — "Contributors," a scaffolding default, a company name
  that doesn't fit — is a question, not an answer. Ask the user who wrote it rather than
  assuming either way. Scaffolding tools routinely stamp wrong attributions on original
  work, and original authors routinely forget to replace them.

## Step 3 — Transform

Read `resources/transforms.md` and apply every transform that fits. In brief: fix the
structure (folder name, `resources/` directory, LICENSE and NOTICE inside the folder);
rewrite the frontmatter (description under 1,024 characters with honest triggers and a
host-requirements sentence where needed); fold in any plugin-level logic the skill depends
on; replace host-specific tool names with host-neutral instructions; convert hard external
dependencies into a graceful ladder; repair orphaned files and broken links; add the
limitations, jurisdiction-honesty, and bundled-resources sections; and clean up code.

The one meta-rule: **the description on the form and the description in the frontmatter must
tell the same truth as the skill's body.** Every time a transform changes what the skill
does — a new format, a renamed dependency, an added fallback — check whether the description
still describes it.

## Step 4 — Validate

Where the host can run Python, run the bundled validator:

```bash
python scripts/validate.py <skill-folder>
```

It checks structure, frontmatter, description length, link resolution, orphaned files,
leftover host-specific tokens, and the presence of LICENSE, NOTICE, and a limitations
section. Fix everything it reports and run it again; a package ships only on a clean pass.

Where the host cannot run Python, perform the same checks by hand — the checklist at the end
of `resources/requirements.md` mirrors the script exactly.

Two checks the script cannot do, so do them yourself every time:

1. **Read the final SKILL.md top to bottom as a stranger.** Does it run correctly with
   nothing but what is inside the folder? Anything it assumes — a connector, a companion
   skill, a plugin file, a directory layout — must be either bundled, laddered, or disclosed.
2. **Check the catalogue for duplicates.** Use the Lawve connector's search where connected;
   otherwise web-search the lawve.ai catalogue; otherwise say plainly that the duplicate
   check could not be run. A near-duplicate is not automatically fatal — but the user decides
   that with the information, not without it.

## Step 5 — Package and deliver

- Zip the folder so the archive contains the named directory at its root:
  `zip -r <name>.zip <name>/`. Deliver as `.zip` — browsers and Finder handle it
  predictably, and Lawve accepts it.
- Produce the **form entries block**: skill name; description (exact text, with character
  count); jurisdictions; category recommendation with one line of reasoning; language;
  visibility; licence. Flag explicitly which fields differ from the form's defaults — as of
  this writing the licence default is AGPL 3.0 and jurisdictions default to All, so most
  submissions need the licence changed and some need jurisdictions narrowed.
- Report what changed, briefly: the substantive adaptations first (what was folded in,
  laddered, or added), the mechanical fixes second. The user should be able to see at a
  glance what is different about the published version and why.

## Bundled resources

- `resources/requirements.md` — the codified Lawve submission requirements: form fields and
  limits, directory conventions, attestations, review notes, and the manual validation
  checklist. Read at the start of any packaging run.
- `resources/gate.md` — the accept / adapt / decline criteria: the law-relatedness test,
  safety and code screens, professional-responsibility flags, licensing bars, duplicates,
  and the quality floor. Read in Step 1.
- `resources/transforms.md` — the standard compliance transforms with the failure each one
  prevents. Read in Step 3.
- `scripts/validate.py` — the programmatic validator. Python 3, standard library only.
  Run in Step 4 where the host allows.

## Limitations and risks

This skill packages other skills for public distribution. It is not legal advice, and its
gate is an editorial judgment, not a legal clearance.

**The requirements are a snapshot.** Lawve's form fields, limits, licence list, and review
criteria are recorded in `resources/requirements.md` as of the version date and will drift.
Where the live form disagrees with the reference file, the live form wins — and the
reference file should be updated.

**The licence step depends on honest provenance.** The skill asks who wrote the input and
takes the answer it is given. It cannot detect misattributed authorship, and a package built
on a wrong answer misattributes in three places at once.

**The gate can be wrong in both directions.** A declined skill may have a legal use the gate
did not see; an accepted one may have a problem review catches later. Lawve's own review is
the real backstop; the gate exists so the user doesn't spend effort on obvious rejections.

**Packaging improves presentation, not substance.** A weak skill emerges from this pipeline
structured, attributed, and disclosed — and still weak. The quality floor in the gate is a
floor, not an endorsement.

**The duplicate check degrades.** With no catalogue access and no web search, it does not
run, and the skill says so rather than pretending it did.

The bundled validator uses only the Python standard library, makes no network calls, spawns
no subprocesses, and writes nothing — it only reads the folder it is pointed at.
