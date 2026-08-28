# P1 Wave A - Generator H Shard: Super-Resolution / Restoration (Windows13)

- **task_id**: `p1_gen_h_sr_restoration`
- **role**: generator (candidate ideas only; NO verified-novelty claims)
- **windows_id**: Windows13 (locked; canonical state untouched)
- **territory**: Super-resolution / restoration - degradation modeling, real-world blind restoration, perceptual-fidelity trade-offs, foundation-model failure modes for restoration, ignored assumptions
- **idea_count**: 100 (id_seed range `W13-P1-H-001` .. `W13-P1-H-100`)
- **evidence policy**: every record labels its claims with [KNOWN FACT] / [HYPOTHESIS] / [EXPECTED RESULT] / [MODEL SPECULATION]. No fabricated papers, numbers, datasets, or experimental results. All predictions are EXPECTED, none were run.
- **novelty status**: `why_possibly_novel` fields are UNVERIFIED model speculation; Wave B dedup + novelty verification must treat all of them as unchecked.

## Cluster overview

| cluster | count | ids |
|---|---|---|
| degradation-modeling | 12 | 001-012 |
| blind-real-world | 10 | 013-022 |
| perception-distortion | 10 | 023-032 |
| generative-prior-failures | 12 | 033-044 |
| fm-restoration | 10 | 045-054 |
| benchmark-weaknesses | 10 | 055-064 |
| ignored-assumptions | 10 | 065-074 |
| video-temporal | 8 | 075-082 |
| downstream-coupling | 8 | 083-090 |
| training-dynamics | 10 | 091-100 |

## Candidate ideas (one-liners)

### degradation-modeling (12)

- **W13-P1-H-001** - The synthetic-to-real gap in super-resolution is dominated by unmodeled noise and compression, not by blur-kernel mismatch, so blind-kernel estimation attacks a second-order problem.
- **W13-P1-H-002** - Large randomized degradation pipelines teach models the artifact statistics of the pipeline itself, and a small set of camera-measured degradations transfers better to real photos.
- **W13-P1-H-003** - The composition order of degradations matters more than degradation diversity for real-world restoration transfer.
- **W13-P1-H-004** - Per-image single-kernel estimation in blind SR is a mis-specified problem because real point-spread functions are spatially varying and chromatically aberrated.
- **W13-P1-H-005** - Modeling degradations in the raw sensor domain and passing them through an ISP simulator transfers better than modeling degradations directly in sRGB space.
- **W13-P1-H-006** - Replacing additive white Gaussian noise with signal-dependent heteroscedastic noise is the single largest lever in degradation modeling for real-world SR.
- **W13-P1-H-007** - Degradation pipelines undersample the mild-degradation regime that dominates real photos, so blind models are miscalibrated toward over-restoration of nearly clean inputs.
- **W13-P1-H-008** - Modern phone photos are already processed by on-device neural enhancement, so the dominant real-world degradation family is neural-network-induced, and classic degradation models are increasingly obsolete.
- **W13-P1-H-009** - Many practically low-quality images were never downsampled, so framing super-resolution as inverse downsampling is a category error for a large share of use cases.
- **W13-P1-H-010** - Blind-SR kernel estimates are echoes of the learned image prior rather than measurements, and they collapse on images that violate natural-image statistics.
- **W13-P1-H-011** - A few minutes of per-device calibration beats universal blind restoration, because devices cluster tightly in degradation space.
- **W13-P1-H-012** - A degradation-space distance between training pipeline outputs and real photos predicts real-world transfer better than benchmark scores do.

### blind-real-world (10)

- **W13-P1-H-013** - Real-world paired SR benchmarks reward slight blur because zoom-lens pair alignment errors make hedged, soft predictions optimal under full-reference metrics.
- **W13-P1-H-014** - Unpaired real-world restoration methods secretly depend on the same hand-crafted degradation assumptions they claim to avoid.
- **W13-P1-H-015** - Per-image test-time adaptation from internal recurrence beats adding more pretraining data for real-world restoration at foundation scale.
- **W13-P1-H-016** - Blind restoration models violate a do-no-harm principle on clean inputs, and identity preservation on high-quality images should be a mandatory reported metric.
- **W13-P1-H-017** - Blind restoration fails as a cliff, not a slope, just outside its training severity range, and the cliff location is predictable from training data alone.
- **W13-P1-H-018** - A small mixture-of-experts routed by degradation archetype beats a monolithic blind model of equal total capacity on real photos.
- **W13-P1-H-019** - A single user-facing fidelity-versus-enhancement dial captures most practical value of degradation estimation, making precise automatic estimation unnecessary for consumer restoration.
- **W13-P1-H-020** - The blind restoration setting ignores freely available capture metadata that carries most of the degradation information the models struggle to estimate.
- **W13-P1-H-021** - Restoration models fail systematically on non-photographic content because both degradation models and image priors are photo-centric, and a content-type failure taxonomy would expose this blind spot.
- **W13-P1-H-022** - Analog degradations in old photos form a structurally different family from digital ones, and models trained on digital pipelines hallucinate when facing film-era artifacts.

