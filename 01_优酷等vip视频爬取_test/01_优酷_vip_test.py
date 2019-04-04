# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 13:37
# @Author  : for 
# @File    : 01_优酷_vip_test.py
# @Software: PyCharm
#两个链接对比
# http://v.youku.com/v_show/id_XNDA0MDg2NzU0OA==.html?spm=a2h03.8164468.2069780.5
#http://y.mt2t.com/lines?url=https://v.qq.com/x/cover/5a3aweewodeclku/b0024j13g3b.html

import requests,re
import json

class VIP(object):
    def __init__(self):
        self.api = 'http://y.mt2t.com/lines?url='
        self.post_url = "http://y.mt2t.com/lines/getdata"
        self.url = 'http://v.youku.com/v_show/id_XNDA0MDg2NzU0OA==.html?spm=a2h03.8164468.2069780.5'
        # self.url = 'https://v.youku.com/v_show/id_XNDA4OTQ0ODQ4NA==.html?spm=a2ha1.12528442.m_4424_c_11054_7.d_2&s=ae9f929cbce811e0bf93&scm=20140719.rcmd.4424.show_ae9f929cbce811e0bf93'
        self.get_videourl = 'http://y2.mt2t.com:91/ifr/api'
# //dd.tt-hk.cn/temp2/c06271d8970a116e64e18a510bbc873b-OWUyMXE5dG9iTjJqdVNWcmdZakZCR0p4elQ1Ukh2ZGFnMzZPY1J1cjZLaFNacGJWWWo3UW1acnEwajhWMEcrcGN0dnFpZU14VWhoMStlVEUvQW9FNVlUQTVnaUU2VkprQ2pURDVzQlhiOHc=.m3u8
    def run(self):
        res = requests.get(self.api+self.url)
        html = res.text
        key = re.search(r'key:"(.*?)"',html).group(1)
        return key

    def get_playlist(self):
        key = self.run()
        data = {
            'url':self.url,
            'key':key
        }
        html = requests.post(self.post_url,data = data)
        dic =  html.json()
        for item in dic:
            # print('这是url:',item['Url'])
            url_param, type = self.url_spilt(item["Url"])
            res = requests.post(self.get_videourl,data={
                "url":url_param,
                "type":type,
                "from": "mt2t.com",
                "device":"",
                "up":"0"
            })
            play = json.loads(res.text)
            print(play)
    def url_spilt(self,url):
        #url = "http://y2.mt2t.com:91/ifr?url=%2bbvqT10xBsjrQlCXafOom96K2rGhgnQ1CJuc5clt8KDHnjH75Q6BhQ4Vnv7gUk%2bSpJYws4A93QjxcuTflk7RojJt0PiXpBkTAdXtRa6%2bLAY%3d&type=m3u8"
        url_param = url.split("?url=")[1].split("&")[0].replace("%2b","+").replace("%3d","=").replace("%2f","/")
        if "type=" in url:
            type = url.split("type=")[1]
        else:
            type = ""
        return url_param,type
if __name__ == '__main__':
    vip = VIP()
    # vip.run()
    vip.get_playlist()