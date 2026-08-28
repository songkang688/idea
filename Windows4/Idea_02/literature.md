# PromptAmnesia — Literature Review (Windows4 / Idea_02)

**Epistemic status:** LITERATURE REVIEW. Every citation below is **inherited from the Windows4 Stage-3/4
verification passes** (`selection_history/stage3_kill_peft_vlm.md`, `stage4_r2_setB.md`,
`literature_anchors.md`). Tags carried forward verbatim:

- `[V]` — fetched and read (abstract or full text) by a Stage-3/4 agent on 2026-08-28;
- `[M]` — memory-cited classic: high confidence it exists, **must be re-verified against arXiv before any
  manuscript quotes it** (tracked as release blocker in `roadmap.md`).

No new citations were added at Stage 7 and no citation below is fabricated. No experimental result of ours
is claimed anywhere in this file.

---

## 1. The phenomenon: fine-tuning erodes SAM's zero-shot behavior

| Paper | Tag | What it establishes | Why it does not close our question |
|---|---|---|---|
| Gu et al., *How to build the best medical image segmentation algorithm using foundation models*, MELBA 2025, arXiv:2404.09957 | [V] | 18 fine-tuning combinations × 17 datasets; vanilla full FT causes collapse/catastrophic forgetting on ViT-B/H; PEFT in enc+dec superior; documents ineffectiveness of popular methods; includes decoder-only arms | Measures **in-domain Dice**; no per-prompt-type zero-shot retention, no matched-gain control, no coverage/forgetting separation, no noise floor |
| CA-SAM, *Continual Alignment for SAM*, arXiv:2511.17201 | [V] | States erosion of generalization as known motivation; method preserves zero-shot on unseen medical datasets (9-dataset continual benchmark); locates the problem at the encoder–decoder interface (Alignment Layer) | Reports OOD Dice of *their* method — not a controlled audit; no prompt-type resolution; interface framing is methodized, not causally probed |
| EvoSAM, arXiv:2503.06236 | [V] | LoRA-expert continual SAM; CL baselines applied to SAM/MedSAM | Fix-lane paper; presupposes the measurement we audit |
| MedSAM, Ma et al., Nature Communications 2024, arXiv:2304.12306 | [M] | Box-only fine-tuning; point prompting unsupported/poor | This is the **coverage effect** — our null model (§8 of proposal), not forgetting |
| SAM-Med2D, Cheng et al., arXiv:2308.16184 | [V] | Fine-tunes with boxes+points+masks; publishes Bbox/1pt/3pt/5pt table for frozen SAM vs FT variants | Table is unmatched-gain, threshold-naive, no negative clicks, no diversity, no seeds/CIs, no mixed-vs-box-only factorial |
| Huang et al., *Segment Anything Model for Medical Images?*, MedIA 2024, arXiv:2304.14660 | [M] | Prompt-type sensitivity of **frozen** SAM mapped | Frozen-model sensitivity ≠ fine-tuning-induced change |
| Kumar et al., *Fine-Tuning can Distort Pretrained Features*, ICLR 2022, arXiv:2202.10054 | [M] | FT trades OOD robustness for ID gain (classification) | Concept-level; no promptable/dense instance |
| WiSE-FT, Wortsman et al., CVPR 2022, arXiv:2109.01903 | [M] | Weight interpolation traces the gain–retention frontier | Used here as α-interpolation **baseline** in P177, and as frontier-plot format in the reporting panel |

## 2. The constructive PEFT-on-SAM lane (saturated; context only)

