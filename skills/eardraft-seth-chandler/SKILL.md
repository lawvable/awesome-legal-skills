---
name: eardraft
description: >-
  Transforms reading-oriented prose into listening-optimized text for flat, neutral vocal
  delivery — TTS, podcasts, audiobooks, CLE audio. Carries a legal layer: case citations,
  section symbols, subsection lettering, Latin terms and footnotes are unspeakable as
  written, so a brief, opinion, statute, contract or memo needs them expanded, restructured
  or stripped before it can be listened to — and quoted authority is never rewritten. Use
  when converting written content for audio, preparing oral argument by ear, producing CLE
  or client-facing audio, or making a document listenable on a commute. Triggers on "make
  this listenable," "convert for audio," "optimize for reading aloud," "prepare for TTS,"
  "make an audio version," "podcast script," "read this aloud." Supports English, French,
  Spanish, Italian, German and Portuguese; outputs plain text, ElevenLabs audio tags, or
  SSML for Amazon Polly, Google or Azure.
metadata:
  author: "Seth J. Chandler"
  author_link: "https://legaled.ai"
  license: "MIT"
  version: "2026-07-29"
  jurisdiction: "All"
  language: "English, French, Spanish, Italian, German, Portuguese"
---

# EarDraft: Text-to-Listening Transformation

Transform reading-oriented prose into listening-optimized text that works perfectly when read aloud with flat, neutral vocal delivery (TTS, podcasts, audiobooks).

## Core Principle

When text will be read aloud without pacing, intonation, or gesture, the only instruments available are syntax, segmentation, and auditory clarity. Transform text to preserve intellectual rigor while ensuring comprehension through sound alone.

**Listening-optimized text should sound like a knowledgeable person talking to intelligent peers about something important.** Not like a motivational speaker, not like a sales pitch, not like someone talking to children.

## Quick Start

When a user asks to transform text for listening:

1. **Check whether the source is legal material**: a brief, opinion, statute, regulation, contract, memo, client letter, CLE script, or student outline. If so, read `resources/legal-audio.md` before transforming — legal prose carries meaning in citations, italics, footnotes and subsection lettering that has no audio equivalent, and the general rules below do not address any of it.
2. **Determine language and format**: Ask if not clear (default: English, plain text)
3. **Apply core transformations**: Use syntax as rhythm, control density, maintain clarity
4. **Follow anti-patterns**: Never fragment into staccato, never adopt motivational cadence
5. **For SSML/tagged output**: Use tags sparingly (2-5 per paragraph max)

## Legal material

Legal sources get their own pass. Load `resources/legal-audio.md` and apply it alongside the language reference.

One rule from that file overrides everything else in this skill: **quoted authority is never rewritten.** The transformations below recast sentences for the ear. Applied to a block quote from an opinion, a statutory provision, or an operative contract term, recasting produces a misquotation — which in legal work is a professional problem, not a stylistic one. Cut by ellipsis, frame verbally, or paraphrase openly and label it as paraphrase. Never smooth a quotation silently.

## Language-Specific Guidelines

Each language has culturally and linguistically optimized transformation patterns. Load the appropriate reference file:

- **English**: `resources/english.md` (default)
- **French**: `resources/french.md` - Discourse particles, melodic phrasing
- **Spanish**: `resources/spanish.md` - Regional variants, conversational markers
- **Italian**: `resources/italian.md` - Melodic rhythm, emotive connectors
- **German**: `resources/german.md` - Formal/conversational registers, compound rhythms
- **Portuguese**: `resources/portuguese.md` - Brazilian focus, discourse particles

And, orthogonal to language, load whenever the source is legal:

- **Legal material**: `resources/legal-audio.md` - citations, symbols, quotation boundaries, footnotes, register by use case

**Always load the language-specific reference before transforming** unless using English with familiar patterns.

## Output Format Options

### 1. Plain Text (default)
Clean prose without markup. Use syntax and structure for pacing.

