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
    dir = f'海賊王/{num}'
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


def file_order_rename(num):
    dir = f'海賊王/{num}'
    files = [file for file in os.listdir(dir)]
    files.sort(key=lambda x: int(x.split('.')[0]))
    for px, file in enumerate(files, 1):
        new = os.path.join(dir, f'{px}.jpg')
        old = os.path.join(dir, file)
        os.renames(old, new)


if __name__ == "__main__":
    num = 1029
    wxurl = 'https://mp.weixin.qq.com/s/tEU7hZZwGTkBegaXqhGP3g'
    down(num, wxurl)
    # file_order_rename(num)