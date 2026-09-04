---
name: law-review-editor
description: >-
  Rigorous multi-pass editor for law review articles, student notes, seminar papers and
  other legal scholarship. Runs six specialized passes — structure, substantive critique,
  Bluebook citations, grammar and clarity, fact-checking against sources, and a synthesizing
  memo — and delivers an editorial memo with issues prioritized as critical, substantial or
  minor and keyed to specific footnotes and paragraphs. Handles articles of any length,
  including 50,000-word pieces, by chunking on section boundaries. Reads .docx directly.
  Use when editing, critiquing, workshopping or pre-submission-reviewing academic legal
  writing. Triggers on "edit my article," "review this draft," "critique my note," "check my
  Bluebook citations," "is my argument sound," "read my law review piece," "workshop this
  paper," "pre-submission review." Chunking needs Python 3; fact-checking needs web search;
  both degrade gracefully without.
metadata:
  author: "Seth J. Chandler"
  author_link: "https://legaled.ai"
  license: "Apache-2.0"
  version: "2026-07-31"
  jurisdiction: "United States"
  language: "English"
  requires: "Python 3 (standard library only) for chunking long articles; web search for the fact-check pass"
---

# Law Review Article Editor

A systematic, multi-pass editing workflow for scholarly legal articles. This skill enables rigorous editing of law review articles through specialized review passes, intelligent chunking for long documents, and comprehensive critique covering all aspects from argumentation to Bluebook citations.

## Overview

Law review articles require specialized editing that goes beyond grammar and style. They demand:
- **Rigorous substantive critique** of legal arguments and claims
- **Bluebook citation accuracy** following technical rules
- **Structural coherence** appropriate to legal scholarship
- **Research completeness** with no major gaps
- **Logical rigor** in argumentation
- **Fact-checking** to prevent errors and hallucinations

This skill provides a structured approach to editing that addresses all these dimensions through multiple specialized passes.

## Core Workflow

### Phase 1: Initial Assessment and Preparation

**Step 1: Analyze Article Metadata**
- Count total words (use `wc -w` or similar)
- Identify article structure (sections, subsections, footnotes)
- Assess article type (doctrinal, theoretical, empirical, historical, comparative, interdisciplinary)
- Note any special features (data tables, appendices, etc.)

**Step 2: Determine Chunking Strategy**

For articles under 10,000 words:
- Process as single unit (no chunking needed)
- Can hold entire article in context for each pass

For articles 10,000-25,000 words:
- Use natural section breaks for chunks
- Aim for chunks of 5,000-8,000 words
- Keep related sections together

For articles over 25,000 words:
- Use `scripts/chunk_article.py` to intelligently chunk by sections
- Default to 8,000-word chunks (adjust based on context window availability)
- The script will create separate chunk files and provide a map

**Chunking command**:
```bash
python scripts/chunk_article.py article.docx 8000
```

This creates files like `article_chunk_1.txt`, `article_chunk_2.txt`, etc., plus a summary showing which sections are in which chunks.

### Phase 2: Multi-Pass Editing

Execute the following passes sequentially. For chunked articles, complete each pass for all chunks before moving to the next pass.

#### Pass 1: Structural Analysis

**Purpose**: Evaluate overall organization and argument structure

**Reference to read**: `resources/article_structure.md`

**Focus areas**:
- Title and abstract effectiveness
- Introduction quality (problem framing, thesis clarity, roadmap)
- Part organization and logical flow
- Section and subsection structure
- Paragraph organization and topic sentences
- Transitions and signposting
- Conclusion effectiveness
- Footnote organization

**Deliverable**: Structural critique memo identifying:
- Organizational strengths and weaknesses
- Parts that should be reorganized, split, or combined
- Missing sections or underdeveloped areas
- Transitions that need improvement
- Heading and outline structure issues

#### Pass 2: Substantive Critique

**Purpose**: Evaluate arguments, claims, research quality, and scholarly contribution

**Reference to read**: `resources/substantive_critique.md`

**Focus areas**:
- Thesis clarity and originality
- Logical reasoning and argumentation quality
- Research completeness and gap identification
- Legal analysis rigor (doctrinal accuracy, case distinctions, precedential weight)
- Empirical claims and data (if applicable)
- Normative arguments and theoretical grounding
- Originality and contribution to scholarship
- Counterargument engagement

**Deliverable**: Substantive critique memo identifying:
- Logical fallacies or weak arguments
- Research gaps (missing cases, statutes, scholarship)
- Overclaims or unsupported assertions
- Areas needing additional authority or evidence
- Counterarguments that should be addressed
- Suggestions for strengthening arguments

#### Pass 3: Bluebook Citation Review

