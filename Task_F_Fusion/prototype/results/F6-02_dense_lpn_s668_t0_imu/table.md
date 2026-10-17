Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s668_t0_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 5.1 | 4.3 | 9.2 | 11.7 | 55.1 | 0.0 | 0.0 | 0.0 | 0.0 | [10.8, 12.3] |
| naviloc | 100.2 | 62.2 | 217.5 | 334.5 | 1115.7 | 55.8 | 34.8 | 2.6 | 15.0 | [246.6, 457.6] |
| naviloc_yaw | 99.6 | 69.0 | 210.4 | 297.5 | 948.1 | 59.1 | 36.7 | 1.7 | 10.0 | [237.1, 389.5] |
| naviloc_causal | 99.9 | 63.4 | 218.8 | 281.6 | 3809.0 | 55.4 | 36.5 | 1.9 | 15.0 | [238.4, 356.8] |
