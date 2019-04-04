#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 17:31
# @Author  : Xuegod Teacher For
# @File    : 03_爬取m3u8视频.py
# @Software: PyCharm
# https://videos5.jsyunbf.com/2019/02/07/iQX7y3p1dleAhIv7/out005.ts
import datetime
import requests
# m3u8是本地的文件路径
def get_ts_urls(m3u8_path,base_url):
    urls = []
    with open(m3u8_path,"r") as file:
        lines = file.readlines()
        for line in lines:
            if line.endswith(".ts\n"):
                urls.append(base_url+line.strip("\n"))
    return urls
def download(ts_urls,download_path):
    for i in range(len(ts_urls)):
        ts_url = ts_urls[i]
        file_name = ts_url.split("/")[-1]
        print("开始下载 %s" %file_name)
        start = datetime.datetime.now().replace(microsecond=0)
        try:
            response = requests.get(ts_url,stream=True,verify=False)
        except Exception as e:
            print("异常请求：%s"%e.args)
            return
        ts_path = download_path+"/{0}.ts".format(i)
        with open(ts_path,"wb+") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        end = datetime.datetime.now().replace(microsecond=0)
        print("耗时：%s"%(end-start))
import threading
if __name__ == '__main__':
    base_url = 'https://videos5.jsyunbf.com/2019/02/07/iQX7y3p1dleAhIv7/'
    urls = get_ts_urls(r'E:\xuegod_code\01_优酷等vip视频爬取_test\playlist.m3u8',base_url)
    download(urls,'./all_ts/')
