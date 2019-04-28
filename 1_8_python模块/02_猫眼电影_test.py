#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 15:50
# @Author  : Xuegod Teacher For
# @File    : 02_猫眼电影_test.py
# @Software: PyCharm
import base64
import re

import chardet
import requests
from fontTools.ttLib import TTFont
url = 'https://piaofang.maoyan.com/?ver=normal'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}
response = requests.get(url=url, headers=headers).content  # 得到字节
charset = chardet.detect(response).get('encoding')  # 得到编码格式
response = response.decode(charset, "ignore")  # 解码得到字符串

# 本地已经下载好的字体处理
base_font = TTFont('font.ttf') #打开本地的ttf文件

base_uni_list = base_font.getGlyphOrder()[2:]   # 获取所有编码，去除前2个，可查看前文图示

# 写出第一次字体文件的编码和对应字体
origin_dict = {'uniE481': '7', 'uniE0AA': '4', 'uniF71E': '9', 'uniE767': '1', 'uniE031': '5', 'uniE4BD': '2','uniF2AA': '3', 'uniE2E3': '6', 'uniE3C9': '8', 'uniEA65': '0'}
# 获取字体文件的base64编码
online_ttf_base64 = re.findall(r"base64,(.*)\) format", response)[0]
online_base64_info = base64.b64decode(online_ttf_base64)
with open('online_font.ttf', 'wb')as f:
    f.write(online_base64_info)
online_font = TTFont('online_font.ttf')  # 网上动态下载的字体文件。
online_uni_list = online_font.getGlyphOrder()[2:]

for uni2 in online_uni_list:
    obj2 = online_font['glyf'][uni2]  # 获取编码uni2在online_font.ttf中对应的对象
    for uni1 in base_uni_list:
        obj1 = base_font['glyf'][uni1]  # 获取编码uni1在base_font.ttf 中对应的对象
        if obj1 == obj2:  # 判断两个对象是否相等
            dd = "&#x" + uni2[3:].lower() + ';'  # 修改为Unicode编码格式
            if dd in response:  # 如果编码uni2的Unicode编码格式 在response中，替换成origin_dict中的数字。
                try:
                    response = response.replace(dd, origin_dict[uni1])
                except:
                    pass


