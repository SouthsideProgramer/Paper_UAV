Config: `{"world": "real", "result_mat": "../../Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 300, "tag": "F3-04_imu_v0", "cfg": "{\"mh_lost_rule\":\"best_child\",\"mh_reach\":false}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| mh_ekf | 32.0 | 8.6 | 21.6 | 28.4 | 4923.3 | 1.6 | 0.7 | 0.6 | 13.0 | [26.1, 31.2] |
