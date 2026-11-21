# Module 02: UI/UX Engineering (Google Stitch) & Collaborative Git

---

## 🎯 Objective

Master production-grade **UI/UX design systems** using **Google Stitch** alongside **collaborative Git engineering** via the command line. Each mentee will deliver both an **Individual Project** (Part A) and a **Pair Group Project** (Part B) following strict visual engineering constraints and professional Git hygiene.

> [!IMPORTANT]
> Check your assigned individual topic, locked pair partner, group topic, and exact branch names in [**`ASSIGNMENTS.md`**](ASSIGNMENTS.md) before starting.

---

## Part 1: Strict UI/UX Engineering Standards (Google Stitch)

Both your **Individual** and **Group** Google Stitch prototypes must strictly adhere to all four engineering standards below:

### 1. 8pt Spatial Grid System
- All margins, padding, gaps, container dimensions, and vertical rhythm must be multiples of **`8px`** (`8, 16, 24, 32, 48, 64px`).
- A **`4px`** micro-grid is permitted *only* for compact internal element alignment (e.g., icon-to-label spacing or badge padding).
- Document your layout grid (columns, gutters, margins) in your project spec.

### 2. 60-30-10 Color Architecture
- **60% Dominant / Neutral:** Primary canvas, background surfaces, and whitespace.
- **30% Secondary Structural:** Cards, sidebars, navigation surfaces, and borders.
- **10% Accent / High-Emphasis:** Primary CTAs, active indicators, and critical status badges.
- Define explicit hex tokens for every color role (including semantic Success, Warning, and Error states).

### 3. WCAG AA Accessibility (`>= 4.5:1` Contrast)
- Normal body text and interactive labels must achieve a minimum **`4.5:1`** contrast ratio against their background.
- Large text (`>= 18pt` / `24px` regular or `>= 14pt` / `18.66px` bold) and UI component boundaries/icons must achieve at least **`3.0:1`**.
- Record your verified foreground/background hex pairs and contrast ratios in your submission.

### 4. Five Interactive Component States
Every core interactive control (buttons, inputs, selectable cards, tabs, or dropdowns) must explicitly demonstrate all **5 states** in your Stitch prototype/component sheet:
1. **Default** (resting state)
2. **Hover** (pointer feedback)
3. **Focus** (visible keyboard focus ring meeting `>= 3:1` contrast)
4. **Active / Pressed** (tactile confirmation)
5. **Disabled** (clearly non-interactive, reduced emphasis)

### 5. Pair Group Component Ownership (Partner A vs. Partner B)

For **Part B (Group Projects)**, paired mentees must divide screens and components cleanly so **no partner duplicates the other's work**:

- **Partner A — System Shell, Navigation & Browse Views:** Responsible for the structural shell, top-level headers, filter controls, hero summaries, and browse/listing grids.
- **Partner B — Core Transaction, Modals & State Flows:** Responsible for interactive drawers, modals, multi-step wizards, state toggles, validation/error/promo states, and confirmation receipts or status badges.
- **Single Controlled Overlap (`SPEC.md` / `tokens.css`):** Both partners must share a single `SPEC.md` and/or `tokens.css` file under `submissions/module-02/groups/group-<1-4>/` for shared 8pt grid rules, 60-30-10 color tokens, and typography definitions. This file is the **only** permitted overlap point and is used intentionally for the mandatory Git merge conflict exercise below.

| Group | Project Topic | Partner A (System Shell, Navigation & Browse Views) | Partner B (Core Transaction, Modals & State Flows) |
| :--- | :--- | :--- | :--- |
| **Group 1** | Multi-Vendor Food & Grocery Delivery Checkout | **Bonaventure:** Storefront & Menu Grid | **Ayuba Garba:** Checkout Drawer, Promo States & Confirmation |
| **Group 2** | Co-Working Space & Desk Reservation Platform | **Rimamtawey:** Workspace Header & Desk Availability Grid | **Kelechi:** Slot Booking Modal, Error States & Pass Receipt |
| **Group 3** | Open-Source Developer Bounty & Issue Tracker | **Joshua:** Repo Header, Bounty Filters & Issue Feed | **Ngbede:** Issue Detail Drawer, Claim Bounty Modal & Payout Badges |
| **Group 4** | Personal Finance & Automated Savings Vaults | **Bitrus:** Balance Hero & Savings Vaults Grid | **Special:** Create Vault Wizard, Auto-Save Toggles & Withdrawal Alert |

