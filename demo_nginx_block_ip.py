#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/17 9:55
# @Author : way
# @Site : 
# @Describe: nginx 自动禁ip

import os
import re
import time
import subprocess

count_limit = 200  # 请求限制200次/小时

today = time.strftime('%Y%m%d', time.localtime())

nginx_log_path = '/var/log/nginx/access.log'    # 日志路径，每天自动截断
block_ip_conf = f'/etc/nginx/default.d/blockip_{today}.conf'

ip_count = {}
with open(nginx_log_path, 'r') as f:
    for row in f.readlines():
        remote_addr, remote_user, time_local, url = re.findall('(.*?) - (.*?) \[(.*?)\] "(.*?)"', row)[0]
        hour = int(re.findall(':(.*?):', time_local)[0])
        ip = (remote_addr, hour)
        ip_count[ip] = ip_count.get(ip, 0) + 1

block_ips = [f'deny {ip[0]};' for ip, count in ip_count.items() if count >= count_limit]

if block_ips:

    ct = 0

    if os.path.exists(block_ip_conf):
        with open(block_ip_conf, 'r') as f:
            ct = len(f.readlines())

    # 有新增则更新文件，重启nginx
    if len(block_ips) > ct:
        with open(block_ip_conf, 'w') as f:
            f.write('\n'.join(block_ips))

        cmd = 'nginx -s reload'
        child_process = subprocess.Popen(cmd, shell=True)  # 重启 nginx
        (stdout, stderr) = child_process.communicate()
