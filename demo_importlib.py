#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/5 17:25
# @Author : way
# @Site : 
# @Describe: 动态导入包

import importlib

module_name = 'os'
module = importlib.import_module(module_name)
for item in dir(module):
    item = getattr(module, item)
    if isinstance(item, type):
        print(item)
