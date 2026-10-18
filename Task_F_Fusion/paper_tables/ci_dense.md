## dense: MH-EKF v3 − X, 95 % CI bootstrap over 300 trajectories (3 retrieval seeds pooled, paired); * = CI excludes 0

p95 difference (m)

| Head | Scenario | − ekf_gated | − pf_topk | − naviloc_yaw |
|---|---|---|---|---|
| baseline | vio | -1 [-1, -1]* | -0 [-0, +0] | -4 [-5, -4]* |
| baseline | imu | -2 [-3, -2]* | -14 [-19, -9]* | -250 [-279, -228]* |
| baseline | init300 | -4 [-16, -2]* | -7 [-8, -6]* | -4 [-5, -4]* |
| baseline | imuinit300 | -7 [-13, -4]* | -580 [-644, -498]* | -250 [-282, -227]* |
| lpn | vio | -0 [-1, -0]* | -0 [-0, +0] | -4 [-5, -4]* |
| lpn | imu | -1 [-1, -1]* | -21 [-28, -14]* | -250 [-279, -227]* |
| lpn | init300 | -1 [-2, -1]* | -7 [-8, -6]* | -4 [-5, -4]* |
| lpn | imuinit300 | -3 [-5, -2]* | -574 [-637, -499]* | -249 [-280, -227]* |
| fsra | vio | -1 [-1, -1]* | -0 [-0, +0] | -4 [-4, -4]* |
| fsra | imu | -2 [-2, -2]* | -15 [-22, -10]* | -250 [-280, -226]* |
| fsra | init300 | -3 [-13, -2]* | -7 [-8, -6]* | -4 [-4, -4]* |
| fsra | imuinit300 | -6 [-11, -4]* | -572 [-652, -498]* | -250 [-279, -227]* |

% runs lost (> 100 m after the first 30 s), difference in percentage points

| Head | Scenario | − ekf_gated | − pf_topk | − naviloc_yaw |
|---|---|---|---|---|
| baseline | vio | +0 [+0, +0] | +0 [+0, +0] | +0 [+0, +0] |
| baseline | imu | -0 [-1, +0] | -4 [-6, -2]* | -88 [-91, -84]* |
| baseline | init300 | -4 [-5, -3]* | +0 [+0, +0] | +0 [+0, +0] |
| baseline | imuinit300 | -4 [-5, -2]* | -56 [-61, -51]* | -88 [-91, -84]* |
| lpn | vio | +0 [+0, +0] | +0 [+0, +0] | +0 [+0, +0] |
| lpn | imu | -0 [-0, +0] | -6 [-8, -4]* | -88 [-91, -85]* |
| lpn | init300 | -2 [-3, -1]* | -0 [-0, +0] | +0 [+0, +0] |
| lpn | imuinit300 | -2 [-3, -1]* | -56 [-61, -51]* | -88 [-91, -85]* |
| fsra | vio | +0 [+0, +0] | +0 [+0, +0] | +0 [+0, +0] |
| fsra | imu | +0 [+0, +0] | -4 [-6, -3]* | -88 [-92, -84]* |
| fsra | init300 | -3 [-5, -2]* | -0 [-0, +0] | +0 [+0, +0] |
| fsra | imuinit300 | -3 [-5, -2]* | -55 [-60, -50]* | -88 [-91, -84]* |

Summary p95: MH-EKF significantly better in 33/36 comparisons, significantly worse in 0.
