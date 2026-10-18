Config: `{"feats": "feats/fsra_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s667_vio", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1257.6 | 823.9 | 3925.5 | 5003.3 | 66.3 | 62.8 | 100.0 | [3852.5, 3964.0] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [96.8, 119.0] |
| ekf_gated | 35.0 | 27.8 | 88.3 | 278.4 | 5.8 | 4.2 | 0.0 | [46.6, 123.9] |
| pf_topk | 26.5 | 27.2 | 36.5 | 81.5 | 0.3 | 0.0 | 0.0 | [35.9, 37.2] |
| mh_ekf | 26.3 | 26.9 | 36.6 | 86.2 | 0.1 | 0.0 | 0.0 | [36.0, 37.1] |
