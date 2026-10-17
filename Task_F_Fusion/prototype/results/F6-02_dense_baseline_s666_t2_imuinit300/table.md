Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s666_t2_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 36.4 | 5.0 | 11.9 | 17.1 | 1526.0 | 2.4 | 2.4 | 2.3 | 4.0 | [13.9, 294.7] |
| naviloc | 89.9 | 60.1 | 194.4 | 255.6 | 987.5 | 55.1 | 33.3 | 1.5 | 11.0 | [221.9, 322.2] |
| naviloc_yaw | 93.1 | 66.5 | 196.7 | 263.9 | 988.9 | 58.6 | 35.3 | 1.2 | 9.0 | [230.1, 326.2] |
| naviloc_causal | 96.6 | 66.6 | 207.6 | 258.6 | 4127.0 | 57.9 | 36.6 | 1.2 | 35.0 | [233.1, 290.5] |
