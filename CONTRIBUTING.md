# Contributing to Lunheng

Thanks for considering a contribution! Lunheng is a Claude-native research tool, so most contributions fall into a few clear categories.

## What I Welcome

### 🎯 Rubric Refinements
The 8-dimension rubric in [`docs/EVALUATION_RUBRIC.md`](docs/EVALUATION_RUBRIC.md) is anchored to NeurIPS / Nature / JACS practice. If you have:
- A concrete venue rubric I missed (Science, Cell, ICML, etc.)
- A field-specific anchor that should be added (medical, social science, theoretical CS...)
- A red-flag pattern that catches something the current rubric misses

→ Open a PR editing the rubric markdown with the change + a paragraph of justification.

### 📋 Reproducibility Checklist Extensions
The current checklist mostly covers ML/computational papers + chemistry add-ons. I welcome additions for:
- Biology / wet-lab reproducibility (cell lines, antibodies, sequencing pipelines)
- HCI / user studies (sample size, IRB, replication packages)
- Theory papers (proof verification, computer-checked proofs)

→ PR to [`docs/REPRODUCIBILITY_CHECKLIST.md`](docs/REPRODUCIBILITY_CHECKLIST.md) with the new section.

### 🧪 Case Studies
Real papers run through Lunheng with permission to share are extremely valuable. If you used Lunheng on a real paper and can share (anonymized OK):
- The R0/R1/R2 score trajectory
- One or two key fixes the framework caught
- A reflection paragraph: where it helped most, where it missed

→ Add a markdown file under [`examples/`](examples/) following the pattern of `dac_paper_case_study.md`.

### 🔧 Skill Improvements
The skills under [`skills/`](skills/) are markdown-only by design. Improvements welcome:
- Better prompts for the Architect / Writer / Refiner / Evaluator agents
- Better stop-condition logic
- Better state-recovery on context-window compaction

→ PR to the relevant `SKILL.md`. Include before/after composite scores on a test paper if possible.

### 🌍 Translations
Right now we have English (`README.md`) and Chinese (`README_CN.md`). I'd welcome:
- Other major languages (Japanese, Korean, Spanish, French, German)
- Translation of `docs/EVALUATION_RUBRIC.md` so non-English authors can use it directly

## What I'd Rather Not Merge

- **Adding non-Claude backends** as the primary path. The point of Lunheng is to be Claude-native; if you want a multi-backend version, please fork.
- **Generating fake reviews** or **fabricating data** — these violate the framework's stated ethical scope. PRs that enable this will be closed without comment.
- **Unscoped expansions** ("let's also write the paper for the user") — Lunheng is review/improvement, not generation.

## Process

1. Open an issue describing what you want to add or change
2. Once we agree on scope, fork → branch → PR
3. PR description should include: motivation, what changed, how it was tested
4. I aim to respond to issues/PRs within 7 days

## Code of Conduct

Standard: be kind, be specific, prefer concrete examples over abstract criticism.

## Author

Yujie Ding · 中国石油大学（北京）克拉玛依校区
