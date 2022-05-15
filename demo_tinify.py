#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/13 23:25
# @Author : way
# @Site : 
# @Describe: tinypng 图片压缩
import os
from concurrent.futures import ThreadPoolExecutor

import tinify

tinify.key = ''  # 申请地址 https://tinypng.com/developers


def transform(source_path, target_parth):
    issuccess = True
    try:
        source = tinify.from_file(source_path)
        source.to_file(target_parth)
        print(f"transform success: {source_path} >> {target_parth} ")
    except Exception as e:
        issuccess = False
        print(f"transform fail: {e} ")
    finally:
        count_num = tinify.compression_count if tinify.compression_count else 0
        return issuccess, count_num


def batch_transform(tinify_keys, source_dir, target_dir):
    targets = []
    for chapter in os.listdir(source_dir):
        source_chapter_path = f"{source_dir}\{chapter}"
        target_chapter_path = f"{target_dir}\{chapter}"
        if not os.path.exists(target_chapter_path):
            os.mkdir(target_chapter_path)
        for i in os.listdir(source_chapter_path):
            source_path = os.path.join(source_chapter_path, i)
            target_parth = os.path.join(target_chapter_path, i)
            if os.path.exists(target_parth):
                print(f'{target_parth} 已存在')
                continue
            targets.append((source_path, target_parth))

    for key in tinify_keys:
        tinify.key = key
        targets = [i for i in targets if not os.path.exists(i[1])]
        targets.sort(key=lambda x: x[0], reverse=True)
        print(f"剩余待处理数量：{len(targets)}")
        try:
            with ThreadPoolExecutor(max_workers=15) as pool:
                for issuccess, count_num in pool.map(transform, *zip(*targets)):
                    if count_num >= 500:
                        print(f'{key} 使用次数用尽（{count_num}），自动切换下一个key')
                        raise Exception
        except:
            ...


if __name__ == "__main__":
    from config import tinify_keys

    source_dir = ''
    traget_dir = ''
    batch_transform(tinify_keys, source_dir, traget_dir)
