#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/9 9:45
# @Author : way
# @Site : 
# @Describe: 根据进程名杀死进程

import psutil


def kill_process(name):
    pids = []
    all_pids = psutil.pids()

    for pid in all_pids:
        p = psutil.Process(pid)
        # print(pid, p.name())
        if p.name() == name:
            pids.append(pid)

    for pid in pids:
        p = psutil.Process(pid)
        for son in p.children(recursive=True):
            son.terminate()
        p.terminate()


if __name__ == "__main__":
    name = 'chromedriver.exe'
    kill_process(name)
