# Idea_03 — B-0114: 4-arm dense-task VPT-as-registers

**Seat:** Windows2 / Idea_03 (ranked #3 of 3). **Status:** archived research package; synthetic 4-arm prototype runnable.

> **Binding constraint (PI_BINDING.md):** the original "afternoon frozen-token pilot" is **struck** —
> VPT's own Fig. 11 Prompt-Fixed ablation already ran it on classification (Jia et al., ECCV 2022,
> arXiv:2203.12119). Only the 4-arm *dense-task* mechanism form is packaged here. The original VPT
> Fig. 11 result is **NOT the flagship** of this project; it is the *control this project must reproduce*
> and the *pre-registered failure mode it must survive*.

> **Provenance banner:** every measured number in this package comes from the CPU **synthetic sandbox**
> under `src/prototype/` (Stage-7 Agent T) and is labeled **sandbox-only**. No ADE20K / Cityscapes /
> NYUv2 / ImageNet / DINOv2 number exists in this package. The sandbox's own content-dominant outcome
> is reported as a **HYPOTHESIS-level risk** (§20, §26), never as a dense-task finding.

---

## One-line claim (battle-locked, Stage-6 `final3.md`)

VPT's dense-task gains are partly **register function** — token arms dissociate register absorption
from added capacity, and the norm-map arm tests artifact maps as free uncertainty.

## Killer experiment (one sentence)

A **4-arm × 2-backbone × 3-seed grid (24 runs) on ADE20K** — full VPT vs frozen-random tokens vs
attention-bias-only vs no-token, on **register-free DINOv2 vs register-equipped DINOv2-reg** — with a
pre-registered decomposition table and the directional test H2 (VPT gains more on the register-free
sibling); **STOP** the mechanism claim if learned embeddings fully explain the gains (the dense-task
replica of VPT Fig. 11).

---

## The 28 sections — index and file map

| § | Section | File |
|---|---------|------|
| 1 | Candidate titles | `proposal.md` |
| 2 | Battle-locked claim & seat definition | `proposal.md` |
| 3 | Executive summary / abstract | `proposal.md` |
| 4 | Provenance & pipeline lineage | `proposal.md` |
| 5 | Research question | `proposal.md` |
| 6 | Falsifiable hypotheses & pre-registered predictions | `proposal.md` |
| 7 | Contributions (conditional on outcomes) | `proposal.md` |
| 8 | Method — arms, decomposition, backbone pair | `proposal.md` |
| 9 | Architecture & system design (mermaid) | `proposal.md` + `diagrams/` |
| 10 | Literature — the VPT / PEFT line (incl. Fig. 11) | `literature.md` |
| 11 | Literature — the register / artifact line | `literature.md` |
| 12 | The connection in print & exact novelty residual | `literature.md` |
| 13 | Mandatory citation set & freshness protocol | `literature.md` + `references/` |
| 14 | Killer experiment specification (24-run grid) | `experiments.md` |
| 15 | Binding ordering condition — exp_02 gate & B-0001 arm | `experiments.md` |
| 16 | Full experiment matrix beyond the killer | `experiments.md` |
| 17 | Metrics & statistical analysis plan | `experiments.md` |
| 18 | Pre-registered interpretation table | `experiments.md` |
| 19 | Stop / pivot / kill criteria | `experiments.md` |
| 20 | Prototype status & sandbox results (sandbox-only) | `experiments.md` + `src/` |
| 21 | Confounds & threats to validity | `experiments.md` |
| 22 | Reviewer-2 attack record (Stage-4 H) & answers | `reviewer_attacks.md` |
| 23 | Anticipated fresh attacks & pre-drafted rebuttals | `reviewer_attacks.md` |
| 24 | Resource plan (GPU / VRAM / calendar) | `roadmap.md` |
| 25 | Milestones & decision points (week-one plan) | `roadmap.md` |
| 26 | Risk register, scoop watch & obsolescence clock | `roadmap.md` |
| 27 | Publication plan & dissociation from B-0001 | `roadmap.md` |
| 28 | Reproducibility, data & promotion checklist | `roadmap.md` |

## Layout

```
package_draft_B0114/
├── README.md            # this file: seat, banners, 28-section index
├── proposal.md          # §1–§9
├── literature.md        # §10–§13
├── experiments.md       # §14–§21
├── reviewer_attacks.md  # §22–§23
├── roadmap.md           # §24–§28
├── diagrams/
│   ├── architecture.mmd     # real-experiment system diagram (mermaid)
│   └── decision_gates.mmd   # exp_02 gate → grid → interpretation-table flow
├── src/
│   ├── README.md            # wrapper: what is prototype, what is real
│   └── prototype/           # verbatim copy of _wip/stage7_proto_B0114 (Agent T)
├── configs/
│   ├── README.md            # real-run config drafts vs prototype configs
│   ├── exp02_gate.yaml      # the binding pre-grid gate (B-0001 decision)
│   ├── killer_ade20k.yaml   # the 24-run killer grid
│   ├── token_sweep.yaml     # K ∈ {1,4,16,64} confound bound
│   └── classification_control.yaml  # Fig.11 reproduction control
└── references/
    └── references.md        # annotated bibliography with URLs + verification labels
```

## Reading order

PI review: `proposal.md` → `experiments.md` §18–§19 (interpretation table + stops) → `roadmap.md` §26.
New collaborator: this README → `proposal.md` → `literature.md` → `experiments.md` → `src/README.md`.
Reviewer simulation: `reviewer_attacks.md` first.

## Git safety

This package writes **only** `Windows2/_wip/package_draft_B0114/`. The sibling packages (C-0306,
A-0028) are owned by Agents U and V. `Windows2/Idea_03/` is not created by this draft.
