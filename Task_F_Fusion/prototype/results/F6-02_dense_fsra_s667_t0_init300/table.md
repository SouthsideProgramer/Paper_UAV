Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s667_t0_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 74.6 | 3.2 | 7.8 | 851.7 | 1770.2 | 6.1 | 6.0 | 6.0 | 6.0 | [8.4, 1239.0] |
| naviloc | 5.1 | 4.6 | 9.1 | 10.6 | 42.6 | 0.0 | 0.0 | 0.0 | 0.0 | [10.4, 10.9] |
| naviloc_yaw | 5.1 | 4.6 | 9.1 | 10.6 | 43.7 | 0.0 | 0.0 | 0.0 | 0.0 | [10.3, 10.8] |
| naviloc_causal | 10.6 | 6.0 | 12.1 | 15.0 | 3761.1 | 1.0 | 0.8 | 0.2 | 26.0 | [14.6, 15.4] |
