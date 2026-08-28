# Literature — B-0114: Prompts as Registers

Sections §10–§13. Full annotated bibliography with URLs and verification labels in
`references/references.md`. Verification labels used below: **[verified]** = URL fetched/confirmed by a
package- or pipeline-stage live search; **[in-record]** = surfaced by a pipeline agent's live search
this cycle and carried in the repo record.

---

## §10 The VPT / PEFT line

**Visual Prompt Tuning** (Jia et al., ECCV 2022, arXiv:2203.12119 — https://arxiv.org/abs/2203.12119)
**[verified]** introduced learnable prompt tokens prepended to a frozen ViT's sequence (VPT-shallow:
input only; VPT-deep: every layer) and showed they rival or beat full fine-tuning on the VTAB-1k suite.
Two facts from this paper are load-bearing for us:

1. **Fig. 11 (Prompt-Fixed ablation).** VPT's own ablation compares Prompt-Learned against
   **Prompt-Fixed** — prompts appended but frozen at random init — and Linear probing, concluding that
   *"updating prompt embeddings offers significant gains, while Prompt-Fixed yields comparable results
   w.r.t. Linear... the final performance of VPT is mainly contributed by the learned prompt embeddings
   instead of the enlarged sequence length."* This is why the original B-0114 pilot is struck
   (`PI_BINDING.md`, L audit Finding 1): **the frozen-token control was run in 2022, on classification.**
   Our arm (b) is that control re-run where it has never been run — dense prediction — plus arm (c),
   which Fig. 11 has no analogue of at all.
2. **VPT's dense-task story is thinner than its classification story.** The paper's segmentation
   experiment (ADE20K, SETR-style head) is a feasibility demonstration, not a mechanism study; no
   Prompt-Fixed analogue exists there.