### 2. ElevenLabs with [AudioTags]
Inline tags for precise TTS control:
- `[pause:short]` (0.5s), `[pause:medium]` (1s), `[pause:long]` (2s)
- `[emphasis]` for critical words
- `[speed:slow/fast/normal]` for pacing
- **CRITICAL**: Use 2-5 tags max per paragraph. Over-tagging creates robotic speech.

### 3. ElevenLabs Implicit
No visible tags. Use punctuation for pacing:
- Periods: 0.5-1s pauses
- Em dashes: 1-2s dramatic pauses
- Paragraph breaks: 2-3s section pauses

### 4. SSML - Amazon Polly
```xml
<speak>
  <break time="1s"/>
  <emphasis level="moderate">critical term</emphasis>
  <prosody rate="slow">complex section</prosody>
</speak>
```

### 5. SSML - Google Cloud TTS
```xml
<speak>
  <break strength="medium"/>
  <emphasis level="strong">key point</emphasis>
  <say-as interpret-as="date">2025-11-03</say-as>
</speak>
```

### 6. SSML - Microsoft Azure TTS
```xml
<speak>
  <mstts:express-as style="newscast">
    <break time="500ms"/>
    <emphasis>important</emphasis>
  </mstts:express-as>
</speak>
```

**For all SSML/tagged formats**: Wrap only strategic moments. Most text should be clean prose.

## Core Transformation Techniques

### Syntax as Rhythm
Mix sentence lengths naturally. Short sentences for emphasis, longer ones for reasoning. Include dependent clauses and natural transitions.

### Auditory Cohesion
Repeat key terms for reinforcement. Varying synonyms weakens recall in listening contexts.

### Transparent Logic
Use clear connectives: "Next," "But that view fails," "Now consider," "The result is this."

### Self-Refreshing Arguments
Reiterate thesis every few paragraphs. Listeners cannot glance backward.

### Short Referential Distance
Avoid pronouns requiring recall of earlier paragraphs. Use micro-redundancy strategically.

### Imageable Language
Prefer concrete nouns and active verbs. Listeners must visualize without tonal help.

### Controlled Density
Clarify complex reasoning through explicit enumeration or sequencing.

### Monotone Robustness
Eliminate clauses whose meaning depends on inflection. Rewrite into explicit declaratives.

## Critical Anti-Patterns (NEVER Do These)

### Anti-pattern: Staccato Fragmentation
DON'T: "The court considered factors. Three factors. In reaching its decision."
DO: "The court considered three factors in reaching its decision."

### Anti-pattern: Motivational Speaker Cadence
DON'T: "You can do this. You will succeed. The future is yours. Act now."
DO: Natural conversational variety with substance over hype.

### Anti-pattern: Over-Prescriptive Commands
DON'T: "Network actively. Build your portfolio. Apply now."
DO: "You might consider networking, building a portfolio, or applying to positions."

### Anti-pattern: Emotion Projection
DON'T: "You are excited" or "You are inspired"
DO: Offer information; let listeners decide how they feel.

### Anti-pattern: One-Word Emphasis Patterns
DON'T: "Think contracts. Think torts. Think procedure."
DO: Natural phrasing that respects intelligent audiences.

### Anti-pattern: False Intimacy
DON'T: Presumptuous "you" statements claiming to know listener's motivations
DO: Respectful communication with intelligent peers.

### Anti-pattern: Transforming Information into Sales Copy
DON'T: "At the forefront of a transformative shift," "your secret weapon"
DO: Maintain objectivity appropriate to source material.

### Anti-pattern: Over-Tagging Audio
DON'T: Tags after every sentence, emphasis on every keyword
DO: 2-5 strategic tags per paragraph maximum.

## TTS Markup Philosophy (CRITICAL for Tagged/SSML Output)

**Natural speech rhythm comes from good writing, not excessive markup.**

### Pause Tags - Use ONLY For:
- Major topic shifts between distinct sections (2-4 max per paragraph)
- Dramatic effect at strategic moments
- Breathing room after dense technical content
- **NOT** after every sentence or clause

### Emphasis Tags - Use ONLY For:
- Truly critical words carrying the entire argument (1-2 max per paragraph)
- Technical terms being defined for first time
- Crucial distinctions or corrections
- **NOT** every important point or keyword

