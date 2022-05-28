#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/10 11:02
# @Author : way
# @Site : 
# @Describe: 异步

import time
import asyncio
from random import randint


async def worker(lt: list):
    while 1:
        time.sleep(3)
        lt.append(1)
        print(lt)

async def worker2(lt: list):
    while 1:
        time.sleep(1)
        lt.append(2)
        print(lt)

s = []
workers = [worker(s), worker2(s)]
loop = asyncio.get_event_loop()
loop.create_task(worker(s))
loop.create_task(worker2(s))
loop.run_forever()
print(s)
