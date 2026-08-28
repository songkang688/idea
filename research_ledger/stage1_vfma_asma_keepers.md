# Stage 1 ingest — VFM-A 180 + ASM-A 180

VFM-A (bc-644cc546): 180 ideas. Top keepers: A0022 worst-case valid clicks; A0051 encoder/decoder probe gap; A0028 cross-prompt disagreement error predictor; A0077 effective LoRA rank; A0101 merge interference from subspace overlap; A0121 frozen/tuned data-scale crossover; A0148 outlier-token renormalization; A0153 CLIP→DINOv2 linear spatial alignment; A0166 SA-1B/eval near-dup leak; A0168 oracle-click simulation leakage.

ASM-A (bc-bfa41bfa): 180 ideas, many LLM-generic. Vision-dense relevant keepers: A0001 rank vs OOD; A0002 LoRA tail forgetting; A0021 overtrained-small vs Chinchilla on dense; A0029 contrastive vs supervised scaling for pixels; A0033 inverse scaling of span boundaries; A0073 prompt vs LoRA under shift; A0093 synth ID+/OOD-; A0109 seed variance > method deltas; A0113 PEFT stability vanishes at matched LR; A0125 val-loss early-stop misselects OOD.

Downweight LLM-only (safety, RAG, MoE serving) for this round's final 3.
