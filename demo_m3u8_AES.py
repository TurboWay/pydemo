#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/27 19:31
# @Author : way
# @Site : 
# @Describe: m3u8 下载器 (AES加密)

import os
import re
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from Crypto.Cipher import AES


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

key = '92c4749ace9c8bba'
cryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC)

class m3u8:

    def __init__(self, dir, num=10):
        """
        :param dir: 下载路径
        :param num: 并发数
        """
        self.dir = dir
        self.num = num

    @staticmethod
    def sort(px):
        for _ in range(5):
            px = '0' + str(px)
            if len(px) == 5:
                break
        return px

    @staticmethod
    def download_ts(path, ts_url):
        if os.path.exists(path):
            return
        path_loading = f'{path}.loading'
        try:
            with open(path_loading, 'wb') as f:
                data = requests.get(ts_url, headers=headers, stream=True, timeout=60).content
                f.write(cryptor.decrypt(data))
            os.rename(path_loading, path)
        except:
            ...

    def get_urls(self):
        urls = []
        with open('魔女m3u8.txt', 'r') as f:
            for px, ts_url in enumerate(re.findall('(.*?js)', f.read())):
                path = f'{dir}/{self.sort(px)}.ts'
                urls.append((path, ts_url))
            return urls

    def download(self):
        urls = self.get_urls()
        with ThreadPoolExecutor(max_workers=self.num) as pool:
            tasks = [pool.submit(self.download_ts, *i) for i in urls]
            for _ in tqdm(as_completed(tasks), desc='下载中......', total=len(tasks)):
                ...

    def merge(self):
        os.chdir(self.dir)
        for path in os.listdir():
            if path.endswith('loading'):
                raise Exception("部分文件未下载成功, 重新执行")

        os.system("copy /b *ts movie.mp4")
        for path in os.listdir():
            if path.endswith('.ts'):
                os.remove(path)


if __name__ == "__main__":
    dir = f'{os.getcwd()}/files/魔女'
    m = m3u8(dir, 20)
    m.download()
    m.merge()
