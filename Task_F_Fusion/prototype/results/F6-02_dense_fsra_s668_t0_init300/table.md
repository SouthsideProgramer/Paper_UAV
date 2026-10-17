Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s668_t0_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 33.4 | 3.0 | 6.5 | 9.1 | 1176.6 | 3.1 | 3.1 | 3.0 | 5.0 | [7.2, 816.8] |
| naviloc | 5.0 | 4.5 | 8.8 | 10.3 | 43.8 | 0.0 | 0.0 | 0.0 | 0.0 | [10.1, 10.6] |
| naviloc_yaw | 5.0 | 4.5 | 8.9 | 10.4 | 43.8 | 0.0 | 0.0 | 0.0 | 0.0 | [10.1, 10.8] |
| naviloc_causal | 10.4 | 5.9 | 12.1 | 14.7 | 3783.8 | 0.9 | 0.7 | 0.2 | 23.0 | [14.3, 15.1] |
