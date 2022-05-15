#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/14 23:05
# @Author : way
# @Site : 
# @Describe: 七牛云 oss 自动监控流量

import logging
import os
import time

from qiniu import Auth, BucketManager, CdnManager

logging.basicConfig(
    filename=f'{os.path.dirname(os.path.abspath(__file__))}/qiniu_monitor.log',
    level=logging.INFO,
    filemode='a',
    format='%(asctime)s [%(name)s] %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s: %(message)s', "%Y-%m-%d %H:%M:%S")
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)


# 修改存储空间权限
def qiniu_bucket_swith(bucket_name, private):
    """
    bucket_name: 存储空间名
    private: 0 公开；1 私有 ,str类型
    """
    # 构建鉴权对象
    q = Auth(qiniu_ak, qiniu_sk)
    # 初始化BucketManager
    bucket = BucketManager(q)
    # 你要测试的空间， 并且这个key在你空间中存在
    ret, info = bucket.bucket_info(bucket_name)
    if ret['private'] == private:
        logger.info(f"无需操作：{bucket_name} 当前为{'公开' if private == 0 else '私有'}空间")
        return True
    ret, info = bucket.change_bucket_permission(bucket_name, private)
    if info.status_code == 200:
        logger.info(f"操作成功：{bucket_name}已修改为{'公开' if private == 0 else '私有'}空间")
        return True
    else:
        logger.info(f"操作失败")
        return False


# 获取本月流量
def qiniu_flux_data(urls):
    q = Auth(qiniu_ak, qiniu_sk)
    cdn_manager = CdnManager(q)
    startDate = time.strftime('%Y-%m-01', time.localtime())
    endDate = time.strftime('%Y-%m-%d', time.localtime())
    granularity = 'day'
    ret, info = cdn_manager.get_flux_data(urls, startDate, endDate, granularity)
    if info.status_code == 200:
        data = ret['data']
        flux_byte_num = 0
        for url in data.values():
            for area in url.values():
                flux_byte_num += sum(area)
        flux_g_num = flux_byte_num / 1024 / 1024 / 1024
        return flux_g_num
    else:
        logger.error(f"流量查询失败：{info}")


# 自动关闭存储
def qiniu_monitor(urls, bucket_name, limit_max):
    flux_g_num = qiniu_flux_data(urls)
    if flux_g_num > limit_max:
        logger.info(
            f'本月已使用流量为 {flux_g_num:.2f} G，已超出设定阈值 {limit_max:.2f} G，超出量为 {flux_g_num - limit_max:.2f} G，将自动关闭存储空间 {bucket_name}')
        qiniu_bucket_swith(bucket_name, 1)
    else:
        logger.info(f'本月已使用流量为 {flux_g_num:.2f} G，距离设定阈值 {limit_max:.2f} G，还有{limit_max - flux_g_num:.2f} G可用')
        qiniu_bucket_swith(bucket_name, 0)


if __name__ == "__main__":
    from config import qiniu_ak, qiniu_sk, qiniu_urls, qiniu_bucket_name, qiniu_limit_max

    qiniu_monitor(qiniu_urls, qiniu_bucket_name, qiniu_limit_max)
