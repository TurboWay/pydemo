#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/31 14:31
# @Author : way
# @Site : 
# @Describe: 生成日期表

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import INT


def generateData(startDate='2019-1-01', endDate='2019-1-31'):
    d = {'id': pd.date_range(start=startDate, end=endDate)}
    data = pd.DataFrame(d)
    data['year'] = data['id'].apply(lambda x: x.year)
    data['month'] = data['id'].apply(lambda x: x.month)
    data['day'] = data['id'].apply(lambda x: x.day)
    data['quarter'] = data['id'].apply(lambda x: x.quarter)
    data['weekofyear'] = data['id'].apply(lambda x: x.weekofyear)
    data['dayofyear'] = data['id'].apply(lambda x: x.dayofyear)
    data['daysinmonth'] = data['id'].apply(lambda x: x.daysinmonth)
    data['dayofweek'] = data['id'].apply(lambda x: x.dayofweek)
    return data


engine = create_engine('postgresql://spider:spider@172.0.0.1:5432/spider_db')

data = generateData(startDate='2019-01-01', endDate='2029-12-31')
data['id'] = data['id'].apply(lambda x: x.strftime('%Y%m%d'))
dtypedict = {key: INT for key in data.keys()}
data.to_sql('dim_date', con=engine, index=False, if_exists='append', dtype=dtypedict)
sql = 'alter table dim_date add CONSTRAINT dim_date_id_pkey primary key(id); -- 增加主键'
pd.read_sql(sql, engine, chunksize=1)

# data.to_csv('DIM_TIME.csv', index = False, index_label = False)
