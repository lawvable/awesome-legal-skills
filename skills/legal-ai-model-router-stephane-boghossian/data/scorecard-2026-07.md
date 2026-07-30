# Legal Model Scorecard — data as of 2026-07

**This is the canonical dataset for the `legal-ai-model-router` skill bundle.** Every skill's
`references/scorecard.md` is a slice of this file. When you update benchmarks, update this file
first, bump the date, and re-slice the per-skill copies. See `../README.md` → "Updating the data".

> **Read this before trusting any number below.** These are point-in-time snapshots from public
> benchmarks that change monthly and disagree with each other. Use them as a **prior**, not a verdict.
> For any high-stakes matter, re-check the live sources (bottom of this file) and keep a human in the loop.

---

## How to read this

Each vertical reports the metric its source benchmark actually measures. They are **not** the same metric,
so scores are **not** comparable across verticals. "Reliability" on legalbenchmarks.ai (all-pass on a
lawyer checklist) is a far harsher scale than "accuracy" on Vals LegalBench (multiple-choice legal reasoning).

Model names reflect what the benchmarks published as of the snapshot date. Vendors ship fast; a name here
may already be superseded. The **archetype** (what a model is *for*) ages slower than its exact rank.

---

## 1. Contract Drafting

**Source:** legalbenchmarks.ai — "Contract Drafting" (34 tasks, 3rd installment, refreshed monthly).
**Metric:** `Reliability` = share of tasks passed *fully* correct on a lawyer-written checklist (binary;
one miss fails the whole task). `Usefulness` = 1–3 mean (clarity / length / structure). Cost = $/task.

| Rank | Model            | Provider  | Reliability | Usefulness | Cost/task |
|-----:|------------------|-----------|------------:|-----------:|----------:|
| 1    | Claude Opus 4.8  | Anthropic | 67.6%       | 2.67       | ~$0.29    |
| 2    | Claude Fable 5   | Anthropic | 61.8%       | 2.66       | ~$0.63    |
| 3    | Grok 4.5         | xAI       | 58.8%       | 2.61       | ~$0.19    |
| 4    | Gemini 3.5 Flash | Google    | 55.9%       | 2.60       | ~$0.08    |
| 5    | Claude Sonnet 4.6| Anthropic | 50.0%       | 2.63       | $0.13     |
| 5    | Gemini 3.1 Pro   | Google    | 50.0%       | 2.69       | $0.07     |
| 7    | GPT 5.6 Sol      | OpenAI    | 44.1%       | 2.75       | ~$0.19    |
| 7    | Qwen 3.7 Max     | Alibaba   | 44.1%       | 2.67       | ~$0.03    |
| 9    | GPT-5.5          | OpenAI    | 41.2%       | 2.77       | $0.15     |
| 10   | DeepSeek V4 Pro  | DeepSeek  | 26.5%       | 2.68       | ~$0.03    |
| 10   | GPT-5.4-mini     | OpenAI    | 26.5%       | 2.55       | ~$0.01    |

**Truths / nots**
- **Opus 4.8** — best all-round drafter; uniquely willing to *flag contradictory instructions* instead of drafting through them. Truth: highest reliability. Not: not the cheapest.
- **Fable 5** — ties Opus on quality but ~2.2× the cost/task without beating it. Not: overpriced for drafting.
- **Grok 4.5** — best non-Anthropic drafter, cheapest of the top 4; uniquely good at *leaving already-sound language untouched* (fewer gratuitous rewrites). Strong value pick.
- **GPT 5.6 Sol** — **highest usefulness (2.75) is a trap:** "more polished than accurate." >50% of its drafts miss ≥1 instruction hidden behind clean prose. Do not route drafting here on the strength of readability.
- **All models** — weak at conflict detection; GPT 5.6 Sol is the worst at silently drafting through contradictions.

---

## 2. Info Extraction

**Source:** legalbenchmarks.ai — "Info Extraction" (29 tasks). Documents sent in **native, unconverted form**,
so file-reading (incl. scanned docs) is part of what's tested. Same two-axis rubric as drafting.

