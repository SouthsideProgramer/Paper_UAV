#!/usr/bin/env bash
# F5-05: the 6 long AerialVL flights, one at a time (disk is short): unzip one flight, extract features for the
# 9 checkpoints (gallery reused from feats/<model>.npz), delete the images, continue.
cd "$(dirname "$0")"
PY=/home/aclab_pc/.venvs/denseuav/bin/python
C=/home/aclab_pc/Desktop/Paper_UAV/DenseUAV_b8de187/checkpoints
D=../../datasets/AerialVL
until grep -q EXTRACT_ALL_DONE feats/extract_all.log; do sleep 30; done
mkdir -p feats/long
for seq in 2023-03-16-18-04-01 2023-03-18-12-18-25 2023-03-18-12-47-05 2023-03-18-14-38-32 2023-03-18-15-01-14 2023-03-18-15-40-18; do
  done_all=1
  for m in baseline lpn fsra; do for s in 666 667 668; do [ -f feats/long/${m}_s${s}_$seq.npz ] || done_all=0; done; done
  [ $done_all = 1 ] && continue
  (cd $D/VAL && 7z x -y VAL.zip.001 "long_trajtr/$seq/*" -o../extracted > /dev/null) || { echo "UNZIP FAIL $seq"; continue; }
  echo "[$(date +%T)] unzipped $seq: $(ls $D/extracted/long_trajtr/$seq | wc -l) frames"
  for m in baseline lpn fsra; do for s in 666 667 668; do
    d=$C/$m; [ $s != 666 ] && d=$C/${m}_s$s
    out=$PWD/feats/long/${m}_s${s}_$seq.npz
    [ -f $out ] && continue
    $PY aerialvl_extract.py --ckpt_dir $d --root $D/extracted --seqs "long_trajtr/$seq" \
      --gallery_from $PWD/feats/${m}_s$s.npz --out $out 2>&1 | grep -E "wrote|Error" 
  done; done
  rm -rf $D/extracted/long_trajtr/$seq
done
echo EXTRACT_LONG_DONE
