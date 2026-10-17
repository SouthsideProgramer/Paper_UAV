Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-05_vits79_val_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 152.3 | 8.9 | 56.9 | 230.1 | 5315.0 | 11.0 | 7.2 | 4.7 | 100.0 | [162.9, 663.3] |
| dead_reckoning | 15.2 | 14.5 | 25.5 | 29.5 | 75.1 | 0.4 | 0.0 | 0.0 | 0.0 | [26.2, 32.8] |
| ekf_gated | 3.4 | 2.8 | 6.1 | 7.6 | 38.4 | 0.0 | 0.0 | 0.0 | 0.0 | [7.1, 8.2] |
| pf_topk | 2.8 | 2.4 | 5.1 | 6.1 | 36.6 | 0.0 | 0.0 | 0.0 | 0.0 | [5.8, 6.6] |
| mh_ekf | 2.8 | 2.5 | 5.1 | 6.1 | 38.4 | 0.0 | 0.0 | 0.0 | 0.0 | [5.8, 6.5] |
