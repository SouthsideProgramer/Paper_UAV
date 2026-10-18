Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s667_t2_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 109.2 | 8.9 | 37.5 | 632.3 | 4272.7 | 8.3 | 6.2 | 5.8 | 100.0 | [586.2, 939.8] |
| ekf_gated | 39.2 | 3.1 | 7.0 | 12.2 | 1271.7 | 4.0 | 4.0 | 4.0 | 4.0 | [7.5, 608.8] |
| pf_topk | 6.2 | 4.2 | 10.2 | 13.3 | 888.2 | 0.4 | 0.3 | 0.0 | 6.0 | [11.8, 15.2] |
| mh_ekf | 3.8 | 2.7 | 5.3 | 6.3 | 930.4 | 0.2 | 0.1 | 0.1 | 25.0 | [5.9, 6.6] |
