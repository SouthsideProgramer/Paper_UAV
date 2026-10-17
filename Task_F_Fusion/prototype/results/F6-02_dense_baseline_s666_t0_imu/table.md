Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s666_t0_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 5.6 | 4.7 | 10.4 | 13.1 | 65.2 | 0.0 | 0.0 | 0.0 | 0.0 | [12.3, 14.1] |
| naviloc | 100.9 | 63.1 | 222.4 | 321.8 | 1030.1 | 55.9 | 35.2 | 2.7 | 16.0 | [243.4, 442.4] |
| naviloc_yaw | 101.1 | 70.5 | 208.8 | 290.8 | 962.8 | 61.2 | 37.3 | 1.8 | 12.0 | [237.2, 381.3] |
| naviloc_causal | 101.0 | 65.5 | 222.0 | 286.9 | 3877.9 | 56.4 | 36.5 | 2.0 | 26.0 | [241.6, 375.1] |
