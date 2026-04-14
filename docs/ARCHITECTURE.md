# Lunheng Architecture

## Design Premise

Lunheng treats paper improvement as a **contract-governed multi-agent process** rather than free-form generation. This addresses three predictable failure modes of single-agent paper improvement:

1. **Structural drift** — sections lose argumentative coherence as the agent forgets early decisions.
2. **Figure-text misalignment** — figures referenced without descriptive context, or described without referencing.
3. **Cross-section inconsistency** — terminology, claims, or notation that contradict between sections.

The remedy is a persistent JSON contract carried *between* sub-agent invocations, plus four specialist roles that coordinate around it.

## The Four Roles

```
                        ┌─────────────────────────┐
                        │   Architect (A_arch)    │
                        │  Reads paper → produces │
                        │   Blueprint + Contract  │
                        └────────┬────────────────┘
                                 │
                                 ▼
                ┌────────────────────────────────────┐
                │   Visual Contract (persistent)     │
                │   - global_visual_registry         │
                │   - section_obligations            │
                │   - terminology_glossary           │
                │   - validation_rules               │
                └────┬─────────────────────────┬─────┘
                     │                         │
                     ▼                         ▼
       ┌──────────────────────┐   ┌──────────────────────┐
       │  Writer (A_w) × N    │   │ Refiner (A_ref)      │
       │  per-section drafts  │   │ global consistency   │
       │  under contract      │   │ + contract update    │
       └──────────┬───────────┘   └──────────┬───────────┘
                  │                          │
                  └──────────┬───────────────┘
                             ▼
            ┌────────────────────────────────────┐
            │   Evaluator Bench (E_1 ... E_8)    │
            │   8 parallel sub-agents,           │
            │   each scoring one dimension       │
            └────────┬───────────────────────────┘
                     │
                     ▼
              Aggregate R = Σ D_k / 8
              ↓
              R ≥ 7.0 ?  → STOP
              R <  7.0 ?  → loop back
```

## Why a Visual Contract?

Single-agent LLM paper improvement collapses on long manuscripts because the model must hold the entire paper in working memory; later edits forget early decisions. Lunheng spawns **fresh-context sub-agents** for each task, so the contract is the *only* mechanism that keeps the team coherent across calls.

The contract enforces three guarantees:

- Every figure has an obligated section, a description, and an actual-references log
- Every term has one and only one canonical form across the manuscript
- Every `\ref{label}` resolves; every defined label is referenced

## Visual Contract Schema

```jsonc
{
  "global_visual_registry": [
    {
      "label": "fig:workflow",
      "type": "figure",
      "file": "figures/Fig1_workflow.png",
      "semantic_description": "End-to-end pipeline: data → features → model → analysis",
      "expected_section": "data_methods",
      "actual_references": ["data_methods:p1"]   // populated by Refiner
    },
    {
      "label": "tab:performance",
      "type": "table",
      "semantic_description": "Cross-validation performance of the ensemble model",
      "expected_section": "results",
      "actual_references": []
    }
  ],

  "section_obligations": {
    "intro": [],
    "data_methods": ["fig:workflow", "fig:overview", "tab:features"],
    "results": ["tab:performance", "fig:pred_vs_actual", "fig:noise_floor"],
    "interpretability": ["fig:shap_composite", "fig:shap_parallel"],
    "discussion": []
  },

  "terminology_glossary": {
    "辅助域": "→ use 'broad-domain CO2 isotherm data' / '广域CO2等温线'",
    "GroupKFold": "use 'GroupKFold' in body, 'GKF' allowed only in tables/figures",
    "ρ": "first occurrence: 'Spearman rank correlation coefficient ρ'"
  },

  "validation_rules": {
    "unique_labels": true,
    "all_visuals_referenced": true,
    "all_references_resolved": true,
    "caption_text_alignment_min_score": 7
  }
}
```

## The Three-Phase Loop

### Phase 1 — Architect (one-shot)

The Architect reads the entire manuscript and produces:
- `blueprint.md` — section-by-section argument outline + identified issues
- `visual_contract.json` — populated registry, obligations, glossary

**Cost:** ~1 sub-agent call.

### Phase 2 — Writer & Refiner (per-section)

For each section flagged for revision:
- Spawn a **Writer** sub-agent with `(section_text, blueprint_section, contract)` → improved section
- After all sections re-drafted, spawn a **Refiner** with the full draft + contract → polished manuscript + updated contract

**Cost:** N + 1 sub-agent calls (N sections + 1 refiner).

### Phase 3 — Evaluators (parallel)

All 8 evaluators are spawned **in a single message** with parallel tool calls:
- Each gets `(refined_manuscript, visual_contract, dimension_rubric)`
- Each returns `{score, confidence, strengths, weaknesses, fixes, score_change_criteria}`

Aggregate: $R = \frac{1}{8} \sum D_k$.

**Cost:** 8 parallel sub-agent calls.

## Convergence Criterion

$$
\text{stop if } R \geq 7.0 \text{ OR } \text{iteration} \geq \text{MAX\_ITERATIONS (default 3)}
$$

