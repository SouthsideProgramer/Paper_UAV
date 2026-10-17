#!/usr/bin/env bash
# F7-02: fine-tune the 9 retrieval checkpoints with the recipe frozen in F7-01 (LR below; epoch picked on val 03-11
# per model), then AerialVL features for all flights (short: in place; long: unzip one flight, extract, delete).
set -u
cd "$(dirname "$0")"
LR=${LR:?set LR}
PY=/home/aclab_pc/.venvs/denseuav/bin/python; C=/home/aclab_pc/Desktop/Paper_UAV/DenseUAV_b8de187/checkpoints
D=../../datasets/AerialVL; FT=$PWD/ft; OUT=$PWD/feats/ft
mkdir -p $OUT/long $OUT/merged
for m in baseline lpn fsra; do for s in 666 667 668; do
  d=$C/$m; [ $s != 666 ] && d=$C/${m}_s$s
  [ -f $FT/${m}_s$s/ft_log.json ] || $PY ft_train.py --ckpt_dir $d --out_dir $FT/${m}_s$s --lr $LR 2>&1 \
     | grep --line-buffered -E "EP|INFO|Error" > $FT/${m}_s$s.log
  echo "[$(date +%T)] trained ${m}_s$s: $(tail -1 $FT/${m}_s$s.log)"
  [ -f $OUT/${m}_s$s.npz ] || $PY aerialvl_extract.py --ckpt_dir $FT/${m}_s$s --root $D/extracted --out $OUT/${m}_s$s.npz 2>&1 | grep -E "wrote|Error"
done; done
LONG="2023-03-16-18-04-01 2023-03-18-12-18-25 2023-03-18-12-47-05 2023-03-18-14-38-32 2023-03-18-15-01-14 2023-03-18-15-40-18"
for seq in $LONG; do
  need=0; for m in baseline lpn fsra; do for s in 666 667 668; do [ -f $OUT/long/${m}_s${s}_$seq.npz ] || need=1; done; done
  [ $need = 0 ] && continue
  (cd $D/VAL && 7z x -y VAL.zip.001 "long_trajtr/$seq/*" -o../extracted > /dev/null) || { echo "UNZIP FAIL $seq"; continue; }
  for m in baseline lpn fsra; do for s in 666 667 668; do
    o=$OUT/long/${m}_s${s}_$seq.npz; [ -f $o ] && continue
    $PY aerialvl_extract.py --ckpt_dir $FT/${m}_s$s --root $D/extracted --seqs "long_trajtr/$seq" \
      --gallery_from $OUT/${m}_s$s.npz --out $o 2>&1 | grep -E "wrote|Error"
  done; done
  rm -rf $D/extracted/long_trajtr/$seq
done
for m in baseline lpn fsra; do for s in 666 667 668; do
  /home/aclab_pc/miniconda3/envs/adas-observer/bin/python merge_feats.py $OUT/${m}_s$s.npz $OUT/merged/${m}_s$s.npz \
    $(for q in $LONG; do echo $OUT/long/${m}_s${s}_$q.npz; done)
done; done
echo F7_02_DONE
