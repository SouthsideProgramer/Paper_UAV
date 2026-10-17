Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s666_t2_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 39.2 | 3.1 | 7.0 | 9.4 | 1480.1 | 3.1 | 3.1 | 3.0 | 4.0 | [7.4, 647.1] |
| naviloc | 5.1 | 4.6 | 8.9 | 10.7 | 30.4 | 0.0 | 0.0 | 0.0 | 0.0 | [10.3, 11.1] |
| naviloc_yaw | 5.1 | 4.6 | 8.9 | 10.6 | 27.7 | 0.0 | 0.0 | 0.0 | 0.0 | [10.3, 11.1] |
| naviloc_causal | 12.4 | 5.7 | 12.0 | 14.9 | 4127.3 | 0.9 | 0.9 | 0.3 | 32.0 | [14.5, 15.4] |
