Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s668_t2_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 126.4 | 8.9 | 32.5 | 712.8 | 4458.9 | 7.8 | 5.7 | 5.4 | 100.0 | [100.8, 927.0] |
| ekf_gated | 52.5 | 3.2 | 7.1 | 395.8 | 1432.9 | 5.0 | 5.0 | 5.0 | 5.0 | [7.4, 945.5] |
| pf_topk | 6.2 | 4.2 | 10.2 | 13.4 | 888.2 | 0.4 | 0.3 | 0.0 | 6.0 | [12.1, 15.6] |
| mh_ekf | 3.7 | 2.6 | 5.0 | 6.0 | 932.6 | 0.2 | 0.2 | 0.1 | 24.0 | [5.6, 6.4] |
