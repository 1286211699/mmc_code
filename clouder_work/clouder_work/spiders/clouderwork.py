# -*- coding: utf-8 -*-
import scrapy
import json
import time

class ClouderworkSpider(scrapy.Spider):
    name = 'clouderwork'
    allowed_domains = ['www.clouderwork.com']
    start_urls = ['https://www.clouderwork.com/api/v2/jobs/search?ts={times}&keyword=&budget_range=&work_status=&pagesize={pagesize}&pagenum={pagenum}']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS" :{
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'Host':'www.clouderwork.com',
            'Referer':'https://www.clouderwork.com/jobs?keyword=',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        }
    }
    def start_requests(self):
        for page in range(1,353):
            yield scrapy.Request(self.start_urls[0].format(times=time.time(),pagesize=20,pagenum=page))
    def parse(self, response):
        json_data = json.loads(response.text)
        for item in json_data['jobs']:
            return item
