# -*- coding: utf-8 -*-

from __future__ import print_function, division
import argparse
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.backends.cudnn as cudnn
import numpy as np
from torchvision import datasets, transforms
import time
import os
import sys
import scipy.io
import yaml
import math
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

# Add current directory and parent to sys.path to ensure module imports work smoothly
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from tool.utils import load_network


def get_parse():
    parser = argparse.ArgumentParser(description='DenseUAV Testing and Feature Extraction')
    parser.add_argument('--gpu_ids', default='0', type=str,
                        help='gpu_ids: e.g. 0  0,1,2  0,2  or -1 for CPU')
    parser.add_argument('--name', default='baseline_vits_single',
                        type=str, help='model / checkpoint directory name')
    parser.add_argument('--checkpoint', default='net_119.pth',
                        type=str, help='checkpoint weights file name')
    parser.add_argument('--test_dir', default='',
                        type=str, help='test dataset directory path')
    parser.add_argument('--batchsize', default=64, type=int, help='inference batch size')
    parser.add_argument('--h', default=224, type=int, help='input height')
    parser.add_argument('--w', default=224, type=int, help='input width')
    parser.add_argument('--ms', default='1', type=str,
                        help='multiple_scale: e.g. 1 1,1.1  1,1.1,1.2')
    parser.add_argument('--num_worker', default=2, type=int, help='dataloader num_workers')
    parser.add_argument('--mode', default=1, type=int,
                        help='1: drone -> satellite | 2: satellite -> drone')
    parser.add_argument('--eval', action='store_true', default=True,
                        help='automatically compute evaluation metrics after extraction')
    return parser


def resolve_paths(opt):
    """Find correct absolute or relative paths for checkpoint and dataset."""
    # Resolve checkpoint dir
    if not os.path.exists(os.path.join('checkpoints', opt.name)) and os.path.exists(os.path.join(CURRENT_DIR, 'checkpoints', opt.name)):
        opt.checkpoint_dir = os.path.join(CURRENT_DIR, 'checkpoints', opt.name)
    else:
        opt.checkpoint_dir = os.path.join('checkpoints', opt.name)

    # Load opts.yaml config from checkpoint directory if available
    config_path = os.path.join(opt.checkpoint_dir, 'opts.yaml')
    if os.path.exists(config_path):
        with open(config_path, 'r') as stream:
            config = yaml.load(stream, Loader=yaml.FullLoader)
        # Preserve specific test CLI overrides
        preserved = {'batchsize', 'num_worker', 'test_dir', 'checkpoint', 'gpu_ids', 'mode', 'eval'}
        for cfg, value in config.items():
            if cfg not in preserved or not getattr(opt, cfg, None):
                setattr(opt, cfg, value)

    # Resolve test_dir
    if not opt.test_dir:
        candidate_paths = [
            os.path.join('datasets', 'DenseUAV', 'test'),
            os.path.join(CURRENT_DIR, 'datasets', 'DenseUAV', 'test'),
            os.path.join(os.path.dirname(CURRENT_DIR), 'datasets', 'DenseUAV', 'test')
        ]
        for p in candidate_paths:
            if os.path.exists(p):
                opt.test_dir = p
                break
        if not opt.test_dir:
            opt.test_dir = os.path.join('datasets', 'DenseUAV', 'test')

    return opt


def fliplr(img):
    '''flip horizontal'''
    inv_idx = torch.arange(img.size(3) - 1, -1, -1).long()
    return img.index_select(3, inv_idx)


def which_view(name):
    if 'satellite' in name:
        return 1
    elif 'street' in name:
        return 2
    elif 'drone' in name:
        return 3
    return -1


