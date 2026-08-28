# Stage 5 — Cluster A Nominees for the Global Top-5 Competition

**Experimental Engineer (Cloud Sub-Agent M) → Supervisor Windows7.**
Two primary nominees plus one conditional third (rule: a third only if ROI is exceptional AND it is cheap — A-0002 qualifies at ≈30 GPU-h for its killer experiment, no training, no annotation). Full designs in `stage5_cluster_A_engineering.md`; scores in `stage5_cluster_A_roi.csv`.

None of these killer experiments overlaps the B/C killer experiments (checked against `stage4_cluster_B_keep.md`, `stage4_cluster_C_keep.md`): B's are evaluation-validity/synthetic-data/supervision-mining designs, C's are training-mechanism causal tests and instrument-validation designs. A's nominees are SAM-family mechanism diagnostics with interventional levers — a distinct lane in the global portfolio.

---

## NOMINEE 1 — A-0017: Causal memory surgery for SAM2 (validated upper-bound diagnostic) — ROI 9.0

**Claim.** Targeted deletion of post-error memory entries decomposes organic SAM2 tracking failure into memory-borne (reversible) and representation-borne (irreversible) shares, and that decomposition is a *validated instrument*: it predicts what independent prevention methods gain.

**Killer Experiment (preregistered, ≈60 GPU-h, zero training).** On ≥200 protocol-harvested organic failures from LVOS v2 + DiDi, at GT reappearance run three arms — (i) targeted deletion (keep conditioning-frame + pre-error memories), (ii) full reset to conditioning frame only, (iii) no-op. Pass requires BOTH:
1. Targeted beats no-op by ≥30 pts AND beats full reset by ≥10 pts (else "surgery" is just the decades-old reset heuristic — the Stage-4 attack wins);
2. Per-sequence reversible fraction predicts per-sequence J&F gains of SAMURAI *and* DAM4SAM at r > 0.6 (else the diagnostic measures nothing prevention methods exploit, and the paper reports the instrument dead).

**Why it competes globally.** Hottest model family (SAM2 video); zero training; every branch of the outcome tree is publishable (headroom table, instrument-death negative, or natural-recovery benchmark finding); comparators (SAMURAI, DAM4SAM, SAM2Long) are all public, training-free SAM2.1 wrappers, so validity runs are cheap and clean.

**Codebases:** facebookresearch/sam2, yangchris11/samurai, jovanavidenovic/DAM4SAM, Mark12Ding/SAM2Long, LingyiHongfd/LVOS + lvos-evaluation. **Budget:** ≈80–120 GPU-h, 1× A100-40GB.

---

## NOMINEE 2 — A-0061: Boundary Nyquist — cutoff at, or far below, the decoder's sampling limit — ROI 8.5

