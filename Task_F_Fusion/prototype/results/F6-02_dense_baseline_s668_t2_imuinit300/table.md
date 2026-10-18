Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s668_t2_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 16.7 | 4.9 | 11.0 | 14.2 | 904.4 | 1.7 | 1.7 | 1.6 | 3.0 | [12.5, 19.3] |
| naviloc | 90.0 | 59.6 | 195.2 | 259.4 | 1024.3 | 54.8 | 32.8 | 1.3 | 10.0 | [224.1, 332.7] |
| naviloc_yaw | 93.5 | 66.3 | 196.0 | 270.3 | 1050.4 | 58.8 | 34.4 | 1.3 | 9.0 | [230.4, 336.5] |
| naviloc_causal | 96.5 | 66.7 | 207.2 | 258.9 | 3490.9 | 57.6 | 36.8 | 1.3 | 36.0 | [234.3, 292.0] |
