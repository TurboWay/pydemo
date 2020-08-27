#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/27 16:03
# @Author : way
# @Site : 
# @Describe: 解析 user-agent 识别用户端和其它相关信息

# 安装 pip install pyyaml ua-parser user-agents

from user_agents import parse

# Let's start from an old, non touch Blackberry device
ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1'
user_agent = parse(ua_string)
# user_agent.is_mobile # returns True
# user_agent.is_tablet # returns False
# user_agent.is_touch_capable # returns False
# user_agent.is_pc # returns False
# user_agent.is_bot # returns False
# str(user_agent) # returns "BlackBerry 9700 / BlackBerry OS 5 / BlackBerry 9700"
print(user_agent.get_device())
print(user_agent.get_os())
print(user_agent.get_browser())
print(user_agent)
print(str(user_agent).split(' / '))