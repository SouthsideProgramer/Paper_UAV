Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s666_t0_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 76.7 | 8.6 | 24.7 | 77.9 | 4290.1 | 6.3 | 4.7 | 4.2 | 100.0 | [63.9, 119.6] |
| ekf_gated | 5.1 | 4.3 | 9.1 | 11.6 | 53.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 12.5] |
| pf_topk | 7.9 | 5.6 | 14.1 | 20.2 | 167.1 | 0.9 | 0.2 | 0.0 | 0.0 | [15.9, 30.0] |
| mh_ekf | 4.9 | 4.1 | 8.6 | 10.8 | 56.8 | 0.0 | 0.0 | 0.0 | 0.0 | [10.0, 11.8] |
