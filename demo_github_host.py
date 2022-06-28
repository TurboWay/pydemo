#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/3 15:01
# @Author : way
# @Site : 
# @Describe: 更新 github 的 host 配置

import subprocess
import requests

url = 'https://gitlab.com/ineo6/hosts/-/raw/master/next-hosts'
res = requests.get(url)
github_hosts = '\n'.join([i for i in res.text.strip().split('\n') if 'github' in i.lower() and not i.startswith('#') or 'Update at' in i])

path = "C:\Windows\System32\drivers\etc\hosts"
bak_path = "C:\Windows\System32\drivers\etc\hosts_bak"
with open(path, 'r', encoding='utf-8') as f:
    # 先备份
    old = ''.join([line for line in f.readlines() if 'github' not in line.lower()])
    with open(bak_path, 'w', encoding='utf-8') as bak:
        bak.write(old)
    # 更新host
    new = old + f'# GitHub Start\n{github_hosts}\n# GitHub End'
    with open(path, 'w', encoding='utf-8') as f2:
         f2.write(new)
print(f"github host 已更新")
child_process = subprocess.Popen('ipconfig /flushdns', shell=True)
(stdout, stderr) = child_process.communicate()