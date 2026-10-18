Config: `{"feats": "feats/fsra_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s667_init300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1257.6 | 823.9 | 3925.5 | 5003.3 | 66.3 | 62.8 | 100.0 | [3852.5, 3964.0] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [686.3, 834.0] |
| ekf_gated | 210.8 | 33.1 | 1196.9 | 1595.3 | 32.3 | 30.3 | 25.2 | [930.8, 1346.9] |
| pf_topk | 109.5 | 32.6 | 509.1 | 1773.0 | 24.7 | 18.6 | 24.8 | [389.4, 727.8] |
| mh_ekf | 60.1 | 27.7 | 242.0 | 1521.3 | 6.9 | 6.2 | 42.2 | [45.6, 484.4] |
