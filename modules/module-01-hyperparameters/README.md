# Module 01: Hyperparameters & Decoding Dynamics

Welcome to **Module 01** of the Dev Lab (SDL) Engineering Cohort. In this module, we dissect the mechanics of autoregressive token generation, softmax temperature scaling, and sampling constraints.

---

## 🧠 Theoretical Foundations

Autoregressive language models predict the conditional probability distribution of the next token $x_t$ given the preceding context $x_{<t}$:

$$P(x_t \mid x_{<t}) = \text{softmax}\left(\frac{z_i}{T}\right) = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}$$

Where:
* $z_i$ represents the raw logit score for token candidate $i$.
* $T$ represents the **Temperature** hyperparameter.

---

## 🔬 Core Decoding Parameters

### 1. Temperature ($T$)
* **$T \to 0$ (Greedy Decoding):** As $T \to 0$, the probability of the highest-logit token approaches 1. The output becomes deterministic, repetitive, and vulnerable to degenerate looping.
* **$T = 1.0$ (True Distribution):** The model samples tokens according to its raw learned probability distribution.
* **$T > 1.0$ (High Thermal Entropy):** The logit distribution flattens, making previously improbable tokens likely. At $T \ge 1.8$, syntax breaks down into phoneme salad and token stutter.

### 2. Top-K Sampling
Top-K sampling restricts the candidate pool to the $K$ most probable tokens:
* Truncates the infinite tail of low-probability noise.
* **Limitation:** Fixed $K$ cannot adapt to distribution shape. For flat distributions, it may be too strict; for peaked distributions, it may include low-quality noise.

### 3. Top-P (Nucleus) Sampling
Top-P sampling dynamically selects the smallest set of tokens whose cumulative probability exceeds threshold $P$:

$$\sum_{i \in V^{(p)}} P(x_t = v_i \mid x_{<t}) \ge P$$

* Dynamically adjusts vocabulary size based on model confidence.
* When the model is confident (peaked distribution), the nucleus shrinks. When uncertain (flat distribution), the nucleus expands.

---

## 📂 Module Navigation
* 📝 [**Exercises & The 7-Run Matrix**](exercises.md)
* 📊 [**100-Point Grading Rubric**](rubric.md)
* 📋 [**Submission Template**](submission-template.md)
