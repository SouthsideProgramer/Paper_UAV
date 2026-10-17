Config: `{"feats": "feats/ft/merged/baseline_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 739.3 | 48.2 | 3404.1 | 5043.0 | 48.9 | 39.0 | 100.0 | [3193.2, 3588.9] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.7, 2034.9] |
| ekf_gated | 309.2 | 38.9 | 1657.7 | 6010.1 | 40.8 | 27.6 | 32.8 | [1288.4, 2078.9] |
| pf_topk | 549.3 | 241.6 | 2045.2 | 7021.1 | 76.9 | 63.7 | 75.9 | [1812.1, 2333.2] |
| mh_ekf | 136.6 | 34.0 | 763.0 | 4544.6 | 31.0 | 15.4 | 46.6 | [373.0, 1098.7] |
| naviloc | 407.3 | 220.2 | 1430.4 | 3364.1 | 85.6 | 70.8 | 73.6 | [1259.0, 1671.5] |
| naviloc_yaw | 410.0 | 275.4 | 1334.9 | 3150.7 | 88.6 | 76.2 | 77.0 | [1209.5, 1494.9] |
