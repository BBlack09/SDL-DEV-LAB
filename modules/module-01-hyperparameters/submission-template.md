# Module 01: Lab Submission Report

**Student Name:** [Your Name]  
**GitHub Username:** @[your-username]  
**Track Selected:** [e.g., Track A: Speculative Hard Sci-Fi]  
**Model & Engine:** [e.g., Gemini 1.5 Pro via Google AI Studio]  

---

## 1. Frozen Prompt

### System Prompt
```text
[Paste system prompt here]
```

### User Prompt
```text
[Paste user prompt here]
```

---

## 2. 7-Run Calibration Matrix

| Run ID | Temp | Top-K | Top-P | Tokens | Coherence (1-10) | Qualitative Observations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Run 1** | 0.0 | 1 | 1.0 | | | Deterministic baseline |
| **Run 2** | 0.2 | 40 | 0.8 | | | Focused coherence |
| **Run 3** | 0.7 | 40 | 0.9 | | | Balanced creativity |
| **Run 4** | 1.2 | 40 | 0.5 | | | High Temp / Constrained Nucleus |
| **Run 5** | 0.9 | 10 | 0.95 | | | High Nucleus / Constrained Top-K |
| **Run 6** | 1.4 | 100 | 0.98 | | | High entropy exploration |
| **Run 7** | 1.8 | 200+ | 1.0 | | | Degeneration stress test |

---

## 3. Empirical Analysis
[Document your theoretical breakdown of the phase transitions and parameter interactions here]

---

## 4. Production Sweet Spot
* **Recommended Vector:** `Temp = X.X`, `Top-K = XX`, `Top-P = X.XX`
* **Engineering Justification:** [Why this vector optimizes quality, diversity, and coherence]
