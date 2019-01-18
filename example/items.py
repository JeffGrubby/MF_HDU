# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field



class MeoItem(Item):
    '''
    name = Field()
    description = Field()
    link = Field()
    crawled = Field()
    spider = Field()
    url = Field()
    '''
    title = Field()
    link = Field()
    more_info = Field()
    crawled = Field()


