Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s666_t1_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 18.1 | 3.4 | 7.1 | 8.5 | 1437.2 | 1.0 | 1.0 | 1.0 | 2.0 | [7.6, 9.9] |
| naviloc | 5.1 | 4.6 | 9.0 | 10.7 | 28.2 | 0.0 | 0.0 | 0.0 | 0.0 | [10.2, 11.2] |
| naviloc_yaw | 5.1 | 4.6 | 8.9 | 10.5 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | [10.1, 10.8] |
| naviloc_causal | 9.4 | 5.9 | 12.1 | 14.8 | 4423.7 | 0.7 | 0.7 | 0.2 | 26.0 | [14.3, 15.1] |
