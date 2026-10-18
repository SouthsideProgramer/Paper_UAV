#!/usr/bin/env bash
# F3-08: one retrieval .mat x trajectory seeds x 4 scenarios on the TEST campuses (design frozen).
# usage: bash run_f3_seeds.sh <tag_prefix> <pytorch_result_1.mat> [traj seeds...]
set -u
cd "$(dirname "$0")"
PY=${PY:-/home/aclab_pc/miniconda3/envs/adas-observer/bin/python}
GPS=../../datasets/DenseUAV/Dense_GPS_ALL.txt
TAG=$1; MAT=$2; shift 2; SEEDS=${*:-0 1 2}
for s in $SEEDS; do
  for spec in "vio --motion vio" "imu --motion imu" "init300 --motion vio --init_err 300" "imuinit300 --motion imu --init_err 300"; do
    set -- $spec; t=$1; shift
    out=results/F3-08_${TAG}_t${s}_${t}
    [ -f $out/errors.npz ] && continue
    $PY run_f2.py --world real --gps_path $GPS --result_mat $MAT --campuses test "$@" \
      --methods retrieval_top1,ekf_gated,pf_topk,mh_ekf --seed $s --workers ${WORKERS:-4} --n_boot 200 --tag $(basename $out) > /dev/null 2>&1 \
      && echo "ok $out" || echo "FAIL $out"
  done
done
