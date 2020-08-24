#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/20 10:52
# @Author : way
# @Site : 
# @Describe: 图片缩放处理

from PIL import Image

img = Image.open("test.png")
out = img.resize((50, 50))
out.save("new.png")
