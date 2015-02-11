#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from lxml import etree

html = open(sys.argv[1])
root = etree.parse(html)

for item in root.xpath('//sentence[@id= "1"]/dependencies[@type= "basic-dependencies"]/dep/governor[@idx= "4"]'):
	for d in item.getparent().iter('dependent'):
		print d.text

