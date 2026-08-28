# Stage 2 — Pool-200 Index (Windows5)

**Pool:** `stage2_pool200.md` — **200 unique ideas** (exact count), 21 clusters, CanonicalIDs W5-001…W5-200.
**Derivation:** 130 (A+B unique pool) + 74 (Batch C survivors) + 12 (auditor revives) = 216 → 16 dedup merges → 200. Target band 195–205: hit.

## 1. Counts by cluster

| Cluster | Theme | Count | of which eval [E] | of which HR/HRHR |
|---|---|---|---|---|
| P1 | Auto-labeling ecology & ground-truth contamination | 9 | 0 | 3 |
| P2 | Benchmark validity & evaluation instruments | 13 | 13 | 1 |
| P3 | Meta-science, replication & attribution | 7 | 7 | 0 |
| P4 | PEFT & fine-tuning recipe science | 17 | 0 | 2 |
| P5 | Forgetting, retention & update geometry | 9 | 1 | 2 |
| P6 | Domain shift, TTA & continual deployment | 11 | 0 | 1 |
| P7 | Language–vision grounding & dense-VLM failure modes | 19 | 1 | 4 |
| P8 | Interactive segmentation & the prompt interface | 6 | 3 | 0 |
| P9 | Transparency, camouflage & layered scenes | 6 | 0 | 4 |
| P10 | Amorphous matter full stack: smoke, fire, wildfire | 12 | 0 | 4 |
| P11 | Small structures & token-lattice artifacts | 11 | 1 | 1 |
| P12 | Uncertainty, calibration & confidence validity | 7 | 0 | 0 |
| P13 | Representation & pretraining science of VFMs | 13 | 0 | 1 |
| P14 | Composed pipelines & preprocessing skepticism | 7 | 0 | 0 |
| P15 | Medical FM capabilities & deployment safety | 16 | 1 | 4 |
| P16 | Synthetic data & derived supervision resources | 7 | 0 | 1 |
| P17 | Detection–segmentation interface & instance science | 6 | 0 | 0 |
| P18 | Boundary error science & loss metrology | 9 | 2 | 0 |
| P19 | Multi-rater disagreement & ambiguity science | 5 | 0 | 2 |
| P20 | Prompt-learning pathologies | 5 | 0 | 1 |
| P21 | Label-efficient learning validity | 5 | 1 | 0 |
| **Total** |  | **200** | **30** | **31** |

Auditor balance check (audit §6.1): core evaluation-genre = 30/200 = 15.0% (≤20% cap satisfied; broadest classification incl. borderline audits ≈ 38/200 = 19%). Constructive/method entries ≈ 38 (19%), up from ~10% pre-audit. HR/HRHR carriers = 31 (15%), including 5 data/partnership-gated bets (B-0177, A-0124, MERGE-16, B-0162, B-0318) per the auditor's reserved-slot rule.

## 2. Merge log

### 2a. Inherited from A+B merge pass (13 unchanged)

MERGE-01 (A-0029+B-0019) · MERGE-02 (A-0185+B-0241) · MERGE-03 (A-0006+B-0226) · MERGE-05 (A-0296+B-0064) · MERGE-06 (A-0303+B-0057) · MERGE-07 (A-0076+B-0248) · MERGE-08 (A-0058+B-0260) · MERGE-10 (A-0141+B-0126) · MERGE-11 (A-0250+B-0024) · MERGE-12 (A-0285+B-0190) · MERGE-13 (A-0021+B-0136) · MERGE-16 (A-0142+B-0159) · MERGE-17 (B-0089+B-0193). Rationales: `stage2_AB_duplicates.md`.

### 2b. This pass — 16 dedup actions (Batch C + revive integration)

