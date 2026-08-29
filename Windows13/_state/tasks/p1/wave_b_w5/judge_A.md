# P1 Wave B — w5_NPO — Judge A (hypothesis-level dedup) — Windows13

- **windows_id / windows_path:** Windows13 (window_locked: true)
- **branch:** `cursor/p1-wave-b-w5-judge-a-dedup-3de9`
- **canonical master (READ-ONLY):** `origin/cursor/p1-wave-b-w3-gate5-repair-f611` → `Windows13/_state/ideas_master.jsonl` (**638** lines). Not rewritten, not appended.
- **inputs (this wave):**
  - gen_n `origin/cursor/p1-gen-n-scaling-memorization-4814` — scaling / memorization / data laws — 100 ideas
  - gen_p `origin/cursor/p1-gen-p-constructive-6c3b` — constructive capability — 104 ideas
  - gen_o `origin/cursor/p1-gen-o-hard-domain-acc5` — hard-domain diversifier — 100 ideas
- **collision-only (wave_b_w4, flag-only, NOT merged here):** gen_k (105), gen_l (100), gen_m (100)

## Verdict summary

| | gen_n | gen_p | gen_o | total |
|---|---|---|---|---|
| input | 100 | 104 | 100 | **304** |
| keep | 86 | 87 | 98 | **271** |
| kill_or_merge | 14 | 17 | 2 | **33** |

- within-wave duplicate groups: **27** (28 kills; all within-shard, 0 cross-shard groups — the three mandates are near-orthogonal)
- master collision groups: **5** (5 kills into accepted master ids); standalone known-result kills: 0
- master collision **flags** on keeps: **47**; off-master (gen_k/l/m) flags on keeps: **17**
- permutation families flagged: **50** (170 unique flagged ids); family merge triggers fired: **6** (+1 cell at cap without merge)
- anomalies protected: **23**; deliberate tensions: **7**; judge clusters: **32**

`kill_or_merge` is a redundancy disposition, not a quality verdict; merged content survives through its primary or master target.

## Method

Hypothesis-level comparison on `core_hypothesis` content (mechanism + falsification design), not title strings. Two ideas are duplicates when they assert the **same mechanism with the same falsification design**, differing only in substrate (task, modality, metric, or the X-slot of a template). Lexical token-Jaccard scans found **no within-wave pair above 0.23, none vs the 638 master above 0.20, none vs gen_k/l/m above 0.18** — duplication in this wave is purely hypothesis-level, exactly as the w2 diversity audit predicted for later waves. The four top lexical pairs were manually adjudicated: P-061/P-065 (0.221) merged; P-004/P-027 (0.218) merged; P-072/P-075 (0.203) merged; N-055/N-068 (0.203) kept as genuinely distinct mechanisms (pre-training risk prediction vs shadow-model replacement).

**Family membership as MERGE TRIGGER (cap ≤6 kept primaries per cell).** Cells were assigned at *mechanism* level, not topic level. Six cells fired or co-fired:

