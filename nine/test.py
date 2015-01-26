#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import Connection

#コネクション作成
con = Connection('192.168.1.245', 27017)

#コネクションからtestデータベースを取得
db = con.test

# 以下のように記載することも可能
# db = con['test']

#testデータベースからfooコレクションを取得
col = db.foo

# 以下のように記載することも可能
# col = db['foo']

print "========find_one========"
print col.find_one()

print "========find========"
for data in col.find():
    print data

print "========find_query========"
for data in col.find({u'a':10}):
    print data
