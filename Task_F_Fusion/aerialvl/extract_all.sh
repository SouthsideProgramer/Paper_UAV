#!/usr/bin/env bash
# F5: AerialVL features for all 9 retrieval checkpoints (3 heads x 3 training seeds).
cd "$(dirname "$0")"
C=/home/aclab_pc/Desktop/Paper_UAV/DenseUAV_b8de187/checkpoints
for m in baseline lpn fsra; do for s in 666 667 668; do
  d=$C/$m; [ $s != 666 ] && d=$C/${m}_s$s
  out=$PWD/feats/${m}_s$s.npz
  [ -f $out ] && continue
  /home/aclab_pc/.venvs/denseuav/bin/python aerialvl_extract.py --ckpt_dir $d --root ../../datasets/AerialVL/extracted --out $out 2>&1 | grep INFO
done; done
echo EXTRACT_ALL_DONE
