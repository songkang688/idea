# P1 Diversity Audit W1 — Auditor A (mode collapse / cluster crowding / SAM+X / LoRA+X / loss+X)

- task_id: p1_diversity_audit_w1
- role: auditor_A_mode_collapse
- windows_id: Windows13 (LOCKED, windows_path Windows13, window_locked true — not modified by this audit)
- audited set: Windows13/_state/ideas_master.jsonl @ origin/cursor/p1-wave-b-consolidator-w1-7a58 (248 accepted records, wave p1_wave_b_w1)
- audit method: deterministic regex/count analysis over all text fields of all 248 records (scripted, reproducible); qualitative sampling of the largest clusters. No records were modified. Canonical state files untouched.
- audited_at_utc: 2026-08-28T19:16:17Z

All numeric claims below are labeled EVIDENCE (measured directly on the 248 records). Interpretations and unverified claims are labeled HYPOTHESIS. No citations are invented anywhere in this audit.

## 1. Verdict summary

Surface-level mode collapse is LOW: the dedup judge worked. Thematic concentration is HIGH: the entire 248-idea portfolio sits inside three macro-territories (evaluation/measurement critique 43.5%, SAM internals + PEFT 32.7%, hard-domain dense prediction 23.8%), gen B has a within-shard fixation on smoke/amorphous media (56% of its ideas use smoke), and calibration/uncertainty is the one theme all three generators independently crowded into. Re-running the same three generators would deepen these crowds; the next wave needs new territories, not more volume in current ones.

## 2. Mode collapse check

- EVIDENCE: 0 near-duplicate one-liner pairs at token-Jaccard >= 0.33 across all 248x247/2 pairs. No two accepted ideas share a surface formulation.
- EVIDENCE: rhetorical-template reuse in one-liners is modest: "not X but Y / rather than" 22 (8.9%), "conflate/confound" 11 (4.4%), all debunk-templates combined 35 (14.1%).
- EVIDENCE: all 248 records carry the contrarian schema (community_default_belief + why_it_might_be_wrong present in 248/248), and 0 records propose a new method/architecture as the primary contribution (crude regex "we propose / new method / novel architecture" matches 0).
- HYPOTHESIS (genre monoculture): the portfolio is near-uniformly "falsify a community belief / audit a measurement" in genre. That is by design of Wave 1's generator mandates, but at the 1000+ scale it becomes a collapse axis of its own: there are almost no constructive capability hypotheses (enabling mechanisms with falsifiable claims), no data-centric hypotheses, and no training-dynamics hypotheses. A reviewer sampling 10 random ideas would correctly guess the house style 10/10 times.

Verdict: no textual mode collapse; clear genre-level and territory-level concentration.

## 3. Cluster crowding

- EVIDENCE: 36 distinct clusters; every cluster is single-shard (no cross-shard cluster labels). Largest clusters: what_peft_actually_learns 12, prompt_geometry_failure_modes 10, encoder_representation_myths 9, sam2_video_memory 9, calibration 9. Largest cluster = 4.8% of portfolio, so no single-cluster blowout.
- EVIDENCE (super-cluster concentration — the real crowding): mapping all 36 clusters to macro-territories gives EVAL_MEASUREMENT 108/248 (43.5%), SAM_INTERNALS_PEFT 81/248 (32.7%), HARD_DOMAIN_DENSE 59/248 (23.8%). Three territories cover 100% of the accepted set.
- EVIDENCE (cross-shard theme crowding): calibration/uncertainty-named clusters exist in all three shards and total 31 ideas (calibration 9 + iou_head_calibration_uncertainty 8 + uncertainty_and_calibration 7 + uncertainty 7 = 12.5%); 46 ideas (18.5%) mention calibration anywhere. Annotation/ground-truth-quality clusters total 21 ideas (8.5%); 95 ideas (38.3%) touch annotation/rater/ground-truth issues. These two themes are where independent generators convergently crowded.
- EVIDENCE (gen B within-shard fixation): the word "smoke" appears in 48/85 (56%) of gen B ideas; the amorphous/scattering-media family (smoke, fire/flame, fog, plume, fluid/spill, dust, transparent/glass/translucent, amorphous/diffuse boundaries) covers 61/85 (72%) of gen B. Meanwhile, inside gen B's own "hard domain" mandate: underwater/sonar 0 ideas, microscopy/biology 0, driving 1, agriculture 1, industrial defect 2, remote sensing 2.
- EVIDENCE (eval-critique framing bleed): 168/248 (67.7%) of all ideas mention benchmark/evaluation/metric somewhere in their text; gen C (69 ideas) is 100% eval/measurement critique by mandate, and its critique targets skew generic ("foundation models" 14, VLM 12) rather than task-specific.

