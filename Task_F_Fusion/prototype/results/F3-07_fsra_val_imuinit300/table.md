Config: `{"world": "real", "result_mat": "/home/aclab_pc/Desktop/Paper_UAV/DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 10, "n_boot": 1000, "tag": "F3-07_fsra_val_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 163.4 | 9.0 | 60.3 | 247.2 | 5469.5 | 11.4 | 7.7 | 4.8 | 100.0 | [199.4, 732.8] |
| dead_reckoning | 434.6 | 379.8 | 792.4 | 918.7 | 1831.1 | 99.5 | 96.9 | 32.5 | 55.0 | [835.8, 1004.4] |
| ekf_gated | 6.2 | 4.6 | 10.6 | 13.7 | 432.9 | 0.5 | 0.3 | 0.0 | 0.0 | [12.6, 15.1] |
| pf_topk | 127.0 | 35.3 | 366.8 | 562.1 | 1794.1 | 40.5 | 30.2 | 6.1 | 23.0 | [412.0, 742.5] |
| mh_ekf | 5.1 | 3.9 | 8.4 | 10.3 | 903.6 | 0.1 | 0.1 | 0.1 | 18.0 | [9.7, 11.1] |
