#!/usr/bin/python
#coding:utf-8
import sys,json
from pymongo import *

con = Connection('localhost', 27017) #コネクション作成
db = con.nlp100_tachibana #コネクションからnlp100_tachibanaデータベースを取得
col = db.tweets #nlp100_tachibanaデータベースからtweetsコレクションを取得

for dic in col.find({"user" : "170626372"}).sort('freq_rted', pymongo.ASCENDING):
    for k,v in dic.items():
        print k,v
