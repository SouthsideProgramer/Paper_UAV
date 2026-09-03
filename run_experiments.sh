#!/bin/bash
set -uo pipefail

PY=/home/internship/miniconda3/envs/denseuav/bin/python
ROOT=/home/internship/thang2/DenseUAV
DATA_DIR=$ROOT/train
TEST_DIR=$ROOT/test
GPU=0

run_config () {
  name=$1
  backbone=$2
  head=$3

  echo "=========================================="
  echo "[$(date)] START $name (backbone=$backbone head=$head)"
  echo "=========================================="

  cd $ROOT
  $PY train.py --name $name --data_dir $DATA_DIR --gpu_ids $GPU --sample_num 1 \
      --block 1 --lr 0.01 --num_worker 8 --head $head --head_pool avg \
      --num_bottleneck 512 --backbone $backbone --h 224 --w 224 --batchsize 16 \
      --load_from no --ra satellite --re satellite --cj no --rr uav \
      --cls_loss CELoss --feature_loss WeightedSoftTripletLoss --kl_loss KLLoss

  if [ ! -d "$ROOT/checkpoints/$name" ]; then
    echo "[$(date)] FAILED train for $name (no checkpoint dir) - skipping eval"
    return
  fi

  cd $ROOT/checkpoints/$name
  $PY $ROOT/test.py --name $name --test_dir $TEST_DIR --gpu_ids $GPU --num_worker 4 --h 224 --w 224
  $PY $ROOT/evaluate_gpu.py
  $PY $ROOT/evaluateDistance.py --root_dir $ROOT
  $PY $ROOT/evaluateMA.py --root_dir $ROOT

  echo "[$(date)] DONE $name"
}

run_config baseline_vits_single ViTS-224 SingleBranch
run_config vits_lpn             ViTS-224 LPN
run_config vits_fsra            ViTS-224 FSRA
run_config resnet50_single      resnet50 SingleBranchCNN

echo "[$(date)] ALL EXPERIMENTS DONE"
