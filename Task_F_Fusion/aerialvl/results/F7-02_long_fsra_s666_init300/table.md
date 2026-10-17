Config: `{"feats": "feats/ft/merged/fsra_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_fsra_s666_init300", "cfg": "", "calib": "val", "calib_from": "feats/ft/fsra_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 718.0 | 49.2 | 3392.6 | 4937.6 | 49.6 | 39.5 | 100.0 | [3323.1, 3499.1] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.6, 879.3] |
| ekf_gated | 198.6 | 28.7 | 1228.7 | 1856.0 | 22.5 | 18.1 | 21.3 | [999.5, 1363.2] |
| pf_topk | 112.5 | 31.7 | 551.4 | 1685.9 | 23.0 | 14.7 | 21.3 | [279.9, 1318.1] |
| mh_ekf | 63.3 | 26.8 | 110.4 | 1824.1 | 10.2 | 5.2 | 39.7 | [57.5, 360.6] |
| naviloc | 99.7 | 29.1 | 495.7 | 2244.6 | 13.3 | 8.3 | 8.0 | [66.1, 1148.7] |
| naviloc_yaw | 59.2 | 29.0 | 288.8 | 838.6 | 13.5 | 8.5 | 5.2 | [68.4, 485.0] |
