# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    username = scrapy.Field()
    sex = scrapy.Field()
    answers = scrapy.Field()
    asks = scrapy.Field()
    posts = scrapy.Field()
    columns = scrapy.Field()
    pins = scrapy.Field()
    follwering = scrapy.Field()
    follwers = scrapy.Field()
