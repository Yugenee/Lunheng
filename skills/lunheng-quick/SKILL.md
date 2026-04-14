---
name: lunheng-quick
description: "Lunheng-quick — single-reviewer 2-round paper polish. Use when paper is structurally OK and only needs writing/clarity polish. Lighter than full lunheng (no architect, no writer/refiner split, no 8-evaluator bench). Use when user says \"quick polish\", \"快速润色\", \"lunheng quick\", or wants a fast review-fix-recompile loop without the full multi-agent setup."
argument-hint: [paper-directory]
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, Agent
---

# Lunheng-Quick — Single-Reviewer Polish Loop

A lightweight version of [lunheng](../lunheng/SKILL.md) for papers that don't need full restructuring.

Operate on the paper at: **$ARGUMENTS**

## When to Use Each

| Paper state | Use |
|-------------|-----|
| Major structural issues (sections out of order, figure–text mismatch, terminology drift) | `lunheng` |
| Polished structurally, just needs writing/clarity sweep | `lunheng-quick` ← (this) |
| Want anchored 8-dim scoring | `lunheng` |
| Want a fast yes/no readiness check | `lunheng-quick` |

## Constants

- **MAX_ROUNDS = 2**
- **STOP_THRESHOLD = 7.0** (composite over the same 8 dimensions)
- **WORKSPACE = `<paper_dir>/lunheng_quick_workspace/`**

## Workflow

### Step 0: Snapshot

```bash
mkdir -p <paper_dir>/lunheng_quick_workspace
cp <paper_dir>/main.pdf <paper_dir>/lunheng_quick_workspace/main_round0.pdf 2>/dev/null
```

### Step 1: Round 1 — Single Reviewer

Spawn ONE Claude sub-agent (`subagent_type: general-purpose`) with this prompt:

```
You are a senior reviewer for a Q1 journal in this paper's field.
Score the paper at <paper_dir>/<main.tex> on the 8-dimension Lunheng rubric.

Anchors (1-10 scale, see docs/EVALUATION_RUBRIC.md):
D1 Soundness | D2 Significance & Originality | D3 Clarity & Organization
D4 Experimental Substance | D5 Reproducibility | D6 Citation Quality
D7 Visual & Tabular Communication | D8 Ethics, Limitations & Broader Impact

For each dimension, return:
- score (1-10)
- 1-2 most critical issues
- 1-2 specific actionable fixes
- score_change_criteria ("Score will rise to X if Y")

Compute composite R = mean(D1..D8).
Provide an Overall verdict (NeurIPS-style 1-6 scale): 6=top-tier, 5=strong accept,
4=borderline accept, 3=borderline reject, 2=reject, 1=strong reject.
```

Save the full review to `lunheng_quick_workspace/round1_review.md`.

### Step 2: Implement Round 1 Fixes

Apply CRITICAL fixes first, then MAJOR. Common fix patterns:

| Issue | Fix |
|-------|-----|
| Data dumping | Rewrite paragraphs as claim → evidence → interpretation |
| Overclaim | Soften language ("证明" → "表明", "validate" → "demonstrate") |
| Terminology drift | Choose canonical form, replace globally |
| Missing tool citations | Add to .bib, cite at first mention |
| Dangling \\ref or \\cite | Remove or define the missing target |
| Caption only labels axes | Rewrite with self-contained description |

### Step 3: Recompile

```bash
xelatex -interaction=nonstopmode <main>.tex
bibtex <main>
xelatex -interaction=nonstopmode <main>.tex
xelatex -interaction=nonstopmode <main>.tex
```

Verify 0 undefined refs/citations.

### Step 4: Round 2 — Fresh Reviewer

Spawn a **fresh** sub-agent with no memory of Round 1. Use the same prompt as Step 1, on the revised paper.

Compute $R_2$. If $R_2 \\geq 7.0$: STOP.

### Step 5: Document

Write `<paper_dir>/LUNHENG_QUICK_LOG.md`:

```markdown
# Lunheng Quick Polish Log

## Composite Scores

| Dimension | R0 | R1 | R2 |
|-----------|-----|-----|-----|
| D1 Soundness | a | b | c |
| ... |
| **R (mean)** | **R0** | **R1** | **R2** |

## Round 1 Findings & Fixes
<critical issues + what was changed>

## Round 2 Findings (final)
<remaining issues + verdict>
```

## Key Differences from Full Lunheng

| Feature | lunheng | lunheng-quick |
|---------|---------|---------------|
| Architect agent | Yes | No |
| Writer/Refiner split | Yes | No (just edits) |
| Evaluator count per round | 8 (parallel) | 1 |
| Visual contract | Persistent JSON | Implicit |
| Sub-agent calls per run | 10–25 per round | 1 per round |
| Best for | Deep restructuring | Polish pass |
