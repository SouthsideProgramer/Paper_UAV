Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-05_vits79_test_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 144.7 | 8.9 | 40.4 | 1306.3 | 4379.3 | 8.8 | 7.4 | 6.7 | 100.0 | [1082.7, 1341.8] |
| dead_reckoning | 230.9 | 162.5 | 521.5 | 712.8 | 1870.9 | 78.0 | 63.4 | 10.9 | 38.0 | [573.1, 870.6] |
| ekf_gated | 5.6 | 4.7 | 10.4 | 13.1 | 65.2 | 0.0 | 0.0 | 0.0 | 0.0 | [12.4, 14.1] |
| pf_topk | 11.4 | 5.7 | 14.6 | 21.3 | 487.4 | 2.2 | 1.6 | 0.0 | 0.0 | [16.1, 42.8] |
| mh_ekf | 4.9 | 4.2 | 9.1 | 11.3 | 45.8 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 11.9] |
