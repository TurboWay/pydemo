#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/10 14:59
# @Author : way
# @Site : 
# @Describe: 多线程并发 + 进度条

import time
import queue
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed


# 多线程 + map (无返回结果)
def threads_map():
    def func(i):
        time.sleep(2)
        print(i)

    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(func, range(50))
        pool.shutdown(wait=True)


# 多线程 + map (多参数、有返回结果)
def threads_map_return():
    def func(a, b):
        time.sleep(2)
        return a + b

    targets = [
        (1, 5), (7, 8), (6, 8)
    ]

    with ThreadPoolExecutor(max_workers=10) as pool:
        for s in pool.map(func, *zip(*targets)):
            print(s)


# 多线程 + 进度条
def threads_tqdm():
    def func(a):
        time.sleep(a)

    with ThreadPoolExecutor(max_workers=10) as pool:
        tasks = [pool.submit(func, i) for i in range(10)]
        for _ in tqdm(as_completed(tasks), desc='处理中...', total=len(tasks)):
            ...


# 多线程 + 进度条(有返回值)
def threads_tqdm_return():
    def func(a, b):
        time.sleep(2)
        return a + b

    with ThreadPoolExecutor(max_workers=10) as pool:
        tasks = [pool.submit(func, *(i, i)) for i in range(50)]
        for r in tqdm(as_completed(tasks), desc='处理中...', total=len(tasks)):
            print(r.result())


# 重写 ThreadPoolExecutor 增加队列大小限制
class BoundThreadPoolExecutor(ThreadPoolExecutor):

    def __init__(self, max_queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._work_queue = queue.Queue(max_queue)


# 多线程(任务数很大时，限制线程池队列大小，防止内存飙升)
def threads_queue():
    def func(i):
        print(i)

    num = 10
    with BoundThreadPoolExecutor(max_queue=num * 2, max_workers=num) as pool:
        for i in range(1000000):
            pool.submit(func, i)
        pool.shutdown(wait=True)
