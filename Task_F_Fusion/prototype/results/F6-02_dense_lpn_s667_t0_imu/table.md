Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s667_t0_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 5.9 | 4.8 | 10.6 | 13.9 | 158.5 | 0.2 | 0.1 | 0.0 | 0.0 | [12.7, 15.0] |
| naviloc | 104.9 | 65.8 | 226.2 | 351.1 | 1149.3 | 56.5 | 35.9 | 3.1 | 18.0 | [255.3, 500.6] |
| naviloc_yaw | 100.7 | 70.2 | 210.7 | 284.2 | 981.3 | 60.4 | 36.5 | 1.9 | 9.0 | [234.0, 403.2] |
| naviloc_causal | 99.7 | 64.7 | 219.9 | 282.6 | 1562.2 | 56.3 | 36.8 | 1.9 | 20.0 | [240.8, 349.1] |
