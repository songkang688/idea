# Ledger index — where Windows1's per-stage funnel records actually live

Status: **retrospective index, written after the Final 3 were already locked and merged to `main`.**
Nothing in this file re-opens a selection decision. It records *attribution* and *location* only.

Epistemic labels used here follow `Windows1/README.md`: KNOWN FACT, EVIDENCE, HYPOTHESIS,
MODEL SPECULATION, EXPECTED RESULT, ACTUAL EXPERIMENTAL RESULT.
No ACTUAL EXPERIMENTAL RESULT appears anywhere in this index, because none exists for this round.

---

## 1. The problem this file solves

**KNOWN FACT.** Windows1's three delivered Idea packages and its three summary documents live under
`Windows1/`. But the per-stage funnel records — the files that show *how* ≥1065 ideas became 3 —
are not under `Windows1/`. They are 12 files in the **repository-root `research_ledger/` directory**.

**KNOWN FACT.** Before this backfill, `Windows1/selection_history/` held only three ~1 KB digests
(`evolution_summary.md`, `eliminated_ideas_summary.md`, `reviewer_summary.md`). A reader starting from
`Windows1/` had no pointer to the root ledger and therefore could not audit any individual stage.

---

## 2. Attribution: all 12 root ledger files are Windows1's

Two independent kinds of evidence establish this. Six files say so in their own title; the other six
are pinned by content that only Windows1's documents contain.

### 2a. Files whose own title names the window (KNOWN FACT, self-identifying)

| File | Exact title line |
|---|---|
| `research_ledger/stage1_seg_keepers.md` | `# Stage 1 ingest — SEG slice (Windows1)` |
| `research_ledger/stage1_vfm_local_pool.md` | `# Local VFM/PEFT/SAM pool (Windows1 supervisor backup)` |
| `research_ledger/stage1_asm_local_pool.md` | `# Local assumption-breaking pool (Windows1 supervisor backup)` |
| `research_ledger/stage2_seg_review.md` | `# Stage 2 — Independent SEG review (Windows1)` |
| `research_ledger/stage4_reviewer2.md` | `# Stage 4 — Reviewer #2 (Windows1)` |
| `research_ledger/meta_audit.md` | `# Meta-audit (Windows1)` |

### 2b. Files with no window marker in the title, attributed by cross-reference (EVIDENCE)

The remaining six carry **no** `(Windows1)` string. Each is attributed below by a specific,
checkable overlap with a Windows1-authored document. Where the phrasing matches near-verbatim,
that is noted, because verbatim overlap is much stronger than topical overlap.

| File | Cross-reference that pins it to Windows1 | Strength |
|---|---|---|
| `stage1_vfma_asma_keepers.md` | Its keeper IDs (`A0022, A0051, A0028, A0077, A0101, A0121, A0148, A0153, A0166, A0168`) are exactly the ID set adjudicated by `stage3_vfm_kills.md`, and its closing line — "Downweight LLM-only … for **this round's final 3**" — is a Windows1 supervisor instruction. | Strong |
| `stage3_priorwork_kill.md` | Its `SURVIVE: 0252, 0275, 0250, 0285(weak)` line is restated in `Windows1/selection_history/reviewer_summary.md` as "strongest remaining SEG science was 0252, 0250, 0275, 0276-M". It adjudicates the SEG-00xx IDs enumerated in the Windows1-marked `stage1_seg_keepers.md`. | Strong |
| `stage3_vfm_kills.md` | Its four kills — `A0022 TETRIS; A0168 RClicks; A0077 PARA; A0148 Registers` — appear as four separate rows in `Windows1/selection_history/eliminated_ideas_summary.md` (`VFM-A0022 \| TETRIS AAAI 2024`, `VFM-A0168 \| RClicks 2024`, `VFM-A0077 \| PARA / AdaLoRA`, `VFM-A0148 \| DINOv2 registers`). Near-verbatim, four-for-four. | Very strong |
| `stage4_reviewer2.md` *(also in 2a)* | Its `Source: bc-90c313c0-…-45733` matches the recovered full panel titled `# Stage 4 — Reviewer #2 Kill Panel (**Windows1 PI**)`. See `stage4_candidates.md`. | Very strong |
| `stage5_0276.md` | SEG-0276-M is the runner-up named in `Windows1/README.md` ("Runner-up **SEG-0276-M** (prior-shape interpolation α) is HRHR and inference-only"). Its "Recommendation from designer: INCLUDE, displace Constrained SAM-FT" is restated in `reviewer_summary.md` as "0276 designer recommended displacing RetainSAM". | Very strong |
| `stage5_killers.md` | Its "Engineer Top-5" #1 `Constrained SAM-FT` is Windows1's `Idea_01` RetainSAM; it references the "auditor Top-8", which is the `Updated working Top-8` list inside the Windows1-marked `meta_audit.md`. | Strong |
| `cheap_killers_0252_0046.md` | Its formula `0252: amplification g ≈ ρ_H · ρ_M` appears in `Windows1/selection_history/evolution_summary.md` as "SEG-0252 label ecology (**cheap ρ_H·ρ_M design exists**)". Its second subject `0046-M` appears in the same evolution_summary line ("0046-M transmittance (matting / SMOKE5K AAAI 2022)"). | Very strong |

