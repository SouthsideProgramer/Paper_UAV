Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s667_t0_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 23.2 | 3.2 | 6.8 | 9.4 | 1291.0 | 2.1 | 2.1 | 2.0 | 3.0 | [7.8, 118.4] |
| naviloc | 5.2 | 4.6 | 9.3 | 11.0 | 44.9 | 0.0 | 0.0 | 0.0 | 0.0 | [10.7, 11.4] |
| naviloc_yaw | 5.2 | 4.6 | 9.1 | 10.8 | 46.1 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 11.1] |
| naviloc_causal | 10.5 | 5.9 | 12.3 | 15.4 | 1784.5 | 1.1 | 0.9 | 0.2 | 27.0 | [14.8, 16.1] |
