---
name: skill-security-auditor
description: Audit an AI agent skill before installing it. Use proactively whenever the user is about to add, install, enable, or evaluate an unfamiliar skill — including phrases like "audit this skill", "is this skill safe", "scan skill before install", "check skill for malicious code", "review this plugin", or any pre-install gate on an untrusted, third-party, or community-distributed skill bundle. Runs ten categories of static checks (code execution, network exfiltration, credential harvesting, persistence, prompt injection, supply-chain hooks, obfuscation, destructive filesystem ops, secrets, Trojan Source / homoglyphs) and emits a PASS / WARN / FAIL verdict.
metadata:
  author: "Dr. Antoine Louis"
  license: "agpl-3.0"
  version: "2026-05-12"
---

# Skill Security Auditor

Static analysis for AI agent skills. Run it on any skill from outside your own
trust boundary before letting an agent execute its scripts. The auditor walks
the entire skill directory and emits findings across ten threat categories,
then collapses them into a single verdict that CI can gate on.

This skill is paranoid by design. It assumes a skill author may be trying
to compromise the host system, exfiltrate credentials, persist beyond the
session, or inject hostile instructions into the model. Most skills will
trip a couple of LOW or MEDIUM findings — that's expected. The signal worth
acting on is CRITICAL and HIGH.

## When to use

Trigger this skill when the user:

- Is about to install a third-party skill, plugin, or agent extension.
- Asks "is this skill safe?", "audit it", "scan it", "is there anything sketchy
  in here?", or similar pre-install review questions.
- Wants a security gate on a skill marketplace, internal skill registry, or
  CI pipeline that ingests user-submitted skills.
- Just cloned a skill repo and wants a one-shot review before running it.

Do **not** use this skill when the user is auditing their own first-party
code — there are better static-analysis tools (Semgrep, Bandit, CodeQL) for
that. This skill specializes in the specific attack surface of *AI agent
skills*: SKILL.md prompt injection, malicious tool helpers, supply-chain
hooks in dependency manifests, and persistence mechanisms that survive the
agent session.

## Quick start

```bash
# Audit a local directory
python3 scripts/audit.py /path/to/skill

# Audit a git repo (cloned to a temp dir, optionally cleaned up after)
python3 scripts/audit.py https://github.com/example/some-skill.git --cleanup

# Strict mode — treat HIGH findings as blocking (recommended for CI)
python3 scripts/audit.py ./skill --strict

# Machine-readable output for CI
python3 scripts/audit.py ./skill --json --output report.json

# Markdown report suitable for pasting into a PR comment
python3 scripts/audit.py ./skill --markdown --output review.md

# Audit a sub-skill inside a repo containing several
python3 scripts/audit.py ./repo --skill skills/my-skill
```

Exit codes: `0` PASS · `1` FAIL · `2` WARN · `3` usage/IO error.

## What gets scanned

Every file under the skill root is classified and routed to the appropriate
scanner. The categories below summarize *what* each scanner looks for;
`references/threat-model.md` covers the *why* in depth.

| Category              | Severity span    | Examples                                                                       |
| --------------------- | ---------------- | ------------------------------------------------------------------------------ |
| **Code execution**    | HIGH–CRITICAL    | `eval`, `exec`, `os.system`, `subprocess(shell=True)`, dynamic `getattr`        |
| **Network exfil**     | MEDIUM–CRITICAL  | hardcoded IPs, webhook sinks (webhook.site, ngrok, interact.sh), `requests.post` to runtime URLs |
| **Credential harvest**| HIGH–CRITICAL    | reads from `~/.ssh`, `~/.aws`, `~/.gnupg`, sensitive env vars, browser cookie DBs |
| **Persistence**       | HIGH–CRITICAL    | cron, systemd, launchctl, shell rc files, git hooks, authorized_keys, registry Run keys |
| **Prompt injection**  | MEDIUM–CRITICAL  | "ignore previous instructions", role markers, `<\|im_start\|>system`, hidden HTML comments | <!-- noqa: SEC-AUDITOR documentation of attack patterns -->
| **Supply chain**      | MEDIUM–CRITICAL  | unpinned deps, typosquats (Levenshtein 1–2 from popular packages), npm `postinstall` hooks |
| **Obfuscation**       | MEDIUM–HIGH      | base64-decoded code, `chr(...)` chains, hex-escape blobs, Bidi / Trojan Source |
| **Filesystem**        | LOW–CRITICAL     | binaries, symlinks escaping the skill, SUID bits, writes to `/etc`, `rm -rf` patterns |
| **Secrets**           | HIGH–CRITICAL    | AWS keys, GitHub tokens, OpenAI/Anthropic keys, private key headers, JWTs    |
| **CI workflow**       | HIGH–CRITICAL    | unescaped `${{ github.event.* }}` in `run:`, `pull_request_target` with checkout |

The scanners run in this order: structure → filesystem → supply-chain →
workflows → prompts → code. A malformed skill surfaces the structural issue
first instead of drowning the reviewer in cascade findings.

## Verdict criteria

The verdict is a three-state collapse of the findings:

- **PASS** — no CRITICAL, no HIGH, fewer than 5 MEDIUM. LOW findings are
  informational and do not affect the verdict.
