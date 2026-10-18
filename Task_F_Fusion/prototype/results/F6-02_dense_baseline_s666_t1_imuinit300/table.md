Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s666_t1_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 35.2 | 5.1 | 13.0 | 20.5 | 1513.2 | 3.6 | 3.5 | 3.0 | 4.0 | [14.6, 680.3] |
| naviloc | 85.1 | 62.1 | 193.2 | 233.1 | 986.2 | 56.8 | 31.7 | 0.8 | 8.0 | [217.6, 258.5] |
| naviloc_yaw | 91.1 | 68.2 | 196.3 | 242.6 | 961.2 | 59.9 | 33.7 | 1.1 | 9.0 | [222.0, 297.4] |
| naviloc_causal | 94.6 | 63.6 | 207.7 | 262.7 | 3187.9 | 57.1 | 35.8 | 1.0 | 36.0 | [238.4, 291.8] |
