#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/5 16:08
# @Author : way
# @Site : 更多用法 https://www.jianshu.com/p/6bd6869631d9
# @Describe:  生成假数据

from faker import Faker

f = Faker(locale='zh_CN')

f.name()  #生成姓名
f.address() #生成地址
f.profile()  #随机生成档案信息
f.simple_profile()  #随机生成简单档案信息

f.company()
f.address()
f.province()
f.sentence()



