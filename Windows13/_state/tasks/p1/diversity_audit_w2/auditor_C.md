# P1 Diversity Audit — Round 2 — Auditor C (Adversary)

- **task_id**: `p1_diversity_audit_w2`
- **role**: `auditor_C_adversary` (round 2; adversarial mandate: permutation families, genre collapse, ignored territories)
- **windows_id / windows_path**: `Windows13` / `Windows13` (window_locked: true)
- **branch**: `cursor/p1-diversity-audit-w2-auditor-c-32c6`
- **audited set**: `Windows13/_state/ideas_master.jsonl`, **494 records**, canonical commit `929445d` (origin/cursor/p1-wave-b-consolidator-w2-3111)
- **audited_at_utc**: 2026-08-28T21:05:00Z
- **independence**: full own analysis pass completed BEFORE reading Auditor A w2 (cross-check section at the end). Auditor B w2 output (`done_auditor_B.json`) does **not exist on any origin branch** at audit time (all-branch `git ls-tree` sweep) — noted, not blocking.
- **method**: deterministic regex/count analysis over all descriptive fields of all 494 master records + all 4 off-master shards (409 ideas); full pairwise one-liner+hypothesis token-Jaccard (121,771 pairs); manual spot-checks of family member one-liners. No model-invented facts; every number below is reproducible from the repo. Labels: EVIDENCE = measured here; HYPOTHESIS = judgment call.
- **timeline fairness note** (KNOWN FACT from commit timestamps): w1 audit consolidator landed 19:44Z. Wave-2 shards D/E/F and gen_g (19:26Z) predate it; gen_h (19:57Z) is effectively concurrent; gen_j (20:24Z) and gen_k (20:38Z) postdate it. Guard violations by pre-guard shards are timing-explainable — but they still must be **repaired at judge time**, which is the enforcement point this audit attacks.

---

## ATTACK 1 — Permutation families survived consolidation inside the accepted 494

Lexical duplication stays LOW (EVIDENCE: max pairwise token-Jaccard 0.246 on one-liner+hypothesis, `E-029` vs `E-054`; only 2 pairs ≥ 0.18). The wave-2 judges killed pairwise duplicates and wave-1 collisions. What they structurally could not kill is **family-level crowding among records that were individually accepted**. Regex family detection over all descriptive fields (mention-level upper bound; primary-membership verified by one-liner spot-check for the top families):

| family | mention-level | share | spans |
|---|---|---|---|
| P4 metric/harness/leaderboard critique | 88 | 17.8% | 6/6 shards |
| P9 calibration/uncertainty (w1 BANNED cluster) | 56 | 11.3% | 6/6 shards |
| P10 annotation-convention mismatch | 49 | 9.9% | 6/6 shards |
| P1 annotation-noise floor / "ground truth is noisy" | 44 | 8.9% | 6/6 shards |
| P2 name/synonym/prompt-wording sensitivity | 19 (12 primary) | 3.8% | C/D/E |
| P3 context/co-occurrence shortcut | 16 | 3.2% | multi |
| P8 reported-gaps-are-noise | 16 | 3.2% | multi |
| P7 contamination/seen-shot | 15 | 3.0% | multi |
| P15 head/tail credit stratification | 14 | 2.8% | multi |
| P6 oracle localization-vs-recognition decomposition | 11 (5 primary) | 2.2% | A/D |
| union of 18 detected families | 276 | 55.9% | — |

- EVIDENCE: **P1 annotation-noise floor has 18 primary members across all six shards** (A-027, B-001/002/008/069/075/084, C-010/025/067/069, D-045/083/093/096/097/098, F-038): six generators independently rediscovered "the ground truth is noisier than the method gaps". Each record is individually defensible; jointly they are one thesis wearing 18 costumes.
- EVIDENCE: **the banned calibration/uncertainty family GREW 31 → 56 mention-level** because pre-guard wave-2 added ~22 (D 9, E 8, F 5). Ban held at zero only for shards that read the audit (gen_j: 0 primary calibration clusters).
- EVIDENCE: P9's primary-cluster core in wave 1 alone: `calibration` 9 + `iou_head_calibration_uncertainty` 8 + `uncertainty_and_calibration` 7 + `uncertainty` 7 = 31 dedicated records.
- HYPOTHESIS: at Stage-2 selection these families will dominate the 200-cut unless capped, because debunk-family records tend to score well on cheapness/falsifiability axes.

**Demanded action (Stage 2, selection-time family caps, extending w1 F1–F5 caps):** P4 ≤ 10, P9 ≤ 8, P10 ≤ 8, P1 ≤ 6, P2 ≤ 5, P6 ≤ 3 of the 200 survivors (slot counts are HYPOTHESIS; the cap mechanism is the demand). Wave-3 judges must treat *family membership* — not just pairwise near-duplication — as a merge trigger.

