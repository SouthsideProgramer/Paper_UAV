Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s667_t2_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 39.2 | 3.1 | 7.0 | 12.2 | 1271.7 | 4.0 | 4.0 | 4.0 | 4.0 | [7.4, 607.9] |
| naviloc | 5.1 | 4.6 | 9.1 | 10.7 | 27.9 | 0.0 | 0.0 | 0.0 | 0.0 | [10.4, 11.0] |
| naviloc_yaw | 5.1 | 4.6 | 9.1 | 10.8 | 25.9 | 0.0 | 0.0 | 0.0 | 0.0 | [10.5, 11.1] |
| naviloc_causal | 10.0 | 5.9 | 12.2 | 14.9 | 2399.2 | 0.9 | 0.8 | 0.3 | 28.0 | [14.4, 15.4] |
