Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s667_t0_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 140.0 | 9.0 | 47.8 | 1290.8 | 4458.7 | 9.7 | 7.9 | 7.1 | 100.0 | [1220.0, 1302.9] |
| ekf_gated | 74.6 | 3.2 | 7.8 | 851.7 | 1770.2 | 6.1 | 6.0 | 6.0 | 6.0 | [8.1, 1300.8] |
| pf_topk | 6.3 | 4.4 | 10.3 | 13.2 | 1091.7 | 0.4 | 0.3 | 0.0 | 8.0 | [11.9, 15.4] |
| mh_ekf | 4.2 | 2.8 | 5.7 | 6.9 | 1773.0 | 0.2 | 0.2 | 0.1 | 20.0 | [6.5, 7.4] |
