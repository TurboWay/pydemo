#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/10 15:03
# @Author : way
# @Site : 
# @Describe: 自动更新 md 索引


md = """# pydemo
记录一些日常用的 python demo

## list

| demo | 功能  | 
| ------------ | ------------ |
"""

import re
import os

for demo in os.listdir():
    if demo.startswith('demo'):
        with open(demo, 'r', encoding='utf-8') as f:
            desc = re.findall("@Describe:(.*)", f.read())
        desc = desc[0].strip() if desc else ''
        str = f"| [{demo}]({demo})       | {desc} |\n"
        md += str

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(md)