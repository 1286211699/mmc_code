# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    volume = scrapy.Field()
    downloads = scrapy.Field()
    follow = scrapy.Field()
    comment = scrapy.Field()
    tags = scrapy.Field()
    rank_num = scrapy.Field()
    rank_num_users = scrapy.Field()
    update_time = scrapy.Field()
    rom = scrapy.Field()
    developer = scrapy.Field()
    _id = scrapy.Field()

