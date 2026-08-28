# P1 Diversity Auditor C — Adversary (permutation families, genre collapse, ignored P1 territories)

- task_id: `p1_diversity_audit_w1`
- role: `auditor_C_adversary`
- window: Windows13 (windows_path `Windows13`, window_locked true)
- audited set: `Windows13/_state/ideas_master.jsonl` @ `origin/cursor/p1-wave-b-consolidator-w1-7a58` (936670f), 248 records
- audited_at_utc: 2026-08-28T19:34:04Z
- independence: full quantitative pass completed BEFORE reading Auditor A or Auditor B shards; peer shards read afterwards for cross-reference only (noted where relevant)
- method: deterministic regex/keyword/token-Jaccard analysis over all text fields of all 248 records, plus manual reading of every cluster's one-liners; off-master branch tree inspection via `git ls-tree`/`git show`. No canonical files modified. Every claim below is labeled EVIDENCE (reproducible from repo contents) or HYPOTHESIS / MODEL SPECULATION. No literature citations are made anywhere in this audit, so none can be fake.

## 1. Verdict in one paragraph

Pairwise dedup was effective — EVIDENCE: max token-Jaccard between any two accepted ideas is 0.20; zero near-duplicate pairs — but the set exhibits structural permutation families and severe genre collapse that lexical dedup cannot see. 85/248 (34.3%) of accepted ideas take SAM/SAM2/SA-1B itself as the experimental subject; ~24–27 gen_a ideas form a single "PEFT-knob factorial on SAM" meta-experiment; 21 gen_c ideas (30% of that shard) instantiate one "published deltas are statistical noise" template; 62/85 (73%) of gen_b runs on the smoke/fire/transparent/scattering model organism. Meanwhile SR/restoration has literally zero real ideas, diffusion/generative-model science ~2 (both eval-critiques), LLM/agent ~3 (all VLM-eval critiques), cross-field transfer 0, and 3D/NeRF/point-cloud 0 dedicated. Object detection is absent from master but a 100-idea wave2 shard (gen_d) already exists off-master, along with three more wave2 shards (gen_e VLM-dense, gen_f synthetic-data, gen_g domain-shift; 402 ideas total) that the next consolidator must ingest before any new generators are commissioned, or wave3 will re-generate territory that already exists.

## 2. Attack: remaining SAM+X / LoRA+X / module mashups in the accepted set

The judges killed the crude "port SAM to domain X" permutations. What survived is subtler: structural families that share subject, apparatus, and measurement, and will cannibalize each other at the 200→50 cut. Marginal information of the k-th family member given the first 3 is low (HYPOTHESIS), so families should carry selection caps.

### F1 — PEFT-knob factorial on SAM (~24–27 ideas, one meta-experiment)
EVIDENCE: `what_peft_actually_learns` (12: A-011..A-022), `adapter_ecosystem_continual` (5: A-086..A-091), `adaptation_interfaces` (5: A-097..A-102), `distillation_efficiency` (5: A-080..A-084). The axis structure is literally a factorial grid: {LoRA rank, LoRA placement, encoder-vs-decoder, bias-only, VPT-vs-LoRA, prompt-type during tuning, sequential order, weight-merging, input stem, positional embeddings, quantization, token merging} x {what does it really learn / what does it silently destroy}. Each idea is individually falsifiable and lexically distinct, but the whole block is one factorial PEFT-on-SAM study sharing a single codebase, datasets, and metric suite.
- Adversarial recommendation: treat F1 as ONE umbrella project at the next cut; cap at 3–4 representatives (suggested keeps: A-015 ambiguity-machinery destruction, A-019 prompt-type overfitting, A-088 subspace-angle interference — MODEL SPECULATION on which are strongest).

