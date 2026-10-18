Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,ekf_topk_nn,pf_topk", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F2-10b_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 426.6 | 9.8 | 1848.0 | 3415.5 | 6972.1 | 31.4 | 20.0 | 12.5 | 100.0 | [3208.7, 3623.4] |
| dead_reckoning | 549.9 | 452.9 | 985.4 | 1240.5 | 4118.7 | 99.6 | 97.1 | 43.3 | 77.0 | [1055.6, 1562.0] |
| ekf_gated | 32.2 | 6.1 | 17.9 | 34.8 | 2016.5 | 4.4 | 3.8 | 1.8 | 6.0 | [21.1, 373.6] |
| ekf_topk_nn | 231.1 | 32.6 | 687.0 | 1219.9 | 4227.3 | 39.5 | 32.9 | 13.0 | 27.0 | [781.6, 1536.7] |
| pf_topk | 314.0 | 147.3 | 857.8 | 1181.0 | 2917.5 | 66.7 | 55.2 | 20.8 | 57.0 | [961.0, 1448.8] |
