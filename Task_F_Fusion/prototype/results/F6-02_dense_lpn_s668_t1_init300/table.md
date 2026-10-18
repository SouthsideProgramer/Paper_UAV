Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s668_t1_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 16.3 | 2.9 | 5.8 | 7.2 | 1361.3 | 1.1 | 1.0 | 1.0 | 3.0 | [6.6, 8.4] |
| naviloc | 5.1 | 4.5 | 9.0 | 10.6 | 30.2 | 0.0 | 0.0 | 0.0 | 0.0 | [10.1, 10.9] |
| naviloc_yaw | 5.1 | 4.5 | 9.0 | 10.7 | 30.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.3, 10.9] |
| naviloc_causal | 10.3 | 6.0 | 12.2 | 15.0 | 3751.2 | 0.8 | 0.8 | 0.3 | 32.0 | [14.5, 15.4] |
