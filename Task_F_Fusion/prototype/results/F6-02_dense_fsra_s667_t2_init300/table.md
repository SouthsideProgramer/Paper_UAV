Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s667_t2_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 74.2 | 3.1 | 7.3 | 558.9 | 1446.4 | 6.2 | 6.2 | 6.0 | 7.0 | [7.5, 1298.3] |
| naviloc | 5.1 | 4.6 | 9.1 | 10.9 | 26.1 | 0.0 | 0.0 | 0.0 | 0.0 | [10.4, 11.2] |
| naviloc_yaw | 5.1 | 4.6 | 9.1 | 11.0 | 26.1 | 0.0 | 0.0 | 0.0 | 0.0 | [10.5, 11.4] |
| naviloc_causal | 10.3 | 5.8 | 12.2 | 15.0 | 3878.4 | 0.9 | 0.8 | 0.3 | 30.0 | [14.5, 15.6] |
