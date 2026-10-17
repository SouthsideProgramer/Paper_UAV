Config: `{"world": "real", "result_mat": "/home/aclab_pc/Desktop/Paper_UAV/DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 10, "n_boot": 1000, "tag": "F3-07_fsra_val_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 163.4 | 9.0 | 60.3 | 247.2 | 5469.5 | 11.4 | 7.7 | 4.8 | 100.0 | [199.4, 732.8] |
| dead_reckoning | 353.6 | 347.5 | 586.9 | 670.2 | 904.7 | 99.5 | 94.2 | 18.2 | 20.0 | [583.3, 715.3] |
| ekf_gated | 4.2 | 2.9 | 6.1 | 7.5 | 433.2 | 0.6 | 0.4 | 0.0 | 0.0 | [6.9, 8.1] |
| pf_topk | 5.8 | 4.1 | 10.0 | 12.9 | 689.5 | 0.4 | 0.3 | 0.0 | 4.0 | [11.6, 15.0] |
| mh_ekf | 3.3 | 2.4 | 4.7 | 5.6 | 903.8 | 0.1 | 0.1 | 0.1 | 18.0 | [5.3, 6.0] |
