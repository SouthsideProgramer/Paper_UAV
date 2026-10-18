#!/usr/bin/env bash
# F8-01: MH-EKF v3 ablation on TEST (analysis only, design not re-selected). One factor per variant.
# Reference (v3) errors come from F7-02 / F5-04 / F5-05 / F3-09 (same runs).
cd "$(dirname "$0")"
PY=/home/aclab_pc/miniconda3/envs/adas-observer/bin/python
GPS=../../datasets/DenseUAV/Dense_GPS_ALL.txt; C=../../../DenseUAV_b8de187/checkpoints
declare -A V=(
  [max1]='"mh_max": 1' [max3]='"mh_max": 3' [max5]='"mh_max": 5' [max20]='"mh_max": 20'
  [k1]='"mh_topk": 1' [k3]='"mh_topk": 3' [k5]='"mh_topk": 5'
  [gate599]='"mh_gate": 5.99' [gate1382]='"mh_gate": 13.82' [gateinf]='"mh_gate": 1e12'
  [noreacq]='"n_reacq": 1000000000' [reachoff]='"mh_reach": false' [vmax10]='"v_max": 10.0' [bestchild]='"mh_lost_rule": "best_child"')
SCN=("vio --motion vio" "imu --motion imu" "init300 --motion vio --init_err 300" "imuinit300 --motion imu --init_err 300")
for v in max1 k1 gateinf noreacq reachoff bestchild vmax10 max3 max5 max20 k3 k5 gate599 gate1382; do
  for s in 666 667 668; do for spec in "${SCN[@]}"; do set -- $spec; t=$1; shift
    for fe in ft zs; do
      F=feats/ft; [ $fe = zs ] && F=feats
      o=F8_short${fe}_${v}_lpn_s${s}_$t
      [ -f aerialvl/results/$o/errors.npz ] || (cd aerialvl && $PY run_aerialvl.py --feats $F/lpn_s$s.npz --split test "$@" --n_noise 5 \
        --methods mh_ekf --cfg "{${V[$v]}}" --workers 11 --n_boot 50 --tag $o > results/$o.log 2>&1) && echo "ok $o" || echo "FAIL $o"
      o=F8_long${fe}_${v}_lpn_s${s}_$t
      [ -f aerialvl/results/$o/errors.npz ] || (cd aerialvl && $PY run_aerialvl.py --feats $F/merged/lpn_s$s.npz --calib_from $F/lpn_s$s.npz \
        --split test_long "$@" --win_step 60 --n_noise 3 --methods mh_ekf --cfg "{${V[$v]}}" --workers 11 --n_boot 50 --tag $o > results/$o.log 2>&1) \
        && echo "ok $o" || echo "FAIL $o"
    done
    [ $s = 666 ] && MAT=$C/lpn/pytorch_result_1.mat || MAT=$C/lpn_s$s/pytorch_result_1.mat
    VD="${V[$v]}"; [[ $VD == *v_max* ]] || VD="$VD, \"v_max\": 0.0"
    o=F8_dense_${v}_lpn_s${s}_t0_$t
    [ -f prototype/results/$o/errors.npz ] || (cd prototype && $PY run_f2.py --world real --gps_path $GPS --result_mat $MAT --campuses test "$@" \
      --cfg "{$VD}" --methods mh_ekf --seed 0 --workers 11 --n_boot 50 --tag $o > results/$o.log 2>&1) && echo "ok $o" || echo "FAIL $o"
  done; done
done
echo F8_ABL_DONE
