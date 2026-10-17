Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-05_vits79_val_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 152.3 | 8.9 | 56.9 | 230.1 | 5315.0 | 11.0 | 7.2 | 4.7 | 100.0 | [162.9, 663.3] |
| dead_reckoning | 227.4 | 158.7 | 502.9 | 693.3 | 1857.2 | 78.5 | 63.3 | 10.1 | 33.0 | [550.1, 864.4] |
| ekf_gated | 5.9 | 4.8 | 11.4 | 14.4 | 51.1 | 0.0 | 0.0 | 0.0 | 0.0 | [13.5, 15.3] |
| pf_topk | 7.4 | 5.5 | 13.9 | 19.0 | 141.5 | 0.3 | 0.1 | 0.0 | 0.0 | [15.3, 24.1] |
| mh_ekf | 4.8 | 4.0 | 9.1 | 11.3 | 41.9 | 0.0 | 0.0 | 0.0 | 0.0 | [10.4, 12.2] |
