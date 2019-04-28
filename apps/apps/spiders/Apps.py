# -*- coding: utf-8 -*-
import scrapy
from fake_useragent import UserAgent

from apps.items import AppsItem
import re
ua = UserAgent()

class AppsSpider(scrapy.Spider):
    name = 'Apps'
    allowed_domains = ['www.coolapk.com']
    start_urls = ['http://www.coolapk.com/apk?p=1']
    #settings 目的是为了修改默认的setting中的文件中的配置
    custom_settings ={
        "DEFAULT_REQUEST_HEADERS" :{
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        }
    }
    def parse(self, response):
        list_items = response.css('.app_left_list>a')
        for item in list_items:
            url = item.css('::attr("href")').extract_first()
            url = response.urljoin(url)
            yield scrapy.Request(url,callback=self.parse_url)
        next_page = response.css('.pagination li:nth-child(8) a::attr(href)').extract_first()
        url = response.urljoin(next_page)
        yield scrapy.Request(url, callback=self.parse)
    def getinfo(self,response):
        info = response.css(".apk_topba_message::text").re("\s+(.*?)\s+/\s+(.*?)下载\s+/\s+(.*?)人关注\s+/\s+(.*?)个评论.*?")
        return info
    def gettags(self,response):
        tags = response.css(".apk_left_span2")
        tags = [item.css('::text').extract_first() for item in tags]
        return tags
    def getappinfo(self,response):
        #app_info = response.css(".apk_left_title_info::text").re("[\s\S]+更新时间：(.*?)")
        body_text = response.body_as_unicode()
        update = re.findall(r"更新时间：(.*)?[<]",body_text)[0]
        rom =  re.findall(r"支持ROM：(.*)?[<]",body_text)[0]
        developer = re.findall(r"开发者名称：(.*)?[<]", body_text)[0]
        return update,rom,developer
    def parse_url(self,response):
        item = AppsItem()
        item["title"] = response.css(".detail_app_title::text").extract_first()
        info = self.getinfo(response)
        item['volume'] = info[0]
        item['downloads'] = info[1]
        item['follow'] = info[2]
        item['comment'] = info[3]
        item["tags"] = self.gettags(response)
        item['rank_num'] = response.css('.rank_num::text').extract_first()
        item['rank_num_users'] = response.css('.apk_rank_p1::text').re("共(.*?)个评分")[0]
        item["update_time"],item["rom"],item["developer"] = self.getappinfo(response)
        print(item)
        yield item