### F2 — SAM component-x-pathology grid (~62 ideas)
EVIDENCE: `prompt_geometry_failure_modes` (10), `decoder_token_mechanics` (8), `iou_head_calibration_uncertainty` (8), `encoder_representation_myths` (9), `data_priors_sa1b` (7), `sam2_video_memory` (9), `robustness_adversarial` (6), plus scattered. Template: "SAM's [component] [encodes/leaks/collapses under] [bias/shortcut], measurable by [cheap frozen-model probe]". Components enumerated: decoder (22 mentions), encoder (18), IoU head, output/mask tokens, memory attention/bank, stability score, positional encodings, SA-1B generation artifacts. This is a component-x-probe permutation grid at the schema level even though no two members are lexically similar.
- Adversarial recommendation: near saturation (concurs with Auditor A read post-hoc); zero further SAM-internals generation; at selection time require each surviving F2 idea to name a distinct downstream consequence, not just a distinct component.

### F3 — "internal score as a free X detector" trick (6 ideas)
EVIDENCE: A-025 (predicted-IoU histograms as OOD detector), A-027 (stability-vs-IoU disagreement as label-error detector), A-058, A-086 (IoU head as adapter router), B-019, B-026 (prompt-jitter spread as ambiguity detector). One trick — reuse a frozen model's self-assessment signal as a free detector — permuted over {OOD, label error, routing, ambiguity}.
- Adversarial recommendation: cap at 2 representatives; ban the template in future shards.

### F4 — gen_b cue-ablation collapse template + organism fixation
EVIDENCE: explicit template members B-012 (glass/specular highlights, cross-polarized imagery), B-041, B-042 (fire/sensor saturation, HDR), B-047 (smoke/blur leakage): "[cue] may be the load-bearing shortcut for [domain]; acquire cue-ablated imagery; model collapses". Same experimental design permuted over cues. Broader: 62/85 (73%) of gen_b ideas run on the smoke/fire/flame/fog/transparent/scattering organism family.
- Adversarial recommendation: hard ban on these organisms in all future shards (concurs with Auditor A post-hoc); the cue-ablation template itself is good science but should be one methods paper, not four ideas.

### F5 — gen_c "published deltas are statistical noise" grid (21 ideas, 30% of gen_c)
EVIDENCE: C-010, C-013, C-019, C-025, C-034, C-046, C-047, C-048, C-052, C-054, C-063, C-067, C-070, C-073, C-074, C-075, C-077, C-080, C-086, C-089, C-090. Template: "{few-shot support draws | random seeds | ablation single-runs | test-label error | resampling noise | contamination}" x "published improvements are within noise once controlled". Shared machinery: bootstrap/variance audit over existing benchmarks.
- Adversarial recommendation: cap at 4–5 representatives at the next cut; ban the template as a primary framing in future shards — gen_c owns it and it is full.

### LoRA+X residual census
EVIDENCE: 37/248 ideas have LoRA/adapter/PEFT as subject matter; 28 of those intersect SAM. Zero surviving "LoRA for domain X" application mashups (the judges did their job); the residual risk is F1's factorial crowding, not application spam.

## 3. Genre collapse (beyond Auditor A's mode-collapse axes)

- EVIDENCE: 248/248 records are contrarian-audit schema (community_default_belief + why_it_might_be_wrong). Under a strict constructive test (proposes building/training something new as the primary contribution) only ~7–11/248 (~3–4%) qualify: A-003, A-021, A-045, A-077, A-080, B-057, C-061 plus ~4 mixed. Auditor B (read post-hoc) counts 46/248 (18.5%) with a looser "constructive-capability" criterion; under either count the portfolio is overwhelmingly observational/debunk.
- EVIDENCE: output-space collapse — 110/248 (44.4%) are mask/segmentation-centric; 85/248 (34.3%) have SAM/SA-1B as subject.
- EVIDENCE: model-organism collapse — gen_a: 81/94 (86%) SAM-centric; gen_b: 62/85 (73%) smoke/fire/transparent/scattering.
- HYPOTHESIS: method-of-falsification collapse — the dominant experimental modes are (a) frozen-model probing/regression and (b) benchmark re-analysis with variance controls. Almost nothing requires training a new capability, so at final-3 selection the window risks producing only critique papers. A 1000-idea pipeline needs interventional/method genres represented before the cut, not after.

