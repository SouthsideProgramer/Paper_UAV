Config: `{"feats": "feats/merged/lpn_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s666_imu", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1244.3 | 829.2 | 3650.1 | 5108.1 | 72.1 | 66.8 | 100.0 | [3519.3, 3800.2] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1578.3, 1891.6] |
| ekf_gated | 206.7 | 39.1 | 1249.8 | 5293.3 | 38.6 | 23.2 | 24.7 | [896.1, 1568.4] |
| pf_topk | 194.5 | 55.0 | 872.0 | 3706.8 | 53.6 | 35.6 | 41.4 | [713.7, 1057.1] |
| mh_ekf | 103.0 | 34.9 | 344.5 | 3668.3 | 26.7 | 12.5 | 14.4 | [210.2, 712.3] |
