Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s667_t2_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 22.1 | 4.8 | 11.3 | 16.1 | 1262.1 | 2.1 | 2.0 | 2.0 | 3.0 | [13.2, 29.7] |
| naviloc | 88.9 | 58.7 | 187.7 | 259.4 | 918.5 | 54.6 | 32.3 | 1.5 | 12.0 | [220.5, 333.3] |
| naviloc_yaw | 92.2 | 66.1 | 190.8 | 256.2 | 1056.4 | 58.1 | 34.6 | 1.2 | 10.0 | [222.4, 324.9] |
| naviloc_causal | 94.9 | 66.7 | 203.1 | 255.7 | 4132.3 | 57.9 | 36.5 | 1.3 | 34.0 | [228.4, 305.3] |
