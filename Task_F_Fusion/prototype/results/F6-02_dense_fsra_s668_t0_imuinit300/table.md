Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s668_t0_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 38.2 | 4.6 | 11.3 | 17.4 | 1780.6 | 3.1 | 3.1 | 3.0 | 5.0 | [12.6, 865.3] |
| naviloc | 101.1 | 63.0 | 219.1 | 320.3 | 1204.2 | 56.5 | 34.7 | 2.4 | 15.0 | [247.7, 429.3] |
| naviloc_yaw | 100.1 | 70.6 | 207.3 | 284.8 | 945.0 | 60.4 | 36.8 | 1.7 | 10.0 | [235.8, 370.9] |
| naviloc_causal | 102.9 | 66.2 | 223.7 | 295.1 | 3783.5 | 56.6 | 37.0 | 2.2 | 38.0 | [250.8, 387.0] |
