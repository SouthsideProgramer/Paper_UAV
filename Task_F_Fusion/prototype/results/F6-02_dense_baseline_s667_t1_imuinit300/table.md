Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s667_t1_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 15.2 | 5.1 | 11.9 | 15.8 | 916.2 | 1.4 | 1.3 | 1.0 | 2.0 | [14.1, 19.2] |
| naviloc | 84.9 | 59.9 | 189.0 | 232.3 | 1020.9 | 55.1 | 32.4 | 0.7 | 10.0 | [218.0, 253.4] |
| naviloc_yaw | 90.3 | 67.7 | 193.7 | 240.7 | 939.0 | 59.3 | 34.3 | 0.8 | 9.0 | [223.2, 275.7] |
| naviloc_causal | 93.5 | 64.8 | 204.7 | 259.6 | 1267.1 | 57.1 | 35.9 | 1.0 | 36.0 | [242.3, 297.8] |