Empirically (case study: see [examples/dac_paper_case_study.md](../examples/dac_paper_case_study.md)):
- Round 1 fixes formatting + visual issues (high gain: typically +1.0 to +2.0 in $R$)
- Round 2 addresses content (statistical rigor, missing baselines, citation completeness; +0.5 to +1.0)
- Round 3 polishes (diminishing returns: +0.2 to +0.4)

## Why Multi-Agent Beats Single-Reviewer

We compare Lunheng to a **single-Claude-agent baseline** (`lunheng-quick`) on the same manuscript:

| Approach | Mechanism | DAC Paper Round 1 Score |
|----------|-----------|--------------------------|
| Single Claude (lunheng-quick) | One review → fix → re-review | 7.6 / 10 |
| **Lunheng (full)** | 4 specialist + 8 evaluator agents + visual contract | **8.04 / 10** |

The contract-governed multi-agent approach catches structural issues (e.g., dangling phantom tables, terminology drift across sections) that a single reviewer often misses because it must hold the entire paper in working memory.

---
---

# 架构（中文版）

## 设计理念

论衡把论文改进视为**契约约束的多智能体过程**而非自由生成。这一设计针对单智能体改稿的三大可预测失败模式：

1. **结构漂移**——agent 改后忘了前面的决定，章节失去论证连贯性
2. **图文错位**——图被引用但缺少上下文，或被描述但未被引用
3. **跨章节不一致**——术语、claim、记号在不同章节互相矛盾

解药是在 sub-agent 调用之间携带一份持久化 JSON 契约，加上四类围绕该契约协同的专业角色。

## 四个角色

```
                        ┌─────────────────────────┐
                        │   架构师 (A_arch)        │
                        │  读论文 → 产出蓝图+契约   │
                        └────────┬────────────────┘
                                 │
                                 ▼
                ┌────────────────────────────────────┐
                │   视觉契约（持久化 JSON）            │
                │   - global_visual_registry         │
                │   - section_obligations            │
                │   - terminology_glossary           │
                │   - validation_rules               │
                └────┬─────────────────────────┬─────┘
                     │                         │
                     ▼                         ▼
       ┌──────────────────────┐   ┌──────────────────────┐
       │  撰写者 (A_w) × N     │   │ 润色者 (A_ref)        │
       │  契约约束的           │   │ 全局一致性             │
       │  per-section草稿      │   │ + 契约更新            │
       └──────────┬───────────┘   └──────────┬───────────┘
                  │                          │
                  └──────────┬───────────────┘
                             ▼
            ┌────────────────────────────────────┐
            │   评估者团 (E_1 ... E_8)            │
            │   8 个并行子代理，每个评一维         │
            └────────┬───────────────────────────┘
                     │
                     ▼
              聚合 R = Σ D_k / 8
              ↓
              R ≥ 7.0 ?  → 停止
              R <  7.0 ?  → 循环
```

## 为什么需要视觉契约

单智能体在长论文上必然崩溃，因为它必须把整篇论文塞进工作记忆；后续编辑会忘记早期决定。论衡为每个任务派发**全新上下文的 sub-agent**，所以契约是跨调用保持团队连贯的**唯一**机制。

契约强制三大保证：
- 每张图都有"必须出现的章节、语义描述、被引用日志"
- 每个术语在全文只有一个标准形式
- 每个 `\ref{label}` 都能解析；每个定义的 label 都被引用过

## 三阶段循环

### 阶段 1 — 架构师（一次性）
读全文，产出 `blueprint.md`（论证大纲+识别问题）+ `visual_contract.json`（注册表/义务/术语表）。**成本：1 次 sub-agent 调用。**

### 阶段 2 — 撰写者 & 润色者（per-section）
对每个待修章节：派发 Writer 子代理改写 → 全部完成后派发 Refiner 全局抛光+更新契约。**成本：N+1 次调用。**

### 阶段 3 — 评估者团（并行）
**单条消息中并行启动 8 个 evaluator**，每个返回 `{score, confidence, strengths, weaknesses, fixes, score_change_criteria}`。聚合 $R = \frac{1}{8} \sum D_k$。**成本：8 次并行调用。**

## 收敛条件

$$ \text{停止条件: } R \geq 7.0 \text{ 或 } \text{iteration} \geq \text{MAX\_ITERATIONS（默认 3）} $$

经验值（参见案例研究）：
- 第 1 轮修排版+视觉问题（高增益：+1.0 到 +2.0）
- 第 2 轮修内容（统计严谨性、缺失 baseline、引用完整性；+0.5 到 +1.0）
- 第 3 轮抛光（边际递减：+0.2 到 +0.4）

## 多智能体为什么打败单评审

| 方法 | 机制 | DAC 论文 R1 综合分 |
|------|------|-------------------|
| 单 Claude（lunheng-quick） | 一评 → 一改 → 重评 | 7.6 / 10 |
| **论衡（full）** | 4 专业 + 8 评估代理 + 视觉契约 | **8.04 / 10** |

契约约束的多智能体方法能捕获单评审者常常错过的结构问题（如悬空幻影表、跨章节术语漂移），因为单评审者必须在工作记忆里同时持有整篇论文。

