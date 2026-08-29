# Evolution summary (Windows1)

## Process

Autonomous PI with ≤3 cloud sub-agents (`claude-fable-5-thinking-xhigh`). Two Stage-1 350-idea cloud runs **timed out**; supervisor wrote local VFM/ASM pools and re-dispatched 180-idea batches. Stage-2 reviewer initially blocked (cloud workspace had no idea text) and was resumed with the full SEG list.

## Generate → mutate → kill highlights

- **Killed as stated:** binary-smoke-as-novelty; watermark-learnability; LogME-style dense probes; unlabeled mIoU prediction as productization; worst-case valid SAM clicks (TETRIS); oracle-click vs human (RClicks); LoRA SVD truncate (PARA); ViT high-norm tokens (registers); replica-spiking inflation curve; typographic mask injection as a lead idea; frozen/tuned descriptive curves; linear CLIP→DINOv2 as lead (Platonic / CLIP-DINOiser).
- **Mutated and kept:** constrained SAM-FT must beat WiSE-FT; lesion suppression drops “universal”; disagreement fields evaluated with ordering-sensitive metrics not ECE.
- **Protected then cut at Stage 6:** SEG-0276-M shape-prior α (Reviewer #2 liked it; lost the eval slot to medical impact); SEG-0252 label ecology (cheap ρ_H·ρ_M design exists; external-validity circularity); 0046-M transmittance (matting / SMOKE5K AAAI 2022).
- **Meta-audit:** portfolio was over-indexed on eval science; medical/physics ideas had been over-killed by adjacency. Final 3 restores method + two medical.

## Clusters that fed the final 3

- SAM / PEFT / forgetting / dual objective (VFM-0263/0274, Stage-5 #1)
- Medical safety of enhancement pipelines (SEG-0085-M)
- Multi-rater uncertainty vs shift (SEG-0074-M; original infiltration-vs-histo form was KILL’d by RAPSODI/ProsRegNet/calibration papers)

---

## Appendix — 2026-08-29 selection-history backfill (retrospective)

Everything above this line is the original Windows1 record and is **unchanged**. This appendix was
appended after the Final 3 were locked, packaged and merged to `main`. It **re-opens no selection
decision** and changes no conclusion in `Windows1/README.md` or `Windows1/research_summary.md`.

### Why it was needed

Two defects in the *record*, not in the deliverables. First, the per-stage funnel files were never
under `Windows1/` — they are 12 files in the repository-root `research_ledger/`, so a reader starting
from `Windows1/` could not audit any stage. Second, Stage 6 was never written down at all: the 5 → 3
adjudication that produced the Final 3 left no primary record, even though every earlier stage kept a
kill sheet.

### Files added to this directory

| File | Purpose |
|---|---|
| `LEDGER_INDEX.md` | Attribution and location index for the 12 root `research_ledger/` files: which stage each covers, the evidence that each belongs to Windows1, and why they stay at the root. |
| `FUNNEL_DEVIATION.md` | Standard chain (1000+ → 200 → 50 → 20 → 5 → 3) against what Windows1 actually ran (1065 → ~84 → ~20 → 12 → 8 → 5 → 3), per level, with sources and a discrepancy list. |
| `stage3_survivors.md` | Stage-3 survivor list, inverted from the two kill sheets (20 SEG + 13 VFM decision units → 24 survivors). |
| `stage4_candidates.md` | All 12 Stage-4 proposals with the **recovered** Reviewer #2 panel. |
| `stage5_top5.md` | The documented Top-8, the engineer's Top-5, the supervisor correction, and a reconciled candidate set. |
| `stage6_battle.md` | Retrospective 5 → 3 record: three winners with binding obligations and death conditions, the runner-up's revival condition, and the recorded conflicts. |

### Stage 4 panel: RECOVERED

The full Reviewer #2 panel was found and indexed. `research_ledger/stage4_reviewer2.md` claims the
panel is on branch `cursor/reviewer2-stage4-kill-panel-5733` "(cloud worktree, **not this repo**)" —
**that parenthetical is wrong.** The branch is in this repository, and the panel
(`research_ledger/stage4_reviewer2_kill_panel.md`, 21,207 bytes, titled "Stage 4 — Reviewer #2 Kill
Panel (Windows1 PI)") was recovered from it: 12 proposals P1–P12, each with rejection, hidden
assumption, confounder, missing baseline, trivial alternative, shut-me-up experiment and verdict. Its
Top-7 matches the summary line in `stage4_reviewer2.md` exactly.

The three sibling branches `cursor/stage4-cluster-{a,b,c}-reviewer2-*` were also checked and are
**not** Windows1: they are headed "Supervisor Windows7", use `A-`/`B-`/`C-` ID namespaces disjoint from
Windows1's, and cover unrelated subject matter. They carry `Windows1/` and `research_ledger/` only
because they branched from a commit that already had Windows1 merged.

### Confirmed not recoverable

- **The Stage-6 session.** No transcript, vote or per-candidate scoring survives. `stage6_battle.md`
  is explicitly labelled retrospective and is built from `README.md`, `reviewer_summary.md`, this file,
  `meta_audit.md`, `stage4_reviewer2.md`, `stage5_0276.md` and `cheap_killers_0252_0046.md`. Stage 6
  is confirmed to have *occurred* by three independent attestations, including the three dissents
  recorded above in `reviewer_summary.md`.
- **Which five candidates entered Stage 6.** Four are certain (Constrained SAM-FT, 0085-M, 0074-M,
  0276-M) and 0252 is near-certain, but the engineer's Top-5 and the "likely final-3 pool" in
  `stage5_killers.md` are two different five-entry lists and neither can be the operative one.
- **No Stage-2 review of the VFM/ASM pools.** The Stage-2 blockage noted above was resolved for the
  SEG list only; `stage2_seg_review.md` closes with "Global 1000 not yet complete: waiting VFM + ASM
  pools" and no such sheet was ever written. One consequence: Idea_01's ancestors (VFM-0263/0274)
  entered at Stage 3 with no Stage-2 scoring.
- **Full idea text for three of five Stage-1 pools.** SEG-0001…0365, VFM-A 180 and ASM-A 180 exist
  only as keeper digests. The `/workspace/research_ledger/` path cited in
  `eliminated_ideas_summary.md` was a cloud worktree; only the two local 350-idea pools were committed.
- **Ten Stage-3 survivors that vanish before Stage 4** (SEG-0019, 0054, 0031, 0122; A0051, A0028,
  A0166, A0073, A0021, A0109), each marked `NO RECORDED REASON — 需人工确认`.
- **Slate letter "C".** The Final 3 are labelled A/B/D; no "C" appears anywhere in the archive.

### Referred for human adjudication (not corrected here)

- Stage-2 bucket counts in `reviewer_summary.md` (31/8/14/4) do not match the ID lists in
  `research_ledger/stage2_seg_review.md` (23/6/15/4, summing to its own "Named-48" header). Only the
  KILL count agrees.
- `stage3_vfm_kills.md` writes `A0263`, but the A-namespace holds 180 ideas; the referent is
  `VFM-0263`.
- `0274` is ambiguous: `SEG-0274` was KILLed at Stage 2, while `VFM-0274` is an ancestor of Idea_01.

### Constraints observed

`research_ledger/` was **not** modified, moved or renamed — all 12 blob hashes are unchanged, and the
rationale for leaving them at the root is in `LEDGER_INDEX.md` §4. No file under
`Windows1/Idea_01|02|03/` was touched, including the three 52-byte `proposal.md` pointers, which are
intentional pointers to each package's `README.md` and not stubs. `Windows1/README.md` and
`Windows1/research_summary.md` are unchanged. The epistemic labels from `README.md` (KNOWN FACT /
EVIDENCE / HYPOTHESIS / MODEL SPECULATION / EXPECTED RESULT / ACTUAL EXPERIMENTAL RESULT) are used
throughout; **no number in the new files is labelled ACTUAL EXPERIMENTAL RESULT**, because no
experiment was run this round. The caveats in `stage2_seg_review.md` — "Scores are REVIEWER JUDGMENT
not facts" and "Do not treat Pub=L as verified novelty" — are honoured: the backfill reports decisions
and their stated rationales without re-asserting reviewer scores as findings.