## 4. Ignored P1 territories (quantified against master @ 248)

| territory | real coverage in master | wave2 off-master coverage | residual gap |
|---|---|---|---|
| SR / restoration / low-level (denoise, deblur, low-light, ISP) | 0 (EVIDENCE: only hit is an incidental blur mention in B-047) | none | TOTAL GAP — top priority |
| diffusion / generative-model science | ~2 (C-037, C-064 — both eval-critiques of generative evals/data, not model science) | gen_f covers synthetic-data engines/pipelines only | model-science gap remains (representations, guidance/inversion pathologies, memorization, diffusion-for-perception) |
| LLM / agent with vision | ~3 (C-006, C-060, C-071 — all VLM-eval critiques) | gen_e is VLM dense prediction, not agent loops | agent/tool-use/test-time-compute gap remains |
| cross-field transfer (vision <-> audio/time-series/graphs/science) | 0 dedicated | none | TOTAL GAP |
| object detection | 0 dedicated (7 keyword hits are all SAM-box-prompt or calibration asides) | gen_d shard: 100 ideas, off-master | covered off-master — DO NOT re-commission; consolidate |
| 3D / point cloud / NeRF / splatting | 0 dedicated (EVIDENCE: 0 regex hits) | none | TOTAL GAP (Auditor A concurs) |
| video beyond SAM2-memory | 25 mentions, nearly all SAM2- or smoke-bound | gen_g touches shift, not video | general video understanding gap |
| training dynamics / objective science | ~3 | none | gap (Auditor A concurs) |
| efficiency / deployment (non-SAM) | ~0 (all 7 efficiency ideas are SAM distillation/quantization) | none | gap |
| embodied / robotics | 0 dedicated (10 incidental) | none | gap |

## 5. Wave2 shards exist off-master (EVIDENCE — verified by git ls-tree/show at audit time)

| shard | ideas | branch |
|---|---|---|
| gen_d_object_detection | 100 (W13-P1-D-001..100) | `origin/cursor/p1-gen-d-object-detection-07a3` |
| gen_e_vlm_dense_prediction | 100 (W13-P1-E-001..100) | `origin/cursor/w13-p1-gen-e-vlm-dense-9412` |
| gen_f_synthetic_data | 102 (W13-P1-F-001..102) | `origin/cursor/w13-p1-gen-f-synthetic-data-3a94` |
| gen_g_domain_shift | 100 (W13-P1-G-001..100) | `origin/cursor/p1-gen-g-domain-shift-0165` |

Total: 402 wave2 ideas NOT in ideas_master.jsonl. WARNING for the consolidator: Auditor A's recommended territories reuse the letters gen_d..gen_g with DIFFERENT mandates (A's gen_d = data-centric scaling, gen_e = 3D, gen_f = hard-domain diversifier, gen_g = VLM interface). The actual pushed shards use those letters for detection / VLM-dense / synthetic-data / domain-shift. Naming must be reconciled to avoid commissioning collisions; my queue below uses fresh letters gen_h..gen_m.

## 6. Recommended next generator queue (anti-crowding constraints attached)

Step 0 — CONSOLIDATE WAVE2 FIRST. Run judges A/B/C + consolidator over gen_d/e/f/g (402 ideas) before commissioning anything. Otherwise wave3 will regenerate detection/VLM/synthetic/shift territory that already exists off-master.

Then, in priority order:

