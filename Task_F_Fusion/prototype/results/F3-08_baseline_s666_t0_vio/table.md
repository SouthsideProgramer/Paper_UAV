Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s666_t0_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 144.7 | 8.9 | 40.4 | 1306.3 | 4379.3 | 8.8 | 7.4 | 6.7 | 100.0 | [1171.0, 1341.8] |
| ekf_gated | 3.5 | 3.1 | 6.3 | 7.7 | 33.5 | 0.0 | 0.0 | 0.0 | 0.0 | [7.1, 8.3] |
| pf_topk | 3.0 | 2.7 | 5.4 | 6.4 | 24.4 | 0.0 | 0.0 | 0.0 | 0.0 | [6.0, 6.9] |
| mh_ekf | 3.0 | 2.7 | 5.3 | 6.4 | 25.1 | 0.0 | 0.0 | 0.0 | 0.0 | [5.9, 6.8] |
