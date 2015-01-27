#!/usr/bin/python
#coding:utf-8
import sys,json
from pymongo import Connection

con = Connection('localhost', 27017) #コネクション作成
db = con.nlp100_tachibana #コネクションからnlp100_tachibanaデータベースを取得
col = db.tweets #nlp100_tachibanaデータベースからtweetsコレクションを取得

for obj in col.find({"url" : "http://twitter.com/monagn_IIDX/status/485830078496927744"}):
    print obj