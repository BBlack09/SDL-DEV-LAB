# Module 02: Locked Cohort Assignments (UI/UX Engineering & Collaborative Git)

> **Status:** 🔒 Locked Baseline | **Pairing History:** Pre-seeded into [`cohort/roster.json`](../../cohort/roster.json) so Module 03+ shuffles automatically generate fresh pairings.

Every mentee is responsible for **two deliverables**:
1. **Part A:** Your assigned **Individual UI/UX + Git Project** on your personal feature branch.
2. **Part B:** Your assigned **Pair Group UI/UX + Git Project** on your shared group branch with your assigned partner.

---

## Part A: 8 Individual UI/UX + Git Projects (Google Stitch)

| # | Mentee | Individual Project Topic | Required Feature Branch |
| :--- | :--- | :--- | :--- |
| 1 | **Kelechi** | Smart Grid & Solar Micro-Inverter Monitor | `feat/m02-ind-kelechi` |
| 2 | **Rimamtawey** | Agritech Farm-to-Market Logistics Portal | `feat/m02-ind-rimamtawey` |
| 3 | **Special** | Telemedicine Triage & Patient Booking Hub | `feat/m02-ind-special` |
| 4 | **Ayuba Garba** | Fintech Cross-Border Escrow & Remittance UI | `feat/m02-ind-ayuba-garba` |
| 5 | **Joshua** | Civic Utility & Municipal Issue Reporter | `feat/m02-ind-joshua` |
| 6 | **Bonaventure** | EdTech Interactive Code & STEM Sandbox | `feat/m02-ind-bonaventure` |
| 7 | **Ngbede** | Fleet Maintenance & Fuel Telemetry Dashboard | `feat/m02-ind-ngbede` |
| 8 | **Bitrus** | Event Ticketing & QR Access Control System | `feat/m02-ind-bitrus` |

---

## Part B: 4 Locked Pair Group Projects

### Partner Role Division Rules (Non-Overlapping Deliverables)

To prevent duplicate screens and ensure clean parallel Git collaboration, every pair splits UI/UX ownership strictly along two non-overlapping tracks:

- **Partner A — System Shell, Navigation & Browse Views:** Owns the app shell, headers, navigation/filter bars, hero summaries, and primary browse/grid views.
- **Partner B — Core Transaction, Modals & State Flows:** Owns interactive drawers, modals, multi-step wizards, toggles, error/promo/validation states, and confirmation receipts/badges.
- **Controlled Overlap Point (`SPEC.md` / `tokens.css`):** Partners must **not** build or edit each other's assigned screens. The **only** shared file both partners intentionally edit concurrently is `SPEC.md` (and/or `tokens.css`) in `submissions/module-02/groups/group-<1-4>/`, which serves as the single controlled overlap point for the mandatory Git merge conflict exercise.

| Group | Group Project Topic | Partner A (System Shell, Navigation & Browse Views) | Partner B (Core Transaction, Modals & State Flows) | Required Feature Branch |
| :--- | :--- | :--- | :--- | :--- |
| **Group 1** | Multi-Vendor Food & Grocery Delivery Checkout | **Bonaventure:** Storefront & Menu Grid | **Ayuba Garba:** Checkout Drawer, Promo States & Confirmation | `feat/m02-grp-1` |
| **Group 2** | Co-Working Space & Desk Reservation Platform | **Rimamtawey:** Workspace Header & Desk Availability Grid | **Kelechi:** Slot Booking Modal, Error States & Pass Receipt | `feat/m02-grp-2` |
| **Group 3** | Open-Source Developer Bounty & Issue Tracker | **Joshua:** Repo Header, Bounty Filters & Issue Feed | **Ngbede:** Issue Detail Drawer, Claim Bounty Modal & Payout Badges | `feat/m02-grp-3` |
| **Group 4** | Personal Finance & Automated Savings Vaults | **Bitrus:** Balance Hero & Savings Vaults Grid | **Special:** Create Vault Wizard, Auto-Save Toggles & Withdrawal Alert | `feat/m02-grp-4` |

---

## Next Steps

1. Read the complete engineering & design specifications in [`exercises.md`](exercises.md).
2. Review how your work will be scored in [`rubric.md`](rubric.md).
3. Submit both CLI-created Pull Requests and register them via the [🔬 Module 02 Lab Submission Issue Form](https://github.com/Skillodev/sdl-lab-dev/issues/new?template=module-02-submission.yml).
