# exp_08 — A-0199-mut: context-completion hallucination in CLASSICAL segmenters — the dose-response law (L revive)

**ID:** W2-A-0199-mut (J's mutation, upgraded per L revive #2: bigger than the "sliver" J granted — NOT the VLM version).
**Pipeline status:** A original → F #16 (never web-attacked) → J framing-KILL via HalluSegBench (arXiv:2506.21546) + HII-DPO (arXiv:2602.10425), mutation survives → L: both scooping papers are VLM-side; the training-data-grounded dose-response version is "the scientifically stronger half" → PI binding revive slot.

## Positioning (mandatory)

HalluSegBench (referring/reasoning segmentation VLMs, counterfactual pairs) and HII-DPO (captioning hallucination, co-occurrence priors, DPO fix) are cited as the **motivating phenomenon** — both EVIDENCE, verified by J and L. Neither can run the causal, training-data-grounded version: **VLMs' training data is unknown; classical segmenters' training data is fully known.** This paper is the mechanism/dose-response complement: hallucination rate as a quantitative function of *mined training co-occurrence strength*.

## Research question

Do classical segmentation networks hallucinate scene-typical classes (water under bridges, sky through gaps) at rates predicted by their training corpus's co-occurrence statistics — a dose-response law — and do those pixels rely on context rather than local appearance?

## Falsifiable hypothesis

H1 (dose-response): hallucinated-pixel rate for class c in context k is an increasing function of the training-set association strength A(c,k) mined from the model's own training corpus, monotone across association deciles, per model family.
H2 (mechanism): evidence-ablation (masking the local region while preserving context) leaves hallucinations largely intact; context-ablation removes them.
Falsified if: hallucination rates are at annotation-noise levels for classical segmenters (the phenomenon is VLM-specific), or rates are flat across association deciles (no dose-response — hallucination exists but co-occurrence doesn't predict it).

## Prediction

HYPOTHESIS: classical segmenters hallucinate less than VLMs but non-trivially, with a monotone (possibly saturating) dose-response. J's hidden assumption 3 (rates non-trivial) is explicitly a pilot gate — no number is assumed.

## Method sketch (modules / dataflow)

1. **Co-occurrence miner:** pairwise class-context association statistics (P(c present | k present), PMI) from ADE20K / COCO-Stuff / Cityscapes *training* sets — exact corpora of the model zoo.
2. **Counterfactual builder (editing-based, per J's cross-cutting note "curation loses to editing"):** inpaint the target class out of context-strong scenes (dry the canal, empty the pool); **artifact control**: matched inpainting edits at context-neutral locations of the same images, so inpainting artifacts affect both arms equally.
3. **Real-scene arm (small):** curated genuinely-absent scenes (dry canals, bridges over roads) as the ecological-validity check only (J's re-scoping).
4. **Hallucination scorer:** per-model hallucinated-pixel rate = predicted-c pixels inside the edited region verified absent; stratified by association decile.
5. **Evidence/context ablation:** local-patch masking vs context masking (H2).
6. **Model zoo:** ≥3 classical families (CNN FCN-line, SegFormer-class transformer, DeepLab-line) trained on the mined corpora — off-the-shelf checkpoints only.

## Data

ADE20K, COCO-Stuff, Cityscapes (training sets for mining, val scenes for editing); ~1–2k edited counterfactuals + ~200 curated real scenes.

## Baselines

Chance/prior-rate baseline (class base rate); annotation-noise floor on unedited regions; HalluSegBench-style VLM numbers quoted for scale context (not compared head-to-head — different task); association-strength-shuffled null (dose-response must beat a permutation test).

## Metrics

Hallucinated-pixel rate per association decile with permutation-test p-values; slope/shape of fitted dose-response per family; H2 ablation deltas; cross-corpus transfer (does a law fitted on ADE20K predict COCO-Stuff-trained models?).

## Killer Experiment

**One corpus (ADE20K), 3 model families, 10 association deciles × ~100 edited counterfactuals + artifact controls → the decile curve with permutation null.** ~2 GPU-days (L's estimate, confirmed plausible: inference + inpainting only). The curve either rises monotonically or the flagship dies immediately.

## GPU/VRAM/time estimate

Inpainting generation: ~1 GPU-day (diffusion inpainter, 24GB). Segmenter inference: ~1–2 GPU-days across the zoo. Full study incl. second corpus + ablations: **≤1 GPU-week.** Curation: ~1–2 weeks part-time for the real-scene arm.

## Stop / pivot / kill criteria

- **Pilot gate (first 2 GPU-days):** if hallucination rates on the top association decile are within the annotation-noise floor → the phenomenon is VLM-specific → publish a short negative note ("classical dense predictors do not context-hallucinate measurably"), kill the flagship.
- **Pivot** if hallucination exists but is decile-flat → the paper becomes "context hallucination is not co-occurrence-driven in classical models" — a genuine surprise contradicting the VLM-side mechanism papers (Causal-LLaVA 2505.19474, Image Tokens Matter 2505.21547, both J-verified); smaller but sharper.
- **Kill** if a classical-segmenter dose-response paper appears (re-search at freeze; the VLM hallucination field is prolific and could port down-stack any quarter).

## Reviewer-2 leftover

Inpainting artifacts as a systematic confound is the attack that never fully dies — the matched-edit control bounds it but a determined reviewer will ask for a second editing method (add one: generative fill vs exemplar-based). "True absence" verification for the real-scene arm is manual and small-N; keep that arm decorative, not load-bearing.

## Expected result (HYPOTHESIZED, not measured)

Monotone dose-response in at least 2/3 families; H2 shows context dependence for high-decile hallucinations; cross-corpus transfer partial.

## Negative-result interpretation

A clean null (no measurable classical hallucination) cleanly separates the phenomenon's locus: context-completion hallucination would then be a property of *language-aligned* models, not of dense prediction per se — directly informative for the VLM mechanism debate, and cheap enough that the null costs almost nothing.
