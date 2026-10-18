Config: `{"world": "real", "result_mat": "/home/aclab_pc/Desktop/Paper_UAV/DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 10, "n_boot": 1000, "tag": "F3-07_fsra_test_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 119.6 | 8.8 | 29.8 | 78.7 | 4428.3 | 6.5 | 4.9 | 4.6 | 100.0 | [64.7, 586.4] |
| dead_reckoning | 435.6 | 377.6 | 795.2 | 924.4 | 2137.4 | 99.1 | 97.1 | 31.5 | 53.0 | [848.8, 1041.7] |
| ekf_gated | 10.1 | 4.8 | 11.1 | 14.7 | 742.1 | 0.9 | 0.8 | 0.7 | 2.0 | [13.1, 18.4] |
| pf_topk | 132.7 | 35.8 | 395.8 | 606.5 | 1899.1 | 40.6 | 29.9 | 6.8 | 29.0 | [461.3, 761.7] |
| mh_ekf | 5.6 | 4.2 | 9.4 | 12.0 | 903.6 | 0.2 | 0.1 | 0.1 | 19.0 | [11.2, 13.0] |
