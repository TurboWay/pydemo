#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/7/13 17:33
# @Author : way
# @Site : 
# @Describe: 执行 sql

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR, INT

# rdbms
ENGINE_CONFIGS = [
    'mysql://user:pwd@127.0.0.1:3306/spider_db?charset=utf8',  # mysql
    'postgresql://user:pwd@127.0.0.1:5432/spider_db',  # postgresql
    'oracle://user:pwd@127.0.0.1:1521/spider_db',  # oracle
    'mssql+pymssql://user:pwd@127.0.0.1:1433/spider_db',  # sqlserver
    'sqlite:///D:/GitHub/pydemo/test.db'  # sqlite
]
ENGINE = create_engine(ENGINE_CONFIGS[-1])

tbname = 'test'
sql = 'delete from test'

META_COL_MAP = {
    'id': INT,
    'name': VARCHAR(50),
}

values = [
    {'id': 456, 'name': '肥仔'},
    {'id': 789, 'name': '测试456'}
]
# 判断表存在，执行 sql
if pd.io.sql.has_table(tbname, con=ENGINE, schema=None):
    pd.read_sql(sql, ENGINE, chunksize=1)

# insert/update 数据
df = pd.DataFrame(values, columns=[key for key in META_COL_MAP.keys()])
df.to_sql(tbname, con=ENGINE, index=False, if_exists='append', dtype=META_COL_MAP)

# 读数据
sql = "select * from test"
data = pd.read_sql(sql, ENGINE)
for row in data.values:
    print(row)