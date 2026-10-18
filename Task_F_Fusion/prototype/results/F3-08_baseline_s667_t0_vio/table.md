Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s667_t0_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 122.3 | 8.9 | 44.0 | 987.9 | 4269.0 | 9.2 | 6.8 | 6.5 | 100.0 | [859.6, 1260.9] |
| ekf_gated | 3.6 | 3.1 | 6.2 | 7.6 | 38.5 | 0.0 | 0.0 | 0.0 | 0.0 | [7.2, 8.4] |
| pf_topk | 3.0 | 2.6 | 5.3 | 6.4 | 26.5 | 0.0 | 0.0 | 0.0 | 0.0 | [6.1, 6.8] |
| mh_ekf | 3.0 | 2.7 | 5.3 | 6.3 | 35.0 | 0.0 | 0.0 | 0.0 | 0.0 | [6.1, 6.7] |
