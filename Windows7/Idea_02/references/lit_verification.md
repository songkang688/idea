# Idea_02 — Literature Verification Log

## Tags

| Tag | Meaning |
|---|---|
| `[S5-verified]` | Existence confirmed by Stage-5 searches, 2026-08-28 |
| `[S6-verified]` | Surfaced or re-checked in the Stage-6 passes, 2026-08-28 |
| `[S6-abstract]` | Abstract read; full text **not** read |
| `[inherited]` | Carried from Stage 3/4 without re-verification |

## Verification debt — clear before submission

| Source | Tag | Missing |
|---|---|---|
| `arXiv:2606.24449` (SENTRY) | `[S6-abstract]` | full text |
| `arXiv:2602.19380` (CL-MC) | `[S6-abstract]` | full text |
| SAMITE, HiM2SAM | known **via** `arXiv:2512.22624` | primary sources not read directly |
| AS-SAM2 (TCSVT 2026) | `[S6-verified]`, code promised | code release unconfirmed |
| SAM2RL "+4.91%" figure | `[S6-verified]` | `EVIDENCE` reported in that group's own setup; motivates only, must not be reused as a baseline number |

## Cleared

| Source | Tag | Note |
|---|---|---|
| `arXiv:2512.22624` — Rethinking Memory Design in SAM-Based VOT, Dec 2025 | `[S6-verified]` | drove the A3 reframing; SAM3 zoo makes E7 cheap |
| `arXiv:2507.08548` — SAM2RL | `[S6-verified]` | second, independent ceiling; cross-check funded |
| SAM3 `arXiv:2511.16719` (Nov 2025), SAM 3.1 (Mar 2026) | `[S6-verified]` | |
| sam2, samurai, DAM4SAM, SAM2Long, LVOS, lvos-evaluation | `[S5-verified]` | existence only; fitness resolved at E0 |

## Standing rules

1. No citation enters this project that was not found in a Windows7 session and logged here.
2. `KNOWN FACT` **No tracking number anywhere in this package was measured by us.** All numbers in
   `README.md` and the prototype output are simulated and exist to validate the decision rule.
3. Stage-5 tagged repos "existence-verified". Stage 6 explicitly recommended distinguishing
   **existence-verified** from **fitness-verified**; that distinction is resolved by E0 and the
   access checklist, not by this file.
