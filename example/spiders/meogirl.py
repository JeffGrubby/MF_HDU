#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Leaf
# @Date  : 2018/12/7 14:51
# @Desc  :
import json
import re
import requests
from collections import defaultdict

import scrapy
from goose3 import Goose
from html2text import html2text
from readability import Document

from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup as bs

from example.items import MeoItem


class MeoSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'Meo'
    # url = 'https://zh.moegirl.org/Special:%E9%9A%8F%E6%9C%BA%E9%A1%B5%E9%9D%A2'
    # start_urls = [url]
    start_urls = ['https://zh.moegirl.org/%E8%A8%80%E5%92%8C%E6%98%93%E5%86%B7#']
    offset = 0

    def parse(self, response):

        res = response.body.decode('utf8')
        soup = bs(res, 'lxml')
        title = soup.title.get_text().split('-')[0]
        print('title:', title)

        '''
        TODO get short titles
        '''
        tiny_title = soup.select('div[id="mw-content-text"]  h2')
        tiny_titles = [i.get_text() for i in tiny_title]
        print('tiny_titles:', tiny_titles)

        '''
        TODO get real shortened contexts
        '''
        result = {}
        for tt in tiny_title:
            contexts = []
            tmp = tt.find_next_sibling()
            while tmp and tmp.name != 'h2':
                # 获取关联组
                if tmp.has_attr('class') and tmp['class'][0] == 'navbox':
                    relations = tmp.get_text()
                    print('relations:', relations)

                context = tmp.get_text().strip('').strip('\r\n').replace(u'\u3000', u' ').replace(u'\xa0', u' ').replace('\n', ' ')
                # print('context:', context)

                # if context.startswith(u'查'):

                if not context.endswith(r');') and 'window' not in tmp.get_text():
                    # print('context:', context)
                    contexts.append(context)
                tmp = tmp.find_next_sibling()

            result[tt.get_text()] = ' '.join(contexts)

        print('result:', result)

        # item = MeoItem()
        # item['title'] = title
        # item['link'] = response.url
        # item['more_info'] = result
        # yield item

        # yield scrapy.Request(self.url, callback=self.parse, dont_filter=True)
        # if self.offset < 1000:
        #     self.offset += 1
        #     yield scrapy.Request(self.url, callback=self.parse, dont_filter=True)


    def test_parse(self,response):
        # res = response.body.decode('utf8')
        # soup = bs(res, 'lxml')
        # title = soup.title.get_text().split('-')[0]
        # print('title:', title)

        # content = soup.select('div[id="mw-content-text"]')[0].get_text()
        # print(content)

        # with Goose() as g:
        #     content = g.extract(raw_html=response.body)
        #     print(content.infos)

        # readable_article = Document(res).summary()
        # # print(readable_article)
        # parsed_article = bs(readable_article, 'lxml').get_text()
        # print(parsed_article.split())

        '''
        TODO get whole context
        '''
        # h = html2text(content)
        # itemList = h.split()
        #
        # assert False
        # results = []
        # for item in itemList:
        #     res = re.match(u'^[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ff]+$', item)
        #     if res and len(res.group()) > 1:
        #         results.append(res.group())
        # print('results:', results)




