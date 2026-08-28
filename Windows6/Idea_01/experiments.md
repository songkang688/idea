# Idea_01 experiments

## Epistemic labels

EXPECTED = hypothesized trend. ACTUAL = not measured in this repo (synthetic unit tests only).

## Killer (Day 1)

1. Run `src/amg_intensity_equiv.py` on synthetic piecewise-constant “CT” (runs CPU, seconds).
2. If even on synthetic blobs AMG-mock (threshold connected components) does not beat SLIC, the **implementation** is wrong — fix before real SAM.
3. On 50 MSD/TotalSegmentator slices: SAM ViT-B AMG vs k-means(k∈{8,16,32}) vs SLIC vs multi-Otsu vs GMM.
4. Metrics (all three, pre-registered): Hungarian mean IoU, ARI on pixel labels from mask maps, boundary-F.
5. Windows: abdomen (W/L 400/40), bone (2000/400), lung (−600/1500) or documented equivalents.
6. Counterfactual: (i) monotone remap of HU inside tissue, edges from Sobel frozen; (ii) permute high-frequency residual with HU mean preserved per superpixel.

## Full matrix

| Factor | Levels |
|--------|--------|
| Model | SAM ViT-B AMG; optional SAM2 |
| Window | 3 clinical |
| Cluster k | 8, 16, 32 |
| AMG points_per_side | 16, 32 |
| Intervention | none, intensity remap, texture shuffle |

## Stop

- **Kill** if SLIC ≥ k-means agreement with AMG on all windows, or texture shuffle ≈ intensity remap.
- **Pivot** if only one window shows clustering equivalence.
- **Continue** if H1+H2 hold on ≥2 windows and ≥2 AMG settings.

## Compute

1×12–24GB GPU for real SAM AMG on ~200 slices: hours, not days. Synthetic path: CPU minutes.
