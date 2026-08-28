# A-0028 synthetic teleport-probe report

Config: `configs/default.yaml` — runtime 30.1s, CPU only, no SAM2, no weights.

**Every number below is MEASURED on the synthetic surrogate memory tracker**
(a SAM2-*style* memory bank with a known arbitration parameter lambda_loc).
**No SAM2 behavior is measured here.** SAM2/SAM3 predictions remain
EXPECTED (hypothesis) — see README and `Windows2/_wip/stage5_agent_N/exp_07.md`.

## E1 — arbitration curves (swap condition, surrogate lambda_loc=0.5)

P(follow-place), marginal over the other two axes:

| displacement d (px) | 4 | 8 | 16 | 32 | 64 |
|---|---|---|---|---|---|
| P(follow-place) | 0.168 | 0.482 | 0.917 | 0.996 | 0.999 |

| temporal gap g (world steps) | 1 | 2 | 4 | 8 | 16 |
|---|---|---|---|---|---|
| P(follow-place) | 0.726 | 0.715 | 0.721 | 0.711 | 0.690 |

| distractor similarity s (cosine) | 0.2 | 0.5 | 0.8 | 0.95 |
|---|---|---|---|---|
| P(follow-place) | 0.574 | 0.650 | 0.770 | 0.856 |

Dummy brackets on the same swap grid (mean P(follow-place) over all cells):

- `location_prior_dummy`: 0.892
- `appearance_matcher_dummy`: 0.030

## E2 — instrument validation (the probe is the claim)

| true lambda_loc | probe location-prior index |
|---|---|
| 0.1 | 0.209 |
| 0.3 | 0.641 |
| 0.5 | 0.780 |
| 0.7 | 0.907 |
| 0.9 | 0.940 |

Spearman rho(lambda, index) = **1.000** (monotone recovery: True).

## E3 — identity continuation (memory pollution) at cell {'displacement': 16, 'gap': 4, 'similarity': 0.5}

| lambda_loc | memory update | P(wrong at manip) | P(persist given wrong) | P(recover given wrong) | template affinity gap (mean) |
|---|---|---|---|---|---|
| 0.2 | on | 0.010 [0.003, 0.029] | 1.000 [0.438, 1.000] | 0.000 [0.000, 0.562] | -0.609 |
| 0.2 | frozen | 0.030 [0.016, 0.056] | 0.222 [0.063, 0.547] | 0.778 [0.453, 0.937] | -0.431 |
| 0.5 | on | 0.970 [0.944, 0.984] | 1.000 [0.987, 1.000] | 0.000 [0.000, 0.013] | +0.578 |
| 0.5 | frozen | 0.870 [0.827, 0.903] | 0.812 [0.760, 0.855] | 0.188 [0.145, 0.240] | -0.431 |
| 0.8 | on | 0.993 [0.976, 0.998] | 1.000 [0.987, 1.000] | 0.000 [0.000, 0.013] | +0.609 |
| 0.8 | frozen | 0.960 [0.931, 0.977] | 0.906 [0.867, 0.935] | 0.094 [0.065, 0.133] | -0.431 |

Positive template affinity gap = the memory bank now encodes the
distractor's appearance (representation-level identity continuation).

## E4 — Reviewer-2 controls

- Placebo (paste-artifact only, nothing moves): disruption rate **0.000** (follow-object 1.000 [0.987, 1.000]).
- Appearance flip (no move): follow-object 1.000 [0.987, 1.000], lost 0.000 [0.000, 0.013].

placebo = paste-artifact-only, nothing moves; if trackers were disrupted here the probe would measure compositing artifacts, not appearance-vs-location arbitration.
