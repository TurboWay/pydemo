#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/15 9:44
# @Author : way
# @Site :  https://docs.python.org/zh-cn/3.6/library/tempfile.html
# @Describe: 优雅地处理临时文件

import tempfile

# 临时文件 方法1 - 主动关闭，关闭即销毁
f = tempfile.TemporaryFile()
f.write(b'123')
f.seek(0)
print(f.read())
f.close()

# 临时文件 方法2 - 自动销毁
with tempfile.TemporaryFile(mode='w+') as f:
    f.write('123\n123')
    f.seek(0)
    print(f.read())

# 临时文件夹 自动销毁，包括文件夹底下的文件
with tempfile.TemporaryDirectory() as tmpdirname:
    with open(f'{tmpdirname}\\test.txt', 'w') as f:
        f.write('123')
    print('created temporary directory', tmpdirname)