### Good vs Bad Tagged Example

**Wrong** (over-tagged, mechanical, exhausting):
```
As students [pause:short] in the Fall 2025 course, [pause:short] you are at the forefront [pause:short] of a transformative shift. [pause:medium]
```

**Right** (natural flow with strategic tags):
```
As students in the Fall 2025 Large Language Models for Lawyers course, you're entering a profession in the middle of transformation. [pause:medium] Dean Tucker's email highlights something concrete—a surge in AI-focused roles at major firms. These aren't theoretical positions. They're [emphasis] hiring now.
```

## Workflow

1. **Identify source characteristics**: Informative? Analytical? Personal narrative? Preserve the voice.
2. **Select language and format**: Use references file if non-English or unfamiliar with language patterns.
3. **Apply transformations**: Focus on syntax, clarity, and natural flow first.
4. **Add markup strategically** (if requested): 2-5 tags per paragraph maximum.
5. **Test for parody**: If it sounds like a corporate trainer or infomercial, dial back.
6. **Present complete transformed text**: No explanatory commentary unless requested.

## Common User Customizations

Users may request audience-specific adaptations:
- "Assume the audience is 12 years old" → Simpler vocabulary, shorter sentences
- "This is for medical professionals" → Preserve technical terminology
- "The audience is nervous" → Warmer, more reassuring tone
- "Make it more conversational" → Increase discourse markers, vary rhythm

**Always preserve the original's intent and voice** while adapting for the specified audience.

## When to Load Language References

Load language-specific references when:
- User specifies non-English language
- Unfamiliar with specific language's oral patterns
- Need regional variant guidance (Spanish dialects, Brazilian vs European Portuguese)
- First time transforming in a particular language

Skip loading references only when:
- Working in English with clear understanding of patterns
- Recent transformation in same language with principles fresh in mind

## Output

Present the complete transformed text immediately. Do not include:
- Commentary about changes made
- Explanations of transformation decisions
- Meta-discussion about the process

Unless specifically requested by user.

## Bundled resources

Load the one language file the job needs, plus the legal file whenever the source is legal material. Do not read all seven.

- `resources/english.md` — English patterns. The default.
- `resources/french.md` — discourse particles, melodic phrasing.
- `resources/spanish.md` — regional variants, conversational markers.
- `resources/italian.md` — melodic rhythm, emotive connectors.
- `resources/german.md` — formal and conversational registers, compound rhythms.
- `resources/portuguese.md` — Brazilian focus, discourse particles.
- `resources/legal-audio.md` — citations, section symbols, quotation boundaries, footnotes, Latin, party shorthand, and register by use case. Orthogonal to language: load it *alongside* a language file whenever the source is a brief, opinion, statute, regulation, contract, memo, client letter, CLE script, or student outline.

## Limitations and risks

This skill rewrites prose so it can be followed by ear. The rewriting is the product, and it is also the risk.

**The output is a rendering, not the document.** Sentence structure, ordering, and emphasis all change. For legal material the citation apparatus is deliberately stripped. Where the exact words govern — an operative contract term, a statutory provision, a holding someone will rely on — the source text governs and the audio does not.

**Transformation pressure works against caveats.** Qualifications, hedges, and disclaimers are dry, and a rewrite optimised for flow wants to cut them. That tendency is most dangerous in exactly the material where the qualification carries the meaning. The legal file makes this a pre-delivery check; honour it.

**Stripping citations removes verifiability.** A listener cannot tell a well-supported claim from an unsupported one once the footnotes are gone. Where the audience needs to check the authority, read citations in full rather than compressing them.

**Nothing here produces audio.** The output is text — plain, tagged, or SSML. Feeding it to a speech engine, and any cost or privacy consequence of doing so, is the user's own step. Consider what a confidential draft means before pasting it into a third-party TTS service.

**SSML support varies.** The tag sets for Amazon Polly, Google Cloud TTS, and Azure differ and change over time. Treat the examples here as the common shape, and check the current documentation for the engine actually in use.

The skill contains no executable code, makes no network calls, and moves no data outside the session.
