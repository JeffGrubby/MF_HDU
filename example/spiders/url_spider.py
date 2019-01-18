from urllib.parse import urlparse

import jieba.posseg as pseg
import nltk
from nltk import clean_html
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup as bs
from readability.readability import Document
# from example.items import ExampleItem

TEACHER_TAGS = ['硕导','博导','硕士生导师','博士生导师','导师风采','导师简介','教师风采']

class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'URL'
    # allowed_domains = ['hdu.edu.cn']
    start_urls = ['http://www.hdu.edu.cn/']

    # rules = [
    #     Rule(LinkExtractor(
    #         restrict_xpaths=('//ul//li')
    #     ), callback='parse_url', follow=True),
    # ]

    def parse(self, response):
        items = []
        # 学院导航
        collageUrls = response.xpath('//div[@id="item1"]/a/@href').extract()
        collageTitles = response.xpath('//div[@id="item1"]/a/text()').extract()

        # 部门网站
        departUrls = response.xpath('//div[@id="item2"]/a/@href').extract()
        departTitles = response.xpath('//div[@id="item2"]/a/text()').extract()

        for i in range(0, len(collageUrls)):
            item = ExampleItem()
            if collageTitles[i].strip().endswith('学院'):
                item['name'] = collageTitles[i]
                item['link'] = collageUrls[i]
                items.append(item)

        for item in items:
            # print(item['link'])
            yield scrapy.Request(url=item['link'],
                                 callback=self.second_parse)

    def has_title_and_href(self,tag):
        return tag.has_attr('title') and tag.has_attr('href')

    def second_parse(self, response):
        items = []
        soup = bs(response.body, 'lxml')
        contents = soup.find_all(self.has_title_and_href)
        for i in contents:
            item = ExampleItem()
            for _ in TEACHER_TAGS:
                if _ in i['title']:
                    item['link'] = response.url+'/'+i['href']
                    items.append(item)
                    continue

        for item in items:
            yield scrapy.Request(url=item['link'], callback=self.third_parse)

    def third_parse(self, response):
        items = []
        soup = bs(response.body, 'lxml')
        contents = soup.find_all(self.has_title_and_href)

        for i in contents:
            item = ExampleItem()
            if len(i['title'].strip()) < 4:
                segs = pseg.cut(i['title'].strip())
                for s in segs:
                    if s.flag == 'nr':
                        item['name'] = i['title'].strip()
                        item['link'] = 'http://'+urlparse(response.url).netloc + '/' + i['href']
                        items.append(item)
                        continue
        for item in items:
            # print(item['link'])
            yield scrapy.Request(url=item['link'],
                                 callback=self.content_parse)
    def content_parse(self,response):
        item = {}

        item['link'] = response.url
        readable_title = Document(response.body).short_title()
        # print(readable_title)
        item['name'] = readable_title

        readable_article = Document(response.body).summary()
        # print(readable_article)
        item['more_info'] = bs(readable_article).get_text()

        yield item
