#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/10 14:59
# @Author : way
# @Site : 
# @Describe: 多线程并发

import time
from concurrent.futures import ThreadPoolExecutor


def test1(val1, val2):
    print(val1 + val2)
    return True


def test2(val):
    time.sleep(3)
    print(val)


targets = [
    (4, 5),
    (6, 7)
]

num = 10
pool = ThreadPoolExecutor(max_workers=num)
for result in pool.map(test1, *zip(*targets)):
    ...

pool = ThreadPoolExecutor(max_workers=num)
for result in pool.map(test2, range(50)):
    ...
