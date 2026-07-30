---
name: case-briefer
description: >-
  Produces detailed law-school case briefs of United States judicial opinions in a fixed
  nine-section structure: memory jogger, facts, procedural history, judicial votes, holding,
  opinion-by-opinion analysis, five future-application hypotheticals, critique, and verified
  key quotations. Also builds vote tables, cross-case consistency tables, perspective-based
  critiques, and LaTeX in article, Beamer and casebook-chapter formats. Use whenever someone
  asks to brief a case, analyse or explain an opinion, summarise a decision for students,
  generate hypotheticals from a holding, critique a judgment, tabulate how justices voted, or
  convert case analysis to LaTeX. Triggers on "brief this case", "case brief", "explain the
  holding", "what did the court hold", "hypotheticals based on", "critique this opinion",
  "vote table", "Beamer presentation", "chapter brief", and on any reference to a judicial
  opinion or Supreme Court decision in a teaching context. Requires web search to verify
  quotations, votes and holdings.
metadata:
  author: "Seth J. Chandler"
  author_link: "https://legaled.ai"
  license: "Apache-2.0"
  version: "2026-07-29"
  jurisdiction: "United States"
  language: "English"
  requires: "Web search"
---

# Case Briefer

Deliver detailed case briefs with comprehensive analysis, examples, and critique for law
students and professors.

## Core Case Brief Structure

Every case brief includes these 9 sections:

### 1. Memory Jogger

One sentence capturing the case's essence — its facts, central holding, or most salient
feature.

- Example for *Carolene Products*: "Footnote 4 establishes justification for tiers of
  scrutiny."

### 2. Detailed Case Facts

Include:

- Key facts giving rise to the dispute
- Relevant statutes, regulations, or constitutional provisions
- Explain the statutory scheme and specific provisions challenged
- Historical or political context when relevant

### 3. Procedural History

Focus on procedural aspects relevant to disposition:

- Lower court rulings and reasoning
- Basis for appeal
- Note distinctions like "the court did not rule plaintiffs prevailed, merely that they pled
  enough to survive a motion to dismiss"

### 4. Judicial Votes

Group by:

- **Majority**: Author and joining justices/judges
- **Concurrence(s)**: Author(s) and any joining justices/judges
- **Dissent(s)**: Author(s) and any joining justices/judges

### 5. Holding

Succinct statement of the court's judgment and the rule announced.

### 6. Analysis of Opinions

For each opinion (majority, concurrences, dissents):

- Reasoning employed
- Key constitutional, statutory, regulatory, or treaty provisions cited
- Key precedents and how they were applied to this case's facts
- Logical structure of the argument

### 7. Examples: Future Applications

Create 5 hypotheticals showing how the rule applies:

- **2 same-side**: Cases that would come out the same way as the principal case
- **2 opposite-side**: Cases that would come out the opposite way
- **1 fence-sitter**: Genuinely unclear outcome

For each, explain *why* it falls where it does under the rule.

### 8. Critique

- Recapitulate scholarly criticism of the opinion(s)
- Develop independent analysis of logical weaknesses
- Identify values or premises that would lead to different conclusions
- Consider both progressive and originalist/textualist perspectives when relevant

### 9. Key Quotations

Present 3–5 important quotes from the opinions, subject to the verification rule below.

## Verification

Quotations, vote counts, and holdings are the three places this skill can do real damage if
it is wrong, because each is the kind of claim a reader will repeat without checking.

- Verify every quotation against the text of the opinion by web search before including it.
- Verify vote line-ups and the identity of opinion authors the same way.
- Where a quotation cannot be verified, either omit it or mark it explicitly as unverified.
  Never present an unverified quotation as though it had been checked.
- Where web search is unavailable, say so at the top of the brief and treat every quotation,
  vote count, and citation in it as unverified.

Distinguish holdings from dicta. Note circuit splits, later overruling, and subsequent
statutory or doctrinal developments where relevant.

## Tone and Quality Standards

- Professional and objective throughout
- Audience: law students and law professors
- For controversial cases, present multiple scholarly perspectives fairly
- If a response is too long for a single output, continue across multiple messages

## Additional Capabilities

### General Discussion

Engage in dialogue about cases as in normal conversation.

### Quotation Requests

When asked for specific quotations, apply the verification rule above.

### Vote Tables

Create tables showing how each justice or judge voted in a case.

### Consistency Tables

Compare voting patterns across multiple cases — showing which justices voted which way in
each case.

### Perspective-Based Critiques

Offer critiques from specified perspectives:

- "Criticize *Seila Law* from a progressive perspective"
- "Criticize *Chevron* from a historical perspective"

## LaTeX Conversion

Three output formats are supported. The preambles, slide-structure examples, and chapter
skeleton live in `resources/latex-preambles.md` — read that file when producing LaTeX rather
than reconstructing the preambles from memory.

### Article format

A standalone brief. Use the article preamble from the resource file.

### Beamer presentation format

A slide deck. Use the Beamer preamble from the resource file, and observe the slide limits:
roughly 5 main items per slide, at most 2 subitems each, and no more than 9 items and
subitems in total.

### Chapter brief format (for casebooks)

**Input pattern**: `Brief [Case Name]. Emphasize [Specific Concept or Historical Context]`

**Output**: a modular LaTeX chapter file for `\input{filename}` in a larger book project.

**Do NOT include** a document class, package imports, or any preamble — the parent document
supplies them. Begin at `\chapter{}` and follow the section skeleton in the resource file,
which mirrors the nine-section structure above.

## Workflow

1. **Receive case request** → identify the case and any emphasis requested
2. **Research** → use web search to gather accurate information about the case
3. **Draft brief** → follow the 9-section structure
4. **Verify** → check holdings, quotations, and vote counts against sources
5. **Deliver** → present in the requested format (standard, LaTeX article, Beamer, or chapter)

## Bundled resources

- `resources/latex-preambles.md` — article and Beamer preambles, Beamer slide guidelines and
  a worked slide example, and the no-preamble chapter skeleton. Read when producing any
  LaTeX output.

## Limitations and risks

This skill produces teaching and study materials about United States judicial opinions. It is
not legal advice and does not produce authority. A brief generated here is a study aid: it
must not be cited, filed, or relied upon in practice in place of reading the opinion.

Three risks are worth naming. First, quotation and vote-count accuracy depends on web search
being available and on the opinion text being reachable; without it the model may reconstruct
plausible but incorrect language, which is why the verification rule requires unverified
material to be marked or omitted. Second, briefs reflect the state of the law at the time of
generation and will not know of later overruling, vacatur, or amendment unless the search
surfaces it. Third, the critique and perspective sections are argumentative by design — they
present the strongest form of a position, including positions the user did not ask about, and
should not be read as a neutral account of scholarly consensus.

The skill contains no executable code, makes no network calls of its own beyond the host's
web search, and moves no data outside the session.
