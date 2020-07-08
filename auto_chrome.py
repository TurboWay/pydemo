#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/8 16:10
# @Author : way
# @Site : 
# @Describe: 自动操作 浏览器

import time
import urllib3
from selenium import webdriver

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 启动浏览器
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # 无头浏览
# chrome_options.add_argument('--disable-gpu')  # 禁用gpu加速
chrome_options.add_argument('--test-type --ignore-certificate-errors')  # 关闭https验证
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()

# cookies登陆
loginurl = "https://***/login"
target_url = "https://***/resource"
cookies = {} # or string

if isinstance(cookies, str):
    cookies = dict([i.strip().split('=', 1) for i in cookies.split(';')])

driver.get(loginurl)
driver.delete_all_cookies()
time.sleep(2)
for name, value in cookies.items():
    kv = {
        'name': name,
        'value': value,
    }
    driver.add_cookie(kv)
time.sleep(2)
driver.get(target_url)

# 模拟点击
#  driver.find_element_by_xpath('//*[@id="itemInfoDivId"]/div/div[1]/div/div[2]/div[1]').click()

time.sleep(10)

# 关闭浏览器
driver.quit()
