#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 10:23
# @Author  : Xuegod Teacher For
# @File    : 01_bilibili_test.py
# @Software: PyCharm
import  requests
import random
import time


def get_json(url):
    #构造请求头
    headers = {
    'Referer': 'http://vc.bilibili.com/p/eden/rank',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }
    #给服务器发送的信息
    params = {
        'page_size': 10,
        'next_offset': 21,
        'tag': '今日热门',
        'platform': 'pc'
    }
    try:
        #模拟网络请求，请求服务器
        html = requests.get(url,params=params,headers = headers)
        #返回文本利用json（） 方法 强制转换为Python课操作对象
        return html.json()
    except:
        print('很遗憾没哟得到json数据')
def download(url,path):
    size = 0
    headers = {
        'Referer': 'http://vc.bilibili.com/p/eden/rank',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }
    response = requests.get(url,headers = headers,stream = True)
    chunk_size = 1024
    content_size = int(response.headers['content-length'])
    if response.status_code == 200:

        print('这是视频大小为:%.2f MB'%(content_size/chunk_size/1024))

        with open(path,'wb') as file:
            for data in response.iter_content(chunk_size = chunk_size):
                file.write(data)
                size += len(data)#已经下载的问价大
#http://api.vc.bilibili.com/board/v1/ranking/top?

if __name__ == '__main__':
    for i in range(10):
        url = 'http://api.vc.bilibili.com/board/v1/ranking/top?'
        num = i*10+1
        html = get_json(url)
        infos = html['data']['items']

        for info in infos:
            title = info['item']['description']

            print('本次下载的视频标题:',title)

            video_url = info['item']['video_playurl']
            try:
                download(video_url,path='./video/'+'%s.mp4'%title)
                print('视频下载状态:','success!')
            except:
                print('视频下载状态:','bad!')
                pass
            time.sleep(2)
        time.sleep(int(format(random.randint(2,8))))