Crowded clusters to stop feeding (see JSON for machine-readable list): calibration/uncertainty (cross-shard, 31 direct + 46 mentions), SAM prompt/decoder/encoder internals (gen A, 36 across four clusters), PEFT-on-SAM science (gen A, 22 across three clusters), smoke/amorphous-media segmentation (gen B, ~61), annotation/ground-truth pathology (cross-shard, 21 direct + 95 mentions), SAM2 video memory (9, adequately covered).

## 4. SAM+X / LoRA+X / loss+X permutation volume

- EVIDENCE (SAM+X): 87/248 (35.1%) mention SAM/SAM2; within gen A it is 77/94 (82%). However only 4 accepted ideas use apply/port-X-to-Y phrasing (W13-P1-A-039, A-097, C-060, C-064), and sampling the big gen A clusters shows mechanism-probe hypotheses (e.g., click-geometry laws, memory-bank confirmation bias) rather than "run SAM on domain X" permutations.
- EVIDENCE (judges already killed the worst): decision.json kill reasons explicitly cite "Permutation kill" (e.g., W13-P1-A-085 early-exit-ported-to-SAM, unanimous). The accepted set is post-filter.
- EVIDENCE (LoRA+X): 25 ideas (10.1%) mention LoRA; 65 (26.2%) mention PEFT/adapter/fine-tuning. The 12-idea what_peft_actually_learns cluster plus adapter_ecosystem_continual (5) and adaptation_interfaces (5) put gen A's PEFT mass at ~22 ideas. These are mostly mechanistic ("rank-1 suffices", "bias-only matches LoRA", "PEFT destroys multimask ambiguity") — science about PEFT, not LoRA+domain permutations.
- EVIDENCE (loss+X): 0 accepted ideas match "new/modified/auxiliary loss or regularizer for task X". loss+X permutation volume is zero.
- VERDICT: permutation contamination inside the accepted 248 is LOW (flag level: watch, not purge). The risk is prospective: the SAM-internals and PEFT-science territories are near saturation, so another generator wave with the same mandates would be forced into permutation-style filler. Recommendation: no further SAM-centric or PEFT-centric generator in the next wave; cap SAM-mentioning ideas in new shards at ~10%.

## 5. Research blind spots (topics <5% of portfolio)

EVIDENCE (regex coverage over all text fields, out of 248):

| topic | count | share |
|---|---|---|
| scaling laws | 0 | 0.0% |
| data curation / data-centric science | 0 | 0.0% |
| optical flow | 1 | 0.4% |
| federated / privacy / memorization | 1 | 0.4% |
| training dynamics / optimization | 3 | 1.2% |
| active learning | 3 | 1.2% |
| 3D / point cloud / LiDAR / NeRF / splatting | 4 | 1.6% |
| remote sensing / satellite / aerial | 4 | 1.6% |
| self-/semi-supervised pretraining science | 4 | 1.6% |
| deployment / quantization / hardware | 7 | 2.8% |
| continual / lifelong (mostly SAM-adapter framing) | 8 | 3.2% |
| generative / diffusion models as perception tools | 10 | 4.0% |
| depth estimation | 11 | 4.4% |

Also: VLM/language-vision is 15 ideas (6.0%) and nearly all of it is gen C eval-critique (vlm-eval-weaknesses cluster), not hypotheses about the language-vision interface itself. Detection is 28 (11.3%) but mostly incidental mentions.

## 6. Missing contrarian hypotheses

