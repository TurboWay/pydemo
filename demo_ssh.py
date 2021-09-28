#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/5 23:15
# @Author : way
# @Site : 
# @Describe: ssh服务器下载文件夹到本地

import os
import paramiko

def RemoteScp(host_ip, host_port, host_username, host_password, remote_path, local_path):
    scp = paramiko.Transport((host_ip, host_port))
    scp.connect(username=host_username, password=host_password)
    sftp = paramiko.SFTPClient.from_transport(scp)
    remote_files = sftp.listdir(remote_path)
    folds = [int(fold) for fold in remote_files]
    folds.sort(reverse=True)
    for fold in folds:
        remote_fold_path = remote_path + '/' + str(fold)
        local_fold_path = os.path.join(local_path, str(fold))
        if not os.path.exists(local_fold_path):
            os.makedirs(local_fold_path)
        files = sftp.listdir(remote_fold_path)
        files.sort(key=lambda x:int(x.split('.')[0]))
        for file in files:  # 遍历读取远程目录里的所有文件
            local_file = os.path.join(local_fold_path, str(file))
            remote_file = remote_fold_path + '/' + str(file)
            if os.path.exists(local_file):
                print(f"{local_file} 已存在")
                continue
            flag = False
            for _ in range(5):
                try:
                    sftp.get(remote_file, local_file)
                    print(f"{local_file} 下载成功")
                    flag = True
                    break
                except:
                    ...
            if not flag:
                if os.path.exists(local_file):
                    os.remove(local_file)
                print(f"{local_file} 下载失败")
        print(f"{local_fold_path} 下载完成！" )

if __name__ == '__main__':
    remote_path = '/root/comic_data/onepiece'  # 这个是远程目录
    local_path = r'F:\海賊王'  # 这个是本地目录
    from config import host_ip, host_port, host_username, host_password
    RemoteScp(host_ip, host_port, host_username, host_password, remote_path, local_path)  # 调用方法