| Paper | Tag | Relevance |
|---|---|---|
| SAMed, Zhang & Liu, arXiv:2304.13785 | [M] | LoRA-on-SAM medical; recipe reference |
| Medical SAM Adapter, Wu et al. | [M] (anchors) | Adapter-PEFT lane crowded — Stage-1 kill-zone list |
| Conv-LoRA, Zhong et al., ICLR 2024, arXiv:2401.17868 | [V] | Advertises "preserves SAM's segmentation knowledge"; placement/inductive-bias engineering (P107's territory, not ours) |
| LoRA, Hu et al., ICLR 2022 | [M] (anchors; arXiv id to re-verify) | The adapted method itself |
| VeRA, Kopiczko et al., ICLR 2024, arXiv:2310.11454 | [V] | Frozen random low-rank directions + trained scaling ≈ LoRA. **Mandatory control arm** (Stage-3 cluster-2 ruling): trained-PEFT effects must beat random directions |
| Dutt et al., *PEFT for Medical Image Analysis: The Missed Opportunity*, MIDL 2024, arXiv:2305.08252 | [V] | 17 PEFT methods, 700+ runs, full-FT baselines swept across data volumes; killed C1-057 (crossover) — we do **not** re-claim crossover |

## 3. Forgetting science we confirm/extend rather than rediscover

| Paper | Tag | Role in PromptAmnesia |
|---|---|---|
| Biderman et al., *LoRA Learns Less and Forgets Less*, TMLR 2024, arXiv:2405.09673 | [V] | Learning–forgetting coupling (LLMs). Our coupling regression is **confirmatory** in the promptable regime (Stage-3 framing order); also predicts small-plasticity fine-tunes show small true forgetting — the engine of the P082 deflation branch |
| Soutif et al., *Empirical Analysis of Forgetting in Pre-trained Models with Incremental Low-Rank Updates*, CoLLAs / PMLR v274, 2025 | [V] | LoRA-rank vs plasticity/forgetting for ViTs |
| CoDyRA, arXiv:2412.01004 | [V] | Rank/placement vs plasticity–stability (vision) |
| Ramasesh et al., *Anatomy of Catastrophic Forgetting*, arXiv:2007.07400 | [M] | Forgetting concentrates in deeper layers (classification). P177 must difference: prompt cross-attention has no classification analogue (Stage-3 F2 divergence mechanism) |
| Davari et al., *Probing Representation Forgetting*, CVPR 2022, arXiv:2203.13381 | [M] | Representation- vs output-level forgetting probes |
| Lee et al., *Surgical Fine-Tuning*, ICLR 2023, arXiv:2210.11466 | [M] | Which block to tune depends on shift — constructive twin of the locus question |
| GEM, Lopez-Paz & Ranzato, NeurIPS 2017, arXiv:1706.08840 | [M] | BWT/FWT scalars — cited to show why we ship a **panel**, not a new scalar (P110 REJECT accepted) |
| Task arithmetic, Ilharco et al., ICLR 2023, arXiv:2212.04089 | [M] | Target-vs-control trade-off panels are routine — same reason |

## 4. Measurement hygiene (the gate's foundations)

| Paper | Tag | Role |
|---|---|---|
| Maier-Hein et al., *Metrics Reloaded*, Nature Methods 2024 | [M] | Threshold/operating-point pitfalls are canon; C1-082 applies them to forgetting claims — insider-known mechanism, unapplied gap |
| RClicks / BREPS line (Stage-3 sam_eval kills) | inherited | Killed naive click-simulation papers; forces our pre-registered simulator + dual-simulator sensitivity duplicate |
| Kornblith et al., CKA, ICML 2019, arXiv:1905.00414 | [M] | Drift covariate logging (P108 residue) |
| Bansal et al., *Revisiting Model Stitching*, NeurIPS 2021, arXiv:2106.07682 | [M] | Stitching-compatibility warning that mandates P177's trained-stitch controls |
| Merchant et al., *What Happens To BERT Embeddings During Fine-tuning?*, arXiv:2004.14448 | [M] | FT-drift anatomy (NLP), context for the covariate log |

## 5. Adjacent claims explicitly NOT made by this package

- **Calibration / IoU-head desync** — P031's paper (Laplace-LoRA arXiv:2308.13111 [V], BLoB, SWAG-LoRA
  arXiv:2405.03425 [V] genre). PromptAmnesia only *hands over* the diversity claim if the oracle
  decomposition resolves to ranking-loss.
- **Placement → error type** — P107 (He et al. arXiv:2110.04366 [M]; Conv-LoRA).
- **Data-size crossover** (killed: Dutt et al.), **PEFT replication honesty** (killed: Gu et al.),
  **random-LoRA-as-paper** (killed: VeRA), **retention scalar** (rejected: P110), **drift prediction**
  (rejected: P108) — all inherited verdicts accepted; residues appear only as controls/covariates/panels.

## 6. Scoop watch (standing queries during execution)

REVIEW JUDGMENT: the highest-risk scoop vectors, to be re-searched before the pre-registration freeze and
again before submission:

1. Any 2026 paper doing prompt-type-resolved retention **at matched gain** or a coverage/forgetting
   factorial (search: "prompt-specific forgetting SAM", "promptability retention fine-tuning").
2. Any audit applying threshold/variance envelopes to SAM-forgetting claims (P082 scoop).
3. Any causal module-splice/stitch study on promptable decoders (P177 scoop).
4. New CL-for-SAM releases with per-prompt retention tables (CA-SAM/EvoSAM successors) — would shrink the
   delta of §1 and must be differenced in the related-work section.

A scoop on (1) alone kills the flagship framing → fallback is the gate/deflation branch plus mechanism arm
(both harder to scoop, being audit- and causal-grade respectively).