1. `gen_h_restoration_lowlevel` — SR, denoising, deblurring, low-light, ISP/imaging-pipeline science. Fills the only 0.0%-everywhere territory. Guards: ban SAM/LoRA-for-restoration mashups (<=5% SAM mentions); >=50% of ideas about restoration-native phenomena (frequency hallucination, perceptual-distortion tradeoffs, real-vs-synthetic degradation gaps); falsification must not be PSNR/SSIM-only.
2. `gen_i_diffusion_model_science` — generative/diffusion models as experimental subject: representations, guidance/inversion pathologies, memorization, diffusion-for-perception. Guards: <=10% synthetic-training-data ideas (gen_f owns that); ban "generative eval metric is broken" framing (gen_c owns it, see F5).
3. `gen_j_llm_agent_vision` — LLM/agent loops around vision: tool use, self-verification, visual programs, test-time compute for perception. Guards: <=20% eval-critique genre; each idea must make a falsifiable claim about the loop/system, not merely the underlying VLM.
4. `gen_k_3d_geometry_video` — 3D/point-cloud/NeRF-splatting/depth/optical-flow + video understanding beyond SAM2 memory. Guards: falsification experiments must not reduce to 2D mask metrics; <=10% SAM2 mentions.
5. `gen_l_cross_field_transfer` — transfer science across fields (vision <-> audio/time-series/graphs/scientific imaging). Guards: each idea must name both fields AND the specific invariance/structure claimed to transfer; hard ban on bare "apply architecture X to field Y" permutations.
6. `gen_m_constructive_capability` — genre rebalancer: enabling-capability hypotheses with falsifiable mechanism claims, any territory. Guards: 0% pure-audit genre; <=10% SAM.

### Global anti-crowding constraints for all future waves (additive to Auditor A's guards, which I endorse post-hoc)

- G1 SAM dilution: new shards <=5% SAM-subject ideas; running master SAM-subject share must fall below 25% after each consolidation (currently 34.3%).
- G2 family fingerprint at judge time: judges tag each idea with a (subject_system, manipulated_variable, measurement_family) triple; any cell accumulating >6 accepted ideas across the whole master triggers a family cap and a merge review.
- G3 template ban-list (from this audit): PEFT-knob-factorial-on-SAM (F1), SAM-component-pathology probes (F2), internal-score-as-free-detector (F3), smoke/fire/transparent organisms and cue-ablation-collapse (F4), published-deltas-are-noise (F5), calibration/uncertainty as primary cluster.
- G4 genre quota: >=25% of each new shard constructive/capability genre; <=40% pure audit/debunk.
- G5 structure quota: >=8 distinct sub-clusters per ~100-idea shard, none >15% of the shard; >=30% of falsification experiments must not depend on segmentation/mask metrics.
- G6 off-master awareness: every consolidator must enumerate generator shards on ALL origin branches (not just master) before accepting a commissioning plan.

## 7. Selection-time caps proposed for the existing 248 (for the 200 -> 50 cut)

- F1 PEFT factorial: keep <=4 of ~24–27.
- F2 SAM component grid: keep <=10 of ~62, each with a distinct downstream consequence.
- F3 free-detector trick: keep <=2 of 6.
- F4 cue-ablation: keep <=2 of 4 (organism ban already in force for generation).
- F5 eval-noise grid: keep <=5 of 21.
- HYPOTHESIS: these caps free ~80 slots at the 50-cut for territories that do not yet exist in master; without them the cut will be dominated by SAM internals and benchmark statistics.

## 8. Scope compliance

- Read-only with respect to canonical state: `ideas_master.jsonl`, `research_state.json`, `window.lock.json` untouched (EVIDENCE: git diff limited to `Windows13/_state/tasks/p1/diversity_audit_w1/auditor_C.*` and `done_auditor_C.json`).
- Windows13 only; own unique branch `cursor/p1-diversity-auditor-c-adversary-c2b5`; no force-push.
- Peer shards (Auditor A, Auditor B) read only AFTER my independent pass; agreements/disagreements are labeled inline above.
- No citations made; no benchmark numbers, datasets, or experimental results asserted as fact.
