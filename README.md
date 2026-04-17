# Lunheng (论衡)

> **Multi-agent paper review framework, anchored to top-tier journal rubrics.**
>
> Pure Claude / Claude Code skill — no extra API key required.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skill: Claude Code](https://img.shields.io/badge/Skill-Claude%20Code-blueviolet)]()
[![Status: Beta](https://img.shields.io/badge/Status-Beta-orange)]()

> *"权衡论证, 校释虚妄"* — 王充《论衡》(~80 CE)
>
> *"Weighing arguments, examining what is false"* — Wang Chong, *Lunheng*

---

## What is Lunheng?

Lunheng is a **multi-agent paper review and improvement framework** that turns Claude into a coordinated review committee. **Six specialist agents** (Architect, Evaluator-9, Writer, Refiner, **Chief Editor**, Aggregator) collaborate around a **persistent visual contract** AND a **word-budget contract** — shared JSON state that tracks figures, tables, terminology, cross-references, AND venue-appropriate length throughout the revision loop.

Distinguishing features:

- **Anchored 1–10 rubric across 9 dimensions** (8 original + **D9 Narrative & Conciseness**), mapped to actual NeurIPS 2025 / Nature / JACS reviewer practice (not generic categories).
- **Venue-aware word budgeting** — `journal` / `thesis` / `nature_sub` / `conference` profiles with enforced per-section char limits.
- **Chief Editor role** (v2.0) — enforces budget and narrative flow; can override Writer additions; prevents the "answer-every-reviewer-in-text" anti-pattern.
- **Every Evaluator proposes `cuts` paired with `fixes`** (v2.0) — no net additions without offsetting deletions.
- **NeurIPS-style 16-item Reproducibility Checklist** with chemistry/materials extensions.
- **Pure Claude sub-agents** — no third-party API key required.
- **Public case study** showing R0 → R3 trajectory on a real Q1-target manuscript.

### What's new in v2.0 (2026-04-14)

v1.0 produced technically polished but **overstuffed** papers — reviewers rewarded additions (expand Limitations to 6 items, add `\paragraph{Protocol}` for every method detail, pad Broader Impact to 1000+ chars). The composite score climbed, but the paper read like an FAQ rather than a coherent narrative. v2.0 fixes this with four structural changes:

1. **Required `venue` parameter** with hard word budgets (`journal` = 8-10k CN chars / 6-8k EN words; `nature_sub` = 2.5-3.5k; `thesis` = 15-30k)
2. **D9 Narrative & Conciseness** as the 9th evaluation dimension — penalizes overshoot, excess `\paragraph` small-headings, FAQ-style fragmentation
3. **Chief Editor role** inserted after Refiner — authority to override Writer; compresses to budget; moves method details to SI
4. **Mandatory `cuts` field** in every Evaluator YAML — each fix must be paired with a comparable-size cut unless the paper is under budget

See `skills/lunheng/SKILL.md` for full v2.0 workflow and anti-pattern catalogue.

### What's new in v2.1 (2026-04-17)

v2.0 shipped a robust budget/narrative framework, but a real-paper audit (a DAC-ML manuscript targeting a Q1 journal) uncovered **17 "placeholder" errors** where Writer agents had emitted specific numbers — subset sizes, enrichment factors, equations, units — that were **never verified against source data**. Representative cases:

- `B subset (n=2142)` — an experiment that was never run; the number came from `3555 × 60%` as a Writer shortcut for "the literature-only subset"
- `C subset (n=3591)` — a stray number from an early draft; the actual dataset had 3555 rows
- `Amine EF = 1.57` — Writer's pen-and-paper arithmetic (`50.4% / 32.1%`) while the real OOF value was `1.33`
- `CC backfill covers ~38%` — actual coverage was 2.6% (91 / 3555 rows)
- SI's Clausius–Clapeyron form written as equi-loading `ln P vs 1/T` when the code actually used van't Hoff equi-pressure `ln(q₁/q₂) vs 1/T`
- `N content (wt%)` in the main-text feature table, when the CSV column and SI both say `mmol/g`

v2.1 adds **numerical grounding** as a Writer hard constraint (HARD CONSTRAINT §8):

1. For **every** specific number / count / percentage / ratio, Writer must cite its source file path (e.g., `data/xxx.csv` row count, `output/yyy.json` field, computed from `zzz.npz`).
2. If the source is inaccessible → use qualitative language ("majority", "small fraction") OR tag `[VERIFY: <description>]` for Refiner / Chief Editor to resolve.
3. **Forbidden**: fabricating a specific count by multiplying total × rounded percentage (e.g., `3555 × 60% → 2142` presented in prose as if from a real experiment).
4. Writer output block must include a traceability section listing each number's source file.

This is a Writer-level patch — no workflow changes, no new agents, no new dimensions. v2.0 pipelines keep working; v2.1 just catches a category of fake-specific numbers that v1.0–v2.0 Writers had been generating without guard-rails.

See `skills/lunheng/SKILL.md` Writer HARD CONSTRAINTS §8 and Anti-patterns #6 for the exact prompt language.

## Why "Lunheng"?

The name comes from *Lunheng* (《论衡》), Wang Chong's ~80 CE treatise — the first systematic Chinese work on weighing evidence and refuting unsupported claims. Lunheng's job is the same: weigh every claim against the evidence the paper provides, and surface what is unsupported.

---

## Quick Start

### Install as a Claude Code / OpenClaw skill

**One-liner (any platform):**

```bash
git clone https://github.com/Yugenee/Lunheng.git && cd Lunheng && python install.py
```

The installer copies both `lunheng` and `lunheng-quick` skills to `~/.claude/skills/`. Run `python install.py --uninstall` to remove.

**Windows users** can also double-click `install.bat`. **macOS / Linux** users: `bash install.sh`.

**Manual install** (if you don't trust the script):

```bash
mkdir -p ~/.claude/skills
cp -r skills/lunheng ~/.claude/skills/
cp -r skills/lunheng-quick ~/.claude/skills/
```

### Run — basic

In Claude Code (or OpenClaw), invoke:

```
/lunheng <YOUR_PAPER_DIR>/
```

**`<YOUR_PAPER_DIR>` is the path to the directory that holds your manuscript** — it is a placeholder, not a literal name. Replace it with your actual directory name. The path can be relative (resolved against the Claude Code working directory) or absolute.

Examples — three users with three different directory layouts:

```
/lunheng paper_final/                                  # relative path, dir named "paper_final"
/lunheng my_thesis/                                    # dir named "my_thesis"
/lunheng D:/research/2026-q1/                          # absolute path on Windows
/lunheng ~/papers/dac_review/                          # absolute path on macOS/Linux
```

For example, if your project layout is:

```
my_paper/
├── main.tex             # ← the manuscript source
├── references.bib       # ← bibliography
└── figures/             # ← figures referenced by main.tex
    ├── Fig1.pdf
    └── Fig2.png
```

then call:

```
/lunheng my_paper/
```

Lunheng will auto-detect `main.tex` as the source, `references.bib` as the bibliography, and `figures/` as the asset directory. Auto-detection priority: `*.tex` (containing `\documentclass`) → `*.md` → `*.docx` → `*.pdf`.

### What happens, step by step

1. **Step 0 — Detect & init** (≈ 5 sec)
   The skill detects the format and creates `<paper_dir>/lunheng_workspace/` to hold all intermediate artifacts.

2. **Step 1 — Architect agent** (≈ 1–3 min, 1 sub-agent)
   Reads the entire manuscript and produces:
   - `lunheng_workspace/blueprint.md` — section-by-section argument outline + 3 most severe structural issues
   - `lunheng_workspace/visual_contract.json` — registry of every figure/table/term that downstream agents must respect

3. **Step 2 — Evaluator bench (Round 1)** (≈ 3–5 min, 8 sub-agents in parallel)
   Eight specialized evaluators score each dimension D1–D8 with anchored 1–10 scores. Composite $R_1 = \frac{1}{8} \sum D_k$ is computed.

4. **Step 3 — Generate-Evaluate-Adapt loop** (≈ 5–10 min per round, only for `tex`/`md`)
   - If $R \geq 7.0$ → **STOP** (paper is at borderline-accept quality).
   - If $R < 7.0$ → dispatch **Writer agents** (one per low-scoring section) and a **Refiner agent** (global polish), then re-run the Evaluator bench. Repeat up to 3 times.

5. **Step 4 — Compile & verify** (≈ 30 sec, only for `tex`/`md`)
   - LaTeX: `xelatex → bibtex → xelatex × 2`, then `grep "undefined"` must be 0
   - Markdown: optional `pandoc → pdf` for a visual check

6. **Step 5 — Visual contract validation**
   Verifies every label in the contract is actually defined and referenced.

7. **Step 6 — Document results**
   Writes `<paper_dir>/LUNHENG_LOG.md` with the complete score progression, per-round changes, and remaining issues.

### Expected output files

After a successful run on a `.tex` paper:

```
my_paper/
├── main.tex                          # ← REVISED in-place by Writer/Refiner
├── main.pdf                          # ← REGENERATED by xelatex
├── LUNHENG_LOG.md                    # ← NEW: full per-round score log
└── lunheng_workspace/
    ├── main_round0.tex               # snapshot of original
    ├── main_round0.pdf
    ├── blueprint.md                  # Architect's plan
    ├── visual_contract.json          # final contract state
    ├── round1_evaluators/            # 8 raw evaluator outputs
    └── round1_writer/                # Writer outputs (if loop ran)
```

For `.docx` / `.pdf` papers, `main.tex` is **not** modified; instead you get `LUNHENG_EDIT_LIST.md` with structured edit instructions to apply manually.

### Run — common variations

| Goal | Command |
|------|---------|
| Default review (auto-detect everything) | `/lunheng paper/` |
| Stricter quality bar (e.g. for top-tier venue) | `/lunheng paper/ — stop_threshold: 8.0` |
| Faster, only 2 rounds | `/lunheng paper/ — max_iterations: 2` |
| Pause for your approval before each round | `/lunheng paper/ — human_checkpoint: true` |
| Auto-detect picks wrong file | `/lunheng paper/ — main: my_paper.tex` |
| Force Word mode (review-only) | `/lunheng paper/ — format: docx` |
| Force PDF mode (read-only review) | `/lunheng paper/ — format: pdf` |
| Emphasize Nature criteria | `/lunheng paper/ — venue: nature` |
| Emphasize NeurIPS criteria | `/lunheng paper/ — venue: neurips` |

### Quick-polish mode

If your paper is structurally sound and you just want a writing/clarity sweep (no Architect, no Writer/Refiner split, single reviewer):

```
/lunheng-quick path/to/paper/
```

- 2 rounds, single reviewer per round
- ≈ 4 sub-agent calls total (vs. 13–25 for full `/lunheng`)
- Best when you want fast feedback before major revision

### Cost & timing reference

Based on the [DAC case study](examples/dac_paper_case_study.md) (28-page chemistry-ML paper):

| Mode | Sub-agent calls | Wall time | Tokens (Opus 4.6) |
|------|------------------|-----------|---------------------|
| Round 0 baseline only | 8 evaluators | ~5 min | ~40k |
| Full first round (Architect + Evaluators) | 9 | ~10 min | ~80k |
| Full revision round (Writer × N + Refiner + Evaluators) | 10–18 | ~15 min | ~120k |
| Quick-polish (`lunheng-quick`) | 4 | ~3 min | ~30k |

### Re-running on the same paper

You can run `/lunheng` repeatedly. Each call starts fresh:
- Archives the previous compiled PDF as `lunheng_workspace/main_round0.pdf`
- Re-detects format and main file (auto-detection runs again)
- Overwrites the previous workspace

This lets you iterate: get a review, manually apply some of the suggestions, then re-run to see the score change.

### Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `Unknown skill: lunheng` | Skill not installed | Run `python install.py` again, or check `~/.claude/skills/lunheng/` exists |
| `Auto-detect found no main file` | `<paper_dir>` is empty or no recognized format | Pin with `--main: filename.tex` or check the path |
| Evaluators run but Writer/Refiner is skipped | Format is `docx` or `pdf` (review-only by design) | Use `tex`/`md` for full pipeline, or use the edit list |
| LaTeX compile fails after revision | Writer introduced a syntax issue | Restore from `lunheng_workspace/main_round0.tex` and re-run with `--max_iterations: 0` to only review |
| Composite score doesn't improve between rounds | Some dimensions need experiments (e.g. external baselines) the agent can't fabricate | Lunheng will document the gap; you must run the actual experiments |

---

## Evaluation Rubric

**9 dimensions** (v2.0 adds D9 Narrative & Conciseness), each scored **1–10** with **anchored anchors** at four levels (1–3 / 4–6 / 7–8 / 9–10), plus an Overall verdict (1–6) and Confidence (1–5).

| Dimension | Aligned with |
|-----------|--------------|
| **D1. Soundness** | NeurIPS Soundness, Nature Technical Rigor |
| **D2. Significance & Originality** | NeurIPS Significance + Originality |
| **D3. Clarity & Organization** | NeurIPS Clarity, JACS Clarity |
| **D4. Experimental Substance** | NeurIPS Quality (claims supported) |
| **D5. Reproducibility** | NeurIPS 16-item Checklist |
| **D6. Citation Quality** | JACS Literature Appropriateness |
| **D7. Visual & Tabular Communication** | Nature Figure Quality |
| **D8. Ethics, Limitations & Broader Impact** | NeurIPS Limitations + Ethics |

📖 Full rubric with anchored examples → [docs/EVALUATION_RUBRIC.md](docs/EVALUATION_RUBRIC.md)

📋 Reproducibility checklist → [docs/REPRODUCIBILITY_CHECKLIST.md](docs/REPRODUCIBILITY_CHECKLIST.md)

🏗 Architecture & contract schema → [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

📄 Multi-format support (`.tex` / `.md` / `.docx` / `.pdf`) → [docs/MULTI_FORMAT.md](docs/MULTI_FORMAT.md)

---

## Supported Input Formats

| Format | Auto-detect | Evaluators | Architect | Writer/Refiner | Output |
|--------|-------------|------------|-----------|----------------|--------|
| `.tex` (LaTeX) | ✅ | ✅ | ✅ | ✅ in-place | revised `.tex` + `LUNHENG_LOG.md` |
| `.md` (Markdown) | ✅ | ✅ | ✅ | ✅ in-place | revised `.md` + `LUNHENG_LOG.md` |
| `.docx` (Word) | ✅ | ✅ | ✅ | edit-list only | `LUNHENG_EDIT_LIST.md` (apply manually) |
| `.pdf` (compiled) | ✅ | ✅ | ✅ | read-only | `LUNHENG_REVIEW.md` (scores + suggested fixes) |

LaTeX and Markdown get the **full pipeline** (multi-agent revision in-place). Word and PDF get **review-only** mode — a structured edit list the author applies. See [docs/MULTI_FORMAT.md](docs/MULTI_FORMAT.md) for full per-format behavior.

---

## Real Case Study

Lunheng was applied to a Chinese-language chemistry-ML manuscript (DAC sorbents prediction, Q1 target) over three rounds:

| Round | Composite Score | What changed |
|-------|-----------------|---------------|
| **R0** (baseline) | **6.89** | Original draft |
| **R3** (after gap fixes) | **8.04** | Targeted fixes per Lunheng's per-dimension `score_change_criteria` outputs (bootstrap CIs, hyperparameter table, Data Availability section, Broader Impact, table column-width fixes) |

📊 Full per-dimension breakdown → [examples/dac_paper_case_study.md](examples/dac_paper_case_study.md)

---

## Architecture in 60 Seconds

```
                Architect ──→ Blueprint + Visual Contract
                                       │
                ┌──────────────────────┼──────────────────────┐
                ▼                      ▼                      ▼
         Writer (per-section)   Refiner (global)      Evaluator Bench
         drafts under contract  polish + contract     (8 parallel agents,
                                update                 one per dimension)
                │                      │                      │
                └──────────────────────┴──────────────────────┘
                                       ▼
                              Aggregate R = Σ Dₖ / 8
                              R ≥ 7.0  →  STOP
                              R <  7.0  →  loop back
```

The **Visual Contract** is a JSON file persisting between agent calls. It carries:
- `global_visual_registry` — every figure/table with semantic description and obligated section
- `section_obligations` — which visuals MUST appear in each section
- `terminology_glossary` — canonical form for every key term
- `validation_rules` — unique-labels, all-visuals-referenced, etc.

This is the mechanism that prevents structural drift across multi-step revision. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the full schema.

---

## Installation Requirements

- [Claude Code CLI](https://claude.com/claude-code) ≥ 0.5 OR an equivalent Claude-agent harness
- A LaTeX distribution (MiKTeX / TeX Live) if you want PDF compilation
- Optional: `pandoc` if you want to also produce DOCX output

---

## Ethical Use

Lunheng is for **author-side self-review** — writers polishing their own papers before submission.

It is **NOT** for:
- Producing fake peer reviews
- Generating fabricated experimental results
- Bypassing journal peer-review processes
- Reviewer impersonation

The framework explicitly refuses to invent experimental data; it only flags missing experiments and suggests what to add.

---

## Roadmap

- [x] v0.1 — Skill files + 8-dim rubric + visual contract schema
- [x] v0.2 — Reproducibility checklist
- [x] v0.3 — DAC case study public artifact
- [x] v0.4 — Multi-format support (`.tex` / `.md` / `.docx` / `.pdf`)
- [ ] v0.5 — Venue-specific rubric profiles (`--venue=neurips/nature/jacs`)
- [ ] v0.6 — JSON schema validation for visual contract
- [ ] v0.7 — Telemetry hooks for review-quality monitoring
- [ ] v1.0 — Stable API + python wrapper for non-Claude-Code users

---

## Citation

If Lunheng helps your paper, please cite:

```bibtex
@software{lunheng2026,
  author = {Ding, Yujie},
  title  = {Lunheng: Multi-agent paper review framework anchored to top-tier journal rubrics},
  year   = {2026},
  url    = {https://github.com/Yugenee/Lunheng}
}
```

---

## License

[MIT](LICENSE) — free to use, modify, and redistribute. No warranty.

---
---

# Lunheng (论衡) — 中文版

> **多智能体学术论文审阅框架，对齐顶刊审稿标准。**
>
> 纯Claude / Claude Code skill — 无需额外API密钥。

> *"权衡论证, 校释虚妄"* — 王充《论衡》(~80 CE)

## 是什么

论衡是一个**契约约束的多智能体论文评审与改进框架**，把Claude变成一个协同工作的评审委员会。四类专业智能体（架构师 / 撰写者 / 润色者 / 评估者团）协同作业，共享一份**持久化视觉契约**——一个JSON状态记录所有图表、术语和交叉引用，在整个改稿循环中保持一致。

**特色**：
- **9维度 1–10 分锚定评分** (v2.0 新增 D9 叙事与精炼)，对齐NeurIPS 2025 / Nature / JACS 的真实审稿规范
- **Venue 感知字数预算** (v2.0): `journal` / `thesis` / `nature_sub` / `conference` 四种预设，按目标场景强约束总字数与小节字数
- **Chief Editor 角色** (v2.0): 在 Refiner 之后强制压到字数预算，防止 "每个审稿点都在正文里答复" 的反模式
- **数字真值约束** (v2.1): Writer 产出的每个数字/计数/百分比必须引用源文件路径，或用 `[VERIFY: ...]` 标签交给 Refiner 兜底；禁止 `总数 × 四舍五入百分比` 凑具体数
- **NeurIPS式16项可复现性清单**，含化学/材料学科扩展
- **纯Claude子代理**，不依赖第三方API
- **公开真实案例**：完整展示 R0→R3 在Q1论文上的轨迹

### v2.1 新增 (2026-04-17)

v2.0 的字数/叙事框架稳定跑了一段时间后，在一次真实论文审计 (DAC-ML 稿件) 中发现 **17 处 Writer 占位符错误**: Writer 为了让段落看起来"具体"，凭 `总数 × 四舍五入百分比` 造出 (1) 从未真正跑过的子集 `n=2142`、(2) 心算推出的 `EF=1.57`（真实 1.33）、(3) 与代码不符的 CC 方程形式、(4) 写错单位 (N 含量 `wt%` vs 实际 `mmol/g`) 等"看似具体但实际未核对"的数字。

v2.1 为 Writer 加一条硬约束:

1. 每个数字、计数、百分比、比率必须引用源文件路径 (`data/*.csv`, `output/*.json`, `*.npz`)
2. 无法访问源文件 → 用定性语言 ("多数"/"少数") 或 `[VERIFY: ...]` 标签交给 Refiner 兜底
3. 禁止 `总数 × 四舍五入百分比 → 具体 N` 的心算造假
4. Writer 输出块必须列每个数字的来源文件路径

这是 Writer 级别的 patch，不改变工作流或智能体数量。详见 `skills/lunheng/SKILL.md` Writer HARD CONSTRAINTS §8。

## 为什么叫"论衡"

王充《论衡》成书约公元80年，是中文世界第一部系统论述"权衡论据、校释虚妄"的著作。本框架的工作本质相同：把论文中的每个claim与其证据进行权衡，识别那些缺乏支撑的部分。

## 快速开始

**一行安装（跨平台）**：

```bash
git clone https://github.com/Yugenee/Lunheng.git && cd Lunheng && python install.py
```

安装脚本会把 `lunheng` 和 `lunheng-quick` 两个skill复制到 `~/.claude/skills/`。卸载用 `python install.py --uninstall`。

Windows用户也可以双击 `install.bat`；macOS/Linux 用 `bash install.sh`。

### 基本调用

在 Claude Code（或 OpenClaw）中：

```
/lunheng <你的论文目录>/
```

**`<你的论文目录>` 是论文所在目录的路径**——这是占位符，不是字面名字。替换为你实际的目录名。可以用相对路径（基于 Claude Code 当前工作目录）或绝对路径。

举例——三个用户的不同目录布局：

```
/lunheng paper_final/                                  # 相对路径，目录叫 paper_final
/lunheng my_thesis/                                    # 目录叫 my_thesis
/lunheng D:/research/2026-q1/                          # Windows 绝对路径
/lunheng ~/papers/dac_review/                          # macOS/Linux 绝对路径
```

例如项目结构：

```
my_paper/
├── main.tex             # ← 论文源
├── references.bib       # ← 参考文献
└── figures/             # ← main.tex 引用的图
    ├── Fig1.pdf
    └── Fig2.png
```

调用 `/lunheng my_paper/`，论衡会自动识别 `main.tex` 是源文件、`references.bib` 是bib、`figures/` 是图目录。自动检测优先级：`*.tex`（含 `\documentclass`）> `*.md` > `*.docx` > `*.pdf`。

### 执行流程（详细）

1. **Step 0 — 检测+初始化**（约5秒）
   检测格式，建立 `<paper_dir>/lunheng_workspace/` 存所有中间产物。
2. **Step 1 — 架构师**（约1-3分钟，1子代理）
   通读全文，产出 `blueprint.md`（论证大纲+3大结构问题）+ `visual_contract.json`（图表/术语注册表）
3. **Step 2 — Round 1 评估者团**（约3-5分钟，8并行子代理）
   按D1-D8锚定打分；综合 $R_1 = \frac{1}{8} \sum D_k$
4. **Step 3 — 改稿循环**（每轮5-10分钟，仅 `tex`/`md`）
   - $R \geq 7.0$ → **STOP**
   - $R < 7.0$ → 撰写者(每低分节1个)+润色者(全局)+再评估，最多3轮
5. **Step 4 — 编译验证**（约30秒，仅 `tex`/`md`）
   `xelatex → bibtex → xelatex × 2`，验证 `0 undefined refs`
6. **Step 5 — 视觉契约校验**：每个label都有定义且被引用
7. **Step 6 — 写日志** `<paper_dir>/LUNHENG_LOG.md`

### 输出文件

`.tex` 论文跑完后：

```
my_paper/
├── main.tex                          # ← 撰写者/润色者已就地修改
├── main.pdf                          # ← xelatex 重新生成
├── LUNHENG_LOG.md                    # ← 新增：完整评分日志
└── lunheng_workspace/
    ├── main_round0.tex               # 原稿快照
    ├── main_round0.pdf
    ├── blueprint.md                  # 架构师蓝图
    ├── visual_contract.json          # 最终契约
    ├── round1_evaluators/            # 8个评估者原始输出
    └── round1_writer/                # 撰写者输出（如循环触发）
```

`.docx`/`.pdf` 不会修改原稿；输出 `LUNHENG_EDIT_LIST.md` 由作者手动应用。

### 常用变种调用

| 目标 | 命令 |
|------|------|
| 默认评审（自动检测） | `/lunheng paper/` |
| 顶刊更严标准 | `/lunheng paper/ — stop_threshold: 8.0` |
| 只跑2轮加快 | `/lunheng paper/ — max_iterations: 2` |
| 每轮等你确认再继续 | `/lunheng paper/ — human_checkpoint: true` |
| 指定主文件（自动选错时） | `/lunheng paper/ — main: my_paper.tex` |
| 强制Word模式（仅评不改） | `/lunheng paper/ — format: docx` |
| 强制PDF模式（只读评审） | `/lunheng paper/ — format: pdf` |
| Nature 标准侧重 | `/lunheng paper/ — venue: nature` |
| NeurIPS 标准侧重 | `/lunheng paper/ — venue: neurips` |

### 快速润色模式

论文结构已成型，只需文字打磨：

```
/lunheng-quick path/to/paper/
```

- 2轮，每轮单评审者
- 共约4子代理调用（vs `/lunheng` 13-25个）
- 适合大改前先要快速反馈

### 成本与耗时（基于 [DAC 案例研究](examples/dac_paper_case_study.md)）

| 模式 | 子代理数 | 墙钟时间 | tokens (Opus 4.6) |
|------|---------|---------|-------------------|
| 仅Round 0基线 | 8评估者 | ~5分钟 | ~40k |
| 完整首轮（架构师+评估者） | 9 | ~10分钟 | ~80k |
| 完整改稿轮（撰写者+润色者+评估者） | 10-18 | ~15分钟 | ~120k |
| 快速润色 | 4 | ~3分钟 | ~30k |

### 重复运行

可在同一论文上反复调 `/lunheng`，每次fresh start：自动归档上轮PDF，重新检测，覆盖workspace。允许"评审→手动改→再评"的迭代工作流。

### 故障排查

| 症状 | 原因 | 修复 |
|------|------|------|
| `Unknown skill: lunheng` | skill未安装 | 跑 `python install.py`，或检查 `~/.claude/skills/lunheng/` |
| `Auto-detect found no main file` | 目录为空或格式不识别 | 用 `--main: filename.tex` 指定 |
| 评估者跑了但撰写者被跳过 | format 是 `docx`/`pdf`（设计上仅评不改） | 用 `tex`/`md` 走完整流程，或按 edit list 手动改 |
| 改稿后LaTeX编译失败 | 撰写者引入语法bug | 从 `lunheng_workspace/main_round0.tex` 恢复，加 `--max_iterations: 0` 仅评审 |
| 评分多轮不涨 | 某些维度需实际实验agent无法伪造 | 论衡会标记gap，需主人自己跑 |

## 8 维评分体系

每维度 **1–10 分制**，4个分数段都有锚点描述（1–3 / 4–6 / 7–8 / 9–10），加 Overall verdict (1–6) 与 Confidence (1–5)。

| 维度 | 对齐顶刊标准 |
|------|-------------|
| **D1. 方法严谨性** | NeurIPS Soundness, Nature Technical Rigor |
| **D2. 重要性与原创性** | NeurIPS Significance + Originality |
| **D3. 清晰度与组织** | NeurIPS Clarity, JACS Clarity |
| **D4. 实验充分性** | NeurIPS Quality |
| **D5. 可复现性** | NeurIPS 16项清单 |
| **D6. 引用质量** | JACS Literature Appropriateness |
| **D7. 图表沟通** | Nature Figure Quality |
| **D8. 伦理/局限/影响** | NeurIPS Limitations + Ethics |

## 支持的输入格式

| 格式 | 自动检测 | 评估者 | 架构师 | 撰写者/润色者 | 输出 |
|------|---------|-------|-------|--------------|------|
| `.tex` (LaTeX) | ✅ | ✅ | ✅ | ✅ in-place | 改稿 `.tex` + `LUNHENG_LOG.md` |
| `.md` (Markdown) | ✅ | ✅ | ✅ | ✅ in-place | 改稿 `.md` + `LUNHENG_LOG.md` |
| `.docx` (Word) | ✅ | ✅ | ✅ | 仅给清单 | `LUNHENG_EDIT_LIST.md`（手动应用） |
| `.pdf` (已编译) | ✅ | ✅ | ✅ | 只读 | `LUNHENG_REVIEW.md`（评分+修复建议） |

LaTeX 和 Markdown 走**完整流水线**（多智能体原地改稿）。Word 和 PDF 走**只评不改**模式——结构化建议清单由作者手动应用。详见 [docs/MULTI_FORMAT.md](docs/MULTI_FORMAT.md)。

## 真实案例

将论衡应用于一篇中文化学-机器学习论文（DAC吸附材料预测，目标Q1期刊）：

| 轮次 | 综合分 | 关键变化 |
|------|--------|---------|
| **R0**（基线） | **6.89** | 原始草稿 |
| **R3**（修补缺口后） | **8.04** | 按论衡 per-dimension `score_change_criteria` 针对性修复（bootstrap CI、超参表、数据可用性、Broader Impact、表格列宽） |

## 视觉契约（核心机制）

**视觉契约（Visual Contract）** 是一份在所有agent调用之间持久化的JSON文件，包含：
- `global_visual_registry` — 每张图/表的语义描述与预期所属章节
- `section_obligations` — 每节必须包含哪些视觉元素
- `terminology_glossary` — 每个关键术语的标准形式
- `validation_rules` — unique-labels / all-visuals-referenced 等

这是防止多步改稿过程中"结构漂移"的核心机制。

## 伦理使用声明

论衡用于**作者自审**——写作者在投稿前自己打磨论文。**不得用于**伪造同行评审、生成虚假实验数据、绕过peer-review、冒充审稿人。框架明确拒绝编造实验数据；仅指出缺失的实验并建议补充方向。

## 协议

[MIT](LICENSE) — 自由使用、修改、再分发。无担保。

