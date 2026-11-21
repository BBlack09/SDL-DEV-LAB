# Contributing to the Dev Lab (SDL) Engineering Cohort

We welcome contributions, lab submissions, and technical discussions from all cohort engineers. Follow this guide to ensure a clean, reproducible workflow.

---

## 🛠️ Lab Submission Workflow

Submissions follow our **Hybrid CLI-to-PR + Issue Registry** workflow so every engineering artifact is backed by real Git history and tracked cleanly for rubric grading:

1. **Local Branching & Atomic Commits:**
   - Sync `main` and create your assigned feature branch (e.g., `feat/m02-ind-<name>` for individual work or `feat/m02-grp-<1-4>` for pair projects).
   - Never commit or push directly to `main`.
   - Use **Conventional Commits** (`feat:`, `fix:`, `docs:`, `style:`, `refactor:`) and selective staging (`git add -p`) for clean, atomic history.
   - For pair/group modules, resolve peer merge conflicts cleanly with `git merge` and preserve the merge commit graph (no `git push --force`).
2. **CLI Pull Request Creation (`gh pr create`):**
   - Push your feature branch and open your Pull Request directly from the terminal using the GitHub CLI:
     ```bash
     git push -u origin <your-branch>
     gh pr create --base main --head <your-branch>
     ```
   - Fill out `.github/pull_request_template.md` completely. For group PRs, your partner must leave a peer review comment or approval.
3. **Issue Registry Filing:**
   - Navigate to the **Issues** tab and click **New Issue**.
   - Select the template corresponding to your module (e.g., `🔬 Module 01 Lab Submission` or `🔬 Module 02 Lab Submission: UI/UX & Collaborative Git`).
   - Register your CLI-created PR URL(s), prototype/artifact links, `git log` proofs, and self-audit checklist.
4. **Labeling & Review:**
   - Issues automatically receive `sdl-cohort`, `module-XX`, and `needs-review` labels.
   - Cohort leads and peer reviewers evaluate submissions against the module's official `rubric.md` ([Module 01](modules/module-01-hyperparameters/rubric.md) | [Module 02](modules/module-02-uiux-git/rubric.md)).
   - Once evaluated, your issue is tagged with `reviewed`.

---

## 💬 Discussion Guidelines

Use the appropriate category in [GitHub Discussions](https://github.com/Skillodev/sdl-lab-dev/discussions):
* **📢 SDL Announcements:** Official cohort updates, module launches, and assignment tables (read-only for students).
* **🔬 Module 01 Labs (Hyperparameters):** Clarifications on formulas, API nuances, and parameter calibration.
* **🎨 Module 02 Labs (UI/UX & Git):** Questions on Google Stitch design systems, WCAG AA contrast audits, `git add -p`, and merge conflict resolution.
* **💡 Show and Tell / Failure Modes:** Share strange edge-cases, UI breakthroughs, and engineering lessons learned.
* **☕ Dev Lab Lounge:** General introductions, tech news, and cohort networking.
