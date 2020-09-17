#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/17 17:53
# @Author : way
# @Site : 
# @Describe: 执行 sql

from sqlalchemy import create_engine, orm

ENGINE_CONFIG = 'postgresql://spider:spider@127.0.0.1:5432/spider_db'


# 'mysql://user:pwd@127.0.0.1:3306/spider_db?charset=utf8',  # mysql
# 'postgresql://user:pwd@127.0.0.1:5432/spider_db',  # postgresql
# 'oracle://user:pwd@127.0.0.1:1521/spider_db',  # oracle
# 'mssql+pymssql://user:pwd@127.0.0.1:1433/spider_db',  # sqlserver
# 'sqlite:///D:/GitHub/pydemo/test.db'  # sqlite

class DB:

    def __init__(self, ENGINE_CONFIG):
        engine = create_engine(ENGINE_CONFIG)
        self.session = orm.sessionmaker(bind=engine)()

    def read(self, sql):
        try:
            cursor = self.session.execute(sql)
            print("执行成功")
            return cursor.fetchall()
        except Exception as e:
            print(f"执行失败：{e}")

    def execute(self, sql):
        try:
            self.session.execute(sql)
            self.session.commit()
            print("执行成功")
        except Exception as e:
            print(f"执行失败：{e}")


if __name__ == '__main__':
    db = DB(ENGINE_CONFIG)
    sql = """
    
    """
    # db.execute(sql)   # ddl
    # rows = db.read(sql)   # read
    # print(rows)
