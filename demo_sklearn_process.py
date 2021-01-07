#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/7 12:23
# @Author : way
# @Site : 
# @Describe: sklearn 数据预处理


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, normalize

# 加载数据
iris = datasets.load_iris()
iris_X, iris_Y = iris.data, iris.target
print(iris_X, iris_Y)
print(iris.target_names)
print(iris.feature_names)

# 切分训练集与测试集
X_train, X_test, Y_train, Y_test = train_test_split(iris_X, iris_Y, train_size=0.3, random_state=20)

# 数据预处理

X = [[1, -1, 2], [0, 2, -1], [0, 1, -2]]
# 标准化
scaler = StandardScaler().fit(X)
new_X = scaler.transform(X)
print('基于mean和std的标准化:', new_X)

# 归一化
scaler = MinMaxScaler(feature_range=(0, 1)).fit(X)
new_X = scaler.transform(X)
print('规范化到一定区间内', new_X)

# 标准化
new_X = normalize(X, norm='l2')
print('求二范数', new_X)