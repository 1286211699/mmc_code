#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 22:27
# @Author  : Xuegod Teacher For
# @File    : 08_copy_test.py
# @Software: PyCharm
import time
import requests # pip install requests
from urllib import request #需要这个下载
#url地址
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%94%AF%E7%BE%8E&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%94%AF%E7%BE%8E&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=60&rn=30&gsm=3c&1554171103838='
#模拟请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
}
#向服务器发送的数据
data_str = '''
    tn: resultjson_com
    ipn: rj
    ct: 201326592
    is:
    fp: result
    queryWord: 唯美
    cl: 2
    lm: -1
    ie: utf-8
    oe: utf-8
    adpicid:
    st:
    z:
    ic:
    hd:
    latest:
    copyright:
    word: 唯美
    s:
    se:
    tab:
    width:
    height:
    face:
    istype:
    qc:
    nc: 1
    fr:
    expermode:
    selected_tags:
    pn: 30
    rn: 60
    gsm: 1e
    1545019467831:
    '''
#todo 分析得到图片的所有url
def get_image_url():
    send_data = {}
    for line in data_str.splitlines():#以行进行分割
        line_data = line.split(': ')  #分割
        if len(line_data) == 2:       #判断
            key,value = line_data     #序列解包赋值
            if key and value:
                send_data[key] = value #添加字典
    response = requests.get(url,headers = headers,params=send_data)
    json_data = response.json()['data']
    for src in json_data:
        img_url = src.get('middleURL')
        if img_url:
            down_image(img_url)
#todo 下载图片
def down_image(url):
    name = str(time.time()) + '.png'
    request.urlretrieve(url = url,filename=name)
    print('{} is download'.format(name))
    time.sleep(1)
#调用
get_image_url()