Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s668_t0_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 134.3 | 8.8 | 37.0 | 918.7 | 4458.7 | 8.3 | 6.2 | 5.9 | 100.0 | [587.7, 1275.8] |
| ekf_gated | 33.4 | 3.0 | 6.5 | 9.1 | 1176.6 | 3.1 | 3.1 | 3.0 | 5.0 | [7.3, 814.8] |
| pf_topk | 6.0 | 4.3 | 10.4 | 13.3 | 686.6 | 0.4 | 0.3 | 0.0 | 6.0 | [11.9, 14.8] |
| mh_ekf | 3.6 | 2.5 | 5.0 | 6.0 | 1169.1 | 0.2 | 0.2 | 0.1 | 19.0 | [5.6, 6.3] |
