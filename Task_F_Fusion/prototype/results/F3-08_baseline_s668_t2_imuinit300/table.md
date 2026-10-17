Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s668_t2_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 120.4 | 8.9 | 31.4 | 600.6 | 4458.3 | 7.5 | 5.7 | 5.1 | 100.0 | [107.0, 1018.7] |
| ekf_gated | 16.7 | 4.9 | 11.0 | 14.2 | 904.4 | 1.7 | 1.7 | 1.6 | 3.0 | [12.5, 19.6] |
| pf_topk | 114.8 | 26.4 | 394.5 | 605.2 | 1465.7 | 33.8 | 24.7 | 7.0 | 24.0 | [464.8, 688.2] |
| mh_ekf | 5.7 | 4.3 | 8.9 | 11.0 | 929.9 | 0.2 | 0.2 | 0.1 | 24.0 | [10.5, 11.7] |
