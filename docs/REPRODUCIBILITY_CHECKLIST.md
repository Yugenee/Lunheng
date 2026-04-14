# Lunheng Reproducibility Checklist

Adapted from the NeurIPS 2025 Paper Checklist, with extensions for chemistry/materials/physics papers. Each item is scored **Yes / Partial / No / N/A**.

A composite reproducibility score $D_5$ on the [main rubric](EVALUATION_RUBRIC.md):
- **9–10**: ≥ 14 of the 16 applicable items satisfied
- **7–8**: 11–13 satisfied
- **4–6**: 7–10 satisfied
- **1–3**: ≤ 6 satisfied

---

## Section A: Claims & Limitations

### A1. Claims–Abstract Alignment
> Do the claims in the abstract and introduction accurately reflect the paper's contributions and scope?

**Pass criteria:** Abstract claims are not stronger than what the experiments support. No "we prove" when only empirical evidence is given.

### A2. Limitations Section
> Does the paper include a Limitations section addressing assumptions, robustness violations, and failure modes?

**Pass criteria:** Distinct paragraph or subsection. Lists at least 3 concrete limitations. Not just "future work."

### A3. Theory Assumptions and Proofs
> Are theoretical results stated with full assumptions and complete proofs?

**Pass criteria:** Every theorem/proposition has explicit assumptions. Proofs in main text or appendix. **N/A** for purely empirical papers.

---

## Section B: Methodology Detail

### B1. Mathematical / Algorithmic Description
> Is the algorithm/model described with sufficient detail to be reimplemented?

**Pass criteria:** Pseudo-code, equations, or precise prose enabling reimplementation by an expert.

### B2. Hyperparameter Disclosure
> Are all hyperparameters reported with their search ranges and final values?

**Pass criteria:** Table or supplementary list of every hyperparameter. Search ranges declared. **Best values explicitly given** (not just "tuned via Optuna").

### B3. Train/Validation/Test Splits
> Are data splits exactly specified (sizes, random seeds, split criteria)?

**Pass criteria:** Sizes given. Splitting criteria documented (random / stratified / GroupKFold / temporal). Reproducible (seed or scripted).

### B4. Preprocessing Pipeline
> Is the preprocessing pipeline (cleaning, feature engineering, normalization) reproducible?

**Pass criteria:** Each step described or scripted. Decisions justified ("we removed X because Y").

---

## Section C: Experimental Setup

### C1. Statistical Significance
> Are error bars / CIs / standard deviations reported on main results?

**Pass criteria:** Mean ± SD or 95% CI on table values. Number of seeds/runs disclosed.

### C2. Multiple Comparisons
> If multiple methods/conditions are compared, is the multiplicity adjustment described?

**Pass criteria:** Bonferroni / Holm / FDR / paired t-test stated. **N/A** if only one comparison.

### C3. Compute Resources
> Is the compute budget (hardware, hours, memory) disclosed?

**Pass criteria:** GPU/CPU model, training time, memory peak. Allows readers to estimate cost.

---

## Section D: Code & Data

### D1. Code Availability
> Is code available for reproduction?

**Pass criteria:** Public repository (GitHub/GitLab/Zenodo). Not "available upon request." Not "will be released." **Partial** if only inference code is released.

### D2. Data Availability
> Is data available for reproduction?

**Pass criteria:** Public dataset (DOI, URL). License clear. **Partial** if data is released but processing scripts aren't.

### D3. Dependencies & Environment
> Are software dependencies pinned (versions) for reproduction?

**Pass criteria:** `requirements.txt`, `environment.yml`, `pyproject.toml`, or Dockerfile. Specific versions, not `>=`.

### D4. Random Seeds
> Are random seeds set and reported?

**Pass criteria:** Seeds in code; OR multiple seeds run and reported with variance.

---

## Section E: Ethics & Compliance

### E1. License Compliance
> If using existing assets (datasets, models, code), are creators cited and licenses respected?

**Pass criteria:** Each asset cited; licenses listed; conflicts noted.

### E2. Asset Documentation
> If releasing new assets, are they documented (model card / data card / dataset documentation)?

**Pass criteria:** README with usage, intended use, limitations, license.

### E3. Human Subjects / Animal Use
> If applicable, IRB/ethics approval documented?

**Pass criteria:** Approval ID, institution, consent procedure. **N/A** for non-applicable papers.

### E4. LLM Usage Declaration
> Is LLM usage in research process declared (if non-trivial)?

**Pass criteria:** "We used GPT-4 for code prototyping" type disclosure. **N/A** if only used for grammar.

---

## Section F: Domain Extensions (Chemistry / Materials)

> Use these for chemistry/materials/physics papers in addition to A–E above. Replace 2 of the N/A items above with these for a chemistry paper.

### F1. Material Synthesis Reproducibility
> Are synthesis protocols complete (precursor purity, solvent, T, time, yield)?

### F2. Characterization Methods
> Are characterization instruments and conditions specified (XRD model, BET conditions, TGA ramp rate)?

### F3. Spectroscopic Data Availability
> Are raw spectra / scattering / chromatograms deposited (e.g., Mendeley Data, Zenodo)?

### F4. Crystallographic Data
> If crystal structures reported, are CIF files deposited at CCDC?

---

## Scoring Examples

### Example 1: Strong reproducibility (D5 = 9.5)
- A1 ✓ A2 ✓ A3 N/A
- B1 ✓ B2 ✓ B3 ✓ B4 ✓
- C1 ✓ C2 ✓ C3 ✓
- D1 ✓ D2 ✓ D3 ✓ D4 ✓
- E1 ✓ E2 ✓ E3 N/A E4 ✓
- → 14 / 14 applicable = 100% → score 9.5

### Example 2: Typical materials paper (D5 = 7.0)
- A1 ✓ A2 partial A3 N/A
- B1 ✓ B2 partial B3 ✓ B4 ✓
- C1 ✓ C2 N/A C3 ✗
- D1 ✗ D2 ✓ D3 ✗ D4 partial
- E1 ✓ E2 N/A E3 N/A E4 N/A
- → 7 ✓ + 3 partial (=1.5) of 11 applicable ≈ 77% → score 7.0
