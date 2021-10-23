#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/5 23:15
# @Author : way
# @Site : 
# @Describe: ssh服务器文件夹上传下载

import os
import paramiko
import stat


class SSH:

    def __init__(self, host_ip, host_port, host_username, host_password):
        scp = paramiko.Transport((host_ip, host_port))
        scp.connect(username=host_username, password=host_password)
        self.sftp = paramiko.SFTPClient.from_transport(scp)
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=host_ip, port=host_port, username=host_username, password=host_password)

    def is_dir(self, remote_path):
        return stat.S_ISDIR(self.sftp.stat(remote_path).st_mode)

    def download_file(self, remote_file, local_file):
        if os.path.exists(local_file):
            print(f"{local_file} 已存在")
        else:
            self.sftp.get(remote_file, local_file)
            print(f"{local_file} 下载成功")

    def download(self, remote_path, local_path):
        if not os.path.exists(local_path):
            os.makedirs(local_path)
        dirs, files = [], []
        for path in self.sftp.listdir(remote_path):
            remote_file = remote_path + '/' + path
            local_file = local_path + '\\' + path
            if self.is_dir(remote_file):
                dirs.append((remote_file, local_file))
            else:
                files.append((remote_file, local_file))
        files.sort(key=lambda x: x[0])
        for _ in map(self.download_file, *zip(*files)):
            ...
        for dir in dirs:
            self.download(*dir)

    def upload_file(self, local_file, remote_file):
        try:
            self.sftp.stat(remote_file)
            print(f"{remote_file} 已存在")
        except IOError:
            if os.path.isdir(local_file):
                self.sftp.mkdir(remote_file)
            else:
                self.sftp.put(local_file, remote_file)
                print(f"{remote_file} 上传成功")

    def upload(self, local_path, remote_path):
        self.upload_file(local_path, remote_path)
        dirs, files = [], []
        if os.path.isdir(local_path):
            for path in os.listdir(local_path):
                remote_file = remote_path + '/' + path
                local_file = local_path + '\\' + path
                if os.path.isdir(local_file):
                    dirs.append((local_file, remote_file))
                else:
                    files.append((local_file, remote_file))
        files.sort(key=lambda x: x[0])
        for _ in map(self.upload_file, *zip(*files)):
            ...
        for dir in dirs:
            self.upload(*dir)

    def exec(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        print(stdout.read().decode())


if __name__ == '__main__':
    from config import host_ip, host_port, host_username, host_password

    ssh = SSH(host_ip, host_port, host_username, host_password)

    num = ''
    title = ''

    if not num or not title:
        exit()

    upload_remote_path = f'/root/comic_data/onepiece/{num}'  # 这个是远程目录
    upload_local_path = f'C:\GitHub\pydemo\海賊王\{num}'  # 这个是本地目录
    ssh.upload(upload_local_path, upload_remote_path)

    down_remote_path = f'/root/comic_data/onepiece/{num}/'  # 这个是远程目录
    down_local_path = f'F:\海賊王\{num}'  # 这个是本地目录
    ssh.download(down_remote_path, down_local_path)  #

    ssh.exec(f'cd /root/ishuhui_flask; python3 meta_add.py {num} {title}')