1. `amodal_extent_geometry` — 8 candidates → 6: merged P-049→P-047 (T-junction order source into order-supervision sufficiency; one pipeline) and P-051→P-048 (amodal-overlap suppression into amodal-extent assignment; one "replace visible-IoU" program).
2. `decode_time_structural_constraints` (vision cell) — 8 → 6: merged P-075→P-072 and P-076→P-072 (support-relation and panoptic-exclusion slices of one relation-statistics rescoring mechanism), and P-083→P-074 (taxonomy back-off decoding, one procedure across classification and tail detection).
3. `long_tail_capability` — 7 → 6, satisfied by the shared P-083→P-074 merge.
4. `weight_space_merging` — 7 → 6: merged P-063→P-070 (assignment-mechanism identity is the sharpened, checkable form of decoder-family compatibility).
5. `annotation_convention_control` — co-fired at cap: merged P-015→P-014 (rater-embedding conditioning is the rater-level substrate of convention-token conditioning) alongside the master kill P-021→B-095; the master's annotation-convention family is already over-occupied per the w2 ruling, so this wave's constructive convention ideas keep only 4 primaries.
6. `eval_statistics_certificates` — 7 → 6: merged P-027→P-004 (segmentation power tables are the MDD certificate's substrate swap).

One cell sits **at** cap without merges: `resolution_as_scaling_axis` (N-002, N-003, N-018, N-019, N-030, N-095) — six distinct manipulations and measurement families; recorded for Stage-2 slot pressure.

**Granularity judgment call (recorded for the consolidator):** gen_o's clusters are large (microscopy keeps 13) but span genuinely distinct physical mechanisms; a topic-level cell assignment would fire caps against gen_o's cross-domain physics templates. Those templates are instead **permutation-flagged**, following w3 precedent (its 17-member `cheap_predictor_of_outcome` family was flagged and kept, not merged). The diversifier mandate argues against collapsing distinct physics into one slot; a consolidator who disagrees should start from the `flagged_permutation` table in `judge_A.json`.

## Master collision groups (kills into master)

1. **mg01** N-054 → **J-038**. J-038 (accepted) owns the sigmoidal duplication→memorization dose law with capacity-shifted midpoint and the dedup-policy payoff. N-054 re-asserts the identical knee law with the identical inject-at-controlled-duplication falsification, in discriminative-membership substrate. This closes the reconciliation duty the w3 judge logged as "J-038 vs N-053/N-054/N-055": N-054 dies; N-053 (capacity-scaling forecast at fixed data) and N-055 (pre-training risk prediction from data properties alone) keep with flags.
2. **mg02** N-070 → **J-074**. Distillation preferentially transfers per-item memorization signal to students; same student-side attack falsification, generative→discriminative substrate swap. Likeliest resurrection candidate of the wave.
3. **mg03** P-021 → **B-095**. Set-valued best-match scoring against multi-rater ground truth is the protocol instantiation of accepted distribution-matching evaluation; same ranking-flip falsification stratified by ambiguity.
4. **mg04** P-034 → **D-096**. Headroom/noise-ceiling-normalized leaderboards generalize accepted noise-floor-normalized strict-IoU metrics; same estimate-ceiling-then-count-flips design.
5. **mg05** P-087 → **A-094**. Learned next-click policy vs accepted gradient-derived click advisor: same "model-derived expected-improvement click placement beats current practice" hypothesis, same clicks-to-quality falsification; advisor construction is an implementation slot.

## Notable within-wave merges (12 in gen_n, 13 in gen_p, 2 in gen_o)

Full reasons in `judge_A.json.duplicate_groups`; highlights:

- **N-011 ← N-099** (scaling structure is a corpus property, architecture-invariant; exponent-equality and break-alignment are parameters of the same fitted curves; N-099's corpus-recomposition arm survives as the escalation experiment).
- **N-052 ← N-059** (near-identical similarity-stratified ladder designs; emergence-as-retrieval and late-scale-gains-as-memorization are two readings of one curve).
- **N-057 ← N-081** (context-keyed replay of duplicated instances in dense models; failure-mode audit and black-box extraction are the same signal, benign and adversarial).
- **N-065 ← N-071** (params-per-unique-image membership-risk law; "bigger is not leakier along the joint path" is one diagonal of the collapsed surface).
- **P-002 ← P-030** (frozen decoding contract + frozen container = one frozen-reference-harness repair of master C-077's harness variance).
- **P-007 ← P-011** (model-verified completion of incomplete test labels; COCO instance arm + federated LVIS rare-class arm).
- **P-065 ← P-061** (cheap-map head reuse across frozen backbones; see top novelty risk below).
- **O-046 ← O-055** (grammar-constrained 2D decoding: table grids and math expression trees are substrate slots of one structural-error-elimination mechanism).
- **O-065 ← O-072** (phenology-grounded time re-parameterization: thermal-time/cross-year and local-phase/hemisphere are substrate slots).

## Master collision flags on keeps (47)

Dominant pattern: **gen_p is the constructive mirror of the master's C/D-shard evaluation critiques** — P-001/P-004 answer C-073/C-054, P-002 answers C-077, P-007/P-017/P-022 answer D-093/D-083, P-023 answers D-099, P-026/P-035 answer C-032/C-029, P-029 answers C-042/C-075, P-031 answers C-034, P-038/P-100 answer D-045/D-097, P-048/P-054 answer D-049, P-086/P-089/P-092 answer A-095/A-096/B-026+A-092. These are family-adjacent constructive counterparts, kept with flags — not duplicates, because the mechanism proposed (a shipping protocol) differs from the accepted pathology finding.

gen_n's memorization/contamination block stands on accepted master ground and is flagged accordingly: N-042/N-053/N-062/N-067 on J-038; N-057 on H-043/H-098; N-084/N-087 on C-023/C-032/F-086; N-091 on C-052; N-092 on C-024; N-035/N-041 on F-101; N-023 on F-097.

**Top novelty-risk keeps:** P-065 (vs **J-009** — kept only for the orthogonality clause and encoder-zoo generalization; dies into J-009 if judges B/C read J-009 as owning the mechanism), P-060 (vs A-039/J-008 and the published registers literature), P-094 (translational relation embeddings echo TransE-style methods — unchecked judge hypothesis), P-014 (vs B-017/B-020/B-021), P-005 (vs D-024/D-078), N-062/N-067 (instrument/tail claims standing on J-038).

## Off-master collision flags (gen_k/l/m, wave_b_w4) — 17 keeps

Strongest reconciliation duties for the w4/w5 consolidation:

- **O-005 vs K-018/K-013**: non-pinhole radial depth-error correction — same mechanism, underwater flat-port vs general-lens substrate. Closest cross-wave pair.
- **O-079 vs K-017**: metric scale for monocular depth from auxiliary physical cues (attenuation vs known-size objects).
- **P-055 vs K-003**: K-003 claims learned feature upsamplers corrupt sub-pixel geometry — the exact artifact P-055 ships as a universal plug-in. Cross-wave tension.
- **P-007 vs L-051**: correlated model errors defeat consensus — L-051 is a direct threat to P-007's mechanism.
- **N-050 vs M-058**: onset order data-determined and corpus-reshufflable (N-050) vs optimization-forced and resampling-invariant (M-058). Direct cross-wave contradiction, logged as tension 7.
- Also: N-027 vs K-014; N-030 vs K-005; N-036 vs M-087/M-093; N-045 vs M-057; N-058/N-088 vs M-083/M-034; P-050/P-079 vs M-070; P-052 vs K-079/K-080; P-057 vs K-020; P-059 vs K-041; P-002 vs L-097.

## Permutation flags (50 families, 170 unique ids)

The wave's dominant templates:

- **`decode_time_structural_constraints`** (9 kept across P+O after three in-cell merges) — "enforce domain structure at decode time; violations vanish at no headline cost." First in line for Stage-2 slot caps.
- **`cheap_predictor_of_outcome_w5`** (N-021, N-055, N-065, O-018, O-092, O-095) — direct continuation of w3's dominant 17-member family.
- gen_o's physics templates: `illumination_direction_artifacts` (7), `physics_channel_injection` (6), `artifact_as_signal` (5), `attenuation_inversion` (5), `physical_sampling_standardization` (3), `narrowband_nuisance_removal` (3), `prior_vs_pixel_substitution_audits` (3).
- gen_n's law templates: `resolution_as_scaling_axis` (6, at cap), `memorization_dose_response` (4), `leakage_persistence_through_stages` (4), `capacity_data_memorization_surface` (3), `planted_canary_instrumentation` (4, cross-shard with P-033).

## GATE-5 / GATE-6

Mechanical audit (digit in `falsifiable_prediction`; `evidence_label` dict present): **gen_n 100/100 + 100/100; gen_p 104/104 + 104/104; gen_o 99/100 thresholds + 100/100 labels.** The single exception is **O-007**, whose kill condition is quantitative but spelled in words ("kill if the synthetic slope is less than one-quarter of the real slope"). Flagged in its `judge_A_meta.gate5`; **not** rewritten — pinning it to digits is judge B's confirmation step, not a fabrication opportunity. Unlike w3, **no retrofit block is needed**: w5 can merge threshold-complete pending that one confirmation.

GATE-6 recorded, not enforced: gen_p self-declares wholesale `constructive_capability` and gen_o is characterization/audit-heavy; genre labels must be re-audited against claim phrasing before genre quotas are applied.

## Anomalies protected (23)

N-004 (scaling-fit functional-form degeneracy), N-007 (transfer ossification), N-024 (text-in-image threshold behind OCR abilities), N-046 (object grouping as attention-graph percolation), N-069 (membership as a property of the image via crawl overlap), N-073 (MI evaluation measures crawl provenance), N-077 (redact-then-encode fails), N-082 (retroactive embedding-privacy decay), N-087 (label-free SSL contamination), N-100 (more data hurts minority domains), P-052 (proposals for fully hidden objects), P-060 (register retrofit), P-097 (exemplar-difference queries), O-018 (ripple-ratio difficulty law), O-028 (PSF-convolved colocalization null), O-038 (MIL attention ≠ localization), O-066 (seasonal-null baseline), O-071 (Kelvin-wake velocimetry for free), O-079 (underwater metric depth from attenuation), O-083 (Rose-criterion photon-budget ordering), O-087 (frozen/FFPE natural experiment), O-089 (x-height master curve), O-096 (nominal-set redundancy audit).

## Deliberate tensions (7 — adjudicate by experiment, not dedup)

1. N-029 vs N-010/N-098: universal shared per-concept exponent vs granularity- and slice-heterogeneous exponents.
2. N-040 vs N-062/J-038-family: near-duplicates as free hard positives vs duplication as the memorization dose — the dedup threshold is a utility–privacy operating point.
3. N-035 vs N-042: repetition tolerance vs memorization onset preceding utility loss on the same epoch axis.
4. P-079 vs P-098: exploit context co-occurrence vs train context invariance (N-033's dose-response is the arbiter).
5. P-092 vs master B-026: training away prompt-jitter variance destroys the ambiguity signal B-026 harvests.
6. N-047 vs P-093/P-095: binding limited by data decorrelation vs recoverable by architecture on existing data.
7. N-050 vs gen_m M-058 (cross-wave): acquisition order data-forced vs optimization-forced.

## Caveats and handoff

- **No novelty verification** was performed; every prior-art remark above is an unverified judge hypothesis; no citations were used or invented. All counts are computed mechanically from the disposition table; Jaccard figures are computed from the shards; no numbers invented.
- Resurrection candidates among kills: N-070, P-034, N-081 (as N-057's extraction arm), P-011 (as P-007's federated arm).
- gen_k/l/m judge outputs (wave_b_w4) were not discoverable on origin at judge time; the 17 off-master flags here are one-directional and need w4-side reconciliation.
- Recommended next task: `p1_wave_b_w5_more_judges` (judge B feasibility — including the O-007 threshold confirmation — and judge C adversary), then wave consolidation.
