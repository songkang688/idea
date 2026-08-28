# Idea_02 — A-0028: SAM2/SAM3 teleport / appearance-vs-location probe

**Seat:** Windows2 / Idea_02 (ranked #2 of 3). **Status:** archived research package; synthetic instrument runnable.

## The claim (battle-locked)

> The distractor-fix papers (DAM4SAM arXiv:2509.13864; SAMURAI arXiv:2411.11922; SAM2/SAM3
> memory-design line arXiv:2512.22624) presuppose an appearance-vs-location arbitration nobody has
> measured — teleport probes measure it directly on SAM2 AND SAM3.

Killer experiment: **1 GPU-day** SAM2-L synthetic swap battery (~10⁴ clips), placebo arm first,
either outcome pre-registered as a finding. Full study: 3–5 GPU-days (SAM2 sizes + SAM3 + DAM4SAM +
SAMURAI + natural-cut validation), single 24 GB GPU, no training.

## Labeling rule (read first, binding on every file)

- **KNOWN** — published literature (URL given) or arithmetic.
- **HYPOTHESIS** — every statement about SAM2/SAM3/DAM4SAM/SAMURAI behavior. No SAM2 number exists
  anywhere in this package.
- **MEASURED (synthetic surrogate)** — numbers from `src/run_synthetic.py` on a surrogate memory
  tracker with a *known* arbitration parameter. These validate the instrument (the probe recovers the
  surrogate's ground-truth arbitration, Spearman ρ = 1.000; placebo disruption 0.000). They are a
  **SYNTHETIC SURROGATE** demonstration — not SAM2, and never presented as SAM2.

## The 28 sections — index

| Sections | File | Contents |
|---|---|---|
| 1–10 | `proposal.md` | candidate titles · battle-locked claim & provenance · executive summary · background · research questions · falsifiable hypotheses · pre-registered predictions (either-outcome table) · genre & positioning · contributions · evidence-labeling rule |
| 11–14 | `literature.md` | SAM2/SAM3 & memory-tracking lineage · the distractor-fix line and what it presupposes (mandatory citation set) · adjacent methodology (psychophysics, object permanence, compositing) · novelty statement & scoop analysis |
| 15–22 | `experiments.md` | method overview (+ architecture mermaid) · stimulus design (placebo + natural-cut arms, non-optional) · subject models · dummy brackets · metrics & statistical plan · **THE KILLER EXPERIMENT (pre-registered gates + RESULT SLOTS)** · full battery E1–E8 & compute budget · datasets & provenance |
| 23–24 | `reviewer_attacks.md` | Reviewer #2 attacks A1–A10 with adjudications (lead attack: "the fix-papers already exist") · residual-risk register R1–R8 |
| 25–28 | `roadmap.md` | binding week-one schedule & milestones · stop/pivot/kill/continue criteria (K1/K2, P1, S1, C1–C3) · paper skeleton, figures, venues · reproducibility, release, ethics/licensing |

Support directories: `diagrams/` (mermaid sources), `src/` (runnable prototype mirror),
`configs/` (synthetic configs + pre-registered killer-battery spec), `references/` (annotated
bibliography + BibTeX, all URLs verified this session).

## Runnable prototype (included, verified in this draft)

`src/` is a verbatim mirror of `Windows2/_wip/stage7_proto_A0028/` (Stage-7 Agent R; provenance in
`src/PROVENANCE.md`) — CPU-only, no GPU, no SAM2 weights, no network:

```bash
cd Windows2/_wip/package_draft_A0028/src
pip install -r requirements.txt                                  # numpy, PyYAML, pytest
python run_synthetic.py --config configs/default.yaml --out results_synthetic/   # ~30 s
python -m pytest tests/ -q                                       # 23 tests
```

Verified at packaging time: smoke run + all 23 tests pass on this mirror. The committed example run
(`src/results_synthetic/report.md`) contains the four synthetic experiments: E1 arbitration curves,
E2 instrument validation (λ-recovery ρ = 1.000), E3 memory-pollution mechanism, E4 placebo/flip
controls. The full per-cell JSON of the canonical run lives at
`Windows2/_wip/stage7_proto_A0028/results/results.json` (deterministically regenerable from the
config seed). The env-gated real-SAM2 adapter stub is `src/src/a0028/sam2_wrapper.py` (OFF by
default; requires `A0028_USE_REAL_SAM2=1` + checkpoint + config + torch/sam2).

## Provenance chain

Agent A (original, C02) → F keep → L revive #3 (PI_BINDING mandate) → N `exp_07.md` (protocol +
"fix-papers presuppose" reframing) → O top20 #6 → Q top5 #3 → S final3 #2 (fourth kill attempt
failed; week-one execution load-bearing) → R synthetic prototype → **this package (Agent V)** → PI
rank Idea_02. Binding conditions from the Stage-6 handoff are enumerated and honored in
`proposal.md` Section 2.
