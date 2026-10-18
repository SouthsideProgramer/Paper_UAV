Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s666_t0_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 71.4 | 3.2 | 8.3 | 682.2 | 1779.4 | 6.2 | 6.2 | 6.0 | 8.0 | [9.6, 1279.9] |
| naviloc | 5.2 | 4.6 | 9.1 | 10.9 | 35.6 | 0.0 | 0.0 | 0.0 | 0.0 | [10.5, 11.1] |
| naviloc_yaw | 5.2 | 4.7 | 9.2 | 10.9 | 35.6 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 11.2] |
| naviloc_causal | 10.3 | 5.9 | 12.4 | 15.3 | 3877.1 | 0.8 | 0.8 | 0.2 | 24.0 | [14.9, 15.8] |
