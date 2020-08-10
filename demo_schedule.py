#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/21 16:42
# @Author : way
# @Site : 
# @Describe: 定时执行命令

import time
import subprocess
import sys

# 开始执行
# hour, min = int(sys.argv[1]), int(sys.argv[2])
hour, min = 16, 47
min_inc = 23 * 60    # 执行间隔（min） 默认 23 小时
print(f"下次执行时间 {hour}:{min}")
print(f"等待...")

while True:
    now = time.localtime()
    if now.tm_hour == hour and now.tm_min == min:
        print(f"{hour}:{min} 开始执行...")

        cmd = ""
        p = subprocess.Popen(cmd, shell=True)
        p.wait()
        print(f"执行完毕")

        # 计算下次执行时间
        hour_inc, min = divmod(min + min_inc, 60)
        _, hour = divmod(hour + hour_inc, 24)
        print(f"下次执行时间 {hour}:{min}")
        print(f"等待...")

