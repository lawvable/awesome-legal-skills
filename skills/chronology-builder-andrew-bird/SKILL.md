---
name: "chronology-builder-andrew-bird"
description: "Builds a litigation chronology from the disclosure bundle itself — every entry attributed to its source document, behind a CPR 31.22 implied-undertaking check, because documents disclosed in English proceedings may only be used for those proceedings. Adds a privilege screen and case-theory significance tagging, so the output is court-facing work product, not a loose timeline. Use when the user asks to build a chronology or timeline from a disclosure bundle, a matter file, or witness statements, or says 'build the chron', 'what happened when', or needs a Statement of Facts ready timeline."
argument-hint: "[slug] [--format=working|sof|witness-[name]]"
metadata:
  author: "Andrew Bird"
  license: "mit"
  version: "2026-06-12"
---

# /chronology

1. Run the CPR 31.22 implied-undertaking check before extracting from disclosed documents.
2. Identify sources: user-provided paths, matter folder, declared sources.
3. Extract dated events, de-duplicate against sources, tag significance per case theory.
4. Output a working chronology by default; Statement-of-Facts or witness-specific variants on request.

---

# Chronology — UK civil litigation

## CPR 31.22 implied-undertaking check

The host workspace enforces the hard gate (matter-slug match against the proceedings reference, privilege posture). If this skill is running, that gate has already passed — this check does not replace it. The skill still performs its own check below and refuses or flags if misuse is indicated; it is not the enforcement.

Before building from any document obtained through standard or extended disclosure in English / Welsh proceedings, confirm the use is permitted:

> CPR 31.22(1): A party to whom a document has been disclosed may use the document only for the purpose of the proceedings in which it is disclosed, except where:
> (a) the document has been read to or by the court, or referred to, at a hearing held in public;
> (b) the court gives permission; or
> (c) the party who disclosed the document and the person to whom the document belongs agree.

Misuse of disclosed documents (using them for a different matter, a different claim, a commercial purpose, or external publication) is a contempt of court.

Confirm before extracting from any source that may have come through disclosure:
- Whether the documents are from disclosure in current proceedings (infer from source path or matter context; surface for confirmation if not evident).
- Whether the chronology is being built for use in those same proceedings (default assumption: yes — same matter slug, same proceedings).

If the answer indicates "different proceedings" or "external use", refuse to build until permission, the parties' agreement, or open-court reference is established — the implied undertaking would otherwise be breached. Flag prominently in the output header: `CPR 31.22 — use restricted to current proceedings unless permitted, agreed, or read in open court.`

Equivalent overlay in disclosure pilot / PD 57AD jurisdictions (Business and Property Courts): the implied undertaking applies; PD 57AD does not displace it.

## Privilege screen

Documents may be subject to legal professional privilege (advice and litigation privilege), common-interest privilege, joint-defence privilege, without-prejudice protection. Extracting privileged content into a chronology that is later shared can risk waiver.

Determine the privilege posture before extracting. Infer from source type (cleared production folder → A; mixed mailbox / dataroom → B; ad-hoc bundle with no review history → B by default; explicit instruction to pause → C). Surface the inferred posture in the output header so counsel can override.

- **A. All sources screened and cleared by counsel.** Extract without flags.
- **B. Mixed or unscreened (default for ambiguous sources).** Extract and tag each entry `priv: ok` / `priv: flag` / `priv: review`. SoF variant filters flagged entries by default.
- **C. Pause and screen first** (use when counsel has explicitly instructed).

## Inputs

- Matter slug, case theory (one sentence — the spine of the case), pivot fact (the single event the case turns on), key facts.
- Sources: disclosure bundle path / cloud folder, supplemental disclosure, witness statements, expert reports, public registers (Companies House, Land Registry), correspondence (open and WP — handle differently).
- Side (claimant / defendant) — drives significance tagging.

## Workflow

### Step 1 — CPR 31.22 implied-undertaking check (above)

### Step 2 — Privilege posture choice (above)

### Step 3 — Source identification

User-provided paths first, then matter folder, then declared sources. Name any source the skill cannot read in the Gaps section — don't silently skip.

### Step 4 — Extraction

For each readable source, identify dated events. One event per document usually. Format: `[date] [actor] [verb] [object/recipient] [content summary]`.

### Step 5 — De-duplication

