Config: `{"feats": "feats/ft/merged/lpn_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s666_init300", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 620.7 | 43.3 | 3237.3 | 4979.8 | 44.0 | 33.7 | 98.3 | [3015.6, 3411.0] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.6, 879.3] |
| ekf_gated | 162.4 | 31.8 | 1042.6 | 1536.9 | 23.2 | 17.2 | 17.2 | [772.9, 1262.4] |
| pf_topk | 93.7 | 30.9 | 554.4 | 1455.4 | 18.1 | 11.3 | 22.4 | [247.5, 742.0] |
| mh_ekf | 64.1 | 28.7 | 76.5 | 1846.6 | 9.2 | 4.8 | 41.4 | [57.4, 580.0] |
| naviloc | 56.4 | 29.9 | 155.5 | 1476.8 | 10.9 | 5.5 | 1.7 | [56.7, 278.9] |
| naviloc_yaw | 51.1 | 30.0 | 124.3 | 994.6 | 11.3 | 5.4 | 1.7 | [57.4, 248.2] |
