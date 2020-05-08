#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 22:18
# @Author  : Xuegod Teacher For
# @File    : 03_baidu_class_test.py
# @Software: PyCharm
import time
import requests # pip install requests
from urllib import request #需要这个下载

class BauduImage(object):
    #url地址
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E7%BE%8E%E5%A5%B3&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=girl&pn=120&rn=30&gsm=78&1586269429211='
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
        queryWord: 美女
        cl: 2
        lm: -1
        ie: utf-8
        oe: utf-8
        adpicid: 
        st: -1
        z: 
        ic: 0
        hd: 
        latest: 
        copyright: 
        word: 美女
        s: 
        se: 
        tab: 
        width: 
        height: 
        face: 0
        istype: 2
        qc: 
        nc: 1
        fr: 
        expermode: 
        force: 
        cg: girl
        pn: 120
        rn: 30
        gsm: 78
        '''
    #todo 分析得到图片的所有url
    def get_image_url(self):
        send_data = {}
        for line in self.data_str.splitlines():#以行进行分割
            line_data = line.split(': ')  #分割
            if len(line_data) == 2:       #判断
                key,value = line_data     #序列解包赋值
                if key and value:
                    send_data[key] = value #添加字典
        response = requests.get(self.url,headers = self.headers,params=send_data)
        json_data = response.json()['data']
        for src in json_data:
            img_url = src.get('middleURL')
            if img_url:
                self.down_image(img_url)#注意：在内部调用外部的函数
    #todo 下载图片
    def down_image(self,url):
        name = str(time.time()) + '.png'
        request.urlretrieve(url = url,filename=name)
        print('{} is download'.format(name))
        time.sleep(1)
    # #调用
    # get_image_url()
if __name__ == '__main__':
    b = BauduImage()
    b.get_image_url()