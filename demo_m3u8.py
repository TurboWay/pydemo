#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/2 12:20
# @Author : way
# @Site : 
# @Describe:  m3u8 下载器

import os
import re
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


class m3u8:

    def __init__(self, url, dir, num=10):
        """
        :param url: m3u8 地址
        :param dir: 下载路径
        :param num: 并发数
        """
        self.url = url
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
                res = requests.get(ts_url, headers=headers, stream=True, timeout=60)
                for chunk in res.iter_content(chunk_size=512):
                    f.write(chunk)
            os.rename(path_loading, path)
        except:
            ...

    def get_urls(self):
        urls = []
        response = requests.get(self.url, headers=headers, timeout=60)
        url_head = '/'.join(self.url.split('/')[:-1])
        for px, ts in enumerate(re.findall('(.*?ts)', response.text)):
            path = f'{dir}/{self.sort(px)}.ts'
            ts_url = f'{url_head}/{ts}'
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
    dir = f'{os.getcwd()}/files/太极张三丰'
    url = 'https://vip.okokbo.com/20171220/u3xevz97/800kb/hls/index.m3u8'
    m = m3u8(url, dir, 20)
    m.download()
    m.merge()
