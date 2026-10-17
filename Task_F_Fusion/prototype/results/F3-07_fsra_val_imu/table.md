Config: `{"world": "real", "result_mat": "/home/aclab_pc/Desktop/Paper_UAV/DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 10, "n_boot": 1000, "tag": "F3-07_fsra_val_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 163.4 | 9.0 | 60.3 | 247.2 | 5469.5 | 11.4 | 7.7 | 4.8 | 100.0 | [199.4, 732.8] |
| dead_reckoning | 227.4 | 158.7 | 502.9 | 693.3 | 1857.2 | 78.5 | 63.3 | 10.1 | 33.0 | [550.1, 864.4] |
| ekf_gated | 5.6 | 4.6 | 10.4 | 13.2 | 129.8 | 0.1 | 0.0 | 0.0 | 0.0 | [12.3, 14.2] |
| pf_topk | 7.7 | 5.3 | 13.8 | 19.2 | 198.0 | 1.1 | 0.3 | 0.0 | 0.0 | [15.1, 29.1] |
| mh_ekf | 4.5 | 3.9 | 8.4 | 10.3 | 41.4 | 0.0 | 0.0 | 0.0 | 0.0 | [9.6, 11.0] |
