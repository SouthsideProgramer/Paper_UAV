Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s666_t0_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 5.1 | 4.3 | 9.1 | 11.6 | 53.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 12.3] |
| naviloc | 97.2 | 61.5 | 209.5 | 299.2 | 1010.9 | 55.3 | 34.6 | 2.2 | 13.0 | [239.9, 402.2] |
| naviloc_yaw | 97.9 | 67.6 | 209.2 | 279.8 | 965.0 | 59.7 | 36.7 | 1.5 | 9.0 | [235.1, 353.1] |
| naviloc_causal | 98.5 | 63.9 | 215.4 | 279.3 | 1261.6 | 56.0 | 36.4 | 1.9 | 17.0 | [235.9, 345.6] |