**Purpose**: Ensure all legal citations conform to Bluebook format

**Reference to read**: `resources/bluebook_guide.md`

**Focus areas**:
- Case citation format (names, reporters, courts, years, pinpoints)
- Statutory citation format
- Law review and book citation format
- Signal usage (*see*, *cf.*, etc.)
- Short form usage (*id.*, *supra*)
- Citation order within footnotes
- Pinpoint citations (ensuring specific page references)
- Typeface (italics vs. roman)
- Spacing and punctuation

**Method for chunked articles**:
- Review all footnotes in each chunk
- Track repeated citations across chunks to ensure consistent short form usage
- Note *supra* references that may need updating if article is restructured

**Deliverable**: Bluebook compliance memo with:
- List of citation errors by footnote number
- Pattern issues (e.g., consistent failure to pinpoint cite)
- Recommendations for fixing systematic problems

#### Pass 4: Grammar, Style, and Clarity

**Purpose**: Polish prose for clarity, concision, and correctness

**Focus areas**:
- Grammar and punctuation errors
- Sentence structure and clarity
- Word choice and precision
- Passive voice overuse
- Legalese and jargon
- Redundancy and wordiness
- Paragraph length and flow
- Consistency in terminology
- Readability and accessibility

**Techniques**:
- Flag unclear or convoluted sentences
- Identify opportunities to simplify without losing precision
- Note inconsistent terminology (switching between terms for same concept)
- Mark instances where examples would aid clarity

**Deliverable**: Style and clarity memo with:
- Specific sentences/passages needing revision
- Pattern issues (e.g., chronic passive voice)
- Suggestions for improving readability

#### Pass 5: Fact-Checking and Research Verification

**Purpose**: Verify factual claims and identify potential hallucinations or errors

**Focus areas**:
- Factual claims about cases (holdings, reasoning, outcomes)
- Statutory provisions (current text, amendments, codification)
- Empirical claims (statistics, studies, data)
- Historical claims
- Claims about other scholarship (fair characterization?)
- Quotations (accuracy and context)
- Current events or recent developments

**Methods**:
- Use whatever web search the host provides to verify factual claims that seem questionable. Where no search is available, mark the claim "unverified" rather than assuming it is sound
- Check that cases cited actually support the propositions claimed
- Verify that statutes haven't been amended since article drafted
- Cross-reference empirical claims against original sources

**Deliverable**: Fact-check memo with:
- Factual errors identified
- Claims needing verification or additional sourcing
- Potential hallucinations or mischaracterizations
- Out-of-date information needing updates

#### Pass 6: Final Polish and Integration

**Purpose**: Synthesize all passes and create comprehensive edit memo

**Focus areas**:
- Prioritize identified issues (critical vs. minor)
- Look for issues missed in specialized passes
- Ensure consistency across all chunks
- Final read-through for overall coherence

**Deliverable**: Comprehensive editorial memo covering all passes

### Phase 3: Revision Production (Optional)

If requested, produce a revised version of the article incorporating suggested edits:

**Options**:
1. **Comprehensive edit memo only** (default) - Provides detailed critique for author to implement
2. **Track-changes version** - Create Word document with suggested edits using tracked changes
3. **Clean revised version** - Implement all changes and provide revised article

**For track-changes version**:
- Use `python-docx` to create the Word document with change tracking. This is the one path requiring a third-party package; where it is unavailable, deliver the memo instead and say why
- Mark all substantive changes
- Add comments for judgment calls or alternatives
- Preserve original footnote numbering

## Handling Special Article Types

### Empirical Articles
- **Extra attention to**: Methodology, data analysis, statistical claims
- **Additional pass**: Review research design and methodology section separately
- **Verify**: Reproducibility of results, proper statistical tests

### Theoretical Articles
- **Extra attention to**: Coherence of theoretical framework, engagement with competing theories
- **Check**: Whether theory is applied concretely to legal problems
- **Verify**: Accurate representation of other theorists' views

### Historical Articles
- **Extra attention to**: Source adequacy (primary vs. secondary), contextualization
- **Check**: Avoiding presentism (judging past by current standards)
- **Verify**: Accuracy of historical claims using web search

### Comparative Articles
- **Extra attention to**: Accurate understanding of compared legal systems
- **Check**: Fair comparison (not cherry-picking)
- **Verify**: Claims about foreign law using web search

### Interdisciplinary Articles
- **Extra attention to**: Competence in both disciplines, accurate representation of non-legal field
- **Check**: Genuine integration vs. superficial citation
- **Verify**: Non-legal claims using web search

## Working with Chunks

### Maintaining Context Across Chunks

