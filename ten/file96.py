#!/usr/bin/python
#-*-coding:utf-8-*-

import xml.sax, xml.sax.handler, sys, re
from xml.sax.handler import ContentHandler

r = re.compile("\[\[(Category:.*)\]\]$")

class printNameHandler(ContentHandler):
    def __init__(self):
        self.flag  = False
        self.flag2 = False
        self.title_name = ""
        self.long_text = ""

    def startElement(self, name, attrs):
        if name == "title":
            self.flag = True

        if name == "text":
            self.flag2 = True

    def endElement(self, name):
        if name == "title":
            self.flag = False

        if name == "text":
            self.flag2 = False

    def characters(self, data):
        if self.flag:
            self.title_name = data

        if self.flag2:
            m = r.search(data)
            if m:
               print self.title_name,"  ",m.group(1) #finditerする必要がある?

def main(text):
    parser = xml.sax.make_parser()
    parser.setContentHandler(printNameHandler())
    print parser.parse(text)

if __name__=="__main__":
    main(sys.argv[1])