def extract_feature(model, dataloader, view_index, use_gpu=True, block=2):
    features = torch.FloatTensor()
    for data in tqdm(dataloader, desc=f"Extracting view {view_index}"):
        img, _ = data
        for i in range(2):
            if i == 1:
                img = fliplr(img)
            input_img = Variable(img.cuda() if use_gpu else img)
            if view_index == 1:
                outputs, _ = model(input_img, None)
            elif view_index == 3:
                _, outputs = model(None, input_img)
            else:
                outputs, _ = model(input_img, None)
            
            outputs = outputs[1]
            if i == 0:
                ff = outputs
            else:
                ff += outputs

        # normalize feature
        if len(ff.shape) == 3:
            fnorm = torch.norm(ff, p=2, dim=1, keepdim=True) * np.sqrt(block)
            ff = ff.div(fnorm.expand_as(ff))
            ff = ff.view(ff.size(0), -1)
        else:
            fnorm = torch.norm(ff, p=2, dim=1, keepdim=True)
            ff = ff.div(fnorm.expand_as(ff))

        features = torch.cat((features, ff.data.cpu()), 0)
    return features


def get_id(img_path):
    labels = []
    paths = []
    for path, _ in img_path:
        folder_name = os.path.basename(os.path.dirname(path))
        labels.append(int(folder_name))
        paths.append(path)
    return np.array(labels), paths


def compute_mAP(index, good_index, junk_index):
    ap = 0
    cmc = torch.IntTensor(len(index)).zero_()
    if good_index.size == 0:
        cmc[0] = -1
        return ap, cmc

    mask = np.in1d(index, junk_index, invert=True)
    index = index[mask]

    ngood = len(good_index)
    mask = np.in1d(index, good_index)
    rows_good = np.argwhere(mask == True).flatten()

    cmc[rows_good[0]:] = 1
    for i in range(ngood):
        d_recall = 1.0 / ngood
        precision = (i + 1) * 1.0 / (rows_good[i] + 1)
        if rows_good[i] != 0:
            old_precision = i * 1.0 / rows_good[i]
        else:
            old_precision = 1.0
        ap = ap + d_recall * (old_precision + precision) / 2

    return ap, cmc


def evaluate_retrieval(query_feature, query_label, gallery_feature, gallery_label, use_gpu=True):
    print('\n------- Computing Retrieval Evaluation (Recall@K, mAP) -------')
    if use_gpu and torch.cuda.is_available():
        query_feature = query_feature.cuda()
        gallery_feature = gallery_feature.cuda()

    CMC = torch.IntTensor(len(gallery_label)).zero_()
    ap = 0.0
    num_queries = len(query_label)

    for i in tqdm(range(num_queries), desc="Evaluating queries"):
        query = query_feature[i].view(-1, 1)
        score = torch.mm(gallery_feature, query).squeeze(1).cpu().numpy()
        index = np.argsort(score)[::-1]

        good_index = np.argwhere(gallery_label == query_label[i])
        junk_index = np.argwhere(gallery_label == -1)

        ap_tmp, CMC_tmp = compute_mAP(index, good_index, junk_index)
        if CMC_tmp[0] == -1:
            continue
        CMC = CMC + CMC_tmp
        ap += ap_tmp

    CMC = CMC.float() / num_queries
    top1_percent = round(len(gallery_label) * 0.01)
    r1 = CMC[0].item() * 100
    r5 = CMC[4].item() * 100 if len(CMC) > 4 else 0.0
    r10 = CMC[9].item() * 100 if len(CMC) > 9 else 0.0
    rtop1 = CMC[top1_percent].item() * 100 if len(CMC) > top1_percent else 0.0
    map_score = (ap / num_queries) * 100

    info = f"Recall@1: {r1:.2f}% | Recall@5: {r5:.2f}% | Recall@10: {r10:.2f}% | Recall@top1%: {rtop1:.2f}% | AP (mAP): {map_score:.2f}%"
    print("\n" + "=" * 75)
    print(f"[*] EVALUATION RESULT [{info}]")
    print("=" * 75)

    with open("results.txt", "w") as f:
        f.write(info + "\n")
    return info