HYPOTHESIS (belief-targets that the 248 ideas never challenge; each is a widely held community default and thus fair game for the contrarian pipeline):
1. Scaling orthodoxy — "more pretraining data/parameters monotonically improves dense-prediction transfer." Zero ideas test scaling behavior.
2. Data-curation orthodoxy — "dedup/filtering/higher-quality captions always help; data composition effects are second-order." Zero ideas.
3. Synthetic-data orthodoxy — only one idea (W13-P1-C-064) touches generative training data.
4. SSL orthodoxy — "contrastive/masked pretraining yields general-purpose features." Essentially untested (4 mentions).
5. Emergence/monotone-progress beliefs — no idea challenges claimed emergent abilities or monotone capability growth in vision FMs.
6. 3D/geometric-consistency beliefs — "2D foundation features are view/geometry consistent enough for 3D lifting." Untested.
7. Optimizer/training folklore — warmup, EMA, fine-tuning learning-rate lore for foundation models. Untested (3 mentions).
8. Privacy/memorization — "vision FMs don't memorize training images in ways that matter." One tangential mention.
9. Language-supervision beliefs — "text supervision teaches visual grounding rather than shortcut alignment." Only touched via eval critique, not mechanism.
10. Human-vision comparison beliefs beyond annotation (psychophysics-style capability contrasts). Absent.

## 7. Recommended next generator territories (task queue for parent)

Priority-ordered; each entry names the gap it fills and an anti-crowding guard. Machine-readable copy in auditor_A.json.

1. gen_d_data_centric_scaling — data curation, pretraining-data composition, scaling behavior, synthetic data, contamination/memorization science. Fills the two 0.0% blind spots (scaling laws, data-centric). Guard: no SAM-specific ideas beyond 10%; every idea must name a data-level intervention as its manipulated variable.
2. gen_e_3d_geometry_physics — 3D/point-cloud/NeRF/splatting, depth, optical flow, multi-view/geometric-consistency beliefs about 2D foundation features. Fills 3D 1.6%, flow 0.4%, depth 4.4%. Guard: falsification experiments must not reduce to 2D segmentation metrics.
3. gen_f_hard_domain_diversifier — underwater/sonar, microscopy/histology, remote sensing, industrial inspection, agriculture. Fills gen B's own blind spots. HARD guard: smoke/fire/fog/transparent/amorphous-media examples banned (gen B has 61 already); max 25% medical (portfolio already 24.6% medical/clinical).
4. gen_g_vlm_language_vision_interface — mechanism-level hypotheses about text-prompted perception, grounding, language-as-supervision (not eval critique; gen C owns that). Fills VLM 6.0%-and-eval-only. Guard: <=20% overlap with gen C's vlm-eval-weaknesses framing; each idea must make a representational or mechanistic claim.
5. gen_h_training_dynamics_objectives — training dynamics, fine-tuning dynamics, optimizer/schedule folklore, objective-function science. Fills 1.2% and the empty loss-science space. HARD guard: no "add loss term X to task Y" permutations; hypotheses must predict when/why an objective matters, with a falsifiable mechanism.
6. gen_i_constructive_capability — enabling-method hypotheses (new capability + falsifiable mechanism claim), to rebalance the 100% debunk-genre portfolio. Guard: keep the falsifiable_prediction schema mandatory; ban benchmark-chasing framings ("beats SOTA") without a mechanism claim.

Anti-crowding guards for ALL next-wave generators (recommended for parent to put in generator prompts):
- Cap SAM/SAM2-mentioning ideas at 10% per shard (portfolio already 35.1%).
- Ban calibration/uncertainty as a primary cluster (31 direct ideas already; all three Wave-1 generators converged there).
- Ban smoke/fire/transparent-media running examples.
- Require >=8 distinct sub-clusters per shard of ~100 ideas, none >15% of the shard.
- Require >=30% of each shard's falsification experiments to not depend on segmentation metrics (portfolio is 50.4% segmentation).

## 8. Scope compliance

- Did NOT modify: ideas_master.jsonl, research_state.json, window.lock.json, research_ledger.md, or any prior task file.
- Did NOT change windows_id (Windows13, locked).
- Wrote ONLY: auditor_A.md, auditor_A.json, done_auditor_A.json under Windows13/_state/tasks/p1/diversity_audit_w1/.
- Own branch, no force-push.
