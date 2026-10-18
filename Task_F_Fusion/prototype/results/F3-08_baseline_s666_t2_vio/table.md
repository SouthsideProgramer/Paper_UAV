Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s666_t2_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 129.6 | 8.9 | 35.9 | 1082.8 | 4379.0 | 8.2 | 6.8 | 6.0 | 100.0 | [592.6, 1283.8] |
| ekf_gated | 3.4 | 3.0 | 6.3 | 7.5 | 30.3 | 0.0 | 0.0 | 0.0 | 0.0 | [7.1, 7.9] |
| pf_topk | 3.0 | 2.6 | 5.5 | 6.6 | 23.7 | 0.0 | 0.0 | 0.0 | 0.0 | [6.2, 7.0] |
| mh_ekf | 3.1 | 2.7 | 5.5 | 6.5 | 26.0 | 0.0 | 0.0 | 0.0 | 0.0 | [6.2, 6.8] |
