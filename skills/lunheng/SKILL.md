---
name: lunheng
description: "Lunheng (论衡) — Multi-agent paper review framework aligned with NeurIPS / Nature / JACS rubrics. 4 specialist agents (Architect, Writer, Refiner, Evaluator-bench) coordinate around a persistent visual contract. Use when user says \"lunheng\", \"论衡\", \"严格评审\", \"top journal review\", \"multi-agent review\", or wants a comprehensive paper assessment with anchored scoring."
argument-hint: [paper-directory]
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, Agent
---

# Lunheng — Multi-Agent Paper Review (论衡)

> "权衡论证, 校释虚妄" — 王充《论衡》(~80 CE)

Operate on the paper at: **$ARGUMENTS**

## What This Skill Does

Lunheng treats paper improvement as a **contract-governed multi-agent process** with five roles:

1. **Architect** (`A_arch`) — reads paper → emits Blueprint + Visual Contract
2. **Writer** (`A_w`) — re-drafts sections under contract constraints
3. **Refiner** (`A_ref`) — global polish + contract update
4. **Evaluator Bench** (`E_1 ... E_8`) — 8 parallel sub-agents, one per dimension
5. **Aggregator** — composite score $R = \frac{1}{8} \sum D_k$, decides loop continuation

The 8 evaluation dimensions are anchored to actual NeurIPS/Nature/JACS scoring practice. See `docs/EVALUATION_RUBRIC.md` for the full anchored scale.

## Constants

- **MAX_ITERATIONS = 3**
- **STOP_THRESHOLD = 7.0** — composite score
- **WORKSPACE = `<paper_dir>/lunheng_workspace/`**
- **CONTRACT_PATH = `<paper_dir>/lunheng_workspace/visual_contract.json`**
- **LOG = `<paper_dir>/LUNHENG_LOG.md`**

## The 8 Dimensions

| ID | Dimension | Aligned with |
|----|-----------|--------------|
| D1 | Soundness | NeurIPS Soundness, Nature Technical Rigor |
| D2 | Significance & Originality | NeurIPS Significance + Originality |
| D3 | Clarity & Organization | NeurIPS Clarity, JACS Clarity |
| D4 | Experimental Substance | NeurIPS Quality (claims supported) |
| D5 | Reproducibility | NeurIPS 16-item Checklist |
| D6 | Citation Quality | JACS Literature Appropriateness |
| D7 | Visual & Tabular Communication | Nature Figure Quality |
| D8 | Ethics, Limitations & Broader Impact | NeurIPS Limitations + Ethics |

## Workflow

### Step 0: Initialize

```bash
mkdir -p <paper_dir>/lunheng_workspace
cp <paper_dir>/main.tex <paper_dir>/lunheng_workspace/main_round0.tex
cp <paper_dir>/main.pdf <paper_dir>/lunheng_workspace/main_round0.pdf 2>/dev/null || true
```

Locate the main `.tex` and `.bib` files (do not assume they are named `main.tex` / `references.bib` — detect them).

### Step 1: Architect Agent

Spawn a Claude sub-agent (`subagent_type: general-purpose`) with this prompt:

```
You are the ARCHITECT agent for the Lunheng paper review framework.

Read the paper at [paper_dir]/[main_tex] and figures in [paper_dir]/figures/.

Produce TWO outputs:

1. blueprint.md — structured outline:
   - Ordered sections {s_1, s_2, ...} with argument outline per section
   - Key claims and their supporting evidence
   - 3 most severe structural issues identified

2. visual_contract.json — following the schema in docs/ARCHITECTURE.md:
   - global_visual_registry (every fig/tab with semantic_description and expected_section)
   - section_obligations (which visuals MUST appear in each section)
   - terminology_glossary (terms that should be unified)
   - validation_rules (unique_labels, all_visuals_referenced, all_references_resolved)

Save to:
- <paper_dir>/lunheng_workspace/blueprint.md
- <paper_dir>/lunheng_workspace/visual_contract.json

Report a 200-word summary highlighting the 3 most severe structural issues.
```

### Step 2: Round 1 Evaluator Bench — establish baseline

Spawn **all 8 evaluators in a single message** (parallel Agent tool calls). Each evaluator gets:
- The current manuscript
- The visual contract from Step 1
- The rubric anchors for its dimension (from `docs/EVALUATION_RUBRIC.md`)

Each returns:

```yaml
dimension: D_k
score: <1-10>
confidence: <1-5>
strengths: [list]
weaknesses:
  CRITICAL: [list]
  MAJOR: [list]
  MINOR: [list]
fixes: [actionable list]
score_change_criteria:
  - "Score will rise to X if Y"
```

Aggregate $R_1 = \frac{1}{8} \sum D_k$. Save to `LUNHENG_LOG.md`.

### Step 3: Generate-Evaluate-Adapt Loop

For `iteration = 1 .. MAX_ITERATIONS`:

If $R \geq 7.0$: **STOP** → Step 6.

Otherwise:

#### Step 3a: Writer agents (per-section, parallel where possible)

For each section flagged by low-scoring dimensions, spawn a Writer sub-agent:

