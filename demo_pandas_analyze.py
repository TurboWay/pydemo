#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/15 10:53
# @Author : way
# @Site : 
# @Describe: pandas 数据统计

import pandas as pd
from faker import Faker

f = Faker(locale='zh_CN')

user = {
    'id': range(10000),
    'name': [f.name() for _ in range(10000)],
    'age': [f.random_int(20,100) for _ in range(10000)],
    'sex': [f.random_sample(['男', '女'], 1)[0] for _ in range(10000)],
    'province': [f.province() for _ in range(10000)],
}
order = {
    'userid': range(10, 500),
    'saleqty': [f.random_int(1,10) for _ in range(10, 500)],
    'saleamt': [f.random_int(100,500) for _ in range(10, 500)],
    'area': [f.province() for _ in range(10, 500)],
}

user = pd.DataFrame(user)
order = pd.DataFrame(order)

# 查看数据集的整体情况
user.info()
user.count()

# 单列分析
user['age'].describe()   # 数值型：总数、均值、方差、最大、最小、从小到大排在 25%/50%/75% 的值
user['sex'].describe()   # 字符串：总数、去重、top 与 top的对应值

# 统计
"""
-- 福建省 年纪最大前 10 的男性 姓名、年龄
select name, age
from user 
where sex='男' 
  and province='福建省' 
order by age desc, name 
limit 10
"""
user[(user['sex']=='男') & (user['province']=='福建省')].loc[:, ['name', 'age']].sort_values(['age', 'name'], ascending=[False, True]).head(10)

""" 
-- 当地下单的省份、性别 的订单量排行前100
select province, sex, sum(b.saleqty) 
from user a 
left join order b on a.id = b.userid and a.province=b.area 
group by province, sex 
order by 2 desc 
limit 100
"""
user_order = pd.merge(user, order, left_on=['id', 'province'], right_on=['userid', 'area'], how='left')
user_order.groupby(['province', 'sex']).agg({'saleqty': 'sum'}).sort_values('saleqty',  ascending=False).head(100)

"""
-- 用户省份销售情况，按销售额、销售量排倒序 TOP10
select province, sum(b.saleamt * b.saleqty), sum(b.saleqty),  
from user a 
inner join order b on a.id = b.userid 
group by province
order by 1 desc, 2 desc 
limit 10 
"""
user_order = pd.merge(user, order, left_on=['id'], right_on=['userid'], how='inner')
user_order['amt'] = user_order['saleqty'] * user_order['saleamt']
user_order.groupby(['province']).agg({'saleqty': 'sum', 'amt': 'sum'}).sort_values(['amt', 'saleqty'],  ascending=[False, False]).head(10)

"""
-- 每个省份消费最多的用户
select *
from (
select a.province, a.name, b.saleamt * b.saleqty as amt,
row_number() over(partition by province order by b.saleamt * b.saleqty desc) as px
from user a 
inner join order b on a.id = b.userid 
) a
where a.px = 1
"""
user_order['px'] = user_order.groupby(['province'])['amt'].rank(ascending=False, method='first')
user_order[user_order['px'] == 1].loc[:, ['name', 'amt', 'province']].reset_index()
# user_order[user_order['province'] == '天津市'].sort_values('amt', ascending=False).loc[:, ['name', 'amt', 'province']].reset_index()
