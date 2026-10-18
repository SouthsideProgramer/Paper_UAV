Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s668_t0_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 95.2 | 8.7 | 24.5 | 51.1 | 4269.0 | 5.1 | 4.2 | 4.0 | 99.0 | [44.6, 78.5] |
| ekf_gated | 5.1 | 4.3 | 9.2 | 11.7 | 55.1 | 0.0 | 0.0 | 0.0 | 0.0 | [10.8, 12.4] |
| pf_topk | 10.0 | 5.6 | 16.2 | 26.4 | 407.5 | 1.7 | 0.8 | 0.0 | 0.0 | [18.3, 40.1] |
| mh_ekf | 4.8 | 4.2 | 8.7 | 10.7 | 46.4 | 0.0 | 0.0 | 0.0 | 0.0 | [10.0, 11.6] |