The same event surfaces in multiple documents (calendar entry, summary email, meeting note). Merge into one entry with multi-source attribution.

### Step 6 — Significance tagging (per side)

- **Claimant (offensive):** 🔴 events establishing elements of the cause (duty, breach, causation, loss, notice), starting limitation in claimant's favour. 🟡 supportive but impeachable. ⚪ background.
- **Defendant (defensive):** 🔴 events breaking causation, establishing limitation, supporting affirmative defence (waiver, estoppel, release, contributory negligence). 🟡 undermining claimant narrative. ⚪ background.

Discipline: 🔴 should be reserved for events that move a factfinder. If everything is 🔴, nothing is.

### Step 7 — Source attribution per entry

Every entry cites its source(s): Bates / disclosure list reference, file path, or witness statement paragraph. Entries derived from web search, model knowledge, or user statement in-session must be tagged `[web search — verify]`, `[model knowledge — verify]`, `[user provided]`.

### Step 8 — Output

Working chronology by default. Variants:

- **Statement of Facts (SoF)**: filtered to 🔴 and select 🟡, prose narrative, with disclosure references. Privilege-flagged entries excluded by default.
- **Witness-specific**: filtered to events where the named witness is sender, recipient, attendee, or subject.

## Output

Produce the chronology with the sections below. Render this as the finished chronology — do not echo this template back, do not leave `[placeholder]` markers or emoji-count scaffolding in the output, and do not invent events to fill rows. Attribute every entry to its source document; if a section has nothing in it, say so.

This is a draft for solicitor review, not legal advice. The chronology and its significance tags are a first pass; counsel decides what goes into a pleading or before the court.

The sections:

- A reviewer-note line: *work product, prepared in contemplation of litigation, subject to litigation privilege.*
- A CPR 31.22 notice naming the proceedings the sources were disclosed in.
- A header: matter slug, build date, case theory, pivot fact, side framing, privilege posture, source count, and entry count by tag.
- The timeline table — one row per de-duplicated event, with date, event, significance tag, privilege flag, and sources.
- Key events (🔴) — the events that move a factfinder, each with what happened, the tie to the case theory, and sources.
- Gaps — date ranges with no events, expected-but-missing events, unreadable sources.

Worked shape for the sections (do not copy the placeholder text — fill from real sources):

[Reviewer note: work product, prepared in contemplation of litigation, subject to litigation privilege.]

> **CPR 31.22 notice.** Sources include documents disclosed in [proceedings]. Use restricted to those proceedings per CPR 31.22 unless permitted, agreed, or already read in open court.

# Chronology — [Matter name]

- **Matter:** [slug]
- **Built:** [YYYY-MM-DD]
- **Case theory:** [one sentence]
- **Pivot fact:** [one sentence]
- **Side framing:** [claimant / defendant]
- **Privilege posture:** A-cleared / B-mixed / C-aborted
- **Sources:** [N] documents across [bundle / supplemental / witness / expert]
- **Entries:** [N] ([N] 🔴 / [N] 🟡 / [N] ⚪)

## Timeline

| Date | Event | Tag | 🔒 | Sources |
|---|---|---|---|---|
| [YYYY-MM-DD] | [actor + verb + object + content] | 🔴/🟡/⚪ | / 🔒-flag / 🔒-review | [D1/123, WS-Smith para 14] |

## Key events (🔴)

### [date] — [event title]
- What: [...]
- Theory tie: [why this matters to the case theory]
- Sources: [...]

## Gaps

- Date ranges with no events: [...]
- Expected but missing: [...]
- Unreadable sources: [...]

## Marker discipline

- `[VERIFY — factual assertion not yet checked against the source doc]`
- `[UNCERTAIN — legal characterisation]`
- `[CITE NEEDED — disclosure reference]`
- `[SME VERIFY — privilege status / borderline significance]`

## Version

- v[N] built on [date] from [source summary]
- v[N-1] superseded

## Incremental builds

If a prior `chronology.md` exists: read, build new from current sources, diff (new / modified / removed), bump version. Preserve provenance and tags.

## What this skill does not do

- Resolve contradictions between sources. Both go in with flags.
- Fill gaps from web search or model knowledge silently. The user is asked first.
- Decide privilege status. The posture is selected; per-entry flags are first-pass; counsel decides distribution.
- Cover Scottish / NI proceedings.
