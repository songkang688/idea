# e0_smoke — 测试脚手架输出

认识论标签：在合成数据上使用存根后端运行时为 **ACTUAL EXPERIMENTAL RESULT（冒烟测试）** —— 仅用于验证决策逻辑；不代表任何关于 SAM 的结论。使用真实 SAM 运行（backend=sam）将产生 E1 的实证证据。

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

## E0 检查项

- boxfill_stub_all_interpolator: PASS
- oracle_stub_seeing_somewhere: PASS
- E0_PASS: PASS
