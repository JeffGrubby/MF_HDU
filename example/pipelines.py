# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from datetime import datetime

import pymongo


# class ExamplePipeline(object):
#     def process_item(self, item, spider):
#         item["crawled"] = datetime.utcnow()
#         item["spider"] = spider.name
#         return item
from scrapy.exceptions import DropItem

from example import settings


class MeoPipeline(object):
    def __init__(self):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        dbName = settings.MONGODB_DBNAME
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]
        self.post = tdb[settings.MONGODB_DOCNAME]
        self.meo_set = set()

    def process_item(self, item, spider):
        link = item['link']
        if link in self.meo_set:
            raise DropItem("Duplicate book found:%s" % item)
        self.meo_set.add(link)

        MeoInfo = dict(item)
        self.post.insert(MeoInfo)
        return item