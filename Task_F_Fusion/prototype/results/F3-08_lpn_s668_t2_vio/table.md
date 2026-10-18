Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s668_t2_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 85.2 | 8.7 | 22.9 | 44.6 | 4272.7 | 4.5 | 3.7 | 3.5 | 98.0 | [37.9, 50.2] |
| ekf_gated | 3.2 | 2.9 | 5.6 | 6.7 | 28.2 | 0.0 | 0.0 | 0.0 | 0.0 | [6.3, 7.0] |
| pf_topk | 2.9 | 2.6 | 5.1 | 6.2 | 26.1 | 0.0 | 0.0 | 0.0 | 0.0 | [5.8, 6.4] |
| mh_ekf | 3.0 | 2.7 | 5.3 | 6.3 | 26.0 | 0.0 | 0.0 | 0.0 | 0.0 | [6.0, 6.6] |
