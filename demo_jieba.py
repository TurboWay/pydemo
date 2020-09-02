#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/1 18:22
# @Author : way
# @Site :
# @Describe: 结巴分词

# import jieba_fast as jieba
import jieba

for i in ('悟空','沙僧','沙和尚','猪八戒','唐僧','唐三藏'):
    jieba.add_word(i)

path = r"C:\Users\Administrator\Desktop\西游记.txt"
with open(path, 'r', encoding='utf-8') as f:
    result = jieba.lcut(f.read())
    new_result = [(i, result.count(i)) for i in set(result) if i in ('悟空','沙僧','沙和尚','猪八戒','唐僧','唐三藏')]
    new_result.sort(key=lambda x:x[1], reverse=True)
    for i in new_result:
        print(i)