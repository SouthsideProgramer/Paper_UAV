Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s668_t0_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 5.7 | 4.6 | 10.4 | 13.3 | 152.3 | 0.1 | 0.1 | 0.0 | 0.0 | [12.3, 14.1] |
| naviloc | 103.8 | 63.9 | 222.9 | 339.2 | 1198.3 | 56.3 | 35.8 | 3.1 | 16.0 | [255.1, 488.5] |
| naviloc_yaw | 99.3 | 70.4 | 205.8 | 278.1 | 992.3 | 60.6 | 36.5 | 1.6 | 11.0 | [228.8, 360.4] |
| naviloc_causal | 100.7 | 64.1 | 221.3 | 292.6 | 2138.8 | 55.8 | 36.5 | 2.1 | 20.0 | [244.3, 374.8] |
