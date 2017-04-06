# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem

class OlxPipeline(object):

    def open_spider(self, spider):
        self.dao = RealEstateDAO()
        self.ids = []

    def close_spider(self, spider):
        self.dao.update_timeframe(self.ids)
        self.dao.close()

    def process_item(self, item, spider):
        self.ids.append(item['estate_id'])
        self.dao.insert(item['estate_id'], item['url'], item['price'], item['ad_text'], item['info'])
