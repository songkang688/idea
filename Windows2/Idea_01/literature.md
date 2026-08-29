# Literature — C-0306 (conformal coverage vs NMS + coverage-preserving suppression)

**Citation-integrity policy for this package.** No citation below is invented. Each entry carries a
verification tag:

- **[PIPELINE-VERIFIED]** — retrieved and checked inside this pipeline (Stage-2 D prior-work attack
  and/or Stage-4 K mandated freshness re-search), with the URL/DOI recorded by that agent.
- **[TEXTBOOK]** — standard, widely-cited work; identifiers are stable common knowledge.
- **[UNVERIFIED — confirm at proposal freeze]** — the work is believed real from memory, but the
  exact identifier/venue was NOT re-retrieved in this pipeline; do not cite in a submission until
  verified. No URLs are given for these, deliberately.

A mandatory freshness re-search (queries in §7 below) runs at proposal freeze AND experiment freeze —
the conformal-OD field prints on a months-scale clock (Stage-4 K: "third conformal-OD paper likely
within months").

---

## 1. Conformal prediction foundations

- Vovk, Gammerman, Shafer, **Algorithmic Learning in a Random World**, Springer, 2005. [TEXTBOOK]
  The source of conformal validity; our guarantee statement is the standard marginal one.
- Papadopoulos, Proedrou, Vovk, Gammerman, **Inductive Confidence Machines for Regression**,
  ECML 2002. [TEXTBOOK] Split/inductive conformal — the construction our conformal layer uses.
- Lei, G'Sell, Rinaldo, Tibshirani, Wasserman, **Distribution-Free Predictive Inference for
  Regression**, JASA 2018, arXiv:1604.04173. [TEXTBOOK] Finite-sample split-conformal quantile
  (⌈(n+1)(1−α)⌉ form implemented in `src/conformal_nms/conformal.py`).
- Angelopoulos, Bates, **A Gentle Introduction to Conformal Prediction and Distribution-Free
  Uncertainty Quantification**, arXiv:2107.07511, 2021. [TEXTBOOK] Standard reference for the
  prediction-set framing.
- Angelopoulos, Bates, Fisch, Lei, Schuster, **Conformal Risk Control**, ICLR 2024,
  arXiv:2208.02814. [TEXTBOOK] Generalizes coverage to monotone risks; the extension path in
  proposal §26.2; also the formal family SeqCRC builds on.
- Angelopoulos, Bates, Candès, Jordan, Lei, **Learn then Test: Calibrating Predictive Algorithms to
  Achieve Risk Control**, arXiv:2110.01052, 2021. [TEXTBOOK] Risk-control-by-testing alternative;
  relevant if reviewers ask for FWER-style guarantees over the (κ, r) grid.

**Relation to C-0306:** we take the split-conformal construction as given (KNOWN machinery); nothing
in this section is claimed as a contribution. Our contribution enters where the *pool* the guarantee
refers to is modified post-calibration.

## 2. Conformal / distribution-free object detection

- **Conformal Object Detection by Sequential Risk Control (SeqCRC)**, arXiv:2505.24038, 2025.
  https://arxiv.org/abs/2505.24038 [PIPELINE-VERIFIED — D retrieved; K re-verified v2 this cycle]
  Defines conformal OD, calibrates *after* NMS, explicitly treating NMS "as part of the OD model
  itself". Closest prior work. Its guarantee conditions on the post-NMS list: objects whose covering
  candidates were all suppressed are outside the event space. C-0306 measures that excluded mass,
  certifies when nominal is unachievable post-NMS (q̂ = +∞), and redesigns the suppression step.
  Baseline #1. Our pipeline C implements its calibrate-after-NMS *skeleton* only; the full SeqCRC
  construction is a method-leg deliverable and must be labeled as such in the paper.
- **Probabilistic Object Detection with Conformal Prediction**, arXiv:2605.07549, 2026.
  [PIPELINE-VERIFIED by D; K flags: "inherited from D, not re-retrieved this session" — re-verify at
  freeze] Scaled/unscaled CP for detection on KITTI/BDD/CODA; NMS upstream and untouched. Confirms
  the field's blind-spot-shaped hole from a second group.
- Earlier conformal-for-detection workshop line (box conformalization / conformal guarantees for
  detection in safety contexts, ca. 2022–2023, incl. a railway-signaling application):
  [UNVERIFIED — confirm at proposal freeze]. Believed-real works by de Grancey et al. (SAFECOMP
  workshop, ~2022) and Andéol et al. (COPA/PMLR, ~2023) conformalize box *coordinates/margins* on
  post-NMS detections. If confirmed, they strengthen the survey ("the whole line sits downstream of
  suppression") and do not overlap the blind-spot measurement, the certificate, or CPS. Until
  verified, they are cited nowhere else in this package.

## 3. NMS: failure modes, softenings, replacements

- Bodla, Singh, Chellappa, Davis, **Soft-NMS — Improving Object Detection With One Line of Code**,
  ICCV 2017, arXiv:1704.04503. [TEXTBOOK] Score decay instead of deletion; motivated by crowded-scene
  recall. Baseline arm and candidate CPS-internal operator (proposal §16.7). No guarantee of any kind.
- Hosang, Benenson, Schiele, **Learning Non-Maximum Suppression**, CVPR 2017, arXiv:1705.02950.
  [TEXTBOOK] Learned suppression optimizing AP; contrast: CPS is training-free with a deterministic
  coverage-transfer proof.
- **Do We Still Need NMS? IoU-Aware Calibration**, WACV 2024,
  https://doi.org/10.1109/wacv57701.2024.00478. [PIPELINE-VERIFIED — found by K in the mandated
  re-search; short title per K's record; confirm full author list/title string at freeze via the DOI]
  Replaces NMS with a calibration that "implicitly accounts for the likelihood of each detection
  being a duplicate". The "delete the step" pole of the design space and the K-MANDATED baseline:
  H2 is falsifiable against it on the coverage/set-size frontier. It optimizes confidence/AP, not
  conformal coverage, and its set-size economics under a coverage constraint are uncharacterized —
  exactly the comparison our frontier evaluator runs.
- Carion, Massa, Synnaeve, Usunier, Kirillov, Zagoruyko, **End-to-End Object Detection with
  Transformers (DETR)**, ECCV 2020, arXiv:2005.12872; Zhu et al., **Deformable DETR**, ICLR 2021,
  arXiv:2010.04159. [TEXTBOOK] One-to-one matching removes NMS; our suppression-free control arm
  (dissociates suppression-specific from detection-specific coverage loss).
- Crowded-scene NMS literature (KNOWN qualitatively; IDs to re-verify at freeze before citing):
  Adaptive-NMS (CVPR 2019) and set-prediction-per-proposal approaches (CrowdDet, CVPR 2020)
  [UNVERIFIED — confirm exact identifiers at proposal freeze]. This line documents recall loss in
  crowds as an AP phenomenon. K's concession stands: qualitatively old news — which is why C-0306's
  novelty must be carried by the conformal-coverage framing, the certificate, and the theorem, not by
  "NMS hurts crowds".

## 4. Uncertainty & calibration evaluation in OD

- **A Systematic Evaluation of Uncertainty Calibration in Pretrained Object Detectors**, IJCV 2024,
  https://link.springer.com/article/10.1007/s11263-024-02219-z. [PIPELINE-VERIFIED — K, in the
  C-0158 attack] Evaluates confidence calibration on raw pre-NMS vs post-processed outputs; warns
  post-processing "might bias the evaluation, especially when evaluating uncertainties". Closest
  measurement-side neighbour; it concerns *probability calibration*, not distribution-free *coverage
  of GT objects*, and contains no blind-spot quantity. Cite in paragraph one.
- Sibling idea W2-C-0158-mut (winner's-curse selection theory of post-NMS miscalibration) shares the
  substrate; see proposal §26.6 for the synergy and the shared deflation risk (M: a single
  "calibrate-before-NMS suffices" result deflates both).

## 5. The metric lemma

- Kosub, **A note on the triangle inequality for the Jaccard distance**, Pattern Recognition Letters,
  2019 (arXiv:1612.02696). [PIPELINE-VERIFIED — carried and used by the Stage-7 prototype; the lemma
  is also classical: Marczewski–Steinhaus 1958] d(A,B) = 1 − IoU(A,B) is a metric on measurable
  sets. This single inequality powers Theorem 1 (proposal §10): IoU(a,g) ≥ IoU(a,b) + IoU(b,g) − 1.
  Note it is set-theoretic — it holds for masks as well as boxes (extension §26.3) — but NOT
  automatically for rotated/3D IoU variants (open lemma, §26.5).

## 6. Datasets

- Lin et al., **Microsoft COCO: Common Objects in Context**, ECCV 2014, arXiv:1405.0312. [TEXTBOOK]
- Gupta, Dollár, Girshick, **LVIS: A Dataset for Large Vocabulary Instance Segmentation**, CVPR 2019,
  arXiv:1908.03195. [TEXTBOOK] Federated annotation protocol → the miss/blind decomposition needs the
  GT-quality sensitivity pass (proposal §19.6).
- Shao et al., **CrowdHuman: A Benchmark for Detecting Human in a Crowd**, arXiv:1805.00123, 2018.
  [TEXTBOOK] The load-bearing crowdedness axis; contains the aggressive-NMS operating regime.

## 7. The gap, and the freshness-search protocol

**Gap statement.** The conformal-OD line (§2) either conditions on the post-NMS list or leaves NMS
untouched upstream; the NMS line (§3) either softens/learns/deletes suppression for AP and confidence
purposes; the calibration-evaluation line (§4) warns that post-processing biases uncertainty but
measures probability calibration, not coverage. **No published work (as verified in-pipeline as of
Stage-4's re-search): (i) measures the fraction of GT objects whose conformal coverage NMS destroys;
(ii) states the post-NMS achievability certificate; (iii) constructs suppression with a provable
coverage-transfer guarantee.** That triple is this proposal.

**Mandatory re-search queries (run at proposal freeze + experiment freeze + quarterly; log results
into this file):**

1. "conformal prediction" + "object detection" (arXiv cs.CV/stat.ML, last 12 months)
2. "conformal" + "non-maximum suppression" / "NMS"
3. "coverage guarantee" + "detection" + "suppression"
4. "risk control" + "object detection"
5. citations of arXiv:2505.24038 (SeqCRC) and of the WACV 2024 IoU-aware-calibration DOI
6. "duplicate removal" + "calibration" + "detection" (WACV-2024 follow-ups)

**Kill trigger (binding, from Q):** a printed coverage-preserving suppression rule or a printed
blind-spot measurement kills the corresponding leg before execution starts.
