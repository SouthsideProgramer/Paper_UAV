Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s668_t0_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 134.3 | 8.8 | 37.0 | 918.7 | 4458.7 | 8.3 | 6.2 | 5.9 | 100.0 | [587.7, 1275.8] |
| ekf_gated | 3.3 | 2.9 | 5.9 | 7.2 | 48.9 | 0.0 | 0.0 | 0.0 | 0.0 | [6.7, 7.5] |
| pf_topk | 2.9 | 2.5 | 5.1 | 6.1 | 33.6 | 0.0 | 0.0 | 0.0 | 0.0 | [5.7, 6.6] |
| mh_ekf | 2.8 | 2.5 | 5.0 | 6.0 | 36.2 | 0.0 | 0.0 | 0.0 | 0.0 | [5.6, 6.3] |
