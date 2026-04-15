---
name: lunheng
description: "Lunheng (论衡) v2.0 — Venue-aware multi-agent paper review framework with Chief Editor role and Narrative dimension. 6 roles (Architect, Evaluator-9, Writer, Refiner, Chief Editor, Aggregator) coordinate around a persistent visual contract AND a word budget contract. Use when user says \"lunheng\", \"论衡\", \"严格评审\", \"top journal review\", \"multi-agent review\", or wants a comprehensive paper assessment with anchored scoring. Requires venue parameter."
argument-hint: [paper-directory] venue:<journal|thesis|nature_sub|conference>
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, Agent
---

# Lunheng — Multi-Agent Paper Review (论衡) v2.0

> "权衡论证, 校释虚妄" — 王充《论衡》(~80 CE)
>
> **v2.0 change log (2026-04-14)**: Added `venue` parameter + word-budget contract + D9 Narrative dimension + Chief Editor role + `cuts` field. v1.0 produced overstuffed papers (14500 chars, 16 `\paragraph` small-headings, fragmented FAQ-style narrative) because all 8 dimensions rewarded additions without a counter-force. v2.0 adds a **budget-enforcing Chief Editor** after Refiner and mandates **every Evaluator propose cuts alongside fixes**.

Operate on the paper at: **$ARGUMENTS**

## What This Skill Does

Lunheng treats paper improvement as a **contract-governed multi-agent process** with six roles:

1. **Architect** (`A_arch`) — reads paper → emits Blueprint (incl. word-budget allocation) + Visual Contract
2. **Evaluator Bench** (`E_1 ... E_9`) — 9 parallel sub-agents, one per dimension; each emits **fixes + cuts**
3. **Writer** (`A_w`) — re-drafts sections under budget + contract constraints
4. **Refiner** (`A_ref`) — global polish + cross-ref + terminology harmonization
5. **Chief Editor** (`A_ed`) — **[NEW in v2.0]** enforces venue word-budget; can override evaluator additions to preserve narrative flow
6. **Aggregator** — composite score $R = \frac{1}{9} \sum D_k$ + budget-check, decides loop continuation

## Constants

- **MAX_ITERATIONS = 3**
- **QUALITY_THRESHOLD = 7.0** — composite score
- **BUDGET_SLACK = 1.10** — allowed overshoot of venue word budget
- **WORKSPACE = `<paper_dir>/lunheng_workspace/`**
- **CONTRACT_PATH = `<paper_dir>/lunheng_workspace/visual_contract.json`**
- **BUDGET_CONTRACT_PATH = `<paper_dir>/lunheng_workspace/word_budget.json`**
- **LOG = `<paper_dir>/LUNHENG_LOG.md`**

## Venue Profiles (required parameter)

| venue | Main text (CN chars) | Abstract | Max `\paragraph` | Small-headings style |
|-------|---------------------:|---------:|-----------------:|----------------------|
| **journal** (default for JMC A / CEJ / Digital Discovery / JACS) | 8,000 – 10,000 | 200-350 | **≤ 3** | Connected paragraphs |
| **nature_sub** (Nat Comm / Nat Comp Sci / Nat Energy) | 2,500 – 3,500 | ≤ 250 words (EN) | **0** | Flowing prose only |
| **conference** (NeurIPS / ICML / ICLR) | 6,000 – 8,000 words (EN) | 150-200 words | ≤ 2 | Connected paragraphs |
| **thesis** (CUPB / 本科 / 硕士毕业) | 15,000 – 30,000 | 400-800 | **allowed** | Sub-headings OK |

**STOP_CRITERION = (R ≥ QUALITY_THRESHOLD) AND (word_count ≤ venue_budget × BUDGET_SLACK)**

If R passes but budget fails → skip Writer/Evaluator, run **Chief Editor only** to trim, then re-check.

## The 9 Dimensions

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
| **D9** | **Narrative Flow & Conciseness** **[NEW v2.0]** | venue-appropriate length + readable prose |

### D9 Rubric anchors (NEW)

- 10: Within 100% of venue budget; ≤ recommended `\paragraph` count; every cut would damage a claim
- 8-9: Within 110% of budget; ≤ 1.5× recommended small-headings; minor tightening possible
- 7: Within 125% of budget OR minor narrative fragmentation from 1-2 excess `\paragraph` blocks
- 5-6: Within 150% of budget OR reads as FAQ/spec sheet rather than prose
- 3-4: > 150% of budget OR section flow broken by >5 excess small-headings
- 1-2: ≥ 2× budget or unreadable as single-narrative paper

