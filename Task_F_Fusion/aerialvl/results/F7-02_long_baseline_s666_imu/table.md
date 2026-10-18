Config: `{"feats": "feats/ft/merged/baseline_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s666_imu", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 739.3 | 48.2 | 3404.1 | 5043.0 | 48.9 | 39.0 | 100.0 | [3193.2, 3588.9] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1580.1, 1892.1] |
| ekf_gated | 78.0 | 31.9 | 179.8 | 4652.6 | 26.4 | 10.2 | 7.5 | [144.8, 258.6] |
| pf_topk | 161.9 | 44.0 | 704.3 | 5666.7 | 44.6 | 27.5 | 36.2 | [589.4, 837.6] |
| mh_ekf | 76.6 | 31.2 | 247.5 | 3306.1 | 23.8 | 9.1 | 10.3 | [141.2, 441.7] |
| naviloc | 407.3 | 220.2 | 1430.4 | 3364.1 | 85.6 | 70.8 | 73.6 | [1259.0, 1671.5] |
| naviloc_yaw | 410.0 | 275.4 | 1334.9 | 3150.7 | 88.6 | 76.2 | 77.0 | [1209.5, 1494.9] |
