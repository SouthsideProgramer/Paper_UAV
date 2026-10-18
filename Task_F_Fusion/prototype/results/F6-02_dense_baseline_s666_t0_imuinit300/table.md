Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s666_t0_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 71.1 | 4.9 | 13.9 | 680.9 | 1912.3 | 5.9 | 5.8 | 5.6 | 8.0 | [15.9, 1266.8] |
| naviloc | 100.9 | 63.1 | 222.4 | 321.8 | 1030.1 | 55.9 | 35.2 | 2.7 | 16.0 | [243.4, 442.4] |
| naviloc_yaw | 101.1 | 70.5 | 208.8 | 290.8 | 962.8 | 61.2 | 37.3 | 1.8 | 12.0 | [237.2, 381.3] |
| naviloc_causal | 103.2 | 67.2 | 226.2 | 298.4 | 3877.9 | 57.0 | 37.2 | 2.2 | 39.0 | [248.4, 389.4] |
