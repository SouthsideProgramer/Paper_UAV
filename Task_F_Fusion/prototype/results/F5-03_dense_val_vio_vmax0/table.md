Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 6, "n_boot": 200, "tag": "F5-03_dense_val_vio_vmax0", "cfg": "{\"v_max\":0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 3.4 | 2.8 | 6.1 | 7.6 | 38.4 | 0.0 | 0.0 | 0.0 | 0.0 | [7.1, 8.1] |
| pf_topk | 2.8 | 2.4 | 5.1 | 6.1 | 36.6 | 0.0 | 0.0 | 0.0 | 0.0 | [5.8, 6.6] |
| mh_ekf | 2.8 | 2.5 | 5.1 | 6.1 | 38.4 | 0.0 | 0.0 | 0.0 | 0.0 | [5.8, 6.5] |
