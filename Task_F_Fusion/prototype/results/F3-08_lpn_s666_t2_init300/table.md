Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s666_t2_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 73.4 | 8.6 | 23.7 | 65.4 | 4294.0 | 5.8 | 4.4 | 3.8 | 100.0 | [55.6, 75.6] |
| ekf_gated | 40.9 | 2.9 | 5.9 | 9.3 | 1301.0 | 4.1 | 4.1 | 3.9 | 4.0 | [6.4, 886.4] |
| pf_topk | 6.2 | 4.2 | 10.1 | 13.2 | 888.2 | 0.4 | 0.3 | 0.0 | 7.0 | [11.9, 15.1] |
| mh_ekf | 3.6 | 2.7 | 5.1 | 6.0 | 930.4 | 0.1 | 0.1 | 0.1 | 24.0 | [5.8, 6.3] |
