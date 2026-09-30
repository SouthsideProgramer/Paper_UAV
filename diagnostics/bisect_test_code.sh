#!/bin/bash
# bisect_test_code.sh — Giai đoạn 0: tìm thay đổi nào trong commit bbfa61f làm hỏng kết quả test.
#
# Chạy CÙNG MỘT checkpoint qua 5 phiên bản code test, mỗi phiên bản chỉ khác đúng một file:
#   A_orig        : test.py + tool/utils.py + SingleBranch.py của repo gốc (b8de187)
#   B_head        : code hiện tại (HEAD)
#   C_old_test    : HEAD, riêng test.py lấy từ b8de187
#   D_old_utils   : HEAD, riêng tool/utils.py lấy từ b8de187
#   E_old_head    : HEAD, riêng models/Head/SingleBranch.py lấy từ b8de187
# Mỗi phiên bản sinh một .mat trong OUT_DIR, sau đó so sánh R@1 bằng diagnose_mat.py.
#
#   A ≈ B        -> code test không phải nguyên nhân; lỗi nằm ở checkpoint / lần train.
#   A ≫ B        -> phiên bản nào trong C/D/E hồi phục về ≈ A thì file đó là thủ phạm.
#
# Cách dùng:
#   bash diagnostics/bisect_test_code.sh <ROOT>/checkpoints/<name> <TEST_DIR> [OUT_DIR] [GPU]
# CKPT_DIR phải nằm trong thư mục tên "checkpoints" (có opts.yaml và net_119.pth).
set -euo pipefail

CKPT_DIR=$(realpath "$1")
TEST_DIR=$(realpath "$2")
OUT_DIR=$(realpath -m "${3:-diagnostics/bisect_out}")
GPU=${4:-0}
PY=${PY:-python}
BASE=b8de187
CHECKPOINT=${CHECKPOINT:-net_119.pth}

REPO=$(git -C "$(dirname "$0")" rev-parse --show-toplevel)
NAME=$(basename "$CKPT_DIR")
RUN_ROOT=$(dirname "$(dirname "$CKPT_DIR")")   # thư mục chứa checkpoints/
[ "$(basename "$(dirname "$CKPT_DIR")")" = "checkpoints" ] || { echo "CKPT_DIR phải là .../checkpoints/<name>"; exit 1; }
mkdir -p "$OUT_DIR"
WT_BASE=$(mktemp -d)
trap 'for w in "$WT_BASE"/*; do git -C "$REPO" worktree remove --force "$w" 2>/dev/null || true; done; rm -rf "$WT_BASE"' EXIT

make_variant () {   # $1=tên, $2..=file lấy từ BASE (hoặc "ALL")
  local name=$1; shift
  local wt="$WT_BASE/$name"
  git -C "$REPO" worktree add --detach -q "$wt" HEAD
  for f in "$@"; do
    if [ "$f" = "ALL" ]; then
      git -C "$wt" checkout -q $BASE -- test.py tool/utils.py models/Head/SingleBranch.py
    else
      git -C "$wt" checkout -q $BASE -- "$f"
    fi
  done
  echo "$wt"
}

run_old_style () {  # test.py gốc: đọc opts.yaml và checkpoint từ cwd = CKPT_DIR
  local name=$1 wt=$2
  echo "[$(date +%T)] $name (test.py gốc)"
  ( cd "$CKPT_DIR" && PYTHONPATH="$wt" $PY "$wt/test.py" --name "$NAME" --test_dir "$TEST_DIR" \
      --gpu_ids "$GPU" --checkpoint "$CHECKPOINT" ) > "$OUT_DIR/$name.log" 2>&1
  mv "$CKPT_DIR/pytorch_result_1.mat" "$OUT_DIR/$name.mat"
}

run_new_style () {  # test.py mới: tìm checkpoints/<name> từ cwd = RUN_ROOT
  local name=$1 wt=$2
  echo "[$(date +%T)] $name (test.py mới)"
  ( cd "$RUN_ROOT" && PYTHONPATH="$wt" $PY "$wt/test.py" --name "$NAME" --test_dir "$TEST_DIR" \
      --gpu_ids "$GPU" --checkpoint "$CKPT_DIR/$CHECKPOINT" ) > "$OUT_DIR/$name.log" 2>&1
  mv "$RUN_ROOT/pytorch_result_1.mat" "$OUT_DIR/$name.mat"
}

run_old_style A_orig      "$(make_variant A_orig ALL)"
run_new_style B_head      "$(make_variant B_head)"
run_old_style C_old_test  "$(make_variant C_old_test test.py)"
run_new_style D_old_utils "$(make_variant D_old_utils tool/utils.py)"
run_new_style E_old_head  "$(make_variant E_old_head models/Head/SingleBranch.py)"

$PY "$REPO/diagnostics/diagnose_mat.py" "$OUT_DIR"/*.mat --json_out "$OUT_DIR/summary.json"
