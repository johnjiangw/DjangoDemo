#!/usr/bin/env python
# coding:utf-8
# author:john
"""
生成图片验证码
"""
import os
import io
import random
from PIL import Image, ImageDraw, ImageFont

class VerifyCode(object):
    """
    验证码相关操作
    """
    def __init__(self):
        pass
    def get_verify_code(self,length=4):
        """
        获取验证码
        :param length: 验证码长度
        :return: 验证码
        """
        # 定义验证码的备选值
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        # 随机选取4个值作为验证码
        rand_str = ''
        for i in range(0, length):
            rand_str += chars[random.randrange(0, len(chars))]
        return rand_str


    def get_verify_img(self,code,needpoint=True, width=100, height=25):
        """
        根据验证码获取验证码图片
        :param code: 验证码
        :param needpoint: 是否需要绘制噪点
        :param width: 图片长度
        :param height: 图片高度
        :return: 返回图片内存
        """
        # 图片背景色
        bgcolor = (69, 195, 241)
        # 创建画面对象
        img = Image.new('RGB', (width, height), bgcolor)
        # 创建画笔对象
        draw = ImageDraw.Draw(img)
        # 调用画笔的point()函数绘制噪点
        if needpoint is True:
            for i in range(0, 100):
                xy = (random.randrange(0, width), random.randrange(0, height))
                fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
                draw.point(xy, fill=fill)

        # 字体windows:C:\Windows\Fonts，ubuntu:'/usr/share/fonts/truetype/freefont'
        font = ImageFont.truetype('ARIALUNI.TTF', 20)
        # 字体颜色
        fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
        # 间距
        distance = int(width/len(code))
        # 绘制文字
        for i in range(0, len(code)):
            draw.text(xy=(i*distance, 1), text=code[i], font=font, fill=fontcolor)
        # 释放画笔
        del draw
        # 内存文件操作-->此方法为python3的
        buffer = io.BytesIO()
        # 将图片保存在内存中，文件类型为png
        img.save(buffer, 'png')
        return buffer
