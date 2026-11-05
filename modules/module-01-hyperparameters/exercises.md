# Module 01: Laboratory Exercises & Calibration Matrix

---

## 🎯 Objective
Empirically observe and map the phase transitions of token generation by systematically varying Temperature ($T$), Top-K, and Top-P across a compulsory universal core benchmark, followed by validating your calibrated sweet-spot settings on a beginner-friendly elective domain track.

---

## Section 1: Universal Core Benchmark (Compulsory for All Students)

All students must execute the identical, frozen benchmark prompt below across the complete 7-run calibration matrix. This standardized anchor allows cohort-wide comparison of how decoding hyperparameters alter cognitive depth, technical precision, and lexical variance.

> [!IMPORTANT]
> **Do not modify a single character** of this benchmark prompt during the 7 calibration runs. The prompt and model runtime must remain strictly frozen.

### 📌 The Frozen Core Benchmark Prompt

#### System Prompt
```text
You are a cognitive science educator and senior software mentor who synthesizes the principles of Barbara Oakley's Learning How to Learn (focused vs. diffuse thinking modes, chunking, and the Einstellung effect) with Angela Duckworth's research on Grit.
```

#### User Prompt
```text
A junior engineer transitioning into technical problem solving is struggling with cognitive overload, feeling stuck on a complex debugging bug, and experiencing intense imposter syndrome.
Write a 3-part mentorship breakdown:
1. Neural Mechanics: Explain how shifting from focused mode to diffuse mode physically works in the brain when tackling a stubborn engineering problem.
2. Actionable Chunking: Give a 3-step practical protocol to deconstruct overwhelming concepts into compact mental chunks without succumbing to the Einstellung effect (getting trapped in a flawed initial approach).
3. The Engineering Mindset: Provide a concise, grounding insight on building grit and a growth mindset when debugging code feels demoralizing.
```

---

### 🧠 Theoretical Parameter Guidance

Observe how the model's behavior shifts across parameter regimes during the benchmark:

| Parameter Setting | Run Reference | Theoretical Dynamic & Expected Behavior |
| :--- | :--- | :--- |
| **$T = 0.0$** | **Run 1A (Run 1)** | **Greedy Decoding:** Standard, predictable cognitive science definitions with near-identical outputs across students. High syntactic rigidity; potential for repetitive phrasing. |
| **$T = 0.7$** | **Run 2A (Run 3)** | **Balanced Standard:** Production baseline combining technical neuroscience accuracy with natural, empathetic mentorship cadence and varied transitions. |
| **$T = 1.2$, $\text{Top-P} = 0.5$** | **Run 2B (Run 4)** | **High Temp / Tight Nucleus:** High thermal entropy constrained by strict probability mass truncation; preserves scientific accuracy while varying sentence structure. |
| **$T = 0.9$, $\text{Top-K} = 10$** | **Run 3A (Run 5)** | **High Nucleus / Restricted Top-K:** Demonstrates vocabulary strangulation where nuanced terms (e.g., *prefrontal cortex*, *neuromodulators*) are prematurely filtered out before nucleus calculation. |
| **$T \ge 1.8$** | **Run 4 / Stress (Run 7)** | **Cognitive Breakdown:** Analogies become absurd, neuroscience terms turn into pseudo-scientific hallucinations, and syntax fragments into repetitive token loops or phoneme salad. |

---

### 🧪 Standard 7-Run Calibration Execution Matrix

Execute all 7 calibration runs sequentially with the frozen benchmark prompt and record all metrics:

| Run ID | Name | Temperature ($T$) | Top-K | Top-P | Target Hypothesis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Run 1A** | Deterministic Anchor | `0.0` | `1` | `1.0` | Greedy decoding; maximum determinism; baseline definition accuracy and loop vulnerability check. |
| **Run 1B** | Low-Entropy Coherence | `0.2` | `40` | `0.8` | Conservative, highly consistent lexical selection; minimal syntactic divergence. |
| **Run 2A** | Balanced Standard | `0.7` | `40` | `0.9` | Optimal creative/analytical baseline; fluent mentorship tone with rigorous cognitive framing. |
| **Run 2B** | High Temp / Tight Nucleus | `1.2` | `40` | `0.5` | Evaluates whether aggressive Top-P truncation can tame extreme thermal entropy. |
| **Run 3A** | Restricted Top-K / High Nucleus | `0.9` | `10` | `0.95` | Demonstrates vocabulary bottlenecking when fixed $K$ prunes candidates prior to nucleus expansion. |
| **Run 3B** | High Entropy Exploration | `1.4` | `100` | `0.98` | Onset of semantic drift, unconventional metaphors, and rising hallucination risk. |
| **Run 4 (Stress)** | Degeneration Stress Test | `1.8 - 2.0` | `200+` | `1.0` | Severe breakdown: pseudo-scientific confabulation, grammar disintegration, and token looping. |

---

## Section 2: Elective Domain Practice (Pick 1 of 5 Tracks)

After completing the core benchmark and identifying your model's optimal decoding "sweet spot" vector (e.g., $T \approx 0.6 - 0.75$, $\text{Top-P} \approx 0.9$, $\text{Top-K} \approx 40$), apply those calibrated settings to **ONE** elective domain track below.

Select the track that best aligns with your interests:

### Track 1: The Product Ad
> **Prompt:**  
> *"Write a short, exciting 100-word launch announcement for an eco-friendly smart backpack built for everyday commuters."*

### Track 2: The Mystery Story
> **Prompt:**  
> *"Write a two-paragraph story scene about a shopkeeper who hears a strange tapping sound coming from an old locked wooden box during a midnight rainstorm."*

### Track 3: The Tech Incident Report
> **Prompt:**  
> *"You are an IT technician. Write a brief, easy-to-read incident report explaining to an office team why the company website went down for 30 minutes and how you fixed it."*

### Track 4: The Social Media Bio
> **Prompt:**  
> *"Write a friendly 4-sentence LinkedIn profile summary for someone who is switching careers from teaching into tech and web design."*

### Track 5: The Fun Office Memo
> **Prompt:**  
> *"Write a funny, lighthearted company email announcing a new office rule: anyone who drinks the last cup of coffee without making a fresh pot has to sing a song at the next team meeting."*

---

## 📝 Step 3: Submission

Submit your results and empirical analysis via the [Module 01 Submission Issue Form](https://github.com/Skillodev/sdl-lab-dev/issues/new?template=module-01-submission.yml).
