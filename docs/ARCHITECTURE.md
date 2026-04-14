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