| # | Action | Constituents | Rationale |
|---|---|---|---|
| 1 | MERGE-04 ‡ext | A-0161 + B-0129 + **C-0264** | C-0264's layer-of-loss tokenization audit is the same information-absent-vs-decoder-limited question; one probe+intervention program. |
| 2 | MERGE-09 ‡ext | A-0267 + B-0329 + **C-0310** | C-0310's soft-label error-structure transfer is the distillation channel of the same teacher-error inheritance claim. |
| 3 | MERGE-14 ‡ext | A-0166 + B-0037 + **C-0245** | C-0245's tolerance-band metrics consume exactly the tolerance estimates MERGE-14 produces; one tolerance program. |
| 4 | MERGE-15 ‡ext | A-0091 + B-0082 + **C-0321** | C-0321 is the identical 3-rater re-annotation noise-floor pilot, independently generated; folds in as the entry study. |
| 5 | MERGE-18 ‡ext | B-0120 + B-0337 + **C-0253** | C-0253's TTA-disagreement-vs-human-disagreement is the third 'free uncertainty source' under the same coverage-test methodology. |
| 6 | MERGE-19 new | B-0270 + C-0020 | Same input-stem hypothesis for cross-modality transfer (interface-vs-semantics split = ceiling-effect design). |
| 7 | MERGE-20 new | A-0078 + C-0034 | Same feature-loss-vs-readout-loss decomposition of forgetting via re-probing frozen features. |
| 8 | MERGE-21 new | A-0089 + C-0040 | Same suppression-not-erasure claim: tiny re-exposure/rewinding sets restore 'forgotten' performance cheaply. |
| 9 | MERGE-22 new | A-0031 + C-0067 | Same prompt-paraphrase-variance-exceeds-SOTA-gaps claim with the same prompt-resampled leaderboard repair. |
| 10 | MERGE-23 new | A-0100 + C-0149 | One laterality program: pipeline-level flip-TTA harm (A) + capability-level left/right probe (C); same stimuli and stake. |
| 11 | MERGE-24 new | B-0081 (revive) + C-0177 | Revive R3 merged with Batch C's top survivor: identical machinery regressing clinical-measurement error on mask metrics. |
| 12 | MERGE-25 new | B-0305 + C-0261 | Two phase-axes (input-size periodicity, translation grid-phase) of one patch-lattice aliasing phenomenon. |
| 13 | MERGE-26 new | A-0170 + C-0276 | Same recovered-vs-hallucinated-detail adjudication with the same synthetic-truth instrument (INR decoders / feature upsamplers). |
| 14 | MERGE-27 new | A-0093 + C-0300 | Same nnU-Net-dominance attribution via matched-budget component swaps (3D context / augmentation / preprocessing stack). |
| 15 | MERGE-28 new | B-0012 + C-0328 | One near-duplicate detection pass serves the general contamination audit and the few-shot inflation claim. |
| 16 | MERGE-29 new | A-0226 + C-0340 | One tuned-baseline, compute-matched (incl. HPO), multi-seed replication program; C generalizes A's genre study. |

Near-merges reviewed and **kept separate** (different claims, shared infrastructure — co-schedule): A-0096↔C-0016 (VFM-vs-specialist sensitivity law vs PEFT-vs-FT size gap); C-0061↔B-0132 (CLIP pooling leakage vs VLM-stack layer decay); A-0187↔C-0076 (general negation fusion failure vs report-supervision negation); C-0094↔B-0114 (prompt-learning vs PEFT seed metrology); C-0339↔MERGE-14 (perturbation vs multi-rater tolerance); A-0103↔C-0233 (model-UQ→rater vs rater→model-error directions); C-0132↔C-0137, C-0204↔C-0273 (kept separate by the C reviewer); MERGE-26↔C-0214 logged as a productive conflict (sub-pixel info is real vs hallucinated).

## 3. Revive log (auditor §5 — all 12 executed)

