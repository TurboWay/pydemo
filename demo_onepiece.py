#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/29 21:26
# @Author : way
# @Site : 
# @Describe: 海贼王漫画下载

import sys
import os
import time
import urllib3
import requests
from selenium import webdriver

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class OnePiece:

    def __init__(self):
        # 启动浏览器
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')  # 无头浏览
        # chrome_options.add_argument('--disable-gpu')  # 禁用gpu加速
        chrome_options.add_argument('--test-type --ignore-certificate-errors')  # 关闭https验证
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.maximize_window()
        self.driver.get('https://manhua.fzdm.com')
        time.sleep(2)

    @staticmethod
    def downpic(url, path):
        for _ in range(10):
            try:
                with open(path, 'wb') as f:
                    f.write(requests.get(url, ).content)
                    print(path + '下载成功')
                    return
            except:
                ...
        print(path + '下载失败：' + url)

    def down(self, chapternum):
        dir = f'海賊王/{chapternum}'
        os.makedirs(dir, exist_ok=True)
        for i in range(100):
            url = f'https://manhua.fzdm.com/2/{chapternum}/index_{i}.html'
            self.driver.get(url)
            time.sleep(2)
            try:
                img = self.driver.find_element_by_xpath('//*[@id="mhpic"]').get_attribute('src')
            except:
                img = None
            if img:
                path = f'{dir}/{i + 1}.jpg'
                self.downpic(img, path)
            else:
                print(f"海賊王第 {chapternum} 话下载完成")
                return


if __name__ == "__main__":
    chapternum = 1000

    if len(sys.argv) > 2:
        chapternum = sys.argv[1]

    op = OnePiece()
    op.down(chapternum)
    op.driver.quit()
