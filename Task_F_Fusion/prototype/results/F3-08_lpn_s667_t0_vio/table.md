Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s667_t0_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 84.1 | 8.8 | 30.4 | 75.8 | 4290.1 | 6.4 | 4.3 | 3.8 | 87.0 | [65.8, 98.2] |
| ekf_gated | 3.5 | 3.0 | 6.1 | 7.5 | 43.8 | 0.0 | 0.0 | 0.0 | 0.0 | [7.0, 8.0] |
| pf_topk | 3.1 | 2.7 | 5.5 | 6.8 | 41.2 | 0.0 | 0.0 | 0.0 | 0.0 | [6.3, 7.1] |
| mh_ekf | 3.2 | 2.8 | 5.5 | 6.7 | 43.8 | 0.0 | 0.0 | 0.0 | 0.0 | [6.2, 7.1] |
