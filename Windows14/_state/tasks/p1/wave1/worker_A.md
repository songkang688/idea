# P1 Wave A — worker_A (SAM / Foundation Model adaptation / PEFT)

- **Task:** `p1_gen_w1_a` (Windows14, window locked, identity taken verbatim from `Windows14/_state/window.lock.json`)
- **Status:** complete
- **Output shard:** `Windows14/_state/tasks/p1/wave1/worker_A.ideas.jsonl`
- **Idea count:** 132 (target was >=120)

## Method

Generated candidate ideas by systematically walking SAM's architecture and the PEFT
practice stack, and at each component asking four questions: what unexamined
observation could be made here, what assumption does the community silently hold,
what failure mode has no mechanistic account, and what would falsify the default
belief. Explicitly avoided the banned templates (Module A+B combos, SAM + loss
swaps, "just LoRA on medical X"): every idea is anchored in a mechanism, a
measurement, an audit, or an ignored assumption, and each carries a concrete
falsifiable prediction plus a fastest-falsification path (most are inference-only
or 1–3 GPU-day experiments).

Idea sources walked:

1. **Prompt interface** — click geometry priors, box gating, negative-click
   asymmetry, click-order hysteresis, prompt-subspace structure, dense-prompt audit.
2. **Mask decoder internals** — multimask token roles, IoU-head calibration and its
   destruction under PEFT, attention collapse, upscaling head, hypernetwork MLP,
   decoder depth vs topology, head specialization.
3. **Positional / resolution assumptions** — patch-grid aliasing, window seams,
   tiling-vs-resize interaction, PE-only high-res tuning, padding bias, PE-rescaling
   bug signatures.
4. **Encoder representation** — probe-based adaptability forecasting, artifact/register
   tokens, scale bands, fracture layers, shape-vs-texture bias, phase-vs-amplitude
   reliance, color (non-)use.
5. **PEFT mechanics & placement science** — rank-vs-prompt-entropy, effective-rank
   collapse, init ordering pathologies, dropout harm, weight decay as forgetting
   dial, neck/patch-embed/global-block/prompt-encoder placements, block atlas.
6. **Forgetting & interactivity** — calibration forgetting, prompt-channel-selective
   forgetting, multimask diversity collapse, click-curve damage, anchor rehearsal,
   alpha-interpolation families.
7. **Test-time & label-free adaptation** — jitter-consistency TTA, cycle
   self-supervision, stability-vs-confidence filtering, retrieval adaptation,
   test-time prompt-embedding optimization, TTA stopping rules.
8. **Evaluation methodology / meta-science** — oracle-prompt ranking fragility,
   prompt-sensitivity variance, baseline under-tuning audits, seed-variance noise
   floor, freezing-bug audits, spatial-prior embarrassing baseline, gap-decomposition
   protocol.
9. **Failure modes as first-class objects** — fractal-boundary representability,
   stuff blindness, shadow policy steering, prompt teleportation, reflection leakage,
   orientation anisotropy, JPEG-lattice resonance, process-defined regions, matting
   from logits, empty-mask prior.
10. **Systems / weight space / video / safety** — embedding-cache ceilings,
    early-exit interactivity, adapter clustering by physics, encoder-vs-decoder rank
    dichotomy, decoder transplant, SAM2 memory compounding and occlusion calibration,
    adapter backdoors, prompt-space adversarial robustness.

## Counts

- Total candidate ideas: **132**
- Clusters: 22 (largest: peft_mechanics 10, failure_modes 9, evaluation_methodology 9,
  novel_peft_mechanism 9, peft_placement 8, data_supervision_assumptions 8)
- All lines carry `evidence_status: "HYPOTHESIS"` — no novelty claims are asserted as
  verified; prior-work checks are Wave B's job.
- Validation: every line parses as JSON; all 15 required fields non-empty on all 132
  lines; id_seeds `w14A-001`..`w14A-132` unique; territory field uniform.

## Evidence hygiene

No fabricated papers, citations, benchmark numbers, or datasets. Named works are
limited to widely-known ones (SAM, SAM 2, SA-1B, LoRA, MAE, DINOv2-class
self-supervised ViTs); everything else is described generically. All novelty
statements are phrased as "appears unexplored/missing" and must be treated as
unverified hypotheses pending Wave B dedup and prior-work screening.

## Recommended next task

`p1_wave_B_dedup` — merge/dedup worker shards, screen against prior work, and only
then consider promotion toward `ideas_master.jsonl` (not this worker's job).