| R# | ID | Disposition | Pool ID | Cluster |
|---|---|---|---|---|
| R1 | IDEA-A-0278 | Revived as standalone (constructive HRHR; no survivor duplicates it) | W5-170 | P16 |
| R2 | IDEA-B-0177 | Revived as standalone, **partnership-gated** with the auditor's go/no-go (public restain-registered pilot first) | W5-163 | P15 |
| R3 | IDEA-B-0081 | Revived and **merged with survivor C-0177** (same clinical-measurement-validity program) → MERGE-24 | W5-159 | P15 |
| R4 | IDEA-A-0052 | Revived at auditor's reduced scope (~120 runs), grid shared with B-0114 | W5-046 | P4 |
| R5 | IDEA-B-0300 | Revived, sequenced after B-0129/B-0132 grouping-probe infrastructure | W5-140 | P13 |
| R6 | IDEA-B-0286 | Revived; shares infrastructure with MERGE-07/MERGE-08 retention geometry | W5-055 | P5 |
| R7 | IDEA-A-0124 | Revived (data-gated HRHR); curation amortized with B-0017/B-0110/MERGE-02 negative-set work | W5-109 | P10 |
| R8 | IDEA-A-0328 | Revived; prompt-log collection shared with MERGE-17 (one user study, three papers) | W5-091 | P8 |
| R9 | IDEA-B-0033 | Revived; frequency-regression machinery shared with A-0033/A-0049; run alongside B-0124 | W5-085 | P7 |
| R10 | IDEA-A-0096 | Revived; co-scheduled (not merged) with C-0016 on one size-stratified sensitivity harness | W5-162 | P15 |
| R11 | IDEA-A-0301 | Revived; the pool's only continual-deployment protocol idea; synthetic-cycle control mandatory | W5-066 | P6 |
| R12 | IDEA-B-0098 | Revived with the auditor's explicit-science condition (attribution + held-out-model/domain generalization) | W5-127 | P12 |

## 4. The 200 CanonicalIDs

