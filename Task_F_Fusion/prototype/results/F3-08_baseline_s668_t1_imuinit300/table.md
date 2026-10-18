Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s668_t1_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 119.5 | 8.9 | 29.3 | 114.2 | 4459.1 | 7.1 | 5.3 | 4.7 | 100.0 | [77.3, 604.3] |
| ekf_gated | 34.9 | 4.8 | 11.3 | 15.2 | 1633.3 | 2.1 | 2.0 | 2.0 | 3.0 | [12.6, 633.2] |
| pf_topk | 124.9 | 35.9 | 397.0 | 541.1 | 1381.0 | 41.5 | 30.7 | 6.2 | 26.0 | [433.7, 649.4] |
| mh_ekf | 5.6 | 4.2 | 9.0 | 11.0 | 925.7 | 0.2 | 0.1 | 0.1 | 26.0 | [10.4, 11.8] |
