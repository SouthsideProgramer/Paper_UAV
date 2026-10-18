Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s666_t1_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 73.3 | 8.7 | 25.4 | 68.0 | 4291.3 | 6.0 | 4.4 | 4.0 | 100.0 | [59.8, 91.8] |
| ekf_gated | 3.2 | 2.8 | 5.6 | 6.8 | 50.9 | 0.0 | 0.0 | 0.0 | 0.0 | [6.4, 7.2] |
| pf_topk | 6.4 | 4.3 | 10.8 | 14.3 | 911.5 | 0.4 | 0.3 | 0.0 | 6.0 | [13.0, 15.8] |
| mh_ekf | 3.7 | 2.7 | 5.4 | 6.4 | 926.1 | 0.1 | 0.1 | 0.1 | 26.0 | [6.1, 6.9] |
