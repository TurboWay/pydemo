#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/13 23:25
# @Author : way
# @Site : 
# @Describe: 图片压缩

import tinify


def transform(key, source_path, target_parth):
    tinify.key = key  # 申请地址 https://tinypng.com/developers
    try:
        source = tinify.from_file(source_path)
        source.to_file(target_parth)
        print(f"transform success: {source_path} >> {target_parth} ")
        return True
    except Exception as e:
        print(f"transform fail: {e} ")
        return False
    finally:
        if tinify.compression_count >= 500:
            return False


if __name__ == "__main__":
    from config import tinify_keys

    source_path = r"F:\海賊王\1048\3.jpg"
    target_parth = r"F:\海賊王\1048\3test.jpg"
    transform(tinify_keys[0], source_path, target_parth)
