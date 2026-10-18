#!/usr/bin/env bash
# Wait for each extra-seed model in stage0_summary.txt, then run its trajectory-seed fusion runs.
cd "$(dirname "$0")"
S=../../../DenseUAV_b8de187/logs/stage0_summary.txt; C=../../../DenseUAV_b8de187/checkpoints
for seed in 667 668; do for m in baseline lpn fsra; do
  until grep -q " ${m}_s${seed}:" $S; do sleep 30; done
  bash run_f3_seeds.sh ${m}_s${seed} $C/${m}_s${seed}/pytorch_result_1.mat 0 1 2
done; done
echo F3_SEEDS_ALL_DONE
