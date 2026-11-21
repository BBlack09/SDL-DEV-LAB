# Module 02: 100-Point Evaluation Rubric

Submissions are evaluated by cohort architects and peers across both the **Individual** and **Group** Pull Requests plus the registered **Module 02 Submission Issue**.

---

## 📊 Point Breakdown

```text
├── 1. Individual UI/UX Engineering          (30 pts)
├── 2. Group UI/UX Cohesion                  (25 pts)
├── 3. Individual Git Hygiene                (20 pts)
└── 4. Collaborative Git & PR Execution      (25 pts)
Total: 100 Points
```

---

### 1. Individual UI/UX Engineering (30 Points)
- **8pt Spatial Grid Discipline (8 pts):** Consistent `8px` spacing rhythm (and `4px` micro-grid where justified) across layout, cards, and typography.
- **60-30-10 Color Architecture (7 pts):** Clear separation of dominant neutral (60%), secondary structural (30%), and accent (10%) tokens documented and applied accurately.
- **WCAG AA Contrast Compliance (7 pts):** All body text and controls meet or exceed `4.5:1` (`3.0:1` for large text/UI components) with verified ratios documented.
- **5 Interactive Component States (8 pts):** Default, Hover, Focus, Active/Pressed, and Disabled states are visually distinct, accessible, and complete in Google Stitch.

### 2. Group UI/UX Cohesion (25 Points)
- **Shared Design System & Token Consistency (10 pts):** Both partners' screens share unified typography, spacing grid, and 60-30-10 color tokens without visual drift.
- **End-to-End User Flow Completeness (8 pts):** Core screens connect seamlessly into a coherent multi-step product experience for the assigned group topic.
- **Accessibility & State Parity (7 pts):** WCAG AA contrast and all 5 interactive states are consistently maintained across every screen contributed by both partners.

### 3. Individual Git Hygiene (20 Points)
- **Branch Isolation & Naming (4 pts):** Correct branch name (`feat/m02-ind-<name>`) branched cleanly from `main` with no direct commits to `main`.
- **Atomic Conventional Commits (8 pts):** Minimum 5 atomic commits adhering strictly to Conventional Commits (`feat:`, `fix:`, `docs:`, `style:`, `refactor:`).
- **Hunk Granularity via `git add -p` (4 pts):** Clean, logically scoped diffs with no monolithic bulk commits or unrelated file noise.
- **CLI PR Execution (4 pts):** PR opened via `gh pr create` with a complete, well-structured description and valid Google Stitch link.

### 4. Collaborative Git & PR Execution (25 Points)
- **Balanced Two-Author Commit History (8 pts):** Both locked partners have meaningful, verifiable commits on `feat/m02-grp-<1-4>`.
- **Peer Merge Conflict Resolution (9 pts):** Genuine merge conflict triggered, resolved cleanly preserving both partners' edits, and evidenced in `git log --oneline --graph` with no force-push erasure.
- **Group CLI PR & Peer Review (8 pts):** Group PR opened via `gh pr create`, peer review comment/approval recorded by the partner, and both PRs properly registered in the Module 02 Issue Form.
