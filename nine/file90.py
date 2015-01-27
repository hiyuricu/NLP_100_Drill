#!/usr/bin/python
#coding:utf-8
import sys,json,pymongo
from pymongo import *

query = unicode(sys.argv[1], "utf-8")

con = Connection('localhost', 27017) #コネクション作成
db = con.nlp100_tachibana #コネクションからnlp100_tachibanaデータベースを取得
col = db.tweets #nlp100_tachibanaデータベースからtweetsコレクションを取得

for data in col.find():
    if query in data["body"]:
        print "%s :\n%s" % (data["nickname"], data["body"])