### D3 Clarity — budget-aware amendments

Add these D3 anchors to the existing rubric:
- -2 on D3 if sub-section introduces redundancy already covered in prior section
- -1 on D3 if `\paragraph{}` title repeats content headline instead of structural transition

## Workflow

### Step 0: Initialize + Venue Budget Contract

```bash
mkdir -p <paper_dir>/lunheng_workspace
cp <paper_dir>/main.tex <paper_dir>/lunheng_workspace/main_round0.tex
cp <paper_dir>/main.pdf <paper_dir>/lunheng_workspace/main_round0.pdf 2>/dev/null || true
```

**Parse `venue` from `$ARGUMENTS`. If missing, ASK user before proceeding.** Do not default silently.

Write `<paper_dir>/lunheng_workspace/word_budget.json`:

```json
{
  "venue": "journal",
  "main_budget_cn_chars": 9000,
  "main_budget_tolerance": 9900,
  "abstract_budget_cn_chars": 300,
  "max_paragraph_directives": 3,
  "per_section_budget": {
    "Abstract": 300,
    "Introduction": 1200,
    "Methods": 2200,
    "Results": 2500,
    "Discussion": 1200,
    "Conclusion": 400,
    "Data_Availability_and_Impact": 200
  }
}
```

### Step 1: Architect Agent (prompt updated for v2.0)

```
You are the ARCHITECT agent for Lunheng v2.0.

Inputs:
- Paper: [paper_dir]/[main_tex]
- Figures: [paper_dir]/figures/
- Venue budget: <word_budget.json> (read first)

Produce THREE outputs:

1. blueprint.md — structured outline with per-section WORD BUDGET:
   - Ordered sections {s_1, s_2, ...} with argument outline
   - Key claims and supporting evidence
   - **Per-section target word count (must sum to main_budget)**
   - **Recommended use/non-use of \paragraph{} sub-headings per section**
   - 3 most severe structural issues

2. visual_contract.json — schema unchanged from v1.0.

3. word_budget.json — update per_section_budget if paper structure differs from template.

Report a 200-word summary:
- 3 structural issues
- Current vs budget word count delta per section
- Which sections will need compression vs expansion
```

### Step 2: Round 1 Evaluator Bench (9 evaluators with CUTS)

Spawn **all 9 evaluators in a single message**. Each returns:

```yaml
dimension: D_k
score: <1-10>
confidence: <1-5>
rubric_anchor_matched: "..."
strengths: [≥3]
weaknesses:
  CRITICAL: [...]
  MAJOR: [...]
  MINOR: [...]
fixes:   # additions
  - 动作: "..."
    位置: "..."
    估计增字: <N>   # [NEW v2.0] words this adds
    预期效果: "..."
cuts:    # [NEW v2.0] mandatory deletions to balance budget
  - 动作: "删除/压缩 X"
    位置: "..."
    估计省字: <N>
    依据: "为何这条对 claim 非必需"
score_change_criteria: [...]
```

D9 evaluator additionally returns:
```yaml
word_budget_check:
  current: <N>
  target: <N>
  overshoot_pct: <%>
  paragraph_count: <N>
  max_allowed_paragraph: <N>
```

Aggregate $R_1 = \frac{1}{9} \sum D_k$. Save to LUNHENG_LOG.

### Step 3: Generate-Evaluate-Adapt Loop

For `iteration = 1 .. MAX_ITERATIONS`:

**If R ≥ QUALITY_THRESHOLD AND word_count ≤ budget × 1.10**: STOP → Step 6.
**If R ≥ QUALITY_THRESHOLD BUT word_count > budget × 1.10**: skip to Step 3d (Chief Editor only).
**Else**: full Writer → Refiner → Chief Editor → Evaluator.

#### Step 3a: Writer agents (per-section, parallel) — v2.0 constraints

```
You are the WRITER agent for section "<s_i>".

Inputs:
- Blueprint constraint (incl. word budget for this section): <budget>
- Visual Contract
- Current section text
- Reviewer feedback (fixes + cuts for this section)

HARD CONSTRAINTS (v2.0):
1. Final section word count MUST be ≤ budget × 1.10
2. Each "fix" may add at most 100 words to the section. If the fix needs more,
   move the details to SI and cite "详见 SI §S<X>".
3. You MUST execute every "cut" proposed by evaluators unless cutting harms a claim.
4. Do NOT introduce new \paragraph{} sub-headings. The blueprint specifies whether \paragraph is allowed for this section; default is NO.
5. Prefer connected paragraphs over enumerate/itemize for lists ≤ 4 items.
6. Reference every visual in section_obligations; 1-2 sentences of context per \ref.
7. Use exactly the terms from terminology_glossary.

Produce:
- Revised LaTeX wrapped in <SECTION_OUTPUT>...</SECTION_OUTPUT>
- Word count reported: <before> → <after>
- Which cuts applied / which cuts refused with reason
- SI delta: list of items moved to SI
```

