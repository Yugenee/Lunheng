# Lunheng (论衡)

> **Multi-agent paper review framework, anchored to top-tier journal rubrics.**
>
> Pure Claude / Claude Code skill — no OpenAI key required.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skill: Claude Code](https://img.shields.io/badge/Skill-Claude%20Code-blueviolet)]()
[![Status: Beta](https://img.shields.io/badge/Status-Beta-orange)]()

> *"权衡论证, 校释虚妄"* — 王充《论衡》(~80 CE)
>
> *"Weighing arguments, examining what is false"* — Wang Chong, *Lunheng*

---

## What is Lunheng?

Lunheng is a **multi-agent paper review and improvement framework**. It treats your manuscript as a contract-governed system: four specialist agents (Architect, Writer, Refiner, Evaluator-bench) coordinate around a **persistent visual contract** that tracks figures, tables, terminology, and cross-references.

It is a Claude-native re-implementation and *extension* of the [Story2Proposal](https://arxiv.org/abs/2603.27065) framework (AgentAlpha 2026). The key extensions:

- **Anchored 1–10 rubric across 8 dimensions**, mapped to actual NeurIPS 2025 / Nature / JACS reviewer practice (not generic categories)
- **NeurIPS-style 16-item Reproducibility Checklist** (with chemistry/materials extensions)
- **Pure Claude sub-agents** — no OpenAI/Codex MCP dependency
- **Public case study** showing R0 → R2 trajectory on a real Q1-target paper

---

## Why "Lunheng"?

The name is taken from *Lunheng* (《论衡》), Wang Chong's ~80 CE treatise — the first systematic Chinese work on weighing evidence and refuting unsupported claims. The framework's job is the same: weigh every claim against the evidence the paper provides, and surface what is unsupported.

---

## Quick Start

### As a Claude Code / OpenClaw skill

```bash
# Copy the skill into your skills directory
cp -r skills/lunheng ~/.claude/skills/
cp -r skills/lunheng-quick ~/.claude/skills/
```

Then in Claude Code:

```
/lunheng path/to/your/paper/
```

The skill will:
1. **Architect** the paper (1 sub-agent) → Blueprint + Visual Contract
2. **Evaluate** on 8 dimensions in parallel (8 sub-agents) → composite score $R_0$
3. **Loop**: if $R < 7.0$, dispatch Writer + Refiner agents to revise, then re-evaluate
4. **Stop** when $R \geq 7.0$ or after 3 iterations
5. **Document** in `LUNHENG_LOG.md` with full per-round changelog

### Quick polish only

If your paper is structurally sound and only needs a writing pass:

```
/lunheng-quick path/to/paper/
```

This is a single-reviewer 2-round loop (~4 sub-agent calls total).

---

## Evaluation Rubric

8 dimensions, each scored **1–10** with **anchored anchors** at four levels (1–3 / 4–6 / 7–8 / 9–10), plus an Overall verdict (1–6) and Confidence (1–5).

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

---

## Real Case Study

Lunheng was applied to a Chinese-language chemistry-ML manuscript (DAC sorbents prediction, Q1 target) over three rounds:

| Round | Composite Score | What changed |
|-------|-----------------|---------------|
| **R0** (baseline) | **6.81** | Original draft |
| **R1** | **8.04** | +1.23 — formatting + visual fixes (figures inlined, citations resolved, terminology unified) |
| **R2** | **8.66** | +0.62 — content (statistical assumption disclosure, hyperparameter tables, ablation moved to main text) |

For comparison, [Story2Proposal's reported scores](https://arxiv.org/abs/2603.27065):
- DirectChat single-shot: **3.96**
- Story2Proposal (mixed backbones): **6.15**

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

## Comparison to Other Tools

| Tool | Backend | Output | Multi-agent | Visual Contract | Anchored Rubric |
|------|---------|--------|--------------|-----------------|-----------------|
| **Lunheng** (this) | Claude only | Annotated revision + 8-dim scores | ✅ 4 + 8 | ✅ | ✅ NeurIPS/Nature/JACS |
| Story2Proposal (paper) | Mixed | LaTeX manuscript | ✅ 4 | ✅ | ❌ generic 8 categories |
| `auto-paper-improvement-loop` | GPT-5.4 via Codex | Revised paper | ❌ single | ❌ | ❌ free-form |
| AI Scientist v2 | OpenAI | End-to-end paper | ✅ tree search | ❌ | ❌ |
| PaperOrchestra (Google) | Mixed | Submission-ready | ✅ | ✅ visual contract | ❌ generic |

---

## Installation

### Requirements
- [Claude Code CLI](https://claude.com/claude-code) ≥ 0.5 OR [OpenClaw](https://github.com/openclaw)
- A LaTeX distribution (MiKTeX / TeX Live) if you want PDF compilation
- Optional: `pandoc` if you want to also produce DOCX output

### Setup

```bash
git clone https://github.com/<your-user>/Lunheng.git
cd Lunheng

# Install both skills
mkdir -p ~/.claude/skills
cp -r skills/lunheng ~/.claude/skills/
cp -r skills/lunheng-quick ~/.claude/skills/
```

Verify in Claude Code:

```
/lunheng paper/        # full multi-agent review
/lunheng-quick paper/  # quick polish
```

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
- [x] v0.2 — Reproducibility checklist (NeurIPS-style)
- [x] v0.3 — DAC case study public artifact
- [ ] v0.4 — Venue-specific rubric profiles (`--venue=neurips/nature/jacs`)
- [ ] v0.5 — JSON schema validation for visual contract
- [ ] v0.6 — Prometheus integration for review-quality monitoring
- [ ] v1.0 — Stable API + python wrapper for non-Claude-Code users

---

## Citation

If Lunheng helps your paper, please cite:

```bibtex
@software{lunheng2026,
  author = {Ding, Yujie},
  title  = {Lunheng: Multi-agent paper review framework anchored to top-tier journal rubrics},
  year   = {2026},
  url    = {https://github.com/<your-user>/Lunheng},
  note   = {A Claude-native re-implementation and extension of Story2Proposal (AgentAlpha 2026, arXiv:2603.27065)}
}
```

And cite the original Story2Proposal paper this work builds on:

```bibtex
@article{story2proposal2026,
  title  = {Story2Proposal: A Scaffold for Structured Scientific Paper Writing},
  author = {AgentAlpha Team},
  year   = {2026},
  eprint = {2603.27065},
  archivePrefix = {arXiv}
}
```

---

## License

[MIT](LICENSE) — free to use, modify, and redistribute. No warranty.

---

## Acknowledgments

- **AgentAlpha** for the original Story2Proposal framework that this work re-implements
- **wanshuiyin/ARIS** for the lightweight skill-based architecture pattern
- **Anthropic** for Claude Code and the Agent tool
- All readers who reviewed and improved this README
