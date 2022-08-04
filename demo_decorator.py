#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/19 10:16
# @Author : way
# @Site : 
# @Describe: 重试、计时装饰器

import time


# 计时器
def timer(function):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = function(*args, **kwargs)
        time_end = time.time()
        cost_time = time_end - time_start
        print("花费时间：{}秒".format(cost_time))
        return result

    return wrapper


# 重试装饰器
def retry(func):
    max_retry = 3

    def run(*args, **kwargs):
        for i in range(max_retry + 1):
            if i > 0:
                print(f"尝试第{i}次执行...")
            if func(*args, **kwargs):
                break

    return run


# 重试装饰器(带传参)
def retry_withparam(*args, **kwargs):
    max_retry = kwargs.get('max_retry', 3)

    def warpp(func):
        def run(*args, **kwargs):
            for i in range(max_retry + 1):
                if i > 0:
                    print(f"尝试第{i}次执行...")
                flag = func(*args, **kwargs)
                if flag:
                    return flag

        return run

    return warpp


@timer
def do1(spider):
    return spider


@retry
def do2(spider):
    print(spider)
    return False


@retry_withparam(max_retry=5)
def do3(spider):
    print(spider)
    return False


print(do1("zhifang"))
print(do2("zhifang"))
print(do3("zhifang"))
