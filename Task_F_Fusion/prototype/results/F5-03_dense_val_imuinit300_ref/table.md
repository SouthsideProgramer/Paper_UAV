Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 6, "n_boot": 200, "tag": "F5-03_dense_val_imuinit300_ref", "cfg": "{}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 12.0 | 4.9 | 12.2 | 16.2 | 792.8 | 1.3 | 1.1 | 0.7 | 1.0 | [14.2, 20.0] |
| pf_topk | 129.2 | 36.6 | 368.4 | 592.6 | 1560.5 | 40.8 | 30.8 | 6.5 | 23.0 | [419.2, 734.9] |
| mh_ekf | 5.4 | 4.0 | 9.2 | 11.5 | 903.6 | 0.2 | 0.1 | 0.1 | 17.0 | [10.7, 12.3] |
