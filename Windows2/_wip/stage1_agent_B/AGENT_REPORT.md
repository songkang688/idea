# AGENT_REPORT — Windows2 Stage 1, Cloud Sub-Agent B

Role: independent idea generator for the VFM / multimodal / fine-tuning / PEFT angle
clusters. Stage 1 only — no final-3 selection, no later-stage work, no overlap with
Agent A (SAM/medical/smoke seg) or Agent C (detection/eval/assumptions) territories.

## Deliverables

| File | Content |
|------|---------|
| `Windows2/_wip/stage1_agent_B/ideas.md` | Full human-readable catalog, 345 ideas grouped by cluster |
| `Windows2/_wip/stage1_agent_B/ideas.jsonl` | One JSON record per idea (machine-readable, same content) |
| `Windows2/_wip/stage1_agent_B/clusters.md` | Cluster map, ID ranges, mutation lineages, counter-intuitive flagships |
| `Windows2/_wip/stage1_agent_B/AGENT_REPORT.md` | This report |

## Counts

- Total ideas: **345** (target ≥340), IDs `W2-B-0001` … `W2-B-0345`, strictly sequential.
- Per-cluster: vfm_failure 35, vlm_dense_failure 35, finetune_instability 30, peft_limits 35,
  catastrophic_forgetting 30, prompt_sensitivity 30, representation_mismatch 30,
  crossdomain_frozen_vs_tuned 28, synthetic_adaptation 25, medical_vfm_science 25,
  language_geometry_alignment 25, agentic_vision_hypotheses 17.
- Every idea has: id, one_liner, problem, core_hypothesis, why_important, why_possibly_novel,
  minimal_experiment, main_risk, cluster; 231 ideas carry `mutate_from` lineage links
  (validated to point to earlier existing IDs).
- 68 ideas carry `UNVERIFIED — needs lit search` tags on prior-work claims. No papers,
  citations, or numbers were fabricated.

## Rule compliance

- Forbidden patterns excluded by construction: no module stacking, no "apply CLIP to X",
  no new adapter layers, no "LoRA on SAM" engineering papers, no loss-only papers, no
  backbone swaps. Ideas are framed as falsifiable scientific hypotheses with a stated
  minimal experiment and main risk.
- Counter-intuitive directions requested by the brief are represented, e.g. inverse scaling
  for small-object segmentation (0013), inverse stability scaling (0092), language
  supervision worsening depth/boundaries (0307, 0306), PEFT preserving wrong invariances
  (0104), PEFT as privacy liability (0133), forgetting as desired behavior (0137, 0158),
  synthetic data trading calibration for accuracy (0254), cleaner labels transferring
  worse (0227).

## 15 highest-ROI candidates (Agent B's own ranking — supervisor decides)

1. `W2-B-0001` — High-norm outlier tokens in DINOv2 spatially predict downstream segmentation error hotspots.
2. `W2-B-0042` — Synonym instability: open-vocab segmentation varies more across synonyms of one class than across model generations.
3. `W2-B-0074` — The CLIP modality gap collapses abruptly during fine-tuning, and the collapse step predicts zero-shot robustness loss.
4. `W2-B-0098` — LoRA dynamics are largely reproduced by full fine-tuning with a rescaled learning rate, questioning capacity-based explanations of PEFT stability.
5. `W2-B-0104` — PEFT preserves pretrained invariances that dense tasks must break, creating an invariance-inheritance ceiling.
6. `W2-B-0136` — Most "catastrophic forgetting" in VFM adaptation is feature rotation, not erasure, recoverable by re-fitting readouts.
7. `W2-B-0154` — Decoder capacity governs backbone forgetting: heavy heads let backbones stay intact, linear heads force destructive rewriting.
8. `W2-B-0175` — Interactive segmentation rankings are simulation-policy artifacts: model orderings flip across simulated user policies.
9. `W2-B-0200` — Linear-probe methodology systematically underestimates dense information, misranking VFMs for dense use.
10. `W2-B-0203` — Bilinear feature upsampling, not feature content, is the binding constraint in frozen-VFM segmentation pipelines.
11. `W2-B-0226` — Frozen features degrade gracefully under shift while tuned features fail sharply, defining a measurable "shift budget" per model.
12. `W2-B-0254` — Synthetic training data buys mean accuracy but sells calibration: generated-data adaptation systematically miscalibrates dense models.
13. `W2-B-0293` — Matched-budget ablation of "medical foundation models": how much do they beat natural VFMs plus medical readouts, really?
14. `W2-B-0307` — Adding language alignment to pretraining degrades metric depth structure relative to purely visual objectives at matched data.
15. `W2-B-0332` — Visual chain-of-thought is often post-hoc theater: intermediate boxes change answers even when wrong, and answers persist when boxes are corrected.

## Method notes for the supervisor

- Ideas were generated per cluster along explicit variation axes (model family, phenomenon,
  task, data regime, measurement) and deduplicated by mechanism, not by wording; where two
  ideas share a mechanism they are chained via `mutate_from` instead of duplicated.
- `clusters.md` lists eight cross-cluster lineages (outlier tokens, invariance-as-liability,
  nameability boundary, calibration-first, frozen-vs-tuned regime theory, PEFT mechanism
  attribution, forgetting-measurement reform, self-referential data loops) that are natural
  units for Stage-2 evolution/mutation.
- Stage-2 lit-search priority: the 68 `UNVERIFIED` tags, especially where an idea's novelty
  claim depends on the absence of prior work (0001, 0098, 0136, 0200, 0213, 0254, 0293).
- Commit for this delivery: `Windows2 Stage1 Agent B: VFM/PEFT/VLM idea catalog` on branch
  `cursor/windows2-stage1-agent-b-8950` (hash reported in the supervisor message; this file
  is part of that commit so cannot embed its own hash).