```
You are the WRITER agent. Re-draft section "<s_i>" of the paper.

Inputs:
- Blueprint constraint for this section: <relevant section of blueprint.md>
- Visual Contract: <visual_contract.json>
- Current section text: <paste>
- Reviewer feedback for this section: <paste relevant CRITICAL/MAJOR weaknesses>

Constraints:
1. Follow the planned argument structure from blueprint
2. Reference EVERY visual in section_obligations[<s_i>] using \ref{} or \cite{}
3. For each \ref, provide 1-2 sentences of context
4. Use exactly the terms from terminology_glossary
5. NO data-dumping — every number must support an argument

Produce:
- Improved LaTeX for this section, wrapped in <SECTION_OUTPUT>...</SECTION_OUTPUT>
- Outside the tags: which contract obligations satisfied / still pending
```

#### Step 3b: Refiner agent (single, global)

Aggregate all section drafts into `draft_round<N>.tex`. Spawn the Refiner:

```
You are the REFINER agent. Polish the full draft at <draft_round<N>.tex>.

Operations (in order):
1. Compress redundancy across sections
2. Harmonize terminology per terminology_glossary
3. For each \ref{fig:X} / \ref{tab:X}, ensure 1-2 sentences of surrounding context
4. Verify cross-reference integrity (all \cite resolve, all \ref resolve)
5. Update the visual contract (mark `actual_references` populated)

Save:
- refined_round<N>.tex
- updated visual_contract.json
- refine_log_round<N>.md (what changed and why)
```

#### Step 3c: Round-N Evaluator Bench

Re-spawn all 8 evaluators **with fresh context** (no memory of Round 1) on the refined draft. Aggregate $R_N$.

If $R_N \geq 7.0$: STOP. Otherwise, increment iteration.

### Step 4: Compile & Verify

```bash
cd <paper_dir>
xelatex -interaction=nonstopmode <main>.tex
bibtex <main>
xelatex -interaction=nonstopmode <main>.tex
xelatex -interaction=nonstopmode <main>.tex
```

Verify:
```bash
grep -c "undefined" <main>.log    # must be 0
grep -c "Overfull" <main>.log     # ≤ 5 acceptable, address > 10pt overfulls
```

### Step 5: Final Visual Contract Validation

```python
import json, re
with open(f'{paper_dir}/lunheng_workspace/visual_contract.json') as f:
    c = json.load(f)
with open(f'{paper_dir}/main.tex') as f:
    tex = f.read()

violations = []
for v in c['global_visual_registry']:
    label = v['label']
    if not re.search(rf'\\\\label\\{{{label}\\}}', tex):
        violations.append(f"Label {label} not defined in main.tex")
    if not re.search(rf'\\\\(ref|eqref)\\{{{label}\\}}', tex):
        violations.append(f"Label {label} never referenced in main.tex")

if violations:
    print(f"⚠️  {len(violations)} contract violations found:")
    for v in violations: print(f"  - {v}")
else:
    print("✅ Visual contract fully satisfied")
```

### Step 6: Document Results

Write `<paper_dir>/LUNHENG_LOG.md`:

```markdown
# Lunheng Review Log

## Final Composite Score: R = X.XX / 10
Verdict: <Accept / Borderline / Reject>

## Per-dimension Scores

| ID | Dimension | R0 | R1 | R2 | R3 (final) | Δ |
|----|-----------|----|----|----|------------|---|
| D1 | Soundness | a | b | c | d | +Δ |
| ... |

## Visual Contract Compliance
- Total visuals registered: N
- All referenced: Yes/No
- All captions contract-aligned: Yes/No
- Cross-section terminology consistent: Yes/No

## Round-by-Round Changelog
### Round 1
**Architect findings:**
- [3 structural issues]

**Writer changes (sections re-drafted):** ...
**Refiner operations:** ...
**Evaluator deltas:** ...

### Round 2
...

## Output Files
- `main.tex` — Final manuscript
- `main.pdf` — Compiled PDF
- `visual_contract.json` — Final contract state
- `lunheng_workspace/` — All intermediate drafts and per-round logs
```

## Key Rules

- **NEVER fabricate experimental results.** Synthetic experiments OK only as marked future work.
- **PRESERVE all raw agent outputs** in `lunheng_workspace/` for audit.
- **FAIL LOUD on contract violations** — if a visual obligation is impossible, the Architect must update the contract; the Writer must not silently drop it.
- **Sub-agent isolation** — every Agent tool call gets a self-contained prompt; never assume shared context across sub-agents.
- **Parallel evaluators** — spawn all 8 in a single message for speed.
- **Anchored scoring** — evaluators must reference the rubric anchors when assigning scores, not vibes.

## Override Examples

- `/lunheng paper/ — max_iterations: 2` — only run 2 rounds
- `/lunheng paper/ — stop_threshold: 8.0` — require higher quality bar
- `/lunheng paper/ — human_checkpoint: true` — pause before each round for user approval
- `/lunheng paper/ — venue: nature` — emphasize Nature-specific criteria (significance/advance heavy)
- `/lunheng paper/ — venue: neurips` — emphasize ML-specific criteria (reproducibility checklist heavy)

## When to Use vs. `lunheng-quick`

- **`lunheng`** (this skill): paper has structural issues (sections out of order, figures mismatched, terminology inconsistent), needs deep restructuring. Costs ~10–25 sub-agent calls per round.
- **`lunheng-quick`**: paper is structurally OK, just needs polish/clarity. One reviewer + one fixer loop, 2 rounds. Costs ~4–6 sub-agent calls total.
