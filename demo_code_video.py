#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/2 14:42
# @Author : way
# @Site : 
# @Describe: 将视频转换成代码视频

import os
import subprocess
import shutil
import cv2
from PIL import Image, ImageFont, ImageDraw

FFMPEG = r'D:\ffmpeg\bin\ffmpeg.exe'

class CodeVideo:

    def __init__(self, **kwargs):
        """
        :param kwargs:
            vediopath: 输入视频文件路径
            gray: 输出视频的颜色 True 灰色 False 彩色 默认 True
            style: 输出视频的代码风格 可选有 0,1,2,3 种 默认 0
            clean: 是否删除临时文件 True 删除 False 不删除 默认 True
            cut: 是否先对原视频做截取处理 True 截取 False 不截取 默认 False
            start: 视频截取开始时间点, 默认 00:00:00 仅当iscut=True时有效
            end: 视频截取结束时间点, 默认 00:00:14 仅当iscut=True时有效
        """
        self.vediopath = kwargs.get('vediopath')
        self.code_color = (169, 169, 169) if kwargs.get('gray', True) else None
        self.clean = kwargs.get('clean', True)
        self.cut = kwargs.get('cut', False)
        self.cut_start = kwargs.get('start', '00:00:00')
        self.cut_end = kwargs.get('end', '00:00:14')
        self.ascii_char = (
            list("MNHQ$OC67)oa+>!:+. "),
            list("MNHQ$OC67+>!:-. "),
            list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:oa+>!:+. "),
            ['.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@'],
        )[kwargs.get('style', 0)]  # 像素对应ascii码

    def main(self):
        file_cut = self.vediopath.split('.')[0] + '_cut.mp4'
        file_mp3 = self.vediopath.split('.')[0] + '.mp3'
        file_temp_avi = self.vediopath.split('.')[0] + '_temp.avi'
        outfile_name = self.vediopath.split('.')[0] + '_code.mp4'
        print("开始生成...")
        if self.cut:
            print("正在截取视频...")
            self.vediocut(self.vediopath, file_cut, self.cut_start, self.cut_end)
            self.vediopath = file_cut
        print("正在转换代码图片...")
        vc = self.video2txt_jpg(self.vediopath)  # 视频转图片，图片转代码图片
        FPS = vc.get(cv2.CAP_PROP_FPS)  # 获取帧率
        vc.release()
        print("正在分离音频...")
        self.video2mp3(self.vediopath, file_mp3)  # 从原视频分离出 音频mp3
        print("正在转换代码视频...")
        self.jpg2video(file_temp_avi, FPS)  # 代码图片转视频
        print("正在合成目标视频...")
        self.video_add_mp3(file_temp_avi, file_mp3, outfile_name)  # 将音频合成到代码视频
        if self.clean:  # 移除临时文件
            print("正在移除临时文件...")
            shutil.rmtree("Cache")
            for file in [file_cut, file_mp3, file_temp_avi]:
                if os.path.exists(file):
                    os.remove(file)
        print("生成成功：{0}".format(outfile_name))

    # 将视频拆分成图片
    def video2txt_jpg(self, file_name):
        vc = cv2.VideoCapture(file_name)
        c = 1
        if vc.isOpened():
            r, frame = vc.read()
            if not os.path.exists('Cache'):
                os.mkdir('Cache')
            os.chdir('Cache')
        else:
            r = False
        while r:
            cv2.imwrite(str(c) + '.jpg', frame)
            self.txt2image(str(c) + '.jpg')  # 同时转换为ascii图
            r, frame = vc.read()
            c += 1
        os.chdir('..')
        return vc

    # 将txt转换为图片
    def txt2image(self, file_name):
        im = Image.open(file_name).convert('RGB')
        # gif拆分后的图像，需要转换，否则报错，由于gif分割后保存的是索引颜色
        raw_width = im.width
        raw_height = im.height
        width = int(raw_width / 6)
        height = int(raw_height / 15)
        im = im.resize((width, height), Image.NEAREST)

        txt = ""
        colors = []
        for i in range(height):
            for j in range(width):
                pixel = im.getpixel((j, i))
                colors.append((pixel[0], pixel[1], pixel[2]))
                if (len(pixel) == 4):
                    txt += self.get_char(pixel[0], pixel[1], pixel[2], pixel[3])
                else:
                    txt += self.get_char(pixel[0], pixel[1], pixel[2])
            txt += '\n'
            colors.append((255, 255, 255))

        im_txt = Image.new("RGB", (raw_width, raw_height), (255, 255, 255))
        dr = ImageDraw.Draw(im_txt)
        # font = ImageFont.truetype(os.path.join("fonts","汉仪楷体简.ttf"),18)
        font = ImageFont.load_default().font
        x = y = 0
        # 获取字体的宽高
        font_w, font_h = font.getsize(txt[1])
        font_h *= 1.37  # 调整后更佳
        # ImageDraw为每个ascii码进行上色
        for i in range(len(txt)):
            if (txt[i] == '\n'):
                x += font_h
                y = -font_w
            if self.code_color:
                dr.text((y, x), txt[i], fill=self.code_color)  # fill=colors[i]彩色
            else:
                dr.text((y, x), txt[i], fill=colors[i])  # fill=colors[i]彩色
            y += font_w
        im_txt.save(file_name)

    # 将像素转换为ascii码
    def get_char(self, r, g, b, alpha=256):
        if alpha == 0:
            return ''
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        unit = (256.0 + 1) / len(self.ascii_char)
        return self.ascii_char[int(gray / unit)]

    # 代码图片转视频
    @staticmethod
    def jpg2video(outfile_name, fps):
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        images = os.listdir('Cache')
        im = Image.open('Cache/' + images[0])
        vw = cv2.VideoWriter(outfile_name, fourcc, fps, im.size)
        os.chdir('Cache')
        for image in range(len(images)):
            frame = cv2.imread(str(image + 1) + '.jpg')
            vw.write(frame)
        os.chdir('..')
        vw.release()

    # 调用 ffmpeg 分离音频
    @staticmethod
    def video2mp3(file_name, outfile_name):
        cmdstr = f'{FFMPEG} -i {file_name} -f mp3 {outfile_name} -y'
        subprocess.call(cmdstr, shell=True, creationflags=0x08000000)

    # 调用 ffmpeg 给视频添加音频
    @staticmethod
    def video_add_mp3(file_name, mp3_file, outfile_name):
        cmdstr = f'{FFMPEG} -i {file_name} -i {mp3_file} -strict -2 -f mp4 {outfile_name} -y'
        subprocess.call(cmdstr, shell=True, creationflags=0x08000000)

    # 调用 ffmpeg 截取视频
    @staticmethod
    def vediocut(file_name, outfile_name, start, end):
        cmdstr = f'{FFMPEG} -i {file_name} -vcodec copy -acodec copy -ss {start} -to {end} {outfile_name} -y'
        subprocess.call(cmdstr, shell=True, creationflags=0x08000000)


if __name__ == '__main__':
    vediopath = r"C:\Users\Administrator\Desktop\test.mp4"
    CodeVideo(vediopath=vediopath).main()