**Correction to the record.** A blanket claim that all 12 titles carry `(Windows1)` would be wrong;
only the six in 2a do. The other six are attributed by content, as tabulated. This distinction is
recorded so a later auditor does not "verify" a title marker that is not there.

### 2c. Additional corroboration: pool sizes are exact, not approximate (KNOWN FACT)

`Windows1/research_summary.md` describes the local pools as "local VFM ~350 + local ASM ~350".
Counting ID-bearing lines in the two root pool files:

| File | IDs found | Range |
|---|---|---|
| `stage1_vfm_local_pool.md` | 350 | `VFM-0001` … `VFM-0350`, no gaps |
| `stage1_asm_local_pool.md` | 350 | `ASM-0001` … `ASM-0350`, no gaps |

So `~350` is exactly 350 in both cases, and `365 + 350 + 350 = 1065` reproduces the
"≥1065" figure in `research_summary.md` precisely. This is arithmetic on files in this repository,
not an estimate.

---

## 3. Stage-by-stage index

Funnel level → ledger file. Every level below is reachable from `Windows1/selection_history/`
via this table.

| Funnel level | Root ledger file | Size | What it contains | Backfilled companion in this directory |
|---|---|---|---|---|
| **Stage 1** generation (SEG slice) | `research_ledger/stage1_seg_keepers.md` | ~2.4 KB | 365 SEG ideas claimed; cluster counts; Top-30 keepers; 13 protected HRHR. **Digest only — the full SEG-0001…0365 text is not in this repo.** | — |
| **Stage 1** generation (VFM pool) | `research_ledger/stage1_vfm_local_pool.md` | ~43 KB | Full 350-idea local VFM/PEFT/SAM pool, one line per idea (`ID \| idea \| hyp \| minExp \| cluster \| risk`). Contains `VFM-0263` and `VFM-0274`, the ancestors of Idea_01. | — |
| **Stage 1** generation (ASM pool) | `research_ledger/stage1_asm_local_pool.md` | ~34 KB | Full 350-idea local assumption-breaking pool. | — |
| **Stage 1** compact batches | `research_ledger/stage1_vfma_asma_keepers.md` | ~1 KB | VFM-A 180 + ASM-A 180. **Keeper digest only — the 360 idea texts are not in this repo.** | — |
| **Stage 2** independent review | `research_ledger/stage2_seg_review.md` | ~1 KB | Named-48 decisions (KEEP200 / PROTECT-HRHR / MUTATE / KILL), 15 under-ranked promotions, 10 over-ranked. Carries its own caveat: "Scores are REVIEWER JUDGMENT not facts." | — |
| **Stage 3** prior-work kill (SEG) | `research_ledger/stage3_priorwork_kill.md` | ~1.2 KB | 5 KILL, 4 SURVIVE, 11 MUTATE, plus a ranked "top scientific territory" list of 10. | `stage3_survivors.md` (new) |
| **Stage 3** prior-work kill (VFM) | `research_ledger/stage3_vfm_kills.md` | ~0.8 KB | 4 KILL, 8 MUTATE, 1 WEAK SURVIVE. Declares "interactive eval merge" dead and sets the WiSE-FT condition on constrained SAM-FT. | `stage3_survivors.md` (new) |
| **Stage 4** Reviewer #2 | `research_ledger/stage4_reviewer2.md` | ~1.1 KB | Summary: 1 KILL (0193), all others KEEP-IF-EXPERIMENT, R2 Top-7, cheap-killer drops, and the 0285/0252 conflict with the meta-audit. | `stage4_candidates.md` (new — **includes the recovered full 12-proposal panel**) |
| **Stage 5** killer specs | `research_ledger/stage5_killers.md` | ~0.8 KB | Engineer Top-5, engineer cuts, and the supervisor correction that 0276-M had been wrongly omitted. | `stage5_top5.md` (new) |
| **Stage 5** single-idea design | `research_ledger/stage5_0276.md` | ~0.5 KB | SEG-0276-M α-design, SSA controls, four numeric gates, cost, and the designer-vs-supervisor split. | `stage5_top5.md`, `stage6_battle.md` (new) |
| **Stage 5** cheap-killer designs | `research_ledger/cheap_killers_0252_0046.md` | ~0.7 KB | Cheap falsifiers for 0252 (`g ≈ ρ_H·ρ_M`) and 0046-M; the prior-art risk on 0046-M. | `stage5_top5.md` (new) |
| **Cross-cutting audit** (feeds Stage 5 and Stage 6) | `research_ledger/meta_audit.md` | ~1.2 KB | Supervisor ACCEPTS / REJECTS / PARTIAL on the auditor's challenge; the "Updated working Top-8"; the instruction to protect 0276 and 0240. | `stage5_top5.md`, `stage6_battle.md` (new) |
| **Stage 6** final 5 → 3 | **no ledger file exists** | — | Stage 6 is asserted by `Windows1/README.md` ("Stage 6 locked method + medical-safety characterization + medical uncertainty method") but was never written down. | `stage6_battle.md` (new — retrospective) |

