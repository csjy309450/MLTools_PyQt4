#! /usr/bin/python2.7
# -*-encoding=utf-8-*-

import numpy as np
import scipy.io as sio
import DocManager.DocManager as dm
import re
import os

def npy2mat(npy_dir, mat_dir, _pattern=None, _docFilter=['.npy']):
    gdm = dm.DocManager(_docFilter)
    filelist = gdm.GetFileList(npy_dir)
    filelist.sort()
    for _name in filelist:
        if re.match(_pattern, _name):
            data = np.load(npy_dir+_name)
            mat_name, _ = os.path.splitext(_name)
            sio.savemat(mat_dir+mat_name, {'point': data})

def mat2npy(mat_dir, npy_dir, _pattern=None, _docFilter=['.mat']):
    gdm = dm.DocManager(_docFilter)
    filelist = gdm.GetFileList(mat_dir)
    filelist.sort()
    for _name in filelist:
        if re.match(_pattern, _name):
            data = sio.loadmat(mat_dir+_name)
            npy_name, _ = os.path.splitext(_name)
            np.save(npy_dir+npy_name, data['point'])

def load_mat(mat_path, var_name):
    """
    读取.mat文件并以list返回矩阵数组
    :param mat_path: ./mat文件路径
    :param var_name: 要提取的数组变量的名称
    :return: 
    """
    data = sio.loadmat(mat_path)
    mat = data[var_name]
    lmat = []
    for it in mat:
        lmat.append(list(it))
    return lmat

def save_mat(data ,mat_path):
    """
    将data中的数据以.mat文件保存
    :param mat_path: ./mat文件路径
    :param data: 要存入文件的数据，要求是dict数据结构
    :return: 
    """
    assert(type(data) is dict)
    np.save(mat_path, data)


if __name__=='__main__':
    npy_dir = '/home/yz/testData/ucsd/labels/vidf1_33_000.y/test_npy/'
    mat_dir = '/home/yz/testData/ucsd/labels/vidf1_33_000.y/point_mat/'
    _pattern = 'vidf1_33_000_f[0-9]{3}_point_label.mat'
    # mat2npy(mat_dir, npy_dir, _pattern)
    # data = np.load('/home/yz/testData/ucsd/labels/vidf1_33_000.y/test_npy/vidf1_33_000_f001_point_label.npy')
    load_mat('/home/yz/testData/ucsd/labels/vidf1_33_000.y/gaussain_mat/vidf1_33_000_f001_gaussian_label.mat',
             'gaussian_labe_data')
    pass