#### Step 3b: Refiner agent (unchanged from v1.0)

Merges all Writer outputs into `draft_round<N>.tex`, harmonizes terminology, verifies \ref / \cite integrity. **Does not compress**.

#### Step 3c: Chief Editor agent [NEW v2.0]

```
You are the CHIEF EDITOR for Lunheng v2.0.

Inputs:
- Refined draft: <refined_round<N>.tex>
- Word budget contract: <word_budget.json>
- Venue: <venue>
- Evaluator cuts compilation (from Step 2)

Your authority:
1. Override any Writer output that exceeded section budget
2. Delete \paragraph{} sub-headings added by Writer
3. Merge short paragraphs into flowing prose
4. Move method-detail, protocol, parameter-dump content to SI
5. Delete hedged/speculative passages that a venue reviewer would flag as padding
6. Condense Limitations enumerate to flowing prose (1 para, max 120 CN chars per limit)

Constraints:
- Preserve every core claim, every number, every \cite, every \ref
- Do NOT delete figures or tables; only in-text descriptions may be condensed
- Maintain terminology_glossary consistency

Output:
- editor_round<N>.tex (compressed draft)
- edit_log_round<N>.md (what was cut, by how much, where moved)
- Updated word_budget.json with actual per_section counts

Report:
- Before/after word count per section
- Total char reduction %
- Sections still over budget (for next iteration)
```

#### Step 3d: Evaluator re-run (fresh context, includes D9)

### Step 4: Compile & Verify (unchanged)

### Step 5: Final Visual Contract Validation (unchanged)

### Step 6: Document Results + Budget Audit

`LUNHENG_LOG.md` now includes:

```markdown
## Budget Compliance
- Venue: <journal/thesis/nature_sub/conference>
- Target main text: <N> CN chars
- Final main text: <N> CN chars
- Overshoot: <%>
- \paragraph count: <N> (max allowed: <M>)
- D9 Narrative score: <N>/10
```

## Key Rules (v2.0 updates in **bold**)

- **NEVER fabricate experimental results.**
- **PRESERVE all raw agent outputs** in `lunheng_workspace/`.
- **FAIL LOUD on contract violations.**
- **Sub-agent isolation.**
- **Parallel evaluators.**
- **Anchored scoring.**
- **[NEW v2.0] Budget is contract, not suggestion** — Chief Editor enforces at every round.
- **[NEW v2.0] Every `fix` must be paired with a `cut` of comparable size** unless the paper is currently under budget. No net additions above budget slack.
- **[NEW v2.0] `\paragraph{}` is opt-in per section** — default is banned for journal/nature_sub/conference venues.
- **[NEW v2.0] Writer cannot override Chief Editor** — order of authority: Architect > Chief Editor > Refiner > Writer.

## Override Examples

- `/lunheng paper/ venue:journal` — standard journal compression
- `/lunheng paper/ venue:thesis` — thesis mode, budget relaxed
- `/lunheng paper/ venue:journal max_iterations:2` — shorter loop
- `/lunheng paper/ venue:journal stop_threshold:8.5` — higher quality bar
- `/lunheng paper/ venue:nature_sub` — Nature-style compression
- `/lunheng paper/ venue:journal skip_editor:true` — v1.0 compat mode (NOT RECOMMENDED)

## When to Use vs. `lunheng-quick`

- **`lunheng`** (this skill): paper needs structural restructuring + length calibration. Costs ~12–30 sub-agent calls per round.
- **`lunheng-quick`**: paper is structurally OK, just needs polish. 2 rounds, ~4–6 sub-agent calls total. (Also inherits v2.0 budget awareness.)

## Anti-patterns Lunheng v2.0 Prevents (learned from v1.0)

1. **"Answer every reviewer question in-text"** → v2.0 moves answers to SI
2. **"Expand Limitations to 6 enumerate points to hit D8 10-band"** → v2.0 D9 penalizes; Chief Editor flattens to prose
3. **"Add \paragraph{协议} for every method detail"** → v2.0 bans \paragraph by default
4. **"Broader Impact 1000+ chars to defend against Ethics reviewer"** → v2.0 hard-caps via budget
5. **"Every fix adds 300 words, no fix ever subtracts"** → v2.0 requires paired cuts
