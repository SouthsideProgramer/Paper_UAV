Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s668_t2_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 52.5 | 3.2 | 7.1 | 395.8 | 1432.9 | 5.0 | 5.0 | 5.0 | 5.0 | [7.8, 945.4] |
| naviloc | 5.0 | 4.5 | 8.9 | 10.6 | 32.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.2, 11.1] |
| naviloc_yaw | 5.0 | 4.5 | 9.0 | 10.8 | 32.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.4, 11.2] |
| naviloc_causal | 10.9 | 5.8 | 12.1 | 15.0 | 3208.2 | 0.8 | 0.8 | 0.3 | 30.0 | [14.5, 15.5] |
