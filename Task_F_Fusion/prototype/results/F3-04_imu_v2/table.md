Config: `{"world": "real", "result_mat": "../../Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 300, "tag": "F3-04_imu_v2", "cfg": "{\"mh_lost_rule\":\"no_gate\",\"mh_reach\":true}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| mh_ekf | 10.9 | 8.6 | 21.2 | 27.4 | 120.3 | 0.8 | 0.0 | 0.0 | 0.0 | [25.2, 29.9] |
