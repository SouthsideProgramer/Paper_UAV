Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s666_t0_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 76.7 | 8.6 | 24.7 | 77.9 | 4290.1 | 6.3 | 4.7 | 4.2 | 100.0 | [63.9, 119.6] |
| ekf_gated | 39.8 | 4.5 | 10.3 | 16.2 | 1811.1 | 3.1 | 3.1 | 3.0 | 3.0 | [11.5, 867.9] |
| pf_topk | 124.7 | 34.9 | 379.9 | 578.0 | 1700.2 | 39.4 | 28.1 | 6.2 | 26.0 | [431.6, 724.6] |
| mh_ekf | 5.5 | 4.1 | 8.6 | 10.9 | 1277.1 | 0.2 | 0.1 | 0.1 | 18.0 | [10.1, 12.0] |
