Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s668_t1_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 5.6 | 4.7 | 10.4 | 13.0 | 77.1 | 0.0 | 0.0 | 0.0 | 0.0 | [12.4, 13.8] |
| naviloc | 83.6 | 58.9 | 186.1 | 232.3 | 980.7 | 55.0 | 31.3 | 0.7 | 6.0 | [215.4, 257.2] |
| naviloc_yaw | 91.2 | 66.0 | 194.8 | 245.6 | 1088.7 | 58.9 | 33.9 | 1.1 | 12.0 | [222.8, 299.8] |
| naviloc_causal | 89.9 | 62.2 | 199.8 | 248.3 | 3187.9 | 56.1 | 35.4 | 0.7 | 12.0 | [230.1, 278.5] |
