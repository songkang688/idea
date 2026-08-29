# Windows4 Research Ledger — Supervisor Log

Last updated: 2026-08-28 (UTC)
Current stage: **Stage 1 — Massive Idea Exploration** (agents in flight)

## Git safety

- Inspected `origin/main`: only `README.md` (`# fnyuan`), commit `990f3eb`.
- No `Windows1`…`WindowsN` directories on this remote.
- User assigned identity **Windows4** → create `Windows4/`, never overwrite other Windows trees.
- Branch: `cursor/windows4-research-idea-evolution-2962`

## Concurrent cloud sub-agents (Stage 1)

Wave-0 (FAILED, activity timeout, empty transcripts — no ideas recovered):
- Batch A `bc-21dd1f64-0380-5cff-90dc-2060bf543547`
- Batch B `bc-9b9c0239-3ece-559c-b745-ada47f055d67`
- Batch C `bc-db3fe9fa-d2d1-5534-a328-f50b5b48d7a4`

Cause: 340 long-form ideas / agent exceeded cloud activity limit. Mitigation: compact 120-row tables, no web browse.

Wave-1 (DONE catalogs):
| Role | Agent ID | Result |
|------|----------|--------|
| A1 | `bc-cf0d6dad-8d99-5cf2-8493-40753ec2897c` | 120 ideas → `stage1_A1.md` (DONE). Protect: A1-027,030,039,046,049,063,067,082,094,099,105,108,115,118,120. Cheap: A1-002,004,008,015,020,023,032,048,058,068,071,084,095,098,110 |
| B1 | `bc-6d41759b-58e9-50f4-9910-f625336d6f29` | 120 ideas → `stage1_B1.md` |
| C1 | `bc-3d8edeb8-ca72-58ae-b909-4ff5a13e209b` | 120 ideas on branch `cursor/stage1-c1-idea-catalog-209b`; copied to `stage1_C1.md` |

Raw pool before dedup: S-001–S-720 + A1 + B1 + C1 ≈ 1080 IDs.

Stage 2 IN FLIGHT (3 reviewers, compact keep-lists):
- Novelty assassin on S-series: `bc-8d9055cc-7185-56e7-9375-4b6a9fa5eeda`
- Feasibility on A1+B1: `bc-616dd955-2a7d-5b08-a53b-5ea8d7531a29`
- C1 + meta-audit: `bc-20f7911c-f82e-5689-8138-448cf5a6f2c1`

## Idea Pool / Top Candidates

Empty until Stage 1 catalogs land. Then:

- Dedup / cluster / merge / split / kill / revive
- Protect: high-risk high-reward, cheap-to-falsify, reviewer-disagreement, counter-intuitive simple hypotheses
- Kill: module stacking, “apply X to medical”, loss-swap, backbone-swap, attention-add with no scientific question

## Epistemic labels in force

Every claim in later packages must be tagged as one of:
KNOWN FACT | EVIDENCE | HYPOTHESIS | MODEL SPECULATION | EXPECTED RESULT | ACTUAL EXPERIMENTAL RESULT

No fabricated papers, citations, or measured numbers.
