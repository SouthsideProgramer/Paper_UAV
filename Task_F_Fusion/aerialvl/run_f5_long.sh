#!/usr/bin/env bash
# F5-05: the 5 long test-day flights, run once: 9 retrieval models x 4 scenarios, MH-EKF v3 frozen.
cd "$(dirname "$0")"
PY=/home/aclab_pc/miniconda3/envs/adas-observer/bin/python
for m in baseline lpn fsra; do for s in 666 667 668; do
  for spec in "vio --motion vio" "imu --motion imu" "init300 --motion vio --init_err 300" "imuinit300 --motion imu --init_err 300"; do
    set -- $spec; t=$1; shift
    out=F5-05_testlong_${m}_s${s}_$t
    [ -f results/$out/errors.npz ] && continue
    $PY run_aerialvl.py --feats feats/merged/${m}_s$s.npz --calib_from feats/${m}_s$s.npz --split test_long "$@" \
      --win_step 60 --n_noise 3 --workers 11 --tag $out > /dev/null 2>&1 && echo "ok $out" || echo "FAIL $out"
  done
done; done
echo F5_LONG_DONE
