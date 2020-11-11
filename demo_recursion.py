#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/11 15:35
# @Author : way
# @Site : 
# @Describe: 秒数时长格式化(递归)

def changeTime(allTime):
    day = 24 * 60 * 60
    hour = 60 * 60
    min = 60
    if allTime < 60:
        return "%d 秒" % allTime
    elif allTime > day:
        days, hours = divmod(allTime, day)
        return "%d 天 %s" % (days, changeTime(hours))
    elif allTime > hour:
        hours, mins = divmod(allTime, hour)
        return '%d 时 %s' % (hours, changeTime(mins))
    else:
        mins, secs = divmod(allTime, min)
        return "%d 分 %d 秒" % (mins, secs)

if __name__ == "__main__":
    new = changeTime(5555)
    print(new)