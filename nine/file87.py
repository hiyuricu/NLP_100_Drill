#!/usr/bin/python
#coding:utf-8
import sys,json
from pymongo import Connection

con = Connection('localhost', 27017) #コネクション作成
db = con.nlp100_tachibana #コネクションからnlp100_tachibanaデータベースを取得
col = db.tweets #nlp100_tachibanaデータベースからtweetsコレクションを取得

for dic in col.find({"$query":{"user":"170626372"}, "$orderby":{"freq_rted":1}}).limit(10):
    for k,v in dic.items():
        print k,v
