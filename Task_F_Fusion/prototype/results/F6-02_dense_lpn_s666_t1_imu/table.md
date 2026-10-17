Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s666_t1_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 5.4 | 4.5 | 10.1 | 12.5 | 49.4 | 0.0 | 0.0 | 0.0 | 0.0 | [11.8, 13.4] |
| naviloc | 84.8 | 57.5 | 188.3 | 231.5 | 959.4 | 53.9 | 31.6 | 1.1 | 9.0 | [213.7, 259.7] |
| naviloc_yaw | 90.7 | 65.4 | 193.8 | 240.5 | 924.8 | 58.6 | 33.9 | 1.0 | 9.0 | [218.9, 290.3] |
| naviloc_causal | 90.2 | 61.9 | 201.6 | 248.7 | 2419.8 | 55.6 | 35.4 | 0.8 | 12.0 | [232.6, 275.6] |
