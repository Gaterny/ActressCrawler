# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ActressItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 演员姓名
    name = scrapy.Field()
    # 演员作品名
    film = scrapy.Field()
    # 作品番号
    tag = scrapy.Field()
    # 作品时间
    date = scrapy.Field()

    # 年龄
    # age = scrapy.Field()
    # height = scrapy.Field()
    # # 腰围
    # waist = scrapy.Field()
    # # 罩杯
    # cup = scrapy.Field()
    # # 生日
    # birth = scrapy.Field()
    # # 胸围
    # bust = scrapy.Field()
    # # 臀围
    # hips = scrapy.Field()

