# Roadmap — B-0114: Prompts as Registers

Sections §24–§28.

---

## §24 Resource plan (GPU / VRAM / calendar)

| Item | Compute | Notes |
|---|---|---|
| exp_02 gate (binding, first) | ~1 GPU-week, one 24–40 GB GPU | probe training hours-scale; I/O-dominated analysis |
| E0 classification control | ~2 GPU-days | prerequisite; bug detector |
| E1 killer grid (24 runs) | **1–1.5 GPU-weeks**, one A100-40GB (fits 24 GB, ViT-B frozen) | 24 × 6–10 h; prompts + head only trainable |
| E2 sink-only arm | ~1 GPU-day | register-free cells only |
| E3 K-sweep | ~3 GPU-days | arms (a),(b), register-free |
| E4 VPT-deep | ~4 GPU-days | |
| E5 Cityscapes + NYUv2 | ~1 GPU-week | |
| E6 supervised patched pair | ~4 GPU-days | PH-Reg / test-time-register patching |
| **Total to killer decision** | **≈ 2.5–3 GPU-weeks** (gate + E0 + E1) | |
| **Total full study** | **4–6 GPU-weeks** | N exp_01 estimate; entered only from a live §18 cell |

No annotation cost (all datasets standard). Storage: cached frozen features for ADE20K/ViT-B ≈
low-hundreds of GB if precomputed; optional — arms can run end-to-end frozen instead.

## §25 Milestones & decision points (week-one plan is binding, from S `final3.md`)

