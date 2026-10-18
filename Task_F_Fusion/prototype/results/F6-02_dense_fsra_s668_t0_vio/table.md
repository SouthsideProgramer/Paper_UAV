Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s668_t0_vio", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 3.3 | 2.9 | 5.9 | 7.2 | 48.9 | 0.0 | 0.0 | 0.0 | 0.0 | [6.7, 7.5] |
| naviloc | 5.0 | 4.5 | 8.8 | 10.3 | 43.8 | 0.0 | 0.0 | 0.0 | 0.0 | [10.1, 10.6] |
| naviloc_yaw | 5.0 | 4.5 | 8.9 | 10.4 | 43.8 | 0.0 | 0.0 | 0.0 | 0.0 | [10.1, 10.8] |
| naviloc_causal | 8.1 | 5.9 | 11.9 | 14.3 | 3783.8 | 0.2 | 0.1 | 0.1 | 7.0 | [13.9, 14.8] |