## ATTACK 2 — Genre collapse persists; wave 2 made it worse

4-way genre classification of one-liner+hypothesis (EVIDENCE, heuristic regex, spot-checked):

| genre | count | share |
|---|---|---|
| debunk/audit | 254 | 51.4% |
| mixed debunk-plus-fix | 118 | 23.9% |
| characterization-law | 84 | 17.0% |
| constructive/capability | 38 | 7.7% |

- EVIDENCE: wave-2 constructive per shard: gen_d 10/79 (12.7%), gen_e 4/79 (5.1%), gen_f 9/88 (10.2%) — all below the ≥25% floor (pre-guard timing acknowledged; the floor did not exist when D/E/F were generated).
- EVIDENCE: the eval/measurement super-genre is **45.5%** of one-liners (225/494; D worst at 52/79 = 66%) — versus 43.5% at the 248-record w1 audit. The w1 "constructive rebalance needed" verdict was correct and nothing has landed yet that acts on it.
- The 38 strictly-constructive ids (protect from genre-blind culling, union with auditor B w1's 46-id list): A-011, A-026, A-043, A-056, A-063, A-093, B-003, B-004, B-040, B-056, C-004, C-037, C-054, C-061, D-020, D-031, D-059, D-072, D-073, D-074, D-077, D-086, D-089, E-007, E-046, E-050, E-052, F-010, F-040, F-043, F-045, F-050, F-054, F-055, F-070, F-071, F-073, F-100.

**Demanded action:** `gen_p_constructive_capability` moves from queue position 8 to **first dispatch**. Off-master reality makes this urgent: gen_h adds 48% pure-debunk, gen_k adds ~49%; after in-flight shards land, the debunk share rises again.

## ATTACK 3 — The w1 quality gates are dead letters without a judge-time enforcement mechanism

- EVIDENCE: numeric kill threshold inside `falsifiable_prediction`: **23/494 (4.7%)** (gate demanded: every record).
- EVIDENCE: structured `evidence_label`: **94/494** — gen_a only; zero of the 400 wave-2/wave-1 non-A records were normalized at judging or consolidation.
- EVIDENCE: off-master compliance is bimodal and tracks whether the generator read the audit:
  - **gen_j (104, post-audit): 104/104 numeric kill thresholds, 104/104 evidence_label, plus family_fingerprint / genre / needs_special_resources / seg_metric_dependent fields. Full compliance — proves the gates are satisfiable.**
  - gen_k (105, post-audit): separate `kill_threshold` field 98/105 (schema drift: threshold not in `falsifiable_prediction`; `evidence_labels` plural vs gen_j's `evidence_label`), no per-record structured prior-work label.
  - gen_h (100, concurrent): 2/100 numeric, 0 evidence_label.
  - gen_g (100, pre-audit): 0/100 numeric, 0 evidence_label.
- ADVERSARY POINT: a gate that only binds agents who happen to read the audit file is not a gate. **Demand: wave-3 judges must either (a) attach kill_threshold + evidence_label to each gen_g/h/k record at judge time, or (b) remand the shard. The wave-3 consolidator must normalize schema (single `evidence_label` dict, kill threshold inside `falsifiable_prediction`) before append. Add gate-compliance check to the consolidator done-file checklist.**

## ATTACK 4 — Pre-judging strike on the off-master shards (409 ideas)

| shard | n | pushed | kill-thresholds | constructive (my heuristic) | pure debunk | eval-genre | family recycling |
|---|---|---|---|---|---|---|---|
| gen_g domain shift | 100 | 19:26Z (pre-audit) | 0/100 | 14% | 41% | 42% | P4 ×15 |
| gen_h SR/restoration | 100 | 19:57Z (concurrent) | 2/100 | 8% | 48% | 37% | P4 ×11, P1 ×8, P9 ×8 |
| gen_j diffusion science | 104 | 20:24Z (post) | 104/104 | 7% phrasing (self-declared 35.6%) | 47% phrasing (self-declared 9.6%) | 31% | P4 ×9 |
| gen_k 3D/geometry/video | 105 | 20:38Z (post) | 98/105 (separate field) | 9% phrasing (self-declared 32.4%) | 49% phrasing | 57% | P9 ×10, P4 ×9 |

- gen_h violates the ≥25% constructive floor (8%) and the ≤40% pure-debunk ceiling (48%), and re-imports the calibration family (8) into restoration clothing. Its restoration-specific guards held: 0 SAM mentions, 0 PSNR/SSIM-only falsifications, ~56% restoration-native phenomena.
- **Self-declared genre labels are inflated** (EVIDENCE of divergence, HYPOTHESIS on cause): gen_j self-labels 37/104 constructive while constructive *phrasing* is ~7%; gen_k self-labels 34/105 vs ~9%. Judges must audit the `genre` field against the actual claim, not trust it — otherwise the genre quota becomes self-certified and useless.
- gen_k's eval-genre share (57% of one-liners) recycles the eval-critique super-genre into 3D territory; its specific w1 guard (falsification must not reduce to 2D seg/mask metrics) held: only 7/105.
- gen_g's `test-time-adaptation` cluster (14 ideas, G-001..G-014) matters for the next-queue design — see Attack 6.

## ATTACK 5 — Letter-registry hazard: retire `gen_i`

EVIDENCE: the w1 queue assigned `gen_i_restoration_lowlevel`, but the dispatcher commissioned the same territory as `gen_h` (branch `p1-gen-h-sr-restoration-1829`). `gen_i` is now a dangling letter with a stale mandate attached in a canonical decision file. This is exactly the collision pattern that produced the w1 gen_d..gen_g letter mess. **Demand: mark `gen_i` permanently RETIRED (never reassign) in the next consolidator decision; letters are append-only.**

## ATTACK 6 — Collision catch against Auditor A w2: proposed `gen_q` overlaps off-master gen_g

Auditor A w2 proposes `gen_q_test_time_compute_adaptation` with a mandate including "TTA failure modes under real shift" and cites master coverage 0.2% as "unowned". EVIDENCE: **off-master gen_g already holds 14 dedicated TTA ideas** (G-001..G-014: entropy-minimization gains vanish on real shift; batch-statistics artifacts at batch-size 1; TTA hyperparameters tuned on test distribution; stream collapse; do-no-harm gating; test-time prompt tuning ≈ augmentation ensembling; etc.). Master-only coverage counting repeats the w1 mistake (off-master blindness) that this seat flagged in round 1. **Demand: narrow gen_q to inference-time compute-scaling laws for perception (test-time search, ensembling laws, test-time training for dense prediction) + A's psychophysics fold-in, with an explicit anti-overlap guard banning TTA-method critique as primary subject; or defer gen_q until gen_g is judged.**

## ATTACK 7 — Citation audit: clean

- EVIDENCE: 494-record master contains citation-like strings in exactly 14 records, all gen_a `prior_work_basis` fields, all naming real, well-known works with correct author-year pairing (SAM Kirillov et al. 2023; LoRA Hu et al. 2021; CKA Kornblith et al. 2019; BitFit Ben Zaken et al. 2022; model soups Wortsman et al. 2022; task arithmetic Ilharco et al. 2022; VPT Jia et al. 2022; MAE He et al. 2022; cue-conflict Geirhos et al. 2019; registers Darcet et al. 2023; HQ-SAM Ke et al. 2023; DETR Carion et al. 2020; SAM 2 Ravi et al. 2024; ToMe Bolya et al.; typographic attacks Goh et al.).
- EVIDENCE: the four off-master shards (409 ideas) contain **zero** citation strings.
- **No fake citations found. This audit adds none.**

## ATTACK 8 — 1000-goal arithmetic: judging, not generation, is the bottleneck

- EVIDENCE: Stage-1 target 1000+; master 494; off-master raw 409 (gen_g 100, gen_h 100, gen_j 104, gen_k 105) + in-flight gen_l (~100 expected, unpushed at audit time — verified absent from all origin branches).
- EVIDENCE: observed acceptance 494/604 = 81.8% (wave 2: 246/302 = 81.5%).
- Arithmetic: 494 + 0.82×509 ≈ **910 after in-flight judging**; remaining queue gen_m/n/o/p (~400 raw ≈ +325) lands ~1235 — comfortably past 1000 **without any new letter**. New letters (q/r/u/s/t) are diversity plays, not volume plays; commission them for coverage, judged against the family caps above. Five shards (gen_g/h/j/k/l) currently await 3 judges + consolidator each — schedule wave-3 judging before or alongside new generation, or off-master inventory keeps growing stale.

---

## Missing territories (adversary round 2; master primary-coverage at 494, off-master/in-flight accounted)

| territory | master primary | owned by |
|---|---|---|
| constructive/capability genre | 7.7% | queued gen_p (elevate to #1) |
| underwater/sonar | 0.0% | queued gen_o |
| microscopy/histology | 0.2% | queued gen_o |
| document/OCR | 0.4% | queued gen_o |
| remote sensing/aerial | 1.0% | queued gen_o |
| training dynamics/objectives | 0.8% | queued gen_m |
| continual/open-world learning | 0.2% | fold into gen_m (my addition) |
| scaling laws / emergence | 0.2% / ~0.4% | queued gen_n |
| memorization/privacy | 0.8% | queued gen_n |
| adversarial security (attack science, backdoors, poisoning) | 0.4% | **UNOWNED → NEW gen_u** |
| fairness/demographic robustness | 0.2% | **UNOWNED → NEW gen_u** |
| inference-time compute scaling | ~0.2% | NEW gen_q (NARROWED; anti-gen_g guard) |
| cross-field transfer (vision ↔ audio/time-series/graphs/sci-imaging) | 0.0% | NEW gen_r (w1-deferred; revisit trigger met) |
| human psychophysics contrasts | 0.0% | fold into gen_q (per A) |
| embodied/active perception | 1.0% | gen_s (reserve) |
| efficiency/deployment science | ~1% dedicated | gen_t (reserve) |
| SR/restoration | 3.0% | **FILLED off-master (gen_h, 100)** |
| diffusion/generative science | 0.0% | **FILLED off-master (gen_j, 104)** |
| 3D/depth/flow/video | ~5% | **FILLED off-master (gen_k, 105)** |
| domain shift/TTA | ~1% | **FILLED off-master (gen_g, 100)** |
| LLM/agent-vision loops | 2.4% | **in-flight gen_l** |

## Recommended next queue (Auditor C round 2)

1. **gen_p_constructive_capability** (was #8) — genre repair. Guards: ≥80% constructive, 0% pure audit, gen_j-style full gate schema mandatory, annotation-pathology hard ban.
2. **gen_o_hard_domain_diversifier** — add explicit document/OCR + underwater + microscopy emphasis; smoke/fire/transparent hard ban; ≤25% medical (beyond-ambiguity lens).
3. **gen_m_training_dynamics_objectives** — extend mandate with continual/open-world learning (0.2% coverage, otherwise unowned); hard ban add-loss-term-X-to-task-Y.
4. **gen_n_scaling_memorization_data_laws** — add emergence-claims audit; strengthened anti-gen_f overlap (gen_f owns 60+ synthetic-engine records).
5. **gen_u_adversarial_security_fairness** (NEW letter, this auditor) — attack science (adversarial patches/perturbations as mechanism claims, backdoor/poisoning of vision FMs and auto-label pipelines, jailbreak-style attacks on VLM-grounded perception), fairness/demographic robustness with falsifiable mechanism claims. Guards: ≤20% eval-critique, ≤5% SAM, each idea names an attack/bias mechanism and a numeric kill threshold; no survey-style records.
6. **gen_q_inference_time_compute** (NARROWED from Auditor A's gen_q) — test-time search/ensembling/compute-scaling laws + psychophysics contrasts; commission only after gen_g judging; hard anti-overlap: TTA-method critique banned as primary subject (gen_g owns G-001..G-014).
7. **gen_r_cross_field_transfer** — w1-deferred; both revisit conditions met (coverage still 0.0%; in-flight h/j/k/l leave it untouched). Keep w1 guards (must name both fields + the transferred invariance; no bare apply-X-to-Y).
8. Reserves: **gen_s_embodied_interactive_perception**, **gen_t_efficiency_deployment_science** (concur with A; commission only if the 1000-margin erodes or wave-3 audit demands).

Letters `gen_a..gen_h, gen_j, gen_k, gen_l` burned/in-flight; `gen_i` RETIRED (Attack 5); next fresh letters after this queue: `gen_v+`.

## Cross-check vs Auditor A w2 (read AFTER my own pass)

**Agreements (independent convergence):** SAM guard held (A: 17.6% vs my 17.2% — regex-scope delta, same conclusion); genre collapse is the dominant axis and gen_p goes first; annotation/convention pathology is the largest surviving family; gen_i not reused; letters g/h/j/k/l burned; no fake citations; eval-critique super-genre still large (A measures 31.4% by cluster-name, I measure 45.5% by one-liner phrasing — different instruments, same direction).

**Adversarial deltas (mine, not in A's report):** (1) the gen_q ↔ gen_g TTA collision (Attack 6) — A's "unowned 0.2%" claim is master-only counting; (2) gate enforcement is mechanism-less (Attack 3) — A notes gates are "enforceable only from gen_h onward"; I show gen_h itself is non-compliant and demand judge-time repair/remand plus schema normalization; (3) self-declared genre inflation in gen_j/gen_k (Attack 4) — quota compliance must be judged from claims, not self-labels; (4) NEW territory gen_u (adversarial security/fairness) — absent from A's queue and from all w1 queues; (5) retire gen_i permanently rather than leave it "deferred".

**Auditor B w2:** absent at audit time; consolidator should not block on it beyond one re-check.

## Scope compliance

- `ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, `window.lock.json`: **NOT touched**.
- Writes confined to `Windows13/_state/tasks/p1/diversity_audit_w2/auditor_C.{md,json}` + `done_auditor_C.json`.
- Own unique branch `cursor/p1-diversity-audit-w2-auditor-c-32c6`; no force-push.
- recommended_next_task_type: `p1_diversity_audit_w2_consolidator`.
