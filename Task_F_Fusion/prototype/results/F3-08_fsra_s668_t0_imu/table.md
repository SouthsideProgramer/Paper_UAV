Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s668_t0_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 134.3 | 8.8 | 37.0 | 918.7 | 4458.7 | 8.3 | 6.2 | 5.9 | 100.0 | [587.7, 1275.8] |
| ekf_gated | 5.4 | 4.5 | 10.0 | 12.7 | 52.9 | 0.0 | 0.0 | 0.0 | 0.0 | [11.8, 13.7] |
| pf_topk | 10.5 | 5.6 | 14.9 | 24.8 | 453.0 | 1.9 | 1.2 | 0.0 | 0.0 | [17.5, 39.3] |
| mh_ekf | 4.5 | 3.9 | 8.2 | 10.2 | 45.2 | 0.0 | 0.0 | 0.0 | 0.0 | [9.6, 11.0] |
