#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/19 10:16
# @Author : way
# @Site : 
# @Describe: 重试装饰器

# 不带传参装饰器
def retry1(func):
    max_retry = 3

    def run(*args, **kwargs):
        for i in range(max_retry + 1):
            if i > 0:
                print(f"尝试第{i}次执行...")
            if func(*args, **kwargs):
                break

    return run


# 带传参装饰器
def retry2(*args, **kwargs):
    max_retry = kwargs.get('max_retry', 3)

    def warpp(func):
        def run(*args, **kwargs):
            for i in range(max_retry + 1):
                if i > 0:
                    print(f"尝试第{i}次执行...")
                if func(*args, **kwargs):
                    break

        return run

    return warpp


@retry1
def do1(spider):
    print(spider)
    return False


@retry2(max_retry=5)
def do2(spider):
    print(spider)
    return False


do1('zhifang')

do2('zhifang2')
