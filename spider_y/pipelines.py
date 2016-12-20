# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import pymongo

class SpiderYPipeline(object):

    def process_item(self, item, spider):
        book_detail = {
            'img': item.get('img'),
            'name': item.get('name', []),

        }
        print 'through'
        return item
    def open_spider(self, spider):
        # self.file = open('items.jl', 'wb')
        pass
    def close_spider(self, spider):
        # self.file.close()
        pass
    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        return item


##TODO 用mongodb 储存照片信息
# class MongoPipeline(object):
#
#     collection_name = 'scrapy_items'
#
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
#         )
#
#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#
#     def close_spider(self, spider):
#         self.client.close()
#
#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert(dict(item))
#         return item