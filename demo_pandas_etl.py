#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/24 14:16
# @Author : way
# @Site : 
# @Describe: pandas 做数据清洗

import re
import pandas as pd

path = r"files\bj_danke.csv"
clean_path = r"files\bj_danke_etl.csv"
data = pd.read_csv(path)
# data = pd.read_csv(path, header=None)  # 如果第一行就是数据的话

################################################## 数据查看 #########################################################

# 整体数据情况 字段数、数据量(不算空值)、数据类型，内存占用大小
data.info()

# 整体数据预览 行数、列数
# print(data.info)

# 查看前面几条 默认5条
data.head()

# 标题行
title = data.columns

# 第5行
row5 = data.loc[4]

# 第5列
col5 = data.iloc[:, 4]

# group by
unique = data.iloc[:, 3].unique()

# group by count
value_counts = data.iloc[:, 3].value_counts()
# value_counts = data['户型'].value_counts()

################################################## 数据处理 #########################################################
# 异常值清洗
data['户型'].unique()
# print(data[data['户型'] == '户型'])
data = data[data['户型'] != '户型']

# 缺失值处理：直接删除缺失值所在行，并重置索引
# print(data.isnull().sum())
data.dropna(axis=0, inplace=True)
data.reset_index(drop=True, inplace=True)

# 数据重复处理: 删除重复值
# print(data[data.duplicated()])
data.drop_duplicates(inplace=True)
data.reset_index(drop=True, inplace=True)

# 清洗，列替换
data.loc[:, '地铁'] = data['地铁'].apply(lambda x: x.replace('地铁：', ''))

# 增加列
data.loc[:, '所在楼层'] = data['楼层'].apply(lambda x: int(x.split('/')[0]))
data.loc[:, '总楼层'] = data['楼层'].apply(lambda x: int(x.replace('层', '').split('/')[-1]))
data.loc[:, '地铁数'] = data['地铁'].apply(lambda x: len(re.findall('号线', x)))
data.loc[:, '距离地铁距离'] = data['地铁'].apply(lambda x: int(re.findall('(\d+)米', x)[-1]) if re.findall('(\d+)米', x) else None)

# 查看空值
# data[data['距离地铁距离'].isnull()]
# data[data['距离地铁距离'].notnull()]

# 数据过滤
data = data[(data['距离地铁距离'] < 300) & (data['位置1'] == '朝阳区')]


################################################## 数据保存 #########################################################

# 查看保存的数据
print(data.info)

# 保存清洗后的数据
data.to_csv(clean_path, index=False)
