#!/usr/bin/python
#coding:utf-8
import sys,json
from pymongo import Connection

#第一引数はtweets100.tsv?
tweet_data = json.load(open(sys.argv[1])) # jsonの取得。tweet_dataは辞書が要素のリスト

con = Connection('localhost', 27017) #コネクション作成
db = con.nlp100_tachibana #コネクションからnlp100_tachibanaデータベースを取得
col = db.tweets #nlp100_tachibanaデータベースからtweetsコレクションを取得

for one_tw in tweet_data: # one_twは辞書っぽい
    tw = {}
    tw["url"] = "http://twitter.com/%s/status/%s" % (one_tw["user"]["screen_name"], one_tw["id_str"])
    tw["date"] = one_tw["created_at"]
    tw["user"] = one_tw["user"]["id_str"]
    tw["nickname"] = one_tw["user"]["name"]
    tw["body"] = one_tw["text"]
    tw["rt_url"] = None
    if "retweeted_status" in one_tw:
        tw["rt_url"] = "http://twitter.com/"+one_tw["retweeted_status"]["user"]["screen_name"]+"/status/"+one_tw["retweeted_status"]["id_str"]
    tw["reply_url"] = None
    if one_tw["in_reply_to_screen_name"] is not None:
        tw["reply_url"] = "http://twitter.com/"+one_tw["in_reply_to_screen_name"]+"/status/"+one_tw["in_reply_to_status_id_str"]
    tw["freq_rted"] = one_tw["retweet_count"]

    col.insert(tw)