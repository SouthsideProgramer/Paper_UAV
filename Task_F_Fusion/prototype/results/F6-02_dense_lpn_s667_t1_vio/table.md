Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s667_t1_vio", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 3.5 | 3.1 | 6.3 | 7.4 | 21.4 | 0.0 | 0.0 | 0.0 | 0.0 | [7.1, 7.8] |
| naviloc | 5.2 | 4.7 | 9.1 | 10.9 | 29.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.5, 11.2] |
| naviloc_yaw | 5.2 | 4.7 | 9.1 | 10.8 | 29.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.5, 11.1] |
| naviloc_causal | 6.7 | 5.9 | 12.0 | 14.5 | 676.8 | 0.1 | 0.0 | 0.0 | 1.0 | [13.9, 14.8] |
