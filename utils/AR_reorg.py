import shutil
import os
import json


def rename_dir(inp_fp):
    for root, dirs, files in os.walk(inp_fp):
        fd = root.split('/')[-1]
        if fd.startswith('p'):
            if len(fd) == 4:
                continue
            elif len(fd) == 3:
                new_fd = fd[0] + '0' + fd[1:]
            elif len(fd) == 2:
                new_fd = fd[0] + '00' + fd[1:]
            new_root = root.replace(fd, new_fd)
            os.rename(root,new_root)


def pair_img(train_fp):
    cnt = 1
    new_root = '../datasets/AR_database_60_43_reorg'
    for root, dirs, files in sorted(os.walk(train_fp)):
        for f in files:
            if cnt <= 500:
                mode = 'train'
            elif cnt <= 600:
                mode = 'test'
            else:
                mode = 'val'
            
            new_dir = os.path.join(new_root, mode, str(cnt).zfill(3))
            os.makedirs(new_dir)
            train_fp = os.path.join(root, f)
            test_fp = train_fp.replace('train','test')
            train_name = '_'.join(train_fp.split('/')[-3:])
            test_name = '_'.join(test_fp.split('/')[-3:])
            dst1 = os.path.join(new_dir, '_'.join(train_fp.split('/')[-3:]))
            dst2 = os.path.join(new_dir, '_'.join(test_fp.split('/')[-3:]))
            shutil.copy(train_fp, dst1)
            shutil.copy(test_fp, dst2)
            cnt += 1


if __name__ == '__main__':
    #inp_fp = '../datasets/AR_database_60_43'
    #rename_dir(inp_fp)
    train_fp = '../datasets/AR_database_60_43/train'
    test_fp = '../datasets/AR_database_60_43/test'
    pair_img(train_fp)


