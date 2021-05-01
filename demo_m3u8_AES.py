#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/27 19:31
# @Author : way
# @Site : 
# @Describe: m3u8 下载器 (AES加密)

import os
import shutil
import re
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from Crypto.Cipher import AES
from urllib.parse import urlparse, urljoin

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


class m3u8:

    def __init__(self, url, key, dir, target, num=10):
        """
        :param url: m3u8 资源链接
        :param key: aes 加密key
        :param dir: 文件夹名称
        :param target: 文件名
        :param num: 并发数
        """
        self.dir = dir
        self.num = num
        self.url = url
        self.target = target.split('.')[0] + '.mp4'
        self.temp_dir = os.path.join(self.dir, target.split('.')[0] + '_temp')
        os.makedirs(self.dir, exist_ok=True)
        os.makedirs(self.temp_dir, exist_ok=True)
        self.cryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC) if key else None
        parse = urlparse(self.url)
        self.host = f"{parse.scheme}://{parse.netloc}"

    @staticmethod
    def sort(px):
        for _ in range(5):
            px = '0' + str(px)
            if len(px) == 5:
                break
        return px

    def download_ts(self, path, ts_url):
        if os.path.exists(path):
            return
        path_loading = f'{path}.loading'
        try:
            with open(path_loading, 'wb') as f:
                data = requests.get(ts_url, headers=headers, stream=True, timeout=60).content
                if self.cryptor:
                    data = self.cryptor.decrypt(data)
                f.write(data)
            os.rename(path_loading, path)
        except:
            ...

    def get_urls(self):
        res = requests.get(self.url, headers=headers).text
        urls = []
        for px, ts_url in enumerate(re.findall('(.*?\.ts)', res)):
            ts_url = urljoin(self.host, ts_url)
            path = f'{self.temp_dir}/{self.sort(px)}.ts'
            urls.append((path, ts_url))
        return urls

    def download(self):
        urls = self.get_urls()
        with ThreadPoolExecutor(max_workers=self.num) as pool:
            tasks = [pool.submit(self.download_ts, *i) for i in urls]
            for _ in tqdm(as_completed(tasks), desc='下载中......', total=len(tasks)):
                ...

    def merge(self):
        os.chdir(self.temp_dir)
        for path in os.listdir():
            if path.endswith('loading'):
                raise Exception("部分文件未下载成功, 重新执行")

        os.system(f"copy /b *ts {self.target}")  # 合并 ts
        tr = os.path.join(self.dir, self.target)
        if os.path.exists(tr):
            os.remove(tr)
        shutil.move(self.target, self.dir)
        os.chdir(self.dir)
        shutil.rmtree(self.temp_dir)  # 移除临时文件夹
        print(f"{self.target} 下载完成！")


if __name__ == "__main__":
    dir = f'{os.getcwd()}/files/猎鹰与冬兵'
    targets = [
        ('https://mhcdn.mhqiyi.com/20210326/7Mvnme5R/1000kb/hls/index.m3u8', '6ae169d7dbacab8e', '猎鹰与冬兵第02集',),
        ('https://mhcdn.mhqiyi.com/20210402/ICU35rhY/1000kb/hls/index.m3u8', '68fa55edaebdbdbc', '猎鹰与冬兵第03集',),
    ]
    for tr in targets:
        url, key, target = tr
        m = m3u8(url, key, dir, target, 20)
        m.download()
        m.merge()
