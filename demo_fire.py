#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/1 10:22
# @Author : way
# @Site : 
# @Describe: python 写命令行工具

# 说明文档 https://github.com/google/python-fire/blob/master/docs/guide.md

import fire
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s: %(message)s', "%Y-%m-%d %H:%M:%S")
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

class Calculator:
    """
    :param a1: 这是一个测试数字1 注释会在 help 中显示
    :param a2: 这是一个测试数字2 注释会在 help 中显示
    """
    def __init__(self, a1=2, a2=0):

        self.a1 = a1
        self.a2 = a2

    def add(self):
        logger.info(f'计算结果为:{self.a1 + self.a2}')

    def multiply(self, x, y):
        return x * y

if __name__ == '__main__':
    fire.Fire(Calculator)