def main():
    parser = get_parse()
    opt = parser.parse_args()
    opt = resolve_paths(opt)

    print(f"[INFO] Model: {opt.name}")
    print(f"[INFO] Checkpoint: {opt.checkpoint}")
    print(f"[INFO] Test Directory: {opt.test_dir}")
    print(f"[INFO] Input Size: {opt.h}x{opt.w}")

    # GPU configuration
    str_ids = str(opt.gpu_ids).split(',')
    gpu_ids = [int(i) for i in str_ids if int(i) >= 0]
    use_gpu = torch.cuda.is_available() and len(gpu_ids) > 0

    if use_gpu:
        torch.cuda.set_device(gpu_ids[0])
        cudnn.benchmark = True
        print(f"[INFO] Using GPU: {torch.cuda.get_device_name(gpu_ids[0])}")
    else:
        print("[INFO] Using CPU mode")

    data_transforms = transforms.Compose([
        transforms.Resize((opt.h, opt.w), interpolation=3),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    data_query_transforms = transforms.Compose([
        transforms.Resize((opt.h, opt.w), interpolation=3),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    if opt.mode == 1:
        query_name = 'query_drone'
        gallery_name = 'gallery_satellite'
    elif opt.mode == 2:
        query_name = 'query_satellite'
        gallery_name = 'gallery_drone'
    else:
        raise ValueError(f"Invalid mode: {opt.mode}. Choose 1 or 2.")

    query_dataset_path = os.path.join(opt.test_dir, query_name)
    gallery_dataset_path = os.path.join(opt.test_dir, gallery_name)

    if not os.path.exists(query_dataset_path) or not os.path.exists(gallery_dataset_path):
        raise FileNotFoundError(
            f"Test folders not found in {opt.test_dir}. "
            f"Please verify {query_name} and {gallery_name} exist."
        )

    image_datasets = {
        query_name: datasets.ImageFolder(query_dataset_path, data_query_transforms),
        gallery_name: datasets.ImageFolder(gallery_dataset_path, data_transforms)
    }

    dataloaders = {
        x: torch.utils.data.DataLoader(
            image_datasets[x],
            batch_size=opt.batchsize,
            shuffle=False,
            num_workers=opt.num_worker,
            pin_memory=use_gpu
        )
        for x in [gallery_name, query_name]
    }

    # Load Model
    print('\n[INFO] Loading model weights...')
    model = load_network(opt)
    model = model.eval()
    if use_gpu:
        model = model.cuda()

    which_gallery = which_view(gallery_name)
    which_query = which_view(query_name)
    print(f"[INFO] Direction: {query_name} ({which_query}) -> {gallery_name} ({which_gallery})")

    gallery_label, gallery_path = get_id(image_datasets[gallery_name].imgs)
    query_label, query_path = get_id(image_datasets[query_name].imgs)

    since = time.time()
    with torch.no_grad():
        block_val = getattr(opt, 'block', 2)
        query_feature = extract_feature(model, dataloaders[query_name], which_query, use_gpu=use_gpu, block=block_val)
        gallery_feature = extract_feature(model, dataloaders[gallery_name], which_gallery, use_gpu=use_gpu, block=block_val)

    time_elapsed = time.time() - since
    time_str = f'Feature extraction completed in {time_elapsed // 60:.0f}m {time_elapsed % 60:.0f}s'
    print(f"\n[INFO] {time_str}")

    with open('inference_time.txt', 'w') as f:
        f.write(time_str + '\n')

    # Save to Matlab format (interface for eval_metrics.py)
    mat_filename = f'pytorch_result_{opt.mode}.mat'
    result = {
        'gallery_f': gallery_feature.numpy(),
        'gallery_label': gallery_label,
        'gallery_path': gallery_path,
        'query_f': query_feature.numpy(),
        'query_label': query_label,
        'query_path': query_path
    }
    scipy.io.savemat(mat_filename, result)
    print(f"[SUCCESS] Saved extracted features to {mat_filename}")

    # Evaluate retrieval metrics
    if opt.eval:
        evaluate_retrieval(query_feature, query_label, gallery_feature, gallery_label, use_gpu=use_gpu)


if __name__ == "__main__":
    main()