When editing a chunked article:
1. **Track cross-references**: Note when one chunk references another
2. **Maintain terminology list**: Track key terms and their definitions across chunks
3. **Note structural issues**: Some problems only apparent when viewing multiple chunks together
4. **Coordinate citation review**: Ensure *supra* references point to correct footnote numbers across chunks
5. **Synthesize at end**: After reviewing all chunks, assess article as a whole

### Chunk Transition Points

Pay special attention to transitions between chunks:
- Does argument flow smoothly across chunk boundary?
- Are there orphaned references (referring to "Part II" when Part II is in different chunk)?
- Do citations at chunk boundaries maintain proper short form usage?

## Common Patterns

### Pattern 1: Quick Review (10,000-word article)

For a standard-length article needing general polish:
1. Single structural pass (1 hour)
2. Single substantive pass (2 hours)
3. Bluebook review (1 hour)
4. Grammar/style pass (1 hour)
5. Comprehensive memo (30 min)
**Total**: roughly 5-6 hours of a human editor's time; correspondingly fewer passes to supervise when run here

### Pattern 2: Major Revision (30,000-word article)

For a long article needing substantial work:
1. Chunk article into 4-5 pieces
2. Complete all 6 passes across all chunks (10-15 hours)
3. Synthesize findings across chunks (2 hours)
4. Produce detailed revision memo (2 hours)
5. Optional: Create track-changes version (3-4 hours)
**Total**: roughly 15-20 hours of a human editor's time; expect to review the output in stages rather than all at once

### Pattern 3: Targeted Review

If author requests review of specific aspects only:
1. Identify which passes are needed
2. Execute only those passes
3. Provide targeted memo

**Example**: "Just review my citations and check for logical gaps"
→ Execute Pass 3 (Bluebook) and relevant parts of Pass 2 (logic/argumentation)

## Quality Standards

### Critical Issues (Must Fix)
- Fundamental misstatements of law
- Major logical fallacies or invalid arguments
- Missing major relevant authority
- Serious Bluebook errors (wrong reporter, wrong year, missing pinpoints)
- Factual errors or hallucinations

### Substantial Issues (Should Fix)
- Organizational problems undermining clarity
- Weak arguments needing strengthening
- Research gaps in important areas
- Systematic citation errors
- Unclear thesis or contribution

### Minor Issues (Nice to Fix)
- Minor citation formatting inconsistencies
- Wordiness or stylistic infelicities
- Small organizational improvements
- Missing citations for completeness

## Best Practices

### Do:
- **Read references first**: Always load relevant reference files before starting each pass
- **Be specific**: Cite particular footnotes, paragraphs, or passages
- **Prioritize**: Distinguish critical issues from minor polish
- **Explain reasoning**: Don't just say "this is wrong" - explain why and how to fix
- **Respect author's voice**: Improve clarity without imposing different style
- **Track issues systematically**: Use consistent format for noting problems
- **Synthesize at end**: Pull together findings from all passes into coherent memo

### Don't:
- Skip the structure review - organization problems undermine everything else
- Assume claims are accurate without verification for critical facts
- Over-edit style at expense of substance
- Make changes that alter author's argument without noting it
- Ignore systematic problems in favor of one-off fixes
- Forget to check across chunks for consistency in long articles

## Deliverable Format

### Comprehensive Editorial Memo Structure

```markdown
# Editorial Review: [Article Title]

**Author**: [Author Name]
**Review Date**: [Date]
**Article Length**: [Word count]
**Reviewer**: Claude (Law Review Editor)

## Executive Summary
[2-3 paragraphs summarizing overall assessment and highest-priority issues]

## I. Structural Assessment
[Findings from Pass 1]

### Strengths
- [List organizational strengths]

### Issues Requiring Attention
#### Critical
- [Major structural problems]

#### Substantial  
- [Important organizational improvements]

#### Minor
- [Small structural refinements]

## II. Substantive Critique
[Findings from Pass 2]

### Argument Quality
[Assessment of thesis, logic, reasoning]

### Research Completeness
[Assessment of authority coverage, gaps identified]

### Specific Concerns
[Detailed substantive issues by section]

## III. Citation Review (Bluebook)
[Findings from Pass 3]

### Systematic Issues
[Pattern problems affecting many citations]

### Specific Citation Errors
[By footnote number]

## IV. Grammar, Style & Clarity
[Findings from Pass 4]

### Pattern Issues
[Recurring style problems]

### Specific Passages Needing Revision
[By paragraph or page]

## V. Fact-Check Results
[Findings from Pass 5]

### Verified Claims
[Important claims that were verified]

### Issues Requiring Correction
[Errors or unverified claims]

### Recommendations for Additional Research
[Areas where more authority would strengthen argument]

## VI. Summary of Recommendations

### Priority 1 (Critical)
[Must-fix issues]

### Priority 2 (Important)
[Should-fix issues]

### Priority 3 (Polish)
[Nice-to-have improvements]

## VII. Overall Assessment

[Final thoughts on article's contribution, strengths, and revision needs]
```

