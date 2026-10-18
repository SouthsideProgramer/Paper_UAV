Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s668_t0_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 123.1 | 8.9 | 32.8 | 613.6 | 4458.7 | 7.7 | 5.9 | 5.3 | 100.0 | [193.2, 1146.4] |
| ekf_gated | 3.4 | 3.0 | 5.9 | 7.3 | 38.5 | 0.0 | 0.0 | 0.0 | 0.0 | [6.7, 8.0] |
| pf_topk | 2.9 | 2.6 | 5.2 | 6.3 | 32.4 | 0.0 | 0.0 | 0.0 | 0.0 | [5.8, 6.9] |
| mh_ekf | 2.9 | 2.6 | 5.2 | 6.2 | 35.0 | 0.0 | 0.0 | 0.0 | 0.0 | [5.8, 6.6] |
