Config: `{"feats": "feats/ft/merged/baseline_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 632.1 | 44.2 | 3094.5 | 4963.6 | 45.6 | 35.8 | 100.0 | [2948.4, 3169.0] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.7, 2034.9] |
| ekf_gated | 318.4 | 38.4 | 1776.2 | 5701.1 | 37.2 | 25.9 | 33.3 | [1423.1, 2141.8] |
| pf_topk | 526.1 | 257.7 | 1911.0 | 5811.5 | 78.1 | 64.7 | 82.2 | [1708.7, 2143.1] |
| mh_ekf | 114.0 | 32.9 | 473.8 | 5135.8 | 25.3 | 11.9 | 47.1 | [246.4, 895.2] |
| naviloc | 364.8 | 200.4 | 1294.0 | 3468.2 | 84.2 | 68.8 | 73.0 | [1132.9, 1418.2] |
| naviloc_yaw | 377.9 | 257.1 | 1172.2 | 3345.6 | 87.3 | 74.1 | 77.6 | [1042.3, 1278.7] |
