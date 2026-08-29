# e0_smoke — harness output

Epistemic tag: **ACTUAL EXPERIMENTAL RESULT (smoke test)** when run with stub
backends on synthetic data — validates the decision logic ONLY; says nothing
about SAM. Real-SAM runs (backend=sam) produce E1 evidence.

| model :: stratum | n | Dice intact | CSG | persist. | trackΔ | NRF | sec.CSG | verdict |
|---|---|---|---|---|---|---|---|---|
| boxfill_stub :: high-contrast/high-solidity | 15 | 0.880 | 0.000 | 1.000 | -0.116 | 1.122 | 0.000 | **interpolator** |
| boxfill_stub :: high-contrast/low-solidity | 15 | 0.819 | 0.000 | 1.000 | -0.171 | 1.089 | 0.000 | **interpolator** |
| boxfill_stub :: low-contrast/high-solidity | 15 | 0.870 | 0.000 | 1.000 | -0.121 | 1.133 | 0.000 | **interpolator** |
| boxfill_stub :: low-contrast/low-solidity | 15 | 0.807 | 0.000 | 1.000 | -0.185 | 1.122 | 0.000 | **interpolator** |
| oracle_threshold_stub :: high-contrast/high-solidity | 15 | 1.000 | 0.414 | 0.586 | 0.157 | 0.988 | 0.134 | **seeing** |
| oracle_threshold_stub :: high-contrast/low-solidity | 15 | 1.000 | 0.405 | 0.595 | 0.153 | 0.893 | 0.206 | **seeing** |
| oracle_threshold_stub :: low-contrast/high-solidity | 15 | 0.746 | 0.177 | 0.664 | -0.199 | 1.324 | 0.136 | **seeing** |
| oracle_threshold_stub :: low-contrast/low-solidity | 15 | 0.769 | 0.153 | 0.784 | -0.127 | 1.169 | 0.199 | **seeing** |

## E0 checks

- boxfill_stub_all_interpolator: PASS
- oracle_stub_seeing_somewhere: PASS
- E0_PASS: PASS
