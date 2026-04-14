# Lunheng vs. Related Frameworks

A side-by-side comparison of Lunheng with three of the most relevant existing tools: the original **Story2Proposal**, AgentAlpha's predecessor **Idea2Paper**, and Sakana's **AI Scientist v2**.

## Summary Table

| Aspect | Lunheng | Story2Proposal | Idea2Paper | AI Scientist v2 |
|--------|---------|----------------|------------|-----------------|
| **License** | MIT (open) | Paper only | Open | Open |
| **Backend** | Claude only | GPT/Claude/Gemini/Qwen | OpenAI-compatible | OpenAI |
| **Goal** | Improve existing paper | Generate manuscript from idea | Generate manuscript from idea | Run experiments + write paper end-to-end |
| **Core mechanism** | Visual contract + 4 agents + 8 evaluators | Visual contract + 4 agents | Multi-agent + KG | Tree search + 6+ agents |
| **Scoring** | 1–10 anchored × 8 dims, mapped to NeurIPS/Nature/JACS | 1–10 generic × 8 dims | Generic | None public |
| **Reproducibility checklist** | NeurIPS 16-item + chemistry | None | None | None |
| **Cost per run** | 10–30 sub-agent calls | Variable | Multi-stage | Many hours of compute |
| **Open-source code** | ✅ This repo | ❌ Paper only | ✅ Predecessor only | ✅ Different focus |

## Detailed Differences

### vs. Story2Proposal (the parent framework)

Lunheng **re-implements** Story2Proposal's contract-governed multi-agent design, but extends it in three concrete ways:

#### 1. Anchored, venue-aligned rubric

Story2Proposal uses 8 generic categories (Structural integrity / Writing clarity / Methodological rigor / Experimental substance / Citation hygiene / Reproducibility / Formatting stability / Visual communication). Each scored loosely 1–10.

Lunheng renames and **anchors** them to actual top-tier reviewer practice:

| Story2Proposal | Lunheng | Anchor source |
|----------------|---------|----------------|
| Structural integrity | (folded into D3 Clarity & D7 Visual) | — |
| Writing clarity | D3 Clarity & Organization | NeurIPS Clarity, JACS Clarity |
| Methodological rigor | D1 Soundness | NeurIPS Soundness, Nature Technical Rigor |
| Experimental substance | D4 Experimental Substance | NeurIPS Quality |
| Citation hygiene | D6 Citation Quality | JACS Literature Appropriateness |
| Reproducibility | D5 Reproducibility | NeurIPS 16-item Checklist |
| Formatting stability | (folded into D7) | — |
| Visual communication | D7 Visual & Tabular Communication | Nature Figure Quality |
| (NEW) | D2 Significance & Originality | NeurIPS Significance + Originality |
| (NEW) | D8 Ethics, Limitations & Broader Impact | NeurIPS Limitations + Ethics |

The two new dimensions matter because:
- **D2** is what gets papers desk-rejected at top venues regardless of execution quality
- **D8** is what NeurIPS introduced as mandatory in 2021 and Nature emphasizes for medical/AI papers

#### 2. Pure Claude implementation

Story2Proposal evaluated GPT/Claude/Gemini/Qwen as backbones (achieving 6.145 with the best). Lunheng commits to Claude-only, with two consequences:

- ✅ No external API key needed beyond what Claude Code already requires
- ✅ Sub-agents inherit the host's authentication
- ⚠️ Cannot benefit from cross-backbone diversity (mitigated by spawning agents in fresh contexts to simulate diversity)

#### 3. Public reference implementation + case study

Story2Proposal source code was not released as of v0.1 of Lunheng (only the paper PDF in [Idea2Paper repo](https://github.com/AgentAlphaAGI/Idea2Paper)). Lunheng is the first open-source implementation following Story2Proposal's architectural design, with a public case study showing R0 → R2 trajectory on a real Q1-target paper.

### vs. Idea2Paper (the predecessor by the same team)

Idea2Paper focuses on the **other half of the pipeline**: turning a research idea into a manuscript skeleton via a Knowledge Graph + multi-agent approach. The two are complementary:

```
Idea → [Idea2Paper] → Draft → [Lunheng] → Polished manuscript
```

Lunheng makes no attempt to generate content from scratch; it only improves existing manuscripts. If you want both phases, run Idea2Paper first to get a draft, then Lunheng to polish.

### vs. AI Scientist v2 (Sakana)

Different problem entirely. AI Scientist v2 runs experiments AND writes papers end-to-end via agentic tree search. It is much more ambitious, more compute-intensive, and harder to direct.

Lunheng's scope is narrower: the user provides a draft (and the experiments behind it), and Lunheng improves the writing/structure/reproducibility of that draft. Use AI Scientist if you want autonomous research; use Lunheng if you want author-side polish.

## When to Choose What

| Need | Use |
|------|-----|
| Polish a near-final manuscript | **Lunheng** |
| Quick clarity sweep on a finished draft | **Lunheng-quick** |
| Generate a draft from a research idea | Idea2Paper |
| Generate experiments + paper end-to-end | AI Scientist v2 |
| Build a custom multi-agent stack from scratch | Story2Proposal (study the paper) |

## Acknowledgments

Lunheng would not exist without:

- **AgentAlpha** for the Story2Proposal design pattern that this framework re-implements
- **NeurIPS Program Chairs** for publishing transparent reviewer guidelines
- **JACS / Nature editorial teams** for clear submission and review criteria
