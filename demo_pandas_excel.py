#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/24 16:14
# @Author : way
# @Site : 
# @Describe: pandas 操作 Excel

import pandas as pd

filepath = r"./files/1.xlsx"

# 覆盖写入
data = {
    'name': ['张三', '李四'],
    'sex': ['男', '女'],
    'age': [25, 25],
}
df = pd.DataFrame(data)
df.to_excel(filepath, columns=['name', 'sex', 'age'], index=False)

# 读、删、改
df2 = pd.read_excel(filepath, sheet_name=0)
print(df2)
# print(df2 )
# print(df2.head(1))  # 查看前面几条
# print(df2.values[0])  # 查看第一行
# print(df2['age'].values)  # 查看 age 列
df2.replace(25, 50, inplace=True)  # 批量替换修改值
df2.loc[0, 'age'] = 80  # 修改某个值
df2.loc[len(df2)] = ['王五', '男', 5]  # 增加行
df2.loc[len(df2)] = ['王五', '男', 5]
df2.drop_duplicates(inplace=True)  # 去重
df2.drop(index=0, inplace=True)  # 删除行
df2.drop('age', axis=1, inplace=True)  # 删除列
df2['city'] = 'Amony'  # 增加列
print(df2)

# 将修改写入另一个 sheet
with pd.ExcelWriter(filepath) as writer:
    df.to_excel(excel_writer=writer, sheet_name='Sheet1', columns=['name', 'sex', 'age'], index=False)
    df2.to_excel(excel_writer=writer, sheet_name='Sheet2', index=False)
    writer.save()

# 先造 10个excel
from faker import Faker

f = Faker(locale='zh_CN')
for i in range(10):
    items = {
        'name': [f.name() for _ in range(5)],
        'job': [f.job() for _ in range(5)],
        'phone_number': [f.phone_number() for _ in range(5)],
    }
    df = pd.DataFrame(items)
    df.to_excel(f"./files/fake{i}.xlsx", index=False)

# 合并 10个excel
frames = []
for i in range(10):
    df2 = pd.read_excel(f"./files/fake{i}.xlsx", sheet_name=0)
    frames.append(df2)
result = pd.concat(frames)
result.to_excel("./files/total.xlsx", index=False)
