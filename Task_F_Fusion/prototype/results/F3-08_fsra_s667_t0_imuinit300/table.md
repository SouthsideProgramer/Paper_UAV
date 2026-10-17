Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s667_t0_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 140.0 | 9.0 | 47.8 | 1290.8 | 4458.7 | 9.7 | 7.9 | 7.1 | 100.0 | [1220.0, 1302.9] |
| ekf_gated | 75.0 | 5.1 | 13.6 | 54.7 | 3636.1 | 5.0 | 5.0 | 5.0 | 6.0 | [14.6, 1369.4] |
| pf_topk | 132.9 | 36.1 | 413.8 | 611.7 | 1646.3 | 40.6 | 30.5 | 7.3 | 31.0 | [483.9, 735.3] |
| mh_ekf | 6.2 | 4.5 | 9.7 | 12.1 | 1773.0 | 0.2 | 0.2 | 0.1 | 20.0 | [11.4, 12.9] |