| Rank | Model            | Provider  | Reliability | Usefulness | Cost/task |
|-----:|------------------|-----------|------------:|-----------:|----------:|
| 1    | GPT 5.6 Sol      | OpenAI    | 89.7%       | 2.78       | ~$0.19    |
| 2    | Claude Opus 4.8  | Anthropic | 86.2%       | 2.54       | ~$0.29    |
| 2    | Claude Fable 5   | Anthropic | 86.2%       | 2.51       | ~$0.63    |
| 4    | GPT-5.5          | OpenAI    | 82.8%       | 2.62       | $0.15     |
| 5    | Grok 4.5         | xAI       | 79.3%       | 2.70       | ~$0.19    |
| 6    | Claude Sonnet 4.6| Anthropic | 72.4%       | 2.47       | $0.13     |
| 7    | Gemini 3.1 Pro   | Google    | 65.5%       | 2.51       | $0.07     |
| 7    | Gemini 3.5 Flash | Google    | 65.5%       | 2.76       | ~$0.08    |
| 9    | DeepSeek V4 Pro  | DeepSeek  | 62.1%       | 2.37       | ~$0.03    |
| 10   | GPT-5.4-mini     | OpenAI    | 58.6%       | 2.75       | ~$0.01    |
| 11   | Qwen 3.7 Max     | Alibaba   | 55.2%       | 2.55       | ~$0.03    |

