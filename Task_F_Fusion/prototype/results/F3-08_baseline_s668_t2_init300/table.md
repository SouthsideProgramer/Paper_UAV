Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s668_t2_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 120.4 | 8.9 | 31.4 | 600.6 | 4458.3 | 7.5 | 5.7 | 5.1 | 100.0 | [107.0, 1018.7] |
| ekf_gated | 16.9 | 3.1 | 6.4 | 8.3 | 744.6 | 2.0 | 2.0 | 2.0 | 3.0 | [7.2, 536.8] |
| pf_topk | 6.3 | 4.2 | 10.2 | 13.7 | 888.2 | 0.5 | 0.3 | 0.1 | 6.0 | [12.3, 15.2] |
| mh_ekf | 3.8 | 2.7 | 5.2 | 6.2 | 930.4 | 0.2 | 0.2 | 0.1 | 24.0 | [5.9, 6.7] |
