Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s668_t2_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 49.1 | 4.9 | 12.7 | 23.8 | 1617.7 | 4.3 | 4.3 | 4.3 | 5.0 | [14.4, 930.3] |
| naviloc | 90.2 | 60.6 | 189.6 | 253.4 | 1163.6 | 55.4 | 32.5 | 1.5 | 11.0 | [221.8, 327.1] |
| naviloc_yaw | 93.8 | 67.5 | 196.5 | 263.6 | 961.9 | 58.8 | 35.6 | 1.4 | 9.0 | [227.8, 338.0] |
| naviloc_causal | 95.6 | 67.3 | 206.7 | 260.6 | 3208.1 | 57.9 | 36.5 | 1.3 | 35.0 | [232.0, 298.4] |
