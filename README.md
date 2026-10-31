# Dev Lab (SDL) Engineering Cohort

Welcome to the **Dev Lab (SDL) Engineering Cohort** repository. This is an intensive, hands-on engineering lab program focused on building a deep, mechanistic understanding of Large Language Models (LLMs), probabilistic decoding, retrieval systems, and autonomous agent orchestration.

---

## 🎯 Program Mission

Rather than treating modern AI systems as opaque black-box APIs, this cohort trains software engineers to investigate, calibrate, and engineer against the underlying probabilistic nature of transformer language models.

* **Probabilistic Decoding Over Guesswork:** Measure logits, entropy, and token distributions directly.
* **Empirical Rigor:** Formulate hypotheses, execute calibration matrices, and systematically record failure modes.
* **Production-Grade Architecture:** Move beyond toy wrappers into resilient, evaluatable generative AI pipelines.

---

## 🗺️ Cohort Curriculum Roadmap

| Module | Title | Core Focus | Status |
| :--- | :--- | :--- | :--- |
| **Module 01** | [**Hyperparameters & Decoding Dynamics**](modules/module-01-hyperparameters/README.md) | Temperature ($T$), Top-K, Top-P (Nucleus), Softmax Calibration | 🟢 Active |
| **Module 02** | **Latent Space & Vector Embeddings** | Semantic clustering, cosine geometry, high-dimensional search | ⚪ Upcoming |
| **Module 03** | **Context Windows & RAG Architectures** | Chunking strategies, hybrid retrieval, reciprocal rank fusion | ⚪ Upcoming |
| **Module 04** | **Prompt Chaining & Tool-Use Agents** | Deterministic JSON schema enforcement, multi-step orchestration | ⚪ Upcoming |
| **Module 05** | **Evaluation, Alignment & Red-Teaming** | LLM-as-a-Judge, adversarial perturbation, benchmark design | ⚪ Upcoming |

---

## 🚀 How to Participate & Submit Labs

1. **Clone & Setup:** Clone this repository and create your working branch:
   ```bash
   git checkout -b feat/module-01-<your-github-username>
   ```
2. **Execute Lab Exercises:** Read the theoretical background in [`modules/module-01-hyperparameters/README.md`](modules/module-01-hyperparameters/README.md) and execute the calibration matrix in [`exercises.md`](modules/module-01-hyperparameters/exercises.md).
3. **Submit Your Work:**
   - Go to [GitHub Issues](https://github.com/Skillodev/sdl-lab-dev/issues/new/choose).
   - Select **Module 01 Lab Submission: Hyperparameters & Decoding**.
   - Fill in your 7-run calibration data, empirical analysis, and narrative artifact.
4. **Engage in Community Discussions:** Review peer submissions and discuss surprising failure modes in [GitHub Discussions](https://github.com/Skillodev/sdl-lab-dev/discussions).

---

## 📜 Code of Engineering Conduct

1. **Data Authenticity:** Report actual observed model responses and metrics. Never fabricate runs or smooth over unexpected model failures.
2. **Curiosity & Peer Review:** Constructive feedback on architectural trade-offs is encouraged across all discussion threads.
3. **Intellectual Honesty:** Document model hallucinations and prompt injection vulnerabilities as first-class engineering findings.
