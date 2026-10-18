Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s667_t0_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 75.0 | 5.1 | 13.6 | 54.7 | 3636.1 | 5.0 | 5.0 | 5.0 | 6.0 | [14.7, 1277.4] |
| naviloc | 106.6 | 65.2 | 227.7 | 355.9 | 1113.2 | 57.1 | 36.4 | 3.3 | 14.0 | [253.2, 519.2] |
| naviloc_yaw | 99.3 | 69.7 | 207.3 | 285.4 | 954.1 | 60.8 | 37.1 | 1.6 | 11.0 | [230.8, 365.3] |
| naviloc_causal | 105.1 | 67.2 | 227.9 | 312.0 | 3761.0 | 57.2 | 37.8 | 2.5 | 42.0 | [254.6, 415.7] |