### perception-distortion (10)

- **W13-P1-H-023** - The practically relevant perception-distortion tradeoff is per-region, not per-model, and a single global operating point is wrong for most images.
- **W13-P1-H-024** - Learned perceptual metrics are gameable by artifact styles matched to their training distribution, and metric-tuned SR models exhibit a recognizable metric texture.
- **W13-P1-H-025** - Human preference between faithful and hallucinated restorations reverses with viewing time and ground-truth knowledge, so time-limited studies structurally favor hallucination.
- **W13-P1-H-026** - The empirical perception-distortion frontier is largely a loss mis-specification artifact, and a properly specified conditional likelihood model can dominate both endpoints simultaneously.
- **W13-P1-H-027** - On real-world paired datasets, the reported perception-distortion tradeoff is confounded by ground-truth misalignment, which taxes fidelity-oriented models more than generative ones.
- **W13-P1-H-028** - Replacing distortion-to-reference with consistency-to-observation as the fidelity axis makes the perception tradeoff much milder, and consistency should be the reported fidelity metric for generative restoration.
- **W13-P1-H-029** - Human-preferred restorations systematically degrade machine consumption (OCR, recognition), so perceptual quality and machine quality are diverging objectives needing separate outputs.
- **W13-P1-H-030** - Restoration models should output a hallucination map, and cross-seed variance of generative restorers already provides one that flags fabricated regions.
- **W13-P1-H-031** - Perceived restoration quality saturates under realistic viewing conditions, and beyond a resolvable-detail threshold the field is optimizing differences invisible to users.
- **W13-P1-H-032** - GAN-versus-diffusion differences in restoration quality are dominated by training data and loss weighting rather than the generative framework itself.

### generative-prior-failures (12)

- **W13-P1-H-033** - Hallucination severity in generative SR scales with prior strength: the better the generative model, the more confidently it fabricates the wrong content.
- **W13-P1-H-034** - Face restoration homogenizes identity, drifting restored faces toward the training distribution's typical attributes, measurable as systematic embedding shift.
- **W13-P1-H-035** - Restoration models should abstain on illegible text instead of fabricating legible wrong characters, and text-aware abstention is implementable without hurting non-text quality.
- **W13-P1-H-036** - Late-stage sampling in diffusion-based SR is only weakly conditioned on the input, so the fine detail users see is mostly prior draw rather than evidence.
- **W13-P1-H-037** - Sample diversity in stochastic restoration is misallocated: seeds vary irrelevant texture while collapsing on semantically ambiguous content where diversity actually matters.
- **W13-P1-H-038** - Fixed default guidance scales in diffusion restoration are wrong for most images, and per-image guidance calibration from consistency residuals recovers substantial quality for free.
- **W13-P1-H-039** - Cross-seed agreement in generative restoration is treated as certainty, but agreement can be confidently wrong, and the agreement-accuracy relationship has never been calibrated.
- **W13-P1-H-040** - One-step distilled diffusion restorers quietly revert to GAN-like regression behavior, losing the posterior diversity that justified diffusion while keeping its reputation.
- **W13-P1-H-041** - Latent-space restoration has a hard fidelity floor set by the autoencoder, and the field under-reports how much fine text and texture is lost before restoration even begins.
- **W13-P1-H-042** - Generative restorers are unstable inverse maps: imperceptible input perturbations flip hallucinated semantic content, undermining forensic use.
- **W13-P1-H-043** - Generative restorers can inject memorized training images into outputs on ambiguous inputs, and restoration needs a memorization-probe protocol like generation has.
- **W13-P1-H-044** - The field needs a formal restoration-versus-reimagination boundary based on information recoverable from the observation, and most perceptual SR crosses it without disclosure.

### fm-restoration (10)

