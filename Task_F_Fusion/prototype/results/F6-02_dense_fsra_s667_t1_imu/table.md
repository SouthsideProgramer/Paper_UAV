Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s667_t1_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 6.7 | 4.8 | 10.9 | 13.7 | 424.4 | 0.4 | 0.3 | 0.0 | 0.0 | [13.0, 15.0] |
| naviloc | 86.2 | 60.7 | 189.8 | 229.5 | 1112.5 | 55.2 | 32.5 | 0.9 | 10.0 | [214.7, 266.9] |
| naviloc_yaw | 90.6 | 68.9 | 195.3 | 242.3 | 1020.4 | 59.7 | 34.5 | 0.8 | 9.0 | [223.4, 285.4] |
| naviloc_causal | 92.1 | 64.3 | 202.9 | 255.1 | 2011.9 | 56.8 | 36.1 | 0.9 | 12.0 | [232.2, 290.4] |
