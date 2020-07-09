#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/9 17:37
# @Author : way
# @Site : 
# @Describe: 下载 科技爱好者周刊 docs 源码, 遍历生成纯资源 md

import re
import os

dirname = r'C:\Users\Administrator\Desktop\docs'
for file in os.listdir(dirname):
    path = os.path.join(dirname, file)
    head = 'https://github.com/ruanyf/weekly/blob/master/docs/'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        resource = re.findall('(## 工具.*?)##', content, re.S)
        if resource:
            with open('resource.md', 'a', encoding='utf-8') as f2:
                f2.write(resource[0].replace('## 工具', f'##  [工具]({head + file})'))