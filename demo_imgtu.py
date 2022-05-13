#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/13 23:22
# @Author : way
# @Site : 
# @Describe: 路过图床自动上传

import json
import re
import time

import requests


class Imgtu:

    def __init__(self):
        self.url = 'https://imgtu.com'
        self.session = requests.session()
        self.token = self.get_token()

    def get_token(self):
        res = self.session.get(url=self.url)
        token = re.findall(r"PF.obj.config.auth_token = \"(\w*)\";", res.text)[0]
        return token

    def upload(self, file_path):
        data = {
            'type': 'file',
            'action': 'upload',
            'timestamp': int(time.time() * 1000),
            'auth_token': self.token,
            'nsfw': 0
        }
        file = {
            'source': (file_path.split('//')[-1], open(file_path, "rb")),
        }
        res = self.session.post(url=self.url+'/json', data=data, files=file)
        try:
            return json.loads(res.text)['image']['url']
        except:
            raise Exception(res.text)


if __name__ == '__main__':
    imgtu = Imgtu()
    import os
    for i in os.listdir(r'F:\海賊王\1048'):
        path = os.path.join(r'F:\海賊王\1048',i)
        url = imgtu.upload(path)
        print(url)