**Week 1**
- Days 1–2: **launch exp_02** (the binding ordering condition — dissociation/merge decision for the
  register micro-field and the B-0001 arm's live-or-die test).
- Days 1–5 (parallel, infrastructure only): token-injection wrapper + attention-bias module
  (test-time-registers construction, arXiv:2506.08010); port the prototype's arm interface
  (`src/README.md` migration map).
- Days 3–5: **E0 classification control** — must reproduce Prompt-Fixed ≈ Linear (VPT Fig. 11) on a
  small run. Failure ⇒ HALT (bug), fix before anything else runs.
- Freshness re-search logged at proposal freeze (§13 protocol).

**Week 2**
- exp_02 returns → **gate verdict**: B-0001 arm dropped or kept (kept = reported under B-0001 only).
- **Commit the 24-run killer grid** (E1) only after the gate verdict. Launch E1.

**Weeks 3–4**
- E1 lands → read against the pre-registered interpretation table (§18). Decision point:
  - K1 → STOP mechanism claim; write deflationary/merged note; notify PI (B-0194 activation decision).
  - P1 → PIVOT to retrofit paper; E-matrix re-prioritized to substitution benchmarks.
  - M1/M2/K2/X* → fund E2–E7 per table row.
- Freshness re-search at experiment freeze.

**Weeks 5–8 (live-cell branches only)**
- E2–E6 complete; E7 analysis; paper draft against the branch title (§1); internal Reviewer-2 pass
  runs `reviewer_attacks.md` §23 as a checklist.

**Standing rule:** any milestone slipping past the quarter boundary triggers the calendar kill review
(§26 R3) — this seat is the portfolio's only now-or-never clock.

## §26 Risk register, scoop watch & obsolescence clock

| ID | Risk | Likelihood / basis | Mitigation / consequence |
|---|---|---|---|
| R1 | **K1 kill cell: dense tasks replicate Fig. 11** (all gain is learned content). Credence raised by the sandbox's content-dominant outcome — logged as HYPOTHESIS-level input, not a dense-task finding (`experiments.md` §20) | material; the toy built to favor the mechanism still came back content-dominant | pre-registered STOP + pre-drafted deflationary title (§1.4); merged-note home with exp_02; seat degrades honestly; **B-0194 activates without a new battle** |
| R2 | **Mush** (outcome outside every §18 row) | bounded by 2-backbone axis + sink arm + K-sweep | pre-registered handling: no headline; merged-note mechanism half; PI decides replacement |
| R3 | **Obsolescence clock**: register-free backbone population decays every quarter (DINOv3 ships register-equipped by default — arXiv:2508.10104) | certain, calendar-driven | binding start-this-quarter condition; H2 arm converts the decay into the paper's boundary law; measurement window, not claim value, is what expires |
| R4 | **Scoop**: (i) test-time-registers group extends 2506.08010 to PEFT-gain attribution; (ii) DA-VPT authors follow their own future-work sentence; (iii) a registers survey adds a VPT row | fastest-moving micro-field in the portfolio; 4+ papers moved during this pipeline's own run | freshness re-search at proposal freeze + experiment freeze (§13); kill trigger = printed dense-task token-arm mechanism paper; mitigation is speed (killer = 24 cheap runs) |
| R5 | **exp_02 upstream scoop** (norm-as-uncertainty paper prints) | flagged by H and L as the fastest check | immediate re-search + PI escalation before the gate runs (N exp_02 lock) |
| R6 | **Softmax-denominator residual** survives all bounds | certain (bounded, not eliminated) | stated in print; claims scoped to what (c)/(e)/K-sweep triangulate (§21.1) |
| R7 | **Backbone-pair run-variance objection** | anticipated (R2-3) | E6 patched-sibling within-run control; direction must agree across pair types |
| R8 | **Sandbox anchoring** (team or reviewers read §20 as evidence) | possible | provenance banners everywhere; §18 predates sandbox and is locked; R2-8 pre-drafted answer |
| R9 | **Compute slip** stretches E1 past the gate window | low (single-GPU scale) | E1 is 24 independent runs — trivially parallel; any 8-GPU day collapses the calendar |

**Scoop-watch queries (logged each freeze):** "visual prompt tuning registers", "prompt tokens
attention sink dense", "register tokens PEFT", "attention bias injection ViT dense prediction",
"VPT mechanism dense segmentation" — arXiv listing date-restricted since last search.

## §27 Publication plan & dissociation from B-0001

**Branch → venue map** (titles from `proposal.md` §1):

| Branch (§18) | Output | Venue class |
|---|---|---|
| M1 / M2 / K2 | full mechanism paper (§1.1/§1.2/§1.5) | CVPR/ICCV/NeurIPS main track |
| P1 | retrofit method paper (§1.3) | CVPR/ECCV main track (method) |
| K1 | deflationary note (§1.4), or mechanism half of the **merged registers paper** with exp_02's audit | short-paper track / workshop / merged full paper if exp_02 also deflates |
| mush | mechanism half of merged exp_02 note only | per PI decision |

**Dissociation from B-0001 (PI binding: one bet unless dissociated — enforced, not asserted):**
- Claim level: this project answers *mechanism attribution* (where do VPT's dense gains come from);
  B-0001 answers *consequence/utility* (is the artifact-norm map usable error signal). Neither implies
  the other; no shared headline term beyond "registers".
- Operational level: **this paper makes no uncertainty claims**; exp_02 contains no PEFT anywhere.
- Code level: the norm-vs-error hook is quarantined (`b0001_hook.py`), flag-gated, banner-printed, and
  import-isolated — enforced by AST tests in the prototype and to be re-enforced at scale (§15).
- Decision level: exp_02 runs first and its pre-registered rule decides merge vs two-paper (§15).

**Authorship/credit note for the PI:** if the merged-note branch fires, the merged registers paper
carries both experiment teams; the Stage-6 record (S `final3.md`, this package) is the pre-registration
trail for both.

## §28 Reproducibility, data & promotion checklist

**Reproducibility commitments:**
- All experiment configs are versioned YAML (`configs/`); seeds fixed and logged; the runner separates
  EXPECTED (pre-registered) from MEASURED blocks (prototype invariant carried to scale).
- Frozen-backbone checkpoints pinned by hash (DINOv2 / DINOv2-reg release artifacts; test-time-register
  code pinned to the released repo commit).
- The decomposition's telescoping identity is asserted programmatically on every run; CI runs the
  prototype's 39-test suite (CPU, seconds) on every push.
- Every table in the eventual paper regenerates from logged JSON dumps (`--json` pathway exists in the
  prototype runner today).

**Data statement:** ADE20K, Cityscapes, NYUv2, and the VTAB-style classification triplet under their
standard research licenses; no new data collected; no human subjects; no annotation spend.

**Ethics/impact note:** mechanism-analysis project on public checkpoints; principal impact is
methodological (how the community attributes PEFT gains and whether a training-free substitute exists);
no dual-use surface identified.

**Promotion checklist (`_wip/package_draft_B0114/` → `Windows2/Idea_03/`) — PI sign-off required on all:**
1. PI has read §18–§19 (interpretation table + stops) and §26 (risk register) and countersigned the
   binding conditions (exp_02 ordering; quarter clock; Fig. 11-replica STOP).
2. Freshness re-search at proposal freeze logged with zero kill-trigger hits (§13).
3. exp_02 scheduled on group compute (the gate is the calendar anchor).
4. Sibling packages (C-0306 Idea_01, A-0028 Idea_02) promoted or explicitly sequenced — portfolio
   ranking is C-0306 #1, A-0028 #2, B-0114 #3; this package does not jump the queue.
5. `Windows2/README.md` / `research_summary.md` ledger updates are made by the supervisor at promotion
   time (deliberately **not** edited by this draft).
