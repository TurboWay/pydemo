#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/29 21:26
# @Author : way
# @Site : 
# @Describe: 海贼王漫画下载

import json
import os
import shutil

import requests
import tinify
from bs4 import BeautifulSoup
from qiniu import Auth, put_file

from config import qiniu_ak, qiniu_sk, qiniu_bucket_name, tinify_keys, qiniu_urls, comic_conn

tinify.key = tinify_keys[-1]


# 下载并压缩图片
def down(num, wxurl):
    dir = f'海賊王/{num}'
    os.makedirs(dir, exist_ok=True)
    res = requests.get(wxurl)
    imgs = BeautifulSoup(res.text, 'lxml').find('div', id="js_content").find_all('img')
    for px, img in enumerate(imgs, 1):
        url = img.get("data-src")
        # print(url)
        path = os.path.join(dir, f'{px}.jpg')
        # with open(path, 'wb') as f:
        #     f.write(requests.get(url).content)
        source = tinify.from_url(url)  # 下载并压缩图片
        source.to_file(path)
        print(f'{path} 下载成功')
    print(f"{dir} 下载完成！")


# 手工清洗后，重新排序生成文件名
def file_order_rename(num):
    dir = f'海賊王/{num}'
    files = [file for file in os.listdir(dir)]
    files.sort(key=lambda x: int(x.split('.')[0]))
    for px, file in enumerate(files, 1):
        new = os.path.join(dir, f'{px}.jpg')
        old = os.path.join(dir, file)
        os.renames(old, new)


# 七牛云上传图片
def qiniu_upload(bucket_name, source_path, target):
    # 构建鉴权对象
    q = Auth(qiniu_ak, qiniu_sk)
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, target, 3600)
    # 要上传文件的本地路径
    ret, info = put_file(token, target, source_path, version='v2')
    if info.status_code == 200:
        print(f"上传成功: {source_path} >> http://{qiniu_urls[0]}/{target}")
        return True
    else:
        print(f"上传失败: {source_path} ")
        return False


# 上传图片并更新到数据库
def update_meta(chapter, title):
    conn = comic_conn
    cur = conn.cursor()
    imgs = []
    if not os.path.exists(f'F:\海賊王\{chapter}'):
        shutil.copy(f'海賊王/{chapter}', f'F:\海賊王\{chapter}')
    source_chapter_path = f"F:\海賊王\{chapter}"
    for i in os.listdir(source_chapter_path):
        source_path = os.path.join(source_chapter_path, i)
        qiniu_upload(qiniu_bucket_name, source_path, f'{chapter}/{i}')
        target = f'http://{qiniu_urls[0]}/{chapter}/{i}'
        imgs.append(target)
    imgs.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    delete_sql = f"delete from chapters where id={chapter}"
    insert_sql = f"""
    INSERT INTO chapters
    (id, title, comic_id, chapter_number, front_cover, refresh_time, images)
    VALUES({chapter}, '{title}', 1, {chapter}, '{imgs[0]}', now(), '{json.dumps(imgs)}');
    """
    cur.execute(delete_sql)
    cur.execute(insert_sql)
    conn.commit()
    cur.close()
    conn.close()
    print(f"海賊王 第{chapter}话 {title} 元数据更新成功!")


if __name__ == "__main__":
    num = 0
    title = ''
    wxurl = ''
    down(num, wxurl)
    # file_order_rename(num)
    # update_meta(num, title)
