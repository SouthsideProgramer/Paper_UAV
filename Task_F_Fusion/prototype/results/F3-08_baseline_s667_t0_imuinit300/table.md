Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s667_t0_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 122.3 | 8.9 | 44.0 | 987.9 | 4269.0 | 9.2 | 6.8 | 6.5 | 100.0 | [859.6, 1260.9] |
| ekf_gated | 34.9 | 4.9 | 12.0 | 17.1 | 3539.5 | 2.3 | 2.1 | 2.0 | 3.0 | [14.1, 182.7] |
| pf_topk | 134.4 | 38.2 | 406.6 | 608.3 | 1752.9 | 42.0 | 31.2 | 7.3 | 25.0 | [481.0, 749.7] |
| mh_ekf | 5.8 | 4.3 | 9.1 | 11.7 | 1557.1 | 0.2 | 0.1 | 0.1 | 19.0 | [10.9, 12.6] |
