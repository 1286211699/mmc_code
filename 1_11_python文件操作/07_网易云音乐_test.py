#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 22:13
# @Author  : Xuegod Teacher For
# @File    : 07_网易云音乐_test.py
# @Software: PyCharm
# 1413585838
# https://music.163.com/#/song?id=1413585838

import requests
import re
#pip install fake-useragent
from fake_useragent import UserAgent

headers  ={
    'User_Agent':UserAgent().random
}
#请求响应
def getResponse(url,headers):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response
        return None
    except:
        return None
# def getSongName()

if __name__ == '__main__':
    songid = '1363948882'
    url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(songid)

    down_url = getResponse(url,headers).url

    response = requests.get(down_url,headers=headers)

    with open('2.mp3','wb') as f:
        f.write(response.content)

