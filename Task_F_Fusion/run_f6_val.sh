#!/usr/bin/env bash
# F6-01: NaviLoc window-size sweep on VAL (AerialVL val flights; DenseUAV val campuses 9, 10), s666 of each head.
cd "$(dirname "$0")"
PY=/home/aclab_pc/miniconda3/envs/adas-observer/bin/python
GPS=../../datasets/DenseUAV/Dense_GPS_ALL.txt; C=../../../DenseUAV_b8de187/checkpoints
ME=naviloc,naviloc_yaw,naviloc_causal,mh_ekf
for W in 30 60 120; do O=$((W / 2)); CFG="{\"nl_W\": $W, \"nl_O\": $O, \"v_max\": 0.0}"
  for m in baseline lpn fsra; do
    for spec in "vio --motion vio" "imu --motion imu" "init300 --motion vio --init_err 300" "imuinit300 --motion imu --init_err 300"; do
      set -- $spec; t=$1; shift
      out=F6-01_aerialvl_${m}_W${W}_$t
      [ -f aerialvl/results/$out/errors.npz ] || (cd aerialvl && $PY run_aerialvl.py --feats feats/${m}_s666.npz --split val "$@" \
        --n_noise 5 --methods $ME --cfg "$CFG" --workers 11 --n_boot 100 --tag $out > results/$out.log 2>&1) && echo "ok $out" || echo "FAIL $out"
      out=F6-01_dense_${m}_W${W}_$t
      [ -f prototype/results/$out/errors.npz ] || (cd prototype && $PY run_f2.py --world real --gps_path $GPS --result_mat $C/$m/pytorch_result_1.mat \
        --campuses val "$@" --methods $ME --cfg "$CFG" --seed 0 --workers 11 --n_boot 100 --tag $out > results/$out.log 2>&1) && echo "ok $out" || echo "FAIL $out"
    done
  done
done
echo F6_VAL_DONE
