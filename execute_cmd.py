#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/13 17:20
# @Author : way
# @Site : 
# @Describe: 执行 shell 命令

import subprocess

cmd = "ls"

# 阻塞执行
p = subprocess.Popen(cmd, shell=True)
p.wait()
print(p.returncode)

# 输出返回信息
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
stdout, stderr = p.communicate()
print(p.returncode, stdout.decode(), stderr.decode('gbk'))

# 记录日志
logfile = 'xxx.log'
with open(logfile, 'a', encoding='utf-8') as log:
    r = subprocess.Popen(cmd, stdout=log, stderr=log, shell=True)
r.wait()