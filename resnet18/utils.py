#!/usr/bin/env python
# -*- coding:utf-8 -*-


import numpy as np

# 1. 计算数据集(图片)的均值和方差(RGB的3个通道)
def compute_mean_var(image):
    # image.shape: [image_num, w, h, c]
    mean = []
    var  = []
    for c in range(image.shape[-1]):
        mean.append(np.mean(image[:, :, :, c]))
        var.append(np.std(image[:, :, :, c]))
    return mean, var

# 2. 归一化图片
def norm_images(image):
    # image.shape: [image_num, w, h, c]
    image = image.astype('float32')
    mean, var = compute_mean_var(image)
    image[:, :, :, 0] = (image[:, :, :, 0] - mean[0]) / var[0]
    image[:, :, :, 1] = (image[:, :, :, 1] - mean[1]) / var[1]
    image[:, :, :, 2] = (image[:, :, :, 2] - mean[2]) / var[2]
    return image

def normalize(x, mean, std):
    x = (x - mean)/std              
    return x

# 3. 学习率调整
def lr_schedule_200ep(epoch):
    if epoch < 60:
        return 0.1
    if epoch < 120:
        return 0.02
    if epoch < 160:
        return 0.004
    if epoch < 200:
        return 0.0008
    if epoch < 250:
        return 0.0003
    if epoch < 300:
        return 0.0001
    else:
        return 0.00006

# 4. 学习率调整
def lr_schedule_300ep(epoch):
    if epoch < 150:
        return 0.1
    if epoch < 225:
        return 0.01
    if epoch < 300:
        return 0.001
