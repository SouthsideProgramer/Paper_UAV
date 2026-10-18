Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s667_t0_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 29.6 | 4.8 | 11.6 | 16.7 | 1367.2 | 2.3 | 2.1 | 2.0 | 2.0 | [13.3, 125.6] |
| naviloc | 104.9 | 65.8 | 226.2 | 351.1 | 1149.3 | 56.5 | 35.9 | 3.1 | 18.0 | [255.3, 500.6] |
| naviloc_yaw | 100.7 | 70.2 | 210.7 | 284.2 | 981.3 | 60.4 | 36.5 | 1.9 | 9.0 | [234.0, 403.2] |
| naviloc_causal | 102.0 | 66.2 | 224.1 | 292.9 | 1562.2 | 56.9 | 37.5 | 2.1 | 36.0 | [247.1, 365.1] |
