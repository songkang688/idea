# Math (Idea_01)

Agreement: greedy/Hungarian matching of mask sets
\[
\mathrm{IoU}_{\mathrm{set}}(\mathcal{A},\mathcal{B})=\frac{1}{|\mathcal{A}|}\sum_{A\in\mathcal{A}}\max_{B\in\mathcal{B}}\mathrm{IoU}(A,B)
\]
(use Hungarian in the real experiment; prototype is greedy).

ARI on a pixel label map obtained by painting mask ids (conflicts → ignore or majority).

No trained loss. Clustering: k-means on scalar HU (or windowed 8-bit).
