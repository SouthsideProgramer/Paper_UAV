#!/usr/bin/env bash
# F4: AerialVL sequence part (11 flights + geo-referenced maps), HF hmf21/AerialVL, ~58 GB split zip.
cd "$(dirname "$0")/VAL"
for i in $(seq -w 1 27); do
  f=VAL.zip.0$i
  wget -q -c https://huggingface.co/datasets/hmf21/AerialVL/resolve/main/images/VAL/$f && echo "[$(date +%T)] ok $f" || echo "[$(date +%T)] FAIL $f"
done
echo DOWNLOAD_DONE
