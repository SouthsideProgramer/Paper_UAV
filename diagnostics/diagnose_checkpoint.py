# -*- coding: utf-8 -*-
"""
diagnose_checkpoint.py — Giai đoạn 0: chẩn đoán một checkpoint (cần torch + timm).

Các bước (mỗi bước in ra [OK] / [WARN]):
  1. Phiên bản môi trường: python, torch, torchvision, timm, CUDA.
  2. opts.yaml: in các tham số quan trọng; --compare_opts để diff với opts.yaml của run khác
     (ví dụ run 82.20% trên máy internship).
  3. Pretrained có thực sự được load không: so norm trọng số backbone timm pretrained=True
     với pretrained=False, và độ gần (cosine) giữa checkpoint với pretrained / random.
  4. Load checkpoint vào model với strict=False, liệt kê missing / unexpected keys.
  5. train.log: số epoch đã chạy, loss đầu/cuối, Drone_Acc / Satellite_Acc cuối.
  6. (tuỳ chọn, --train_dir) R@1 drone->satellite trên một phần tập TRAIN.
     R@1 train thấp  -> lỗi ở khâu huấn luyện / load.
     R@1 train cao nhưng test thấp -> lỗi ở khâu test (hoặc overfit nặng).

Ví dụ:
  python diagnostics/diagnose_checkpoint.py --ckpt_dir checkpoints/baseline_vits_single
  python diagnostics/diagnose_checkpoint.py --ckpt_dir checkpoints/baseline_vits_single \
      --compare_opts /path/to/run_82/opts.yaml --train_dir /data/DenseUAV/train --n_classes 200
"""
import argparse
import os
import re
import sys
import platform

import numpy as np
import torch
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

TIMM_NAME = {
    'ViTS-224': 'vit_small_patch16_224',
    'ViTS-384': 'vit_small_patch16_384',
    'ViTB-224': 'vit_base_patch16_224',
    'resnet50': 'resnet50',
    'senet': 'legacy_seresnet50',
    'DeitS-224': 'deit_small_distilled_patch16_224',
    'Convnext-T': 'convnext_tiny',
}
KEY_OPTS = ['backbone', 'head', 'head_pool', 'block', 'lr', 'batchsize', 'num_epochs', 'h', 'w',
            'num_bottleneck', 'droprate', 'cls_loss', 'feature_loss', 'kl_loss', 'load_from',
            'ra', 're', 'cj', 'rr', 'sample_num', 'autocast', 'warm_epoch', 'nclasses', 'data_dir']


def section(title):
    print('\n' + '=' * 70 + f'\n{title}\n' + '=' * 70)


def check_env():
    section('1. Môi trường')
    import torchvision
    import timm
    print(f'python      {platform.python_version()} ({platform.system()})')
    print(f'torch       {torch.__version__}  cuda={torch.cuda.is_available()}')
    print(f'torchvision {torchvision.__version__}')
    print(f'timm        {timm.__version__}')
    print('[INFO] Bài gốc dùng torch 1.10 / torchvision 0.11; run 82.20% dùng torch 2.0. '
          'requirements.txt không pin timm -> ghi lại phiên bản này vào log.')


def load_opts(path):
    with open(path) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def check_opts(ckpt_dir, compare):
    section('2. opts.yaml')
    opts = load_opts(os.path.join(ckpt_dir, 'opts.yaml'))
    for k in KEY_OPTS:
        print(f'{k:16s} {opts.get(k)}')
    if compare:
        other = load_opts(compare)
        diff = {k: (opts.get(k), other.get(k)) for k in sorted(set(opts) | set(other))
                if opts.get(k) != other.get(k) and k not in ('name', 'gpu_ids', 'use_gpu')}
        print(f'\n--- khác biệt so với {compare} ---')
        for k, (a, b) in diff.items():
            print(f'{k:16s} this={a!r:30s} other={b!r}')
        if not diff:
            print('[OK] không có khác biệt')
    return opts


def flat(sd, prefix=''):
    return torch.cat([v.float().flatten() for k, v in sd.items()
                      if k.startswith(prefix) and v.dtype.is_floating_point])


def check_pretrained_and_ckpt(opts, ckpt_path):
    import timm
    from argparse import Namespace
    from models.taskflow import make_model

    section('3. Pretrained weights')
    name = TIMM_NAME.get(opts['backbone'])
    pre = rnd = None
    if name is None:
        print(f'[SKIP] chưa map backbone {opts["backbone"]} sang tên timm')
    else:
        kw = {'img_size': (opts['h'], opts['w'])} if name.startswith('vit') else {}
        try:
            pre = timm.create_model(name, pretrained=True, **kw).state_dict()
        except Exception as e:
            print(f'[WARN] không tải được pretrained ({e}). Nếu lúc train cũng vậy thì model train từ random!')
        rnd = timm.create_model(name, pretrained=False, **kw).state_dict()
        if pre is not None:
            n_pre, n_rnd = flat(pre).norm().item(), flat(rnd).norm().item()
            print(f'norm pretrained={n_pre:.2f}  norm random={n_rnd:.2f}')
            print('[OK] pretrained khác random' if abs(n_pre - n_rnd) / n_rnd > 0.01
                  else '[WARN] pretrained ~ random: pretrained KHÔNG được load')

    section('4. Checkpoint')
    ckpt = torch.load(ckpt_path, map_location='cpu')
    print(f'{ckpt_path}: {len(ckpt)} tensors')
    opt = Namespace(**opts)
    opt.load_from = 'no'
    model = make_model(opt)
    res = model.load_state_dict(ckpt, strict=False)
    print(f'missing keys    ({len(res.missing_keys)}): {res.missing_keys[:10]}')
    print(f'unexpected keys ({len(res.unexpected_keys)}): {res.unexpected_keys[:10]}')
    if res.missing_keys or res.unexpected_keys:
        print('[WARN] checkpoint không khớp kiến trúc hiện tại (khác timm version / head?)')
    else:
        print('[OK] checkpoint khớp hoàn toàn')

    if pre is not None:
        bb = {k[len('backbone.backbone.'):]: v for k, v in ckpt.items() if k.startswith('backbone.backbone.')}
        common = [k for k in bb if k in pre and bb[k].shape == pre[k].shape and bb[k].dtype.is_floating_point]
        c = torch.cat([bb[k].float().flatten() for k in common])
        p = torch.cat([pre[k].float().flatten() for k in common])
        r = torch.cat([rnd[k].float().flatten() for k in common])
        cos = torch.nn.functional.cosine_similarity
        cp, cr = cos(c, p, dim=0).item(), cos(c, r, dim=0).item()
        print(f'cosine(ckpt backbone, pretrained)={cp:.3f}  cosine(ckpt backbone, random)={cr:.3f}')
        print('[OK] backbone được fine-tune từ pretrained' if cp > 0.5
              else '[WARN] backbone KHÔNG gần pretrained -> có thể đã train từ random init')
    return model


