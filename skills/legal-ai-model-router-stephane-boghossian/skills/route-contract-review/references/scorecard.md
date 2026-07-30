# Contract Review — extended notes (data as of 2026-07)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-07.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

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
