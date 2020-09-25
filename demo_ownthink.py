#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/25 18:15
# @Author : way
# @Site : 
# @Describe: 思知机器人

import requests

class Robot:

    def __init__(self, appid):
        self.appid = appid

    def reply(self, user, spoken):
        url = f'https://api.ownthink.com/bot?appid=xiaosi&userid={user}&spoken={spoken}'
        response = requests.get(url).json()
        if response['message'] == 'success':
            return response['data']['info']['text']
        else:
            return "你说什么，风太大，我听不见"

if __name__ == '__main__':
    fatboy = '0b519464452ebad4fcae4a59f05aa750'
    mumu = '00db9faed5c1a06cfdecb892ba1e9b6e'
    robot_fatboy = Robot(fatboy)
    robot_mumu = Robot(mumu)
    spoken = '你好'
    while 1:
        spoken = robot_fatboy.reply(mumu, spoken)
        print(f'fatboy: {spoken}')
        spoken = robot_mumu.reply(fatboy, spoken)
        print(f'mumu: {spoken}')
