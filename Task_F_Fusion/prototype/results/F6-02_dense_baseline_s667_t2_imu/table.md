Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s667_t2_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 6.0 | 4.9 | 11.2 | 14.4 | 55.1 | 0.0 | 0.0 | 0.0 | 0.0 | [13.6, 15.1] |
| naviloc | 90.9 | 62.2 | 189.7 | 262.7 | 971.1 | 55.7 | 33.2 | 1.6 | 10.0 | [229.2, 319.0] |
| naviloc_yaw | 91.5 | 66.4 | 190.3 | 255.3 | 946.1 | 58.3 | 35.0 | 1.1 | 11.0 | [225.8, 309.4] |
| naviloc_causal | 91.7 | 65.7 | 201.1 | 249.5 | 2399.7 | 57.0 | 36.0 | 1.1 | 14.0 | [225.2, 277.6] |
