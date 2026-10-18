#!/usr/bin/env bash
# F3 — fusion trên retrieval THẬT (DenseUAV). Chạy trên server ML4U, xem Running_On_Server.md.
# Cách dùng:
#   bash run_f3_server.sh <Dense_GPS_ALL.txt> <pytorch_result_1.mat> [<pytorch_result_1.mat> ...]
# Mỗi .mat (LPN, FSRA, ViT-S, ...) cho ra results/F3_<tên checkpoint>_{vio,imu,init300}_val/.
# Chỉ chạy seed 0 (val). Seed 1 (test) chỉ chạy khi cấu hình đã chốt.
set -euo pipefail
cd "$(dirname "$0")"
GPS="$1"; shift
PY="${PY:-python}"
"$PY" -c "import scipy, numpy, matplotlib" || { echo "Cần scipy + numpy + matplotlib"; exit 1; }
for MAT in "$@"; do
  NAME=$(basename "$(dirname "$MAT")")
  echo "=================== $NAME ($MAT)"
  sha256sum "$MAT" | cut -c1-16
  "$PY" run_f2.py --world real --gps_path "$GPS" --result_mat "$MAT" --motion vio --seed 0 --tag "F3_${NAME}_vio_val"
  "$PY" run_f2.py --world real --gps_path "$GPS" --result_mat "$MAT" --motion imu --seed 0 --tag "F3_${NAME}_imu_val"
  "$PY" run_f2.py --world real --gps_path "$GPS" --result_mat "$MAT" --motion vio --init_err 300 --seed 0 --tag "F3_${NAME}_init300_val"
  for T in vio imu init300; do
    "$PY" analyze_f2.py "results/F3_${NAME}_${T}_val" ekf_gated retrieval_top1 pf_topk ekf_gated ekf_topk_nn ekf_gated
  done
done 2>&1 | tee results/F3_log.txt
