Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s666_t2_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 32.9 | 3.2 | 7.2 | 10.1 | 1301.0 | 3.0 | 3.0 | 2.9 | 5.0 | [7.8, 567.9] |
| naviloc | 5.2 | 4.6 | 9.3 | 10.9 | 26.9 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 11.3] |
| naviloc_yaw | 5.2 | 4.6 | 9.3 | 11.1 | 33.0 | 0.0 | 0.0 | 0.0 | 0.0 | [10.7, 11.5] |
| naviloc_causal | 10.4 | 5.8 | 12.2 | 15.2 | 4064.0 | 0.8 | 0.8 | 0.2 | 29.0 | [14.7, 15.8] |
