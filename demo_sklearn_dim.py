#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/7 12:24
# @Author : way
# @Site : 
# @Describe: sklearn 降维

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# 加载数据
iris = datasets.load_iris()
iris_X, iris_Y = iris.data, iris.target
X_train, X_test, Y_train, Y_test = train_test_split(iris_X, iris_Y, train_size=0.3, random_state=20)

# PCA（主成分分析）
pca = PCA(n_components='mle', whiten=False, svd_solver='auto')
pca.fit(iris_X)
reduced_X = pca.transform(iris_X)  # reduced_X为降维后的数据
print('PCA:')
print('降维后的各主成分的方差值占总方差值的比例', pca.explained_variance_ratio_)
print('降维后的各主成分的方差值', pca.explained_variance_)
print('降维后的特征数', pca.n_components_)
print(reduced_X)

# LDA（线性评价分析）
lda = LinearDiscriminantAnalysis(n_components=2)
lda.fit(X_train, Y_train)
reduced_X = lda.transform(iris_X)
print('LDA:')
print('LDA的数据中心点:', lda.means_)  # 中心点
print('LDA做分类时的正确率:', lda.score(X_test, Y_test))  # score是指分类的正确率
print('LDA降维后特征空间的类中心:', lda.scalings_)  # 降维后特征空间的类中心
print(reduced_X)