**Truths / nots**
- **GPT 5.6 Sol** — best at *exhaustive clause retrieval* and *cross-document comparison*. Blind spots: **scanned documents**, and **flattening conditional answers into absolutes** ("if X then Y" → "Y"). Verify conditionals.
- **Opus 4.8 / Fable 5** — most dependable pair (tied #2), but the **most verbose** answers tested; you pay in output tokens and post-processing.
- **Grok 4.5** — **best scanned-document handling of any model**, but under-returns on completeness ("almost all" instead of all). Route here for image-heavy/OCR-adjacent extraction, then double-check coverage.
- **Cheap tier (Qwen 3.7 Max, GPT-5.4-mini, DeepSeek V4 Pro)** — bottom of reliability (55–62%). Fine for low-stakes triage, not for extraction you'll rely on.

**Related academic anchors (Wei Chen / Atticus Project):** **CUAD** (clause extraction, 510 contracts, 41 clause types), **MAUD** (M&A reading comprehension, 92 question types), **ACORD** (clause retrieval, 1–5 relevance). These are the open datasets the field uses when it wants reproducible extraction/retrieval evaluation.

---

## 3. Legal Research & Analysis

**Source A:** Vals AI — **LegalBench** (Stanford CodeX partnership; 124 models; updated 2026-07-09).
Measures legal *reasoning* across six task types: issue-spotting, rule-recall, rule-conclusion,
rule-application, interpretation, rhetorical understanding. **Metric:** accuracy (± CI). Cost per M tokens.

| Rank | Model                        | Provider  | Accuracy      | Cost In/Out (per M) | Latency |
|-----:|------------------------------|-----------|--------------:|--------------------:|--------:|
| 1    | Claude Fable 5               | Anthropic | 88.56% ±0.33  | $10 / $50           | 8.96s   |
| 2    | Gemini 3.1 Pro Preview (2/26)| Google    | 87.40% ±0.33  | $2 / $12            | 10.06s  |
| 3    | Gemini 3 Pro (11/25)         | Google    | 87.03% ±0.37  | $2 / $12            | 8.33s   |
| 4    | GPT-5.6 Sol                  | OpenAI    | 86.97% ±0.41  | $5 / $30            | 6.20s   |
| 5    | Gemini 3 Flash (12/25)       | Google    | 86.86% ±0.36  | $0.5 / $3           | 4.67s   |
| 6    | GPT-5.5                      | OpenAI    | 86.52% ±0.41  | $5 / $30            | 18.14s  |
| 7    | GPT-5.4 (xhigh)              | OpenAI    | 86.04% ±0.41  | $2.5 / $15          | 27.79s  |
| 8    | GPT-5                        | OpenAI    | 86.02% ±0.38  | $1.25 / $10         | 18.59s  |
| 9    | Grok 4.5                     | xAI       | 85.97% ±0.41  | $2 / $6             | 67.88s  |
| 10   | GPT-5.1                      | OpenAI    | 85.68% ±0.40  | $1.25 / $10         | 7.05s   |

*(114 more models below the top 10 on the live board.)*

**Truths / nots**
- **The top 10 sit inside ~2.9 percentage points.** On this benchmark, "which model is #1" is mostly noise — pick on cost/speed/constraints, not the leaderboard rank.
- **Gemini 3 Flash is the value story:** 86.86% at **$0.5/$3 and 4.67s** — near-top accuracy, cheapest and fastest in the top tier.
- **Fable 5** leads accuracy but is the most expensive here ($10/$50).
- **Grok 4.5** is competitive on accuracy but **catastrophically slow (67.88s)** — do not put it in an interactive research loop.
- Vals' own caveat: performance varies a lot task-to-task, and even top models mis-cite the wrong rule on FRCP-style Rule-QA. **There is still significant room for improvement for models in law.**

**Source B:** Harvey — **Legal Agent Benchmark (LAB)** (1,200+ agent tasks, 24 practice areas, 75,000+
expert rubric criteria, **all-pass grading**, built from real client matters; long-horizon agentic work).
**No public scores yet** (baselines "coming"). Use LAB as the *task-design standard* for agentic legal
research (multi-step, review-quality output), not as a scoreboard. Its predecessor **BigLaw Bench** covered
short-horizon reasoning (read a contract, answer a question).

---

## 4. Contract Review

**No single public benchmark isolates "contract review."** It is a *composite* skill = find the clauses
(**Info Extraction**, §2) + judge risk/deviation from standard (**legal reasoning**, §3) + propose redlines
(**Contract Drafting**, §1) + catch internal contradictions (**conflict detection**). Route by composing
those three tables and weighting toward the sub-task that dominates the specific review.

**Derived guidance (composite, not a measured leaderboard)**
- **Extraction-heavy review** (find every clause of type X, build an obligations matrix): weight §2 → **GPT 5.6 Sol** leads, but **verify conditionals** (it flattens them) and **Opus 4.8** if you need the safer, more dependable read.
- **Risk/deviation analysis** (is this indemnity market? what's the exposure?): weight §3 → top cluster is a wash on accuracy; pick **Gemini 3 Flash** for cost/speed or **Fable 5 / Opus 4.8** for the safest reasoning.
- **Redline drafting** (rewrite to protect the client): weight §1 → **Opus 4.8** (best drafter *and* best at flagging contradictions) or **Grok 4.5** (leaves sound language alone, cheaper).
- **Conflict detection across a long agreement**: **Opus 4.8** is the documented standout; **avoid GPT 5.6 Sol** (worst at silently drafting through contradictions).
- **Long agreements (100+ pages):** advertised context ≠ effective context. Only **Gemini 3 Deep Think** holds quality near 1M tokens; most models degrade past ~200–400K. Chunk + map-reduce for the rest.

---

## 5. Legal Translation

**Weakest public-benchmark coverage of the five verticals — treat this section as directional, not
benchmark-backed the way §1–§3 are.** There is **no clean legal-translation leaderboard** for frontier
LLMs. Guidance is triangulated from (a) general MT benchmarks that don't touch legal text, (b) multilingual-
reasoning benchmarks used as a proxy, and (c) dedicated legal-MT studies. **Certified/sworn translation
always requires a qualified human translator — the LLM is a first-draft engine here, never the signatory.**

**General translation quality**
- **WMT25** (field's rigor standard): human eval → **Gemini** family won (topped 14/16 language pairs);
  GPT and Cohere Command-A close; DeepSeek/Claude second tier. Rankings are **metric-dependent** — a
  separate methodology put GPT-5, Grok 4, Claude Opus, Gemini in a different order. No settled "leader."
- **Per-language split (directional):** Claude leads German/Japanese/Korean/Dutch/Italian and is
  **preferred by professional translators for tone/register**; Gemini leads Chinese/Brazilian-Portuguese/
  Ukrainian and carries the larger context window for long documents.

**Multilingual reasoning (proxy when no legal-MT number exists)**
- Roughly: **Gemini 3.1 Pro** tops raw multilingual knowledge (~94 MMLU, approx.), **GPT-5.x** close and
  strongest on MMLU-ProX, **Claude Opus** a strong #3 with notably good multilingual math (MGSM).
- This is reasoning *in* a language, not translation *quality* — a proxy, not a substitute.

**Legal-translation-specific evidence (thin but real)**
- **SwiLTra-Bench** (arXiv 2503.01372) — the most rigorous dedicated legal-MT benchmark found (Swiss
  statutes/case-law, DE/FR/IT/Romansh). Finding: **general-purpose LLMs still trail specialized legal-MT
  systems** on terminology equivalence, statutory register, and precedent-preserving case-law translation.
- **EU EUR-Lex** explicitly tells users **not** to rely on its own MT tool for legislation — only the
  human-verified official-language texts are authentic. Institutional distrust of legal MT is stated, direct.
- Glossaries fix *terminology consistency* but not **negation accuracy**, **jurisdiction-concept mapping**
  (common-law "discovery"/"plea bargain" have no civil-law equivalent), **cross-reference integrity**, or
  **legal effect**. These are the failure modes that make legal MT dangerous.

**Arabic / MENA**
- **No Arabic legal-*translation* benchmark exists** — a genuine gap. Arabic legal *reasoning* benchmarks
  exist (**ArabLegalEval**, **ALARB**); tellingly, ArabLegalEval was built by machine-translating English
  LegalBench into Arabic *then* expert-verifying — an implicit admission that raw MT needs human check.
- General Arabic reasoning: **Gemini 3.1 Pro / 3 Pro** lead (~93), **Claude Opus** close (~91–92). Claude's
  Arabic prose is reported (soft/qualitative) as more natural.
- **Mistral is a documented Arabic weak point.** **Qwen** (Qwen-MT line) and **Cohere Aya** are purpose-built
  multilingual and are the strongest *self-hostable* Arabic options.
- **RTL is a UI problem, not a model problem** — output text is fine; display alignment is a front-end
  concern (relevant only if you build your own Arabic UI on the API).

**Routing metric:** none published. Route on the proxies above; **human legal-linguist review is mandatory,
not optional** — that is documented industry consensus, not a hedge.

---

## Generalist context (why not to route off a generalist leaderboard)

- **Verticals re-rank the podium.** The Artificial Analysis intelligence-index leader (Fable 5 ~60, GPT-5.6 Sol ~58–59, Opus 4.8 ~56) is *not* the leader on every legal cut — e.g. Opus 4.8 tops Contract Drafting while GPT 5.6 Sol tops Info Extraction. Never route a legal task off a generalist board.
- **Saturation hides gaps.** GPQA/AIME sit at 94–100% for the top tier — zero routing signal. **HLE** (~53% Fable 5, ~50% Grok 4 Heavy, ~46% Opus 4.8) is the one reasoning test still separating models.
- **Advertised vs effective context diverges 30–60 points past ~200K tokens.** Only Gemini 3 Deep Think holds near its 1M spec.
- **Cost floor:** Chinese open-weight models (DeepSeek V4 Flash ~$0.06/M, Qwen) are 10–50× cheaper than closed frontier — relevant for on-prem/privacy and high-volume triage, at a reliability cost on legal tasks.
- **Scaffold ≠ model** on agentic benchmarks (GAIA scores swing ~30 pts by harness). Judge the *system*, not the model, for agentic legal research.

---

## Cross-cutting caveats (bake these into every routing decision)

1. **Capability ≠ controllability** (Wei Chen, Atticus Project). A high benchmark score does not mean a model stays in scope, cites truthfully, or is safe to deploy unsupervised. Governance is a separate axis from raw performance.
2. **All-pass reality** (Harvey). A review that catches 8 of 10 risks is not 80% useful — it is materially incomplete. Route for reliability on high-stakes work, not average quality.
3. **Grading is imperfect.** legalbenchmarks.ai reliability is scored by a *single* LLM judge (Claude Sonnet 4.6); usefulness by a 2-judge panel (~82% agreement). Their own bias check: Sonnet tops neither board and Anthropic models rank lowest on length — evidence against self-grading favoritism, but LLM-judged scores are still not ground truth.
4. **Coverage is narrow.** legalbenchmarks.ai is English-only, US/UK-skewed, single-turn, one run per task (no drift/consistency testing), with a private task set. Vals LegalBench is multiple-choice reasoning, not drafting. **Non-US, non-English, multi-turn, and long-horizon work is under-measured.**
5. **Benchmark drift & routing collapse.** Numbers here go stale monthly; and a router that always picks one dominant model has stopped routing. Re-validate when new frontier models ship.
6. **Silent quality regression.** Cost savings show up instantly on the bill; quality loss shows up days later in the work product. Gate any cost-driven downgrade behind a spot-check.

---

## Live sources — re-check before high-stakes routing

- Contract Drafting & Info Extraction: https://www.legalbenchmarks.ai/leaderboard (+ /research/phase-2-research)
- Legal reasoning (LegalBench, 124 models, live): https://www.vals.ai/benchmarks/legal_bench
- Agentic legal task design: https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
- "The Path to Better Legal AI: Benchmarks" (Wei Chen): https://www.linkedin.com/pulse/path-better-legal-ai-benchmarks-wei-chen-jpksc
- Atticus open datasets (CUAD/MAUD/ACORD): https://www.atticusprojectai.org/
- Generalist cross-check: https://artificialanalysis.ai/leaderboards/models · https://lmarena.ai · https://www.swebench.com
- Long-context efficiency (Mamba vs transformers on long legal docs): https://arxiv.org/abs/2509.00141

**Snapshot date: 2026-07.** If today is >2 months later, treat ranks as suspect and re-pull the live boards.
