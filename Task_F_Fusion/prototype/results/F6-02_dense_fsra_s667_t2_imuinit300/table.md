Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s667_t2_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 79.8 | 5.2 | 14.7 | 559.2 | 1900.5 | 6.2 | 6.2 | 5.7 | 7.0 | [16.1, 1357.9] |
| naviloc | 89.3 | 59.6 | 192.7 | 251.8 | 1211.5 | 55.1 | 32.9 | 1.2 | 10.0 | [222.5, 303.3] |
| naviloc_yaw | 92.0 | 66.3 | 194.1 | 262.1 | 974.6 | 58.2 | 34.5 | 1.1 | 10.0 | [231.2, 303.4] |
| naviloc_causal | 95.0 | 66.6 | 204.2 | 256.2 | 3878.8 | 57.5 | 36.5 | 1.3 | 34.0 | [226.9, 300.7] |
