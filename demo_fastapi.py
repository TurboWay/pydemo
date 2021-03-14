#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/14 16:51
# @Author : way
# @Site : https://fastapi.tiangolo.com/zh/#_2
# @Describe: fastapi 写 api 服务

# 安装  pip install fastapi uvicorn
# 启动  uvicorn demo_fastapi:app --reload

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}
