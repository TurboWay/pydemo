#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/12 11:31
# @Author : way
# @Site : 
# @Describe: numpy 类型练习

# https://blog.csdn.net/weixin_37887248/article/details/81744755

import numpy as np

# 零维张量 = 标量 = 对象
n0 = 1

# 一维张量 = 向量 = 列表
n1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.int16)
# print(n1.shape[0])

# 二维张量 = 矩阵 = 嵌套一层的列表
n2 = np.array([
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
])

# 三维张量 = 矩阵 = 嵌套二层的列表
n3 = np.array([
    [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ],
    [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
])

# 张量形状
# print(' x '.join([str(i) for i in n1.shape]))
# print(' x '.join([str(i) for i in n2.shape]))
# print(' x '.join([str(i) for i in n3.shape]))

# 常用方法，多维张量可以指定 计算纬度
# print(n1, n1.sum(axis=0), n1.min(), n1.max(), n1.argmin(), n1.argmax(), )
# print(n2, n2.sum(axis=1), n2.min(), n2.max(), n2.argmin(), n2.argmax(), )
# print(n3, n3.sum(axis=2), n3.min(), n3.max(), n3.argmin(), n3.argmax(), )

# 重塑成新对象 公用内存
# 拆分成 二维张量
n12 = n1.reshape((2, -1))
n1[0] = 333
print(n12)

# 拆分成 五维张量
n31 = n3.reshape((5, -1))
print(n31)


