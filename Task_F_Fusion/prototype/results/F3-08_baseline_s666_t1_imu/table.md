Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s666_t1_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 136.6 | 9.0 | 39.4 | 1174.4 | 4379.8 | 8.7 | 7.1 | 5.9 | 99.0 | [686.4, 1299.3] |
| ekf_gated | 5.9 | 4.9 | 11.2 | 13.9 | 56.7 | 0.0 | 0.0 | 0.0 | 0.0 | [13.1, 14.7] |
| pf_topk | 10.0 | 5.9 | 17.4 | 31.1 | 284.7 | 2.2 | 0.8 | 0.0 | 0.0 | [20.6, 44.9] |
| mh_ekf | 5.2 | 4.4 | 9.6 | 11.9 | 51.4 | 0.0 | 0.0 | 0.0 | 0.0 | [11.3, 12.4] |
