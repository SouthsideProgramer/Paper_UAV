Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-05_vits79_test_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 144.7 | 8.9 | 40.4 | 1306.3 | 4379.3 | 8.8 | 7.4 | 6.7 | 100.0 | [1082.7, 1341.8] |
| dead_reckoning | 435.6 | 377.6 | 795.2 | 924.4 | 2137.4 | 99.1 | 97.1 | 31.5 | 53.0 | [848.8, 1041.7] |
| ekf_gated | 71.1 | 4.9 | 13.9 | 680.9 | 1912.3 | 5.9 | 5.8 | 5.6 | 8.0 | [15.5, 1266.6] |
| pf_topk | 130.1 | 36.7 | 397.2 | 618.3 | 1682.2 | 40.7 | 29.7 | 7.1 | 26.0 | [450.0, 771.2] |
| mh_ekf | 5.6 | 4.1 | 9.1 | 11.4 | 1263.3 | 0.2 | 0.1 | 0.1 | 20.0 | [10.7, 12.1] |
