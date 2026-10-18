Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s666_t2_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 40.9 | 2.9 | 5.9 | 9.3 | 1301.0 | 4.1 | 4.1 | 3.9 | 4.0 | [6.4, 873.5] |
| naviloc | 5.0 | 4.5 | 9.1 | 10.6 | 29.6 | 0.0 | 0.0 | 0.0 | 0.0 | [10.4, 11.0] |
| naviloc_yaw | 5.0 | 4.5 | 9.1 | 10.6 | 27.0 | 0.0 | 0.0 | 0.0 | 0.0 | [10.3, 11.0] |
| naviloc_causal | 9.2 | 5.9 | 11.9 | 14.3 | 3204.6 | 0.7 | 0.7 | 0.2 | 26.0 | [13.9, 14.7] |
