Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s666_t0_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 10.1 | 4.8 | 11.1 | 14.7 | 742.1 | 0.9 | 0.8 | 0.7 | 2.0 | [13.0, 17.4] |
| naviloc | 102.8 | 65.7 | 217.7 | 308.5 | 1269.9 | 57.0 | 35.4 | 2.8 | 14.0 | [239.5, 439.4] |
| naviloc_yaw | 99.9 | 69.7 | 207.0 | 297.1 | 1051.0 | 60.5 | 36.5 | 1.8 | 12.0 | [233.1, 385.4] |
| naviloc_causal | 102.1 | 65.5 | 223.6 | 292.6 | 3744.4 | 56.6 | 37.1 | 2.0 | 34.0 | [245.3, 357.7] |
