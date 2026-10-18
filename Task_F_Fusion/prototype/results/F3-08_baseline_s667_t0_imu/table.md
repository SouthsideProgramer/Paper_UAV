Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s667_t0_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 122.3 | 8.9 | 44.0 | 987.9 | 4269.0 | 9.2 | 6.8 | 6.5 | 100.0 | [859.6, 1260.9] |
| ekf_gated | 6.0 | 4.8 | 10.9 | 14.2 | 146.1 | 0.1 | 0.1 | 0.0 | 0.0 | [13.1, 15.5] |
| pf_topk | 11.1 | 5.9 | 16.6 | 27.2 | 462.7 | 2.6 | 1.4 | 0.0 | 0.0 | [18.7, 48.0] |
| mh_ekf | 5.0 | 4.3 | 9.0 | 11.5 | 52.8 | 0.0 | 0.0 | 0.0 | 0.0 | [10.7, 12.4] |