---

## Part 2: Strict Git & Collaborative CLI Workflow

All version-control work must be executed from the terminal (no GitHub web-editor commits).

### 1. Feature Branch Isolation
- Never commit directly to `main`.
- Always branch from an up-to-date `main`:
  ```bash
  git checkout main && git pull origin main
  # Individual branch (see ASSIGNMENTS.md for your exact slug)
  git checkout -b feat/m02-ind-<name>
  # Group branch (shared with your partner)
  git checkout -b feat/m02-grp-<1-4>
  ```
- Place your exported Stitch specs, design token documentation, contrast audit, and project README under:
  - Individual: `submissions/module-02/individual/<name>/`
  - Group: `submissions/module-02/groups/group-<1-4>/`

### 2. Atomic Conventional Commits (`>= 5` Commits + `git add -p`)
- Each branch must contain a **minimum of 5 atomic Conventional Commits** using standard prefixes (`feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `chore:`).
- Use interactive hunk staging (**`git add -p`**) to keep every commit scoped to a single logical change—monolithic "add everything" commits will lose points.
- Example progression:
  ```bash
  git add -p
  git commit -m "docs(m02): initialize project architecture and 8pt grid spec"
  git commit -m "style(m02): define 60-30-10 color tokens and WCAG AA contrast table"
  git commit -m "feat(m02): document 5 interactive component states from Google Stitch"
  git commit -m "feat(m02): add core user flow screens and Stitch prototype links"
  git commit -m "fix(m02): correct contrast ratio on disabled and focus states"
  ```

### 3. Mandatory Peer Merge Conflict Resolution (Group Branch Only)
Both partners on `feat/m02-grp-<1-4>` must keep their assigned screens/components strictly separate and use the shared **`SPEC.md`** or **`tokens.css`** file as their **single controlled overlap point** to intentionally trigger and cleanly resolve at least **one real Git merge conflict**:
1. Both partners commit concurrently against the shared `feat/m02-grp-<1-4>` branch, editing the **same section** of the shared `SPEC.md` or `tokens.css` file in `submissions/module-02/groups/group-<1-4>/` (e.g., adding Partner A's shell tokens and Partner B's modal/state tokens in the same token block).
2. Partner A pushes first to `origin feat/m02-grp-<1-4>`.
3. Partner B runs `git fetch origin && git merge origin/feat/m02-grp-<1-4>`, encounters the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), resolves them manually so **both partners' work is preserved**, stages the resolved file, and completes the merge commit.
4. Do **not** force-push (`git push --force`) or squash away the merge commit—reviewers will verify the merge history via `git log --oneline --graph`.

### 4. Terminal Pull Request Creation (`gh pr create`)
Open **both** Pull Requests (1 Individual PR + 1 Group PR) from your terminal using the GitHub CLI:
```bash
git push -u origin feat/m02-ind-<name>
gh pr create --base main --head feat/m02-ind-<name> \
  --title "feat(m02): <Your Name> - <Individual Topic>" \
  --body-file modules/module-02-uiux-git/submission-template.md
```
For the Group PR, one partner opens the PR via `gh pr create` on `feat/m02-grp-<1-4>` and the second partner must leave a **peer code/design review comment or approval** on the PR.

---

## Part 3: Hybrid Submission Registry

Once both PRs are live on GitHub:
1. Open the [**🔬 Module 02 Lab Submission Form**](https://github.com/Skillodev/sdl-lab-dev/issues/new?template=module-02-submission.yml).
2. Select your name and locked group from the dropdowns.
3. Paste your **Individual PR URL**, **Group PR URL**, **Individual & Group Google Stitch Prototype URLs**, and **`git log`** outputs.
4. Complete the self-audit checkboxes against the [**100-Point Rubric (`rubric.md`)**](rubric.md).
