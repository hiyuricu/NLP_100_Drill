#!/usr/bin/python
#-*-coding:utf-8-*-
#(98) 現在時刻を表示するCGIを，自分のウェブサイト上で公開せよ．
#http://cl.sd.tmu.ac.jp/~ryu/file98.cgi

#このcgiをpublic_html以下におけば良い。またこのfile98.cgiとpublic_htmlのパーミッションを
#「755(rwxr-xr-x)」にしておく必要がある。

from datetime import datetime

print "Content-Type: text/html; charset=utf-8"
print
print "<h1>"
print datetime.now()
print "<h1>"