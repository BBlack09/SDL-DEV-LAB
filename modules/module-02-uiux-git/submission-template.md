# Module 02: Lab Submission Report

**Mentee Name:** [Your Name]  
**GitHub Handle:** @[your-username]  
**Project Type:** [Individual / Group]  
**Branch Name:** `feat/m02-...`  
**Assigned Topic:** [Paste exact topic from ASSIGNMENTS.md]  
**Group Partner (if Group PR):** [Partner Name / N/A]  

---

## 1. Prototype & Pull Request Links

- **Google Stitch Prototype URL:** [Paste shareable Google Stitch URL]
- **Pull Request URL (created via `gh pr create`):** [Paste PR URL]

---

## 2. UI/UX Engineering Audit

### 8pt Spatial Grid
- **Base Grid:** `8px` (micro-grid: `4px`)
- **Layout Columns / Gutter / Margin:** [e.g., 12-col desktop, 24px gutter, 32px margin]

### 60-30-10 Color Tokens & WCAG AA Contrast Audit

| Role | Share | Hex Token | Paired Foreground/Background | Contrast Ratio | WCAG AA Pass (`>= 4.5:1`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Dominant / Neutral** | 60% | `#FFFFFF` | `#111827` text on `#FFFFFF` | `17.7:1` | Yes |
| **Secondary Surface** | 30% | `#F3F4F6` | `#1F2937` text on `#F3F4F6` | `13.2:1` | Yes |
| **Accent / Primary CTA** | 10% | `#1D4ED8` | `#FFFFFF` text on `#1D4ED8` | `6.7:1` | Yes |

### 5 Interactive Component States Checklist
- [ ] **Default**
- [ ] **Hover**
- [ ] **Focus** (visible keyboard focus ring)
- [ ] **Active / Pressed**
- [ ] **Disabled**

---

## 3. Git Hygiene & Commit History (`git log --oneline --graph`)

```text
[Paste output of: git log --oneline --graph -n 15]
```

---

## 4. Peer Merge Conflict Resolution (Group PRs Only)

- **Conflicting File(s):** [e.g., `submissions/module-02/groups/group-1/design-tokens.md`]
- **Merge Commit Hash:** `[commit-sha]`
- **Resolution Summary:** [Briefly explain what conflicted between both partners and how both contributions were preserved.]
