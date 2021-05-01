#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/29 21:26
# @Author : way
# @Site : 
# @Describe: 海贼王漫画下载

import os
import requests
from bs4 import BeautifulSoup

def down(num, wxurl):
    dir = f'{os.getcwd()}/files/海賊王/{num}'
    os.makedirs(dir, exist_ok=True)
    res = requests.get(wxurl)
    imgs = BeautifulSoup(res.text, 'lxml').find('div', id="js_content").find_all('img')
    for px, img in enumerate(imgs, 1):
        url = img.get("data-src")
        # print(url)
        path = os.path.join(dir, f'{px}.jpg')
        with open(path, 'wb') as f:
            f.write(requests.get(url).content)
    print(f"{dir} 下载完成！")

if __name__ == "__main__":
    num = 1011
    wxurl = 'https://mp.weixin.qq.com/s/VoIwzJKPRDjVtMqI0YcXYg'
    down(num, wxurl)
