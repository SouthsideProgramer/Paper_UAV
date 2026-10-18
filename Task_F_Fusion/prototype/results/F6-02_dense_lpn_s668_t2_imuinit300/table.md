Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s668_t2_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 20.4 | 4.5 | 9.8 | 12.6 | 1364.9 | 1.3 | 1.3 | 1.3 | 3.0 | [11.2, 20.1] |
| naviloc | 88.8 | 58.7 | 188.7 | 256.9 | 947.5 | 54.6 | 32.9 | 1.7 | 12.0 | [219.0, 314.2] |
| naviloc_yaw | 90.9 | 65.0 | 193.1 | 248.8 | 1035.1 | 58.0 | 35.2 | 1.0 | 8.0 | [221.9, 289.5] |
| naviloc_causal | 93.8 | 66.5 | 208.1 | 254.6 | 2774.4 | 57.3 | 36.8 | 1.1 | 31.0 | [233.7, 281.7] |
