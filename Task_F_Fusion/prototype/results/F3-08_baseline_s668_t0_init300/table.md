Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s668_t0_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 123.1 | 8.9 | 32.8 | 613.6 | 4458.7 | 7.7 | 5.9 | 5.3 | 100.0 | [193.2, 1146.4] |
| ekf_gated | 56.3 | 3.2 | 7.4 | 135.3 | 1286.1 | 5.1 | 5.0 | 5.0 | 5.0 | [8.1, 1179.5] |
| pf_topk | 6.0 | 4.3 | 10.1 | 13.0 | 686.6 | 0.3 | 0.3 | 0.0 | 4.0 | [11.7, 14.6] |
| mh_ekf | 3.8 | 2.5 | 5.1 | 6.2 | 903.8 | 0.2 | 0.2 | 0.1 | 18.0 | [5.8, 6.6] |
