#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Leaf
# @Date  : 2018/11/10 9:54
# @Desc  :
import re

text = '''
    徐荣华
    '''
# import nltk
# # nltk.download()
# tokens = nltk.word_tokenize(text)  #分词
# tagged = nltk.pos_tag(tokens)  #词性标注
# entities = nltk.chunk.ne_chunk(tagged)  #命名实体识别
# a1=str(entities) #将文件转换为字符串
# print(entities)

# import jieba.posseg as pseg
# segs = pseg.cut(text.strip())
# for i in segs:
#     if i.flag == 'nr':
#         print(i.word,i.flag)


str = '使用VOCALOID的歌曲'
res = re.match(u'^[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ffa-zA-Z]+$', str)
print(res)