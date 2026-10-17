Config: `{"world": "real", "result_mat": "/home/aclab_pc/Desktop/Paper_UAV/DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 10, "n_boot": 1000, "tag": "F3-07_fsra_val_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 163.4 | 9.0 | 60.3 | 247.2 | 5469.5 | 11.4 | 7.7 | 4.8 | 100.0 | [199.4, 732.8] |
| dead_reckoning | 15.2 | 14.5 | 25.5 | 29.5 | 75.1 | 0.4 | 0.0 | 0.0 | 0.0 | [26.2, 32.8] |
| ekf_gated | 3.3 | 2.9 | 5.9 | 7.2 | 31.2 | 0.0 | 0.0 | 0.0 | 0.0 | [6.7, 7.7] |
| pf_topk | 2.7 | 2.4 | 4.7 | 5.6 | 19.1 | 0.0 | 0.0 | 0.0 | 0.0 | [5.3, 6.0] |
| mh_ekf | 2.7 | 2.4 | 4.8 | 5.6 | 19.5 | 0.0 | 0.0 | 0.0 | 0.0 | [5.3, 5.9] |
