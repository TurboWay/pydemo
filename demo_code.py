#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/24 10:49
# @Author : way
# @Site : 
# @Describe: 字符编码处理

text1 = """é\x9d\x9eäººå\x93\x89ç¬¬600è¯\x9d"""
text1 = text1.encode('raw_unicode_escape').decode()
print(text1)

text2 = '\u5403\u9e21\u6218\u573a'
text2 = text2.encode().decode()
print(text2)