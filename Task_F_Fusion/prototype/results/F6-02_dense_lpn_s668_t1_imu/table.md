Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s668_t1_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 5.2 | 4.4 | 9.6 | 11.8 | 47.0 | 0.0 | 0.0 | 0.0 | 0.0 | [11.3, 12.6] |
| naviloc | 84.6 | 59.7 | 191.1 | 230.4 | 940.7 | 55.0 | 32.4 | 0.8 | 7.0 | [215.5, 253.5] |
| naviloc_yaw | 92.3 | 66.4 | 197.3 | 248.4 | 962.0 | 58.7 | 34.5 | 1.1 | 11.0 | [224.6, 306.6] |
| naviloc_causal | 89.4 | 62.2 | 197.4 | 244.6 | 3750.8 | 56.1 | 34.9 | 0.7 | 12.0 | [227.7, 270.0] |
