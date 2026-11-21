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
| **Module 02** | [**UI/UX Engineering (Google Stitch) & Collaborative Git**](modules/module-02-uiux-git/exercises.md) | 8pt Grid, 60-30-10 Color, WCAG AA, 5 States, Conventional Commits, Peer Merge Conflicts ([Assignments](modules/module-02-uiux-git/ASSIGNMENTS.md)) | 🟢 Active |
| **Module 03** | **Latent Space & Vector Embeddings** | Semantic clustering, cosine geometry, high-dimensional search | ⚪ Upcoming |
| **Module 04** | **Context Windows & RAG Architectures** | Chunking strategies, hybrid retrieval, reciprocal rank fusion | ⚪ Upcoming |
| **Module 05** | **Prompt Chaining & Tool-Use Agents** | Deterministic JSON schema enforcement, multi-step orchestration | ⚪ Upcoming |
| **Module 06** | **Evaluation, Alignment & Red-Teaming** | LLM-as-a-Judge, adversarial perturbation, benchmark design | ⚪ Upcoming |

---

## 🚀 How to Participate & Submit Labs (Hybrid CLI-to-PR + Issue Registry)

1. **Check Assignments & Branch Locally:**
   - Review your module exercises and assigned branch names (e.g., [`modules/module-02-uiux-git/ASSIGNMENTS.md`](modules/module-02-uiux-git/ASSIGNMENTS.md)).
   - Never commit directly to `main`. Create your feature branch:
     ```bash
     git checkout main && git pull origin main
     git checkout -b feat/m02-ind-<name>
     ```
2. **Build & Commit Atomically:**
   - Complete the lab deliverables (e.g., Google Stitch UI/UX prototypes + design specs for Module 02).
   - Stage hunks selectively with `git add -p` and write atomic Conventional Commits (`feat:`, `fix:`, `docs:`, `style:`, `refactor:`).
   - For pair projects, intentionally resolve a peer merge conflict on your shared group branch (`feat/m02-grp-<1-4>`).
3. **Open Pull Request(s) via CLI (`gh pr create`):**
   ```bash
   git push -u origin feat/m02-ind-<name>
   gh pr create --base main --head feat/m02-ind-<name>
   ```
4. **Register Submission in GitHub Issues:**
   - Go to [GitHub Issues](https://github.com/Skillodev/sdl-lab-dev/issues/new/choose) and select the active module template (e.g., **🔬 Module 02 Lab Submission: UI/UX & Collaborative Git**).
   - Paste your CLI-created PR URL(s), prototype links, and `git log` proofs.
5. **Engage in Community Discussions:** Follow official updates in `📢 SDL Announcements` and collaborate in [GitHub Discussions](https://github.com/Skillodev/sdl-lab-dev/discussions).

---

## 🔀 Automated Cohort Pairing & Topic-Reshuffling Engine

To ensure every mentee collaborates with a fresh partner on each new module, this repository includes a zero-dependency Python 3 pairing engine backed by [`cohort/roster.json`](cohort/roster.json) (pre-seeded with Module 02's locked pairs).

### Run Locally
1. Create `modules/<module-slug>/topics.json` with at least 8 `individual_topics` and 4 `group_topics` (see [`modules/module-02-uiux-git/topics.json`](modules/module-02-uiux-git/topics.json) for the schema).
2. Run the reshuffler:
   ```bash
   python scripts/pair_mentees.py \
     --module module-03-frontend-arch \
     --record-history \
     --output modules/module-03-frontend-arch/ASSIGNMENTS.md
   ```
   Pass `--seed <integer>` for a deterministic shuffle; omit `--seed` to generate a cryptographically random seed via `secrets.randbelow(10**8)`.

### Run via GitHub Actions
Navigate to **Actions → Shuffle Cohort Pairings & Topics → Run workflow** (`.github/workflows/shuffle-cohort.yml`), enter `module_slug`, optionally set `custom_seed`, keep `record_history` enabled, and the workflow will automatically generate `ASSIGNMENTS.md`, update `cohort/roster.json`, and commit + push as `github-actions[bot]`.

---

## 📜 Code of Engineering Conduct

1. **Data Authenticity:** Report actual observed model responses and metrics. Never fabricate runs or smooth over unexpected model failures.
2. **Curiosity & Peer Review:** Constructive feedback on architectural trade-offs is encouraged across all discussion threads.
3. **Intellectual Honesty:** Document model hallucinations and prompt injection vulnerabilities as first-class engineering findings.
