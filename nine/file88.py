#!/usr/bin/python
#coding:utf-8
import sys,json,pymongo
from pymongo import *

con = Connection('localhost', 27017) #コネクション作成
db = con.nlp100_tachibana #コネクションからnlp100_tachibanaデータベースを取得
col = db.tweets #nlp100_tachibanaデータベースからtweetsコレクションを取得

for data in col.find():
    pre_char = "<s>"
    bigrams = list()
    for char in data["body"]:
        bigrams.append(pre_char+char)
        pre_char = char
    bigrams.append(pre_char+"</s>")
    data["bigram"] = bigrams
    col.save(data)
col.create_index([("bigram", ASCENDING)])