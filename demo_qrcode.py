#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/16 20:58
# @Author : way
# @Site : 
# @Describe: 二维码的生成与解读


import qrcode
import zxing

# 生成二维码
data = "https://www.baidu.com"
img = qrcode.make(data=data)
img.show()
img.save("baidu.jpg")

# 解析二维码
reader = zxing.BarCodeReader()
barcode = reader.decode("baidu.jpg")
print(barcode.parsed)