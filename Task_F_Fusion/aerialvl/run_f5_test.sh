#!/usr/bin/env bash
# F5-04: AerialVL TEST (flights of 2023-03-18), run once: 9 retrieval models x 4 scenarios, MH-EKF v3 frozen.
cd "$(dirname "$0")"
PY=/home/aclab_pc/miniconda3/envs/adas-observer/bin/python
SPLIT=${SPLIT:-test}
for m in baseline lpn fsra; do for s in 666 667 668; do
  f=feats/${m}_s$s.npz
  until [ -f $f ]; do sleep 30; done
  for spec in "vio --motion vio" "imu --motion imu" "init300 --motion vio --init_err 300" "imuinit300 --motion imu --init_err 300"; do
    set -- $spec; t=$1; shift
    out=F5-04_${SPLIT}_${m}_s${s}_$t
    [ -f results/$out/errors.npz ] && continue
    $PY run_aerialvl.py --feats $f --split $SPLIT "$@" --n_noise 5 --workers 10 --tag $out > /dev/null 2>&1 && echo "ok $out" || echo "FAIL $out"
  done
done; done
echo F5_${SPLIT}_DONE