def check_train_log(ckpt_dir):
    section('5. train.log')
    path = os.path.join(ckpt_dir, 'train.log')
    if not os.path.exists(path):
        print('[WARN] không có train.log')
        return
    pat = re.compile(r'Loss: ([\d.]+).*Satellite_Acc: ([\d.]+)\s+Drone_Acc: ([\d.]+)')
    rows = [tuple(map(float, m.groups())) for m in map(pat.search, open(path, errors='ignore')) if m]
    if not rows:
        print('[WARN] không parse được dòng loss nào')
        return
    loss = [r[0] for r in rows]
    print(f'epochs={len(rows)}  loss[0]={loss[0]:.4f}  loss[-1]={loss[-1]:.4f}  min={min(loss):.4f}')
    print(f'Satellite_Acc cuối={rows[-1][1]:.4f}  Drone_Acc cuối={rows[-1][2]:.4f}')
    step = max(1, len(loss) // 10)
    print('loss mỗi ~10%:', ' '.join(f'{x:.3f}' for x in loss[::step]))
    if len(rows) < 120:
        print(f'[WARN] chỉ có {len(rows)} epoch (mặc định 120)')
    if loss[-1] > 0.8 * loss[0]:
        print('[WARN] loss gần như không giảm')


def eval_train_subset(model, opts, train_dir, n_classes, batchsize, use_gpu):
    from PIL import Image
    from torchvision import transforms
    import importlib.util
    # nạp test.py của repo theo đường dẫn (tránh trùng tên với module chuẩn `test`)
    spec = importlib.util.spec_from_file_location('repo_test', os.path.join(ROOT, 'test.py'))
    repo_test = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(repo_test)
    extract_feature = repo_test.extract_feature

    section(f'6. R@1 drone->satellite trên {n_classes} class của tập TRAIN')
    tf = transforms.Compose([
        transforms.Resize((opts['h'], opts['w']), interpolation=3),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    classes = sorted(os.listdir(os.path.join(train_dir, 'drone')))[:n_classes]

    class Folder(torch.utils.data.Dataset):
        def __init__(self, view):
            self.items = [(os.path.join(train_dir, view, c, f), int(c))
                          for c in classes for f in sorted(os.listdir(os.path.join(train_dir, view, c)))]

        def __len__(self):
            return len(self.items)

        def __getitem__(self, i):
            p, y = self.items[i]
            return tf(Image.open(p).convert('RGB')), y

    feats, labels = {}, {}
    model = model.eval().cuda() if use_gpu else model.eval()
    with torch.no_grad():
        for view, idx in (('drone', 3), ('satellite', 1)):
            ds = Folder(view)
            dl = torch.utils.data.DataLoader(ds, batch_size=batchsize, num_workers=2)
            feats[view] = extract_feature(model, dl, idx, use_gpu=use_gpu, block=opts.get('block', 1)).numpy()
            labels[view] = np.array([y for _, y in ds.items])
    score = feats['drone'] @ feats['satellite'].T
    top1 = labels['satellite'][score.argmax(1)]
    r1 = (top1 == labels['drone']).mean() * 100
    print(f'drone={len(labels["drone"])}  satellite={len(labels["satellite"])}  R@1(train subset)={r1:.2f}%')
    print('[INFO] So sánh với R@1 test: train thấp -> lỗi train/load; train cao, test thấp -> lỗi test.')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--ckpt_dir', required=True)
    ap.add_argument('--checkpoint', default='net_119.pth')
    ap.add_argument('--compare_opts', default='', help='opts.yaml của run khác để diff')
    ap.add_argument('--train_dir', default='', help='thư mục train/ (có drone/ và satellite/)')
    ap.add_argument('--n_classes', default=200, type=int)
    ap.add_argument('--batchsize', default=32, type=int)
    ap.add_argument('--cpu', action='store_true')
    args = ap.parse_args()

    check_env()
    opts = check_opts(args.ckpt_dir, args.compare_opts)
    model = check_pretrained_and_ckpt(opts, os.path.join(args.ckpt_dir, args.checkpoint))
    check_train_log(args.ckpt_dir)
    if args.train_dir:
        eval_train_subset(model, opts, args.train_dir, args.n_classes, args.batchsize,
                          use_gpu=torch.cuda.is_available() and not args.cpu)


if __name__ == '__main__':
    main()
