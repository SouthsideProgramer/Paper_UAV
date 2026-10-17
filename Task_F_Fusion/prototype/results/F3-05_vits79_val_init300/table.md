Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-05_vits79_val_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 152.3 | 8.9 | 56.9 | 230.1 | 5315.0 | 11.0 | 7.2 | 4.7 | 100.0 | [162.9, 663.3] |
| dead_reckoning | 353.6 | 347.5 | 586.9 | 670.2 | 904.7 | 99.5 | 94.2 | 18.2 | 20.0 | [583.3, 715.3] |
| ekf_gated | 11.5 | 2.9 | 6.5 | 8.5 | 756.8 | 1.5 | 1.4 | 1.0 | 1.0 | [7.4, 12.8] |
| pf_topk | 6.3 | 4.2 | 10.6 | 13.7 | 714.6 | 0.7 | 0.5 | 0.0 | 4.0 | [12.1, 15.8] |
| mh_ekf | 3.4 | 2.5 | 5.1 | 6.2 | 903.8 | 0.2 | 0.1 | 0.1 | 17.0 | [5.8, 6.6] |
