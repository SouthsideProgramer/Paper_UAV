Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s668_t0_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 123.1 | 8.9 | 32.8 | 613.6 | 4458.7 | 7.7 | 5.9 | 5.3 | 100.0 | [193.2, 1146.4] |
| ekf_gated | 55.3 | 4.9 | 13.1 | 28.8 | 1667.5 | 4.7 | 4.6 | 4.5 | 5.0 | [14.6, 1211.3] |
| pf_topk | 134.0 | 37.2 | 400.4 | 627.5 | 1780.5 | 41.1 | 30.6 | 7.3 | 26.0 | [470.1, 748.5] |
| mh_ekf | 5.6 | 4.1 | 8.6 | 10.6 | 903.6 | 0.2 | 0.2 | 0.1 | 18.0 | [10.1, 11.3] |