---

## 4. Why these files stay at the repository root

**They are not moved, renamed, or deleted by this backfill. This is deliberate, not an oversight.**

1. **KNOWN FACT — the identical blobs are reachable from other branches.** The same 12 files, at the
   same paths, with byte-identical git blob hashes, appear on at least three other branches
   (`cursor/stage4-cluster-a-reviewer2-f1fa`, `…-b-…-b25a`, `…-c-…-c1be`). Those branches carry a
   *different* window's Stage-4 work (`A-`/`B-`/`C-` ID namespaces, a different supervisor) and merely
   inherited `research_ledger/` from their base commit. Relocating the directory on `main` would put
   a rename on the merge path of every such branch and turn a documentation cleanup into
   cross-window merge conflicts.
2. **KNOWN FACT — `research_ledger/` is a shared path, not a Windows1-owned one.** The branch
   `cursor/reviewer2-stage4-kill-panel-5733` writes a *new* file into the same directory
   (`research_ledger/stage4_reviewer2_kill_panel.md`). The directory is a shared drop-box for agent
   output across windows; it is not Windows1's private tree, so "move it under `Windows1/`" is not a
   correct normalization in the first place.
3. **An index is sufficient and reversible.** Attribution and navigability were the actual defects.
   Both are fixed by this file plus the backfilled per-stage records, with zero risk to other branches.

**Consequence to accept.** `Windows1/` is therefore *not* self-contained. Auditing Windows1 requires
the repository root as well. That trade is taken knowingly, and this file is the pointer that makes it
navigable. If a future round wants per-window ledgers, the right move is to write *new* files under
`Windows15/`-style window directories going forward, not to retro-move this shared directory.

---

## 5. Known gaps in the ledger (detail in `FUNNEL_DEVIATION.md`)

- **No Stage 6 file.** Backfilled retrospectively as `stage6_battle.md`; the original 5 → 3 session
  was never recorded.
- **Three of five Stage-1 pools are digest-only.** The full text of SEG-0001…0365, VFM-A 180 and
  ASM-A 180 is absent from this repository. `Windows1/selection_history/eliminated_ideas_summary.md`
  states "Full pools live in `/workspace/research_ledger/`" — that `/workspace/` path was a cloud
  worktree, and only the two local 350-idea pools were ever committed here.
- **No standalone survivor lists for Stages 3, 4 and 5.** Only kill sheets and fragments were kept.
  Reconstructed in this directory, with every unsupported row marked
  `NO RECORDED REASON — 需人工确认`.
- **A namespace error inside the ledger.** `stage3_vfm_kills.md` writes `A0263 constrained SAM-FT`,
  but the `A` namespace (VFM-A / ASM-A) only runs to 180 ideas. The referent is `VFM-0263` in
  `stage1_vfm_local_pool.md` ("Constrained FT: maximize target Dice s.t. SA-1B drop < ε"), which
  `stage4_reviewer2.md` correctly cites as `VFM-0263/0274`. Logged for human confirmation, not
  silently corrected.
