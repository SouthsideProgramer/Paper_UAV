#!/usr/bin/env bash
# F6-02: NaviLoc (W = 30, O = 15, K = 3, chosen on val in F6-01) on exactly the runs of F5-04 (AerialVL short test),
# F5-05 (AerialVL long test) and F3-09 (DenseUAV test campuses). One cheap existing method is rerun with it to check
# that the runs are bit-identical, so the other methods' errors can be taken from those experiments. Run once.
cd "$(dirname "$0")"
PY=/home/aclab_pc/miniconda3/envs/adas-observer/bin/python
GPS=../../datasets/DenseUAV/Dense_GPS_ALL.txt; C=../../../DenseUAV_b8de187/checkpoints
NL=naviloc,naviloc_yaw,naviloc_causal
SCN=("vio --motion vio" "imu --motion imu" "init300 --motion vio --init_err 300" "imuinit300 --motion imu --init_err 300")
run() { [ -f $1/results/$2/errors.npz ] && return; (cd $1 && shift && t=$1 && shift && $PY "$@" --tag $t > results/$t.log 2>&1) \
          && echo "ok $2" || echo "FAIL $2"; }
for m in baseline lpn fsra; do for s in 666 667 668; do
  for spec in "${SCN[@]}"; do set -- $spec; t=$1; shift
    run aerialvl F6-02_short_${m}_s${s}_$t run_aerialvl.py --feats feats/${m}_s$s.npz --split test "$@" --n_noise 5 \
      --methods dead_reckoning,$NL --workers 11 --n_boot 100
    run aerialvl F6-02_long_${m}_s${s}_$t run_aerialvl.py --feats feats/merged/${m}_s$s.npz --calib_from feats/${m}_s$s.npz \
      --split test_long "$@" --win_step 60 --n_noise 3 --methods dead_reckoning,$NL --workers 11 --n_boot 100
  done
done; done
for m in baseline lpn fsra; do for ms in 666 667 668; do
  [ $ms = 666 ] && MAT=$C/$m/pytorch_result_1.mat || MAT=$C/${m}_s$ms/pytorch_result_1.mat
  for s in 0 1 2; do for spec in "${SCN[@]}"; do set -- $spec; t=$1; shift
    run prototype F6-02_dense_${m}_s${ms}_t${s}_$t run_f2.py --world real --gps_path $GPS --result_mat $MAT --campuses test "$@" \
      --cfg '{"v_max": 0.0}' --methods ekf_gated,$NL --seed $s --workers 11 --n_boot 100
  done; done
done; done
echo F6_TEST_DONE