Context for the seat, not targets: the broader PEFT families — LoRA (Hu et al., arXiv:2106.09685 —
https://arxiv.org/abs/2106.09685) **[verified]**, AdaptFormer (Chen et al., arXiv:2205.13535 —
https://arxiv.org/abs/2205.13535) **[in-record]** — modify weights, not sequence composition, so the
register question is specific to token-based PEFT. The ViT substrate is Dosovitskiy et al.
(arXiv:2010.11929 — https://arxiv.org/abs/2010.11929) **[verified]**.

## §11 The register / artifact line

**Vision Transformers Need Registers** (Darcet, Oquab, Mairal, Bojanowski, ICLR 2024,
arXiv:2309.16588 — https://arxiv.org/abs/2309.16588) **[verified]** established that large ViTs trained
without spare slots develop **high-norm artifact tokens** in low-information background patches; these
tokens hold global information, corrupt *spatial* feature maps, and degrade dense downstream use.
Appending dedicated **register tokens** during training absorbs this computation and cleans the maps.
Crucially for us: the damage and the cure are both **dense-task phenomena** — classification metrics
barely move. This is the entire reason the Fig. 11 result may fail to generalize to dense prediction,
and hence the reason this seat exists.

The backbone pair comes from the same line: **DINOv2** (Oquab et al., arXiv:2304.07193 —
https://arxiv.org/abs/2304.07193) **[verified]** is the canonical register-free artifact-bearing
backbone, and the **DINOv2-with-registers** checkpoints released with Darcet et al. (same data, same
recipe, registers added; distributed via the DINOv2 repo — https://github.com/facebookresearch/dinov2)
**[verified]** give us the cleanest register-free/register-equipped sibling pair in the ecosystem.

The mechanism-refinement wave this package must speak the language of:

- **Vision Transformers Don't Need Trained Registers** (Jiang, Dravid, Efros, Gandelsman, NeurIPS 2025
  Spotlight, arXiv:2506.08010 — https://arxiv.org/abs/2506.08010; code:
  https://github.com/nickjiang2378/test-time-registers) **[verified]**: a sparse set of *register
  neurons* creates the high-norm outliers; shifting their activations into an appended untrained token
  mimics registers **training-free**. This is the exact construction of our arm (c) — and its existence
  is double-edged: it supplies our instrument, and it is the strongest prior claim that register
  function is an *attention-geometry* effect reproducible without learning. Our contribution relative
  to it: they retrofit registers to clean features; nobody has asked whether **VPT was already doing
  this by accident**, or decomposed a PEFT method's *task gains* against it.
- **PH-Reg / Vision Transformers with Self-Distilled Registers** (Chen et al., NeurIPS 2025 Spotlight,
  arXiv:2505.21501 — https://arxiv.org/abs/2505.21501) **[verified]**: post-hoc registers via
  self-distillation; also documents that artifact behavior is not exhausted by *high*-norm tokens —
  the reason our signature battery never uses norms alone (§8, §21).
- **SINDER** (Wang et al., ECCV 2024, arXiv:2407.16826 — https://arxiv.org/abs/2407.16826)
  **[in-record]**: repairs DINOv2's singular defects; evidence that artifact direction is
  weight-determined — relevant to why frozen-random tokens (arm b) may fail to attract sink mass even
  when learned ones do.
- **A Unifying View of Attention Sinks** (arXiv:2606.08105 — https://arxiv.org/html/2606.08105v1)
  **[in-record]**: splits register/sink function into **NOP vs broadcast** mechanisms with concrete
  diagnostics on DINOv2-reg. L's audit makes these diagnostics **mandatory readout axes** — a 4-arm
  study without them "will look coarse at review time."
- **Do All Vision Transformers Need Registers?** (arXiv:2603.25803 —
  https://arxiv.org/html/2603.25803) **[in-record]**: reassesses register need across architectures;
  scopes which backbones our claims can generalize to.
- Attention sinks originate in the LLM literature: **StreamingLLM** (Xiao et al., arXiv:2309.17453 —
  https://arxiv.org/abs/2309.17453) **[verified]** — cited for the sink concept's provenance.
- **DINOv3** (Siméoni et al., arXiv:2508.10104 — https://arxiv.org/abs/2508.10104) **[verified]**
  ships register-equipped by default — the primary evidence for this seat's **obsolescence clock**
  (§26 of `roadmap.md`): the register-free backbone population decays every quarter.

## §12 The connection in print & the exact novelty residual

**The connection is already in print — this package never claims otherwise.** H's Stage-4 attack
established the boundary and it is adopted verbatim:

- **DA-VPT** (Ren et al., CVPR 2025, arXiv:2505.23694 — https://arxiv.org/abs/2505.23694; §Artifact
  Consideration) **[verified]** observes Darcet-style artifacts in VPT prompt attention maps, cites the
  register paper, calls registers *"analogous to learnable prompts,"* and explicitly leaves "the nature
  and impact of these artifacts on model performance" as "an intriguing avenue for future
  investigation." **DA-VPT opened the question; it did not answer it.** It is cited up front in every
  outward-facing document of this project (H's survival condition).
- **Test-time registers** (arXiv:2506.08010) shows register function is reproducible by pure attention
  manipulation — the "more specific competitor mechanism" H requires us to disaggregate, which is
  exactly what arm (c) vs arm (b) vs arm (e) does.

**The exact residual this project owns (nobody has printed any of these):**

1. A **quantified decomposition** of VPT's *dense-task* gains into learned-content / insertion /
   attention-geometry components. (VPT Fig. 11: classification only, two arms, no bias arm. DA-VPT:
   observation, no decomposition. 2506.08010: feature cleaning, not PEFT gain attribution.)
2. The **register-free vs register-equipped sibling contrast for a PEFT method** (H2). No paper
   conditions VPT behavior on backbone register regime.
3. **Register-signature characterization of learned prompts** with NOP/broadcast diagnostics on the
   same runs as the gains — connecting the sink-mechanism literature to PEFT empirically.
4. The **retrofit reading**: if arm (c) carries ≥50% of the gain, attention-bias injection is a
   training-free VPT substitute on dense tasks — constructive, not just analytic.

**Scoop-surface analysis (who could publish this first, from where):** (i) the test-time-registers
group extending 2506.08010 from feature quality to PEFT-gain attribution — the shortest path, one
figure away from our RQ1; (ii) the DA-VPT authors following their own "future investigation" sentence;
(iii) any registers-survey/ablation paper adding a VPT row to a busy table. Mitigation is calendar,
not cleverness: the killer grid is 24 cheap runs and the seat is bound to start this quarter (§26).

## §13 Mandatory citation set & freshness protocol

**Mandatory set (binding, from N exp_01 + H + L; every outward document cites all of these):**

| # | Paper | ID / URL | Role |
|---|---|---|---|
| 1 | VPT (Jia et al., ECCV 2022) | arXiv:2203.12119 — https://arxiv.org/abs/2203.12119 | method under study; Fig. 11 is the control we must reproduce |
| 2 | Vision Transformers Need Registers (Darcet et al., ICLR 2024) | arXiv:2309.16588 — https://arxiv.org/abs/2309.16588 | register phenomenon; dense-task damage |
| 3 | DA-VPT (Ren et al., CVPR 2025) | arXiv:2505.23694 — https://arxiv.org/abs/2505.23694 | the connection in print; cited up front (H condition) |
| 4 | Vision Transformers Don't Need Trained Registers (Jiang et al., NeurIPS 2025) | arXiv:2506.08010 — https://arxiv.org/abs/2506.08010 | arm-(c) construction; competitor mechanism |
| 5 | Do All Vision Transformers Need Registers? | arXiv:2603.25803 — https://arxiv.org/html/2603.25803 | generalization scope |
| 6 | A Unifying View of Attention Sinks | arXiv:2606.08105 — https://arxiv.org/html/2606.08105v1 | NOP/broadcast diagnostics (mandatory per L) |
| 7 | PH-Reg (Chen et al., NeurIPS 2025) | arXiv:2505.21501 — https://arxiv.org/abs/2505.21501 | low-norm caveat; supervised-pair patching |
| 8 | DINOv2 (Oquab et al.) | arXiv:2304.07193 — https://arxiv.org/abs/2304.07193 | register-free backbone |
| 9 | DINOv3 (Siméoni et al.) | arXiv:2508.10104 — https://arxiv.org/abs/2508.10104 | obsolescence-clock evidence |

Supporting set (datasets, substrate, adjacent PEFT) in `references/references.md`.

**Freshness protocol (binding):**

- **Re-search at proposal freeze and at experiment freeze** (minimum; the register micro-field moved
  4+ papers inside this pipeline's own run). Queries logged in the package repo: "VPT registers",
  "prompt tokens attention sink", "register tokens dense prediction PEFT", "attention bias visual
  prompt", each with date-restricted arXiv listing.
- **Kill trigger:** a printed register-mechanism paper **with dense-task token arms** (i.e., our RQ1 on
  a real dense benchmark) kills the seat (Stage-6 lock). An observation-only paper (another DA-VPT) is
  a citation obligation, not a kill.
- **exp_02's own stop:** any paper selling the norm map as per-pixel uncertainty triggers immediate
  re-search and PI escalation before the gate runs (N exp_02; fastest-moving check in the batch).
- Every citation added after this draft carries a verification label and fetch date in
  `references/references.md`.