**Claim.** The empirical contour-frequency cutoff of segmentation decoders sits either at the architectural sampling limit (sampling-limited: raising decoder resolution buys boundary quality) or well below it (training-limited: the field's default fix is wasted). The theorem fixes the bound; the experiment finds the operating point — and either world changes decoder-design decisions.

**Killer Experiment (≈15 GPU-h, inference-only).** The **cutoff-ratio table**: for ≥4 architectures at ≥3 output resolutions (SAM 256² path, HQ-SAM's high-res token path, SAM2, Mask2Former), measure the empirical error-energy cutoff on a synthetic parametric contour suite with *exact analytic ground truth* (annotation-bias attack dead by construction) plus DIS-5K fine masks, and divide by the oracle bound obtained by passing GT through each decoder's own output grid (no model in the loop). Ratio ≈ 1 across models = sampling-limited; ratio ≪ 1 = training-limited. One measured table settles the verdict, plus the octave-shift test: does the cutoff move by one octave when output resolution doubles?

**Why it competes globally.** Cheapest survivor (10–20 GPU-h core, no training, no annotation); both outcomes redirect real engineering budgets (whether HQ-style resolution work is the right lever); cross-model design-law framing gives it more reach than a single-model audit; the synthetic suite is a reusable released artifact.

**Codebases:** facebookresearch/segment-anything, SysCV/sam-hq, facebookresearch/sam2, facebookresearch/Mask2Former, xuebinqin/DIS, hbldh/pyefd, deepmind/surface-distance. **Budget:** ≈10–20 GPU-h, single GPU.

---

## CONDITIONAL THIRD — A-0002: Spectral surgery on SAM's prompt-encoder RFF — ROI 8.0

**Kept under the cheap-and-exceptional rule:** the entire killer battery is ≈30 GPU-h, inference-only, white-box, and Stage 4's strongest attack (attribution ambiguity between three architectural gratings) is answered by a *discriminating* test, not a consistency check.

**Killer Experiment (≈30 GPU-h, inference-only).** On the same ≥500 objects, one battery: (i) bandlimit only the point-path RFF rows at inference (dense image PE untouched) vs (ii) equal-energy random-row attenuation control; (iii) compare measured flip-map spectra against the *exactly known* RFF spectrum vs the 16-px patch-grid comb (quantitative model comparison — the two hypotheses make different predictions); (iv) shift AMG's 32×32 prompt grid by a half period and measure instance-recall movement (the machine-prompting consequence that answers "sub-pixel flips are below human click noise, who cares"). Pass = flips track the RFF manipulation, not the control, and spectra favor the RFF model. Fail = clean attribution negative redirecting to the patch grid — also publishable.

**Why third and not higher.** Cleanest causal design in the cluster and the cheapest, but the phenomenon's significance ceiling is lower than the two nominees': even a full win is a mechanism attribution plus an AMG-protocol recommendation, not a field-redirect.

**Codebases:** facebookresearch/segment-anything, emb-ai/rclicks, SysCV/sam-hq, ChaoningZhang/MobileSAM, facebookresearch/sam2. **Budget:** ≈80–100 GPU-h full, ≈30 GPU-h killer battery, single GPU.

---

## Why the other four dropped

- **A-0178 (artifact tokens → prompt failures, ROI 7.5).** Best upside-per-GPU-hour of the drops, but it carries an existential gate: Darcet et al. note MAE-lineage encoders (SAM's ancestry) show weak-to-no artifacts, so the flagship model may void on day 1. The gate is cheap (~1 GPU-h audit) and honest — recommend running the audit as a side quest regardless — but a nominee whose flagship arm may not exist can't take a global slot from two designs with no existential risk.
- **A-0107 (PEFT swap matrix, ROI 7.0).** Both outcome branches carry content and the dual-decoder serving table has real deployment teeth, but it is the only survivor needing a substantial training program (~450 GPU-h, 34 runs), and its novelty sits closest to an instantiation of LP-FT — the weakest position in a global competition judged on surprise-per-dollar.
- **A-0062 (sigma-stratified HQ re-scoring, ROI 6.5).** The sigma-stratification + injected-improvement-calibration design is decisive, but the binding constraint is external: $4–8k and 250–400 annotator-hours of careful boundary tracing before the headline read exists. It also competes in the evaluation-validity lane where Cluster B already fields two pure-analysis nominees (B-0121, M5) — the global portfolio doesn't need a third validity instrument from A. The zero-cost LIDC-IDRI pilot is worth running before any revival.
- **A-0271 (SA-1B filter fingerprints, ROI 6.0).** Strategically the biggest question (auto-labeling era) with a clean same-image causal design, but ≈1,000 GPU-h across relabeling plus five student trainings makes it the cluster's most expensive survivor by 2×. Its 25-GPU-h MVE (label-arm signature deltas only, no training) is a cheap option the supervisor can exercise independently; the full program should only run if the MVE gate passes and budget exists after the global top-5 is funded.

---

**Branch:** `cursor/stage5-cluster-a-engineering-ed30` (contains full Stage-3/4 lineage plus the three Stage-5 outputs).
