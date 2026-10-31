# Module 01: 100-Point Evaluation Rubric

Submissions will be evaluated by cohort architects and peers using this structured 100-point rubric.

---

## 📊 Point Breakdown

```
├── 1. Calibration Matrix Execution & Data Rigor (30 pts)
├── 2. Theoretical Analysis & Decoding Mechanics  (35 pts)
├── 3. Prompt Track Execution & Evaluation        (20 pts)
└── 4. Documentation, Reproducibility & Peer Review (15 pts)
Total: 100 Points
```

---

### 1. Calibration Matrix Execution & Data Rigor (30 Points)
* **Prompt Integrity (10 pts):** Identical system and user prompt verified across all 7 runs without parameter leakage.
* **Matrix Completeness (10 pts):** All 7 parameter vectors precisely executed and tabulated with accurate token counts and qualitative metrics.
* **Failure Mode Capture (10 pts):** Run 7 clearly reproduces and documents catastrophic degeneration (e.g., token stuttering, hallucinatory syntax, repetitive loops).

### 2. Theoretical Analysis & Decoding Mechanics (35 Points)
* **Mathematical Grounding (15 pts):** Clear explanation of how temperature rescaled the logit vector in the softmax calculation across runs.
* **Parameter Interaction Analysis (10 pts):** Deep comparative analysis of Run 4 (High Temp / Tight Nucleus) vs. Run 5 (Tight Top-K / High Nucleus).
* **Sweet Spot Formulation (10 pts):** Justified recommendation of the optimal hyperparameter vector for production deployment of the chosen prompt track.

### 3. Prompt Track Execution & Evaluation (20 Points)
* **Track Fidelity (10 pts):** Strong alignment with the selected genre's vocabulary, pacing, and tone.
* **Prompt Constraint Robustness (10 pts):** Evaluation of how stylistic constraints held up under high-temperature regimes.

### 4. Documentation, Reproducibility & Peer Review (15 Points)
* **Formatting & Structure (10 pts):** Clean Markdown tables, legible token formatting, and proper adherence to the issue template.
* **Cohort Contribution (5 pts):** Constructive comment or feedback left on at least one peer submission in GitHub Discussions.
