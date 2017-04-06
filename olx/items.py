# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class OlxRealEstate(scrapy.Item):
    estate_id = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    ad_text = scrapy.Field()
    info = scrapy.Field()
