#!/usr/bin/env bash
# F3-09: F3-08 rerun with MH-EKF v3 (v_max = 0, frozen at F5-03). Only ekf_gated (determinism check vs F3-08) and mh_ekf.
# usage: bash run_f3_09.sh
set -u
cd "$(dirname "$0")"
PY=${PY:-/home/aclab_pc/miniconda3/envs/adas-observer/bin/python}
GPS=../../datasets/DenseUAV/Dense_GPS_ALL.txt
C=../../../DenseUAV_b8de187/checkpoints
for m in baseline lpn fsra; do for ms in 666 667 668; do
  [ $ms = 666 ] && MAT=$C/$m/pytorch_result_1.mat || MAT=$C/${m}_s$ms/pytorch_result_1.mat
  for s in 0 1 2; do
    for spec in "vio --motion vio" "imu --motion imu" "init300 --motion vio --init_err 300" "imuinit300 --motion imu --init_err 300"; do
      set -- $spec; t=$1; shift
      out=results/F3-09_${m}_s${ms}_t${s}_${t}
      [ -f $out/errors.npz ] && continue
      $PY run_f2.py --world real --gps_path $GPS --result_mat $MAT --campuses test "$@" --cfg '{"v_max": 0.0}' \
        --methods ekf_gated,mh_ekf --seed $s --workers ${WORKERS:-11} --n_boot 200 --tag $(basename $out) > $out.log 2>&1 \
        && echo "ok $out" || echo "FAIL $out"
    done
  done
done; done
echo F3_09_DONE