## Troubleshooting

**Issue**: Article structure not recognized by chunking script
- **Solution**: Manually identify natural breakpoints and chunk by word count ranges
- Use section headers as guides even if not perfectly formatted

**Issue**: Can't verify factual claim
- **Solution**: Flag claim as "unverified" and recommend author double-check original source
- Don't assume it's wrong, but note the need for verification

**Issue**: Citations seem correct but don't match Bluebook guide
- **Solution**: Law reviews sometimes have house styles that deviate from Bluebook
- Note the deviation and suggest checking law review's specific submission guidelines

**Issue**: Argument seems weak but can't articulate why
- **Solution**: Return to substantive_critique.md and systematically check against criteria
- Often issue is logical fallacy, unsupported assumption, or missing counterargument

**Issue**: Too many issues to address in single memo
- **Solution**: Prioritize ruthlessly - focus on critical and substantial issues
- Group minor issues by type rather than listing individually

## Tips for Efficiency

1. **Use search/grep**: When looking for specific issues across chunks, use grep or search functions
2. **Create issue tracker**: Keep running list of issues as you work through chunks
3. **Batch similar tasks**: Review all footnotes at once, all topic sentences at once, etc.
4. **Use examples**: When suggesting revisions, provide concrete example text
5. **Use web search**: Don't guess about current law - verify recent developments, and say so plainly when search is unavailable
6. **Preserve author intent**: Understand what author is trying to say before suggesting changes

## Bundled resources

Read the reference for a pass at the start of that pass, not before. Each is long; loading all three at once wastes the context the article itself needs.

- `resources/article_structure.md` — macro and micro structure for legal scholarship: title and abstract, introduction architecture, Part organization, paragraph and topic-sentence discipline, transitions, footnote organization. Read at the start of Pass 1.
- `resources/substantive_critique.md` — the systematic criteria for evaluating thesis, argumentation, research completeness, doctrinal accuracy, empirical claims, and scholarly contribution. Read at the start of Pass 2, and return to it when an argument seems weak but the reason is not obvious.
- `resources/bluebook_guide.md` — condensed citation rules (21st edition) covering the forms that actually recur: cases, statutes, law reviews, books, signals, short forms, typeface. Read at the start of Pass 3.
- `scripts/chunk_article.py` — splits a long article on section boundaries. Python 3, standard library only. Reads `.docx` directly, extracting body text and footnotes; also accepts plain text and Markdown.

## Limitations and risks

This skill produces editorial critique of legal scholarship. It is not legal advice, and its assessments of doctrine are an editor's read rather than an authority.

**The fact-check pass is only as good as the search behind it.** Without web access the skill cannot verify holdings, quotations, statutory currency, or empirical claims. The correct output in that situation is a claim marked "unverified," not a claim silently accepted. An article that passes a searchless fact-check pass has not been fact-checked.

**Citation review checks form, not existence.** The Bluebook pass evaluates whether a citation is correctly formatted. A perfectly formatted citation to a case that does not exist, or that does not support the proposition, will pass unless the fact-check pass independently catches it. For AI-assisted drafts this is the failure mode that matters most, and the two passes must both run.

**Chunking degrades cross-cutting review.** Splitting a long article on section boundaries preserves local coherence but not global. Repeated citations, `supra` references, terminology drift, and structural problems visible only across Parts can be missed. The synthesis step exists to compensate and does so imperfectly; on articles long enough to require chunking, treat structural findings as provisional.

**Section detection is heuristic.** The chunker infers structure from heading patterns. Unnumbered headings, unconventional schemes, and footnote text that resembles a heading can produce a wrong section map. Read the map it prints before trusting the chunks.

**Editing pressure works against the author's voice.** Passes 4 and 6 optimize for clarity and concision, and scholarly prose sometimes earns its complexity. Where a suggested revision would flatten a distinction the author is drawing, the distinction wins.

**The critique is US-centric.** The Bluebook guide, the citation forms, and the doctrinal expectations assume American legal scholarship. Structure and argumentation passes transfer to other systems; citation review does not.

`scripts/chunk_article.py` uses only the Python standard library (`re`, `sys`, `zipfile`, `typing`). It makes no network calls, spawns no child processes, evaluates no dynamic code, and writes only chunk files beside the article it is given. The optional track-changes output path is the sole feature requiring a third-party package (`python-docx`).
