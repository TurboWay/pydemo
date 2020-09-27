#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/25 18:15
# @Author : way
# @Site : 
# @Describe: 思知机器人

import requests


class Robot:

    def __init__(self, user):
        self.user = user

    def reply(self, spoken):
        url = f'https://api.ownthink.com/bot?appid=xiaosi&userid={self.user}&spoken={spoken}'
        response = requests.get(url).json()
        if response['message'] == 'success':
            return response['data']['info']['text']
        else:
            return "你说什么，风太大，我听不见"


if __name__ == '__main__':
    robot_fatboy = Robot('fatboy20200927')
    robot_mumu = Robot('mumu20200927')
    spoken = '你好'
    while 1:
        spoken = robot_fatboy.reply(spoken)
        print(f'fatboy: {spoken}')
        spoken = robot_mumu.reply(spoken)
        print(f'mumu: {spoken}')
