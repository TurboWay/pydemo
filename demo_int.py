#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/8 13:16
# @Author : way
# @Site : 
# @Describe: 进制转换

# 十进制 》十六进制
hex(16)
# 十进制 》八进制
oct(16)
# 十进制 》二进制
bin(16)

# 字符串 》十进制
int('10')
# 字符串 》十六进制
int('12',16)
# 字符串 》十六进制
int('0x10',16)
# 字符串 》八进制
int('10',8)
# 字符串 》八进制
int('010',8)
# 字符串 》二进制
int('10',2)

# 中文字符 》 unicode 》十六进制
font = '肥'
unicode_str = font.encode('unicode-escape').decode()
print(unicode_str)
sixteen_str = unicode_str.replace('\\u', '0x')
print(int(sixteen_str,16))
