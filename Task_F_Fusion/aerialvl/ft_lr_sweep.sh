#!/usr/bin/env bash
# F7-01: lr sweep on LPN s666, model selection on val 03-11.
cd "$(dirname "$0")"
PY=/home/aclab_pc/.venvs/denseuav/bin/python; C=/home/aclab_pc/Desktop/Paper_UAV/DenseUAV_b8de187/checkpoints
for lr in 1e-5 3e-5 1e-4; do
  [ -f ft/dev_lpn_lr$lr/ft_log.json ] && continue
  $PY ft_train.py --ckpt_dir $C/lpn --out_dir ft/dev_lpn_lr$lr --lr $lr 2>&1 | grep -E "EP|INFO|Error" > ft/dev_lpn_lr$lr.log
done
echo F7_01_DONE
