Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-05_vits79_val_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 152.3 | 8.9 | 56.9 | 230.1 | 5315.0 | 11.0 | 7.2 | 4.7 | 100.0 | [162.9, 663.3] |
| dead_reckoning | 434.6 | 379.8 | 792.4 | 918.7 | 1831.1 | 99.5 | 96.9 | 32.5 | 55.0 | [835.8, 1004.4] |
| ekf_gated | 12.0 | 4.9 | 12.2 | 16.2 | 792.8 | 1.3 | 1.1 | 0.7 | 1.0 | [14.4, 20.4] |
| pf_topk | 129.2 | 36.6 | 368.4 | 592.6 | 1560.5 | 40.8 | 30.8 | 6.5 | 23.0 | [427.4, 740.7] |
| mh_ekf | 5.4 | 4.0 | 9.2 | 11.5 | 903.6 | 0.2 | 0.1 | 0.1 | 17.0 | [10.5, 12.5] |
