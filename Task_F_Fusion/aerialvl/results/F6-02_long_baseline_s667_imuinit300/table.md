Config: `{"feats": "feats/merged/baseline_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_baseline_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1714.7, 2048.8] |
| naviloc | 674.9 | 385.9 | 2318.6 | 4041.8 | 92.5 | 84.4 | 82.8 | [2089.5, 2585.6] |
| naviloc_yaw | 629.3 | 406.2 | 2095.5 | 3971.7 | 93.7 | 86.7 | 82.8 | [1875.2, 2271.0] |
| naviloc_causal | 727.6 | 385.6 | 2685.9 | 4258.3 | 86.3 | 77.5 | 94.8 | [2426.8, 3064.4] |
