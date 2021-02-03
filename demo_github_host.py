#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/3 15:01
# @Author : way
# @Site : 
# @Describe: 更新 github 的 host 配置

import re
import requests

github_hosts = """# GitHub Start
ip1 assets-cdn.github.com
ip2 user-images.githubusercontent.com
ip2 raw.githubusercontent.com
ip2 gist.githubusercontent.com
ip2 cloud.githubusercontent.com
ip2 camo.githubusercontent.com
ip2 avatars.githubusercontent.com
ip2 avatars0.githubusercontent.com
ip2 avatars1.githubusercontent.com
ip2 avatars2.githubusercontent.com
ip2 avatars3.githubusercontent.com
ip2 avatars4.githubusercontent.com
ip2 avatars5.githubusercontent.com
ip2 avatars6.githubusercontent.com
ip2 avatars7.githubusercontent.com
ip2 avatars8.githubusercontent.com
# GitHub End
"""

ip_map = {
    'ip1': 'https://github.com.ipaddress.com/assets-cdn.github.com',
    'ip2': 'https://githubusercontent.com.ipaddress.com/raw.githubusercontent.com',
}

for key, url in ip_map.items():
    ip = re.findall('"comma-separated"><li>(.*?)</li>', requests.get(url).text)[0]
    github_hosts = github_hosts.replace(key, ip)

path = "C:\Windows\System32\drivers\etc\hosts"
with open(path, 'r', encoding='utf-8') as f:
    new = ''.join([line for line in f.readlines() if 'github' not in line.lower()]) + github_hosts
    with open('hosts', 'w', encoding='utf-8') as f2:
         f2.write(new)
print(f"github host 已更新，自行替换到 {path[:-6]}")