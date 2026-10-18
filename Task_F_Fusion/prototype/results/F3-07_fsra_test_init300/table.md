Config: `{"world": "real", "result_mat": "/home/aclab_pc/Desktop/Paper_UAV/DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 10, "n_boot": 1000, "tag": "F3-07_fsra_test_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 119.6 | 8.8 | 29.8 | 78.7 | 4428.3 | 6.5 | 4.9 | 4.6 | 100.0 | [64.7, 586.4] |
| dead_reckoning | 353.4 | 347.7 | 586.6 | 670.4 | 904.0 | 99.7 | 94.0 | 18.5 | 20.0 | [581.5, 716.0] |
| ekf_gated | 9.4 | 3.1 | 6.6 | 8.5 | 572.9 | 1.1 | 1.1 | 1.0 | 2.0 | [7.5, 11.1] |
| pf_topk | 6.1 | 4.4 | 10.3 | 13.4 | 686.6 | 0.3 | 0.3 | 0.0 | 5.0 | [12.0, 15.0] |
| mh_ekf | 3.8 | 2.7 | 5.6 | 6.9 | 903.8 | 0.1 | 0.1 | 0.1 | 19.0 | [6.3, 7.6] |
