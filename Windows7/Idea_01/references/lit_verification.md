# Idea_01 — Literature Verification Log

Verification state of every source cited in `literature.md` and `proposal.md`. This file exists so
that nothing enters a submission bibliography on the strength of a chain of summaries.

## Tags

| Tag | Meaning |
|---|---|
| `[S5-verified]` | Existence confirmed by the Stage-5 engineer's web searches, 2026-08-28 |
| `[S6-verified]` | Surfaced or re-checked during the Stage-6 adversarial pass, 2026-08-28 |
| `[S6-abstract]` | Abstract read; full text **not** read |
| `[inherited]` | Carried from the Stage-3/4 ledger; **not** independently re-verified |

## Verification debt — must clear before submission

| Source | Current tag | What is missing |
|---|---|---|
| TBS, AAAI 2024 | `[inherited]` | venue, year and actual content unverified in Stage 5/6 |
| AENet, ECCV 2024 | `[inherited]` | same |
| Iterative modulation, CVPR 2024 | `[inherited]` | same |
| `arXiv:2501.13529` (support dilution) | `[S6-abstract]` | full text unread |
| `arXiv:2607.24706` (SADe) | `[S6-abstract]` | full text unread |
| Open-V / X2 "37 points" | `[S6-verified]`, figure is `EVIDENCE` reported by that group | primary source must be re-read before the number is quoted |

## Cleared

| Source | Tag | Note |
|---|---|---|
| BAM, Lang et al., CVPR 2022 Oral | `[S5-verified]` | repo and checkpoints located; also a panel member |
| SAM3, `arXiv:2511.16719`, Nov 2025 | `[S6-verified]` | drove the A1 reframing |
| SAM 3.1, Mar 2026 | `[S6-verified]` | |
| Panel repos (PFENet, HSNet, Matcher, PerSAM, FSSAM, SegGPT, SAM/SAM2) | `[S5-verified]` | existence only — fitness is resolved by E0 |

## Standing rule

No citation is added to this project that was not found in a Windows7 session and logged here. If a
paper is needed and is not in this table, it gets searched and logged first. `KNOWN FACT` No
benchmark number anywhere in this package was measured by us.
