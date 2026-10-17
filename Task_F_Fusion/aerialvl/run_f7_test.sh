#!/usr/bin/env bash
# F7-02: F5-04 (short test) and F5-05 (long test) rerun with the FINE-TUNED retrieval features (feats/ft/), filter
# design frozen (MH-EKF v3), calibration offset re-measured on the val flights of the same feature file. Run once.
cd "$(dirname "$0")"
PY=/home/aclab_pc/miniconda3/envs/adas-observer/bin/python
ME=retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw
SCN=("vio --motion vio" "imu --motion imu" "init300 --motion vio --init_err 300" "imuinit300 --motion imu --init_err 300")
for m in baseline lpn fsra; do for s in 666 667 668; do
  for spec in "${SCN[@]}"; do set -- $spec; t=$1; shift
    o=F7-02_short_${m}_s${s}_$t
    [ -f results/$o/errors.npz ] || { $PY run_aerialvl.py --feats feats/ft/${m}_s$s.npz --split test "$@" --n_noise 5 \
      --methods $ME --workers 11 --n_boot 200 --tag $o > results/$o.log 2>&1 && echo "ok $o" || echo "FAIL $o"; }
    o=F7-02_long_${m}_s${s}_$t
    [ -f results/$o/errors.npz ] || { $PY run_aerialvl.py --feats feats/ft/merged/${m}_s$s.npz --calib_from feats/ft/${m}_s$s.npz \
      --split test_long "$@" --win_step 60 --n_noise 3 --methods $ME --workers 11 --n_boot 200 --tag $o > results/$o.log 2>&1 \
      && echo "ok $o" || echo "FAIL $o"; }
  done
done; done
echo F7_TEST_DONE
