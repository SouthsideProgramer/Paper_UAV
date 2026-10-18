Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s667_t2_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 26.9 | 3.0 | 6.3 | 8.4 | 1262.1 | 2.9 | 2.9 | 2.9 | 3.0 | [6.9, 571.6] |
| naviloc | 5.2 | 4.7 | 9.2 | 10.9 | 45.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.4, 11.3] |
| naviloc_yaw | 5.2 | 4.7 | 9.3 | 11.1 | 45.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 11.6] |
| naviloc_causal | 9.9 | 5.9 | 12.1 | 14.8 | 4132.3 | 0.8 | 0.7 | 0.2 | 28.0 | [14.3, 15.3] |
