Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s668_t2_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 126.4 | 8.9 | 32.5 | 712.8 | 4458.9 | 7.8 | 5.7 | 5.4 | 100.0 | [100.8, 927.0] |
| ekf_gated | 5.6 | 4.7 | 10.3 | 12.8 | 46.7 | 0.0 | 0.0 | 0.0 | 0.0 | [12.3, 13.4] |
| pf_topk | 9.7 | 5.7 | 16.5 | 25.7 | 223.8 | 2.2 | 1.1 | 0.0 | 0.0 | [19.2, 38.9] |
| mh_ekf | 4.6 | 4.0 | 8.3 | 10.3 | 36.6 | 0.0 | 0.0 | 0.0 | 0.0 | [9.8, 10.9] |