- **W13-P1-H-045** - Text-to-image foundation priors import aesthetic bias into restoration: outputs drift toward beautified renditions rather than faithful ones.
- **W13-P1-H-046** - Vision-language-guided restoration converts caption errors into confident pixel hallucinations, a compounding error mode absent from caption-free restorers.
- **W13-P1-H-047** - Restoration quality saturates with model scale much earlier than generation quality because the task is observation-bounded, making restoration a poor showcase for foundation-scale compute.
- **W13-P1-H-048** - Universal all-in-one restoration models suffer negative transfer on hard cases, losing to per-task specialists at matched capacity despite average-metric parity.
- **W13-P1-H-049** - Self-supervised foundation features are worse perceptual-loss backbones than older supervised features because SSL objectives explicitly learn invariances that a fidelity metric must not have.
- **W13-P1-H-050** - Instruction-based restoration is prompt-fragile: paraphrases of the same enhancement request produce materially different outputs, and no benchmark measures this instability.
- **W13-P1-H-051** - A systematic failure atlas of foundation-model restoration would show failures concentrating where the prior is strongest and the evidence weakest, inverting the intuition that strong priors help most on hard content.
- **W13-P1-H-052** - In-context restoration examples act as style anchors rather than degradation evidence: shuffled or mismatched example pairs work nearly as well as correct ones.
- **W13-P1-H-053** - Hallucination severity in restoration increases with the underlying generative model's training compute, making prior scale a liability metric that should be disclosed.
- **W13-P1-H-054** - Repeated passes through neural processing (restoration, editing, recompression) create a compounding neural degradation family that classic degradation models cannot express, and future restorers must model it explicitly.

### benchmark-weaknesses (10)

- **W13-P1-H-055** - Standard SR ground truths are themselves degraded, imposing a hidden quality ceiling and penalizing models that exceed ground-truth quality.
- **W13-P1-H-056** - Classic SR test sets are tiny and photographically dated, and method rankings would reshuffle on modern imagery, meaning part of reported progress is dataset-era artifact.
- **W13-P1-H-057** - Luma-only PSNR evaluation lets SR models neglect chroma, and hidden color artifacts are widespread but unmeasured.
- **W13-P1-H-058** - Silent differences in evaluation conventions (border cropping, color conversion, bit-depth handling) across SR papers are large enough to reorder nearby methods, and a conventions audit would reveal non-reproducible margins.
- **W13-P1-H-059** - No-reference quality metrics actively reward hallucination in generative SR because modern fabrication artifacts lie outside their training distortion domains.
- **W13-P1-H-060** - Crop-based human studies over-sample regions where hallucination looks good, and whole-image task-driven protocols would flip some perceptual-SR conclusions.
- **W13-P1-H-061** - The community has collectively overfit standard SR benchmarks through years of repeated evaluation, and a freshly collected secret test set would compress claimed differences.
- **W13-P1-H-062** - Re-degradation consistency (does the restored image reproduce the observed input under the forward model) should be a mandatory reported metric, and many perceptual SR models fail it badly.
- **W13-P1-H-063** - Real degradation severity is bimodal (mostly mild plus a hard tail) while benchmarks concentrate on mid-range severity, so deployment-weighted evaluation would change model choices.
- **W13-P1-H-064** - Expected-distortion evaluation of stochastic restorers penalizes legitimate posterior diversity, and set-based or distributional fidelity metrics are required to compare generative restoration fairly.

### ignored-assumptions (10)

- **W13-P1-H-065** - Training restoration losses in gamma-encoded sRGB misweights shadow and highlight errors, and linear-light loss computation changes model behavior visibly in low light.
- **W13-P1-H-066** - The field optimizes 4x magnification while deployment overwhelmingly needs mild continuous scales, and mild-scale performance is not predicted by 4x benchmark scores.
- **W13-P1-H-067** - High-resolution training targets contain sensor noise that models learn to reproduce, so part of learned texture synthesis is actually noise imitation, and denoised-target training changes the perceptual character of outputs.
- **W13-P1-H-068** - Real degradations vary strongly across the frame, and globally-conditioned restoration produces spatially inconsistent quality that per-region degradation conditioning fixes.
- **W13-P1-H-069** - Restoration models exploit the correlation between content and degradation in real data as a shortcut, and they misrestore counterfactual images where the correlation is broken.
- **W13-P1-H-070** - Tiled inference silently degrades large-image restoration through seam artifacts and context truncation, and patch-benchmark scores hide a whole-image quality gap.
- **W13-P1-H-071** - Training against a single ground-truth realization teaches models false confidence at high magnification, and the one-target assumption is the root of both blur (regression) and overconfident fabrication (generation).
- **W13-P1-H-072** - Eight-bit quantization of training pairs imposes an ignored information floor, causing banding-related failure modes and capping low-contrast detail recovery that higher-bit-depth training would unlock.
- **W13-P1-H-073** - Restored images are almost always re-compressed downstream, and optimizing restoration jointly with expected re-compression changes what the optimal output looks like, devaluing fragile hallucinated texture.
- **W13-P1-H-074** - Restoration models entangle tone and color enhancement with structural restoration, and disentangling shows part of perceived restoration quality is uncredited color grading.

### video-temporal (8)