- **P1** (9): W5-001(MERGE-01) · W5-002(A-0007) · W5-003(MERGE-09) · W5-004(B-0001) · W5-005(B-0191) · W5-006(B-0320) · W5-007(B-0009) · W5-008(B-0006) · W5-009(B-0053)
- **P2** (13): W5-010(MERGE-15) · W5-011(MERGE-14) · W5-012(A-0340) · W5-013(A-0336) · W5-014(A-0337) · W5-015(MERGE-28) · W5-016(B-0017) · W5-017(B-0108) · W5-018(B-0110) · W5-019(B-0294) · W5-020(A-0254) · W5-021(A-0246) · W5-022(C-0339)
- **P3** (7): W5-023(A-0245) · W5-024(MERGE-29) · W5-025(A-0242) · W5-026(MERGE-11) · W5-027(A-0261) · W5-028(C-0094) · W5-029(C-0315)
- **P4** (17): W5-030(A-0055) · W5-031(A-0067) · W5-032(A-0072) · W5-033(B-0114) · W5-034(B-0253) · W5-035(B-0257) · W5-036(B-0269) · W5-037(MERGE-19) · W5-038(B-0272) · W5-039(B-0306) · W5-040(B-0315) · W5-041(A-0238) · W5-042(C-0001) · W5-043(C-0011) · W5-044(C-0016) · W5-045(C-0023) · W5-046(A-0052)
- **P5** (9): W5-047(MERGE-07) · W5-048(MERGE-20) · W5-049(MERGE-21) · W5-050(MERGE-08) · W5-051(B-0251) · W5-052(C-0050) · W5-053(C-0056) · W5-054(C-0057) · W5-055(B-0286)
- **P6** (11): W5-056(MERGE-05) · W5-057(MERGE-06) · W5-058(B-0054) · W5-059(B-0072) · W5-060(B-0078) · W5-061(B-0279) · W5-062(A-0239) · W5-063(B-0304) · W5-064(A-0305) · W5-065(C-0325) · W5-066(A-0301)
- **P7** (19): W5-067(A-0041) · W5-068(A-0187) · W5-069(A-0183) · W5-070(MERGE-02) · W5-071(A-0199) · W5-072(A-0181) · W5-073(B-0124) · W5-074(MERGE-22) · W5-075(A-0033) · W5-076(A-0049) · W5-077(B-0132) · W5-078(B-0174) · W5-079(B-0185) · W5-080(C-0061) · W5-081(C-0072) · W5-082(C-0076) · W5-083(C-0078) · W5-084(C-0329) · W5-085(B-0033)
- **P8** (6): W5-086(MERGE-17) · W5-087(B-0083) · W5-088(B-0104) · W5-089(B-0128) · W5-090(B-0282) · W5-091(A-0328)
- **P9** (6): W5-092(MERGE-10) · W5-093(MERGE-16) · W5-094(B-0075) · W5-095(B-0162) · W5-096(A-0157) · W5-097(A-0154)
- **P10** (12): W5-098(A-0121) · W5-099(A-0122) · W5-100(MERGE-03) · W5-101(A-0128) · W5-102(A-0126) · W5-103(A-0123) · W5-104(A-0125) · W5-105(B-0318) · W5-106(B-0055) · W5-107(A-0319) · W5-108(B-0219) · W5-109(A-0124)
- **P11** (11): W5-110(MERGE-04) · W5-111(A-0003) · W5-112(A-0313) · W5-113(B-0288) · W5-114(A-0176) · W5-115(A-0174) · W5-116(B-0122) · W5-117(MERGE-25) · W5-118(MERGE-26) · W5-119(C-0269) · W5-120(C-0287)
- **P12** (7): W5-121(A-0103) · W5-122(MERGE-18) · W5-123(B-0084) · W5-124(A-0097) · W5-125(B-0310) · W5-126(A-0280) · W5-127(B-0098)
- **P13** (13): W5-128(A-0001) · W5-129(A-0013) · W5-130(MERGE-13) · W5-131(A-0202) · W5-132(A-0203) · W5-133(A-0266) · W5-134(A-0211) · W5-135(A-0223) · W5-136(A-0225) · W5-137(A-0207) · W5-138(C-0289) · W5-139(C-0301) · W5-140(B-0300)
- **P14** (7): W5-141(B-0217) · W5-142(B-0223) · W5-143(B-0233) · W5-144(B-0331) · W5-145(B-0338) · W5-146(B-0285) · W5-147(C-0273)
- **P15** (16): W5-148(A-0118) · W5-149(MERGE-27) · W5-150(MERGE-23) · W5-151(B-0156) · W5-152(B-0182) · W5-153(B-0184) · W5-154(C-0150) · W5-155(C-0151) · W5-156(C-0162) · W5-157(C-0164) · W5-158(C-0173) · W5-159(MERGE-24) · W5-160(C-0326) · W5-161(C-0332) · W5-162(A-0096) · W5-163(B-0177)
- **P16** (7): W5-164(B-0186) · W5-165(MERGE-12) · W5-166(B-0189) · W5-167(B-0200) · W5-168(A-0283) · W5-169(A-0287) · W5-170(A-0278)
- **P17** (6): W5-171(C-0179) · W5-172(C-0187) · W5-173(C-0190) · W5-174(C-0192) · W5-175(C-0196) · W5-176(C-0204)
- **P18** (9): W5-177(C-0205) · W5-178(C-0206) · W5-179(C-0208) · W5-180(C-0210) · W5-181(C-0212) · W5-182(C-0214) · W5-183(C-0218) · W5-184(C-0290) · W5-185(C-0311)
- **P19** (5): W5-186(C-0233) · W5-187(C-0234) · W5-188(C-0235) · W5-189(C-0249) · W5-190(C-0124)
- **P20** (5): W5-191(C-0091) · W5-192(C-0095) · W5-193(C-0101) · W5-194(C-0113) · W5-195(C-0316)
- **P21** (5): W5-196(C-0121) · W5-197(C-0127) · W5-198(C-0132) · W5-199(C-0137) · W5-200(C-0143)

*End of index.*