- **WARN** — at least one HIGH (in default mode), or 5+ MEDIUM. Means: a
  human should look at this before installing, but nothing is definitely
  malicious.
- **FAIL** — at least one CRITICAL, *or* any HIGH in `--strict` mode.
  Means: do not install. Either there's a clear malicious pattern, or
  there's something that needs explanation from the skill author before
  it can be trusted.

For automated gates, run with `--strict`. The default (non-strict) mode is
for interactive review where a human is in the loop.

## Reading a finding

Each finding has the same shape:

```
🔴 CRITICAL  (3 findings)
────────────────────────────────────────────────────────────────────────
scripts/install.py
  scripts/install.py:42  [CODE-EXEC]
    │ os.system(base64.b64decode(payload).decode())
    Risk: Decodes and executes a base64-encoded payload at runtime
    Fix:  Remove. Skills must not execute arbitrary decoded strings.
```

- The **category tag** (`CODE-EXEC`) is stable across runs — use it to
  build baseline rules or filter in CI.
- The **snippet** is the trimmed source line (max 140 chars). Long lines
  are truncated with `...`.
- The **risk** and **fix** fields are one sentence each, deliberately short
  so a reviewer can triage 20 findings in under a minute.

## Suppression

Two suppression mechanisms exist, intentionally orthogonal:

**1. Line-level (`# noqa: SEC-AUDITOR`)** — when a legitimate skill genuinely
needs a flagged pattern. Add the marker as a trailing comment on the line:

```python
import pickle  # noqa: SEC-AUDITOR — internal-only cache, never deserialized from network
```

Equivalent markers `auditor:ignore-line` and `audit-skip` also work. Lines
with any of these markers are skipped during scanning.

**2. Baseline file (fingerprint suppression)** — for accepting findings
without modifying source. Each finding has a stable 16-char fingerprint
derived from `sha256(file + snippet + pattern + category)` — line numbers
don't matter, so the fingerprint survives reformatting and reordering.

Get fingerprints from a JSON run:

```bash
python3 scripts/audit.py ./skill --json | jq '.findings[] | {fingerprint, category, file}'
```

Then commit a `baseline.yml`:

```yaml
suppressions:
  - fingerprint: a1b2c3d4e5f60718
    reason: reviewed 2025-04-30, internal HTTP call to corporate API
  - fingerprint: 0123456789abcdef
    reason: false positive in vendored library, see ticket SEC-441
```

And run with `--baseline baseline.yml`. See `assets/baseline.example.yml`
for the full schema.

## CI integration

GitHub Actions, gated on CRITICAL findings, opening a PR comment on WARN:

```yaml
name: Skill security audit
on: [pull_request]
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - name: Clone auditor
        run: git clone https://github.com/your-org/skill-security-auditor.git /tmp/auditor
      - name: Run audit
        id: audit
        run: |
          python3 /tmp/auditor/scripts/audit.py . \
            --strict \
            --markdown \
            --output audit-report.md
        continue-on-error: true
      - name: Post review comment
        if: always()
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const body = fs.readFileSync('audit-report.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body
            });
      - name: Fail on critical
        if: steps.audit.outcome == 'failure'
        run: exit 1
```

For pre-commit, just call the auditor directly:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: skill-audit
        name: skill-security-auditor
        entry: python3 scripts/audit.py
        args: [--strict, --quiet]
        language: system
        pass_filenames: false
        always_run: true
```

## References

Detailed reading lives in the `references/` directory:

- **`references/threat-model.md`** — Full taxonomy of attacks a malicious
  skill can mount, with concrete examples per category. Read this if you're
  writing a new pattern or evaluating whether the auditor covers a given
  attack scenario.
- **`references/pattern-catalog.md`** — Complete list of every pattern the
  auditor recognizes, grouped by category, with example malicious source
  and the regex that catches it.
- **`references/remediation-guide.md`** — How to *fix* each finding category.
  Linked from the `fix` field when guidance doesn't fit in one line.

## Limitations

Stated honestly because security tools that pretend to be exhaustive are
worse than ones that admit gaps:

- **No taint tracking.** The auditor sees `requests.post(url, data=secret)`
  and flags it, but it doesn't trace whether `url` came from a trusted
  config. False positives are accepted as the cost of catching real
  exfiltration.
- **No dynamic analysis.** A skill that downloads its payload at runtime
  from a CDN with no suspicious-looking hardcoded URL won't be caught here.
  Pair this with sandboxed execution and network monitoring.
- **Pattern arms race.** Obfuscation techniques evolve; a determined attacker
  will find ways around any static check. CRITICAL findings are reliable;
  HIGH and MEDIUM are pattern matches that benefit from human eyes.
- **Python AST coverage only.** JS/TS/shell get regex coverage but no AST
  pass, so aliased-import attacks in those languages are weaker checks.
- **No reputation data.** This is a pure static analyzer — no calls to
  package registries or threat-intel feeds. Combine with `pip-audit` /
  `npm audit` for known-CVE coverage.

## Why this exists

Skills run with the agent's full execution capability. A compromised skill
can read your credentials, exfiltrate your data, persist on your system, or
inject hostile instructions into the model that survive across conversations.
Software that ingests untrusted code without static review is software that
gets owned. This skill is the static review.