- **W13-P1-H-075** - Warped-frame temporal consistency metrics reward temporally stable hallucination over faithful but variable detail, making them anti-fidelity in exactly the hard cases.
- **W13-P1-H-076** - The multi-frame advantage of video SR collapses on properly anti-aliased or heavily compressed footage, because models exploit temporal aliasing as their main cross-frame cue.
- **W13-P1-H-077** - Codec-informed video restoration using bitstream metadata (block boundaries, motion vectors, quantization levels) beats blind pixel-space restoration at equal capacity, and discarding the bitstream is an unforced error.
- **W13-P1-H-078** - Recurrent video restorers accumulate hallucination drift over long sequences, diverging from input content in ways short-clip benchmarks never measure.
- **W13-P1-H-079** - Short-clip training gives recurrent video restorers an implicit state-reset bias, making their effective temporal receptive field far shorter than architecture diagrams claim.
- **W13-P1-H-080** - Face-video enhancement alters lip and expression micro-motion, measurably changing perceived speech and emotion, a safety-relevant failure invisible to every current metric.
- **W13-P1-H-081** - Video restoration allocates compute suboptimally across frames: temporal information saturates after a few neighbors, and reallocating compute to per-frame quality dominates at fixed budget.
- **W13-P1-H-082** - Synthetic video SR benchmarks miss the coupling between motion blur, shutter time, and frame rate in real capture, and this coupling breaks synthetic-to-real transfer more than spatial degradation mismatch.

### downstream-coupling (8)

- **W13-P1-H-083** - Restore-then-recognize pipelines lose to recognition models trained directly on degraded inputs, because restoration destroys machine-relevant evidence while adding human-pleasing detail.
- **W13-P1-H-084** - Generative restoration invalidates images as evidence, and restoration systems for forensic contexts should emit per-region fidelity certificates grounded in observation consistency.
- **W13-P1-H-085** - Natural-photo priors contaminate scientific imagery: restoration models trained on photographs inject natural-image statistics into scientific data, creating plausible artifacts that could mislead analysis.
- **W13-P1-H-086** - In safety-critical imaging, hallucination concentrates on exactly the fine structures that matter most, and abstention-based restoration (enhance only what evidence supports) is the correct product for these domains.
- **W13-P1-H-087** - Restoration-as-decoder compression schemes (send low quality, restore at receiver) are evaluated with perceptual metrics that hide semantic drift, and round-trip semantic audits would cap their claimed bitrate savings.
- **W13-P1-H-088** - Human-optimal and OCR-optimal restorations of degraded text diverge: images that read best to machines look worse to humans, motivating task-conditional restoration outputs.
- **W13-P1-H-089** - For machine consumption, restoring feature embeddings directly beats restoring pixels first: pixel space is a human-oriented bottleneck that wastes capacity on visually pleasing but task-irrelevant detail.
- **W13-P1-H-090** - Face enhancement shifts identity-verification scores asymmetrically across demographic groups, so restoration can silently change biometric outcomes with disparate impact.

### training-dynamics (10)

- **W13-P1-H-091** - Most claimed architecture gains in SR are training-recipe gains: under matched modern recipes, a decade of architectural innovations compresses into a much smaller quality spread than the literature implies.
- **W13-P1-H-092** - SR models are not scale-consistent (twice 2x differs from once 4x), and enforcing scale-composition consistency at training improves generalization to unseen scales for free.
- **W13-P1-H-093** - Small-crop training biases SR models against global structure: long edges, vanishing lines, and large-scale gradients are reconstructed with systematic errors that large-context training fixes.
- **W13-P1-H-094** - SR models get amplitude spectra roughly right but phase systematically wrong, and phase error is the better predictor of perceived structural artifacts, motivating phase-aware losses.
- **W13-P1-H-095** - Restoration data scaling hits diminishing returns quickly on content diversity but not on degradation diversity, so data budgets should buy degradations, not images.
- **W13-P1-H-096** - SR models collapse rare textures onto common ones: outputs re-render unusual materials as the nearest frequent texture family, a measurable prior-collapse effect invisible to aggregate metrics.
- **W13-P1-H-097** - Blind training over mixed severities teaches models a severity-averaged inverse that is wrong for every severity, and cheap explicit severity conditioning dominates blind averaging.
- **W13-P1-H-098** - Overparameterized SR models memorize training patches retrievably: nearest-neighbor probes on outputs would reveal patch-level copying, qualifying texture-generalization claims.
- **W13-P1-H-099** - Iterative refinement helps sampling, not restoration: at matched compute, single-pass fidelity models match multi-step ones, and iteration only pays when the goal is drawing from a distribution.
- **W13-P1-H-100** - Test-time geometric self-ensembling gains expose a fixable equivariance defect: equivariance-regularized training recovers the ensemble's benefit in a single pass.
